import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2,2 ,figsize=(9,9))
'''
fig.subplots_adjust( wspace = 0.5, hspace = 0.3,
                    left = 0.125, right = 0.9,
                    top = 0.9, bottom = 0.1)
'''
plt.show()


def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=16)
    ax.set_ylabel('y-label', fontsize=8)
    ax.set_title('Title', fontsize=24)
    
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)
plt.tight_layout()
'''
fig.subplots_adjust( wspace = 0.5, hspace = 0.3,
                    left = 0.125, right = 0.9,
                    top = 0.9, bottom = 0.1)
'''
plt.show()