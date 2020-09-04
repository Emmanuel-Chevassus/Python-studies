# -*- coding: utf-8 -*-


from datetime import datetime,timedelta
import cartopy
import matplotlib.pyplot as plt
import numpy as np
from siphon.cdmr import Dataset
from metpy.plots import ctables, add_timestamp
from siphon.catalog import TDSCatalog
from siphon.radarserver import RadarServer

cat=TDSCatalog('http://thredds.ucar.edu/thredds/radarServer/catalog.xml')
rs=RadarServer(cat.catalog_refs['NEXRAD Level III Radar from IDD'].href)

query=rs.query()
now=datetime.utcnow()
query.stations('NQA').time_range(now - timedelta(hours=1),now).variables('N0Q')
query_cat=rs.get_catalog(query) 

print(sorted(query_cat.datasets))

def plot_radar(data,field_name):
    rng=data.variables['gate'][:]
    az=data.variables['azimuth'][:]
    ref=data.variables[field_name][:]
    
    distance_in_degrees=3
    ax.set_extent([data.RadarLongitude-distance_in_degrees,data.RadarLongitude+distance_in_degrees,data.RadarLatitude-distance_in_degrees,data.RadarLatitude+distance_in_degrees])
    x=rng*np.sin(np.deg2rad(az))[:,None]
    y=rng*np.cos(np.deg2rad(az))[:,None]

    norm,cmap=ctables.registry.get_with_range('NWSReflectivity',-30,-100) 
    mesh=ax.pcolormesh(x,y,ref,cmap=cmap,norm=norm,zorder=0)
    return mesh

field_name='BaseReflectivityDR'

base_file=query_cat.datasets[0].remote_access()

proj=cartopy.crs.LambertConformal(central_longitude=base_file.RadarLongitude,central_latitude=base_file.RadarLatitude)

state_borders=cartopy.feature.NaturalEarthFeature(category='cultural',name='admin_1_states_provinces_lakes',scale='50m',facecolor='none')

fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(1,1,1,projection=proj)

artists=[]

ax.add_feature(state_borders,edgecolor='black',linewidth=2,zorder=2)

for ds_name in sorted(query_cat.datasets):
    ds=query_cat.datasets[ds_name]
    data=Dataset(ds.access_urls['CdmRemote'])
    
    field_name=[var.name for var in data.variables.values()
         if var.ndim>=2 and not var.name.endswith('RAW')][0]
    
    text=ax.text(0.5,1.02,data.time_coverage_start,ha='center',transform=ax.transAxes)
    
    mesh=plot_radar(data,field_name)
    
    artists.append([text,mesh])

plt.rcParams['animation.html']='jshtml'
from matplotlib.animation import ArtistAnimation

anim=ArtistAnimation(fig,artists,interval=100)

anim