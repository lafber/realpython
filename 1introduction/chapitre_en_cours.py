''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''

import matplotlib
matplotlib.use('Agg') # non-interactive backend and use SVG
import matplotlib.pyplot as plt

from numpy import random

plt.hist(random.randn(10000), 20)

plt.annotate("expected mean", xy=(0, 0), xytext=(0, 300), ha="center",
    arrowprops=dict(facecolor='black'), fontsize=20)

plt.savefig('graph.svg')