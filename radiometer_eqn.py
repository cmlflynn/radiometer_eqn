import numpy as np

import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-t', action="store", dest="Tsys", type=float)
parser.add_argument('-dt', action="store", dest="dt", type=float)
parser.add_argument('-g', action="store", dest="gain", type=float)
parser.add_argument('-s', action="store", dest="S", type=float)
parser.add_argument('-bw', action="store", dest="bw", type=float)
parser.add_argument('-np', action="store", dest="np", type=int)

results = parser.parse_args()

print("BW = ",results.bw, "MHz ")
print("Np = ",results.np, "polarisations")
print("Tsys = ",results.Tsys, "K")
print("G = ",results.gain, "K/Jy")
print("S = ",results.S, "Jy")
print("dt = ",results.dt, " sec")

SNR = np.sqrt(results.bw*1e6*results.np*results.dt)*results.gain*results.S/results.Tsys

print("SNR = ",SNR)


    

