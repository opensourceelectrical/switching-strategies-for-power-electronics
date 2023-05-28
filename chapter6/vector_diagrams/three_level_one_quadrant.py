# This file generates the one quadrant of the vector diagram of a 3-phase 3-level converter

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
# level 0 - S3, S4 are ON
# level 1 - S2, S3 are ON
# level 2 - S1, S2 are ON
S_pattern = []
for count1 in range(3):
    for count2 in range(3):
        for count3 in range(3):
            S_pattern.append([count1, count2, count3])


def unbundle_levels(pattern, possible_levels):
    '''Translates ON/OFF value to dc voltage level'''
    return possible_levels[pattern]


S = []

# Translate the switching status to pole voltages
# Voltage between output of a leg and negative of dc bus
# For a 3-level converter, output can be 0, Vdc/2 or Vdc
for S_item in S_pattern:
    S_translate = [unbundle_levels(item, [0, 0.5, 1]) for item in S_item]
    S.append(S_translate)


def ln_volts(sw):
    '''Calculate line-neutral voltages from pole voltages'''
    return [
        (2/3)*sw[0] - (1/3)*sw[1] - (1/3)*sw[2],
        -(1/3)*sw[0] + (2/3)*sw[1] - (1/3)*sw[2],
        -(1/3)*sw[0] - (1/3)*sw[1] + (2/3)*sw[2]
    ]


# Calculate line-neutral voltages for each switching combination
V = [ln_volts(x) for x in S]


def abc_alphabeta(vabc):
    """Clarke's transformation"""
    return [
        (2/3) * (vabc[0] - 0.5*vabc[1] - 0.5*vabc[2]),
        (2/3) * math.sqrt(3)/2 * (vabc[1] - vabc[2])
    ]


# Transform line-neutral output voltages to alpha-beta domain
Valpha_beta = [abc_alphabeta(x) for x in V]

# For debugging purposes
# The vectors, the switch combinations and their alpha-beta values are printed.
print('Number of vectors = {}'.format(len(Valpha_beta)))
print('-'*80)
for x_count, x in enumerate(Valpha_beta):
    print('V{} - [{}, {}, {}] produces [{}, {}] = [{}, {}]'.format(
        x_count,
        S_pattern[x_count][0], S_pattern[x_count][1], S_pattern[x_count][2],
        x[0], x[1],
        math.sqrt(x[0]*x[0] + x[1]*x[1]), math.atan2(x[1], x[0])*180/math.pi
    )
    )
print('-'*80)

fig = plt.gcf()
ax = fig.gca()

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
# Except for those vectors in this list vectors_to_omit
# vectors_to_omit = [24, 18]
# vectors_to_omit = [9, 12]
vectors_to_omit = []
for vector_item in V_collection:
    skip_vector = False
    for vector_to_omit in vectors_to_omit:
        if vector_to_omit in vector_item[1]:
            skip_vector = True
            break
    if (not skip_vector) and (vector_item[0][0] or vector_item[0][1]):
        QV_item = plt.quiver(
            0, 0, vector_item[0][0], vector_item[0][1], angles='xy', scale_units='xy', scale=1)
        QVs.append(QV_item)
        vector_string_items = [
            r'$\overline{V}_{' + str(v_index) + r'}$' for v_index in vector_item[1]]
        vector_string = ','.join(vector_string_items)
        vector_angle = math.atan2(
            vector_item[0][1], vector_item[0][0]) * 180/math.pi
        offsetx = 0
        offsety = 0
        if abs(vector_angle) > 58 and abs(vector_angle) < 62:
            label_pos = 'E'
        elif abs(vector_angle) > 118 and abs(vector_angle) < 122:
            label_pos = 'W'
        elif abs(vector_angle) > 28 and abs(vector_angle) < 32:
            label_pos = 'E'
        elif abs(vector_angle) > 148 and abs(vector_angle) < 152:
            label_pos = 'W'
        elif abs(vector_angle) > 88 and abs(vector_angle) < 92:
            label_pos = 'W'
        else:
            label_pos = 'S'
        # Adjusting the labels on a few vectors
        if 15 in vector_item[1]:
            label_pos = 'N'
        if 12 in vector_item[1]:
            offsetx = 0.005
            offsety = 0.025
        if 9 in vector_item[1]:
            offsetx = 0.005
            offsety = 0.025
            label_pos = 'E'
        if 18 in vector_item[1]:
            label_pos = 'E'
        if vector_item[0][0] > -0.1 and vector_item[0][1] > -0.1:
            plt.quiverkey(QV_item, vector_item[0][0]+offsetx, vector_item[0][1]+offsety,
                          0, vector_string, coordinates='data', visible=False, labelpos=label_pos)

# Dashed lines to create triangles with voltage vectors
lines_between_vectors = [
    [9, 10], [9, 12], [12, 3], [9, 21], [12, 21], [12, 15],
    [18, 21], [21, 24], [24, 15], [15, 6], [18, 19]
]
for line_between_vectors in lines_between_vectors:
    if line_between_vectors[0] not in vectors_to_omit and line_between_vectors[1] not in vectors_to_omit:
        plt.plot([Valpha_beta[line_between_vectors[0]][0], Valpha_beta[line_between_vectors[1]][0]], [
                 Valpha_beta[line_between_vectors[0]][1], Valpha_beta[line_between_vectors[1]][1]], lw=2, ls='--', color='black')

# Adding circular trajectories for output voltage vectors
circle1 = plt.Circle((0, 0), 0.5, ls='--', fill=False)
ax.add_patch(circle1)

circle2 = plt.Circle((0, 0), 0.2, ls='--', fill=False)
ax.add_patch(circle2)

plt.xlim([-0.1, 0.75])
plt.xticks([0, 0.6])
plt.ylim([-0.1, 0.65])
plt.yticks([0, 0.6])

plt.title("Converter voltage vectors")
plt.xlabel(r"$v_{\alpha}$")
plt.ylabel(r"$v_{\beta}$")
plt.tight_layout()
plt.axes().set_aspect('equal')
plt.savefig("fig1.eps", format="eps")

plt.show()
