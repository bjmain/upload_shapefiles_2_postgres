import glob
import os
import config # this config.py needs to be updated with your info

# run this script from within the directory containing your county-specific .shp files

#Each county has unique shapefiles: https://www.cdpr.ca.gov/docs/emon/grndwtr/gis_shapefiles.htm
files = glob.glob("*shp")

for f in files:
    county = f.strip().split("_")[1]
    table_name = "bmain.township_"+county
    os.system("shp2pgsql -s 3310:4326 -I %s %s | PGPASSWORD=%s psql -U %s -h %s -p 5432 %s " % (f,table_name, config.password, config.user, config.host, config.dbname))
    

 

#Additional Notes: 

#DPR GIS shapefiles: http://wiki.spatialmanager.com/index.php/Coordinate_Systems_objects_list
### EPSG:3310 - NAD83 / California Albers [NAD83 / California (Teale) Albers / NAD83 / CA Albers / NAD_1983_California_Teale_Albers]

#Gateway stuff
###EPSG:4326 - WGS 84 [GCS_WGS_1984]
