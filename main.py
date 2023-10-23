import numpy as np
import matplotlib.pyplot as plt

my_data = np.array([55, 67, 28, 235, 114])
x_axis = np.arange(len(my_data))
my_mean = my_data.mean()
my_stdev = my_data.std()


my_data_normed = (my_data - my_mean) / my_data.std()

my_data_domain_standardised = (my_data - my_data.min()) / (my_data.max() - my_data.min())


fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(10,5))
ax1.plot(x_axis,my_data)
ax1.set_title('Original')
ax2.plot(x_axis,my_data_normed)
ax2.set_title('Normalised \n(mean = 0, stddev = 1)')
ax3.plot(x_axis,my_data_domain_standardised)
ax3.set_title('Domain standardised \n(data points between 0 and 1)')
plt.show()