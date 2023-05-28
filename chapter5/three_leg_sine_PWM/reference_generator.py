# This file generates three-phase modulation signals
# The outputs are VariableStorage elements that can be accessed in another control file

import math
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

    ref_volt_A = mod_signal_A
    ref_volt_B = mod_signal_B
    ref_volt_C = mod_signal_C

    t1 += dt
