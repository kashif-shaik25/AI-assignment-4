import geopandas as geo_pd
import matplotlib.pyplot as plot_plt
import fiona
import random

fiona.drvsupport.supported_drivers['KML'] = 'rw'

source_file = "telangana.kml"
spatial_df = geo_pd.read_file(source_file, driver='KML')
label_key = "District" if "District" in spatial_df.columns else "Name"

neighbor_map = {}
for i, entry in spatial_df.iterrows():
    border_contacts = spatial_df[spatial_df.geometry.touches(entry.geometry)][label_key].tolist()
    neighbor_map[entry[label_key]] = border_contacts

area_names = list(neighbor_map.keys())
palette = ["red", "green", "blue", "yellow"]

def verify_placement(loc, tone, current_set, relations):
    for peer in relations.get(loc, []):
        if peer in current_set and current_set[peer] == tone:
            return False
    return True

def run_backtracking(history, items, options, graph):
    if len(history) == len(items):
        return history

    remaining = [item for item in items if item not in history]
    target = max(remaining, key=lambda x: len(graph[x]))

    randomized_options = options[:]
    random.shuffle(randomized_options)

    for choice in randomized_options:
        if verify_placement(target, choice, history, graph):
            history[target] = choice
            if run_backtracking(history, items, options, graph):
                return history
            history.pop(target)
    return None

computed_output = run_backtracking({}, area_names, palette, neighbor_map)

def assign_shading(row):
    return computed_output.get(row[label_key], "gray")

spatial_df["color_val"] = spatial_df.apply(assign_shading, axis=1)

canvas, subplot = plot_plt.subplots(figsize=(15, 15))
spatial_df.plot(ax=subplot, color=spatial_df["color_val"], edgecolor="black", linewidth=1.5)

for i, entry in spatial_df.iterrows():
    if entry.geometry:
        center = entry.geometry.centroid
        subplot.text(center.x, center.y, str(entry[label_key]), fontsize=8, ha='center', weight='bold',
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

plot_plt.title("Regional CSP Visualization", fontsize=16)
plot_plt.axis('off')
plot_plt.show()
  
