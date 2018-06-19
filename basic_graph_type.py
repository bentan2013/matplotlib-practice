from matplotlib.pyplot import *

# 引用Python数据可视化编程实战一书，第三章，主要是将注释翻译为中文
# 在熟练之后会加入更多的应用

# 用例数据
x = [1,2,3,4]
y = [5,4,3,2]

# 创建新图表
figure()


# subplot(nrows, ncols, index, **kwargs)
# 将图表分为2行，3列，并选择第1个
subplot(2, 3, 1)
# 线状图
plot(x, y)

# 选择第2个
# 条状图
subplot(2, 3, 2)
bar(x, y)

# 选择第三个
subplot(2, 3, 3)
# 绘制水平条状图
barh(x, y)

# 选择第四个
subplot(2, 3, 4)
bar(x, y)
y1 = [7,8,5,3]
# 绘制多分类，累积柱状图
bar(x, y1, bottom=y, color='r')

#box plot
subplot(2, 3, 5)

# 箱线图
boxplot(x)

subplot(2, 3, 6)
# 散点图
scatter(x, y)
show()






