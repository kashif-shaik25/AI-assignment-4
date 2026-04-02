# Geospatial Constraint Satisfaction: Regional Map Coloring

This project implements an automated boundary detection and map coloring system. It processes geospatial data (KML) to identify district adjacencies and applies a Constraint Satisfaction Problem (CSP) solver to ensure a valid 4-color mapping.

## Technical Requirements
To run this visualization, you will need the following Python libraries:
- **GeoPandas**: For handling spatial dataframes and KML parsing.
- **Matplotlib**: For rendering the final colored map.
- **Fiona**: To provide the necessary drivers for KML file access.
- **Random**: To ensure varied color assignments across different runs.

## Features
- **Automated Adjacency Detection**: Uses the `.touches()` geometric predicate to find neighboring districts without manual entry.
- **Heuristic-Based Backtracking**: Implements a "Most Constrained Variable" (MRV) heuristic, prioritizing districts with the most neighbors to find a solution faster.
- **Dynamic Labeling**: Automatically calculates the centroid of each district polygon to place text labels accurately.

## Data Source
The script is configured to read from a `telangana.kml` file. This data was sourced from OpenCity India

## Execution
Ensure your KML file is in the root directory and run:

```bash
python regional_csp_plot.py

