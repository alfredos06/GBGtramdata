import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Läs fil
df = pd.read_csv(r"C:\Users\Sara Svedberg\Desktop\Python\Goteborg_Sporvagnar\M34-607_log_can0.csv")

# Hämta signaler
tid = df["Time (ms)"]
unetz = df["T02_02:.UNETZ_02"]

# Funktion för 8-bitars konvertering
def int8_convert(v):
    if pd.isna(v):
        return np.nan
    v = int(v)
    # Konvertera 0-255 till -128 till 127
    if v > 127:
        return v - 256
    else:
        return v

# Konverter
itrak_int8 = df["T02_02:.ITRAK_02"].apply(int8_convert)

# Rita graf
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Övre graf
ax1.plot(tid, unetz, color="blue")
ax1.set_title("T02_02:.UNETZ_02")
ax1.set_ylabel("Värde")
ax1.grid(True)

# Nedre graf
ax2.plot(tid, itrak_int8, color="red")
ax2.set_title("T02_02:.ITRAK_02 (int8)")
ax2.set_xlabel("Tid (ms)")
ax2.set_ylabel("Värde")
ax2.grid(True)

plt.tight_layout()
plt.show()