import os
import subprocess
import sys
import time

current_path = '/users/sena.mumcu/ODYSSEUS_simulations/simulations'
print(current_path)
Energies = ["N30_030", "RQR6_080", "RQR8_100", "x120kV"] 

os.chdir("/Users/senamumcu/Desktop/ODYSSEUS_simulations/simulations/100kV")
print(len(os.listdir(os.getcwd())))