import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

def event_scheme():
    fig, ax = plt.subplots()
    evts = 11

    grid = np.zeros(shape=(evts, 2))
    for i in range(evts):
        grid[i] = [i/evts, 0]

    patches = []
    central = []

    for i in range(0, evts):
        rect = mpatches.Rectangle(grid[i], 0.05, 0.1, fc="red")
        patches.append(rect)

    rectcentral = mpatches.Rectangle(grid[5], 0.05, 0.1, fc="red")
    central.append(rectcentral)

    collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.6)
    ax.add_collection(collection)

    centralhit = PatchCollection(
        central, cmap=plt.cm.hsv, alpha=0.6, color='red')
    ax.add_collection(centralhit)

    plt.annotate(s='', xy=(0.0, -0.05), xytext=(0.4, -0.05),
                 arrowprops=dict(arrowstyle='<->'))
    plt.annotate(s='', xy=(0.55, -0.05), xytext=(0.95, -0.05),
                 arrowprops=dict(arrowstyle='<->'))
    plt.text(0.1, -0.1, 'NEIGHBOURS')
    plt.text(0.65, -0.1, 'NEIGHBOURS')
    plt.text(0.32, -0.2, 'event to classify', fontsize=14,
             bbox=dict(facecolor='red', alpha=0.2))
    plt.annotate(s='', xy=(0.48, -0.15), xytext=(0.48, 0.05),
                 arrowprops=dict(arrowstyle='<-'))
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()

    plt.show()
