# -*- coding: utf-8 -*-
# LoRa Receive Program
# Last updated: 2024.08.07
# Created by: Andrei Casimina

import serial
import time
import datetime
import subprocess
import os
import csv
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN #四捨五入用

subprocess.call(["sudo", "systemctl", "stop", "serial-getty@ttyS0.service"])
# subprocess.call(["sudo", "systemctl", "disable", "serial-getty@ttyS0.service"])
# 
con = serial.Serial(            #LoRa用の設定
    port = "/dev/ttyS0",        #Raspiシリアル通信を用いる
    baudrate = 115200,              #baudレート
    parity = serial.PARITY_NONE,    #パリティ
    bytesize = serial.EIGHTBITS,    #データのビット数
    stopbits  = serial.STOPBITS_ONE,    #ストップビット数
    timeout = 1,                  #タイムアウト値
    xonxoff = 0,                     #ソフトウェアフロー制御
    rtscts = 0,                      #RTS/CTSフロー制御
)

while True:
    try:
        print("Trying to read message...")
        received_message = con.readline().decode() #1行ごとに読み込み、処理を繰り返す

        if received_message != None:
            print(received_message)
            reply = "Got your message!\r\n"        
            con.write(reply.encode())
        else:
            print("No messages received!")
    except Exception as e:
        print(e)
    finally:
        con.flushInput()
        con.flushOutput()
