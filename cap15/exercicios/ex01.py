# ---------------------------------------------------------------------------- #
#!                                 15.1 Cubos                                  #
# ---------------------------------------------------------------------------- #

# Um número elevado a terceira potencia se chama cubo.

# Plote os primeiros 5 numeros cubicos e, em seguida, plote os primeiros 5000 numeros cubicos

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)
ax.ticklabel_format(style='plain') 

plt.show()