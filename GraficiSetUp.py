import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file1 = "DATA\CH1.csv"
file2 = "DATA\CH2.csv"
file3 = "DATA\CH3.csv"
file4 = "DATA\CH4.csv"

CH1 = pd.read_csv(file1)
CH2 = pd.read_csv(file2)
CH3 = pd.read_csv(file3)
CH4 = pd.read_csv(file4)

V1 = np.array(CH1.V)
dV1 = np.array(CH1.dV)
Count1 = np.array(CH1.Count)
dCount1 = np.array(CH1.dCount)

V2 = np.array(CH2.V)
dV2 = np.array(CH2.dV)
Count2 = np.array(CH2.Count)
dCount2 = np.array(CH2.dCount)

V3 = np.array(CH3.V)
dV3 = np.array(CH3.dV)
Count3 = np.array(CH3.Count)
dCount3 = np.array(CH3.dCount)

V4 = np.array(CH4.V)
dV4 = np.array(CH4.dV)
Count4 = np.array(CH4.Count)
dCount4 = np.array(CH4.dCount)

plt.figure(figsize=(12, 11))
plt.subplot(221)
plt.title("CH1 set up")
plt.errorbar(V1, Count1, dCount1, dV1, linestyle="-", marker="o", linewidth=1, capsize=4)
plt.xlabel("$V[V]$")
plt.ylabel("Counts")
plt.grid(which="both")
plt.subplot(222)
plt.title("CH2 set up")
plt.errorbar(V2, Count2, dCount2, dV2, linestyle="-", marker="o", linewidth=1, capsize=4)
plt.xlabel("$V[V]$")
plt.ylabel("Counts")
plt.grid(which="both")
plt.subplot(223)
plt.title("CH3 set up")
plt.errorbar(V3, Count3, dCount3, dV3, linestyle="-", marker="o", linewidth=1, capsize=4)
plt.xlabel("$V[V]$")
plt.ylabel("Counts")
plt.grid(which="both")
plt.subplot(224)
plt.title("CH4 set up")
plt.errorbar(V4, Count4, dCount4, dV4, linestyle="-", marker="o", linewidth=1, capsize=4)
plt.xlabel("$V[V]$")
plt.ylabel("Counts")
plt.grid(which="both")
plt.savefig("PLOTS\Graph.png", transparent=None, dpi='figure', format="png",
            metadata=None, bbox_inches=None, pad_inches=0.01,
            facecolor='auto', edgecolor='auto', backend=None, )
plt.show()
