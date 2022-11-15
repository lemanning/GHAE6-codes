from machine import PIN, ADC
from time import sleep

pot =ADC(A0)
pot.atten(ADC.ATTN_11DB)

while True:
    pot_value = pot.read()
    print(pot_value)
    sleep(0.1)