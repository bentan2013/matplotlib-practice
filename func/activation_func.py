from matplotlib.pyplot import *
import numpy as np


# 理解函数形状尤为重要
# 由于对np不太熟悉，里面有些代码不优美，后续会改进
# 激活函数有哪些 https://zhuanlan.zhihu.com/p/41894523
# 绘图参考 https://blog.csdn.net/weixin_34397291/article/details/86752128
# sigmoid
# tanh
# relu

# 阶跃函数
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


def step_function_np(x):
    return np.array(x > 0 , dtype=np.int)

# sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ReLu
def relu(x):
    return np.maximum(0, x)

# PReLU
def prelu(x):
    return np.where(x < 0, 0.25*x, x)

# tanh
def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

# softmax
def softmax(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x 
    return y

# 用例数据
x = np.linspace(-10, 10, 50)

# 创建新图表
figure()

# 阶跃函数 
# 将图表分为2行，3列，并选择第1个
subplot(2, 3, 1).set_title('step')
z = step_function_np(x)
plot(x, z)

# sigmoid
subplot(2, 3, 2).set_title('sigmoid')
z = sigmoid(x)
plot(x, z)

# relu 
subplot(2, 3, 4).set_title('relu')
z = relu(x)
plot(x, z)

# prelu 
subplot(2, 3, 5).set_title('prelu')
z = prelu(x)
plot(x, z)

# tanh
subplot(2, 3, 3).set_title('tanh')
z = tanh(x)
plot(x, z)

# softmax
# 如上所示，softmax函数的输出是0.0到1.0之间的实数。
# 并且，softmax函数的输出值的总和是1。
# 输出总和为1是softmax函数的一个重要性质。
# 正因为有了这个性质，我们才可以把softmax函数的输出解释为“概率”。
# 一般而言，神经网络只把输出值最大的神经元所对应的类别作为识别结果。
# 并且，即便使用softmax函数，输出值最大的神经元的位置也不会变。
# 因此，神经网络在进行分类时，输出层的softmax函数可以省略。
subplot(2, 3, 6).set_title('softmax')
z = softmax(x)
bar(x, z)

# 调整子图间距
subplots_adjust(wspace=0.3, hspace=0.5)  

# 显示图表
show()






