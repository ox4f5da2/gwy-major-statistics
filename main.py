from utils.parseExcel import parse_excel
from utils.statistics import statistics
from utils.classificationMajor import count
import utils.draw as draw
from utils.createExcel import create_excel
from utils.add import get_data
import json

def main():
  parse_data = parse_excel("./1.xlsx")
  result = statistics(parse_data)
  no_limit = result["专业"]["不限"]
  major_count = count(result["字典"], result["专业"])

  draw.save_bar(result["政治面貌"], "政治面貌统计")
  draw.save_bar(result["学历"], "学历统计")
  second_major = get_data(major_count, 1, no_limit)
  draw.save_pie(second_major, "各专业大类数量")
  for major in major_count["children"]:
    third_major = get_data(major, 1, no_limit)
    draw.save_pie(third_major, major["name"] + "中各专业可报岗位数量")
  
  # create_excel(major_count["children"])

if __name__ == "__main__":
  main()