# This code is written for remotely controlling the TTI 1604 multimeter
def open_inst():
    import serial  # Import libraries
    import time

    serialcomm = serial.Serial()  # Open serial port
    serialcomm.port = 'COM6'  # Enter the name of the serial port
    print("Serial details parameters:", serialcomm)  # Print the serial port parameters
    serialcomm.setRTS(0)  # Give the correct value to connection lines RTS and DTR
    serialcomm.setDTR(1)

    serialcomm.open()  # Check if the port is open
    print(serialcomm.port)  # Get the current open serial name

    z = 'g'  # Open multimeter
    serialcomm.write(z.encode())
    i = 'u'  # Enter remote mode
    serialcomm.write(i.encode())
    time.sleep(1)
    j = 'n'  # Select the unit of measurement, 'f' stands for Volts
    serialcomm.write(j.encode())            # 'a' up, 'b' down, 'c' Auto, 'd' Ampere, 'e' mA, 'f' Volt, 'g' Operate, 'i' Ohm, 'j' Hz
                                            # 'k' Shift, 'l' AC, 'm' DC, 'n' mV, 'v' local mode

open_inst()








