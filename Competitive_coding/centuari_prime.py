t = int(input())
kingdoms = []
vowels = ["A","E","I","O","U","a","E","I","O","U",]

for i in range(1,t +1) :
    k = input()
    kingdoms.append(k)
t=1


for i in kingdoms :
    if i[len(i)-1]== "y" or i[len(i)-1]== "Y" :
        print("Case #"+ str(t) +": "+ i + "is ruled by nobody.")
    elif i[len(i)-1] in vowels :
        print("Case #"+ str(t) +": "+ i + "is ruled by Alice.")
    else:
        print("Case #"+ str(t) +": "+ i + "is ruled by Bob.")
    
    t +=1
    
    