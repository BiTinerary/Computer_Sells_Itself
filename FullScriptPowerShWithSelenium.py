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

MODELPRNT = str("Model: " + MANUFACTURER + " " + MODEL)
HDDPRNT = str("HDD: " + str(HDDTOTAL) + "GB")
RAMPRNT = str("RAM: " + str(RAMTOTAL) + "GB")
CPUPRNT = str("CPU: " + CPUINFO.name)
OSPRNT = str("OS: " + OSINFO.caption)

def ALLTHESPECS():
	MODELPRNT = str("Model: " + MANUFACTURER + " " + MODEL)
	HDDPRNT = str("HDD: " + str(HDDTOTAL) + "GB")
	RAMPRNT = str("RAM: " + str(RAMTOTAL) + "GB")
	CPUPRNT = str("CPU: " + CPUINFO.name)
	OSPRNT = str("OS: " + OSINFO.caption)

os.system('cls')

print ALLTHESPECS()
print "\r"
print MODELPRNT
print "\r"
print HDDPRNT
print RAMPRNT
print CPUPRNT
print OSPRNT

with open('selenium_header.txt','r') as a, open('selenium_body_repeated.txt','r') as b, open('selenium_footer.txt','r') as c:
    
    html_header = a.read()
    body_repeat = b.read()
    html_footer = c.read()

lenghead = str(len(html_header))
lengbody = str(len(body_repeat))
lengfoot = str(len(html_footer))

print("\r\n")
print("Selenium Header Length: ") + lenghead
print("Selenium Body Length: ") + lengbody
print("Selenium Footer Length: ") + lengfoot

listinginfo = [[MODELPRNT,HDDPRNT,RAMPRNT,CPUPRNT,OSPRNT]]

final_html = ""
final_html += html_header

for line in listinginfo:
	model_numba = line[0]
	hdd_capacity = line[1]
	ram_capacity = line[2]
	cpu_specs = line[3]
	os_type = line[4]
	final_html += str(body_repeat.replace('MAKEMANU',model_numba).replace('MODELNAMENUMBER',model_numba).replace('POSTINGTITLE',hdd_capacity))
"""
full_sku = "${LOADID}-${STORAGE}-${INITIALS}-${SKUZ}"
noteone = "${"
notetwo = "}"
"""
	
final_html += html_footer
    
with open('Final_Selenium_Output','w+') as f:
    f.write(final_html)
	
	
print('DONE.')
