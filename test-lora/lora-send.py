# -*- coding: utf-8 -*-
# LoRa Send Program
# Last updated: 2024.08.07
# Created by: Andrei Casimina

import serial
import datetime
import time
import subprocess

subprocess.call(["sudo","systemctl","stop","serial-getty@ttyS0.service"])
subprocess.call(["sudo","systemctl","disable","serial-getty@ttyS0.service"])

con = serial.Serial(               #LoRa用の設定
        port = "/dev/ttyS0",           #RasPiシリアル通信を用いる
        baudrate = 115200,                 #baudレート
        parity = serial.PARITY_NONE,     #パリティ
        bytesize = serial.EIGHTBITS,     #データのビット数
        stopbits = serial.STOPBITS_ONE,  #ストップビット数
        timeout = 5,                  #タイムアウト値
        xonxoff = 0,                     #ソフトウェアフロー制御
        rtscts = 0,                      #RTS/CTSフロー制御
    )

time.sleep(1)

while True:
    print("Trying to send message...")

    message = "Hello, I am transmitter-a!\r\n"        
    con.write(message.encode())

    reply_message = con.readline()
    reply_message = reply_message.decode()

    print(reply_message)
        
    con.flushInput()
    con.flushOutput()