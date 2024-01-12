import numpy as np
from sklearn.preprocessing import StandardScaler

integer_array = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 7, 15, 31, 57, 94, 146, 212, 292, 385, 490, 602, 715, 828, 941, 1051, 1156, 1255, 1347, 1432, 1508, 1576, 1629, 1673, 1710, 1740, 1763, 1780, 1792, 1798, 1800, 1798, 1789, 1776, 1760, 1742, 1722, 1701, 1678, 1654, 4530, 6816, 1574, 1544, 1514, 1484, 1453, 1423, 1392, 3393, 1331, 1552, 973, 962, 950, 938, 924, 910, 896, 881, 865, 849, 832, 814, 796, 777, 759, 740, 720, 701, 681, 661, 640, 620, 599, 578, 557, 536, 515, 493, 472, 450, 429, 407, 385, 363, 341, 320, 298, 276, 254, 233, 211, 190, 168, 147, 125, 104, 83, 62, 41, 21])
integer_array = integer_array.reshape(-1, 1)

# Initialize StandardScaler
scaler = StandardScaler()

# Fit and transform the integer array
scaled_array = scaler.fit_transform(integer_array)

# Convert scaled array back to a 1D array
scaled_array = scaled_array.flatten()

# Display the scaled array
print("Scaled Array:", scaled_array)