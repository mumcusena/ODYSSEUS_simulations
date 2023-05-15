import os
import random
import itertools
import re

Energies = ["N30_030", "RQR6_080", "RQR8_100", "x120kV"] #put .spc names without .spc
Material_Combinations = ["0", "1", "2", "3"]
Polyweight_ratio = ["02", "03", "04"]
Thickness = ["oneL030", "oneL060", "oneL090", "oneL120"] #put .geo names without .geo
Materials = ["Bi", "W", "Sb", "Sn", "Cu", "B", "Ba"] #put .mat names without .mat
Two_Materials = [] #put .mat names without .mat
Three_Materials = [] #put .mat names without .mat

current_path = os.getcwd()

for energy in Energies:

    if energy == "N30_030":
        folder = os.path.join(current_path,"30kV/N30_030_1")
        os.chdir(folder)
        for simulation_folder in os.listdir(folder):
            if re.match('^N30_030_1_04_oneL..._B$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/B.mat .')
            elif re.match('^N30_030_1_04_oneL..._Ba$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f) 
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Ba.mat .')
            elif re.match('^N30_030_1_04_oneL..._Bi$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Bi.mat .')
            elif re.match('^N30_030_1_04_oneL..._Cu$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Cu.mat .')
            elif re.match('^N30_030_1_04_oneL..._Sb$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Sb.mat .')
            elif re.match('^N30_030_1_04_oneL..._Sn$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Sn.mat .')
            elif re.match('^N30_030_1_04_oneL..._W$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/W.mat .')


    elif energy == "RQR6_080":
        folder = os.path.join(current_path,"80kV/RQR6_080_1")
        os.chdir(folder)
        for simulation_folder in os.listdir(folder):
            if re.match('^RQR6_080_1_04_oneL..._B$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/B.mat .')
            elif re.match('^RQR6_080_1_04_oneL..._Ba$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f) 
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Ba.mat .')
            elif re.match('^RQR6_080_1_04_oneL..._Bi$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Bi.mat .')
            elif re.match('^RQR6_080_1_04_oneL..._Cu$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Cu.mat .')
            elif re.match('^RQR6_080_1_04_oneL..._Sb$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Sb.mat .')
            elif re.match('^RQR6_080_1_04_oneL..._Sn$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Sn.mat .')
            elif re.match('^RQR6_080_1_04_oneL..._W$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/W.mat .')


    elif energy == "RQR8_100":
        folder = os.path.join(current_path,"100kV/RQR8_100_1")
        os.chdir(folder)
        for simulation_folder in os.listdir(folder):
            if re.match('^RQR8_100_1_04_oneL..._B$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/B.mat .')
            elif re.match('^RQR8_100_1_04_oneL..._Ba$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f) 
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Ba.mat .')
            elif re.match('^RQR8_100_1_04_oneL..._Bi$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Bi.mat .')
            elif re.match('^RQR8_100_1_04_oneL..._Cu$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Cu.mat .')
            elif re.match('^RQR8_100_1_04_oneL..._Sb$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Sb.mat .')
            elif re.match('^RQR8_100_1_04_oneL..._Sn$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Sn.mat .')
            elif re.match('^RQR8_100_1_04_oneL..._W$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/W.mat .')


    if energy == "x120kV":
        folder = os.path.join(current_path,"120kV/x120kV_1")
        os.chdir(folder)
        for simulation_folder in os.listdir(folder):
            if re.match('^x120kV_1_04_oneL..._B$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/B.mat .')
            elif re.match('^x120kV_1_04_oneL..._Ba$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f) 
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Ba.mat .')
            elif re.match('^x120kV_1_04_oneL..._Bi$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Bi.mat .')
            elif re.match('^x120kV_1_04_oneL..._Cu$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Cu.mat .')
            elif re.match('^x120kV_1_04_oneL..._Sb$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Sb.mat .')
            elif re.match('^x120kV_1_04_oneL..._Sn$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/Sn.mat .')
            elif re.match('^x120kV_1_04_oneL..._W$', simulation_folder):
                f = os.path.join(folder, simulation_folder)
                os.chdir(f)
                os.system('cp ../../../../penelope_peneasy/penelope/pendbase/W.mat .')

