import csv
import random
import string
import datetime


from discord.utils import find
globalBeans=[]
class Beans:
    def getBeanBank():
        beans=[]
        
        with open('/discordBot/BeanBank.csv') as csv_file:
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
        filename = "/discordBot/BeanBank.csv"
            
        # writing to csv file 
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
                
            # writing the fields 
            csvwriter.writerow(fields) 
                
            # writing the data rows 
            csvwriter.writerows(beans)

    def beanLog(userid1,beanTrade,userid2):
        rowLog=[]        
        characters = string.ascii_letters + string.digits
        transid = ''.join(random.choice(characters) for i in range(32))        
        currentTime = str(datetime.datetime.now())
        filename="/discordBot/BeanBankLog.csv"
    
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are \n{", ".join(row)}')
                    line_count += 1
                else:
                    rowLog.insert(line_count, [row[0],row[1],row[2],row[3],row[4]])
                    print(f'\tuserid-source:{row[0]} beanTrade:{row[1]} userid-dest {row[2]} time: {row[3]} transid {row[4]}.')
                    line_count += 1
            #print(f'Imported {line_count-1} lines.')

        fields = ['userid-source','beanTrade','userid-dest','time','tansid']
        
        rowLog.append([userid1,beanTrade,userid2,currentTime,transid])
        print('Transaction:',rowLog)
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
                
            # writing the fields 
            csvwriter.writerow(fields) 
                
            # writing the data rows 
            csvwriter.writerows(rowLog)
        
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
        
        #print('Value pre-deposit\n',beans[index])
        
        beansValue = int(beans[index][2]) + beansAmount
        beansValue=str(beansValue)
        
        beans[index][2] = beansValue
        #print('Value post-deposit\n',beans[index])

        return beans
    
    def withdrawlBeans(beans,index,beansAmount):
        #print('Value pre-withdrawl\n',beans[index])
        
        beansValue = int(beans[index][2]) - beansAmount
        beansValue=str(beansValue)
        
        #beans.replace(index,(beans[index][0],beans[index][1],beansValue))
        beans[index][2] = beansValue
        #print('Value post-withdrawl\n',beans[index])
        return beans

    def getBeanBalance(beans,index):
        balance=int(beans[index][2])
        return balance
    
    