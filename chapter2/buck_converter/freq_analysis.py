import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq
import pandas as pd

# Fonts for plots
font = {
    'family' : 'normal',
    'weight' : 'normal',
    'size'   : 12
}
matplotlib.rc('font', **font)

# Reading the simulation output data file
df = pd.read_csv("ckt_output.dat", delim_whitespace=True)
# Columns can be found in the file plotkey.txt.
# All variables must be specified in the array
df.columns = ['Time', 'i_in', 'i_L', 'i_d1', 'i_load', 'i_cout', 'vsw', 'vo', 'm', 'c', 'g']

# Extracting data from Pandas data frame to Numpy arrays
time_array = np.array(df['Time'])
vo = np.array(df['vo'])
vsw = np.array(df['vsw'])

no_of_data = len(time_array)

# FFT of the square wave signal
freq_v_sw = fft(vsw)/no_of_data
freq_array = fftfreq(no_of_data, time_array[1] - time_array[0])

freq_v_output = fft(vo)/no_of_data

# Uncomment the plt.savefig() statements to save plots to file

# Plot of the frequency responses of the voltage waveforms
plt.figure()
plt.plot(freq_array, np.abs(freq_v_sw))
plt.title('Frequency response')
plt.xlim([-500000, 500000])
plt.xlabel('Frequency (Hz)')
# plt.savefig("fig1.eps", format="eps")

plt.figure()
plt.plot(freq_array, np.abs(freq_v_sw))
plt.title('Frequency response')
plt.xlim([-30000, 30000])
plt.xlabel('Frequency (Hz)')
# plt.savefig("fig2.eps", format="eps")

plt.figure()
plt.plot(freq_array, np.abs(freq_v_output))
plt.title('Frequency response')
plt.xlim([-30000, 30000])
plt.xlabel('Frequency (Hz)')
# plt.savefig("fig3.eps", format="eps")

plt.show()
