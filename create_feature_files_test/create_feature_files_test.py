import re
import numpy as np
from sklearn.decomposition import PCA
import csv

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
    with open('mat.mat', 'r') as file:
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

def flatten_basic(file_name):
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
                'atom_per_mol_5', 'mean_excit']

    csv_data = [mass_den]

    # Process the atom data
    for i in range(0, len(atom_data), 2):
        csv_data.extend([int(atom_data[i]), float(atom_data[i + 1])])

    # Fill the remaining columns with -1 if needed
    while len(csv_data) < len(csv_columns):
        csv_data.append(-1)

    csv_data.pop()
    csv_data.append(mean_excitation_energy)

    # Create CSV file
    with open('basic_features.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(csv_columns)
        
        # Write data
        writer.writerow(csv_data)
    return result

file_name = 'mat.mat'

mass_den = mass_density(file_name)
atom_num, atom_per_mol = atomic_num_atom_per_mol(file_name)
mean_excit = mean_excitation(file_name)
photo_electric = photoelectric(file_name)

# Now, the data list contains each row with float values
print(mass_den)
print(atom_num)
print(atom_per_mol)
print(mean_excit)
print(flatten_basic(file_name))
print(photo_electric)
