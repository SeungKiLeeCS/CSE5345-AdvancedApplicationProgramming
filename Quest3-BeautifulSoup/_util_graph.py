import matplotlib.pyplot as plt

def graphthis(xlist, ylist, xlabel, ylabel, title, color):
    x = xlist
    yval = ylist
    x_pos = [i for i, _ in enumerate(x)]
    plt.figure(figsize=(10,6))
    plt.bar(x_pos, yval, color=color)
    plt.xticks(x_pos, x)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()