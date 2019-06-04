# pylogger19
Python network-tables data logger

This repository is a Python3 / pynetwork tables program that
periodically logs sensor data to log files for analysis after matches.

This provides a network tables server at the Raspberry Pi
address with a table named "SensorLogger". This table
has the following keys:

accel - This is a networktables array of 3 numbers, default is [0,0,0]
gyro - This is a nettworktables array of 3 numbers, default is [0,0,0]
enc - This is a networktables array of 2 numbers, default is [0,0]

# File Format

Currently the logger opens a logfile named "datalog.csv" in the
directory where started. It writes one record per line with a #
comment header identifying fields.

Current line/record format is:

timestamp(in milliseconds), ax, ay, az, gx, gy, gz, enc_left, enc_right \n



