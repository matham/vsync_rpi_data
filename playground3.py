import numpy as np
import matplotlib.pylab as plt
from scipy import signal
from os.path import join


def schmitt_trigger(up, high, down, low, data):
    result = []
    for s, val in enumerate(data):
        if val < low:
            state = 'low'
            result.append((s, 0))
            break
        elif  val > high:
            state = 'high'
            result.append((s, 1))
            break

    for i in range(s, len(data)):
        val = data[i]
        if state == 'low':
            if val >= up:
                state = 'up'
                result.append((i, 1))
        elif state == 'up':
            if val >= down:
                state = 'up2'
        elif state == 'up2':
            if val >= high:
                state = 'high'
        elif state == 'high':
            if val < down:
                state = 'down'
                result.append((i, 0))
        elif state == 'down':
            if val < up:
                state = 'down2'
        elif state == 'down2':
            if val < low:
                state = 'low'

    return result


up, high, down, low = .15, .67, .5, .07  # wait 60
#up, high, down, low = .15, .82, .55, .09  # wait
#up, high, down, low = .3, .87, .61, .17  # rt
#up, high, down, low = .15, .82, .67, .09  # vanilla
digital = np.loadtxt(r'C:\Users\Matthew Einhorn\Desktop\digital_wait_60.csv', delimiter=',')
analog = np.loadtxt(r'C:\Users\Matthew Einhorn\Desktop\analog_wait_60.csv', delimiter=',', usecols=(0, 1))

digital2 = np.zeros((2 * digital.shape[0] - 1, 2))
digital2[::2, :] = digital[:, :]
digital2[1::2, 0] = digital[1:, 0]
digital2[1::2, 1] = digital[:-1, 1]
analog[:, 1] /= np.max(analog[:, 1])
analog[:, 1] = signal.medfilt(analog[:, 1])

states = np.array(schmitt_trigger(up, high, down, low, analog[:, 1]), dtype=np.float64)
states[:, 0] = analog[map(int, states[:, 0]), 0]
states2 = np.zeros((2 * states.shape[0] - 1, 2))
states2[::2, :] = states[:, :]
states2[1::2, 0] = states[1:, 0]
states2[1::2, 1] = states[:-1, 1]

plt.plot(digital2[:, 0], digital2[:, 1])
plt.plot(analog[:, 0], analog[:, 1])
plt.plot(states2[:, 0], states2[:, 1])
plt.show()

t_img = states[:, 0]
t_io = digital[:len(t_img), 0]
plt.plot(t_img[1:], t_io[1:] - t_img[1:])
plt.xlabel('Time (s)')
plt.ylabel('flip to io delay (s)')
plt.show()

plt.hist(t_io[1:] - t_img[1:], bins=50)
plt.xlabel('Delay (s)')
plt.ylabel('Count')
plt.show()

plt.hist(t_img[1:] - t_img[:-1], bins=50)
plt.xlabel('Light/dark frame duration (s)')
plt.ylabel('Count')
plt.show()
