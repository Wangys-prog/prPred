import os
import argparse

import pandas as pd
import glob
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input',help ='the input folder',required=True,type = str)
    parser.add_argument('-o', '--output', help='the output file', required=True, type=str)
    args = parser.parse_args()
    input = args.input
    output = args.output
    return (input,output)

def merge_tables (input,output):
    folder_path = input
    # 获取所有子文件夹中的 CSV 文件路径
    all_csv_files = glob.glob(folder_path + '/**/domain_result', recursive=True)
    # 创建一个空的 DataFrame 用于存储合并后的数据
    merged_data = pd.DataFrame()
    # 获取文件总数
    total_files = len(all_csv_files)
    # 创建进度条
    progress_bar = tqdm(total=total_files, unit='file', desc='Merging CSV files')
    # 逐个读取并合并 CSV 文件
    for file in all_csv_files:
        try:
            df = pd.read_csv(file)  # 读取 CSV 文件
            merged_data = pd.concat([merged_data, df], ignore_index=True)  # 合并数据
        except pd.errors.ParserError as e:
            print(f"解析文件 {file} 时出错：{e}")
        # 更新进度条
        progress_bar.update(1)
    # 关闭进度条
    progress_bar.close()

    # 指定要保存合并后数据的输出文件路径
    output_file = output
    # 保存合并后的数据到新的 CSV 文件
    merged_data.to_csv(output_file, index=False)
    print("CSV files merged successfully!")


def main():
    input,output = parse_args()
    merge_tables(input,output)

if __name__ == "__main__":
    main()