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

#DPR GIS shapefiles use the NAD83 datum (GRS80 ellisoid) and the California (Teale) Albers projection (translation from ellipsoid to map) 
# spatial reference system identifier (SRID) = 3310
# This North American Datum remains constant over time for points on the North American plate.
# http://wiki.spatialmanager.com/index.php/Coordinate_Systems_objects_list

# maps already on our DB use the World Geodetic System (WGS84), which uses the wgs84 ellipsoid, which is slightly more accurate than GRS80.
# This datum gets updated periodically as the earths plates move using stations throughout the world.
# spatial reference system identifier (SRID) = 4326

