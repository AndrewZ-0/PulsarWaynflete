from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

def GetVariance(data: np.ndarray):
    dataMean = np.mean(data)
    varList = np.square(data - dataMean)
    return varList


validFile = False
while not validFile:
    try:
        fileName = input("Read file: ")
        input_data = read(f"wavs/{fileName}.wav")
        data = input_data[1]
    except:
        print("Invalid input: try again")
    else:
        validFile = True


validChoice = False
while not validChoice:
    varianceFlag = input("Use Variance? (Y/N): ").upper()

    validChoice = True
    if varianceFlag == "Y":
        varianceFlag = True
    elif varianceFlag == "N":
        varianceFlag = False
    else:
        print("Invalid choice: Try again")
        validChoice = False

plt.rcParams["figure.figsize"] = [13.5, 6.5]
plt.rcParams["figure.autolayout"] = True

if varianceFlag:
    plt.plot(GetVariance(data))
    plt.ylabel("Signal Amplitude Variance (σ²)")
else:
    plt.plot(data)
    plt.ylabel("Signal Amplitude")


plt.xlabel("Time")
plt.show()
