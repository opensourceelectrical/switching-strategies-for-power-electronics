# This file is to generate a vector diagram for the line-line
# output voltages of a three-phase three-leg converter

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

font = {
    "family": "normal",
    "weight": "normal",
    "size": 12
}
matplotlib.rc("font", **font)

# defining switching combinations
S1 = [1, 0, 0]
S2 = [0, 1, 0]
S3 = [0, 0, 1]
S4 = [0, 1, 1]
S5 = [1, 0, 1]
S6 = [1, 1, 0]
S = [S1, S2, S3, S4, S5, S6]


def ln_volts(sw):
    '''Calculating three-phase L-L output voltages for a switching combination'''
    return [
        sw[0] - sw[1],
        sw[1] - sw[2],
        sw[2] - sw[0]
    ]


# Calculating line-neutral output voltages for all switching combinations
V = [ln_volts(x) for x in S]


def abc_alphabeta(vabc):
    """Clarke's transformation"""
    return [
        (2/3) * (vabc[0] - 0.5*vabc[1] - 0.5*vabc[2]),
        (2/3) * math.sqrt(3)/2 * (vabc[1] - vabc[2])
    ]


# Calculating transformed output voltages for all switching combinations
Valpha_beta = [abc_alphabeta(x) for x in V]

# Separating into vectors
V1 = Valpha_beta[0]
V2 = Valpha_beta[1]
V3 = Valpha_beta[2]
V4 = Valpha_beta[3]
V5 = Valpha_beta[4]
V6 = Valpha_beta[5]

plt.figure()

# using quiver to draw an arrow - originx, originy, pointx, pointy
QV1 = plt.quiver(0, 0, V1[0], V1[1], angles='xy', scale_units='xy', scale=1)
QV2 = plt.quiver(0, 0, V2[0], V2[1], angles='xy', scale_units='xy', scale=1)
QV3 = plt.quiver(0, 0, V3[0], V3[1], angles='xy', scale_units='xy', scale=1)
QV4 = plt.quiver(0, 0, V4[0], V4[1], angles='xy', scale_units='xy', scale=1)
QV5 = plt.quiver(0, 0, V5[0], V5[1], angles='xy', scale_units='xy', scale=1)
QV6 = plt.quiver(0, 0, V6[0], V6[1], angles='xy', scale_units='xy', scale=1)

# using quiverkey to create a label for each quiver vector
plt.quiverkey(QV1, V1[0], V1[1], 0,
              r'$\overline{V}_{1}(1, 0, 0)$', coordinates='data', visible=False, labelpos='E')
plt.quiverkey(QV2, V2[0], V2[1], 0,
              r'$\overline{V}_{2}(0, 1, 0)$', coordinates='data', visible=False, labelpos='W')
plt.quiverkey(QV3, V3[0], V3[1], 0,
              r'$\overline{V}_{3}(0, 0, 1)$', coordinates='data', visible=False, labelpos='W')
plt.quiverkey(QV4, V4[0], V4[1], 0,
              r'$\overline{V}_{4}(0, 1, 1)$', coordinates='data', visible=False, labelpos='W')
plt.quiverkey(QV5, V5[0], V5[1], 0,
              r'$\overline{V}_{5}(1, 0, 1)$', coordinates='data', visible=False, labelpos='E')
plt.quiverkey(QV6, V6[0], V6[1], 0,
              r'$\overline{V}_{6}$(1, 1, 0)', coordinates='data', visible=False, labelpos='N')

plt.xlim([-2.0, 2.0])
plt.xticks([-1.5, 0, 1.5])
plt.ylim([-1.5, 1.5])
plt.yticks([-1.5, 0, 1.5])

plt.title("Converter voltage vectors")
plt.xlabel(r"$v_{\alpha}$")
plt.ylabel(r"$v_{\beta}$")
plt.tight_layout()
plt.axes().set_aspect('equal')
plt.savefig("fig2.eps", format="eps")

plt.show()
