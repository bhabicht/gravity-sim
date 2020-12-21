from itertools import cycle

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def plot3D(x):
    """Plot color coded trajectories."""
    cycol = cycle('bgrcmk')
    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(5):
        ax.scatter(x[:, i, 0], x[:, i, 1], x[:, i, 2], c=next(cycol),
                   marker='.')
    plt.show()
