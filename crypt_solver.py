from itertools import permutations

elements = ['T', 'W', 'O', 'F', 'U', 'R']
numbers = range(10)

for sequence in permutations(numbers, len(elements)):
    t_val, w_val, o_val, f_val, u_val, r_val = sequence
    
    if t_val == 0 or f_val == 0:
        continue
    
    val1 = (100 * t_val) + (10 * w_val) + o_val
    val2 = (1000 * f_val) + (100 * o_val) + (10 * u_val) + r_val
    
    if val1 + val1 == val2:
        print("Success! Values found:")
        print(f"T:{t_val} W:{w_val} O:{o_val} F:{f_val} U:{u_val} R:{r_val}")
        print(f"{val1} + {val1} = {val2}")
        break
      
