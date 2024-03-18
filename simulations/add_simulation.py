import os
import random
import re
import shutil

# number of the simulations to be added
NUM_SIMULATION = 100
current_path = os.getcwd()

for i in range(1):
    random_energy_level = "120kV/x120kV_1" if random.randint(1, 2) == 1 else "100kV/RQR8_100_1"

    simulations_path = os.path.join(current_path, "simulations/{}".format(random_energy_level))

    random_simulation_number = random.randint(1, 84)
    simulation_list = os.listdir(simulations_path)

    lucky_simulation = simulation_list[random_simulation_number]
    # print(lucky_simulation)
    parts = lucky_simulation.split("_")
    if(len(parts) == 6):
        poly_ratio = parts[3]
        element = parts[5]
    else: 
        poly_ratio = parts[2]
        element = parts[4]

    simulation_140 = "{}_{}_oneL140_{}".format(random_energy_level[6:] ,poly_ratio, element)
    simulation_150 = "{}_{}_oneL150_{}".format(random_energy_level[6:] ,poly_ratio, element)
    simulation_200 = "{}_{}_oneL200_{}".format(random_energy_level[6:] ,poly_ratio, element)
    simulation_250 = "{}_{}_oneL250_{}".format(random_energy_level[6:] ,poly_ratio, element)
    os.mkdir(os.path.join(simulations_path, simulation_140))
    os.mkdir(os.path.join(simulations_path, simulation_150))
    os.mkdir(os.path.join(simulations_path, simulation_200))
    os.mkdir(os.path.join(simulations_path, simulation_250))

    spc_file = random_energy_level[:-2]
    spc_file = spc_file[6:]
    print(spc_file)

    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "Aire.mat")), os.path.join(simulations_path, simulation_140))
    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "penEasy.x")), os.path.join(simulations_path, simulation_140))
    shutil.copy(os.path.join(simulations_path, "{}/{}.spc".format(lucky_simulation, spc_file)), os.path.join(simulations_path, simulation_140))

    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "Aire.mat")), os.path.join(simulations_path, simulation_150))
    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "penEasy.x")), os.path.join(simulations_path, simulation_150))
    shutil.copy(os.path.join(simulations_path, "{}/{}.spc".format(lucky_simulation, spc_file)), os.path.join(simulations_path, simulation_150))

    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "Aire.mat")), os.path.join(simulations_path, simulation_200))
    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "penEasy.x")), os.path.join(simulations_path, simulation_200))
    shutil.copy(os.path.join(simulations_path, "{}/{}.spc".format(lucky_simulation, spc_file)), os.path.join(simulations_path, simulation_200))

    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "Aire.mat")), os.path.join(simulations_path, simulation_250))
    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "penEasy.x")), os.path.join(simulations_path, simulation_250))
    shutil.copy(os.path.join(simulations_path, "{}/{}.spc".format(lucky_simulation, spc_file)), os.path.join(simulations_path, simulation_250))




