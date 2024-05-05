from openpyxl import Workbook
import os


def create_folder(result_folder):
  if not os.path.exists(result_folder):
    os.makedirs(result_folder)


def create_excel(data):
  # 创建一个新的Workbook对象
  wb = Workbook()

  for dict in data:
    for major in dict["children"]:
      # 创建新的工作表
      ws = wb.create_sheet(title=major["name"])
      ws.append(['专业名称', '可报考岗位的具体数量', '占二级专业总数的百分比'])
      
      sum = 0
      for sub_dict in major["children"]:
        sum += sub_dict["val"]

      for sub_dict in major["children"]:
        val = sub_dict["val"]
        ws.append([sub_dict["name"], val, round(val / sum * 100, 2) if sum != 0 else 0])

  # 保存Workbook到文件
  create_folder("result")
  wb.save('./result/各三级专业可报岗位具体数量统计.xlsx')

