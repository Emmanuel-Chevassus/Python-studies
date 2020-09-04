

import numpy as np

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import animation

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


T = 20.0 # t
X = 10.0 # x

n = 300
m = 300

h = T / (n - 1)
k = X / (m - 1)

C = 0.5

U = np.zeros((n, m))

# Set the initial values
for i in range(0, n):
    U[i, 0] = np.exp(- (i * k - 0.2) ** 2)

for j in range(1, m):
    for i in range(1, n):
        U[i, j] = (k * U[i, j - 1] + C * h * U[i - 1, j]) / (k + C * h)

tn = np.zeros((m, 1))
for j in range(0, m):
    tn[j] = j * h

xn = np.zeros((n, 1))

for j in range(0, n):
    xn[j] = j * k

fig = plt.figure(1)

for i in [0, 20, 40, 60, 80, 100]:
    subfig = fig.add_subplot(1, 1, 1)
    label = 't = ' + str(tn[i][0])
    subfig.plot(xn, U[:, i], label=label)
    subfig.legend()
    subfig.grid(True)

# Save Image
plt.xlabel('x: position')
plt.ylabel('u: u(x, t)')
plt.title(r'$\frac{\partial u}{\partial t} + C \frac{\partial u}{\partial x} = 0$')

plt.savefig('transport-equation')

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-1, 1))
ax.grid()

line, = ax.plot([], [], lw=2)

time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def init():
    global time_text

    line.set_data([], [])
    time_text.set_text('')
    return line,

def animate(i):
    global U
    global xn
    global tn

    time_text.set_text('time = %.1f' % tn[i])
    line.set_data(xn, U[:, i])

    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
anim.save('transport-equation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])