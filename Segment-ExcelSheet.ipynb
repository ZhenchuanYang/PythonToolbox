# 自动读取文件夹内所有Excel文件，并拆分每个Excel中多个Sheet为csv文件

# 读取文件夹中的所有Excel文件
import os
file0 = r"path of your target folder"
os.chdir(file0)
files = os.listdir()
files_xls = [f for f in files if f[-3:] == 'xls']
print(files_xls)

# 自动拆分Excel中多个Sheet为csv文件
def autodivide_Excelsheet(path, path_root):
    # path为Excel文件的路径，path_root为储存Excel文件的文件夹的路径
    '''自动拆分Excel中多个Sheet为csv文件'''
    # 导入numpy和pandas
    import numpy as np
    import pandas as pd
    # 读取Excel中所有数据
    df = pd.read_excel(path, sheet_name=None)
    keys = df.keys()
    # 将keys转换为list
    keys = list(keys)
    # 以list keys为基础读取每个sheet并将其存入csv文件中
    # 导入os模块
    import os
    for i in range(len(keys)):
        df[keys[i]].to_csv(os.path.join(path_root, keys[i] + '.csv'), header=True, index=False)

# 应用autodivide_Excelsheet函数自动拆分目标文件夹中所有Excel中的sheet为单独csv文件
for i in range(len(files_xls)):
    files_xls[i] = os.path.join(file0, files_xls[i])
    autodivide_Excelsheet(files_xls[i], file0)
