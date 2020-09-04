# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:25:57 2019

@author: Emmanuel
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:06:26 2019

@author: Emmanuel
"""
from datetime import datetime,timedelta
from siphon.catalog import TDSCatalog
from siphon.radarserver import RadarServer
import cartopy
import matplotlib.pyplot as plt
import numpy as np
from siphon.cdmr import Dataset

cat=TDSCatalog('http://thredds.ucar.edu/thredds/radarServer/catalog.xml')
rs=RadarServer(cat.catalog_refs['NEXRAD Level III Radar from IDD'].href)

query=rs.query()
now=datetime.utcnow()
query.stations('FTG').time_range(now - timedelta(hours=1),now).variables('N0Q')
query_cat=rs.get_catalog(query) 


list(cat.catalog_refs)

#pour utiliser n'importe quelle partie du catalogue d'UCAR
cat.catalog_refs['NEXRAD Level III Radar from IDD'].href

rs=RadarServer(cat.catalog_refs['NEXRAD Level III Radar from IDD'].href)

data=query_cat.datasets[0].remote_access()
print(list(data.variables))

field_name= 'BaseReflectivityDR'
range_data=data.variables['gate'][:]
azimuth_data=data.variables['azimuth'][:]
radar_data=data.variables[field_name][:]

x=range_data*np.sin(np.deg2rad(azimuth_data))[:,None]
y=range_data*np.cos(np.deg2rad(azimuth_data))[:,None]

radar_data=np.ma.array(radar_data,mask=np.isnan(radar_data))

proj=cartopy.crs.LambertConformal(central_longitude=data.RadarLongitude,central_latitude=data.RadarLatitude)

print(data.time_coverage_start)
data_time=datetime.strptime(data.time_coverage_start, '%Y-%m-%dT%H:%M:%SZ') #string parse time
print(data_time)
from metpy.plots import ctables, add_timestamp

state_borders=cartopy.feature.NaturalEarthFeature(category='cultural',name='admin_1_states_provinces_lakes',scale='50m',facecolor='none')

fig=plt.figure(figsize=(10,10))
ax=plt.subplot(1,1,1,projection=proj)
#cmap couleur carte
norm,cmap=ctable=ctables.registry.get_with_steps('NWSReflectivity',16,16)
mesh=ax.pcolormesh(x,y,radar_data,norm=norm,cmap=cmap,zorder=0)
add_timestamp(ax,time=data_time) 
ax.add_feature(state_borders,edgecolor='black',linewidth=2,zorder=2)

distance_in_degrees=1.8
#ax.set_extent([data.RadarLongitude-distance_in_degrees,data.RadarLongtitude+distance_in_degrees,data.RadarLatitude-distance_in_degrees,data.RadarLatitude+distance_in_degrees])
#pour dézoomer
#carte Colorado
