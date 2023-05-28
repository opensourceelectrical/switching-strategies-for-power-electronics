# This is a gate signal generator for a three-phase three-leg converter
# The three-phase modulation signals are generated externally
# but are accessed in this file for generating PWM gate signals

import math
from math import sin, pi

# Switching frequency of 2.5KHz
sw_freq = 2500.0
carr_slope_mag = 4.0 * sw_freq

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal variable

    if not carr_slope:
        carr_slope = carr_slope_mag

    carr_signal += carr_slope * dt
    # carr_signal_ps += carr_slope_ps * dt

    # Changing slope at the limits
    # This is also defined as the beginning of the switching cycle
    # At the beginning of the switching cycle, the external modulation signals
    # are assigned to the modulator and kept constant during the entire
    # switching cycle to ensure gate signals are symmetric across the cycle.
    if carr_signal >= 1.0:
        carr_slope = -carr_slope_mag
        mod_signal_A = ref_volt_A
        mod_signal_B = ref_volt_B
        mod_signal_C = ref_volt_C

    if carr_signal <= -1.0:
        carr_slope = carr_slope_mag

    if mod_signal_A > carr_signal:
        s1_gate = 1.0
        s2_gate = 0.0
    else:
        s1_gate = 0.0
        s2_gate = 1.0

    if mod_signal_B > carr_signal:
        s3_gate = 1.0
        s4_gate = 0.0
    else:
        s3_gate = 0.0
        s4_gate = 1.0

    if mod_signal_C > carr_signal:
        s5_gate = 1.0
        s6_gate = 0.0
    else:
        s5_gate = 0.0
        s6_gate = 1.0

    # Data storage
    pwm_carrier = carr_signal

    pwm_mod_a = mod_signal_A
    pwm_mod_b = mod_signal_B
    pwm_mod_c = mod_signal_C

    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate
    pwm_s3_gate = s3_gate
    pwm_s4_gate = s4_gate
    pwm_s5_gate = s5_gate
    pwm_s6_gate = s6_gate

    # Time increment
    t1 += dt
