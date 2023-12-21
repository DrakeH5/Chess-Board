import serial

SerialObj = serial.Serial('/dev/tty.usbmodem101') # COMxx  format on Windows     ttyUSBx format on Linux
SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8   # Number of data bits = 8
SerialObj.parity  ='N'   # No parity
SerialObj.stopbits = 1   # Number of Stop bits = 1

def ArduinoCommunication(x1, y1, x2, y2):
    message = str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2)
    SerialObj.write(bytes(message, "utf-8"))


#SerialObj.close()      # Close the port
