import numpy as np
import matplotlib.pyplot as plt

# Example:

# Boltzmann constant k_B:
k_b = 1.380649e-23 #m2 kg s-2 K-1

# Header
def thermal_pressure(nden, temp):
  # Body
  """
  Function used to compute the thermal pressure of ideal gases.
  Inputs: nden (number density), temp (temperature)
  Output: prs (pressure)
  Author: W.E.B.B.
  Date created: 28/04/23
  Date modified: 26/02/2024
  Second modification: 19/02/2025
  """

  # What you compute
  prs = nden*k_b*temp

  # What you return
  return prs


# Call the function
ndens1 = 100. #m^{-3}
temp1 = 290 #K

pres1 = thermal_pressure(ndens1, temp1)

#print("The pressure in N/m^2 is:", pres1)



# Evaluate function using vectors
n_vector = np.arange(-3., 5., 0.1) # in log10 scale
T_vector = np.arange(1., 9., 0.1) # in log10 scale

# Create a 2D grid
n_2D, T_2D = np.meshgrid(n_vector, T_vector)

#print(n_vector.shape)
#print(T_vector.shape)
#print(n_2D.shape, T_2D.shape)   



# Call the function:

pres_2D = thermal_pressure(10**n_2D, 10**T_2D) # This is to fee the function with linear quantities

#print(pres_2D.shape)




#  Ready to plot the solution (2d array)

plt.figure()

# This is to plot a surface
Z = plt.pcolor(n_2D, T_2D, np.log10(pres_2D))

plt.plot(np.log10(ndens1), np.log10(temp1), linestyle = " ", marker = "o", color = "white")

# Add a colour bar
plt.colorbar(Z)

# Axes labels
plt.xlabel(r"$\log_{10}(n) [m^{-3}]$")
plt.ylabel(r"$\log_{10}(T) [K]$")

plt.show()




# Surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(n_2D, T_2D, np.log10(pres_2D), cmap = 'viridis')

ax.set_xlabel(r"$\log_{10}(n) [m^{-3}]$")
ax.set_ylabel(r"$\log_{10}(T) [K]$")

plt.show()