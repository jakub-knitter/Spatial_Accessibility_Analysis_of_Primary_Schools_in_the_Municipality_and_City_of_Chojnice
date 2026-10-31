# Spatial Accessibility Analysis of Primary Schools in the Municipality and City of Chojnice

## About the Project
The goal of this project was to analyze pedestrian accessibility to primary educational institutions across the Municipality and City of Chojnice, as well as to identify areas of spatial exclusion (> 3,000 meters from the nearest school)

## Tools & Methodology
- **Software:** QGIS 3.40.12
- **Network Analysis:**
  * `ORS Tools` - calculation of 3 km walking isochrones along the road network.
  * `QNEAT3` - matrix cost calculation (OD Matrix) from residential building centroids to school facilities using the OpenStreetMap (OSM) network.
- **Data Sources:** OpenStreetMap, BDOT10k, PRG (Polish National Register of Boundaries), QuickOSM.

## Workflow & Steps Taken
1. Gathering public domain data for the Municipality and City of Chojnice.
2. Loading the basemap and spatial layers via OpenStreetMap and QuickOSM.
3. Generating centroids for residential building geometries.
4. Generating an OD Matrix layer via the QNEAT3 plugin from residential centroids to school facilities along the OSM network.
5. Joining the resulting network analysis layer back to the residential building dataset.
6. Assigning residential buildings to the nearest schools based on shortest road distance (total_cost).
7. Calculating 3,000-meter reachability isochrones from schools.
8. Identifying spatial exclusion zones and composing the final map layout with analytical inset maps.


![Optimal School Network Map](<img/Spatial Accessibility Analysis of Schools in the Municipality and City of Chojnice.png>)
---
*Author: Jakub Knitter*  
*Date: 10.2026*
