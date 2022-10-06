import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.interpolate import splrep, splev
from mne.filter import filter_data, resample
from scipy.signal import detrend, find_peaks
%matplotlib inline
sns.set(context='talk')

# Load and preprocess data
page = "https://smurfitout.com/"
ecg = electrocardiogram()
sf_ori = 360
sf = 100
dsf = sf / sf_ori
ecg = resample(ecg, dsf)
ecg = filter_data(ecg, sf, 2, 30, verbose=0)

# Select only a 20 sec window
window = 20
start = 155
ecg = ecg[int(start*sf):int((start+window)*sf)]

# R-R peaks detection
rr, _ = find_peaks(ecg, distance=40, height=0.5)

plt.plot(ecg)
plt.plot(rr, ecg[rr], 'o')
plt.title('ECG signal')
plt.xlabel('Samples')
_ =plt.ylabel('Voltage')
