import pandas as pd
class Node:
    def __init__(self,split = None,left = None,right = None,value = None):
        self.split = split
        self.left = left
        self.right = right
        self.value = value
class decision_tree:

    def impurity(self,y):
        n = len(y)
        count = {}
        for k in range(n):
            if y[k] in count:
                count[y[k]] +=1
            else:
                count[y[k]] = 1
        
        total = 0
        for value in count:
            p = ((count[value]/n) ** 2)
            total+=p
        return(1-total)
    def majority_label(self,y):
        n = len(y)
        count = {}
        for k in range(n):
            if y[k] in count:
                count[y[k]] +=1
            else:
                count[y[k]] = 1
        max_label = None
        maximum = 0
        
        for value in count:
            if count[value]>maximum:
                maximum = count[value]
                max_label = value
        return max_label

    def information_gain(self,start,end):
        return start-end
    def best_split(self,x,y):
        sorted_x = sorted(x)
        n = len(x)
        split_areas = []
        start_impurity = self.impurity(y)
        best_s = None
        best_gain = 0

        for i in range(0,len(sorted_x)-1):
            mid = (sorted_x[i]+sorted_x[i+1])/2
            split_areas.append(mid)
        for split in split_areas:
            leftx = []
            rightx =[]
            righty = []
            lefty = []
            for j in range(len(x)):
                if x[j]<split:
                    leftx.append(x[j])
                    lefty.append(y[j])
                else:
                    rightx.append(x[j])
                    righty.append(y[j])
            if len(lefty) == 0 or len(righty) == 0:
                continue
            left_impurity = self.impurity(lefty)
            right_impurity = self.impurity(righty)
            weighted = ((len(lefty)/n)*left_impurity)+((len(righty)/n)*right_impurity)
            gain = self.information_gain(start_impurity,weighted)
            if gain>best_gain:
                best_s = split
                best_gain = gain
        return best_s
    def build(self,x,y):
        
        x2 = x
        y2 = y


        split = self.best_split(x2,y2)
        if len(set(y2)) == 1:
            return Node(value=y2[0])
        if split == None:
            return Node(value=self.majority_label(y2))
        leftx =[]
        rightx = []
        lefty =[]
        righty = []
        for i in range(len(x2)):
            if x2[i]<split:
                leftx.append(x2[i])
                lefty.append(y2[i])
            else:
                rightx.append(x2[i])
                righty.append(y2[i])
        right_child = self.build(rightx,righty)
        left_child = self.build(leftx,lefty)
        node = Node(split,left_child,right_child)
        return node

def predict(tree,value):
    if tree.left == None and tree.right == None:
        return tree.value
    else:
        if value<tree.split:
            return predict(tree.left,value)
        else:
            return predict(tree.right,value)

def accuracy(tree,percentage,x,y):
    accurate = 0
    num = 0
    for i in range(len(x)):
        num+=1
        if predict(tree,x[i])==y[i]:
            accurate+=1
    return(accurate/num)






height = [13,25,12,11,19]
classes = ["A","B","A","C","A"]
tree = decision_tree()
root = tree.build(height,classes)
print(predict(root,12.5))

data=pd.read_csv(r"C:\Users\rakhi\Downloads\iris.csv")
y = list(data["species"])
x = list(data["sepal_length"])
tree = decision_tree()
root = tree.build(x,y)
print(predict(root,7.4))
print(accuracy(tree,2,x,y))