def find_dict_by_name(array, key):
  for item in array:
    if isinstance(item, dict) and "name" in item and item["name"] == key:
      return item
  return None


def initial_val(dict, keys):
  for key in keys[::-1]:
    children = dict["children"]
    result = find_dict_by_name(children, key)
    if result is not None:
      dict = result
      continue
    else:
      dict = {
        "val": 0,
        "name": key,
        "children": []
      }
      children.append(dict)


def get_classification_major(dict, no_limit_val):
  major_dict = {
    "name": "all",
    "val": no_limit_val,
    "children": []
  }
  for key, value in dict.items():
    initial_val(major_dict, [key] + value)
  return major_dict


def add_leaf_child(data, val):
  if len(data["children"]) == 0:
    data["val"] += val
    return
  for child in data["children"]:
    add_leaf_child(child, val)


def add_val(dict, path, val):
  for key in path[::-1]:
    result = find_dict_by_name(dict["children"], key)
    dict = result
  dict["val"] += val


def count(major_dict, result):
  count_dict = get_classification_major(major_dict, result["不限"])
  for key, value in result.items():
    paths = [key] + major_dict.get(key, [])
    add_val(count_dict, paths, value)
  return count_dict
    
    
