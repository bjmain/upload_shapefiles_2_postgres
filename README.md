# upload_shapefiles_2_postgres
#### Additional Notes: 

#### DPR GIS shapefiles use the: 
* NAD83 datum (GRS80 ellisoid) and 
* the California (Teale) Albers projection (translation from ellipsoid to map) 
* SRID = 3310        (spatial reference system identifier)
##### This North American Datum remains constant over time for points on the North American plate.
##### http://wiki.spatialmanager.com/index.php/Coordinate_Systems_objects_list

##### maps already on our DB use: 
* the World Geodetic System (WGS84) 
* wgs84 ellipsoid, which is slightly more accurate than GRS80.
* SRID = 4326       
##### This datum gets updated periodically as the earths plates move using stations throughout the world.
