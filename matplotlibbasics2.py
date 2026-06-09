import matplotlib.pyplot as mpb
#histogram
# ages = [22,23,26,68,7,9,34,6,89,90,12,15,17,26]
# bins = [0,10,20,30,40,50,60,70,80,90,100]
# mpb.hist(ages,bins,histtype="bar",rwidth = 0.8)
# mpb.xlabel("Age")
# mpb.ylabel("Frequency")
# mpb.title("HIstogram")
# mpb.show()

# #pie chart
# slices = [1,2,3,4,5]
# activities = ["Swimming","Running","Dance","Rounders","Football"]
# col = ["c","m","r","b","g"]
# mpb.pie(slices,labels = activities,colors=col,shadow=True)
# mpb.show()

#stackplot
# days = [0,1,2,3,4,5]
# eating =[1,4,5,8,3,8]
# sleeping = [3,6,7,4,9,4]
# playing = [2,5,8,3,7,9]

# mpb.plot([],[],color = "m",label = "Eating",linewidth = 5)
# mpb.plot([],[],color = "c",label = "Sleeping",linewidth = 5)
# mpb.plot([],[],color = "r",label = "Playing",linewidth = 5)
# mpb.stackplot(days,eating,sleeping,playing,colors = ["m","c","r"])
# mpb.show()

#subplot
import numpy as np
def f(x):
    return np.cos(2*np.pi*x)*np.exp(-x)
x1 = np.arange(0,5)
x2 = np.arange(0,5)

mpb.figure()
mpb.subplot(221)
mpb.plot(x1,f(x1),"bo")

mpb.subplot(224)
mpb.plot(x2,np.cos(2*np.pi*x2))

mpb.show()