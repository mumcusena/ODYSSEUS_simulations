import os
import subprocess
import sys
import time

class Tmux(object):

    WAIT_SECS = 5

    def __init__(self, session_name, param):
        self.name = session_name
        self.p = subprocess.Popen(['tmux', 'new', '-d', '-s', session_name])

    def execute(self, cmd, wait_secs=WAIT_SECS):
        time.sleep(wait_secs)
        os.system('tmux send-keys -t ' + self.name + ' "' + cmd + '" Enter')

    def horizontal_split(self):
        time.sleep(1)
        os.system('tmux split-window -v -t %s' % self.name)

print('running simulations............')

current_path = '/users/sena.mumcu/ODYSSEUS_simulations/simulations'
print(current_path)
Energies = ["N30_030", "RQR6_080", "RQR8_100", "x120kV"] 

for i in range(1):
    if Energies[i] == "N30_030":
        tmux = Tmux("N30_030", 999)
        tmux.execute('srun --immediate --container-remap-root --container-image=debian --container-mounts=/users/sena.mumcu/:/home/shared_folder --time=600 --pty bash')
        tmux.execute('cd home/shared_folder/ODYSSEUS_simulations/simulations/30kV')
        tmux.execute('apt-get update')
        tmux.execute('apt-get install gfortran')
        tmux.execute('y')
        tmux.execute('apt-get install libgfortran5')
        print(os.getcwd())
        tmux.execute('cd home/shared_folder/ODYSSEUS_simulations/simulations/30kV')
        counter = 0
                # Path to the parent directory where the list of directories is stored
        parent_dir_path = '/users/sena.mumcu/ODYSSEUS_simulations/simulations/30kV'

        # Load the list of directories from the parent directory
        with open(os.path.join(parent_dir_path, "directory_list_30kV.txt"), "r") as f:
            directory_list = f.read().splitlines()

        for directory in os.listdir(parent_dir_path):
            if directory == 'N30_030_0' or directory == 'N30_030_1' or directory == 'directory_list_30kV.txt':
                continue
            if directory in directory_list:
                # Directory already in the list, continue
                continue
            
            # Directory not in the list, increment the counter and add it to the list
            tmux.execute('cd {}'.format(directory))
            tmux.execute('./penEasy.x < penEasy.in > penEasy.out &')
            counter += 1
            directory_list.append(directory)
            tmux.execute('cd ..')
            # Write the updated list back to the parent directory
            with open(os.path.join(parent_dir_path, "directory_list_30kV.txt"), "w") as f:
                f.write("\n".join(directory_list))
            
            # Stop the loop if the counter reaches 20
            if counter == 50:
                break
    if Energies[i] == "RQR6_080":
        tmux = Tmux("RQR6_080", 999)
        tmux.execute('srun --immediate --container-remap-root --container-image=debian --container-mounts=/users/sena.mumcu/:/home/shared_folder --time=600 --pty bash')
        tmux.execute('apt-get update')
        tmux.execute('apt-get install gfortran')
        tmux.execute('y')
        tmux.execute('apt-get install libgfortran5')
        tmux.execute('cd home/shared_folder/ODYSSEUS_simulations/simulations/80kV')
        counter = 0
                # Path to the parent directory where the list of directories is stored
        parent_dir_path = '/users/sena.mumcu/ODYSSEUS_simulations/simulations/80kV'

        # Load the list of directories from the parent directory
        with open(os.path.join(parent_dir_path, "directory_list_80kV.txt"), "r") as f:
            directory_list = f.read().splitlines()

        for directory in os.listdir(parent_dir_path):
            if directory == 'RQR6_080_0' or directory == 'RQR6_080_1' or directory == 'directory_list_80kV.txt':
                continue
            if directory in directory_list:
                # Directory already in the list, continue
                continue
            
            # Directory not in the list, increment the counter and add it to the list
            tmux.execute('cd {}'.format(directory))
            tmux.execute('./penEasy.x < penEasy.in > penEasy.out &')
            counter += 1
            directory_list.append(directory)
            tmux.execute('cd ..')
            # Write the updated list back to the parent directory
            with open(os.path.join(parent_dir_path, "directory_list_80kV.txt"), "w") as f:
                f.write("\n".join(directory_list))
            
            # Stop the loop if the counter reaches 20
            if counter == 50:
                break
    if Energies[i] == "RQR8_100":
        tmux = Tmux("RQR8_100", 999)
        tmux.execute('srun --immediate --container-remap-root --container-image=debian --container-mounts=/users/sena.mumcu/:/home/shared_folder --time=600 --pty bash')
        tmux.execute('apt-get update')
        tmux.execute('apt-get install gfortran')
        tmux.execute('y')
        tmux.execute('apt-get install libgfortran5')
        tmux.execute('cd home/shared_folder/ODYSSEUS_simulations/simulations/100kV')
        counter = 0
                # Path to the parent directory where the list of directories is stored
        parent_dir_path = '/users/sena.mumcu/ODYSSEUS_simulations/simulations/100kV'

        # Load the list of directories from the parent directory
        with open(os.path.join(parent_dir_path, "directory_list_100kV.txt"), "r") as f:
            directory_list = f.read().splitlines()

        for directory in os.listdir(parent_dir_path):
            if directory == 'RQR8_100_0' or directory == 'RQR8_100_1' or directory == 'directory_list_100kV.txt':
                continue
            if directory in directory_list:
                # Directory already in the list, continue
                continue
            
            # Directory not in the list, increment the counter and add it to the list
            tmux.execute('cd {}'.format(directory))
            tmux.execute('./penEasy.x < penEasy.in > penEasy.out &')
            counter += 1
            directory_list.append(directory)
            tmux.execute('cd ..')
            # Write the updated list back to the parent directory
            with open(os.path.join(parent_dir_path, "directory_list_100kV.txt"), "w") as f:
                f.write("\n".join(directory_list))
            
            # Stop the loop if the counter reaches 20
            if counter == 50:
                break
    if Energies[i] == "x120kV":
        tmux = Tmux("x120kV", 999)
        tmux.execute('srun --immediate --container-remap-root --container-image=debian --container-mounts=/users/sena.mumcu/:/home/shared_folder --time=600 --pty bash')
        tmux.execute('apt-get update')
        tmux.execute('apt-get install gfortran')
        tmux.execute('y')
        tmux.execute('apt-get install libgfortran5')
        tmux.execute('cd home/shared_folder/ODYSSEUS_simulations/simulations/120kV')
        counter = 0
                # Path to the parent directory where the list of directories is stored
        parent_dir_path = '/users/sena.mumcu/ODYSSEUS_simulations/simulations/120kV'

        # Load the list of directories from the parent directory
        with open(os.path.join(parent_dir_path, "directory_list_120kV.txt"), "r") as f:
            directory_list = f.read().splitlines()

        for directory in os.listdir(parent_dir_path):
            if directory == 'x120kV_0' or directory == 'x120kV_1' or directory == 'directory_list_120kV.txt':
                continue
            if directory in directory_list:
                # Directory already in the list, continue
                continue
            
            # Directory not in the list, increment the counter and add it to the list
            tmux.execute('cd {}'.format(directory))
            tmux.execute('./penEasy.x < penEasy.in > penEasy.out &')
            counter += 1
            directory_list.append(directory)
            tmux.execute('cd ..')
            # Write the updated list back to the parent directory
            with open(os.path.join(parent_dir_path, "directory_list_120kV.txt"), "w") as f:
                f.write("\n".join(directory_list))
            
            # Stop the loop if the counter reaches 20
            if counter == 50:
                break

