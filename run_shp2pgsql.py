import glob
import os
import config # this config.py needs to be updated with your info

# run this script from within the directory containing your .shp files
files = glob.glob("*shp")

for f in files:
    county = f.strip().split("_")[1]
    table_name = "bmain.township_"+county
    os.system("shp2pgsql -s 3310 -I %s %s | PGPASSWORD=%s psql -U %s -h %s -p 5432 %s " % (f,table_name, config.password, config.user, config.host, config.dbname))
