# This file is to generate a vector diagram for the line-neutral
# output voltages of a three-phase three-leg converter
# And shows the capacity of a converter

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
              r'$\overline{V}_{1}(1, 0, 0)$', coordinates='data', labelpos='E', visible=False, labelsep=0.15)
plt.quiverkey(QV2, V2[0], V2[1], 0,
              r'$\overline{V}_{2}$(0, 1, 0)', coordinates='data', visible=False, labelsep=0.25)
plt.quiverkey(QV3, V3[0], V3[1], 0,
              r'$\overline{V}_{3}(0, 0, 1)$', coordinates='data', labelpos='S', visible=False, labelsep=0.25)
plt.quiverkey(QV4, V4[0], V4[1], 0,
              r'$\overline{V}_{4}$(0, 1, 1)', coordinates='data', labelpos='W', visible=False, labelsep=0.15)
plt.quiverkey(QV5, V5[0], V5[1], 0,
              r'$\overline{V}_{5}(1, 0, 1)$', coordinates='data', labelpos='S', visible=False, labelsep=0.25)
plt.quiverkey(QV6, V6[0], V6[1], 0,
              r'$\overline{V}_{6}(1, 1, 0)$', coordinates='data', visible=False, labelsep=0.25)

plt.xlim([-1.25, 1.25])
plt.xticks([-0.75, 0, 0.75])
plt.ylim([-1, 1])
plt.yticks([-0.75, 0, 0.75])

# Assume the required output voltages to have magnitude vomag
vomag = 0.3

# Output voltage will be a vector which occupies various positions on a circle
# This trajectory will lie within the vector hexagon
circle1 = plt.Circle((0, 0), vomag, ls='--', fill=False)
ax.add_patch(circle1)

# Join the edges of the vectors to form a hexagon
plt.plot([V1[0], V6[0]], [V1[1], V6[1]], lw=2, color='black')
plt.plot([V6[0], V2[0]], [V6[1], V2[1]], lw=2, color='black')
plt.plot([V2[0], V4[0]], [V2[1], V4[1]], lw=2, color='black')
plt.plot([V4[0], V3[0]], [V4[1], V3[1]], lw=2, color='black')
plt.plot([V3[0], V5[0]], [V3[1], V5[1]], lw=2, color='black')
plt.plot([V5[0], V1[0]], [V5[1], V1[1]], lw=2, color='black')

# Take a sample output voltage with magnitude equal
# to the mangitude of one of the converter voltage vectors
conv_volt_mag = math.sqrt(V1[0]*V1[0] + V1[1]*V1[1])
# This trajectors will lie outside the vector hexagon
circle2 = plt.Circle((0, 0), conv_volt_mag, ls='--', fill=False)
ax.add_patch(circle2)

# Converter limit circle
# circle3 = plt.Circle((0, 0), conv_volt_mag*math.cos(30*math.pi/180.0), ls='--', fill=False)
# ax.add_patch(circle3)

# Instead of plotting a circle, a scatter plot with actual references can be used below

T_cycle = 1/50      # For 50 Hz grid. Change if different
t_sample = 0.0005   # Sampling time interval for generating data points
no_of_points = int(T_cycle / t_sample)
grid_w = 2 * math.pi * 50       # Grid angular frequency
# Time array for data points
t_array = [t_sample*i for i in range(no_of_points)]

# Set a magnitude of output voltage magnitude to check if it can be produced
# As an example, this magnitude is set to the limit of the converter
# But it can be set to anything to see if converter can produce it without saturation
check_output_volt_mag = conv_volt_mag*math.cos(30*math.pi/180)
# Generate phase a,b,c voltages with this magnitude
vra = [check_output_volt_mag * math.cos(grid_w*td) for td in t_array]
vrb = [check_output_volt_mag *
       math.cos(grid_w*td - 120*math.pi/180) for td in t_array]
vrc = [check_output_volt_mag *
       math.cos(grid_w*td - 240*math.pi/180) for td in t_array]
vrabc = [[vra[i], vrb[i], vrc[i]] for i in range(no_of_points)]
# Clarke's tranformation
Vralpha_beta = [abc_alphabeta(x) for x in vrabc]
Vralpha = [volt_item[0] for volt_item in Vralpha_beta]
Vrbeta = [volt_item[1] for volt_item in Vralpha_beta]
# Scatter plot generates a sequence of dots which shows the trajectory
# of a single cycle of the required output voltage
plt.scatter(Vralpha, Vrbeta, marker='.', color='black')

Vo1 = [V1[0]*math.cos(30*math.pi/180), V1[0]*math.tan(30*math.pi/180)]
QVo1 = plt.quiver(0, 0, Vo1[0], Vo1[1], angles='xy', scale_units='xy', scale=1)
plt.quiverkey(QVo1, Vo1[0], Vo1[1], 0,
              r'$\overline{V}_{r1}$', coordinates='data', labelpos='E', visible=False, labelsep=0.15)

Vo2 = [0, conv_volt_mag*math.cos(30*math.pi/180)]
QVo2 = plt.quiver(0, 0, Vo2[0], Vo2[1], angles='xy', scale_units='xy', scale=1)
plt.quiverkey(QVo2, Vo2[0], Vo2[1], 0,
              r'       $\overline{V}_{r2}$', coordinates='data', visible=False, labelpos='S')

plt.title("Converter voltage vectors")
plt.xlabel(r"$v_{\alpha}$")
plt.ylabel(r"$v_{\beta}$")
plt.tight_layout()
plt.axes().set_aspect('equal')
plt.savefig("fig1.eps", format="eps")

plt.show()
