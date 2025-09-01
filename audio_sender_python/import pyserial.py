import serial
from time import time_ns
verbose = True

def send_data_block(uart, bytes, counter):
  length = len(bytes) - counter
  if length > 255: length = 255
  out = bytearray(length + 6)
  out[0] = 0x55                   # Head
  out[1] = 0x3C                   # Sync
  out[2] = 0x01                   # Block Type
  out[3] = length                 # Data length
  # Set the data
  for i in range(0, length):
    out[i + 4] = bytes[counter + i]
  # Compute checksum
  cs = 0
  for i in range (2, length + 6 - 2):
    cs += out[i]
  cs &= 0xFF
  out[length + 6 - 2] = cs        # Checksum
  out[length + 6 - 1] = 0x55      # Trailer
  counter += length
  r = uart.write(out)
  return counter

def show_verbose(message):
    if verbose is True: print(message)


def await_ack(uart, timeout=2000):
  buffer = bytes()
  now = (time_ns() // 1000000)
  while ((time_ns() // 1000000) - now) < timeout:
    if uart.in_waiting > 0:
      buffer += uart.read(uart.in_waiting)
      if "\n" in buffer.decode():
        show_verbose("RX: " + buffer[:-1].decode())
        return True
  # Error -- No Ack received
  return False

if __name__ == "__main__":
    import serial

    # Set your Pico's serial device here
    device = "/dev/ttyACM0"
    baudrate = 115200

    # Open serial port
    uart = serial.Serial(port=device, baudrate=baudrate)

    # Example data to send
    data_bytes = bytearray([0x01, 0x02, 0x03, 0x04, 0x05])

    # Send data in blocks
    counter = 0
    while counter < len(data_bytes):
        counter = send_data_block(uart, data_bytes, counter)
        if not await_ack(uart):
            print("No ACK received, aborting.")
            break

    uart.close()