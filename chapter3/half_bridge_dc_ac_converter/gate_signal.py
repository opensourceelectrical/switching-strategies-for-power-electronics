# This is a gate signal generator file for a half-bridge converter
# The output is only a R-L load

import math
from math import sin, pi

# Switching frequency of 10KHz
sw_freq = 2500.0
sw_period = 1/sw_freq
carr_slope_mag = 2 / (sw_period/2)

# Sample ac system frequency of 50 Hz
op_freq = 50.0
w_op_freq = 2*pi*op_freq

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:
    # Triangular carrier waveform
    if carr_slope == 0.0:
        carr_slope = carr_slope_mag

    # Calculating present sample w.r.t previous sample
    carr_signal += carr_slope*dt

    # Changing slope at the limits
    if carr_signal >= 1.0:
        carr_slope = -carr_slope_mag

    if carr_signal <= -1.0:
        carr_slope = carr_slope_mag

    # Sine wave modulation signal
    mod_index = 0.8
    sine_wave = mod_index * sin(w_op_freq * t1)

    if sine_wave >= carr_signal:
        s1_gate = 1.0
        s2_gate = 0.0
    else:
        s1_gate = 0.0
        s2_gate = 1.0

    # Data storage
    pwm_carr_signal = carr_signal
    pwm_mod_signal = sine_wave
    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate

    # Time increment
    t1 += dt
