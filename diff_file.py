
import os

def compare_folders(folder1, folder2):
    # 获取文件夹1和文件夹2的文件列表
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    # 计算文件夹1比文件夹2多的文件
    extra_in_folder1 = files1 - files2

    # 计算文件夹2比文件夹1多的文件
    extra_in_folder2 = files2 - files1

    print(f"文件夹1比文件夹2多的文件:")
    for file in extra_in_folder1:
        print(f"  {file}")

    print(f"\n文件夹2比文件夹1多的文件:")
    for file in extra_in_folder2:
        print(f"  {file}")

# 使用示例
folder1 = r'E:\DongOu\FDRS相关\相关工具数据\FDRS_PROCYON_JAVA\com.ford.fdt.hmi.host-72.5.29\com\ford\fdt\hmi\host\licensemanager'
folder2 = r'E:\DongOu\FDRS相关\解密后包\FRDS\DecryptClass\com.ford.fdt.hmi.host-72.5.29.jar\com\ford\fdt\hmi\host\licensemanager'

compare_folders(folder1, folder2)
