import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt  # 后面的方法省略了import
plt.rcParams['font.sans-serif']=['Hiragino Sans GB'] # 修改字体
plt.rcParams['axes.unicode_minus'] = False
color=[
  '#5470c6', 
  '#92cc76', 
  '#fac858',
  '#ef6666',
  '#73c0de',
  '#3ba272',
  '#fc8452',
  '#9a60b4',
  '#ea7ccc'
]

def create_folder(result_folder):
  if not os.path.exists(result_folder):
    os.makedirs(result_folder)


def save_bar(data, title):
  # 提取标签和大小
  categories = list(data.keys())
  values = list(data.values())

  # 柱状图
  bars = plt.bar(categories, values, color=color)
  plt.xlabel(title)
  plt.ylabel('人数')
  plt.title(title + '统计')
  for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')
  
  result_folder = "result"
  create_folder(result_folder)
  plt.savefig(os.path.join(result_folder, title + '.png'))
  plt.clf()


def save_pie(data, title):
  # 提取名称和值
  labels = [d['name'] for d in data]
  sizes = [d['val'] for d in data]

  # 创建子图
  fig, axs = plt.subplots(1, 2, figsize=(16, 8))

  # 饼图
  axs[0].pie(sizes, labels=labels, autopct="%1.2f%%", startangle=0, colors=color)
  axs[0].axis('equal')  # 使饼图保持圆形
  axs[0].set_title(title + '统计百分比', pad=20)

  # 绘制柱状图
  bars = axs[1].bar(labels, sizes, color=color)
  axs[1].set_xlabel(title)
  axs[1].set_ylabel('人数')
  axs[1].set_title(title + '统计')

  for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')

  # 调整布局
  plt.tight_layout()

  # 显示图形
  result_folder = "result"
  create_folder(result_folder)
  plt.savefig(os.path.join(result_folder, title + '.png'))
  plt.clf()
