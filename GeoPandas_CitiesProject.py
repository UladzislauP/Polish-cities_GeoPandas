import geopandas as gpd
import matplotlib.pyplot as plt

shapefile_path = 'polska.shp'
gdf = gpd.read_file(shapefile_path)
print(gdf.crs)

if gdf.crs != "EPSG:4326":
    gdf = gdf.to_crs("EPSG:4326")

cities = {
    'Warszawa': (21.0122, 52.2297),
    'Kraków': (19.9445, 50.0647),
    'Wrocław': (17.0385, 51.1079),
    'Gdańsk': (18.6466, 54.3520)
}

cities_gdf = gpd.GeoDataFrame(
    cities.keys(),
    geometry=gpd.points_from_xy([c[0] for c in cities.values()], [c[1] for c in cities.values()]),
    crs="EPSG:4326"
)

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
gdf.plot(ax=ax, color='lightgrey', edgecolor='black')
cities_gdf.plot(ax=ax, color='red', markersize=50)

for city, coords in cities.items():
    plt.text(coords[0], coords[1], city, fontsize=12, ha='right')

plt.title('Mapa Województw z Wybranymi Miastami')
plt.show()