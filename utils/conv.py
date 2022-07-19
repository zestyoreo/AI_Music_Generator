import pypianoroll
import os
 
# Get the list of all files and directories
lvl0_folder_path = "lpd/lpd_cleansed"
lvl0_dir_list = os.listdir(lvl0_folder_path) #A
i=1
for lvl1_folder in lvl0_dir_list:
    lvl1_folder_path = lvl0_folder_path+"/"+lvl1_folder
    if not os.path.isfile(lvl1_folder_path):
        lvl1_dir_list = os.listdir(lvl1_folder_path)
        for lvl2_folder in lvl1_dir_list: #A/A
            lvl2_folder_path = lvl1_folder_path+"/"+lvl2_folder
            if not os.path.isfile(lvl2_folder_path):
                lvl2_dir_list = os.listdir(lvl2_folder_path)
                for lvl3_folder in lvl2_dir_list: #A/A/A
                    lvl3_folder_path = lvl2_folder_path+"/"+lvl3_folder
                    if not os.path.isfile(lvl3_folder_path):
                        lvl3_dir_list = os.listdir(lvl3_folder_path)
                        for lvl4_folder in lvl3_dir_list: #A/A/A/xxxmmm
                            lvl4_folder_path = lvl3_folder_path+"/"+lvl4_folder
                            if not os.path.isfile(lvl4_folder_path):
                                lvl4_dir_list = os.listdir(lvl4_folder_path)
                                for lvl5_folder in lvl4_dir_list: #A/A/A/xxxxmm/nnn.npz
                                    lvl5_file = lvl4_folder_path+"/"+lvl5_folder
                                    if os.path.isfile(lvl5_file):
                                        if lvl4_folder!=".DS_Store":
                                            print(lvl5_file)
                                            data_file = pypianoroll.load(lvl5_file)
                                            data_file_name = "music_data/"+str(i)+".mid"
                                            pypianoroll.write(data_file_name,data_file)
                                            i=i+1

print("Total files: ",i)
