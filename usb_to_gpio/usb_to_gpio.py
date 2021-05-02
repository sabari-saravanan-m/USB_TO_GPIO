"""
Author                          : SABARI SARAVANAN M
Developed Tool and Version      : Python 3.9
Description                     : General functions for HPA172 USB interface adapter
Module Name                     : USB-TO-GPIO
Module Version                  : 0.0.1
Created                         : April 2021
"""

import clr                                                                                          # Import clr from 'pythonnet' to interface runtime engine with .net
from System import Byte

class USB_TO_GPIO(object):

    def __init__(self):
        """ SAA adapter constructor -  discovering a device via the SMBus API.
            This library file provides you with the information required to use functions for remotely controlling your instrument.

            from usb-to-gpio import USB_TO_GPIO                                             # Importing USB_TO_GPIO file

            TI = USB_TO_GPIO()                                                              # Initialize & opens an instrument reference

            TI.configure(pec_enabled=False)                                                 # Selects 100-KHz/400-KHz bus speed & PEC mode
            TI.send_byte(dev_addr=0x001, cmd_addr=0x00)                                     # Performs a “Send_Byte”
            TI.write_byte(dev_addr=0x01, cmd_addr=0x00, data=0x00)                          # Performs a “Write_Byte”

            TI.close()                                                                      # Close the device reference

        """
        try:
            clr.AddReference("C:\\Program Files (x86)\\Texas Instruments Fusion API\\Library\\TIDP.SAA.dll")    # Load the dll file(C:\\ folder)
            import TIDP.SAA as API                                                                              # Import TIDP.SAA dll file

            if API.SMBusAdapter.Discover() != 0:                                                                # Find an adapter
                self.device = API.SMBusAdapter.Adapter                                                          # Import class from C# namespace
                print('Device has opened')
            else:
                print("No Adapter Found")
        except:
            import_error()

    def __repr__(self):
        ''' print statement to compute the "informal" string representation of an object '''
        return repr(self.device)

    ###########################################
    # Error Handler
    ###########################################

    def import_error(self):
        ''' Update import error reported by the system of loading dll driver error.
        '''
        print("dll file not loaded, 'TI USB-TO-GPIO driver was not present/installed'.")
        exit()

    def exception_handler(self, exception):
        print("Exception occured:", exception)

    ###########################################
    # SMBus Adapter
    ###########################################

    def configure(self, pec_enabled=False):
        ''' Select 100-KHz/400-KHz bus speed & PEC mode'''
        self.device.Set_Bus_Speed(self.device.BusSpeed.Speed100KHz)
        self.device.Set_PEC_Enabled(pec_enabled)

    def send_byte(self, dev_addr, cmd_addr):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'

        Returns:
            (bool) True if successful
            (bool) False otherwise
        '''
        try:
            if self.device.Send_Byte(Byte(dev_addr), Byte(cmd_addr)) == 0:                  # 0 = received acknowledgement
                return 'Success'

        except Exception as ex:
            self.exception_handler(ex)

    def write_byte(self, dev_addr, cmd_addr, data):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'
            (uint8) data = Data Byte to Write (0-255) - b'\xFF'

        Returns:
            (bool) True if successful
            (bool) False otherwise
        '''
        try:
            if self.device.Write_Byte(Byte(dev_addr), Byte(cmd_addr), Byte(data)) == 0:     # 0 = received acknowledgement
                return 'Success'

        except Exception as ex:
            self.exception_handler(ex)

    def read_byte(self, dev_addr, cmd_addr):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'

        Returns:
            (uint8) Data Byte if successful
            NACK otherwise
        '''
        try:
            status = self.device.Read_Byte(Byte(dev_addr), Byte(cmd_addr))
            if status.SAA_Status == 'ACK':
                return int(status.Data.Hex, base=16)
            else:
                return 'NACK'

        except Exception as ex:
            self.exception_handler(ex)

    def i2c_write(self, byteaddr=0x70, bytecmd=0x04, bytedata=[0x00]):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'
            (uint8) data = Data Byte to Write (0-255) - b'\xFF'

        Returns:
            (uint8) Data Byte if successful
            NACK otherwise
        '''
        try:
            if self.device.I2C_Write(Byte(byteaddr), Byte(bytecmd), bytes(bytedata)) == 0:
                return 'Success'

        except Exception as ex:
            self.exception_handler(ex)

    def close(self):
        try:
            self.device.Dispose()
            print('Device has closed')
        except Exception as ex:
            self.exception_handler(ex)
