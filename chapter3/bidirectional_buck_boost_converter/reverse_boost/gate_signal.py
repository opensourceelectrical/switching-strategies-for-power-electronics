# This is the gate signal generator file for the bidirectional buck-boost converter
# The converter uses two separate converter legs fed by their separate dc sources
# The converter legs are interconnected by an inductor
# Only reverse power flow is handled in this file.
# Only boost mode is handled in this file (Vo > Vin)
# Voltage source at output feeds power back to a capacitor at the input

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

    # Reverse boost mode
    # Only S3 is switched
    # Inductor current energizes through S3-D1 and freewheels through D4-D1
    leg1_mod = 0.0
    s1_gate = 0.0
    s2_gate = 0.0

    leg2_mod = 0.5
    if leg2_mod >= carr_signal:
        s3_gate = 1.0
        s4_gate = 0.0
    else:
        s3_gate = 0.0
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
