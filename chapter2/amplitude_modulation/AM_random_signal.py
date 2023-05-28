import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq
from numpy.random import random as rm

# This program demonstrates AM with a modulation signal that is variable
# The amplitude and frequency that varies from constant values by random distributions

fm = 50.0               # base frequency of audio signal
omega_m = 2*np.pi*fm
Am = 0.5                # base amplitude of audio signal
fc = 5000.0             # frequency of carrier signal
omega_c = 2*np.pi*fc

# Duration of the time window
t_duration = 1.0
# Sampling time interval and frequency
t_step = 1.0e-6
fsampling = 1/t_step

# Time array which is integers from 0 to 1 million - 1
time_array = np.arange(0, t_duration, t_step)
no_of_data = np.size(time_array)

Ar = 0.2                # Max magnitude of random variation to audio signal
fr = 30.0               # Max frequency of random variation to audio signal

# Audio signal to be modulated
mod_signal = (Am - rm()*Ar) * np.cos(time_array*(omega_m -2*fr*np.pi*rm()))

# Carrier signal
carr_signal = np.cos(time_array*omega_c)

# Resultant (modulated) signal
trans_signal = mod_signal * carr_signal

# FFT of the entire waveform
freq_trans_signal = fft(trans_signal)/no_of_data
freq_array = fftfreq(no_of_data, t_step)

# Uncomment the plt.savefig() statements to save plots to file

# Fonts for plots
font = {
    'family' : 'normal',
    'weight' : 'normal',
    'size'   : 12
}
matplotlib.rc('font', **font)

# Plotting the complete modulated waveform
plt.figure()
plt.title('AM Signal')
plt.xlim([0.0, 1.0])
plt.xlabel('Time')
plt.plot(time_array, trans_signal)
# plt.savefig('fig1.eps', format='eps')

# Zooming in on the plot
plt.figure()
plt.plot(time_array, trans_signal)
plt.title('AM Signal')
plt.xlim([0.78, 0.8])
plt.xlabel('Time')
plt.xticks([0.78, 0.79, 0.8])
# plt.savefig('fig2.eps', format='eps')

# Plot of the frequency spectrum modulated signal
plt.figure()
plt.plot(freq_array, np.abs(freq_trans_signal))
plt.title('Frequency response')
plt.xlabel('Frequency (Hz)')
plt.xlim([-50000, 50000])
# plt.savefig('fig3.eps', format='eps')

plt.figure()
plt.plot(freq_array, np.abs(freq_trans_signal))
plt.title('Frequency response')
plt.xlabel('Frequency (Hz)')
plt.xlim([4800, 5200])
#plt.savefig('fig4.eps', format='eps')

plt.show()
