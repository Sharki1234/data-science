import matplotlib.pyplot as mpt
import pandas as p
# x = [1,2,3,4,5,6,7]
# y = [1,2,3,4,5,6,7]
# mpt.plot(x,y)#ro,g^,r--,g--,b--,b-,can be done as combinations with first letter as colour
# mpt.show()


# #mpt.axis([1,5,0,6])#limits axis
# #mpt.show()

# mpt.plot(x,y)
# mpt.xlabel("Xaxis")
# mpt.ylabel("Yaxis")
# mpt.legend()
# mpt.show()

# mpt.plot([1,2,3,4,5],[1,4,9,16,25],"r-",label = "Y=x^2",)
# mpt.plot([1,2,3,4,5],[3,12,27,42,75],"g-",label = "Y=x^2*3")
# mpt.axis([0,10,0,10])
# mpt.show()

# m = int(input("m?"))
# c = int(input("c?"))
# x = [1,2,3,4,5]
# y =[]
# for i in x:
#     y.append(int(i*m)+c)
# mpt.plot(x,y)
# mpt.show()

# mpt.bar([1,2,3,4,5],[2,4,6,8,10],color = "b")#x can be labels aswell
# mpt.bar([6,7,8,9,0],[2,5,6,18,10],color = "g")
# #mpt.bar(["Female","Male"],[17,6])
# mpt.show()
titanic = p.read_csv(r"C:\Users\rakhi\Downloads\titanic.csv")
pclass_grouped = titanic["Pclass"].value_counts()
pclass = [1,2,3]
value = [pclass_grouped[1],pclass_grouped[2],pclass_grouped[3]]
mpt.bar(pclass,value)
mpt.show()