from utils.getDict import get_dict


def statistics_dict(dict, data):
  for j in range(len(data)):
    key = data[j]
    if key in dict:
      dict[key] += 1
    else:
      dict[key] = 1


def parse_major(data, major_dict, major_count):
  for i in range(len(data)):
    major = data[i]
    if major in major_dict:
      # other_major = major_dict[major]
      statistics_dict(major_count, [major])
      

def statistics(data):
  education = {}
  political_status = {}
  major = {}
  major_dict = get_dict("json")

  for i in range(len(data)):
    row = data[i]
    political_status_data = row["政治面貌"]
    education_data = row["学历"]
    major_data = row["专业"]

    statistics_dict(political_status, political_status_data)
    statistics_dict(education, education_data)
    parse_major(major_data, major_dict, major)
  
  return {
    "政治面貌": political_status,
    "学历": education,
    "专业": major,
    "字典": major_dict
  }


    
    