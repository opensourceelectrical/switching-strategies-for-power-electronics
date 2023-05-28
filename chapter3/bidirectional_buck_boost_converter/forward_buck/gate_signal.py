# This is the gate signal generator file for the bidirectional buck-boost converter
# The converter uses two separate converter legs fed by their separate dc sources
# The converter legs are interconnected by an inductor
# Only forward power flow is handled in this file.
# Only buck mode is handled in this file (Vo < Vin)
# Input voltage source feeds power to a capacitor that supplies a resistive load

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

    # Forward buck mode
    # Only S1 is switched
    # Inductor energizes with S1-D3 and freewheels through D2-D3
    leg1_duty_ratio = 0.38     # For vOUT = 9 V
    if leg1_duty_ratio >= carr_signal:
        s1_gate = 1.0
        s2_gate = 0.0
    else:
        s1_gate = 0.0
        s2_gate = 0.0

    leg2_duty_ratio = 0.0
    s3_gate = 0.0
    s4_gate = 0.0

    # Data storage
    pwm_carr_signal = carr_signal

    pwm_s1_mod_signal = leg1_duty_ratio
    pwm_s2_mod_signal = leg1_duty_ratio
    pwm_s3_mod_signal = leg2_duty_ratio
    pwm_s4_mod_signal = leg2_duty_ratio

    pwm_s1_gate = s1_gate
    pwm_s2_gate = s2_gate
    pwm_s3_gate = s3_gate
    pwm_s4_gate = s4_gate

    # Time increment
    t1 += dt
