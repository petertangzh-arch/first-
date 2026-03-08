#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import folium
from folium.plugins import MarkerCluster

# TSMC Fab locations
taiwan_fabs = [
    {"name": "Fab 18 (3nm Base)", "location": [22.9927, 120.2172], "process": "N3/N5/N7", "city": "Tainan"},
    {"name": "Fab 14", "location": [22.9930, 120.2270], "process": "N16/N12", "city": "Tainan"},
    {"name": "Fab 15", "location": [24.1778, 120.6417], "process": "N28/N22", "city": "Taichung"},
    {"name": "Fab 16", "location": [24.8544, 121.2153], "process": "N16", "city": "Longtan"},
    {"name": "Fab 8", "location": [24.7818, 120.9722], "process": "N7/N5", "city": "Hsinchu"},
]

overseas_fabs = [
    {"name": "Fab 21 Arizona", "location": [33.4919, -111.9281], "process": "N5/N3", "city": "Phoenix, USA"},
    {"name": "JASM Japan", "location": [32.8856, 130.8550], "process": "N28/N16", "city": "Kumamoto, Japan"},
    {"name": "ESMC Germany (Planned)", "location": [51.0330, 13.7330], "process": "N28", "city": "Dresden, Germany"},
]

# Create Taiwan map centered on Taiwan
taiwan_map = folium.Map(location=[23.7, 121.0], zoom_start=8, tiles='OpenStreetMap')

# Add markers for Taiwan fabs
for fab in taiwan_fabs:
    folium.Marker(
        location=fab["location"],
        popup=f"<b>{fab['name']}</b><br>Process: {fab['process']}<br>City: {fab['city']}",
        tooltip=fab["name"],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(taiwan_map)

# Add circle for emphasis on Tainan (3nm base)
folium.Circle(
    location=[22.9927, 120.2172],
    radius=8000,
    color='red',
    fill=True,
    fillColor='red',
    fillOpacity=0.3,
    popup="3nm Production Base"
).add_to(taiwan_map)

taiwan_map.save('/Users/henryt/.openclaw/workspace/tsmc-taiwan-map.html')
print("Taiwan map HTML saved!")

# Create world map
world_map = folium.Map(location=[30, 20], zoom_start=2, tiles='OpenStreetMap')

# Add Taiwan marker
folium.Marker(
    location=[23.7, 121.0],
    popup="<b>Taiwan</b><br>Main Fabs: Fab 8, 14, 15, 16, 18",
    tooltip="Taiwan - Main Fabs",
    icon=folium.Icon(color='red', icon='home')
).add_to(world_map)

# Add overseas fabs
for fab in overseas_fabs:
    folium.Marker(
        location=fab["location"],
        popup=f"<b>{fab['name']}</b><br>Process: {fab['process']}<br>{fab['city']}",
        tooltip=fab["name"],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(world_map)

# Add circles for regions
folium.Circle(location=[23.7, 121.0], radius=500000, color='red', fillOpacity=0.1).add_to(world_map)  # Taiwan
folium.Circle(location=[33.5, -112], radius=100000, color='blue', fillOpacity=0.1).add_to(world_map)  # USA
folium.Circle(location=[33, 131], radius=100000, color='blue', fillOpacity=0.1).add_to(world_map)  # Japan
folium.Circle(location=[51, 14], radius=100000, color='blue', fillOpacity=0.1).add_to(world_map)  # Germany

world_map.save('/Users/henryt/.openclaw/workspace/tsmc-world-map.html')
print("World map HTML saved!")

print("\nHTML maps created. Converting to images...")

# Now convert to screenshots using browser
print("Done - files saved as HTML")
