# This is a gate generator file for a three-phase three-level converter
# Space Vector Pulse Width Modulation (SVPWM) is used
# The reference voltage is obtained externally to this file

from math import sin, cos, pi

# Switching frequency of 2.5KHz
sw_freq = 2500.0
T_sw = 1 / sw_freq

# Carrier waveform is only to identify begin and end
# of switching cycles when plotting gate signals
carr_slope_mag = 4.0 * sw_freq

# Sampling time interval
dt = 1.0e-6

# Reference value of the dc bus voltage
dc_cap_volt_ref = 12    # Volts

if t_clock > t1:  # t_clock is an internal variable

    # Carrier Signal Generation
    if not carr_slope:
        carr_slope = carr_slope_mag
        carr_signal = -1

    carr_signal += carr_slope * dt
    # carr_signal_ps += carr_slope_ps * dt

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
        mod_signal_alpha = round(ref_volt_alpha, 4)
        mod_signal_beta = round(ref_volt_beta, 4)

    # Balancing the dc bus capacitors
    if not balancing_status:
        # Initially, when deviation crosses an upper limit
        # status is 1 and when it crosses a lower limit
        # it is set to -1
        if vc1 > vc2 and vc1 - vc2 > 0.01*dc_cap_volt_ref:
            balancing_status = 1.0
        elif vc1 < vc2 and vc2 - vc1 > 0.01*dc_cap_volt_ref:
            balancing_status = -1.0
    else:
        # If the upper capacitor is charging
        # look for the deviation to cross lower limit
        if balancing_status > 0:
            if vc1 < vc2 and vc2 - vc1 > 0.01*dc_cap_volt_ref:
                balancing_status = -1.0
            else:
                balancing_status = 1.0
        else:
            # If the lower capacitor is charging
            # look for deviation to cross upper limit
            if vc1 > vc2 and vc1 - vc2 > 0.01*dc_cap_volt_ref:
                balancing_status = 1.0
            else:
                balancing_status = -1.0

    # Vector Selection %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    if (mod_signal_alpha >= 0 and mod_signal_beta >= 0):  # First Quadrant

        if (mod_signal_alpha <= 0.1666):
            if (mod_signal_beta <= (1.7320 * mod_signal_alpha)):
                index_1 = 0
                index_2 = 9
                index_3 = 12
                index_4 = 13
            elif (mod_signal_beta <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 3
                    index_3 = 12
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 16
                    index_3 = 25
                    index_4 = 26
            elif (mod_signal_beta <= (0.2887 + (0.1666 - mod_signal_alpha) * 1.7320)):
                index_1 = 3
                index_2 = 12
                index_3 = 15
                index_4 = 16
            else:
                index_1 = 12
                index_2 = 15
                index_3 = 24
                index_4 = 25
        elif (mod_signal_alpha <= 0.3333):
            if (mod_signal_beta <= (0.3333 - mod_signal_alpha) * 1.7320):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 9
                    index_3 = 12
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 22
                    index_3 = 25
                    index_4 = 26
            elif (mod_signal_beta <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 9
                    index_2 = 12
                    index_3 = 21
                    index_4 = 22
                else:
                    index_1 = 25
                    index_2 = 22
                    index_3 = 21
                    index_4 = 12
            elif (mod_signal_beta <= (1.7320 * mod_signal_alpha)):
                index_1 = 12
                index_2 = 21
                index_3 = 24
                index_4 = 25
            else:
                index_1 = 12
                index_2 = 15
                index_3 = 24
                index_4 = 25
        elif (mod_signal_alpha <= 0.5000):
            if (mod_signal_beta <= (mod_signal_alpha - 0.3333) * 1.7320):
                index_1 = 9
                index_2 = 18
                index_3 = 21
                index_4 = 22
            elif (mod_signal_beta <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 9
                    index_2 = 12
                    index_3 = 21
                    index_4 = 22
                else:
                    index_1 = 25
                    index_2 = 22
                    index_3 = 21
                    index_4 = 12
            else:
                index_1 = 12
                index_2 = 21
                index_3 = 24
                index_4 = 25
        else:
            index_1 = 9
            index_2 = 18
            index_3 = 21
            index_4 = 22
    elif (mod_signal_alpha <= 0 and mod_signal_beta >= 0):  # Second Quadrant

        if (abs(mod_signal_alpha) <= 0.1666):
            if (mod_signal_beta <= (1.7320 * abs(mod_signal_alpha))):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 3
                    index_3 = 4
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 16
                    index_3 = 17
                    index_4 = 26
            elif (mod_signal_beta <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 3
                    index_3 = 12
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 16
                    index_3 = 25
                    index_4 = 26
            elif (mod_signal_beta <= (0.2887 + (0.1666 - abs(mod_signal_alpha)) * 1.7320)):
                if balancing_status <= 0:
                    index_1 = 3
                    index_2 = 12
                    index_3 = 15
                    index_4 = 16
                else:
                    index_1 = 25
                    index_2 = 16
                    index_3 = 15
                    index_4 = 12
            else:
                index_1 = 3
                index_2 = 6
                index_3 = 15
                index_4 = 16
        elif (abs(mod_signal_alpha) <= 0.3333):
            if (mod_signal_beta <= (0.3333 - abs(mod_signal_alpha)) * 1.7320):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 3
                    index_3 = 4
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 16
                    index_3 = 17
                    index_4 = 26
            elif (mod_signal_beta <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 3
                    index_2 = 4
                    index_3 = 7
                    index_4 = 16
                else:
                    index_1 = 17
                    index_2 = 16
                    index_3 = 7
                    index_4 = 4
            elif (mod_signal_beta <= (1.7320 * abs(mod_signal_alpha))):
                index_1 = 3
                index_2 = 6
                index_3 = 7
                index_4 = 16
            else:
                index_1 = 3
                index_2 = 6
                index_3 = 15
                index_4 = 16
        elif (abs(mod_signal_alpha) <= 0.5000):
            if (mod_signal_beta <= (abs(mod_signal_alpha) - 0.3333) * 1.7320):
                index_1 = 4
                index_2 = 7
                index_3 = 8
                index_4 = 17
            elif (mod_signal_beta <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 3
                    index_2 = 4
                    index_3 = 7
                    index_4 = 16
                else:
                    index_1 = 17
                    index_2 = 16
                    index_3 = 7
                    index_4 = 4
            else:
                index_1 = 3
                index_2 = 6
                index_3 = 7
                index_4 = 16
        else:
            index_1 = 4
            index_2 = 7
            index_3 = 8
            index_4 = 17
    elif (mod_signal_alpha <= 0 and mod_signal_beta <= 0):  # Third Quadrant

        if (abs(mod_signal_alpha) <= 0.1666):
            if (abs(mod_signal_beta) <= (1.7320 * abs(mod_signal_alpha))):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 1
                    index_3 = 4
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 14
                    index_3 = 17
                    index_4 = 26
            elif (abs(mod_signal_beta) <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 1
                    index_3 = 10
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 14
                    index_3 = 23
                    index_4 = 26
            elif (abs(mod_signal_beta) <= (0.2887 + (0.1666 - abs(mod_signal_alpha)) * 1.7320)):
                index_1 = 1
                index_2 = 10
                index_3 = 11
                index_4 = 14
            else:
                index_1 = 1
                index_2 = 2
                index_3 = 11
                index_4 = 14
        elif (abs(mod_signal_alpha) <= 0.3333):
            if (abs(mod_signal_beta) <= (0.3333 - abs(mod_signal_alpha)) * 1.7320):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 1
                    index_3 = 4
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 14
                    index_3 = 17
                    index_4 = 26
            elif (abs(mod_signal_beta) <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 1
                    index_2 = 4
                    index_3 = 5
                    index_4 = 14
                else:
                    index_1 = 17
                    index_2 = 14
                    index_3 = 5
                    index_4 = 4
            elif (abs(mod_signal_beta) <= (1.7320 * abs(mod_signal_alpha))):
                index_1 = 1
                index_2 = 2
                index_3 = 5
                index_4 = 14
            else:
                index_1 = 1
                index_2 = 2
                index_3 = 11
                index_4 = 14
        elif (abs(mod_signal_alpha) <= 0.5000):
            if (abs(mod_signal_beta) <= (abs(mod_signal_alpha) - 0.3333) * 1.7320):
                index_1 = 4
                index_2 = 5
                index_3 = 8
                index_4 = 17
            elif (abs(mod_signal_beta) <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 1
                    index_2 = 4
                    index_3 = 5
                    index_4 = 14
                else:
                    index_1 = 17
                    index_2 = 14
                    index_3 = 5
                    index_4 = 4
            else:
                index_1 = 1
                index_2 = 2
                index_3 = 5
                index_4 = 14
        else:
            index_1 = 4
            index_2 = 5
            index_3 = 8
            index_4 = 17
    elif (mod_signal_alpha >= 0 and mod_signal_beta < 0):  # Fourth Quadrant

        if (mod_signal_alpha <= 0.1666):
            if (abs(mod_signal_beta) <= (1.7320 * mod_signal_alpha)):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 9
                    index_3 = 10
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 22
                    index_3 = 23
                    index_4 = 26
            elif (abs(mod_signal_beta) <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 1
                    index_3 = 10
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 14
                    index_3 = 23
                    index_4 = 26
            elif (abs(mod_signal_beta) <= (0.2887 + (0.1666 - mod_signal_alpha) * 1.7320)):
                if balancing_status <= 0:
                    index_1 = 1
                    index_2 = 10
                    index_3 = 11
                    index_4 = 14
                else:
                    index_1 = 23
                    index_2 = 14
                    index_3 = 11
                    index_4 = 10
            else:
                index_1 = 10
                index_2 = 11
                index_3 = 20
                index_4 = 23
        elif (mod_signal_alpha <= 0.3333):
            if (abs(mod_signal_beta) <= (0.3333 - mod_signal_alpha) * 1.7320):
                if balancing_status <= 0:
                    index_1 = 0
                    index_2 = 9
                    index_3 = 10
                    index_4 = 13
                else:
                    index_1 = 13
                    index_2 = 22
                    index_3 = 23
                    index_4 = 26
            elif (abs(mod_signal_beta) <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 9
                    index_2 = 10
                    index_3 = 19
                    index_4 = 22
                else:
                    index_1 = 23
                    index_2 = 22
                    index_3 = 19
                    index_4 = 10
            elif (abs(mod_signal_beta) <= (1.7320 * mod_signal_alpha)):
                index_1 = 10
                index_2 = 19
                index_3 = 20
                index_4 = 23
            else:
                index_1 = 10
                index_2 = 11
                index_3 = 20
                index_4 = 23
        elif (mod_signal_alpha <= 0.5000):
            if (abs(mod_signal_beta) <= (mod_signal_alpha - 0.3333) * 1.7320):
                index_1 = 9
                index_2 = 18
                index_3 = 19
                index_4 = 22
            elif (abs(mod_signal_beta) <= 0.2887):
                if balancing_status <= 0:
                    index_1 = 9
                    index_2 = 10
                    index_3 = 19
                    index_4 = 22
                else:
                    index_1 = 23
                    index_2 = 22
                    index_3 = 19
                    index_4 = 10
            else:
                index_1 = 10
                index_2 = 19
                index_3 = 20
                index_4 = 23
        else:
            index_1 = 9
            index_2 = 18
            index_3 = 19
            index_4 = 22

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # Vector Definition
    V = [[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
         [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
         [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
         [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
         [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
         [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
         [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
         [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
         [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
         [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
         [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
         [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]]

    V_alpha = [0.0,
               -0.1666,
               -0.3333,
               -0.1666,
               -0.3333,
               -0.5,
               -0.3333,
               -0.5,
               -0.6666,
               0.3333,
               0.1666,
               0.0,
               0.1666,
               0.0,
               -0.1666,
               0.0,
               -0.1666,
               -0.3333,
               0.6666,
               0.5,
               0.3333,
               0.5,
               0.3333,
               0.1666,
               0.3333,
               0.1666,
               0.0]  # Real Part

    V_beta = [0.0,
              -0.2887,
              -0.5773,
              0.2887,
              0.0,
              -0.2887,
              0.5773,
              0.2887,
              0.0,
              0.0,
              -0.2887,
              -0.5773,
              0.2887,
              0.0,
              -0.2887,
              0.5773,
              0.2887,
              0.0,
              0.0,
              -0.2887,
              -0.5773,
              0.2887,
              0.0,
              -0.2887,
              0.5773,
              0.2887,
              0.0]  # Imaginary Part

    # Ignoring the smallest vector as
    # we shift the triangle to origin
    # based on the smallest vector
    V_x_alpha = V_alpha[index_2]
    V_x_beta = V_beta[index_2]
    V_y_alpha = V_alpha[index_3]
    V_y_beta = V_beta[index_3]

    # For all vectors in the triangle
    # Transposing towards the origin
    # using the first vector in the sequence
    mod_signal_alpha_T = mod_signal_alpha - V_alpha[index_1]
    mod_signal_beta_T = mod_signal_beta - V_beta[index_1]

    V_x_alpha_T = V_x_alpha - V_alpha[index_1]
    V_x_beta_T = V_x_beta - V_beta[index_1]

    V_y_alpha_T = V_y_alpha - V_alpha[index_1]
    V_y_beta_T = V_y_beta - V_beta[index_1]

    # Timing Calculation
    T_x = (V_y_beta_T * mod_signal_alpha_T - V_y_alpha_T * mod_signal_beta_T) / (
        V_x_alpha_T * V_y_beta_T - V_y_alpha_T * V_x_beta_T) * T_sw / 2
    T_y = (V_x_beta_T * mod_signal_alpha_T - V_x_alpha_T * mod_signal_beta_T) / (
        V_y_alpha_T * V_x_beta_T - V_x_alpha_T * V_y_beta_T) * T_sw / 2
    # Error checking
    # If wrong vectors are chosen, the time intervals will be negative
    if T_x < 0 or T_y < 0:
        print('Negative values in vectors ' + str(index_1)+'-'+str(index_2) +
              '-'+str(index_3)+'-'+str(index_4) + ': ' + str(T_x) + ',' + str(T_y))
    if (2 * (T_x + T_y) > T_sw):
        print('Negative values: ' + str((T_sw - 2 * (T_x + T_y)) / 4))
    if (2 * (T_x + T_y) < T_sw):
        T_n = (T_sw - 2 * (T_x + T_y)) / 4
    else:
        T_n = 0.0

    # Timing Sequence Generation
    t_seq = [
        T_n,  # smallest vector
        T_x,  # smallest vector + Vx
        T_y,  # smallest vector + Vx + Vy
        2 * T_n,  # smallest vector + Vx + Vy + 2*smallest vector
        T_y,  # smallest vector + Vx + Vy + 2*smallest vector + Vy
        T_x,  # smallest vector + Vx + Vy + 2*smallest vector + Vy + Vx
        T_n  # smallest vector + Vx + Vy + 2*smallest vector + Vy + Vx + smallest vector
    ]

    # Initialization at start of every switching cycle
    if (sequence_counter < 0):
        sequence_counter = 0
        # t2 is a time event variable that has the running value of the pulse width
        t2 += t_seq[0]

    if sequence_counter == 0:
        s1_gate = V[index_1][0]
        s2_gate = V[index_1][1]
        s3_gate = V[index_1][2]
        s4_gate = V[index_1][3]
        s5_gate = V[index_1][4]
        s6_gate = V[index_1][5]
        s7_gate = V[index_1][6]
        s8_gate = V[index_1][7]
        s9_gate = V[index_1][8]
        s10_gate = V[index_1][9]
        s11_gate = V[index_1][10]
        s12_gate = V[index_1][11]
    elif sequence_counter == 1:
        s1_gate = V[index_2][0]
        s2_gate = V[index_2][1]
        s3_gate = V[index_2][2]
        s4_gate = V[index_2][3]
        s5_gate = V[index_2][4]
        s6_gate = V[index_2][5]
        s7_gate = V[index_2][6]
        s8_gate = V[index_2][7]
        s9_gate = V[index_2][8]
        s10_gate = V[index_2][9]
        s11_gate = V[index_2][10]
        s12_gate = V[index_2][11]
    elif sequence_counter == 2:
        s1_gate = V[index_3][0]
        s2_gate = V[index_3][1]
        s3_gate = V[index_3][2]
        s4_gate = V[index_3][3]
        s5_gate = V[index_3][4]
        s6_gate = V[index_3][5]
        s7_gate = V[index_3][6]
        s8_gate = V[index_3][7]
        s9_gate = V[index_3][8]
        s10_gate = V[index_3][9]
        s11_gate = V[index_3][10]
        s12_gate = V[index_3][11]
    elif sequence_counter == 3:
        s1_gate = V[index_4][0]
        s2_gate = V[index_4][1]
        s3_gate = V[index_4][2]
        s4_gate = V[index_4][3]
        s5_gate = V[index_4][4]
        s6_gate = V[index_4][5]
        s7_gate = V[index_4][6]
        s8_gate = V[index_4][7]
        s9_gate = V[index_4][8]
        s10_gate = V[index_4][9]
        s11_gate = V[index_4][10]
        s12_gate = V[index_4][11]
    elif sequence_counter == 4:
        s1_gate = V[index_3][0]
        s2_gate = V[index_3][1]
        s3_gate = V[index_3][2]
        s4_gate = V[index_3][3]
        s5_gate = V[index_3][4]
        s6_gate = V[index_3][5]
        s7_gate = V[index_3][6]
        s8_gate = V[index_3][7]
        s9_gate = V[index_3][8]
        s10_gate = V[index_3][9]
        s11_gate = V[index_3][10]
        s12_gate = V[index_3][11]
    elif sequence_counter == 5:
        s1_gate = V[index_2][0]
        s2_gate = V[index_2][1]
        s3_gate = V[index_2][2]
        s4_gate = V[index_2][3]
        s5_gate = V[index_2][4]
        s6_gate = V[index_2][5]
        s7_gate = V[index_2][6]
        s8_gate = V[index_2][7]
        s9_gate = V[index_2][8]
        s10_gate = V[index_2][9]
        s11_gate = V[index_2][10]
        s12_gate = V[index_2][11]
    elif sequence_counter == 6:
        s1_gate = V[index_1][0]
        s2_gate = V[index_1][1]
        s3_gate = V[index_1][2]
        s4_gate = V[index_1][3]
        s5_gate = V[index_1][4]
        s6_gate = V[index_1][5]
        s7_gate = V[index_1][6]
        s8_gate = V[index_1][7]
        s9_gate = V[index_1][8]
        s10_gate = V[index_1][9]
        s11_gate = V[index_1][10]
        s12_gate = V[index_1][11]

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

    # Data storage
    pwm_carr_signal = carr_signal

    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate
    pwm_s3_gate = s3_gate
    pwm_s4_gate = s4_gate
    pwm_s5_gate = s5_gate
    pwm_s6_gate = s6_gate
    pwm_s7_gate = s7_gate
    pwm_s8_gate = s8_gate
    pwm_s9_gate = s9_gate
    pwm_s10_gate = s10_gate
    pwm_s11_gate = s11_gate
    pwm_s12_gate = s12_gate

    # Time increment
    t1 += dt
