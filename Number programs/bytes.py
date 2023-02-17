#Python code to convert bytes to KB, MB, GB and TB

byte = int(input("Enter Bytes: "))

#Conversion to Kilobytes
kb = byte/1024
print("{} Kilo Bytes".format(kb))

#Conversion to Megabytes
mb = byte/(1024 * 1024)
print("{} MegaBytes".format(mb))

#Conversion to Gigabytes
gb = byte/(1024 * 1024 * 1024)
print("{} Giga Bytes".format(gb))

#Conversion to Terrabytes
tb = byte/(1024 * 1024 * 1024 * 1024)
print("{} Tera Bytes".format(tb))