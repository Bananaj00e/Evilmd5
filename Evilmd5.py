#This script by Banana j00e

from colorama import Fore, Back, Style
import pyfiglet
import time
import os


os.system('clear')

ascii_banner = pyfiglet.figlet_format("EvilMd5")

print (Fore.RED + "        Welcome  To  Evilmd5    ")
print (Fore.RED + " ##################################")
print(Fore.RED + ascii_banner)
print (Fore.RED +" ##################################")
print (Fore.RED + "                        By Banana j00e")


print ("")
print ("")
print ("")
md5 = input ("Enter The Original file MD5 : ")
md52 = input ("Enter The Suspected File MD5 : ")

print ("")
print ("[*] Scanning The MD5")
time.sleep(1)
time.sleep(2)

if md5 == md52 :
 print ("")
 print ("")
 print (Fore.GREEN + "[*] This File Is Clean")

else :
  print ("")
  print ("")
  print (Fore.GREEN + "[*] This File is",Fore.RED +"Edited",Fore.GREEN + " (Can Be A Malware)")


