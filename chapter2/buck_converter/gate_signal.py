# This is the gate signal generator for a single device buck controller
# Duty ratio is assumed fixed and set in this code.

# Switching frequency of 10KHz
sw_freq = 10000.0

# Defining carrier slope
carr_slope = 1 / (1 / sw_freq)

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal variable

    # Sawtooth waveform
    carr_signal += carr_slope * dt

    if carr_signal > 1.0:
        carr_signal = 0.0

    # Buck mode
    duty_ratio = 0.38     # For Vout = 9 V
    if duty_ratio >= carr_signal:
        s1_gate = 1.0
    else:
        s1_gate = 0.0

    # Data storage
    pwm_mod_signal = duty_ratio
    pwm_carr_signal = carr_signal
    pwm_gate_signal = s1_gate

    t1 += dt
