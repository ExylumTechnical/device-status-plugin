# device-status-plugin
This is a plugin to be used in an &lt;iframe> element of a webpage. The scripts will ping a device and see if it is reachable through an icmp echo, then update the plugin page with a status indicator.


# Basic operation
the primary script was designed in a linux environment. The script will ping a list of hosts located in the equipment.list file, then figure out the percentage of successful pings. The script will then produce a .htm page with the status of each device in a color format to the left of the device name.

<br>
<b>equipment.list</b>
<br>
This file should be a list of devices first the IP address then followed by the desired name for example
<br>
<b>192.168.1.1,Router</b>

# device-status.py
***equipment_status(dest="./html/device-status.htm", lst="./equipment.list")***
the variuble dest will be where the device-status plugin will be put
the lst variuble is where the list of equipment will be located
***ping_test(addr,count=5, temp="./ping.tmp"):***
addr : the destination IP address in string form
count : the number of pings to be sent out to the destination address the default value is 5
temp : the ping results will be dumped here default destination is in this same directory ***this file will be deleted once the pings are complete***
# Considerations
- The network that this plugin is used must allow icmp traffic from this host
- The list of hosts is not encrypted and is in plaintext so be sure that the context of which the script is run is secure enough for the devices that are being probed
- ***The status images must be put into the same destination directory as device-status.htm***
