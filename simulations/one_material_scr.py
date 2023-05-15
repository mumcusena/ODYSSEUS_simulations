import os
import random
import itertools

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
        folder = os.path.join(current_path, "30kV")
        os.chdir(folder)
        for filename in os.listdir(folder):
            f = os.path.join(folder, filename)
            os.chdir(f)
            original_spc = current_path + "/{}.spc".format(energy) 
            spc_file = open(original_spc)
            with open("{}.spc".format(energy), 'w') as spc:
                for line in spc_file:
                    spc.write(line)
            spc_file.close()
            material_folder = os.path.join(current_path, "focused_folder")
            aire = material_folder + "/Aire.mat"
            aire_file = open(aire)
            with open('Aire.mat', 'w') as aire_mat:
                for line in aire_file:
                    aire_mat.write(line)
            aire_file.close()
            os.system('rm ./penEasy.x')
            os.system('cp ../../penEasy.x .')
            os.chdir(folder)
    elif energy == "RQR6_080": 
        folder = os.path.join(current_path, "80kV")
        os.chdir(folder)
        for filename in os.listdir(folder):
            f = os.path.join(folder, filename)
            os.chdir(f)
            original_spc = current_path + "/{}.spc".format(energy) 
            spc_file = open(original_spc)
            with open("{}.spc".format(energy), 'w') as spc:
                for line in spc_file:
                    spc.write(line)
            spc_file.close()
            material_folder = os.path.join(current_path, "focused_folder")
            aire = material_folder + "/Aire.mat"
            aire_file = open(aire)
            with open('Aire.mat', 'w') as aire_mat:
                for line in aire_file:
                    aire_mat.write(line)
            aire_file.close()
            os.system('rm ./penEasy.x')
            os.system('cp ../../penEasy.x .')
            os.chdir(folder)
    elif energy == "RQR8_100": 
        folder = os.path.join(current_path, "100kV")
        os.chdir(folder)
        for filename in os.listdir(folder):
            f = os.path.join(folder, filename)
            os.chdir(f)
            original_spc = current_path + "/{}.spc".format(energy) 
            spc_file = open(original_spc)
            with open("{}.spc".format(energy), 'w') as spc:
                for line in spc_file:
                    spc.write(line)
            spc_file.close()
            material_folder = os.path.join(current_path, "focused_folder")
            aire = material_folder + "/Aire.mat"
            aire_file = open(aire)
            with open('Aire.mat', 'w') as aire_mat:
                for line in aire_file:
                    aire_mat.write(line)
            aire_file.close()
            os.system('rm ./penEasy.x')
            os.system('cp ../../penEasy.x .')
            os.chdir(folder)
    elif energy == "x120kV": 
        folder = os.path.join(current_path, "120kV")
        os.chdir(folder)
        for filename in os.listdir(folder):
            f = os.path.join(folder, filename)
            os.chdir(f)
            original_spc = current_path + "/{}.spc".format(energy) 
            spc_file = open(original_spc)
            with open("{}.spc".format(energy), 'w') as spc:
                for line in spc_file:
                    spc.write(line)
            spc_file.close()
            material_folder = os.path.join(current_path, "focused_folder")
            aire = material_folder + "/Aire.mat"
            aire_file = open(aire)
            with open('Aire.mat', 'w') as aire_mat:
                for line in aire_file:
                    aire_mat.write(line)
            aire_file.close()
            os.system('rm ./penEasy.x')
            os.system('cp ../../penEasy.x .')
            os.chdir(folder)

    # for combo in Material_Combinations:
    #     if combo == "0" and 0:
    #         for thick in Thickness:
    #             for material in Materials:
    #                 os.mkdir("{}_{}_00_{}_{}".format(energy, combo, thick, material))
    #                 folder_2 = os.path.join(folder, "{}_{}_00_{}_{}".format(energy, combo, thick, material))
    #                 os.chdir(folder_2)
                    
    #                 original_spc = current_path + "/{}.spc".format(energy) 
    #                 spc_file = open(original_spc)
    #                 with open("{}.spc".format(energy), 'w') as spc:
    #                     for line in spc_file:
    #                         spc.write(line)
    #                 spc_file.close()
    #                 material_folder = os.path.join(current_path, "focused_folder")
    #                 focused_material = material_folder + "/{}.mat".format(material)
    #                 focused_material_file = open(focused_material)
    #                 with open('{}.mat'.format(material), 'w') as copy_material:
    #                     for line in focused_material_file:
    #                         copy_material.write(line)
    #                 aire = material_folder + "/Aire.mat"
    #                 aire_file = open(aire)
    #                 with open('Aire.mat', 'w') as aire_mat:
    #                     for line in aire_file:
    #                         aire_mat.write(line)
    #                 aire_file.close()
    #                 focused_material_file.close()
    #                 folder_2 = folder
    #                 os.system('cp ../../penEasy.x .')
    #                 os.chdir(folder_2)
    #     if combo == "1" and energy != "N30_030":
    #         for ratio in Polyweight_ratio:
    #             for thick in Thickness:
    #                 for material in Materials:

    #                     folder_2 = os.path.join(folder, "{}_{}_{}_{}_{}".format(energy, combo, ratio, thick, material))
    #                     os.chdir(folder_2)
                        
    #                     original_spc = current_path + "/{}.spc".format(energy) 
    #                     spc_file = open(original_spc)
    #                     with open("{}.spc".format(energy), 'w') as spc:
    #                         for line in spc_file:
    #                             spc.write(line)
    #                     spc_file.close()
    #                     material_folder = os.path.join(current_path, "focused_folder")
    #                     focused_material = material_folder + "/{}.mat".format(material)
    #                     focused_material_file = open(focused_material)
    #                     with open('{}.mat'.format(material), 'w') as copy_material:
    #                         for line in focused_material_file:
    #                             copy_material.write(line)
    #                     aire = material_folder + "/Aire.mat"
    #                     aire_file = open(aire)
    #                     with open('Aire.mat', 'w') as aire_mat:
    #                         for line in aire_file:
    #                             aire_mat.write(line)
    #                     aire_file.close()
    #                     focused_material_file.close()
    #                     folder_2 = folder
    #                     os.system('rm ./penEasy.x')
    #                     os.system('cp ../../penEasy.x .')
    #                     os.chdir(folder_2)
    #     elif combo == "2":
    #         for ratio in Polyweight_ratio:
    #             for thick in Thickness:
    #                 for material in Two_Materials:
    #                     poly_ratio = float(ratio)
    #                     poly_ratio /= 10
    #                     remaining_ratio = 1-poly_ratio
    #                     first_ratio = round(random.uniform(0.1, remaining_ratio-0.1), 2)
    #                     second_ratio = round(remaining_ratio - first_ratio, 2)
    #                     material_ratios = str(first_ratio) + "_" + str(second_ratio)
    #                     folder_2 = os.path.join(folder, "{}_{}_{}_{}_{}_{}".format(energy, combo, ratio, thick, material, material_ratios))
    #                     os.chdir(folder_2)
                       
    #                     original_spc = current_path + "/{}.spc".format(energy) 
    #                     spc_file = open(original_spc)
    #                     with open("{}.spc".format(energy), 'w') as spc:
    #                         for line in spc_file:
    #                             spc.write(line)
    #                     spc_file.close()
    #                     material_folder = os.path.join(current_path, "focused_folder")
    #                     focused_material = material_folder + "/{}.mat".format(material)
    #                     focused_material_file = open(focused_material)
    #                     with open('{}.mat'.format(material), 'w') as copy_material:
    #                         for line in focused_material_file:
    #                             copy_material.write(line)
    #                     aire = material_folder + "/Aire.mat"
    #                     aire_file = open(aire)
    #                     with open('Aire.mat', 'w') as aire_mat:
    #                         for line in aire_file:
    #                             aire_mat.write(line)
    #                     aire_file.close()
    #                     focused_material_file.close()
    #                     folder_2 = folder
    #                     os.system('rm ./penEasy.x')
    #                     os.system('cp ../../penEasy.x .')
    #                     os.chdir(folder_2)
    #     elif combo == "3":
    #         for ratio in Polyweight_ratio:
    #             for thick in Thickness:
    #                 for material in Three_Materials:
    #                     poly_ratio = float(ratio)
    #                     poly_ratio /= 10
    #                     remaining_ratio = 1-poly_ratio
    #                     first_ratio = round(random.uniform(0.1, remaining_ratio-0.1), 2)
    #                     remaining_ratio -= first_ratio
    #                     second_ratio = round(random.uniform(0.1, remaining_ratio-0.1), 2)
    #                     third_ratio = round(remaining_ratio - second_ratio, 2)
    #                     material_ratios = str(first_ratio) + "_" + str(second_ratio) + "_" + str(third_ratio)
    #                     folder_2 = os.path.join(folder, "{}_{}_{}_{}_{}_{}".format(energy, combo, ratio, thick, material, material_ratios))
    #                     os.chdir(folder_2)
                        
    #                     original_spc = current_path + "/{}.spc".format(energy) 
    #                     spc_file = open(original_spc)
    #                     with open("{}.spc".format(energy), 'w') as spc:
    #                         for line in spc_file:
    #                             spc.write(line)
    #                     spc_file.close()
    #                     material_folder = os.path.join(current_path, "focused_folder")
    #                     focused_material = material_folder + "/{}.mat".format(material)
    #                     focused_material_file = open(focused_material)
    #                     with open('{}.mat'.format(material), 'w') as copy_material:
    #                         for line in focused_material_file:
    #                             copy_material.write(line)
    #                     aire = material_folder + "/Aire.mat"
    #                     aire_file = open(aire)
    #                     with open('Aire.mat', 'w') as aire_mat:
    #                         for line in aire_file:
    #                             aire_mat.write(line)
    #                     aire_file.close()
    #                     focused_material_file.close()
    #                     folder_2 = folder
    #                     os.system('rm ./penEasy.x')
    #                     os.system('cp ../../penEasy.x .')
    #                     os.chdir(folder_2)
    #                     folder_2 = folder
    #                     os.chdir(folder_2)
