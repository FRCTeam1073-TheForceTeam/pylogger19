from networktables import NetworkTables
import time
import sys

NetworkTables.initialize()
sl = NetworkTables.getTable("SensorLogger")

logfile = open("./datalog.txt", "w");
logfile.write("# time ax ay az gx gy gz encl encr")

while True:
    millis = int(round(time.time() * 1000))
    accel = sl.getNumberArray("accel", [0,0,0])
    gyro = sl.getNumberArray("gyro", [0,0,0])
    enc = sl.getNumberArray("enc", [0,0])
    logfile.write("%f,%f,%f,%f,%f,%f,%f,%f,%f\n"
                  % (millis, accel[0],accel[1],accel[2],
                     gyro[0],gyro[1],gyro[2],
                     enc[0], enc[1]))

    # Run at 10Hz
    time.sleep(100)
