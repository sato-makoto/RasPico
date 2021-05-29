import utime
import machine

# send message to serial port
# and blink LED

uart = machine.UART(0, 115200, bits=8, parity=None, stop=1)
uart.write('Hello, Serial World!\r\n'.encode())
fb = 'fizzbuzz\r\n'.encode()
b = 'buzz\r\n'.encode()
f = 'fizz\r\n'.encode()
def fizzbuzz(time):
    for x in range(1,time + 1):
        if(x%15==0):
            uart.write(fb)
        elif(x%5==0):
            uart.write(b)
        elif(x%3==0):
            uart.write(f)
        else:
            num = str(x) + '\r\n' 
            uart.write(num.encode())
            
def blink(sec):
    led_onboard = machine.Pin(25, machine.Pin.OUT)
    led_onboard.value(1)
    utime.sleep(sec)
    led_onboard.value(0)
while True:
    blink(1.5)
    fizzbuzz(2000)
        
