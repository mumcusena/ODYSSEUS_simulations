import os 
import re

current_path = os.getcwd()

for directory in os.listdir(current_path):
    print(directory)
    if directory == '30kV':
        for sub_directory in os.listdir(os.path.join(current_path, directory)):
            if sub_directory == "N30_030_0" or sub_directory == "N30_030_1" or sub_directory == "directory_list_30kV.txt" or sub_directory == "ref":
                continue
            else:
                os.chdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                with open(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory), "penEasy.in"), "r") as f:
                    input_string = f.read()
                new_input = re.sub(r'\s[A-Z]+[a-z]*\_[A-Z]+[a-z]*\_.*(?<!Aire)\.mat ', ' mat.mat ', input_string)
                print(new_input)
                with open(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory), "penEasy.in"), "w") as w:
                    w.write(new_input)
    elif directory == '80kV':
        for sub_directory in os.listdir(os.path.join(current_path, directory)):
            if sub_directory == "RQR6_080_0" or sub_directory == "RQR6_080_1" or sub_directory == "directory_list_80kV.txt":
                continue
            else:
                os.chdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                with open(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory), "penEasy.in"), "r") as f: # type: ignore
                    input_string = f.read()
                new_input = re.sub(r'\s[A-Z]+[a-z]*\_[A-Z]+[a-z]*\_.*(?<!Aire)\.mat ', ' mat.mat ', input_string)
                with open(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory), "penEasy.in"), "w") as w:
                    w.write(new_input)
    if directory == '100kV':
        for sub_directory in os.listdir(os.path.join(current_path, directory)):
            if sub_directory == "RQR8_100_0" or sub_directory == "RQR8_100_1" or sub_directory == "directory_list_100kV.txt":
                continue
            else:
                os.chdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                with open(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory), "penEasy.in"), "r") as f:
                    input_string = f.read()
                new_input = re.sub(r'\s[A-Z]+[a-z]*\_[A-Z]+[a-z]*\_.*(?<!Aire)\.mat ', ' mat.mat ', input_string)
                with open(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory), "penEasy.in"), "w") as w:
                    w.write(new_input)
    if directory == '120kV':
        for sub_directory in os.listdir(os.path.join(current_path, directory)):
            if sub_directory == "x120kV_0" or sub_directory == "x120kV_1" or sub_directory == "directory_list_120kV.txt":
                continue
            else:
                os.chdir(os.path.join(os.path.join(current_path, directory),sub_directory))
                with open(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory), "penEasy.in"), "r") as f:
                    input_string = f.read()
                new_input = re.sub(r'\s[A-Z]+[a-z]*\_[A-Z]+[a-z]*\_.*(?<!Aire)\.mat ', ' mat.mat ', input_string)
                with open(os.path.join(os.path.join(os.path.join(current_path, directory),sub_directory), "penEasy.in"), "w") as w:
                    w.write(new_input)