"""The script causes the kernel to die in certain environments,
and I cannot figure out why it happens.
"""
import geopandas as gpd
import pandas as pd
import time


# gpd_engine="pyogrio"
# gpd_engine="fiona"
gpd_engine=None

print("Write a DataFrame")
pd.DataFrame({"A": [1, 2]}).to_excel("test.xlsx",
                                     engine='openpyxl',
                                     # engine='xlsxwriter',
                                     )
print("OK")

print("Read a DataFrame")
pd.read_excel("test.xlsx")
print("OK")


df = pd.DataFrame({'col1': ['name1', 'name2'],
                   'wkt': ['POINT (1 2)', 'POINT (2 1)']})
gs = gpd.GeoSeries.from_wkt(df['wkt'])
gdf = gpd.GeoDataFrame(df, geometry=gs, crs="EPSG:4326")

print("Write a GeoDataFrame")
geofile = "geopandas-test.gpkg"  # This causes the kernel error later
# geofile = "geopandas-test.geojson"  # This is always fine
gdf.to_file(geofile, engine=gpd_engine)
print("OK")

print("Read a GeoDataFrame")
gpd.read_file(geofile, engine=gpd_engine)
print("OK")

print("Write a DataFrame")
time.sleep(1)  # Without sleep, the previous print() gets lost sometimes

# Kernel death happens here sometimes

pd.DataFrame({"A": [1, 2]}).to_excel("test.xlsx",
                                     # engine='openpyxl',
                                     # engine='xlsxwriter',
                                     )
print("OK")

print("Read a DataFrame")
time.sleep(1)  # Without sleep, the previous print() gets lost sometimes
# Kernel death happens here sometimes
pd.read_excel("test.xlsx")
print("OK")

print("Test finished successfully")
