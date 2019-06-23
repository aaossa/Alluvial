import alluvial
import matplotlib.pyplot as plt
import matplotlib.cm as colormap


# Method to clean text from file
def clean(text):
    # Remove any undesired character
    text = text.replace("ï»¿", "")
    return text


# Load input data from file
input_data = []
with open("data.csv") as f:
    for line in f:
        line = clean(line)  # Using the line cleaning method
        line = line.strip().split(";")
        input_data.append(line)


# Get labels and sort them (optional)
a_elements = []
b_elements = []
for input_element in input_data:
    a_elements.append(input_element[0])
    b_elements.append(input_element[1])
a_elements = sorted(set(a_elements))
b_elements = sorted(set(b_elements), key=int)


# Generate plot
ax = alluvial.plot(
    input_data,  # Input data from file
    alpha=0.4,  # Transparency
    color_side=0,  # Where is the color assigned (left)
    disp_width=False,  # Display vein weight
    cmap=colormap.get_cmap('inferno'),  # Colormap
    a_sort=a_elements,  # Left labels order
    b_sort=b_elements,  # Right labels order
    labels=('Tipo', 'Valor'),  # Label description
    figsize=(7, 5),  # Figure size
    fontname='Monospace',  # Figure font
)
ax.set_title('Example 3', fontsize=20, fontname='Monospace')
plt.show()
