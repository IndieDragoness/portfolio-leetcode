# Trapping Rain Water
#
# Given an array representing elevation, compute the amount of water that can be held.

# Indexing in Python
# Positive: 0 (First entry), 1 (Second entry), 2, etc.
# Negative: -1 (Last entry), -2 (Second from last entry)
# Slicing a List:
#   - list[start : end : step]
#   - If no end is specified, it will keep stepping through til end

#              _   
#      _      | |_   _
#  _  | |_   _|   |_| |_
# | |_|   |_|           |
elevation_array = [0,1,0,2,1,0,1,3,2,1,2,1]

water_volume = 0

for i, current_height in enumerate(elevation_array):
    max_right = max(elevation_array[i::1])
    max_left = max(elevation_array[i::-1])

    if min(max_right, max_left) > current_height:
        water_volume += min(max_right, max_left) - current_height

# Print the calculated water volume
print(water_volume)