import numpy as np
from numpy import diff
import matplotlib.pyplot as plt


with open("data1.txt") as f:
    data = f.read()

data = data.split('\n')
x = [row.split()[0] for row in data]
x =  map(float, x)

y = [row.split()[1] for row in data]
y =  map(float, y)


xA = np.asarray(x)
yA = np.asarray(y)

dy = diff(y)/diff(x)
#derivative of voltages

temp = []

z = max(dy)


fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Time Series of the Membrane Voltage of a Neuron")
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (mV)')

ax1.plot(x,y, c='r', label='membrane voltage')
leg = ax1.legend()

plt.show();

arr = np.array(dy)
q = np.mean(arr, axis =0)
l = np.std(arr, axis=0)

spikes = []
times = []
tiempo = []

m = 0

for i, s in enumerate(arr):

    if ( (s > (q + l*7) ) & (arr[i]-arr[i-1] < 0) & ((xA[i] - xA[m]) > 0.005)) :
        m = i
        for t in range(0, 20):
            if(yA[i+t-1] < yA[i+t]) :
                temp.append(yA[i+t])
                times.append(xA[i+t])
        spikes.append(max(temp))
        tiempo.append(max(times))
        temp[:] = []

isi = diff(tiempo)
isiAr = np.array(isi)

meanOfISI = np.mean(isiAr, axis =0)
print "mean of ISI ",meanOfISI
stdOfISI = np.std(isiAr, axis=0)
print "standard deviation of ISI ", stdOfISI
medianOfISI = np.median(isiAr, axis =0)
print "median of ISI ", medianOfISI
isiMS = isiAr * 1000

print isiMS

plt.title("ISI Histogram")
plt.xlabel("time (ms)")
plt.ylabel("Counts")
n, bins, patches = plt.hist(isiMS, 5)
plt.axis([300, 500, 0, 4])
plt.grid(True)
plt.show()
