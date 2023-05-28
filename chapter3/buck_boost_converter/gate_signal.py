# This is the gate signal generator for a buck-boost converter
# that uses two controllable devices and two diodes
# Buck and boost mode of operation are separate
# Each controllable device has a separate duty ratio

# Switching frequency of 10KHz
sw_freq = 10000.0

# Slope of the carrier waveform
carr_slope = 1 / (1 / sw_freq)

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal varaible

    # Sawtooth waveform
    carr_signal += carr_slope * dt

    if carr_signal > 1.0:
        carr_signal = 0.0

    # Use only in buck mode or in boost mode
    # Comment the other block of code.

    # Buck mode
    d1 = 0.38     # For Vout = 9 V
    if d1 >= carr_signal:
        s1_gate = 1.0
    else:
        s1_gate = 0.0

    d2 = 0.0
    s2_gate = 0.0

    # Boost mode
    # d1 = 1.0
    # s1_gate = 1.0
    # d2 = 0.20   # For Vout = 30 V
    # if d2 >= carr_signal:
    #     s2_gate = 1.0
    # else:
    #     s2_gate = 0.0

    # Data storage
    pwm_s1_mod_signal = d1
    pwm_s2_mod_signal = d2
    pwm_carrier_signal = carr_signal
    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate

    t1 += dt