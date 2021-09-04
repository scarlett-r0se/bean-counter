import csv
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
    
    
    #findBeanAccount(getBeanBank(), '176784920465768448')
    #withdrawlBeans(getBeanBank(),findBeanAccount(getBeanBank(), '687144803973369532'),1000)
    #depositBeans(getBeanBank(),findBeanAccount(getBeanBank(), '274474601800753552'),1000)