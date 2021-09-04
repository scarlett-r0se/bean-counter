import csv
import random
import string

from discord.utils import find
globalBeans=[]
class Beans:
    def getBeanBank():
        beans=[]
        
        with open('BeanBank.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are \n{", ".join(row)}')
                    line_count += 1
                else:
                    beans.insert(line_count, [row[0],row[1],row[2]])
                    print(f'\tUSER:{row[0]} ID:{row[1]} has {row[2]} Beans.')
                    line_count += 1
            print(f'Imported {line_count-1} lines.')
        
        return beans

    def getTotalbeans(beans):
       result = Beans.findBeanAccount(beans,'69')
       index = result[0]
       accountExists = result[1]
       if accountExists:
        return int(beans[index][2])
       else:
           return 0
    
    def totalBranchBeans(beans):
        beanCount=0
        for bean in beans:
            if bean[1] !='69':
                beanCount = beanCount + int(bean[2])

        return beanCount
            

    def setBeanBank(beans):
        # field names 
        fields = ['username','user-id','beans']
            
        # name of csv file 
        filename = "BeanBank.csv"
            
        # writing to csv file 
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
                
            # writing the fields 
            csvwriter.writerow(fields) 
                
            # writing the data rows 
            csvwriter.writerows(beans)

    def beanLog(beans,userName1,userid1,beansAmount,username2,userid2):
        characters = string.ascii_letters + string.digits + string.punctuation
        transid = ''.join(random.choice(characters) for i in range(8))
        print("Transaction ID is",transid)
        
        return 0


    def findBeanAccount(beans,userid):
        print('Looking up Bean account...')
        index=0        
        for id in beans:
            #print(id[1])
            if id[1] == userid:
                break
            else:
                index=index+1

        if index == len(beans):
            index=-1
            print('Bean account NOT found!')
            return [index,False]
            
        else:
            print('Bean account found at',index)
            return [index,True]
            
    
        return index

    def boolBeanAccount(beans,userid):
        print('Looking up Bean account...')
        index=0
        for id in beans:
            #print(id[1])
            if id[1] == userid:
                break
            else:
                index=index+1

        if index == len(beans):
            print('Bean account NOT found!')
            return False
        else:
            print('Bean account found')
            return True
    


    def depositBeans(beans,index,beansAmount):
        
        print('Value pre-deposit\n',beans[index])
        
        beansValue = int(beans[index][2]) + beansAmount
        beansValue=str(beansValue)
        
        beans.insert(index,(beans[index][0],beans[index][1],beansValue))
        print('Value post-deposit\n',beans[index])

        return beans
    
    def withdrawlBeans(beans,index,beansAmount):
        print('Value pre-withdrawl\n',beans[index])
        
        beansValue = int(beans[index][2]) - beansAmount
        beansValue=str(beansValue)
        
        beans.insert(index,(beans[index][0],beans[index][1],beansValue))
        print('Value post-withdrawl\n',beans[index])
        return beans
    
    
    b = getBeanBank()
    setBeanBank(b)