import os
import csv
import numpy as np
import re
from sklearn.decomposition import PCA

current_path = os.getcwd()
first_row = 0
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
                'atom_per_mol_5', 'mean_excit', 'thickness']

    for i in range(1000, 120001, 1000):
        column_name = f'spc_{i}'
        csv_columns.append(column_name)
    csv_columns.append('energy_ratio')
    

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
    for i in range(120):
        csv_data.pop()
    csv_data.pop()
    csv_data.append(mean_excitation_energy)
    csv_data.append(geo_number)
    if spc == 30:
        array = [-0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30748163, -0.30489568, -0.28827172, -0.22731721, -0.07105202, 0.23889241
, 0.7409359, 1.42251812, 2.17022675, 2.92754033, 3.6065366, 4.11190488
, 4.35978654, 4.28294692, 3.83705546, 2.99736094, 1.76127742, 0.14284289
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105
, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105, -0.30785105]

        for element in array:
            csv_data.append(element)
    elif spc == 80:
        array = [-0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625
, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625
, -0.81513625, -0.8141581, -0.80926738, -0.79361708, -0.75742576, -0.68699939
, -0.5735347, -0.41311909, -0.22140288, -0.00327678, 0.23245591, 0.47601375
, 0.71663715, 0.94650098, 1.15973636, 1.35243071, 1.52067147, 1.66445863
, 1.75933859, 1.82487423, 1.87280328, 1.90312575, 1.91975419, 1.92268862
, 1.91486347, 1.89725688, 1.86986885, 1.83661196, 1.78574847, 1.72803798
, 1.66739306, 1.60576999, 1.54121249, 1.47665499, 1.4101412, 1.34362742
, 1.27613548, 1.20766541, 1.1362609, 1.06387825, 0.9914956, 0.92106924
, 0.84966473, 0.78021651, 0.71076829, 0.64132007, 1.11474173, 1.45807026
, 0.43590984, 0.36743977, 0.29896969, 0.23245591, 0.16594212, 0.09942833
, 0.03487083, 0.30679484, -0.09424417, -0.08544087, -0.23705318, -0.29476367
, -0.35345231, -0.41214095, -0.47082958, -0.52854007, -0.58625057, -0.64396106
, -0.70167155, -0.7584039, -0.81513625, -0.81513625, -0.81513625, -0.81513625
, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625
, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625
, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625
, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625
, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625
, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625, -0.81513625]

        for element in array:
            csv_data.append(element)
    elif spc == 100:
        array = [-0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627
, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627
, -0.93353627, -0.93241597, -0.93017537, -0.92121297, -0.89768668, -0.8517544
, -0.77445373, -0.66130348, -0.51902544, -0.35098051, -0.16052959, 0.04336493
, 0.25286094, 0.46123666, 0.66064997, 0.84774, 1.01802552, 1.16926596
, 1.28017562, 1.36531838, 1.43365665, 1.48631073, 1.52440092, 1.5501678
, 1.5647317, 1.5680926, 1.5636114, 1.5501678, 1.52104002, 1.48407013
, 1.44373935, 1.40116797, 1.35635598, 1.3093034, 1.26225082, 1.21407794
, 1.16478476, 1.11549158, 1.06171721, 1.00794283, 0.95416845, 0.90151437
, 0.84998059, 0.79844682, 0.74803334, 0.69874016, 2.62341476, 4.08316506
, 0.55422152, 0.50492834, 0.45787576, 0.41194348, 0.36601119, 0.32119921
, 0.27750753, 1.48070923, 0.19124447, 0.38617659, 0.01199654, -0.01937185
, -0.05074023, -0.08210862, -0.11347701, -0.14596569, -0.17733408, -0.20982277
, -0.24119115, -0.27367984, -0.30616853, -0.33865721, -0.3711459, -0.40363459
, -0.43500297, -0.46749166, -0.49998035, -0.53134873, -0.56383742, -0.59520581
, -0.62769449, -0.65906288, -0.69043127, -0.72179966, -0.75204774, -0.78341613
, -0.81366422, -0.84391231, -0.87416039, -0.90440848, -0.93353627, -0.93353627
, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627
, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627
, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627, -0.93353627]
        for element in array:
            csv_data.append(element)
    elif spc == 120:
        array = [-8.98493075e-01, -8.98493075e-01, -8.98493075e-01, -8.98493075e-01
, -8.98493075e-01, -8.98493075e-01, -8.98493075e-01, -8.98493075e-01
, -8.98493075e-01, -8.98493075e-01, -8.98493075e-01, -8.98493075e-01
, -8.98493075e-01, -8.98493075e-01, -8.98493075e-01, -8.98493075e-01
, -8.98493075e-01, -8.97414894e-01, -8.96336713e-01, -8.90945808e-01
, -8.82320361e-01, -8.65069467e-01, -8.37036763e-01, -7.97144069e-01
, -7.41078662e-01, -6.69918722e-01, -5.83664250e-01, -4.83393425e-01
, -3.70184430e-01, -2.49428168e-01, -1.27593726e-01, -5.75928302e-03
, 1.16075160e-01, 2.34675059e-01, 3.47884055e-01, 4.54623965e-01
, 5.53816608e-01, 6.45461985e-01, 7.27403734e-01, 8.00720036e-01
, 8.57863624e-01, 9.05303584e-01, 9.45196278e-01, 9.77541705e-01
, 1.00233987e+00, 1.02066894e+00, 1.03360711e+00, 1.04007620e+00
, 1.04223256e+00, 1.04007620e+00, 1.03037257e+00, 1.01635622e+00
, 9.99105323e-01, 9.79698067e-01, 9.58134449e-01, 9.35492650e-01
, 9.10694489e-01, 8.84818147e-01, 3.98566644e+00, 6.45038799e+00
, 7.98563674e-01, 7.66218247e-01, 7.33872820e-01, 7.01527393e-01
, 6.68103784e-01, 6.35758357e-01, 6.02334749e-01, 2.75977475e+00
, 5.36565714e-01, 7.74843694e-01, 1.50576949e-01, 1.38716959e-01
, 1.25778788e-01, 1.12840617e-01, 9.77460841e-02, 8.26515514e-02
, 6.75570187e-02, 5.13843051e-02, 3.41334106e-02, 1.68825160e-02
, -1.44655938e-03, -2.08538157e-02, -4.02610721e-02, -6.07465093e-02
, -8.01537657e-02, -1.00639203e-01, -1.22202821e-01, -1.42688258e-01
, -1.64251876e-01, -1.85815495e-01, -2.08457294e-01, -2.30020912e-01
, -2.52662711e-01, -2.75304510e-01, -2.97946309e-01, -3.20588108e-01
, -3.43229907e-01, -3.66949887e-01, -3.89591686e-01, -4.13311666e-01
, -4.35953465e-01, -4.59673445e-01, -4.83393425e-01, -5.07113405e-01
, -5.30833385e-01, -5.53475184e-01, -5.77195164e-01, -6.00915144e-01
, -6.24635124e-01, -6.47276923e-01, -6.70996903e-01, -6.93638702e-01
, -7.17358682e-01, -7.40000481e-01, -7.63720461e-01, -7.86362260e-01
, -8.09004059e-01, -8.31645858e-01, -8.54287657e-01, -8.75851276e-01]
        for element in array:
            csv_data.append(element)
    csv_data.append(energy_ratio)

    with open('/Users/berkecaliskan/Documents/Odysseus/ODYSSEUS_simulations/simulations/feature_files/all_basic_features_spc_dist.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        global first_row
        if first_row == 0:
            writer.writerow(csv_columns)
            first_row = 1
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
