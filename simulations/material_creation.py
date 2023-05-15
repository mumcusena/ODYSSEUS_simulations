import os
import re
import subprocess

def two_material_density_calc(material1_mass, material2_mass, material3_mass, material1_density, material2_density, material3_density):
    material2_mass = float(material2_mass)
    material2_density = float(material2_density)
    material3_mass = float(material3_mass)
    material3_density = float(material3_density)
    mixture_density = ((material1_mass + material2_mass + material3_mass) * material3_density * material1_density * material2_density) / (material1_mass*material2_density*material3_density + material2_mass * material1_density*material3_density+material3_mass*material1_density*material2_density)
    return mixture_density    
def three_material_density_calc(material1_mass, material2_mass, material3_mass, material4_mass, material1_density, material2_density, material3_density, material4_density):
    material2_mass = float(material2_mass)
    material2_density = float(material2_density)
    material3_mass = float(material3_mass)
    material3_density = float(material3_density)
    material4_mass = float(material4_mass)
    material4_density = float(material4_density)
    mixture_density = ((material1_mass + material2_mass + material3_mass + material4_mass) * material3_density * material1_density * material2_density * material4_density) / (material1_mass*material2_density*material3_density*material4_density + material2_mass * material1_density*material3_density*material4_density+material3_mass*material1_density*material2_density*material4_density+material4_mass*material1_density*material2_density*material3_density)
    return mixture_density


atomic_numbers = {
    "Bi": 83,
    "W": 74,
    "Sb": 51,
    "Sn": 50,
    "Cu": 29,
    "B": 5,
    "Ba": 56
}

densities = {
    "Bi": 9.78,
    "W": 19.25,
    "Sb": 6.697,
    "Sn": 7.31,
    "Cu": 8.92,
    "B": 2.46,
    "Ba": 3.51
}



Energies = ["N30_030", "RQR6_080", "RQR8_100", "x120kV"]

simulations_path = os.getcwd()


for energy in Energies:
    if energy == "N30_030":
        folder = os.path.join(simulations_path,"30kV")
        os.chdir(folder)
        for simulation_folder in os.listdir(folder):
            print(simulation_folder)
            if re.match('N30_030_2_.._......._', simulation_folder):
                material_names = simulation_folder[21:]
                material_list = material_names.split("_")
                print(material_list)
                material_name = material_list[0] + "_" + material_list[1] + "_" +material_list[2] + "_" +material_list[3]
                c_ratio = 0
                h_ratio = 0
                if re.match('N30_030_2_02_......._', simulation_folder):
                    h_ratio = 0.028743
                    c_ratio = 0.171257
                    mixture_density = two_material_density_calc(0.2, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                elif re.match('N30_030_2_03_......._', simulation_folder):
                    h_ratio = 0.043115
                    c_ratio = 0.256885
                    mixture_density = two_material_density_calc(0.3, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                    #print(float(material_list[2]) + float(material_list[3]))
                elif re.match('N30_030_2_04_......._', simulation_folder):
                    h_ratio = 0.057486
                    c_ratio = 0.342514
                    mixture_density = two_material_density_calc(0.4, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                os.chdir("../../penelope_peneasy/penelope/pendbase")
                os.system('''echo "{}
                {}
                {}
                {}
                {} {}
                {} {}
                {} {}
                {} {}
                {}
                {}
                {}
../../../simulations/30kV/{}/mat.mat" | ./material.exe'''.format(1, material_name, 4, 2, 1, h_ratio, 6, c_ratio, atomic_numbers[material_list[0]], float(material_list[2]), atomic_numbers[material_list[1]], float(material_list[3]), 2, mixture_density, 2, simulation_folder))
                os.chdir(folder)        
            if re.match('N30_030_3_.._......._', simulation_folder):
                material_names = simulation_folder[21:]
                material_list = material_names.split("_")
                material_name = material_list[0] + "_" + material_list[1] + "_" +material_list[2] + "_" +material_list[3] + "_" +material_list[4] + "_" +material_list[5]
                c_ratio = 0
                h_ratio = 0
                if re.match('N30_030_3_02_......._', simulation_folder):
                    h_ratio = 0.028743
                    c_ratio = 0.171257
                    mixture_density = three_material_density_calc(0.2, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])
                elif re.match('N30_030_3_03_......._', simulation_folder):
                    h_ratio = 0.043115
                    c_ratio = 0.256885
                    mixture_density = three_material_density_calc(0.3, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])                    #print(float(material_list[2]) + float(material_list[3]))
                elif re.match('N30_030_3_04_......._', simulation_folder):
                    h_ratio = 0.057486
                    c_ratio = 0.342514
                    mixture_density = three_material_density_calc(0.4, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])
                os.chdir("../../penelope_peneasy/penelope/pendbase")
                os.system('''echo "{}
                {}
                {}
                {}
                {} {}
                {} {}
                {} {}
                {} {}
                {} {}
                {}
                {}
                {}
../../../simulations/30kV/{}/mat.mat" | ./material.exe'''.format(1, material_name, 5, 2, 1, h_ratio, 6, c_ratio, atomic_numbers[material_list[0]], float(material_list[3]), atomic_numbers[material_list[1]], float(material_list[4]), atomic_numbers[material_list[2]], float(material_list[5]), 2, mixture_density, 2, simulation_folder))
                os.chdir(folder)
    elif energy == "RQR6_080":
        folder = os.path.join(simulations_path,"80kV")
        os.chdir(folder)
        for simulation_folder in os.listdir(folder):
            print(simulation_folder)
            if re.match('RQR6_080_2_.._......._', simulation_folder):
                material_names = simulation_folder[22:]
                material_list = material_names.split("_")
                print(material_list)
                material_name = material_list[0] + "_" + material_list[1] + "_" +material_list[2] + "_" +material_list[3]
                c_ratio = 0
                h_ratio = 0
                if re.match('RQR6_080_2_02_......._', simulation_folder):
                    h_ratio = 0.028743
                    c_ratio = 0.171257
                    mixture_density = two_material_density_calc(0.2, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                elif re.match('RQR6_080_2_03_......._', simulation_folder):
                    h_ratio = 0.043115
                    c_ratio = 0.256885
                    mixture_density = two_material_density_calc(0.3, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                    #print(float(material_list[2]) + float(material_list[3]))
                elif re.match('RQR6_080_2_04_......._', simulation_folder):
                    h_ratio = 0.057486
                    c_ratio = 0.342514
                    mixture_density = two_material_density_calc(0.4, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                    #print(float(material_list[2]) + float(material_list[3]))
                os.chdir("../../penelope_peneasy/penelope/pendbase")
                os.system('''echo "{}
                {}
                {}
                {}
                {} {}
                {} {}
                {} {}
                {} {}
                {}
                {}
                {}
../../../simulations/80kV/{}/mat.mat" | ./material.exe'''.format(1, material_name, 4, 2, 1, h_ratio, 6, c_ratio, atomic_numbers[material_list[0]], float(material_list[2]), atomic_numbers[material_list[1]], float(material_list[3]), 2, mixture_density, 2, simulation_folder))
                os.chdir(folder)        
            if re.match('RQR6_080_3_.._......._', simulation_folder):
                material_names = simulation_folder[22:]
                material_list = material_names.split("_")
                print(material_list)
                material_name = material_list[0] + "_" + material_list[1] + "_" +material_list[2] + "_" +material_list[3] + "_" +material_list[4] + "_" +material_list[5]
                c_ratio = 0
                h_ratio = 0
                if re.match('RQR6_080_3_02_......._', simulation_folder):
                    h_ratio = 0.028743
                    c_ratio = 0.171257
                    mixture_density = three_material_density_calc(0.2, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])
                elif re.match('RQR6_080_3_03_......._', simulation_folder):
                    h_ratio = 0.043115
                    c_ratio = 0.256885
                    mixture_density = three_material_density_calc(0.3, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])                    #print(float(material_list[2]) + float(material_list[3]))
                elif re.match('RQR6_080_3_04_......._', simulation_folder):
                    h_ratio = 0.057486
                    c_ratio = 0.342514
                    mixture_density = three_material_density_calc(0.4, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])
                os.chdir("../../penelope_peneasy/penelope/pendbase")
                os.system('''echo "{}
                {}
                {}
                {}
                {} {}
                {} {}
                {} {}
                {} {}
                {} {}
                {}
                {}
                {}
../../../simulations/80kV/{}/mat.mat" | ./material.exe'''.format(1, material_name, 5, 2, 1, h_ratio, 6, c_ratio, atomic_numbers[material_list[0]], float(material_list[3]), atomic_numbers[material_list[1]], float(material_list[4]), atomic_numbers[material_list[2]], float(material_list[5]), 2, mixture_density, 2, simulation_folder))
                os.chdir(folder)
    elif energy == "RQR8_100":
        folder = os.path.join(simulations_path,"100kV")
        os.chdir(folder)
        for simulation_folder in os.listdir(folder):
            print(simulation_folder)
            if re.match('RQR8_100_2_.._......._', simulation_folder):
                material_names = simulation_folder[22:]
                material_list = material_names.split("_")
                material_name = material_list[0] + "_" + material_list[1] + "_" +material_list[2] + "_" +material_list[3]
                c_ratio = 0
                h_ratio = 0
                if re.match('RQR8_100_2_02_......._', simulation_folder):
                    h_ratio = 0.028743
                    c_ratio = 0.171257
                    mixture_density = two_material_density_calc(0.2, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                elif re.match('RQR8_100_2_03_......._', simulation_folder):
                    h_ratio = 0.043115
                    c_ratio = 0.256885
                    mixture_density = two_material_density_calc(0.3, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                    #print(float(material_list[2]) + float(material_list[3]))
                elif re.match('RQR8_100_2_04_......._', simulation_folder):
                    h_ratio = 0.057486
                    c_ratio = 0.342514
                    mixture_density = two_material_density_calc(0.4, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                    #print(float(material_list[2]) + float(material_list[3]))
                os.chdir("../../penelope_peneasy/penelope/pendbase")
                os.system('''echo "{}
                {}
                {}
                {}
                {} {}
                {} {}
                {} {}
                {} {}
                {}
                {}
                {}
../../../simulations/100kV/{}/mat.mat" | ./material.exe'''.format(1, material_name, 4, 2, 1, h_ratio, 6, c_ratio, atomic_numbers[material_list[0]], float(material_list[2]), atomic_numbers[material_list[1]], float(material_list[3]), 2, mixture_density, 2, simulation_folder))
                os.chdir(folder)        
            if re.match('RQR8_100_3_.._......._', simulation_folder):
                material_names = simulation_folder[22:]
                material_list = material_names.split("_")
                material_name = material_list[0] + "_" + material_list[1] + "_" +material_list[2] + "_" +material_list[3] + "_" +material_list[4] + "_" +material_list[5]
                c_ratio = 0
                h_ratio = 0
                if re.match('RQR8_100_3_02_......._', simulation_folder):
                    h_ratio = 0.028743
                    c_ratio = 0.171257
                    mixture_density = three_material_density_calc(0.2, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])
                elif re.match('RQR8_100_3_03_......._', simulation_folder):
                    h_ratio = 0.043115
                    c_ratio = 0.256885
                    mixture_density = three_material_density_calc(0.3, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])                    #print(float(material_list[2]) + float(material_list[3]))
                elif re.match('RQR8_100_3_04_......._', simulation_folder):
                    h_ratio = 0.057486
                    c_ratio = 0.342514
                    mixture_density = three_material_density_calc(0.4, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])
                os.chdir("../../penelope_peneasy/penelope/pendbase")
                os.system('''echo "{}
                {}
                {}
                {}
                {} {}
                {} {}
                {} {}
                {} {}
                {} {}
                {}
                {}
                {}
../../../simulations/100kV/{}/mat.mat" | ./material.exe'''.format(1, material_name, 5, 2, 1, h_ratio, 6, c_ratio, atomic_numbers[material_list[0]], float(material_list[3]), atomic_numbers[material_list[1]], float(material_list[4]), atomic_numbers[material_list[2]], float(material_list[5]), 2, mixture_density, 2, simulation_folder))
                os.chdir(folder)
    elif energy == "x120kV":
        folder = os.path.join(simulations_path,"120kV")
        os.chdir(folder)
        for simulation_folder in os.listdir(folder):
            print(simulation_folder)
            if re.match('x120kV_2_.._......._', simulation_folder):
                material_names = simulation_folder[20:]
                material_list = material_names.split("_")
                material_name = material_list[0] + "_" + material_list[1] + "_" +material_list[2] + "_" +material_list[3]
                c_ratio = 0
                h_ratio = 0
                if re.match('x120kV_2_02_......._', simulation_folder):
                    h_ratio = 0.028743
                    c_ratio = 0.171257
                    mixture_density = two_material_density_calc(0.2, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                elif re.match('x120kV_2_03_......._', simulation_folder):
                    h_ratio = 0.043115
                    c_ratio = 0.256885
                    mixture_density = two_material_density_calc(0.3, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                    #print(float(material_list[2]) + float(material_list[3]))
                elif re.match('x120kV_2_04_......._', simulation_folder):
                    h_ratio = 0.057486
                    c_ratio = 0.342514
                    mixture_density = two_material_density_calc(0.4, material_list[2], material_list[3], 0.95, densities[material_list[0]], densities[material_list[1]])
                    #print(float(material_list[2]) + float(material_list[3]))
                os.chdir("../../penelope_peneasy/penelope/pendbase")
                os.system('''echo "{}
                {}
                {}
                {}
                {} {}
                {} {}
                {} {}
                {} {}
                {}
                {}
                {}
../../../simulations/120kV/{}/mat.mat" | ./material.exe'''.format(1, material_name, 4, 2, 1, h_ratio, 6, c_ratio, atomic_numbers[material_list[0]], float(material_list[2]), atomic_numbers[material_list[1]], float(material_list[3]), 2, mixture_density, 2, simulation_folder))
                os.chdir(folder)        
            if re.match('x120kV_3_.._......._', simulation_folder):
                material_names = simulation_folder[20:]
                material_list = material_names.split("_")
                material_name = material_list[0] + "_" + material_list[1] + "_" +material_list[2] + "_" +material_list[3] + "_" +material_list[4] + "_" +material_list[5]
                c_ratio = 0
                h_ratio = 0
                if re.match('x120kV_3_02_......._', simulation_folder):
                    h_ratio = 0.028743
                    c_ratio = 0.171257
                    mixture_density = three_material_density_calc(0.2, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])
                elif re.match('x120kV_3_03_......._', simulation_folder):
                    h_ratio = 0.043115
                    c_ratio = 0.256885
                    mixture_density = three_material_density_calc(0.3, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])                    #print(float(material_list[2]) + float(material_list[3]))
                elif re.match('x120kV_3_04_......._', simulation_folder):
                    h_ratio = 0.057486
                    c_ratio = 0.342514
                    mixture_density = three_material_density_calc(0.4, material_list[3], material_list[4], material_list[5], 0.95, densities[material_list[0]], densities[material_list[1]], densities[material_list[2]])
                os.chdir("../../penelope_peneasy/penelope/pendbase")
                os.system('''echo "{}
                {}
                {}
                {}
                {} {}
                {} {}
                {} {}
                {} {}
                {} {}
                {}
                {}
                {}
../../../simulations/120kV/{}/mat.mat" | ./material.exe'''.format(1, material_name, 5, 2, 1, h_ratio, 6, c_ratio, atomic_numbers[material_list[0]], float(material_list[3]), atomic_numbers[material_list[1]], float(material_list[4]), atomic_numbers[material_list[2]], float(material_list[5]), 2, mixture_density, 2, simulation_folder))
                os.chdir(folder)           