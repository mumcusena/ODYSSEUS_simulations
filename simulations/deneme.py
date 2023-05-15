import os
import subprocess
import sys
import time

# class Tmux(object):

#     WAIT_SECS = 5

#     def __init__(self, session_name, param):
#         self.name = session_name
#         self.p = subprocess.Popen(['tmux', 'new', '-d', '-s', session_name])

#     def execute(self, cmd, wait_secs=WAIT_SECS):
#         time.sleep(wait_secs)
#         os.system('tmux send-keys -t ' + self.name + ' "' + cmd + '" Enter')

#     def horizontal_split(self):
#         time.sleep(1)
#         os.system('tmux split-window -v -t %s' % self.name)

# print('running simulations............')

# current_path = '/clusterusers/berke.caliskan@boun.edu.tr/simulations'
# print(current_path)
Energies = ["N30_030", "RQR6_080", "RQR8_100", "x120kV"] 

# for energy in Energies:
#     if energy == "N30_030":
#         tmux = Tmux("N30_030_1", 999)
#         tmux.execute('srun --container-image=debian --container-mounts=/clusterusers/berke.caliskan@boun.edu.tr/:/home/shared_folder --time=600 --pty bash')
#         tmux.execute('apt-get update')
#         tmux.execute('apt-get install gfortran')
#         tmux.execute('y')
#         folder = os.path.join(current_path,"30kV/N30_030_1")
#         i = 0
#         for simulation_folder in os.listdir(folder):
#             if i == 0:
#                 tmux.execute('cd home/shared_folder/simulations/30kV/N30_030_1/{}'.format(simulation_folder))
#             else:
#                 tmux.execute('cd ../../30kV/N30_030_1/{}'.format(simulation_folder))
#             tmux.execute('./penEasy.x < penEasy.in > penEasy.out &')
#             i += 1

# os.chdir(current_path)

curr = os.getcwd()
for energy in Energies:
    if energy == "RQR8_100":
        f = os.path.join(curr, "100kV/RQR8_100_1")
        os.chdir(f)
        for sim in os.listdir(f):
            ff = os.path.join(f, sim)
            os.chdir(ff)
            subprocess.call(["./penEasy.x", "<", "penEasy.in", ">", "penEasy.out", "&"])
