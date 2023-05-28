# This file generates three-phase modulation signals
# These modulation signals are transformed using Clarke's transformation
# The transformed outputs are VariableStorage elements that can be accessed in another control file

from math import sin, cos, pi

# Grid frequency
mod_sig_freq = 50.0

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal variable

    # Modulation Signal Generation
    mod_index = 0.6
    mod_signal_A = mod_index * sin(2 * pi * mod_sig_freq * t1)
    mod_signal_B = mod_index * sin(2 * pi * mod_sig_freq * t1 - 2 * pi / 3)
    mod_signal_C = mod_index * sin(2 * pi * mod_sig_freq * t1 + 2 * pi / 3)

    # Clarke Transform
    mod_signal_alpha = mod_signal_A
    mod_signal_beta = 0.577 * mod_signal_A + 1.155 * mod_signal_B

    ref_volt_alpha = mod_signal_alpha
    ref_volt_beta = mod_signal_beta

    t1 += dt
