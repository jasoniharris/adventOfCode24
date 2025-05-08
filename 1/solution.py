#!/usr/bin/env python3

def calculate_total_distance(input_file):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Parse the left and right lists
    left_list = []
    right_list = []
    
    for line in lines:
        if not line.strip():
            continue
        
        parts = line.strip().split()
        if len(parts) >= 2:
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the distance between each pair
    total_distance = 0
    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
    
    return total_distance

if __name__ == "__main__":
    result = calculate_total_distance("input.txt")
    print(f"The total distance between the lists is: {result}")