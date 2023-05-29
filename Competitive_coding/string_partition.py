def partitionLabels(s):
        main_list = []
        main_list.append([s[0:1]])
        print (main_list)

        for i in s[1:len(s)] :
            length = len(main_list)
            c,ind,one = 0,0,0
            print (i , " : ",end=" ")

            for l in main_list :

                if one==1 :
                    break

                if i not in l :
                    c+=1
                    if c==length :
                        main_list.append([i])

                else :
                    one = one + 1

                    main_list[length - 1].append(i)
                    
                    temp_l = main_list[ind]
                    for x in range(ind+1,length) :
                        temp_l += main_list[x]
                    
                    del main_list[ind:length+1]
                    
                    main_list.append(temp_l)  


                ind +=1
            
            print (main_list)
        

        len_l = []
        for i in main_list :
            len_l.append(len(i))
        
        print (len_l)


partitionLabels("abaklij")