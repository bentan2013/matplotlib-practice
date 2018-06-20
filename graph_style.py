from matplotlib.pyplot import *


# 用例数据
x = [1,2,3,4]
y = [5,4,3,2]

# 创建新图表
figure()

# 坐标轴与大小自适应
autoscale()

# 可以设置线宽，线的样式，标记的样式，标志和图例
plot(x, y, linewidth=1.5, color=(0.5,0.5,1), label='plot', linestyle="-", marker='+')
legend(loc=3)
grid()
show()



