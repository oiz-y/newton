import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def newton_method(f, x, init_value, num):
    df = sp.diff(f, x)
    next_value = 0
    for i in range(num):
        next_value = init_value - f.subs(x, init_value) / df.subs(x, init_value)
        init_value = next_value
    return next_value

    
def plot_graph():
    x_ = np.linspace(0, 2, 100)
    y_ = np.sin(x_) - 0.5
    plt.plot(x_, y_, label='sin(x) - 0.5')
    plt.plot(x_, [0] * len(x_), color='black')
    plt.scatter([init_value], [0], c='blue', label='initial point')
    plt.scatter([solution], [0], c='red', label='solution')
    plt.legend()
    plt.show()
    
    
if __name__ == '__main__':
    x = sp.Symbol('x')
    f = sp.sin(x) - 0.5
    init_value = 0.1
    num = 10
    solution = newton_method(f, x, init_value, num)
    print(solution)
    # グラフをプロット
    plot_graph()
