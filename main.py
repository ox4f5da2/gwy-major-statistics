from utils.parseExcel import parse_excel
from utils.statistics import statistics
from utils.classificationMajor import count
import utils.draw as draw
from utils.createExcel import create_excel

def main():
  parse_data = parse_excel("./1.xlsx")
  result = statistics(parse_data)
  major_count = count(result["字典"], result["专业"])

  draw.save_bar(result["政治面貌"], "政治面貌统计")
  draw.save_bar(result["学历"], "学历统计")
  draw.save_pie(major_count["children"], "文科报考公务员各专业大类数量")
  for major in major_count["children"]:
    draw.save_pie(major["children"], major["name"] + "中各专业数量")
  
  create_excel(major_count["children"])

if __name__ == "__main__":
  main()