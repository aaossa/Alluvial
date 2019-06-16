# Alluvial

> Basado en [vinsburg/alluvial_diagram](https://github.com/vinsburg/alluvial_diagram)

Script (a convertir en módulo) para generar diagramas del tipo ["alluvial"](https://en.wikipedia.org/wiki/Alluvial_diagram), usando matplotlib y numpy.

## Usando el código

Para usar el código, copia `alluvial.py` en tu directorio de trabajo y sigue la sintaxis de los siguientes ejemplos. Ve la sección [Uso Avanzado](#uso-avanzado) para ver la documentación de los parámetros disponibles.

### Prerequisitos

* `matplotlib`
* `numpy`

### Instalación

Copia `alluvial.py` en tu directorio de trabajo.

## Ejemplos

### Ejemplo 1

```python
import alluvial
import matplotlib.pyplot as plt
import numpy as np

input_data = {'a': {'aa': 0.3, 'cc': 0.7,},
              'b': {'aa': 2, 'bb': 0.5,},
              'c': {'aa': 0.5, 'bb': 0.5, 'cc': 1.5,}}

ax = alluvial.plot(input_data)
fig = ax.get_figure()
fig.set_size_inches(5,5)
plt.show()
```

![Ejemplo 1](/image_examples/Example1.png)

### Ejemplo 2

```python
import alluvial
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np

# Generating the input_data:
seed=7
np.random.seed(seed)
def rand_letter(num): return chr(ord('A')+int(num*np.random.rand()))

input_data = [[rand_letter(15), rand_letter(5)*2] for _ in range(50)]

# Plotting:
cmap = matplotlib.cm.get_cmap('jet')
ax = alluvial.plot(
    input_data,  alpha=0.4, color_side=1, rand_seed=seed, figsize=(7,5),
    disp_width=True, wdisp_sep=' '*2, cmap=cmap, fontname='Monospace',
    labels=('Capitals', 'Double Capitals'), label_shift=2)
ax.set_title('Utility display', fontsize=14, fontname='Monospace')
plt.show()
```

![Ejemplo 2](/image_examples/Example2.png)

## Uso Avanzado

Formato de input adicional: Una lista de tuplas con la siguiente estructura:

```python
input_data = [
    ('a_item0', 'b_item0'),
    ('a_item0', 'b_item1'),
    ('a_item1', 'b_item0'),
]
```

La mejor forma de entender cómo funcionan los siguientes parámetros es probando distintos valores y viendo cómo cambian los gráficos de salida.

> Las venas (*veins*) son las líneas de algún color que unen ambos extremos del gráfico.

* `alpha=0.5`,  define el facecolor alpha para todas las venas (`float` entre `0` y `1`).
* `color_side=0`, color de las venas determinado por los términos de la izquieda (`0`) o los de la derecha (`1`). 
* `x_range=(0, 1)`, cambia las coordenadas horizontales del gráfico.
* `res=20`, determina el número de puntos que constituyen la ranura de la vena aluvial.
* `h_gap_frac=0.03`, cambia la separación horizontal entre las etiquetas, entre los rectángulos de la vena base y entre las venas.
* `v_gap_frac=0.03`, cambia la separación vertical entre las venas.
* `colors=None`, una lista opcional de [colores disponibles en `matplotlib`](https://stackoverflow.com/a/37232760/3281097). El largo de la lista debe ser igual al número de elementos en el lado determinado por `color_side`.
* `cmap=None`, una instancia de un *color map* de `matplotlib` ([`matplotlib.cm`](https://matplotlib.org/3.1.0/api/cm_api.html)) para elegir colores aleatorios. Si el valor es `None`, se utiliza `"hsv"`.
* `rand_seed=1`, la *seed* utilizada para el generador de colores aleatorios.
* `a_sort=None, b_sort=None`, listas definiendo el orden en el gráfico de los elementos de cada extremo. Si el valor es `None`, los elementos son ordenados según su ancho.
* `disp_width=False`, si es `True` se muestra el ancho de las venas junto a las etiquetas de los elementos.
* `wdisp_sep=7*' '`, si `disp_width` es `True` este es el ancho de la separación entre la etiqueta y el ancho del elemento.
* `width_in=True`, mostrar el ancho entre el texto del elemento y el gráfico. El orden se invierte si es `False`.
* `labels=None`, una tupla de la forma `("a_label", "b_label")` que corresponde a la descripción de las etiquetas. Si el valor es `None`, no se muestran estos valores.
* `figsize=(10, 15)`, el tamaño de la figura
* `fontname='Arial'`, la *font* de todo el texto de la figura.

---

## License

> This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details