import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection


def event_scheme(path):
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
    plt.savefig(path+'/event_scheme.pdf', bbox_inches='tight')



def plot_variables(var, back_to_back, three_gamma, phantom_scatt, det_scatt, prompt):
    sns.distplot(back_to_back[var], color="red", label="2g")
    sns.distplot(three_gamma[var], color="blue", label="3g")
    sns.distplot(phantom_scatt[var], color="green", label="phantom scatt")
    sns.distplot(det_scatt[var], color="c", label="det scatt")
    sns.distplot(prompt[var], color="skyblue", label="prompt")

def plot_comparison(path, back_to_back, three_gamma, phantom_scatt, det_scatt, prompt):
    plt.figure(figsize=(16, 6))
    plt.subplot(3, 2, 1)
    plot_variables("energy",back_to_back, three_gamma, phantom_scatt, det_scatt, prompt)
    plt.subplot(3, 2, 2)
    plot_variables("time",back_to_back, three_gamma, phantom_scatt, det_scatt, prompt)
    plt.subplot(3, 2, 3)
    plot_variables("hitX",back_to_back, three_gamma, phantom_scatt, det_scatt, prompt)
    plt.subplot(3, 2, 4)
    plot_variables("hitY",back_to_back, three_gamma, phantom_scatt, det_scatt, prompt)
    plt.subplot(3, 2, 5)
    plot_variables("hitZ",back_to_back, three_gamma, phantom_scatt, det_scatt, prompt)
    plt.legend(loc=(1.5,0))
    plt.savefig(path+'/variables_comparison.pdf', bbox_inches='tight')
