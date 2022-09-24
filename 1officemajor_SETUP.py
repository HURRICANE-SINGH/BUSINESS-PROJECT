import pandas as pd
import datetime as dte
from datetime import date
from datetime import datetime
class officemajor_SETUP:
    global dname
    global lname
    lname=[]
    global ltransc
    ltransc=[]
    dtradate=[]
    dname={'NAME':lname}
    def setup():
        global dname
        global lname
        ldob=[]
        fori=[]
        lsalary=[]
        demp={}
        demp3={}
        ltransc=[]
        dtradate=[]
        print("                            WELCOME TO HARSAHIB'S BUSINESS SOFTWARE")
        print()
        print()
        print("Let's start SETUP PROCESS!!!...............")
        owner=input("ENTER OWNER'S NAME:- ")
        age=float(input("Enter age:- "))
        while(age<18):
            age=float(input("AGE should be at least 18 years, please enter again:- "))
        company_name=input('What would you like to have the name of your company?\n')
        c_t=input('CATEGORY OF COMPANY :-')
        gst_in=input('Enter your 15 digit GSTIN number :- ')
        while(len(gst_in)!=15):
            print('EXAMPLE OF GSTIN - 22AAAAA0000A1Z5')
            gst_in=input('Enter VALID 15 digit GSTIN number :- ')
        print()
        print('Now, enter two of your contact numbers :- ',end='')
        nno1=int(input('ENTER FIRST CONTACT NUMBER :- '))
        nno2=int(input('ENTER SECOND CONTACT NUMBER :- '))
        mail=input('ENTER YOUR email id :- ')
        while('@' not in mail or mail.lower()!=mail or '.com' not in mail):
            mail=input('ENTER VALID email id :- ')
        address=input('Enter your address :- ')
        auth=input('YOU ARE AUTHORISED DEALERS OF WHICH BRAND?(can leave empty if no authorisation)\n NOTE:-USE COMMA IF MORE THAN ONE BRAND\n')
        deal=input('YOUR BUSINESS DEALS IN:-')
        dicbill={'OWNER':owner.upper(),'AGE':age,'CN':company_name.upper(),'CT':c_t.upper(),'GSTIN':gst_in,'M1':nno1,'M2':nno2,'MAIL':mail,'ADDRESS':address.upper(),'AUTH':auth.upper(),'DEAL':deal.upper()}
        dfbill=pd.DataFrame(dicbill,index=['BILL'])
        dfbill.to_csv('D://MAJOR/MAJORDETBILL.csv',sep=' ')          
        n=int(input('HOW MANY EMPLOYEES YOU WANT TO HAVE ? \n'))
        for i in range(0,n):
            print('------------------------------------')
            fori.append(i+1)
            print('ENTER NAME OF EMPLOYEE NO. ',i+1,' - ')
            name=input()
            name=name.upper()
            lname.append(name)
            dob=input('ENTER DATE OF BIRTH OF EMPLOYEE in DD/MM/YYYY FORMAT')
            dob1=dte.datetime.strptime(dob,'%d/%m/%Y').strftime('%d-%m-%Y')
            birthDate2=datetime.strptime(dob,'%d/%m/%Y').strftime('%Y,%m,%d')
            birthDate3=birthDate2.split(',')
            birthDate4=[]
            for i in birthDate3:
                x=int(i)
                birthDate4.append(x)
            y=birthDate4[0]
            m=birthDate4[1]
            d=birthDate4[2]
            birthDate=date(y,m,d)
            today = date.today()
            age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
            while(age<18):
                print('ERROR!! AGE should be equal or greater than 18')
                dob=input('ENTER DATE OF BIRTH OF EMPLOYEE in DD/MM/YYYY FORMAT :- ')
                dob1=dte.datetime.strptime(dob,'%d/%m/%Y').strftime('%d-%m-%Y')
                birthDate2=datetime.strptime(dob,'%d/%m/%Y').strftime('%Y,%m,%d')
                birthDate3=birthDate2.split(',')
                birthDate4=[]
                for i in birthDate3:
                    x=int(i)
                    birthDate4.append(x)
                y=birthDate4[0]
                m=birthDate4[1]
                d=birthDate4[2]
                birthDate=date(y,m,d)
                today = date.today()
                age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
            ldob.append(dob1)
            salary=float(input('Enter his salary -  ₹'))
            lsalary.append(salary)
            demp={'S.NO':fori,'NAME':lname,'DATE OF BIRTH':ldob,'SALARY':lsalary}
            demp3[name]=salary
            print()
        print('------------------------------------')
        print('          EMPLOYEES DATA')
        print('------------------------------------')
        dfemp=pd.DataFrame(demp,index=lname)
        dfemp.to_csv('D://MAJOR/MAJOREMP.csv',sep=' ',index=False)
        dfimemp = pd.read_csv('D://MAJOR/MAJOREMP.csv',sep=' ',header=0)
        dfimemp222=dfimemp.set_index('S.NO')
        print(dfimemp222)#It is required
        dfexattend=pd.DataFrame(dname,index=lname)
        dfexattend.to_csv('D://MAJOR/MAJOREMPattend.csv',sep=' ')
        print('------------------------------------')
        passattenmod=input('PLEASE SET 8 DIGIT PASSWORD FOR ATTENDANCE DEPARTMENT FOR EMPLOYEES -\n NOTE:- USE OF SYMBOLS AND SPECIAL CHARACTERS IS RECOMMENDED\n')
        while(len(passattenmod)!=8):
            passattenmod=input('ENTER EXACTLY 8 DIGITS NEITHER MORE NOR LESS')
        passattenmod2=input('PLEASE confirm SET PASSWORD - ')
        while(passattenmod!=passattenmod2):
            print('ENTER BOTH PASSWORD SAME!!!')
            passattenmod=input(('ENTER PASSWORD -'))
            passattenmod2=input('PLEASE confirm SET PASSWORD - ')
            if(len(passattenmod)!=8):
                print('ENTER EXACTLY 8 DIGITS NEITHER MORE NOR LESS')
                passattenmod2=10000001864161681000000008
        print('PASSWORD SET SUCCESSFULLY!!.............')
        acc_no=input('ENTER YOUR BANK ACCOUNT NO.\n PRIVATE SECTOR BANK ACCOUNT NO. HAVE 11 DIGIT\nPUBLIC SECTOR BANK ACCOUNT NO. HAVE 12 or 14 DIGIT\n-')
        while(len(acc_no)!=11) and (len(acc_no)!=12) and (len(acc_no)!=14 ):
             acc_no=input('PLEASE RECHECK YOUR ACCOUNT NUMBER AND ENTER AGAIN\n-')
        cust_id=input('ENTER YOUR CUSTOMER ID or CIF\n NOTE:- It can be of 9,8 or 6 digit\n-')
        while((len(cust_id)!=9) and (len(cust_id)!=6) and (len(cust_id)!=8)):
            cust_id=input('PLEASE RECHECK YOUR CUSTOMER ID AND ENTER AGAIN\n-')
        print('Loading!!!!!!!!..................')
        pin=int(input('Please set six digit transcation PIN \n NOTE:- ONLY 0-9 DIGITS ARE ALLOWED\n-'))
        pinn=str(pin)
        while(len(pinn)!=6):
            pin=int(input('ENTER EXACTLY 6 DIGITS NEITHER MORE NOR LESS\n-'))
            pinn=str(pin)
        pin2=int(input(('PLEASE confirm SET PIN - ')))
        while(pin!=pin2):
            print('ENTER BOTH PINS SAME!!!\n-')
            pin=input(('ENTER PIN -'))
            pin2=input('PLEASE confirm SET PIN - ')
            if(len(pin)!=6):
                print('ENTER EXACTLY 6 DIGITS NEITHER MORE NOR LESS')
                pin2=6500000001564894848941
        
        balance=float(1000000)
        print()
        dffinance=pd.DataFrame([acc_no,cust_id,balance],index=['acc','cust','SUM'],columns=['TOTAL'])
        dffinance.to_csv('D://MAJOR/MAJORFINANCE.csv',sep=' ',header=False)
        
        print('Waiting Confirmation from your bank!!...........')
        print('PIN SET SUCCESSFULLY!!.............')
        print()
        print()
        print('-----------------------------------------')
        print('Loading!!!!!!!!..................')              
        print('YOUR ACCOUNT BALANCE is :- ',balance)
        print('IF YOU want more start importing and exporting your material fast!!!')
        dtradate={}
        dftransac=pd.DataFrame(dtradate,index=['SALARY','IMPORT','EXPORT'],columns=ltransc)
        dftransac.to_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
        dt=datetime.now()
        dt2=dt.strftime("%d-%m-%Y %H:%M:%S")
        DTRANSAC2={'TRANSACTIONS':[0.0],'RESULT':['SUCCESSFUL'],'TYPE':['-'],'TO/FROM':['-']}
        dftransac2=pd.DataFrame(DTRANSAC2,index=[dt2])
        dftransac2.to_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
        adminpass=input('PLEASE SET 8 DIGIT ADMIN PASSWORD FOR ALL ADMIN PURPOSES -\n NOTE:- USE OF SYMBOLS AND SPECIAL CHARACTERS IS RECOMMENDED\n')
        while(len(adminpass)!=8):
            adminpass=input('ENTER EXACTLY 8 DIGITS NEITHER MORE NOR LESS')
        adminpass2=input('PLEASE confirm SET PASSWORD - ')
        while(adminpass!=adminpass2):
            print('ENTER BOTH PASSWORD SAME!!!')
            adminpass=input(('ENTER PASSWORD -'))
            adminpass2=input('PLEASE confirm SET PASSWORD - ')
            if(len(adminpass)!=8):
                print('ENTER EXACTLY 8 DIGITS NEITHER MORE NOR LESS')
                adminpass2=10000001864161681000000008
        print('PASSWORD SET SUCCESSFULLY!!.............')
        dfpassword=pd.DataFrame([adminpass,passattenmod,pin],index=['ADMIN PASSWORD','ATTEDANCE PASSWORD','PIN'],columns=['PASSWORD'])
        dfpassword.to_csv('D://MAJOR/MAJOREMPPASSWORD.csv',sep=' ',header=False)
        print('---------------------------------------------------------------')
        print('          WELCOME TO PRODUCT REGISTRATION SEGMENT')
        print('---------------------------------------------------------------')
        llnofit=[]
        lprice1=[]
        lprice2=[]
        dprice={}
        llnofit1=[]
        lCATEGORY=[]
        dcproductb={}
        dproductb={}
        dfadminpass = pd.read_csv('D://MAJOR/MAJOREMPPASSWORD.csv',sep=' ',names=['PASSWORD'])
        dfadminpass3=pd.DataFrame(dfadminpass)
        adminpass3=str((dfadminpass3.loc['ADMIN PASSWORD','PASSWORD']))
        adminpass=input('PLEASE ENTER ADMIN PASSWORD\n-')
        while(adminpass!=adminpass3):
            print('ADMIN PASSWORD ENTERED IS WRONG!!!!')                                
            adminpass=input('ENTER PASSWORD AGAIN- ') 
        print('SUCCESS!!!!!!!.........')
        print()
        print()
        print('-------------------------------------------------------')            
        print("NOTE:- WHAT IS CATEGORY,BRAND AND PRODUCT NAME\n For EX- If we have APPLE IPHONE 13 PRO 256 GB \nTHEN CATEGORY is 'PHONE',\nBRAND is 'APPLE' and 'PRODUCT NAME' is 'IPHONE 13 PRO 256 GB'")
        print()
        nofit=int(input('ENTER HOW MANY CATEGORIES YOU WANT TO HAVE?\n'))
        for i in range (0,nofit):
            dproductb={}
            print('------------------------------------------------------------------')
            print('Enter name of category',(i+1),':- ')
            a=input()
            lCATEGORY.append(a.upper())
            b=int(input('How many brands are there in this category?\n'))
            j=0
            for j in range(0,b):
                print('ENTER NAME OF BRAND',(j+1),':- ',end='')
                C=input()
                j=0
                F=int(input('How many PRODUCTS are there of this BRAND?\n'))
                llnofit=[]
                for k in range(0,F):
                    print('ENTER NAME OF PRODUCT',(k+1))
                    B=input('-')
                    price1=float(input('Enter its COST price ₹'))
                    price2=float(input('Enter its MARKET price ₹'))
                    print()
                    llnofit.append(B.upper())
                    llnofit1.append(B.upper())
                    lprice1.append(price1)
                    lprice2.append(price2)
                    dproductb[C.upper()]=llnofit
                dcproductb[a.upper()]=dproductb
        LQTY=[0]*len(llnofit1)
        SQTY=[0]*len(llnofit1)
        dprice={'CP':lprice1,'MP':lprice2,'QTY':LQTY,'SQTY':SQTY}        
        dfproduct=pd.DataFrame(dcproductb)
        dfproduct.to_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
        dfproduct2=pd.DataFrame(dprice,index=llnofit1)
        dfproduct2.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
        DFDISC=pd.DataFrame([0],index=['DISCOUNT'],columns=['DISCOUNT'])
        DFDISC.to_csv('D://MAJOR/MAJORPRODUCTDISCOUNT.csv',sep=' ')
officemajor_SETUP.setup()
print()
print('SETUP COMPLETE SUCCESSFULLY!!!!!!.............')