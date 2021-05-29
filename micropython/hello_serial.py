from machine import UART
uart = UART(0, 115200, bits=8, parity=None, stop=1)
uart.write('シリアルポートから世界にこんにちは!\r\n'.encode())
