# Australian Map Coloring

This repository contains a Python implementation of a backtracking algorithm designed to solve the classic Map Coloring problem. The objective is to assign a color to every state and territory in Australia such that no two adjacent regions share the same color.

## Overview
The project uses a **Backtracking Search** algorithm to navigate the constraints of the map. By treating the map as a graph where regions are nodes and shared borders are edges, the solver ensures a valid coloring configuration using a limited palette.

## Project Structure
- **Adjacency Logic**: Represents the physical borders of Australia (WA, NT, SA, QLD, NSW, VIC, TAS) as a dictionary-based graph.
- **Validation Engine**: A recursive function that checks the validity of a color assignment against a region's neighbors before proceeding.
- **Recursive Solver**: Systematically attempts assignments and backtracks when it hits a "dead end" where no legal colors remain for a specific region.

## Colors Used
The solver is configured to find a solution using a three-color palette:
* Red
* Green
* Blue

## Getting Started
To run the solver, ensure you have Python 3 installed and execute the script:

```bash
python AUS_map_color.py
