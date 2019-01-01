import pigpio
pi = pigpio.pi()

#open an i2c connection to the BNO055
SDA = 2
SCL= 3
baud = 10000
i2c_address = 0x28  #0x29 is alternate if COM3 pin is changed
#OPR_MODE_reg = ?
NDOF_MODE_VAL=0b1100
mode_switch_time = 0.010 #wait ten milliseconds for the mode to change
END = 0
ESCAPE = 1
START = 2
STOP = 3
ADDRESS = 4
FLAGS = 5
READ = 6
WRITE = 7
WRITE_MASK = 0b0
READ_MASK = 0b1
ST_RESULT_ADDRESS = 0x36    # in page 0

i2c_bus = pi.bb_i2c_open(SDA, SCL, baud)

#things to do
# 1. check Power On Self Test reg ST_RESULT for a bit set (self test passed)
print(pi.bb_i2c_zip(SDA, [ADDRESS,i2c_address,START,WRITE,1,ST_RESULT_ADDRESS,START,WRITE,1,((i2c_address<<1)|READ_MASK),READ,1,STOP]))
# 2. run Build in Self Test. Check ST_RESULT.
# 3. set power mode (optional, defaults to normal)
# 4. Set calibration values (obtain from IMU_calibration.py)
# 5. Axis remap (optional)
# 6. Set Euler angles to Degrees
# 7. Set Data output format
# 8. change calibration offsets (optional)
# 9. set operation mode to fusion mode NDOF (set by writing to [OPR_MODE] register)
#    starts in config mode
# 10. wait for operation mode to change from config mode (7 ms)
# 11. start polling IMU at 100Hz.
# 12. get temp (optional)

#close the i2c bus
pi.bb_i2c_close(SDA)
