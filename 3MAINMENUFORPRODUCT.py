import pandas as pd
import datetime as dte
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt
print()
print()
print('           WELCOME TO PRODUCTS SEGMENT')
dfadminpass = pd.read_csv('D://MAJOR/MAJOREMPPASSWORD.csv',sep=' ',names=['PASSWORD'])
dfadminpass3=pd.DataFrame(dfadminpass)
adminpass3=str((dfadminpass3.loc['ADMIN PASSWORD','PASSWORD']))
adminpass=input('PLEASE ENTER ADMIN PASSWORD - ')
while(adminpass!=adminpass3):
    print('ADMIN PASSWORD ENTERED IS WRONG!!!!')                                
    adminpass=input('ENTER PASSWORD AGAIN- ')    
ch=''
while(ch.upper()!='X'):
    print('      MENU')
    print('Press A TO ADD NEW PRODUCT')
    print('Press B TO ADD NEW BRAND')
    print('Press C TO ADD NEW CATEGORY')
    print('Press D TO DELETE PRODUCT')
    print("Press E TO CHANGE PRODUCT's COST PRICE")
    print("Press F TO CHANGE PRODUCT's MARKET PRICE")
    print('Press S TO START SALE')
    print('Press N FOR ANALYSIS/VISUALS')
    print('Press I TO IMPORT PRODUCT')
    print('Press T TO SEE ALL TRANSACTIONS')
    print('Press P TO SEE ALL PRODUCT DETAILS PRICES,QUANTITY,STOCK LEFT,SOLD,etc')
    print('Press X TO EXIT',end='')
    ch=input('-')
    print()
    print()
    if(ch.upper()=='A'):        
        dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        dfproduct=pd.read_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')           
        llnofit1=dfproduct2["Unnamed: 0"].tolist()
        lbrand=dfproduct["Unnamed: 0"].tolist()
        dfproduct3a=dfproduct.set_index("Unnamed: 0")
        dfproductpr=dfproduct2.set_index("Unnamed: 0")
        lprice2=dfproductpr['MP'].tolist()
        lprice1=dfproductpr['CP'].tolist()
        LQTY=dfproductpr['QTY'].tolist()
        SQTY=dfproductpr['SQTY'].tolist()
        print('THESE ARE THE CATEGORIES YOU ARE HAVING:-')
        for i in dfproduct3a.columns:
            print(i)
        category2=input('Enter the category of new product\n')
        while(category2.upper() not in dfproduct3a.columns):
            category2=input('NO SUCH CATEGORY PRESENT PLEASE ENTER AGAIN!!\n')
        category=category2.upper()
        print()
        print('THESE ARE THE BRANDS YOU ARE HAVING:-')
        for i in dfproduct3a.index:
            print(i)
        brand2=input('Enter the brand of new product\n')
        while(brand2.upper() not in dfproduct3a.index):
            brand2=input('NO SUCH BRAND PRESENT PLEASE ENTER AGAIN!!\n')
        brand=brand2.upper()
        print()
        new_product2=input('Enter new product\n')
        new_product=new_product2.upper()
        llnofit1.append(new_product)
        price1=float(input('Enter its COST price ₹'))
        price2=float(input('Enter its MARKET price ₹'))
        lprice1.append(price1)               
        lprice2.append(price2)          
        LQTY.append(0)             
        SQTY.append(0)
        STproduct3=dfproduct3a.loc[brand,category]
        STproduct4=STproduct3.replace('[','')
        STproduct5=STproduct4.replace(']','')
        STproduct6=STproduct5.replace(', ',',')
        STproduct7=STproduct6.replace("'",'')
        Ldfproduct=list(STproduct7.split(','))
        Ldfproduct.append(new_product)
        lenl=len(Ldfproduct)
        dfproduct3a.loc[brand,category]=Ldfproduct
        dprice={'CP':lprice1,'MP':lprice2,'QTY':LQTY,'SQTY':SQTY}
        dfproduct2=pd.DataFrame(dprice,index=llnofit1)
        dfproduct2.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        dfproduct3a.to_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
        print('PRODUCT ADDED SUCCESFULLY!!!!!............')
    elif(ch.upper()=='B'):
        dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        dfproduct=pd.read_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')           
        llnofit1=dfproduct2["Unnamed: 0"].tolist()
        lbrand=dfproduct["Unnamed: 0"].tolist()
        dfproduct3a=dfproduct.set_index("Unnamed: 0")
        dfproductpr=dfproduct2.set_index("Unnamed: 0")
        lprice2=dfproductpr['MP'].tolist()
        lprice1=dfproductpr['CP'].tolist()
        LQTY=dfproductpr['QTY'].tolist()
        SQTY=dfproductpr['SQTY'].tolist()
        print('THESE ARE THE CATEGORIES YOU ARE HAVING:-')
        for i in dfproduct3a.columns:
            print(i)
        category2=input('Enter the category of new BRAND\n')
        while(category2.upper() not in dfproduct3a.columns):
            category2=input('NO SUCH CATEGORY PRESENT PLEASE ENTER AGAIN!!\n')
        category=category2.upper()
        print()
        brand2=input('Enter the name of new BRAND:-\n')
        while(brand2.upper()  in dfproduct3a.index):
            brand2=input('BRAND ALREADY PRESENT PLEASE ENTER AGAIN!!\n')
        brand=brand2.upper()
        print()
        llnofit=[]
        F=int(input('How many PRODUCTS are there of this BRAND'))           
        k=0
        for k in range(0,F):
            print('ENTER NAME OF PRODUCT',(k+1))
            B=input()
            price1=float(input('Enter its COST price ₹'))
            price2=float(input('Enter its MARKET price ₹'))
            llnofit.append(B.upper())
            llnofit1.append(B.upper())
            lprice1.append(price1)               
            lprice2.append(price2)          
            LQTY.append(0)             
            SQTY.append(0)
        dfproduct3a.loc[brand,category]=llnofit
        dprice={'CP':lprice1,'MP':lprice2,'QTY':LQTY,'SQTY':SQTY}
        dfproduct2=pd.DataFrame(dprice,index=llnofit1)
        print(dfproduct2)
        dfproduct2.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        dfproduct3a.to_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
        print()
        print('BRAND ADDED SUCCESSFULLY!!!!!!...........')
    
    elif(ch.upper()=='C'):
        dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        dfproduct=pd.read_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
        llnofit1=dfproduct2["Unnamed: 0"].tolist()
        lbrand=dfproduct["Unnamed: 0"].tolist()
        dfproduct3a=dfproduct.set_index("Unnamed: 0")
        dfproductpr=dfproduct2.set_index("Unnamed: 0")
        print('-------------------------------')
        print()
        print()
        print('THESE ARE THE CATEGORIES WE ARE ALREADY HAVING :-\n')
        lcat=dfproduct3a.columns
        for i in lcat:
            print(i)
        print()
        print('Enter name of new category')
        lprice2=dfproductpr['MP'].tolist()
        lprice1=dfproductpr['CP'].tolist()
        LQTY=dfproductpr['QTY'].tolist()
        SQTY=dfproductpr['SQTY'].tolist()
        a=input()
        b=int(input('How many brands are there in this category?\n'))
        j=0
        llnofit=[]
        for j in range(0,b):
            print('ENTER NAME OF BRAND',(j+1),':- ')
            C=input()
            lbrand.append(C)  
            F=int(input('How many PRODUCTS are there of this BRAND?\n'))           
            k=0
            for k in range(0,F):
                print('ENTER NAME OF PRODUCT',(k+1))
                B=input()
                price1=float(input('Enter its COST price ₹'))
                price2=float(input('Enter its MARKET price ₹'))
                llnofit.append(B.upper())
                llnofit1.append(B.upper())
                lprice1.append(price1)               
                lprice2.append(price2)          
                LQTY.append(0)             
                SQTY.append(0)
        dfproduct3a.loc[C,a]=llnofit
        print()
        dprice={'CP':lprice1,'MP':lprice2,'QTY':LQTY,'SQTY':SQTY}
        dfproduct2=pd.DataFrame(dprice,index=llnofit1)
        dfproduct2.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        dfproduct3a.to_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
        print('CATEGORY',a,' is added Successfully!!!!!!.............')  
    elif(ch.upper()=='D'):
        print('                 WELCOME TO DELETION SEGMENT')
        print('------------------------------------------------------------------')
        print()
        dfproduct=pd.read_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
        dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        if("Unnamed: 0"in dfproduct.columns):
            dfproduct3a=dfproduct.set_index("Unnamed: 0")
        else:
            dfproduct3a=pd.read_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
        if("Unnamed: 0"in dfproduct2.columns):
            dfproductpr=dfproduct2.set_index("Unnamed: 0")
        else:
            dfproductpr=dfproduct2.set_index("PRODUCT") 
        #print(dfproduct3a)
        dproduct=dfproduct3a.to_dict('list')
        lCATEGORY=dproduct.keys()
        print('CATEGORIES PRESENT IN YOUR STORE')
        names=dfproduct3a.columns.tolist()
        for i in range(0,len(names)):
            print(names[i])
        CAT=input('ENTER CATEGORY WHOSE PRODUCT YOU WANT TO DELETE:-')
        while(CAT.upper() not in dproduct.keys()):
            CAT=input('NO SUCH CATEGORY PRESENT PLEASE ENTER AGAIN')
        CAT2=CAT.upper()
        print()
        print()
        print('THESE ARE THE BRANDS WE ARE HAVING:-')
        names2=dfproduct3a.index.tolist()
        for i in range(0,len(names2)):
            print(names2[i])
        BRAND=input('ENTER BRAND WHOSE PRODUCT YOU WANT TO DELETE:-')
        while(BRAND.upper() not in names2):
            BRAND=input('NO SUCH BRAND PRESENT PLEASE ENTER AGAIN:-')
        BRAND2=BRAND.upper()
        STproduct3=str(dfproduct3a.loc[BRAND2,CAT2])##
        STproduct4=STproduct3.replace('[','')
        STproduct5=STproduct4.replace(']','')
        STproduct6=STproduct5.replace(', ',',')
        STproduct7=STproduct6.replace("'",'')
        Ldfproduct=list(STproduct7.split(','))
        lenl=len(Ldfproduct)
        print(CAT2,'OF',BRAND2,'ARE  :-')
        i=0
        while (i < lenl):
            i=i+1
            if(Ldfproduct[i-1]=='nan'):
                continue
            print(i-1,' for ',end='')
            print(Ldfproduct[i-1])
        print('ENTER RESPECTIVE GIVEN NUMBER FOR THE PRODUCT YOU WANT TO DELETE!!!\n')
        chi=int(input())
        dfproductpr2=dfproductpr.drop(Ldfproduct[chi],axis=0)
        dfproductpr2.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        Ldfproduct.pop(chi)
        for i in range(len(Ldfproduct)):
            Ldfproduct[i]=str(Ldfproduct[i])
        #print(Ldfproduct)
        #Ldfproduct2=map(str,Ldfproduct)
        #print(Ldfproduct2)
        dfproduct3a.loc[BRAND2,CAT2]=Ldfproduct
        dfproduct3a.to_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
        print('PRODUCT DELETED SUCCESFULLY!!!!!............')
    elif(ch.upper()=='E'):
        dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        LNAME=dfproduct2["Unnamed: 0"].tolist()
        dfproductpr=dfproduct2.set_index("Unnamed: 0")        
        print('THESE ARE THE PRODUCTS WE ARE HAVING :-')
        for i in LNAME:
            print(i)
        print()
        DEL2=input('Enter exact name of product whose COST PRICE you want to change:- ')
        DEL=DEL2.upper()
        ncp=float(input('ENTER new COST PRICE ₹'))       
        dfproductpr.loc[DEL,'CP']=ncp
        print('NEW COST PRICE:-',dfproductpr.loc[DEL,'CP'])
        dfproductpr.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        print('COST PRICE UPDATED SUCCESSFULLY!!!!!!!.....')
        #UPDATE TO ALL ITEMS
    elif(ch.upper()=='F'):
        dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        LNAME=dfproduct2["Unnamed: 0"].tolist()
        dfproductpr=dfproduct2.set_index("Unnamed: 0")
        print('THESE ARE THE PRODUCTS WE ARE HAVING :-')
        for i in LNAME:
            print(i)
        print()
        DEL2=input('Enter exact name of product whose COST PRICE you want to change:- ')
        DEL=DEL2.upper()
        print('OLD MARKET PRICE:-',dfproductpr.loc[DEL,'MP'])
        nmp=float(input('ENTER new MARKET PRICE ₹'))       
        dfproductpr.loc[DEL,'MP']=nmp
        print()
        print('NEW MARKET PRICE:- ₹',dfproductpr.loc[DEL,'MP'])
        dfproductpr.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        print('MARKET PRICE UPDATED SUCCESSFULLY!!!!!!!.....')  
    elif(ch.upper()=='I'):
        dfpassword2 = pd.read_csv('D://MAJOR/MAJOREMPPASSWORD.csv',sep=' ',names=['PASSWORD'])
        dfpassword3=pd.DataFrame(dfpassword2)
        passworddf=str((dfpassword3.loc['ATTEDANCE PASSWORD','PASSWORD']))
        pin=str((dfpassword3.loc['PIN','PASSWORD']))
        dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        dfproductpr=dfproduct2.set_index("Unnamed: 0")
        dfFINANCE = pd.read_csv('D://MAJOR/MAJORFINANCE.csv',sep=' ',names=['TOTAL'])
        dfFINANCE2=pd.DataFrame(dfFINANCE)
        dfproductpr.index.name="PRODUCT"
        print(dfproductpr.loc[:,['CP','QTY']])
        dfproductpr.index.name="Unnamed: 0"
        balance=float(dfFINANCE2.loc['SUM','TOTAL'])
        pp=0
        while(pp==0):
            DEL=input('Enter exact name of product which you want to import\n')
            while(DEL.upper() not in dfproductpr.index):
                DEL=input('NAME ENTERED WRONGLY!!!\nEnter exact name of product which you want to import\n')          
            DEL2=DEL.upper()
            n=int(input('NOTE:- WE RECOMMEND TO IMPORT AT LEAST ONE ITEM (OPTIONAL) OTHERWISE THIS TRANSACTION WILL BE CONSIDERED AS UNSUCCESSFUL\nENTER HOW MUCH QUANTITY YOU WANT TO IMPORT:- \n'))
            X=int(dfproductpr.loc[DEL2,'QTY'])
            cp=float(dfproductpr.loc[DEL2,'CP'])
            BALANCE_DEDUCTED=n*cp
            print('BALANCE PRESENT :- ',balance)
            print('TOTAL :',BALANCE_DEDUCTED)
            INPII=''
            if(balance<BALANCE_DEDUCTED):
                print('INSUFFICIENT BALANCE PLEASE REDUCE YOUR IMPORT')
                print('ENTER AGAIN')
                INPII=input("PRESS 'X' TO CANCEL TRANSACTION OTHERWISE PRESS ENTER :- ")
                if(INPII.upper()=='X'):
                    print()
                    break
                continue
            pp=1
        if(INPII.upper()=='X'):
            continue
        datee=date.today()            
        datee2=datee.strftime('%d-%m-%Y')
        TSU=0
        pinen=input('ENTER 6 DIGIT TRANSACTION PIN- ')
        if(pinen!=pin):
                i=2
                while(i>0):
                     if(pinen!=pin):
                         print('PIN ENTERED IS WRONG!!!! \n AFTER ',i,' ATTEMPTS YOUR ACCOUNT WILL BE BLOCKED')                                
                         pinen=input('ENTER PIN - ')
                         if(i==0):
                             print('------ACCOUNT BLOCKED')
                             print('PLEASE TRY AGAIN LATER!!!!.....')
                             print('THIS PART TO BE UPDATED SOON!!!')
                     else:
                         print('PIN ENTERED IS CORRECT')
                         print("                                                   DATE:-",datee2)
                         choi=input('PRESS ENTER TO CONFIRM PAYMENT OTHERWISE PRESS ANY APLHABET')
                         if(choi==''):
                             balance=balance-BALANCE_DEDUCTED
                             dfFINANCE2.loc['SUM','TOTAL']=balance
                             dfproductpr.loc[DEL.upper(),'QTY']=n+X
                             dfproductpr.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
                             print('-------------------------------------------------')
                             print(n,' ',DEL,'IMPORTED SUCCESSFULLY')
                             TSU=1
                     i=i-1
        else:            
            print('PIN ENTERED IS CORRECT')
            print("                                                   DATE:-",datee2)
            choi=input('PRESS ENTER TO CONFIRM PAYMENT OTHERWISE PRESS ANY APLHABET')
            if(choi==''):
                balance=balance-BALANCE_DEDUCTED
                dfFINANCE2.loc['SUM','TOTAL']=balance
                dfproductpr.loc[DEL.upper(),'QTY']=n+X
                dfproductpr.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
                print('-------------------------------------------------')
                print(n,DEL,'IMPORTED SUCCESSFULLY')
                TSU=1
        dftransac2 = pd.read_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
        dftransac=dftransac2.set_index('Unnamed: 0')
        dtransc=dftransac.to_dict('list')
        dftransac22 = pd.read_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
        dftransac222=dftransac22.set_index('Unnamed: 0')
        dt=datetime.now()
        dt2=dt.strftime("%d-%m-%Y %H:%M:%S")       
        dftransac222.loc[dt2,'TYPE']='IMPORT'
        dftransac222.loc[dt2,'TO/FROM']=DEL2
        if(TSU!=0):
            BALANCE_DEDUCTED=n*cp
            dftransac222.loc[dt2,'RESULT']='SUCCESSFUL'
            dtransc=dftransac.to_dict('list')
            if(datee2 not in dtransc.keys()):
                dftransac[datee2]=0.0               
            b123=dftransac.loc['IMPORT',datee2]
            a=-1*BALANCE_DEDUCTED
            dftransac.loc['IMPORT',datee2]=a+b123
            dftransac222.loc[dt2,'TRANSACTIONS']=-1*BALANCE_DEDUCTED
            print('TRANSACTION SUCCESFUL!!!!!!!!...........')
            print('MONEY DEDUCTED :- ₹',BALANCE_DEDUCTED)
            print('BALANCE LEFT :- ₹',balance)
            dfFINANCE2.loc['SUM','TOTAL']=balance
            dfFINANCE2.to_csv('D://MAJOR/MAJORFINANCE.csv',sep=' ')
            dftransac.to_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
            dftransac222.to_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
        else:
            BALANCE_DEDUCTED=0
            dftransac222.loc[dt2,'RESULT']='UNSUCCESSFUL'
            print('TRANSACTION UNSUCCESFUL!!!!!!!!...........')
            dftransac222.loc[dt2,'TRANSACTIONS']=-1*0
            print('MONEY DEDUCTED :- ₹',BALANCE_DEDUCTED)
            print('BALANCE LEFT :- ₹',balance)
            dfFINANCE2.loc['SUM','TOTAL']=balance
            dftransac222.to_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
            print('--------------------------------------------------------------------------------')  
    elif(ch.upper()=='P'):
        dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        dfproductpr=dfproduct2.set_index("Unnamed: 0")
        dfproductpr.index.name='PRODUCTS'
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        print(dfproductpr)
        dfproductpr.index.name="Unnamed: 0"
    elif(ch.upper()=='S'):  
        DFDISC=pd.read_csv('D://MAJOR/MAJORPRODUCTDISCOUNT.csv',sep=' ')
        DFDISC2=DFDISC.set_index("Unnamed: 0")
        print('PRESENT DISCOUNT is',DFDISC2.loc['DISCOUNT','DISCOUNT'],'%')
        discount=float(input('ENTER HOW MUCH % DISCOUNT YOU WANT TO GIVE?'))
        while(discount<0):
            discount=float(input('SORRY BUT DISCOUNT SHOULD BE MORE THAN 0% PLEASE ENTER AGAIN'))
        DFDISC2.loc['DISCOUNT','DISCOUNT']=discount
        DFDISC2.to_csv('D://MAJOR/MAJORPRODUCTDISCOUNT.csv',sep=' ')
        print(discount,'%  DISCOUNT APPLIED SUCCESSFULLY!!!!!......')
        print('SALE STARTS!!!............')
    elif(ch.upper()=='T'):
        dftransac2 = pd.read_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
        dftransac=dftransac2.set_index('Unnamed: 0')
        dftransac22 = pd.read_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
        dftransac222=dftransac22.set_index('Unnamed: 0')
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        choo=input('Type A to see total import and export \nType D to see detail transactions\n-')
        print()
        print()
        print()
        print('------------------------------------')
        if(choo.upper()=='A'):           
            dftransac.index.name=''
            print(dftransac)            
        if(choo.upper()=='D'): 
            dftransac222.index.name=''
            print(dftransac222)
    elif(ch.upper()=='N'):
        chp=''
        while(chp.upper()!='X'):           
            print('                    MENU')
            print("PRESS A TO SEE PIE CHART OF TODAY'S TRANSACTIONS")
            print("PRESS B TO SEE TIME LINE OF TODAY'S TRANSACTIONS")
            print("PRESS C TO SEE TIME LINE OF ALL TRANSACTIONS TILL NOW")
            print("PRESS D TO SEE BAR CHART OF COST PRICE")
            print("PRESS E TO SEE BAR CHART OF MARKET PRICE")
            print("PRESS F TO SEE BAR CHART OF STOCK LEFT")
            print("PRESS G TO SEE BAR CHART OF STOCK SOLD")
            print('Press X TO EXIT')
            chp=input('\n-')
            if(chp.upper()=='A'):
                datee=date.today()
                date2=datee.strftime('%d-%m-%Y')
                dftransac2 = pd.read_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
                dftransac=dftransac2.set_index('Unnamed: 0')
                if(date2 not in dftransac.columns):    
                    dftransac[date2]=0
                    print('NO TRANSACTIONS TILL NOW!!!!')
                balance=dftransac.loc['IMPORT',date2]
                dftransac.loc['IMPORT',date2]=-1*balance
                balance=dftransac.loc['SALARY',date2]
                dftransac.loc['SALARY',date2]=-1*balance
                dftransac.plot(kind='pie',y=date2)
                plt.ylabel(date2, loc='top')
                plt.show()
            elif(chp.upper()=='B'):
                today=datetime.today()
                today2=today.date()
                dftransac2 = pd.read_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
                dftransac=dftransac2.set_index('Unnamed: 0')
                ltransac=dftransac.index
                ltransactt=[]
                ltransacd=[]
                ltransact=[]
                for i in range(0,len(ltransac)):
                    a4=ltransac[i]
                    a=dte.datetime.strptime(a4,'%d-%m-%Y %H:%M:%S')
                    a1=a.date()
                    a2=a.time()
                    a3=str(a2)
                    if(today2==a1):
                        #print('true')
                        k=dftransac.loc[a4,'TRANSACTIONS']
                        ltransactt.append(k)
                        ltransacd.append(a1)
                        ltransact.append(a3)
                dicttrans={'TIME':ltransact,'TRANSACTIONS':ltransactt}
                dfdftransacfpl=pd.DataFrame(dicttrans)
                dfdftransacfpl.index.name='TIME(24hrs format)'
                title2='TRANSACTIONS PER HOUR for '+str(today2)
                dfdftransacfpl.plot(kind='line' ,title=title2,marker='o',color='red',markersize=10,markerfacecolor='green')
                plt.ylabel('TRANSACTIONS IN RS')
                ticks=dfdftransacfpl.index.tolist()
                plt.xticks(ticks,ltransact)
                plt.xticks(rotation=90,ha='right')
                plt.show()           
            elif(chp.upper()=='C'):
                today=datetime.today()
                today2=today.date()
                dftransac = pd.read_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
                dftransac.plot(kind='line' ,title='TRANSACTIONS PER HOUR',marker='o',color='green',markersize=10,markerfacecolor='yellow')
                ltransact2=[]
                ltransact=dftransac['Unnamed: 0']
                for i in range(0,len(ltransact)):
                    ltransact[i]=str(ltransact[i])
                    ltransact2.append(ltransact[i])
                plt.ylabel('TRANSACTIONS IN RS')
                ticks=dftransac.index.tolist()
                plt.xticks(ticks,ltransact2)
                plt.xticks(rotation=90,ha='right')
                plt.show()
            elif(chp.upper()=='D'):
                dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
                dfproductpr=dfproduct2.set_index("Unnamed: 0")
                Lproduct=dfproductpr.index
                LCP=dfproductpr['CP']
                dfproductprCP=pd.DataFrame({'COST PRICE':LCP},index=Lproduct)
                dfproductprCP.plot(kind='bar',title='COST PRICE OF PRODUCTS',color='orange')
                plt.xlabel('Products')
                plt.ylabel('PRICES')
                plt.show()
                dfproductprCP.index.name='PRODUCT'
                print()
                print("     'COST PRICE OF PRODUCT FROM HIGHER TO LOWER'")
                print('--------------------------------------------------------- ')
                print(dfproductprCP.sort_values(by='COST PRICE',ascending=False))
                print('--------------------------------------------------------- ')
                print('HIGHEST COST PRICE:- ₹',max(LCP)) 
                
            elif(chp.upper()=='E'):
                dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
                dfproductpr=dfproduct2.set_index("Unnamed: 0")
                Lproduct=dfproductpr.index
                LCP=dfproductpr['MP']
                dfproductprCP=pd.DataFrame({'MARKET PRICE':LCP},index=Lproduct)
                dfproductprCP.plot(kind='bar',title='MARKET PRICE OF PRODUCTS',color='green')
                plt.xlabel('Products')
                plt.ylabel('PRICES')
                plt.show()
                dfproductprCP.index.name='PRODUCT'
                print()
                print("     'MARKET PRICE OF PRODUCT FROM HIGHER TO LOWER'")
                print('--------------------------------------------------------- ')
                print(dfproductprCP.sort_values(by='MARKET PRICE',ascending=False))
                print('--------------------------------------------------------- ')
                print('HIGHEST MARKET PRICE:- ₹',max(LCP)) 
            elif(chp.upper()=='F'):
                dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
                dfproductpr=dfproduct2.set_index("Unnamed: 0")
                Lproduct=dfproductpr.index
                LCP=dfproductpr['QTY']
                dfproductprCP=pd.DataFrame({'STOCK LEFT':LCP},index=Lproduct)
                dfproductprCP.plot(kind='bar',title='QUANTITY OF RESPECTIVE PRODUCTS',color='magenta')
                plt.xlabel('QUANTITY REMAINING')
                plt.ylabel('PRICES')
                plt.show()
                dfproductprCP.index.name='PRODUCT'
                print()
                print("     'STOCK OF PRODUCTS LEFT FROM HIGHER TO LOWER'")
                print('--------------------------------------------------------- ')
                print(dfproductprCP.sort_values(by='STOCK LEFT',ascending=False))
                print('--------------------------------------------------------- ')
            elif(chp.upper()=='G'):
                dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
                dfproductpr=dfproduct2.set_index("Unnamed: 0")
                Lproduct=dfproductpr.index
                LCP=dfproductpr['SQTY']
                dfproductprCP=pd.DataFrame({'QUANTITY SOLD':LCP},index=Lproduct)
                dfproductprCP.plot(kind='bar',title='QUANTITY  SOLD OF RESPECTIVE PRODUCTS',color='purple')
                plt.xlabel('Products')
                plt.ylabel('QUANTITY SOLD')
                plt.show()
                dfproductprCP.index.name='PRODUCT'
                print()
                print("     'QUANTITY OF PRODUCTS FROM HIGHER TO LOWER'")
                print('--------------------------------------------------------- ')
                print(dfproductprCP.sort_values(by='QUANTITY SOLD',ascending=False))
                print('--------------------------------------------------------- ')
            elif(chp.upper()=='X'):
                print('EXITING!!!!!............')
            else:
                print('WRONG INPUT ENTERED!!!!!')
            print('MORE OPTIONS COMING SOON')
    elif(ch.upper()=='X'):
        print('EXITING!!!!!!...........')
    else:
        print('WRONG INPUT ENTERED!!!!!.....')
        print('WORK IN PROGRES!!!!!!!!!')
    print()
    print('THANK YOU!!!!...')
    print()
    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('---------------------------------------------------------')