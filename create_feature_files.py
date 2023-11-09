import os
import csv
import numpy as np
import re
from sklearn.decomposition import PCA

current_path = os.getcwd()
def mass_density(file_name):
    mass_density_pattern = r'Mass density = ([\d.Ee+-]+) g/cm\*\*3'

    # Initialize variables to store the mass density value
    mass_density = None

    # Open the file and read line by line
    with open(file_name, 'r') as file:
        for line in file:
            match = re.search(mass_density_pattern, line)
            if match:
                # Extract and convert the mass density value to a float
                mass_density = float(match.group(1))
                break  # Stop searching once the first match is found
    return mass_density

def atomic_num_atom_per_mol(file_name):
    # Define a regular expression pattern for matching atomic number and atoms/molecule lines
    pattern = r'atomic number\s*=\s*(\d+),\s*atoms/molecule\s*=\s*([\d.Ee+-]+)'

    # Initialize lists to store the atomic number and atoms/molecule values
    atomic_numbers = []
    atoms_per_molecule = []

    # Open the file and read line by line
    with open(file_name, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                atomic_number = int(match.group(1))
                atoms_value = float(match.group(2))
                atomic_numbers.append(atomic_number)
                atoms_per_molecule.append(atoms_value)
    return (atomic_numbers, atoms_per_molecule)


def mean_excitation(file_name):
    mean_excitation_energy_pattern = r'Mean excitation energy = ([\d.Ee+-]+) eV'

    # Initialize variables to store the mean excitation energy value
    mean_excitation_energy = None

    # Open the file and read line by line
    with open(file_name, 'r') as file:
        for line in file:
            match = re.search(mean_excitation_energy_pattern, line)
            if match:
                # Extract and convert the mean excitation energy value to a float
                mean_excitation_energy = float(match.group(1))
                break  # Stop searching once the first match is found
    return mean_excitation_energy

def single_value_decomp(data):
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    standardized_data = (data - mean) / std_dev

    # Step 3: Apply SVD
    U, S, VT = np.linalg.svd(standardized_data, full_matrices=False)

    # Step 4: Choose the number of components to retain (e.g., n_components=1)
    n_components = 1

    # Step 5: Reduce dimensionality using SVD
    reduced_data = U[:, :n_components] @ np.diag(S[:n_components]) @ VT[:n_components, :]

    # Step 6: Inverse transform to get a single value
    aggregate_value = reduced_data[0, 0]  # Extract the single value from the matrix
    return aggregate_value

def pca(data):
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    standardized_data = (data - mean) / std_dev

    pca = PCA(n_components=1)
    pca.fit(standardized_data)

    # Step 4: Transform the data using PCA
    reduced_data = pca.transform(standardized_data)

    # Step 5: Extract the single value (the mean of the reduced data)
    aggregate_value = np.mean(reduced_data)
    return aggregate_value  


def photoelectric(file_name):
    # Define a regular expression pattern for matching data rows
    data_pattern = r'\s+([\d.Ee+-]+)'

    # Initialize variables to keep track of when to start and stop extracting data
    start_extraction = False
    all_photoelectric_svd = []
    data = []

    # Open the file and read line by line
    with open(file_name, 'r') as file:
        for line in file:
            if start_extraction and not line.startswith(' *** Photoelectric cross sections,') and not line.startswith(' PENELOPE') and not line.startswith('              0'):
                # Split the line using the regular expression pattern
                values = re.findall(data_pattern, line)
                if values:
                    # If values are found, add them to the data list as a list of strings
                    data.append(values)
                else:
                    # If no values are found, assume an empty list
                    data.append([])
            elif line.startswith(' *** Photoelectric cross sections,'):
                if len(data) != 0:
                    for i in range(len(data)):
                        data[i] = [float(value) for value in data[i]]
                    data = np.array(data)
                    all_photoelectric_svd.append(single_value_decomp(data))
                    data = []
                # Start extraction from 2 lines below the header
                start_extraction = True
            elif start_extraction and line.startswith(' PENELOPE'):
                for i in range(len(data)):
                        data[i] = [float(value) for value in data[i]]
                data = np.array(data)
                all_photoelectric_svd.append(single_value_decomp(data))
    #flattened_data = [value for row in data for value in row]
    return all_photoelectric_svd
 

def flatten_basic(file_name, geo_number, spc, aire_energy):
    mass_den = mass_density(file_name)
    atomic_number, atom_per_molecule = atomic_num_atom_per_mol(file_name)
    mean_excit = mean_excitation(file_name)
    result = [mass_den]
    for i in range(len(atomic_number)):
        result.append(atomic_number[i])
        result.append(atom_per_molecule[i]) 
    result.append(mean_excit)
    mass_den = result[0]
    mean_excitation_energy = result[-1]
    atom_data = result[1:-1]  # Exclude mass_density and mean_excitation_energy

    # Initializing lists for CSV data
    csv_columns = ['mass_den', 'atom_num_1', 'atom_per_mol_1', 'atom_num_2', 'atom_per_mol_2',
                'atom_num_3', 'atom_per_mol_3', 'atom_num_4', 'atom_per_mol_4', 'atom_num_5',
                'atom_per_mol_5', 'mean_excit', 'thickness', 'spc', 'energy_ratio']

    csv_data = [mass_den]

    # Process the atom data
    for i in range(0, len(atom_data), 2):
        csv_data.extend([int(atom_data[i]), float(atom_data[i + 1])])

    # Fill the remaining columns with -1 if needed
    while len(csv_data) < len(csv_columns):
        csv_data.append(-1)

    most_curr_path = os.getcwd()
    tally_file_path = os.path.join(most_curr_path, 'tallyEnergyDeposition.dat')
    if os.path.exists(tally_file_path):
        with open("tallyEnergyDeposition.dat", 'r') as file:
                content = file.read()
                
                # Use regular expression to find the value after '2' in the 'Material' line
                match = re.search(r'^\s*2\s+([0-9.]+[Ee][+-]\d+)\s*', content, re.MULTILINE)

                
                if match:
                    value = float(match.group(1))
        print(value, aire_energy)
        energy_ratio = value / (1.0 * aire_energy)
    else:
        energy_ratio = 1
    csv_data.pop()
    csv_data.pop()
    csv_data.pop()
    csv_data.pop()
    csv_data.append(mean_excitation_energy)
    csv_data.append(geo_number)
    csv_data.append(spc)
    csv_data.append(energy_ratio)


    # Create CSV file
    with open('basic_features.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(csv_columns)
        
        # Write data
        writer.writerow(csv_data)
    with open('/Users/berkecaliskan/Documents/Odysseus/ODYSSEUS_simulations/simulations/all_basic_features.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data)
    return result


for directory in os.listdir(current_path):
    print(directory)
    if directory == '30kV':
        for sub_directory in os.listdir(os.path.join(current_path, directory)):
            if sub_directory == "N30_030_0" or sub_directory == "N30_030_1":
                for sub_sub_directory in os.listdir(os.path.join(os.path.join(current_path, directory),sub_directory)):
                    os.chdir(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
                    all_files = os.listdir(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
                    mat_files = [file for file in all_files if file.endswith('.mat') and file != 'Aire.mat']
                    if len(mat_files) == 1:
                        geo_file_pattern = re.compile(r'oneL(\d+).geo')
                        geo_files = [file for file in all_files if geo_file_pattern.match(file)]
                        geo_file_name = geo_files[0]
                        geo_number_match = geo_file_pattern.match(geo_file_name)
                        geo_number = int(geo_number_match.group(1))
                        mat_file_name = mat_files[0]
                        flatten_basic(mat_files[0], geo_number, 30, float(1.92544E+00))
                    else:
                        print("There are either zero or multiple '.mat' files in the directory. ", os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
            elif sub_directory == "directory_list_30kV.txt" or sub_directory == "ref":
                continue
            else:
                os.chdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                all_files = os.listdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                mat_files = [file for file in all_files if file.endswith('.mat') and file != 'Aire.mat']
                if len(mat_files) == 1:
                    geo_file_pattern = re.compile(r'oneL(\d+).geo')
                    geo_files = [file for file in all_files if geo_file_pattern.match(file)]
                    geo_file_name = geo_files[0]
                    geo_number_match = geo_file_pattern.match(geo_file_name)
                    geo_number = int(geo_number_match.group(1))
                    mat_file_name = mat_files[0]
                    flatten_basic(mat_files[0], geo_number, 30, float(1.92544E+00))
                else:
                    print("There are either zero or multiple '.mat' files in the directory. ", os.path.join(os.path.join(current_path, directory),sub_directory))

    elif directory == '80kV':
        for sub_directory in os.listdir(os.path.join(current_path, directory)):
            if sub_directory == "RQR6_080_0" or sub_directory == "RQR6_080_1":
                for sub_sub_directory in os.listdir(os.path.join(os.path.join(current_path, directory),sub_directory)):
                    os.chdir(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
                    all_files = os.listdir(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
                    mat_files = [file for file in all_files if file.endswith('.mat') and file != 'Aire.mat']
                    if len(mat_files) == 1:
                        geo_file_pattern = re.compile(r'oneL(\d+).geo')
                        geo_files = [file for file in all_files if geo_file_pattern.match(file)]
                        geo_file_name = geo_files[0]
                        geo_number_match = geo_file_pattern.match(geo_file_name)
                        geo_number = int(geo_number_match.group(1))
                        mat_file_name = mat_files[0]
                        flatten_basic(mat_files[0], geo_number, 80, float(8.71549E-01))
                    else:
                        print("There are either zero or multiple '.mat' files in the directory. ", os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
            elif sub_directory == "directory_list_80kV.txt":
                continue
            else:
                os.chdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                all_files = os.listdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                mat_files = [file for file in all_files if file.endswith('.mat') and file != 'Aire.mat']
                if len(mat_files) == 1:
                    geo_file_pattern = re.compile(r'oneL(\d+).geo')
                    geo_files = [file for file in all_files if geo_file_pattern.match(file)]
                    geo_file_name = geo_files[0]
                    geo_number_match = geo_file_pattern.match(geo_file_name)
                    geo_number = int(geo_number_match.group(1))
                    mat_file_name = mat_files[0]
                    flatten_basic(mat_files[0], geo_number, 80, float(8.71549E-01))
                else:
                    print("There are either zero or multiple '.mat' files in the directory. ", os.path.join(os.path.join(current_path, directory),sub_directory))

    if directory == '100kV':
        for sub_directory in os.listdir(os.path.join(current_path, directory)):
            if sub_directory == "RQR8_100_0" or sub_directory == "RQR8_100_1":
                for sub_sub_directory in os.listdir(os.path.join(os.path.join(current_path, directory),sub_directory)):
                    os.chdir(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
                    all_files = os.listdir(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
                    mat_files = [file for file in all_files if file.endswith('.mat') and file != 'Aire.mat']
                    if len(mat_files) == 1:
                        geo_file_pattern = re.compile(r'oneL(\d+).geo')
                        geo_files = [file for file in all_files if geo_file_pattern.match(file)]
                        geo_file_name = geo_files[0]
                        geo_number_match = geo_file_pattern.match(geo_file_name)
                        geo_number = int(geo_number_match.group(1))
                        mat_file_name = mat_files[0]
                        flatten_basic(mat_files[0], geo_number, 100, float(7.73834E-01))
                    else:
                        print("There are either zero or multiple '.mat' files in the directory. ", os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
            elif sub_directory == "directory_list_100kV.txt":
                continue
            else:
                os.chdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                all_files = os.listdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                mat_files = [file for file in all_files if file.endswith('.mat') and file != 'Aire.mat']
                if len(mat_files) == 1:
                    geo_file_pattern = re.compile(r'oneL(\d+).geo')
                    geo_files = [file for file in all_files if geo_file_pattern.match(file)]
                    geo_file_name = geo_files[0]
                    geo_number_match = geo_file_pattern.match(geo_file_name)
                    geo_number = int(geo_number_match.group(1))
                    mat_file_name = mat_files[0]
                    flatten_basic(mat_files[0], geo_number, 100, float(7.73834E-01))
                else:
                    print("There are either zero or multiple '.mat' files in the directory. ", os.path.join(os.path.join(current_path, directory),sub_directory))

    if directory == '120kV':
        for sub_directory in os.listdir(os.path.join(current_path, directory)):
            if sub_directory == "x120kV_0" or sub_directory == "x120kV_1":
                for sub_sub_directory in os.listdir(os.path.join(os.path.join(current_path, directory),sub_directory)):
                    os.chdir(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
                    all_files = os.listdir(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
                    mat_files = [file for file in all_files if file.endswith('.mat') and file != 'Aire.mat']
                    if len(mat_files) == 1:
                        geo_file_pattern = re.compile(r'oneL(\d+).geo')
                        geo_files = [file for file in all_files if geo_file_pattern.match(file)]
                        geo_file_name = geo_files[0]
                        geo_number_match = geo_file_pattern.match(geo_file_name)
                        geo_number = int(geo_number_match.group(1))
                        mat_file_name = mat_files[0]
                        flatten_basic(mat_files[0], geo_number, 120, float(6.30952E-01))
                    else:
                        print("There are either zero or multiple '.mat' files in the directory. ", os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory),sub_sub_directory))
            elif sub_directory == "directory_list_120kV.txt":
                continue
            else:
                os.chdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                all_files = os.listdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                mat_files = [file for file in all_files if file.endswith('.mat') and file != 'Aire.mat']
                if len(mat_files) == 1:
                    geo_file_pattern = re.compile(r'oneL(\d+).geo')
                    geo_files = [file for file in all_files if geo_file_pattern.match(file)]
                    geo_file_name = geo_files[0]
                    geo_number_match = geo_file_pattern.match(geo_file_name)
                    geo_number = int(geo_number_match.group(1))
                    mat_file_name = mat_files[0]
                    flatten_basic(mat_files[0], geo_number, 120, float(6.30952E-01))
                else:
                    print("There are either zero or multiple '.mat' files in the directory. ", os.path.join(os.path.join(current_path, directory),sub_directory), mat_files)
