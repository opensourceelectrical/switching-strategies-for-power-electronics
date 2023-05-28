from math import sin, cos, pi


def quantize(val, interval):
    return (val // interval) * interval


# Grid frequency
mod_sig_freq = 50.0

# Sampling time interval
dt = 1.0e-6

if t_clock > t1:    # t_clock is an internal variable

    q_int = 1.0e-6

    # Modulation Signal Generation
    mod_index = 0.3
    mod_signal_A = mod_index * sin(2 * pi * mod_sig_freq * t1)
    mod_signal_B = mod_index * sin(2 * pi * mod_sig_freq * t1 - 2 * pi / 3)
    mod_signal_C = mod_index * sin(2 * pi * mod_sig_freq * t1 + 2 * pi / 3)

    # Clarke Transform
    mod_signal_alpha = mod_signal_A
    mod_signal_beta = 0.577 * mod_signal_A + 1.155 * mod_signal_B

    ref_volt_alpha = quantize(mod_signal_alpha, q_int)
    ref_volt_beta = quantize(mod_signal_beta, q_int)

    t1 += dt
