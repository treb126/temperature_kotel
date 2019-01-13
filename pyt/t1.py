tfile=open("/sys/bus/w1/devices/28-0000047938ac/w1_slave")
ttext=tfile.read()
tfile.close()
temp=ttext.split("\n")[1].split(" ")[9]
temperature1=float(temp[2:])/1000
print temperature1