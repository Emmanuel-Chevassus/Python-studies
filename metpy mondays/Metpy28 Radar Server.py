# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:06:26 2019

@author: Emmanuel
"""

from siphon.catalog import TDSCatalog
from siphon.radarserver import RadarServer

cat=TDSCatalog('http://thredds.ucar.edu/thredds/radarServer/catalog.xml')
list(cat.catalog_refs)

#pour utiliser n'importe quelle partie du catalogue d'UCAR
cat.catalog_refs['NEXRAD Level III Radar from IDD'].href

rs=RadarServer(cat.catalog_refs['NEXRAD Level III Radar from IDD'].href)
from datetime import datetime,timedelta

query=rs.query()
now=datetime.utcnow()
query.stations('FTG').time_range(now - timedelta(hours=1),now).variables('N0Q')

#https://www.ncdc.noaa.gov/data-access/radar-data/nexrad-products
query_cat=rs.get_catalog(query) 
sorted(query_cat.datasets)

query.stations('FTG').time_range(now - timedelta(hours=1),now).variables('N0Q','NOC')

query.stations('FTG','INX').time_range(now - timedelta(hours=1),now).variables('N0Q','NOC')

##########################################
product_codes=['N0Q','N0C','N0H']
query_catalogs=[]
for product_code in product_codes:
    query.stations('FTG').time_range(now - timedelta(hours=1),now).variables('product_code')
    query_cat=rs.get_catalog(query)
    query_catalogs.append(query_cat)
query_catalogs
##########################################
product_codes=['N0Q','N0C','N0H']
query_catalogs=dict()
for product_code in product_codes:
    query.stations('FTG').time_range(now - timedelta(hours=1),now).variables('product_code')
    query_cat=rs.get_catalog(query)
    query_catalogs[product_code]=query_cat
query_catalogs

sorted(query_catalogs['N0C'].datasets)

