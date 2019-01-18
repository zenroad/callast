import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('201807.csv',parse_dates=True)
data['ts'] = pd.to_datetime(data['ts'])
data['ts'] = data['ts'].astype(int)
#print(data.info())
#print(data.head())
#data['ts'].astype(int)
#data.plot.scatter(x='ts', y='var001')
data.set_index('ts', inplace=True)
for i in range(1,10):
    name = 'var00'+str(i)
    df = data[name]
    df.plot(title=name)
    plt.show()
for i in range(10,69):
    name = 'var0'+str(i)
    df = data[name]
    df.plot(title=name)
    plt.show()
'''
data = pd.read_csv('ss.csv',parse_dates=True)
data['ts'] = pd.to_datetime(data['ts'])
data.set_index('ts', inplace=True)
#print(data.head(2))
#print(data.info())
df = pd.DataFrame(data['var001'])
plt.plot()
'''
'''
# 用来正常显示负号
plt.rcParams['axes.unicode_minus']=False

# 刻度大小
plt.rcParams['axes.labelsize']=16
# 线的粗细
plt.rcParams['lines.linewidth']=2
# x轴标签大小
plt.rcParams['xtick.labelsize']=14
# y轴标签大小
plt.rcParams['ytick.labelsize']=14
#图例大小
plt.rcParams['legend.fontsize']=14
# 图大小
plt.rcParams['figure.figsize']=[12,8]

# 生成-5~5 的10个数 array([-5, -4, -3, -2, -1,  0,  1,  2,  3,  4])
'''
#x = np.arange(-5,5)
#y = [10,13,5,40,30,60,70,12,55,25] 
'''
x = data['ts']
y = data['var001']
# 正常显示中文字体
plt.rcParams['font.sans-serif']=['Microsoft YaHei']

# 绘图，设置(label)图例名字为'第一条线'，显示图例plt.legend()
plt.plot(x,y,label='第一条线')

# x轴标签
plt.xlabel('横坐标')
# y轴标签
plt.ylabel('纵坐标')

# 可视化图标题
plt.title('这是一个折线图')

# 显示图例
plt.legend()
# 显示图形
plt.show() 

def loadCSVfile2(): 
    tmp = np.loadtxt("train.csv", dtype=np.str, delimiter=",") 
    data = tmp[1:,1:].astype(np.float)#加载数据部分 
    label = tmp[1:,0].astype(np.float)#加载类别标签部分 
    return data, label #返回array类型的数据
'''