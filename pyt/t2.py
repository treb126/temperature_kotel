tfile=open("/sys/bus/w1/devices/28-000004794177/w1_slave")
ttext=tfile.read()
tfile.close()
temp=ttext.split("\n")[1].split(" ")[9]
temperature2=float(temp[2:])/1000
print temperature2