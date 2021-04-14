import numpy as np
import matplotlib.pyplot as plt


def plot_restrictions(point_on_boarder=False):
    x_point = 0.4288
    y_point = 0.3213
    d = np.linspace(-5, 5, 300)
    x1, x2 = np.meshgrid(d, d)

    if point_on_boarder:
        plt.imshow(
            ((-x1 <= 0) & (x1 - 2 * x2 - 0.3 <= 0) & (x1 + x2 - 0.7501 <= 0) & (-x1 + 2 * x2 - 1 <= 0)).astype(int),
            extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha=0.3)
    else:
        plt.imshow(((-x1 <= 0) & (x1 - 2 * x2 - 0.3 <= 0) & (x1 + x2 - 1 <= 0) & (-x1 + 2 * x2 - 1 <= 0)).astype(int),
                   extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha=0.3)

    x1 = np.linspace(-1, 1.2, 200)
    y1 = x1
    y2 = (x1 - 0.3) / 2
    y3 = (x1 + 1) / 2
    if point_on_boarder:
        y4 = 0.7501 - x1
    else:
        y4 = 1 - x1

    plt.plot(0 * x1, y1, label=r'$-x_1\leq0$')
    plt.plot(x1, y2, label=r'$x_1-2x_2-0.3\leq0$')
    plt.plot(x1, y3, label=r'$-x_1+2x_2-1\leq0$')
    if point_on_boarder:
        plt.plot(x1, y4, label=r'$x_1+x_2-0.7501\leq0$')
    else:
        plt.plot(x1, y4, label=r'$x_1+x_2-1\leq0$')

    plt.scatter(x_point, y_point, c="black")
    text = "(" + str(x_point) + "," + str(y_point) + ")"
    plt.text(x_point + 0.1, y_point - 0.1, text)

    plt.xlim(-0.4, 1.2)
    plt.ylim(-0.6, 1.2)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')

    plt.show()
