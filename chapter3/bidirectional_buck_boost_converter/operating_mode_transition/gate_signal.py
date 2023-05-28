# This is the gate signal generator file for the bidirectional buck-boost converter
# The converter uses two separate converter legs fed by their separate dc sources
# The converter legs are interconnected by an inductor
# Operation changes from forward buck to reverse buck
# Only buck mode is handled in this file (Vo < Vin)
# But power flow reverses
# There are two voltage sources - one at input and one at output
# But in any mode only one is enabled. The other is disconnected.
# This way only one voltage source supplies power to the other side being a capacitor.

# Switching frequency of 10KHz
sw_freq = 10000.0

# Carrier waveform slope
carr_slope = 1 / (1 / sw_freq)

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal varaible

    # Sawtooth waveform
    carr_signal += carr_slope * dt

    if carr_signal > 1.0:
        carr_signal = 0.0

    # At t=0.1s, the operating mode changes from
    # forward buck to reverse buck mode
    if t_clock < 0.1:
        # Forward buck mode
        # Enabling voltage source at input
        vin_gate = 1.0
        # Disconnecting voltage source at output
        vo_gate = 0.

        # For vo = 9V
        leg1_mod = 0.34
        if leg1_mod >= carr_signal:
            s1_gate = 1.0
            s2_gate = 0.0
        else:
            s1_gate = 0.0
            s2_gate = 0.0

        leg2_mod = 0.0
        s3_gate = 0.0
        s4_gate = 0.0
    else:
        # Reverse buck mode
        # Disconnecting voltage source at input
        vin_gate = 0.0
        # Enabling voltage source at output
        vo_gate = 1.0

        # For vin = 24V
        leg1_mod = 0.63
        if leg1_mod >= carr_signal:
            s1_gate = 0.0
            s2_gate = 1.0
        else:
            s1_gate = 0.0
            s2_gate = 0.0

        leg2_mod = 1.0
        s3_gate = 1.0
        s4_gate = 0.0

    # Data storage
    pwm_carr_signal = carr_signal

    pwm_s1_mod_signal = leg1_mod
    pwm_s2_mod_signal = leg1_mod
    pwm_s3_mod_signal = leg2_mod
    pwm_s4_mod_signal = leg2_mod

    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate
    pwm_s3_gate = s3_gate
    pwm_s4_gate = s4_gate

    # Time increment
    t1 += dt
