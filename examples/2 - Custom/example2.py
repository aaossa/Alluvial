import alluvial
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np

# Generating the input_data:
SEED = 7
np.random.seed(SEED)


def rand_letter(num):
    return chr(ord('A')+int(num*np.random.rand()))


input_data = [
    [rand_letter(15), rand_letter(5)*2]
    for _ in range(50)
]

# Plotting:
cmap = matplotlib.cm.get_cmap('jet')
ax = alluvial.plot(
    input_data,  alpha=0.4, color_side=1, rand_seed=SEED, figsize=(7, 5),
    disp_width=True, wdisp_sep=' '*2, cmap=cmap, fontname='Monospace',
    labels=('Capitals', 'Double Capitals'), label_shift=2)
ax.set_title('Utility display', fontsize=14, fontname='Monospace')
plt.show()
