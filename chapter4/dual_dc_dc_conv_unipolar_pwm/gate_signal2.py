# This is gate generator file for a full-bridge converter
# The converter functions as a dc-dc converter
# Unipolar PWM will be used for dc applications
# These gate signals are for one of two full-bridge converters interconnected by an inductor
# The duty ratio can therefore also be negative

import math
from math import sin, pi

# Switching frequency of 2.5KHz
sw_freq = 2500.0
sw_period = 1/sw_freq
# Sawtooth carrier waveform slope magnitude
carr_slope = 1.0/sw_period

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal varaible

    # Initialization of the carrier waveforms
    # Initial values in control interface
    # To ensure that they are 180 degree phase shifted
    if carr_signal1 > 0.5:
        carr_signal1 = 0.0
    if carr_signal2 < -0.5:
        carr_signal2 = 0.0

    # Calculating present sample w.r.t previous sample
    carr_signal1 -= carr_slope * dt
    carr_signal2 += carr_slope * dt

    # Changing slope at the limits
    if carr_signal1 <= -1.0:
        carr_signal1 = 0.0

    if carr_signal2 >= 1.0:
        carr_signal2 = 0.0

    # Duty ratio > 0 will produce a positive output voltage
    # Duty ratio < 0 will produce a negative output voltage
    mod_index = 0.3

    if mod_index >= carr_signal1:
        s1_gate = 1.0
        s2_gate = 0.0
    else:
        s1_gate = 0.0
        s2_gate = 1.0
    if mod_index >= carr_signal2:
        s3_gate = 0.0
        s4_gate = 1.0
    else:
        s3_gate = 1.0
        s4_gate = 0.0

    # Data storage
    pwm2_carr_signal1 = carr_signal1
    pwm2_carr_signal2 = carr_signal2
    pwm2_mod_signal = mod_index

    pwm2_s1_gate = s1_gate
    pwm2_s2_gate = s2_gate
    pwm2_s3_gate = s3_gate
    pwm2_s4_gate = s4_gate

    # Time increment
    t1 += dt
