import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import signal
from numpy.fft import fft, fftfreq

def compare(a, b):
    '''Comparator'''
    if a > b:
        return 1
    else:
        return -1
vcompare = np.vectorize(compare)

# This program demonstrates the principle of a Sinusoidal Pulse Width Modulation (SPWM)
# The frequency spectrum of the SPW modulated waveform is plotted with no dominant harmonics seen

fm = 50.0               # frequency of sinusoidal signal in Hz
omega_m = 2*np.pi*fm
fc = 5000.0             # frequency of triangular carrier signal in Hz (>=20*fm)
omega_c = 2*np.pi*fc

# Duration of the time window
t_duration = 1.0
# Sampling time interval and frequency
t_step = 1.0e-6
fsampling = 1/t_step

# Time array which is integers from 0 to 1 million - 1
time_array = np.arange(0, t_duration, t_step)
no_of_data = np.size(time_array)

# Modulation signal
mod_index = 0.8         # modulation index
mod_signal = mod_index*np.cos(time_array*omega_m)

# Carrier signal
# The sawtooth waveform goes from (0, -1) to (pi, 1) for 0.5 duty cycle.
carr_signal = signal.sawtooth(omega_c*time_array, 0.5)

# PWM waveform
switch_wave = vcompare(mod_signal, carr_signal)

# FFT of the square wave signal
freq_v_output = fft(switch_wave)/no_of_data
freq_array = fftfreq(no_of_data, t_step)

# Fonts for plots
font = {
    'family' : 'normal',
    'weight' : 'normal',
    'size'   : 12
}
matplotlib.rc('font', **font)

# Uncomment the plt.savefig() statements to save plots to file

# Plot of the Sine PWM signal
plt.figure()
plt.plot(time_array, switch_wave)
plt.plot(time_array, mod_signal)
plt.plot(time_array, carr_signal)
plt.title('Result of Comparison')
plt.xlim([0.78, 0.785])
plt.xlabel('Time')
plt.xticks([0.78, 0.785])
# plt.savefig('fig1.eps', format='eps')

plt.figure()
plt.plot(time_array, switch_wave)
plt.plot(time_array, mod_signal)
plt.plot(time_array, carr_signal)
plt.title('Result of Comparison')
plt.xlim([0.783, 0.784])
plt.xlabel('Time')
plt.xticks([0.783, 0.784])
# plt.savefig('fig2.eps', format='eps')

# Plot of the frequency spectrum of the Sine PWM signal
plt.figure()
plt.plot(freq_array, np.abs(freq_v_output))
plt.title('Frequency response')
plt.xlim([0, 50000])
plt.xlabel('Frequency (Hz)')
# plt.savefig('fig3.eps', format='eps')

plt.figure()
plt.plot(freq_array, np.abs(freq_v_output))
plt.title('Frequency response')
plt.xlim([0, 6000])
plt.xlabel('Frequency (Hz)')
# plt.savefig('fig4.eps', format='eps')

plt.show()
