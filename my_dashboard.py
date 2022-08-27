"""Make a simple dashboard with streamlit"""
# Import main libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import streamlit as st


# set variables defining normal distribution: mean, standard deviation, sample size

mu_in = 50
std_in = 5
size  = 500

# define function to make normal distribution

def norm_dist(mean, std, size = 200):
    """Generate normal distribution from three inputs: mean, standard deviation
    and sample size (default value 200)"""

    return norm.rvs(mean, std, size)

# generate random number from normal distribution

data = norm_dist(mu_in, std_in, size)
print(f'Numpy array with numbers randomly extrated from Normal distribution with mean {mu_in} and standard deviation {std_in}\n')
print(f"The data type is {type(data)}, with length {len(data)}\n")
print(data)

# determine mean and standard deviation of randomly generated data

mu, std = norm.fit(data)
print(f"The mean value and standard deviation of generated data are {mu=:.2f} and {std=:.2f}, respectively")


#make simple plot

x = np.linspace(0, 100, 100)
y = norm.pdf(x, mu, std)

title = f"Fit results: mean, {mu=:.2f} and standard deviation, {std=:.2f}"
fig, ax = plt.subplots()
ax.hist(data, bins =200, density = True)
ax.plot(x, y, 'k', linewidth = 2)
ax.set_title(title)
plt.show()

st.pyplot(fig)


print('Script read correctly')