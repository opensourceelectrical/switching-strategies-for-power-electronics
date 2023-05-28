# This file is to generate a vector diagram for the line-neutral
# output voltages of a three-phase three-leg converter
# And plot circular voltage trajectories and sample output voltages

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
    '''Calculating three-phase L-N output voltages for a switching combination'''
    return [
        (2/3)*sw[0] - (1/3)*sw[1] - (1/3)*sw[2],
        -(1/3)*sw[0] + (2/3)*sw[1] - (1/3)*sw[2],
        -(1/3)*sw[0] - (1/3)*sw[1] + (2/3)*sw[2]
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

fig = plt.gcf()
ax = fig.gca()

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
              r'$\overline{V}_{2}$(0, 1, 0)', coordinates='data', visible=False)
plt.quiverkey(QV3, V3[0], V3[1], 0,
              r'$\overline{V}_{3}(0, 0, 1)$', coordinates='data', visible=False, labelpos='S')
plt.quiverkey(QV4, V4[0], V4[1], 0,
              r'$\overline{V}_{4}$(0, 1, 1)', coordinates='data', visible=False, labelpos='W')
plt.quiverkey(QV5, V5[0], V5[1], 0,
              r'$\overline{V}_{5}(1, 0, 1)$', coordinates='data', visible=False, labelpos='S')
plt.quiverkey(QV6, V6[0], V6[1], 0,
              r'$\overline{V}_{6}(1, 1, 0)$', coordinates='data', visible=False)

plt.xlim([-1.25, 1.25])
plt.xticks([-0.75, 0, 0.75])
plt.ylim([-1, 1])
plt.yticks([-0.75, 0, 0.75])

# Assume the required output voltages to have magnitude vomag
vomag = 0.3

# Output voltage will be a vector which occupies various positions on a circle
circle1 = plt.Circle((0, 0), vomag, ls='--', fill=False)
ax.add_patch(circle1)

# Take a sample value of the output voltage vector
Vo1 = [vomag*math.cos(30*math.pi/180), vomag*math.sin(30*math.pi/180)]
# Plot it on same vector diagram
QVo1 = plt.quiver(0, 0, Vo1[0], Vo1[1], angles='xy', scale_units='xy', scale=1)
plt.quiverkey(QVo1, Vo1[0], Vo1[1], 0,
              r'$\overline{V}_{r1}$', coordinates='data', visible=False, labelpos='E', labelsep=0.15)

# Take another sample value of the output voltage vector
Vo2 = [vomag*math.cos(260*math.pi/180), vomag*math.sin(260*math.pi/180)]
# Plot it on same vector diagram
QVo2 = plt.quiver(0, 0, Vo2[0], Vo2[1], angles='xy', scale_units='xy', scale=1)
plt.quiverkey(QVo2, Vo2[0], Vo2[1], 0,
              r'$\overline{V}_{r2}$', coordinates='data', visible=False, labelpos='S', labelsep=0.15)

# Plot the maximum and minimum beta values for the first sample vector
# to show the limits of a sector
plt.plot([Vo1[0], Vo1[0]], [0, Vo1[1]], lw=2, ls='--', color='black')
plt.plot([Vo1[0], Vo1[0]], [-Vo1[0]*math.tan(60*math.pi/180), Vo1[0]
         * math.tan(60*math.pi/180)], lw=2, ls='--', color='black')

# Label these max and min beta values
plt.text(Vo1[0]-0.15, -0.075, r'$v_{r \alpha}$')
plt.text(Vo1[0]+0.025, Vo1[0]*math.tan(60*math.pi/180) -
         0.05, r'$v_{r \beta max}$')
plt.text(Vo1[0]+0.025, -Vo1[0]*math.tan(60*math.pi/180), r'$v_{r \beta min}$')

plt.title("Converter voltage vectors")
plt.xlabel(r"$v_{\alpha}$")
plt.ylabel(r"$v_{\beta}$")
plt.tight_layout()
plt.axes().set_aspect('equal')
plt.savefig("fig1.eps", format="eps")

plt.show()
