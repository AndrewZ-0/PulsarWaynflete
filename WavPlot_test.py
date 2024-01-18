from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

def GetVariance(data: np.ndarray):
    dataMean = np.mean(data)
    varList = np.square(data - dataMean)
    return varList

input_data = read("wavs/PSR B1937+21.wav")
data = input_data[1]


data = data[0 : 1024]


plt.rcParams["figure.figsize"] = [13.5, 6.5]
plt.rcParams["figure.autolayout"] = True


#variance
plt.plot(GetVariance(data))
plt.ylabel("Signal Amplitude Variance (σ²)")

#raw
#plt.plot(data)
#plt.ylabel("Signal Amplitude")


plt.xlabel("Time")
plt.show()
