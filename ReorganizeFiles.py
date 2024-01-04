import pandas as pd
import numpy as np
import os
import shutil

# 将参与者编号填入partis列表中(需要自定义)
partis = ['2009','2014','2015','2017','2020','2023','2026','2037','2067','2068','2080']
devices = ['air','band','foot','gps','light','mic','noise']
# 根据partis列表中的参与者编号，创建对应的空文件夹
for parti in partis:
    os.mkdir(r'F:\GLAN_Data\final\{}'.format(parti)) #路径需要自定义
    for device in devices:
        os.mkdir(r'F:\GLAN_Data\final\{}\{}'.format(parti, device)) # 在每个参与者文件夹中，根据devices创建对应的设备文件夹
# 将所有文件按参与者编号-设备类别进行编排
for root,dirs,files in os.walk(r"F:\GLAN_Data\wave2_cw1"):
    # 遍历所有子文件夹
    for name in dirs:
        # 遍历子文件夹中的文件
        path = os.path.join(root, name)
        for root_2, dir_2, files_2 in os.walk(path):
                for file in files_2:
                    # 提取文件名前四个字符
                    i = file[0:4]
                    src_file = os.path.join(root_2, file)
                    dst_folder = os.path.join(r'F:\GLAN_Data\final', i, name)
                    shutil.copy(src_file,dst_folder)
                else:
                        pass
# 将设备类别名称加至文件名最前面
# 只遍历下一层子文件夹
root_path = r'F:\GLAN_Data\final'
folder_name = os.listdir(root_path)
folder_path = [os.path.join(root_path, name) for name in folder_name]
for i in folder_path:
    for root, dirs, files in os.walk(i):
        for name in dirs:
            # 遍历子文件夹中的文件
            path = os.path.join(root, name)
            for root_2, dir_2, files_2 in os.walk(path):
                    for file in files_2:
                        # 重命名文件，将name加至每个文件名前面
                        os.rename(os.path.join(root_2, file), os.path.join(root_2, name + '-' + file))
