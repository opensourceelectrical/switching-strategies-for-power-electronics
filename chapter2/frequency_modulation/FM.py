import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq

# This program demonstrates FM from a purely theoretical perspective
# With a modulation signal having a constant amplitude and frequency

fm = 50.0               # frequency of audio signal
omega_m = 2*np.pi*fm
fc = 10000.0            # frequency of carrier signal
omega_c = 2*np.pi*fc

# Duration of the time window
t_duration = 1.0
# Sampling time interval and frequency
t_step = 1.0e-6
fsampling = 1/t_step

# Time array which is integers from 0 to 1 million - 1
time_array = np.arange(0, t_duration, t_step)
no_of_data = np.size(time_array)

# Audio signal to be modulated
mod_signal = np.cos(time_array*omega_m)

# Carrier signal
carr_signal = np.cos(time_array*omega_c)

# Resultant (modulated) signal
trans_signal = np.cos(time_array*(omega_c + mod_signal))

# FFT of the entire waveform
freq_trans_signal = fft(trans_signal)/no_of_data
freq_array = fftfreq(no_of_data, t_step)

# Fonts for plots
font = {
    'family' : 'normal',
    'weight' : 'normal',
    'size'   : 12
}
matplotlib.rc('font', **font)

# Uncomment the plt.savefig() statements to save plots to file

# Plot of the frequency spectrum modulated signal
plt.figure()
plt.plot(freq_array, np.abs(freq_trans_signal))
plt.title('Frequency response')
plt.xlabel('Frequency (Hz)')
plt.xlim([-50000, 50000])
# plt.savefig('fig1.eps', format='eps')

plt.figure()
plt.plot(freq_array, np.abs(freq_trans_signal))
plt.title('Frequency response')
plt.xlabel('Frequency (Hz)')
plt.xlim([9800, 10200])
# plt.savefig('fig2.eps', format='eps')

plt.show()
