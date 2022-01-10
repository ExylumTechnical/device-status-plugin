#---------------------------------------------
#
# Programmed by Nicholas Howland in January 2022
#
#---------------------------------------------

from os import system
import time
def equipment_status(dest="./html/device-status.htm", lst="./equipment.list"):
	stat_page=open(dest,"w")
	stat_config=open(lst,"r")	
	status = []
	title = []
	devices=stat_config.readlines()
	for i in devices:
		equip=i.split(",")
		name = equip[1]
		title.append(name[:-1])
		status.append(ping_test(equip[0]))
	cmd="echo '' > "+str(dest)
	system(cmd)
	count =0
	for i in status:
		if(i==1):
			stat_page.write(str("<p style='font-size:23;'><img src='green.png'></img> "+title[count]+"</p>"))
		elif(i>0 and i<1): 	
			stat_page.write(str("<p style='font-size:23;'><img src='yellow.png'></img> "+title[count]+"</p>"))
		elif(i==0):
			stat_page.write(str("<p style='font-size:23;'><img src='red.png'></img> "+title[count]+"</p>"))
		count=count+1
	stat_page.close()


def ping_test(addr,count=5, temp="./ping.tmp"):
	cmd = "ping -c "+str(count)+" "+addr+" >"+temp
	system(cmd)
	pt = open(temp)
	pt_lns=pt.readlines()
	success = 0
	for i in pt_lns:
		if("64 bytes from" in i):
			success=success+1
		else:
			success=success
	system("rm ./ping.tmp")
	if(success>0):
		return success/count
	else:
		return 0

equipment_status()
