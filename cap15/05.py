# ---------------------------------------------------------------------------- #
#!          PLOTANDO E ESTILIZANDO PONTOS INDIVIDUAIS COM O SCATTER()          #
# ---------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

plt.style.use("ggplot")

fig, ax = plt.subplots()

ax.scatter(2, 4, s=200) # plota um unico ponto com x, y, "s" altera o tamanho


ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


ax.tick_params(labelsize=14)

plt.show()

