from matplotlib import pyplot as plt
from point import Point

point1 = "points1.txt"
point2 = "points2.txt"
point3 = "points3.txt"
point4 = "points4.txt"

# Create an instance of Point class
p = Point()

# Call the method to read points from a file
points, pointsx, pointsy = p.read_points(point4)

#Create a function for the slopes
def pairwise_slope(x1, y1, x2, y2):
  
  try:
    slope_AB = (y2 - y1) / (x2 - x1)
    if slope_AB == -0.0:
      slope_AB = 0.0
  except ZeroDivisionError:
    slope_AB = 0.0
    
  return float(slope_AB)

# Perfromed the slope function while looping through the points
positions = []
calculated_pairs = set()  # To keep track of calculated pairs

for i in range(len(points)):
    for j in range(len(points)):
        if i != j and (i, j) not in calculated_pairs and (j, i) not in calculated_pairs:
          #making sure we're not calculating the same pair twice
            slope_AB = pairwise_slope(pointsx[i], pointsy[i], pointsx[j], pointsy[j])
            point = (i, j, slope_AB)
            positions.append(point)
            calculated_pairs.add((i, j))  # Mark the pair as calculated


# Count occurrences of the third number in each group
counts = {}
for item in positions:
    counts[item[2]] = counts.get(item[2], 0) + 1

# Extract groups where the third number appears 6 times or more
third = [group for group in positions if counts[group[2]] >= 6]

# Group tuples based on the third number
grouped_data = {}
for item in third:
    third_num = item[2]
    if third_num in grouped_data:
        grouped_data[third_num].append(item)
    else:
        grouped_data[third_num] = [item]

# Extract the groups that have the numbers in positions 1 and 2 appear 3 times or more
occurrences = {}
result = []

for data in grouped_data.values():
    # Count occurrences of 1st and 2nd numbers in each group
    for item in data:
        for i in range(2):
            if item[i] in occurrences:
                occurrences[item[i]] += 1
            else:
                occurrences[item[i]] = 1

    # Extract 1st and 2nd numbers if they appear 3 or more times
    for item in data:
        count_1st = occurrences[item[0]]
        count_2nd = occurrences[item[1]]

        if count_1st >= 3 and count_2nd >= 3:
            result.append(item)

    # Clear occurrences for the next iteration
    occurrences = {}


# Group tuples based on the third number
grouped_data = {}
for item in result:
    third_num = item[2]
    if third_num in grouped_data:
        grouped_data[third_num].append(item)
    else:
        grouped_data[third_num] = [item]

selected_groups = {}

for key, group in grouped_data.items():
    unique_numbers = set()
    for tup in group:
        unique_numbers.add(tup[0])
        unique_numbers.add(tup[1])

    if len(unique_numbers) >= 4:
        selected_groups[key] = list(unique_numbers)


sorted_data = {}
for key, values in selected_groups.items():
  sorted_data[key] = sorted(values)

# Find the sorted data since the location for the points are the same for x and y
x = []
for key,group in sorted_data.items():
  x_new = group
  x.append(x_new)


# Extract x and y locations based on group indices
grouped_points = [[list(points[i]) for i in group] for group in x]

# Display x and y locations for each group with a line prefix
for i, group in enumerate(grouped_points):
    line = ' '.join([f"({point[0]}, {point[1]})" for point in group])
    print(f"Line: {line}")

# Display x and y locations for each group
newx = []
newy = []
for group in grouped_points:
    for point in group:
      newx.append(point[0])
      newy.append(point[1])


plt.plot(newx, newy,"ro")

for i in range(0, len(newx), 4):
  plt.plot(newx[i:i + 4], newy[i:i + 4])

  
  
plt.show()
