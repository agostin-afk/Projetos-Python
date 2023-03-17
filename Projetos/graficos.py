import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(10, 10)
circle = plt.Circle((0.6, 0.6), 0.3, fill=False)
axes.set_aspect(1)
axes.add_artist(circle)
plt.title('Teste')
plt.show()
