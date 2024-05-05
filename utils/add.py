def add_node_val(data):
  sum = data["val"]
  if len(data["children"]) == 0:
    return sum
  for child_data in data["children"]:
    sum += add_node_val(child_data)
  return sum


def get_node_val(data, depth):
  node_list = []
  if depth <= 0:
    result = add_node_val(data)
    node_list.append({
      "name": data["name"],
      "val": result
    })
  else:
    for child_data in data["children"]:
      node_list += get_node_val(child_data, depth - 1)
  return node_list


def get_data(data, depth, no_limit):
  filter_data = get_node_val(data, depth)
  filter_data = [{'name': item['name'], 'val': item['val'] + no_limit} for item in filter_data]
  filter_data = [item for item in filter_data if item['name'] != '不限']
  return filter_data