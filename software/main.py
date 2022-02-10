from machine import Pin

BUTTON_GPIO = 26

R_PIN = ...
G_PIN = ...
B_PIN = ...

count = 0

gpioR = Pin(R_PIN, Pin.OUT)
gpioG = Pin(G_PIN, Pin.OUT)
gpioB = Pin(B_PIN, Pin.OUT)


def set_led_color(r, g, b):
    if r:
        gpioR.on()
    else:
        gpioR.off()

    if g:
        gpioG.on()
    else:
        gpioG.off()

    if b:
        gpioB.on()
    else:
        gpioB.off()


def irq(pin):
    count++
    if count == 1:
        set_led_color(True, False, False)
    elif count == 2:
        set_led_color(False, True, False)
    elif count == 3:
        set_led_color(False, False, True)
    elif count == 4:
        set_led_color(True, True, True)
    elif count >=5:
        count = 0


gpio = Pin(BUTTON_GPIO, Pin.IN, Pin.PULL_DOWN)
gpio.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=irq)