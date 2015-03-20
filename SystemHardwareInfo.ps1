$System = Get-CimInstance CIM_ComputerSystem
$BIOS = Get-CimInstance CIM_BIOSElement
$OS = Get-CimInstance CIM_OperatingSystem
$CPU = Get-CimInstance CIM_Processor
$HDD = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID = 'C:'"
$EXTXT = "$env:USERPROFILE\Desktop\welp.txt"
 
Clear-Host

$LISTMANU = "Model: " + $System.Manufacturer + " "
$LISTMODEL = $System.Model($LISTMODEL.length - 4, 4)
$LISTMANU + $LISTMODEL >> $EXTXT
"CPU: " + $CPU.Name >> $EXTXT
"RAM: " + "{0:N2}" -f ($System.TotalPhysicalMemory/1GB) + "GB" >> $EXTXT
"HDD Capacity: "  + "{0:N2}" -f ($HDD.Size/1GB) + "GB" >> $EXTXT
"Operating System: " + $OS.caption >> $EXTXT