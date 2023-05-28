# This is the gate signal generator file for the bidirectional buck converter
# The converter uses a converter leg
# Only reverse power flow is handled in this file.
# Voltage source at the output feeds power to a capacitor at the input

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

    # Buck mode for reverse power flow
    d1 = 0.0
    s1_gate = 0.0
    d2 = 0.62
    if d2 >= carr_signal:
        s2_gate = 1.0
    else:
        s2_gate = 0.0

    # Data storage
    pwm_s1_mod_signal = d1
    pwm_s2_mod_signal = d1
    pwm_carr_signal = carr_signal
    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate

    t1 += dt
