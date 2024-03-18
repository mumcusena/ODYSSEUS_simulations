import os

current_path = os.getcwd()
RUN = 1
Energies = ["N30_030", "RQR6_080", "RQR8_100", "x120kV"] 

for i in range(RUN):
    if Energies[i] == "N30_030":

        # Path to the parent directory where the list of directories is stored
        parent_dir_path = '/users/sena.mumcu/ODYSSEUS_simulations/simulations/30kV'

        # Load the list of directories from the parent directory
        with open(os.path.join(parent_dir_path, "directory_list_30kV.txt"), "r") as f:
            directory_list = f.read().splitlines()

        counter = 0

        for directory in os.listdir(parent_dir_path):
            if directory == 'N30_030_0' or directory == 'N30_030_1' or directory == 'directory_list_30kV.txt': # VERY IMPORTANNNT
                continue
            if directory in directory_list:
                # Directory already in the list, continue
                continue
            
            os.system("cd {}".format(os.path.join(parent_dir_path, directory)))
            # Directory not in the list, increment the counter and add it to the list
            os.system("./penEasy.x < penEasy.in > penEasy.out &")
            counter += 1
            directory_list.append(directory)
            os.system('cd ..')
            # Write the updated list back to the parent directory
            with open(os.path.join(parent_dir_path, "directory_list_30kV.txt"), "w") as f:
                f.write("\n".join(directory_list))
            
            # Stop the loop if the counter reaches 20
            if counter == 50:
                break