# This is gate generator file for a full-bridge converter
# Converter is used in high-frequency dc-dc applications
# These applications need a transformed
# Output of the full-bridge converter needs to be high-frequency ac

import math
from math import sin, pi

# Switching frequency of 2.5KHz
sw_freq = 2500.0
carr_slope = 1/(1/sw_freq)

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal varaible

    duty_ratio = 0.2

    # Initialization of the carrier waveforms
    # Triangular carrier waveforms c1(t) = -c2(t)
    # The duty ratio becomes the phase shift between them
    if carr_signal1 < -0.5:
        carr_signal1 = 0.0
        carr_signal2 = -duty_ratio

    # Calculating present sample w.r.t previous sample
    carr_signal1 += carr_slope * dt
    carr_signal2 -= carr_slope * dt

    # Changing slope at the limits
    if carr_signal1 >= 1.0:
        carr_signal1 = 0.0

    if carr_signal2 <= -1.0:
        carr_signal2 = 0.0

    # Setting comparison for carriers to be 0.5 for 50% duty ratio operation
    mod_signal = 0.5

    if -0.5 >= carr_signal2:
        s1_gate = 1.0
        s2_gate = 0.0
    else:
        s1_gate = 0.0
        s2_gate = 1.0

    if 0.5 >= carr_signal1:
        s3_gate = 0.0
        s4_gate = 1.0
    else:
        s3_gate = 1.0
        s4_gate = 0.0

    # Data storage
    pwm_carr_signal1 = carr_signal1
    pwm_carr_signal2 = carr_signal2
    pwm_mod_signal = mod_signal

    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate
    pwm_s3_gate = s3_gate
    pwm_s4_gate = s4_gate

    # Time increment
    t1 += dt
