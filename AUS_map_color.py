region_list = ["WA", "NT", "Queensland", "SA", "NSW", "V", "T"]
color_options = ["Red", "Green", "Blue"]

border_map = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Queensland"],
    "SA": ["WA", "NT", "Queensland", "NSW", "V"],
    "Queensland": ["NT", "SA", "NSW"],
    "NSW": ["Queensland", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

def check_consistency(loc, c, current_map, graph):
    for adjacency in graph[loc]:
        if adjacency in current_map and current_map[adjacency] == c:
            return False
    return True

def find_solution(current_map, regions, palette, graph):
    if len(current_map) == len(regions):
        return current_map

    target_loc = regions[len(current_map)]

    for choice in palette:
        if check_consistency(target_loc, choice, current_map, graph):
            current_map[target_loc] = choice
            
            outcome = find_solution(current_map, regions, palette, graph)
            if outcome:
                return outcome
            
            del current_map[target_loc]

    return None

final_result = find_solution({}, region_list, color_options, border_map)

if final_result:
    for area, paint in final_result.items():
        print(f"Region {area} -> Color: {paint}")
else:
    print("Failure: No valid configuration exists.")
