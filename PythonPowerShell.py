import os
import wmi
import math

c = wmi.WMI()    
SYSINFO = c.Win32_ComputerSystem()[0]
OSINFO = c.Win32_OperatingSystem()[0]
CPUINFO = c.Win32_Processor()[0]
HDDINFO = c.Win32_LogicalDisk()[0]
RAMINFO = c.Win32_PhysicalMemory()[0]

MANUFACTURER = SYSINFO.Manufacturer
MODEL = SYSINFO.Model
RAMTOTAL = int(SYSINFO.TotalPhysicalMemory) / 960000000 # rounding doesn't work
HDDTOTAL = int(HDDINFO.size) / 982000000 # rounding doesn't work
RAMSIZE = round(RAMTOTAL) # rounding doesn't work
HDDSIZE = round(HDDTOTAL) # rounding doesn't work

os.system('cls')
print "Model: " + MANUFACTURER + " " + MODEL
print "\r"
print "HDD: " + str(HDDTOTAL) + "GB"
print "RAM: " + str(RAMTOTAL) + "GB"
print "CPU: " + CPUINFO.name
print "OS: " + OSINFO.caption

"""
DIRECT POWERSHELL COMMANDS (FOR REFERENCE)

EXTXT = "$env:USERPROFILE\Desktop\welp.txt"
LISTCPU = "CPU: " + CPU.Name >> EXTXT
"RAM: " + "{0:N2}" -f (System.TotalPhysicalMemory/1GB) + "GB" >> EXTXT
"HDD Capacity: "  + "{0:N2}" -f (HDD.Size/1GB) + "GB" >> EXTXT
"Operating Systemzz: " + OS.caption + "`r`n" >> EXTXT
"""