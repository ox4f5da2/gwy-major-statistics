import os
import json

def get_dict(json_folder_path):
  # 定义一个空的大字典
  merged_dict = {}

  # json_folder_path 指定 JSON 文件夹路径

  # 获取 JSON 文件夹下所有的 .json 文件路径
  file_paths = [os.path.join(json_folder_path, file) for file in os.listdir(json_folder_path) if file.endswith(".json")]

  # 读取并合并字典文件
  for file_path in file_paths:
      with open(file_path, "r") as file:
          data = json.load(file)
          merged_dict.update(data)

  # 打印合并后的大字典
  return merged_dict