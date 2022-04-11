# radiometer_eqn

Computes S/N of a single radio pulse of width dt and peak flux density S. 

Needs to know the telescope gain, G, the bandwidth BW, system temperature Tsys
and number of poles, Np

Units of G, BW and Tsys are in K/Jy, MHz, K.

S is in Jy. 

Peak width dt is in seconds.

Example use for the Vela pulsar at Molonglo (EW arm):

python radiometer_eqn.py -bw 15 -np 1 -tsys 300 -G 1.8 -S 100 -d 0.003 

BW =  15.0 MHz 
Np =  1 polarisations
Tsys =  300.0 K
G =  1.8 K/Jy
S =  100.0 Jy
dt =  0.003  sec

SNR =  127.27922061357856

Pulses typically have an SNR of 150 in observations. 
