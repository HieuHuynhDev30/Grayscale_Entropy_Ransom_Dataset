import glob
import numpy as np

files = glob.glob("dll/entropy/*.npy")

X_entropy = np.stack([np.load(f) for f in files])
print(X_entropy)
