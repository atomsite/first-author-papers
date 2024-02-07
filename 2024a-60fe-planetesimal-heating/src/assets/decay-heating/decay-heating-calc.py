import matplotlib.pyplot as plt
from numpy import exp,logspace


def decay_heating(t,m,E,tau):
  # Constants
  A     = 6.0221408e+23
  ln2   = 0.69314718056
  myr2s = 3.15576e+13
  mev2j = 1.60218e-13
  # Convert variables
  tau_sec = tau * myr2s
  t_sec   = t*myr2s
  Ej      = E * mev2j
  l       = ln2 / tau_sec
  # Calculate H0
  H   = (A/m) * Ej * l
  # Scale in accordance with decay law
  H  *= exp(-t_sec/tau_sec)
  return H

def heating_solarsystem(H,fss,Zss):
  Q = H*fss*Zss
  print(Q[0])
  return Q

# Define 
t_array = logspace(-2,1,1000)
# Calculate heating constant 
al26_q_array = decay_heating(t_array,25.9868919e-3,3.210,0.717)
fe60_q_array = decay_heating(t_array,59.93407e-3,2.712,2.600)
# Calculate solar system equivalents
al26_q_ss_array = heating_solarsystem(al26_q_array,0.0085,5.250e-5)
fe60_q_ss_array = heating_solarsystem(al26_q_array,0.1828,1.150e-8)

# Formatting
plt.rcParams.update({"text.usetex": True,
                     "font.family": "Computer Modern"})
fig, ax = plt.subplots(2, 1, sharex=True, sharey=False,figsize=(5,5))

# Plot one, mass normalised
ax[0].set_xscale("log")
ax[0].set_yscale("log")
ax[0].set_ylabel(r"$H$ (W$\,$kg$^{-1}$)")
ax[0].set_ylim(1e-6,1)
ax[0].set_xlim(1e-2,1e1)
ax[0].grid(True,which="both",linestyle=":")
# Plotting
ax[0].plot(t_array,al26_q_array,label="$^{26}$Al")
ax[0].plot(t_array,fe60_q_array,label="$^{60}$Fe")
# ax[0].legend()
# Plot 2, solar system normalised
ax[1].plot(t_array,al26_q_ss_array,label="$^{26}$Al")
ax[1].plot(t_array,fe60_q_ss_array,label="$^{60}$Fe")
ax[1].plot(t_array,al26_q_ss_array+fe60_q_ss_array,label="$Q_\\textrm{T}$",linestyle=":",c="red")
ax[1].legend()
ax[1].set_yscale("log")
ax[1].set_ylabel(r"$Q_\textrm{ss}$ (W$\,$kg$^{-1}$)")
ax[1].set_ylim(1e-14,1e-6)
ax[1].grid(True,which="both",linestyle=":")
# Handle common axis 
ax[1].sharex(ax[0])
ax[1].set_xlabel("$t$ (Myr)")
# Save figure
plt.savefig("decay_heating.pdf",bbox_inches="tight")


plt.figure(figsize=(5,3))

slrs = ["${^10}Be","${^26}Al","${^"]
