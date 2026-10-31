import geopandas as gpd
import pandas as pd

file = r'C:\Users\rumca\Documents\Optymalna sieć szkół_miasto_gmina_Chojnice\data\assigned buildings.gpkg'
layer_name = 'assigned buildings'

df = gpd.read_file(file, layer=layer_name)

# 'total_cost' may contain non-numeric data — 'coerce' turns invalid entries into NaN without stopping the program
df['total_cost'] = pd.to_numeric(df['total_cost'], errors='coerce')

#delete NULL lines
df = df.dropna(subset=['total_cost'])

if len(df) == 0:
    print("Error: The 'total_cost' column does not contain any valid numeric values. All values are NULL.")
else:
    df_filtered = df.loc[df.groupby('origin_id')['total_cost'].idxmin()].reset_index(drop=True)

    output_path = r'C:\Users\rumca\Documents\Optymalna sieć szkół_miasto_gmina_Chojnice\data\shortest_route.csv'

    # If you want to keep text/numeric columns without geometry in the CSV:
    if isinstance(df_filtered, gpd.GeoDataFrame):
        df_filtered.drop(columns='geometry', errors='ignore').to_csv(output_path, index=False)
    else:
        df_filtered.to_csv(output_path, index=False)

    print(f"Done! The file with the lowest costs has been saved as: {output_path}")
    print(df_filtered.head())
