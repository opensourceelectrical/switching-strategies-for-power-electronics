import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq

# This program demonstrates the frequency spectrum of 
# a fixed frequency rectangular wave signal
# The fundamental and the dominant harmonics are seen

def compare(a):
    '''Comparator'''
    if a > 0:
        return 1
    else:
        return -1
vcompare = np.vectorize(compare)

fsqw = 50.0                 # frequency of the square wave switching signal in Hz
omega_sqw = 2*np.pi*fsqw    # frequency of the square wave signal in rad/s

# Duration of the time window
t_duration = 1.0
# Sampling time interval and frequency
t_step = 1.0e-6
fsampling = 1/t_step

# Time array which is integers from 0 to 1 million - 1
time_array = np.arange(0, t_duration, t_step)
no_of_data = np.size(time_array)

# Sine wave
sine_wave = np.sin(omega_sqw*time_array)

# Square wave signal
sq_wave = vcompare(sine_wave)

# FFT of the square wave signal
freq_v_output = fft(sq_wave)/no_of_data
freq_array = fftfreq(no_of_data, t_step)

# Fonts for plots
font = {
    'family' : 'normal',
    'weight' : 'normal',
    'size'   : 12
}
matplotlib.rc('font', **font)

# Uncomment the plt.savefig() statements to save plots to file

# Plot of the square wave signal
plt.figure()
plt.title('Voltage Output')
plt.xlim([0.0, 1.0])
plt.xlabel('Time')
plt.plot(time_array, sine_wave)
plt.plot(time_array, sq_wave)
# plt.savefig('fig1.eps', format='eps')

plt.figure()
plt.plot(time_array, sine_wave)
plt.plot(time_array, sq_wave)
plt.title('Voltage Output')
plt.xlim([0.775, 0.805])
plt.xlabel('Time')
plt.xticks([0.78, 0.79, 0.8])
# plt.savefig('fig2.eps', format='eps')

# Plot of the frequency spectrum of the square wave signal
plt.figure()
plt.plot(freq_array, np.abs(freq_v_output))
plt.title('Frequency response')
plt.xlim([-50000, 50000])
plt.xlabel('Frequency (Hz)')
# plt.savefig('fig3.eps', format='eps')

plt.figure()
plt.plot(freq_array, np.abs(freq_v_output))
plt.title('Frequency response')
plt.xlim([0, 1000])
plt.xticks([250, 500, 750])
plt.xlabel('Frequency (Hz)')
# plt.savefig('fig4.eps', format='eps')

plt.show()
