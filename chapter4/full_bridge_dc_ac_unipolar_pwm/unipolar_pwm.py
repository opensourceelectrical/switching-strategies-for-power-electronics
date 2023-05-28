# This is gate generator file for a full-bridge converter
# The converter functions as a dc-ac converter
# Unipolar PWM will be used

import math
from math import sin, pi

# Switching frequency of 2.5KHz
sw_freq = 2500.0
sw_period = 1/sw_freq
# Carrier waveform slope
carr_slope_mag = 4.0/sw_period

# Sample ac system frequency of 50 Hz
op_freq = 50.0
w_op_freq = 2*pi*op_freq

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal varaible

    if not carr_slope:
        carr_slope = carr_slope_mag

    # Triangular carrier waveforms c1(t) = -c2(t)
    # Calculating present sample w.r.t previous sample
    carr_signal_1 += carr_slope * dt
    carr_signal_2 = - carr_signal_1

    # Changing slope at the limits
    if carr_signal_1 >= 1.0:
        carr_slope = -carr_slope_mag

    if carr_signal_1 <= -0.0:
        carr_slope = carr_slope_mag

    # Sample sine wave modulation signal
    mod_index = 0.8
    sine_wave = mod_index * sin(w_op_freq * t1)

    if sine_wave >= carr_signal_2:
        s1_gate = 1.0
        s2_gate = 0.0
    else:
        s1_gate = 0.0
        s2_gate = 1.0

    if sine_wave >= carr_signal_1:
        s4_gate = 1.0
        s3_gate = 0.0
    else:
        s4_gate = 0.0
        s3_gate = 1.0

    # Data storage
    pwm_carr_signal1 = carr_signal_1
    pwm_carr_signal2 = carr_signal_2
    pwm_mod_signal = sine_wave

    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate
    pwm_s3_gate = s3_gate
    pwm_s4_gate = s4_gate

    # Time increment
    t1 += dt
