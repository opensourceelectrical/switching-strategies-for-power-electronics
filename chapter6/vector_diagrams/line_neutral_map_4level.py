# This file generates the vector diagram of a 3-phase 4-level converter

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

# Create switching patterns for the three converter legs
# level 0 - S4, S5, S6 are ON
# level 1 - S3, S4, S5 are ON
# level 2 - S2, S3, S4 are ON
# level 2 - S1, S2, S3 are ON
S_pattern = []
for count1 in range(4):
    for count2 in range(4):
        for count3 in range(4):
            S_pattern.append([count1, count2, count3])


def unbundle_levels(pattern, possible_levels):
    '''Translates ON/OFF value to dc voltage level'''
    return possible_levels[pattern]


S = []
# Translate the switching status to pole voltages
# Voltage between output of a leg and negative of dc bus
# For a 4-level converter, output can be 0, Vdc/3, 2Vdc/3 or Vdc
for S_item in S_pattern:
    S_translate = [unbundle_levels(item, [0, 0.333, 0.6667, 1])
                   for item in S_item]
    S.append(S_translate)


def ln_volts(sw):
    '''Calculate line-neutral voltages from pole voltages'''
    return [
        (2/3)*sw[0] - (1/3)*sw[1] - (1/3)*sw[2],
        -(1/3)*sw[0] + (2/3)*sw[1] - (1/3)*sw[2],
        -(1/3)*sw[0] - (1/3)*sw[1] + (2/3)*sw[2]
    ]


V = [ln_volts(x) for x in S]


def abc_alphabeta(vabc):
    return [
        (2/3) * (vabc[0] - 0.5*vabc[1] - 0.5*vabc[2]),
        (2/3) * math.sqrt(3)/2 * (vabc[1] - vabc[2])
    ]


# Calculate line-neutral voltages for each switching combination
Valpha_beta = [abc_alphabeta(x) for x in V]

plt.figure()

# Extract the unique vectors from the complete list
QVs = []
V_collection = []
for V_count, V_alpha_beta_item in enumerate(Valpha_beta):
    if len(V_collection) > 0:
        vector_found = False
        for V_exist in V_collection:
            if abs(V_alpha_beta_item[0] - V_exist[0][0]) < 0.01 and abs(V_alpha_beta_item[1] - V_exist[0][1]) < 0.01:
                vector_found = True
                V_exist[1].append(V_count)
                break
        if not vector_found:
            V_collection.append([V_alpha_beta_item, [V_count,]])
    else:
        V_collection.append([V_alpha_beta_item, [V_count,]])

# Plot these unique vectors
for vector_item in V_collection:
    if vector_item[0][0] or vector_item[0][1]:
        # Vector is drawn only for the unique vector
        QV_item = plt.quiver(
            0, 0, vector_item[0][0], vector_item[0][1], angles='xy', scale_units='xy', scale=1)
        QVs.append(QV_item)
        # Label each vector with all the vectors that exist in that position
        vector_string_items = [
            r'$\overline{V}_{' + str(v_index+1) + r'}$' for v_index in vector_item[1]]
        # For clarity in display, more than 2 vectors at a location are not labeled
        if len(vector_string_items) < 2:
            vector_string = ','.join(vector_string_items)
        else:
            vector_string = ''
        # vector_string = ','.join(vector_string_items)
        vector_angle = math.atan2(
            vector_item[0][1], vector_item[0][0]) * 180/math.pi
        if abs(vector_angle) > 58 and abs(vector_angle) < 62:
            label_pos = 'E'
        elif abs(vector_angle) > 28 and abs(vector_angle) < 32:
            label_pos = 'E'
        elif abs(vector_angle) > 118 and abs(vector_angle) < 122:
            label_pos = 'W'
        elif abs(vector_angle) > 148 and abs(vector_angle) < 152:
            label_pos = 'W'
        elif vector_angle < -78 and vector_angle > -82:
            label_pos = 'S'
        elif vector_angle < -98 and vector_angle > -102:
            label_pos = 'S'
        else:
            label_pos = 'N'
        plt.quiverkey(QV_item, vector_item[0][0], vector_item[0][1], 0,
                      vector_string, coordinates='data', visible=False, labelpos=label_pos)

plt.xlim([-0.75, 0.75])
plt.xticks([-0.6, 0, 0.6])
plt.ylim([-0.75, 0.75])
plt.yticks([-0.6, 0, 0.6])

plt.title("Converter voltage vectors")
plt.xlabel(r"$v_{\alpha}$")
plt.ylabel(r"$v_{\beta}$")
plt.tight_layout()
plt.axes().set_aspect('equal')
plt.savefig("fig1.eps", format="eps")

plt.show()
