import matplotlib.pyplot as mpb

days = [0,1,2,3,4,5]
school =[1,4,5,8,3,8]
sleep = [3,6,7,4,9,4]
leisure = [2,5,8,3,7,9]
study = [2,5,8,3,7,4]

mpb.plot([],[],color = "m",label = "school",linewidth = 5)
mpb.plot([],[],color = "c",label = "Sleep",linewidth = 5)
mpb.plot([],[],color = "r",label = "leisure",linewidth = 5)
mpb.plot([],[],color = "r",label = "study",linewidth = 5)
mpb.stackplot(days,study,school,sleep,leisure,colors = ["m","c","r"])
mpb.show()

def sum(list):
    total = 0
    for i in list:
        total+=i
    return total
def maximum(list):
    maximum = 0
    for i in list:
        if i>maximum:
            maximum=i
    return maximum

activities = ["school","sleep","leisure","study"]
sums = [sum(school),sum(sleep),sum(leisure),sum(study)]
print(activities[sums.index(maximum(sums))])
