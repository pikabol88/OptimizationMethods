import numpy as np
import matplotlib.pyplot as plt


def plot_restrictions():
    d = np.linspace(-5, 5, 300)
    x1, x2 = np.meshgrid(d, d)
    plt.imshow(((-x1 <= 0) & (-x2 <= 0) & (x1 + x2 - 0.5 <= 0) & (x1 - 2 * x2 <= 0)).astype(int),
               extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha=0.3);

    x1 = np.linspace(-1, 1, 200)
    y1 = x1
    y2 = (x1 * 0) + 0
    y3 = x1 / 2
    y4 = 0.5 - x1

    plt.plot(0 * x1, y1, label=r'$-x_1\leq0$')
    plt.plot(x1, y2, label=r'$-x_2\leq0$')
    plt.plot(x1, y3, label=r'$x_1-2x_2\leq0$')
    plt.plot(x1, y4, label=r'$x_1+x_2-0.5\leq0$')

    plt.xlim(-0.25, 0.8)
    plt.ylim(-0.25, 0.8)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')

    plt.show()
