# usb_to_gpio Package

![USB_TO_GPIO](https://github.com/sabari-saravanan-m/usb_to_gpio)

usb_to_gpio package makes easy to set up and run. The package contains a repository of peripheral classes and a system for running experiment procedures.

usb_to_gpio runs on Python 3.6, 3.7, 3.8 and 3.9, and is tested with continous-integration on Windows.


## Install

```bash
$ https://www.ni.com/en-in/support/downloads/drivers/download.ni-845x-driver-software.html#346270

$ pip install C:\..\Downloads\usb_to_gpio
```

## Simple Demo

```python
# import files
from usb_to_gpio import i2c, spi, spistream, dio

# import class instance and play
import usb_to_gpio                                                              # Importing USB_TO_GPIO file

TI = usb_to_gpio.USB_TO_GPIO()                                                  # Initialize & opens an instrument reference
TI.configure(pec_enabled=False)                                                 # Selects 100-KHz/400-KHz bus speed & PEC mode
TI.send_byte(dev_addr=0x001, cmd_addr=0x00)                                     # Performs a “Send_Byte”
TI.write_byte(dev_addr=0x01, cmd_addr=0x00, data=0x00)                          # Performs a “Write_Byte”
TI.close()                                                                      # Close the device reference
```

## Development

### Contributing

Long-term discussion and bug reports are maintained via GitHub Issues.
Code review is done via GitHub Pull Requests.
