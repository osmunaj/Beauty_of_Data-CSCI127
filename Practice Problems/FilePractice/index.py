import math

myfile = open("text.txt","w")
myfile.write("here's some data: \n")

for i  in range(1,10+1):
    #print(i," Times pi is", i*math.pi)

    myfile.write(str(i)+" Times pi is "+str(i*math.pi)+"\n")    
myfile.close()
