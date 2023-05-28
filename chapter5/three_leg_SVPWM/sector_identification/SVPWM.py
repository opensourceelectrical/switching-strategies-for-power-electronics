# This is a gate generator file for a three-phase three-leg converter
# Space Vector Pulse Width Modulation (SVPWM) is used
# The reference voltage is obtained externally to this file
# In this file, the sector is identified in which the output vector is located
# Knowing the sector the vectors and their sequence are identified

import math
from math import sin, pi

# Switching frequency of 2.5KHz
sw_freq = 2500.0
T_sw = 1 / sw_freq

# Carrier waveform is only for illustrative purposes
# To be able to plot the gate signals with the carrier waveform
# To mark the beginning and end of switching cycles
carr_slope_mag = 4.0 * sw_freq

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:  # t_clock is an internal variable

    # Carrier Signal Generation
    if not carr_slope:
        carr_slope = carr_slope_mag

    carr_signal += carr_slope * dt

    # Changing slope at the limits
    if carr_signal >= 1.0:
        carr_slope = -carr_slope_mag

    if carr_signal <= -1.0:
        carr_slope = carr_slope_mag

    # The sequence counter marks the vector that is currently being generated
    # It is initialized to -1 at the beginning of the simulation
    # And also at the end of every switching cycle
    # This negative value can be used to determine the beginning of a new switching cycle
    # At the beginning of a new switching cycle, the new reference output voltage is extracted
    # and kept constant for the rest of the switching cycle
    if sequence_counter < 0:
        mod_signal_alpha = ref_volt_alpha
        mod_signal_beta = ref_volt_beta

    # Sector Selection
    # Refer to vector diagram generator files in vector_diagrams folder
    if (mod_signal_alpha > 0):
        if (mod_signal_beta >= 0):
            if (mod_signal_beta < 1.732 * mod_signal_alpha):
                sec = 1
            else:
                sec = 2
        else:
            if (mod_signal_beta < -1.732 * mod_signal_alpha):
                sec = 5
            else:
                sec = 6
    elif (mod_signal_alpha < 0):
        if (mod_signal_beta >= 0):
            if (mod_signal_beta < -1.732 * mod_signal_alpha):
                sec = 3
            else:
                sec = 2
        else:
            if (mod_signal_beta < 1.732 * mod_signal_alpha):
                sec = 5
            else:
                sec = 4
    else:
        if (mod_signal_beta > 0):
            sec = 2
        else:
            sec = 5

    # Vector Definitions
    # Zero vectors
    V_0 = [0, 0, 0]
    V_7 = [1, 1, 1]
    # Non-zero vectors
    # Sequence in counter-clockwise sense
    # For sequence, checkout vector diagram generator files in vector_diagrams folder
    V_1to6 = [[1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1], [1, 0, 1]]
    # Real and imaginary part of each non-zero vector in alpha-beta plane
    V_alpha = [1, 0.5, -0.5, -1, -0.5, 0.5]  # Real Part
    V_beta = [0, 0.866, 0.866, 0, -0.866, -0.866]  # Imaginary Part

    # Vector Selection from sector information
    if (sec % 2 == 1):
        index_x = sec - 1
        index_y = sec % 6
    else:
        index_x = sec % 6
        index_y = sec - 1

    # V_x and V_y are the two non-zero vectors in every sector
    V_x = V_1to6[index_x]
    V_y = V_1to6[index_y]
    V_x_alpha = V_alpha[index_x]
    V_y_alpha = V_alpha[index_y]
    V_x_beta = V_beta[index_x]
    V_y_beta = V_beta[index_y]

    # Timing Calculation
    T_x = (V_y_beta * mod_signal_alpha - V_y_alpha * mod_signal_beta) / (
        V_x_alpha * V_y_beta - V_y_alpha * V_x_beta) * T_sw / 2
    T_y = (V_x_beta * mod_signal_alpha - V_x_alpha * mod_signal_beta) / (
        V_y_alpha * V_x_beta - V_x_alpha * V_y_beta) * T_sw / 2
    if (2 * (T_x + T_y) < T_sw):
        T_n = (T_sw - 2 * (T_x + T_y)) / 4
    else:
        T_n = 0.0

    # Timing Sequence Generation
    t_seq = [
        T_n,  # zero vector
        T_x,  # zero + Vx
        T_y,  # zero + Vx + Vy
        2 * T_n,  # zero (V0) + Vx + Vy + 2 zero (V7)
        T_y,  # zero (V0) + Vx + Vy + 2zero (V7) + Vy
        T_x,  # zero (V0) + Vx + Vy + 2zero (V7) + Vy + Vx
        T_n  # zero (V0) + Vx + Vy + 2zero (V7) + Vy + Vx + zero (V0)
    ]

    # Initialization at start of every switching cycle
    if (sequence_counter < 0):
        sequence_counter = 0
        # t2 is a time event variable that has the running value of the pulse width
        t2 += t_seq[0]

    if sequence_counter == 0:
        s1_gate = V_0[0]
        s3_gate = V_0[1]
        s5_gate = V_0[2]
    elif sequence_counter == 1:
        s1_gate = V_x[0]
        s3_gate = V_x[1]
        s5_gate = V_x[2]
    elif sequence_counter == 2:
        s1_gate = V_y[0]
        s3_gate = V_y[1]
        s5_gate = V_y[2]
    elif sequence_counter == 3:
        s1_gate = V_7[0]
        s3_gate = V_7[1]
        s5_gate = V_7[2]
    elif sequence_counter == 4:
        s1_gate = V_y[0]
        s3_gate = V_y[1]
        s5_gate = V_y[2]
    elif sequence_counter == 5:
        s1_gate = V_x[0]
        s3_gate = V_x[1]
        s5_gate = V_x[2]
    elif sequence_counter == 6:
        s1_gate = V_0[0]
        s3_gate = V_0[1]
        s5_gate = V_0[2]

    if t_clock >= t2:
        # When a particular vector's time expires
        # Pick the next vector in the sequence
        # And update t2 with the time corresponding to new vector
        sequence_counter += 1
        if sequence_counter <= 6:
            t2 += t_seq[sequence_counter]
        else:
            # If all vectors are dealt with, set sequence counter negative
            # to mark end of switching cycle
            sequence_counter = -1

    # Lower devices are complimentary to upper devices
    s2_gate = not (s1_gate)
    s4_gate = not (s3_gate)
    s6_gate = not (s5_gate)

    # Data storage
    pwm_carr_signal = carr_signal

    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate
    pwm_s3_gate = s3_gate
    pwm_s4_gate = s4_gate
    pwm_s5_gate = s5_gate
    pwm_s6_gate = s6_gate

    pwm_sector = sec

    pwm_vec1_t1 = T_x
    pwm_vec2_t2 = T_y
    pwm_vec0_t0 = T_n

    # Time increment
    t1 += dt
