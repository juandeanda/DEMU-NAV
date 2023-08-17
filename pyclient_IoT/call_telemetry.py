#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import serial
import time
import io
from client_selfDriving2 import *
from datetime import datetime

Datain=''

Flag=False

datadir = '../Blockchain/keystore/UTC--2023-08-15T19-24-24.364683653Z--61b0a494871685f8f658d1c3e79f333f0c958763'
abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "key",
				"type": "string"
			}
		],
		"name": "get_Navigation_information",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "key",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "val",
				"type": "uint256"
			}
		],
		"name": "set_Navigation_information",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
address = "0x10F606699F2EDf10825b690fB14128160D3cA75E"
obj_client = Client("http://localhost:8545")
it = 0

def Send_BCH(Data):
    global obj_client, abi, address, datadir, it
    print(Data)
    now = datetime.now()
    key = obj_client.reedkey(datadir)
    robot_caller = "robot1_"+str(now.year)+"_"+str(now.month)+"_"+str(now.day)+"."+str(it)

    obj_client.connected(abi,key,address,robot_caller,Data)
    it = it+1
    print(robot_caller,"=",Data)
    #result=cl.call_sm(Data)
    #print("result:",result)

def Receive_data():
    while True:
        try:
            Datain=str(Serialport.read(12))
            Datain=Datain.lstrip('b')
            Datain=Datain.strip('\'')
            if(Datain.isnumeric()):
                Send_BCH(int(Datain))

            Datain=''
            Serialport.reset_input_buffer()
            Serialport.reset_output_buffer()
            break

        except KeyboardInterrupt:
            print("Exiting")
            break

        time.sleep(0.1)


try:
    Serialport=serial.Serial('/dev/ttyUSB0',115200, timeout=1)
    time.sleep(1.8)
    Serialport.reset_input_buffer()
    Serialport.reset_output_buffer()

except serial.SerialException:
    print('Port is not available')
    Flag=True

except serial.portNotOpenError:
    print('Attempting to use a port that is not open')
    print('End of script')
    Flag=True


while True:
    if Flag:
        print('Serial device not connected!')
        time.sleep(0.2)
    else:
        Receive_data()
        time.sleep(0.2)
