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
HDDTOTAL = int(HDDINFO.size) / 999000000 # rounding doesn't work
RAMSIZE = round(RAMTOTAL) # rounding doesn't work
HDDSIZE = round(HDDTOTAL) # rounding doesn't work

MODELPRNT = str("Model: " + MANUFACTURER + " " + MODEL)
HDDPRNT = str("HDD: " + str(HDDTOTAL) + "GB")
RAMPRNT = str("RAM: " + str(RAMTOTAL) + "GB")
CPUPRNT = str("CPU: " + CPUINFO.name)
OSPRNT = str("OS: " + OSINFO.caption)

print("\r\n")
ASKCONTACT = "What contact name do you want listed? \n"
LISTCONTACT = raw_input(ASKCONTACT)
print("\r\n")
ASKNUMBA = "What telephone number do you want listed? \n"
PHONENUMBA = raw_input(ASKNUMBA)
print("\r\n")
ASKPRICE = "How much are you selling the computer for? \n"
PRICEDAT = raw_input(ASKPRICE)
print("\r\n")
TITLE = str(str(MANUFACTURER) + " " + str(MODEL) + " (" + str(RAMSIZE) + "GB RAM, " + str(HDDSIZE) + "GB HDD)")

os.system('cls')

def ALLTHESPECS():
	MODELPRNT = str("Model: " + MANUFACTURER + " " + MODEL)
	HDDPRNT = str("HDD: " + str(HDDTOTAL) + "GB")
	RAMPRNT = str("RAM: " + str(RAMTOTAL) + "GB")
	CPUPRNT = str("CPU: " + CPUINFO.name)
	OSPRNT = str("OS: " + OSINFO.caption)
	print MODELPRNT
	print HDDPRNT
	print RAMPRNT
	print CPUPRNT
	print OSPRNT

ALLTHESPECS()

def LISTINGDETAILS():
	print "\r"
	print("Listing Name: " + LISTCONTACT)
	print("Listing Phone Number: " + PHONENUMBA)
	print("Listing Asking Price: $" + PRICEDAT)
	print("Listing Title: " + TITLE)

LISTINGDETAILS()

with open('selenium_header.txt','r') as a, open('selenium_body_repeated.txt','r') as b, open('selenium_footer.txt','r') as c:
    
    html_header = a.read()
    body_repeat = b.read()
    html_footer = c.read()

lenghead = str(len(html_header))
lengbody = str(len(body_repeat))
lengfoot = str(len(html_footer))

print("\r")
print("Selenium Header Length: ") + lenghead
print("Selenium Body Length: ") + lengbody
print("Selenium Footer Length: ") + lengfoot

listinginfo = [[MODELPRNT,HDDPRNT,RAMPRNT,CPUPRNT,OSPRNT,PHONENUMBA,LISTCONTACT,TITLE,PRICEDAT]]

final_html = ""
final_html += html_header

for line in listinginfo:
	model_numba = line[0]
	hdd_capacity = line[1]
	ram_capacity = line[2]
	cpu_specs = line[3]
	os_type = line[4]
	telenumba = line[5]
	listedname = line[6]
	postedtitle = line[7]
	askingprice = line[8]
	final_html += str(body_repeat.replace('POSTINGBODY',model_numba + "\r" + hdd_capacity + "\r" + ram_capacity + "\r" + cpu_specs + "\r" + os_type).replace('PHONE',telenumba).replace('CONTACTNAME',listedname).replace('POSTINGTITLE',postedtitle).replace('PRICE',askingprice))
	
final_html += html_footer
    
with open('Final_Selenium_Output','w+') as f:
    f.write(final_html)
	
print('DONE.')
