import time; from machine import Pin, PWM; list = [0,2,4]
def PWMChange(pinNumber, intensity, delayTime): pwm2 = PWM(Pin(pinNumber), freq=20000, duty=intensity); time.sleep_ms(delayTime)
def flashing():
    for elements in list: PWMChange(elements, 0, 10)
    for elements in list:
        for i in range (0,255): PWMChange(elements, i, 10)
        if i > 253:
            for i in range(255, 0, -1): PWMChange(elements, i, 10)
while True: flashing();
