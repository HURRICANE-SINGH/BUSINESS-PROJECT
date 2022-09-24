import pandas as pd
import datetime as dte
from datetime import date
from datetime import datetime
class officemajor:
    global dname
    global lname
    lname=[]
    dname={'NAME':lname}
    def attendance():
        global lname
        lattend=[]
        dattend={}
        dattend1={}
        dfimattend = pd.read_csv('D://MAJOR/MAJOREMPattend.csv',sep=' ',header=0)
        dfimattend=dfimattend.drop('Unnamed: 0',axis=1)
        lname=dfimattend['NAME'].tolist()
        lenlname=len(lname)
        dattend=dfimattend.to_dict('list')
        print('               WELCOME TO ATTENDANCE SEGMENT \n \n         NOTE:- MARK P FOR PRESENT AND A FOR ABSENT')        
        print('-----------------------------------------')
        datee=date.today()
        date2=datee.strftime('%d-%m-%Y')
        if(date2 in dfimattend):
            print('ATTENDACE ALREADY MARKED FOR TODAY!!!!!')
        else:
            print('ATTENDANCE FOR',date2)
            i=int(0)
            while i<lenlname:
                print('Is ',lname[i],' present!',end='')
                attend=input()
                if(attend.upper()=='P' or (attend.upper()=='A')):
                    i=i+1
                    lattend.append(attend.upper())
                else:
                    print('PLEASE ENTER CORRECT DATA P OR A')
                    i=i
                print('-------------------------')
            dattend1[date2]=lattend
            dattend.update(dattend1)
            dfattend=pd.DataFrame(dattend)
            dfattend.to_csv('D://MAJOR/MAJOREMPattend.csv',sep=' ')
            dfattend2=dfattend.set_index('NAME')
            print(dfattend2[date2])
            print('ATTENDANCE MARKED SUCCESFULLY!!!!!..........')
            
    def attendance_viewer():
        CHOICE=''
        while(CHOICE.upper()!='X'):           
            dfpassword2 = pd.read_csv('D://MAJOR/MAJOREMPPASSWORD.csv',sep=' ',names=['PASSWORD'])
            #print(dfpassword2)
            dfpassword3=pd.DataFrame(dfpassword2)
            passworddf=str((dfpassword3.loc['ATTEDANCE PASSWORD','PASSWORD']))
            dfimattend2 = pd.read_csv('D://MAJOR/MAJOREMPattend.csv',sep=' ',header=0)
            if('Unnamed: 0' in dfimattend2.columns):
                dfimattend2=dfimattend2.drop('Unnamed: 0',axis=1)
                dfimattend=dfimattend2.set_index('NAME')
            else:
                dfimattend=pd.read_csv('D://MAJOR/MAJOREMPattend.csv',sep=' ',header=0)              
            CHOICE=input('   CHOOSE DESIRED OPTION\nTYPE S TO SEE PARICULAR DATE ATTENDANCE \nTYPE M TO SEE MULTIPLE DATE ATTENDANCE\nTYPE U TO UPDATE ATTENDANCE\nTYPE D TO DELETE ATTENDANCE\n          OR\nPRESS X TO EXIT\n')
            if(CHOICE.upper()=='S'):
                sda=input('ENTER DATE OF WHICH ATTENDANCE YOU WANT TO CHECK?  in DD/MM/YYYY FORMAT \n')
                sdaa=dte.datetime.strptime(sda,'%d/%m/%Y').strftime('%d-%m-%Y')
                while(sdaa not in dfimattend.columns):
                    print('DATE NOT PRESENT!!!\nPLEASE ENTER AGAIN!!!')
                    sda=input('ENTER DATE OF WHICH YOU WANT TO CHECK ATTENDANCE  in DD/MM/YYYY FORMAT?\nTYPE X TO EXIT\n-')
                    if(sda.upper()=='X'):                    
                         break
                    sdaa=dte.datetime.strptime(sda,'%d/%m/%Y').strftime('%d-%m-%Y')
                CHOICE2=input('TYPE S FOR SINGLE PERSON DATA \n           OR\n     TYPE A FOR ALL\nPRESS X TO EXIT\n')
                if(CHOICE2.upper()=='S'):
                    nam=input('ENTER NAME OF EMPLOYEE WHOSE ATTENDANCE YOU WANT TO SEE:-')
                    print('ATTENDANCE- ',dfimattend.loc[nam.upper(),sdaa])
                if(CHOICE2.upper()=='A'):
                   print('ATTENDANCE- \n',dfimattend[sdaa])
            elif(CHOICE.upper()=='M'):
                sda1=input('ENTER DATE FROM WHICH YOU WANT TO CHECK ATTENDANCE  in DD/MM/YYYY FORMAT ?\n')
                sda11=dte.datetime.strptime(sda1,'%d/%m/%Y').strftime('%d-%m-%Y')
                while(sda11 not in dfimattend.columns):
                    print('DATE NOT PRESENT!!!\n PLEASE ENTER AGAIN!!!')
                    sda1=input('ENTER DATE FROM WHICH YOU WANT TO CHECK ATTENDANCE  in DD/MM/YYYY FORMAT ?\nTYPE X TO EXIT\n-')
                    if(sda1.upper()=='X'):                    
                         break
                    sda11=dte.datetime.strptime(sda1,'%d/%m/%Y').strftime('%d-%m-%Y')
                sda2=input('ENTER DATE TO WHICH YOU WANT TO CHECK ATTENDANCE  in DD/MM/YYYY FORMAT?\n')
                
                sda22=dte.datetime.strptime(sda2,'%d/%m/%Y').strftime('%d-%m-%Y')
                while(sda22 not in dfimattend.columns):
                    print('DATE NOT PRESENT!!!\n PLEASE ENTER AGAIN!!!')
                    sda2=input('ENTER DATE TO WHICH YOU WANT TO CHECK ATTENDANCE  in DD/MM/YYYY FORMAT?\nTYPE X TO EXIT\n-')
                    if(sda2.upper()=='X'):                    
                         break
                    sda22=dte.datetime.strptime(sda2,'%d/%m/%Y').strftime('%d-%m-%Y')
                #DATE NOT PRESENT
                
                CHOICE2=input('TYPE S FOR SINGLE PERSON DATA \n           AND\n     TYPE A FOR ALL\n-')
                if(CHOICE2.upper()=='S'):
                    nam=input('ENTER NAME OF EMPLOYEE WHOSE ATTENDANCE YOU WANT TO SEE:-')
                    print('ATTENDANCE- \n',dfimattend.loc[nam.upper(),sda11:sda22])
                if(CHOICE2.upper()=='A'): 
                   print('ATTENDANCE- ',dfimattend.loc[:,sda11:sda22])
            elif(CHOICE.upper()=='D'):        
                passworden=input('ENTER PASSWORD OF ATTENDANCE DEPARTMENT FOR EMPLOYEES- ')
                if(passworden!=passworddf):
                     i=2
                     while(i>0):
                         if(passworden!=passworddf):
                             print('PASSWORD ENTERED IS WRONG!!!! \n AFTER ',i,' ATTEMPTS YOUR ACCOUNT WILL BE BLOCKED')
                             passworden=input('ENTER PASSWORD - ')
                             if(i==0):
                                 print('------ACCOUNT BLOCKED')
                             i=i-1                                           
                         else:
                             print('SUCCESS - PASSWORD IS CORRECT!!!')
                             date1=input('ENTER DATE OF WHICH ATTENDANCE YOU WANT TO DELETE \n USE FORMAT DD/MM/YYYY')
                             date2=dte.datetime.strptime(date1,'%d/%m/%Y').strftime('%d-%m-%Y')
                             dfimattend21=dfimattend.drop(date2,axis=1)
                             dfimattend21.to_csv('D://MAJOR/MAJOREMPattend.csv',sep=' ')
                             print('.........deleted!!!!')
                         break
                else:
                    print('SUCCESS - PASSWORD IS CORRECT!!!')
                    date1=input('ENTER DATE OF WHICH ATTENDANCE OU WANT TO DELETE \n USE FORMAT DD/MM/YYYY')
                    date2=dte.datetime.strptime(date1,'%d/%m/%Y').strftime('%d-%m-%Y')
                    dfimattend21=dfimattend.drop(date2,axis=1)
                    dfimattend21.to_csv('D://MAJOR/MAJOREMPattend.csv',sep=' ')
                    print('.........deleted!!!!')
            elif((CHOICE.upper()=='U')):
                print('            WELCOME TO UPDATATION SEGMENT')
                print('NOTE:- TO UPDATE ATTENDANCE FOR ALL EMPLOYEES\n Then firstly delete attendance for that date and \n then enter it.')
                print("       THIS SEGEMENT IS FOR SINGLE PERSON'S ATTENDANCE UPDATION!!.")
                nam=input('Enter the name of person whose attendance you want to update')
                datu=input('ENTER THE DATE OF WHICH ATTENDANCE YOU WANT TO UPDATE in DD/MM/YYYY FORMAT')
                datu2=dte.datetime.strptime(datu,'%d/%m/%Y').strftime('%d-%m-%Y')
                attend=input('ENTER P FOR PRESENT AND A FOR ABSENT')
                dfimattend.loc[nam.upper(),datu2]=attend.upper()
                dfimattend.to_csv('D://MAJOR/MAJOREMPattend.csv',sep=' ')
                print('ATTENDANCE UPDATED SUCCESFULLY!!!!!!!!............')          
            elif(CHOICE.upper()=='X'):
                print('EXITING!!!!!.......')
            else:
               print('WRONG INPUT ENTERED !!!!!')
           
    def employees_CONTROL():
        dfempcontrol = pd.read_csv('D://MAJOR/MAJOREMP.csv',sep=' ')
        dfFINANCE = pd.read_csv('D://MAJOR/MAJORFINANCE.csv',sep=' ',names=['TOTAL'])
        dfpassword2 = pd.read_csv('D://MAJOR/MAJOREMPPASSWORD.csv',sep=' ',names=['PASSWORD'])
        dfFINANCE2=pd.DataFrame(dfFINANCE)
        dfempcontrol2=dfempcontrol.set_index('NAME')
        lsalary=dfempcontrol2['SALARY'].tolist()
        dfpassword3=pd.DataFrame(dfpassword2)
        passworddf=str((dfpassword3.loc['ATTEDANCE PASSWORD','PASSWORD']))
        pin=str((dfpassword3.loc['PIN','PASSWORD']))
        finance=float(dfFINANCE2.loc['SUM','TOTAL'])
        balance=finance
        passworden=input('ENTER PASSWORD OF ATTENDANCE DEPARTMENT FOR EMPLOYEES- ')
        while(passworden!=passworddf):
            print('PASSWORD ENTERED IS WRONG!!!!')
            passworden=input('ENTER PASSWORD CORRECTLY - ')          
        print('SUCCESS - PASSWORD IS CORRECT!!!')
        choice=''
        while(choice!='X'):          
            choice=input("Type I to change Salary of Employee\nType D to change DATE OF BIRTH of Employee\nType C to issue SALARY of Employees\nType R to Remove Employees\n              OR\nPRESS X TO EXIT-")      
            if(choice.upper()=='I'):
                nam=input('Enter the name of employee whose salary you want to change')
                nsalary=float(input('Enter new Salary'))
                dfempcontrol2.loc[nam.upper(),'SALARY']=nsalary
                dfempcontrol2.to_csv('D://MAJOR/MAJOREMP.csv',sep=' ')
                print('Salary changed Sucessfully!!!!!\n')
                print(dfempcontrol2)
            if(choice.upper()=='D'):                   
                nam=input('Enter the name of employee whose DATE OF BIRTH you want to change')
                dta=input('Enter correct DATE OF BIRTH')
                dta2=dte.datetime.strptime(dta,'%d/%m/%Y').strftime('%d-%m-%Y')
                dfempcontrol2.loc[nam.upper(),'DATE OF BIRTH']=dta2
                dfempcontrol2.to_csv('D://MAJOR/MAJOREMP.csv',sep=' ')
                print('Date of Birth changed Sucessfully!!!!!')
            if(choice.upper()=='C'):
                pinen=input('ENTER 6 DIGIT TRANSACTION PIN- ')
                dt=datetime.now()
                dt2=dt.strftime("%d-%m-%Y %H:%M:%S")
                if(pinen!=pin):
                    i=2
                    while(i>0):
                         if(pinen!=pin):
                             print('PIN ENTERED IS WRONG!!!! \n AFTER ',i,' ATTEMPTS YOUR ACCOUNT WILL BE BLOCKED')                                
                             pinen=input('ENTER PIN - ')
                             if(i==0):
                                 print('------ACCOUNT BLOCKED')
                             i=i-1
                         else:
                             inp=input('PRESS ENTER TO ISSUE SALARY OF ALL EMPLOYESS')
                             if(inp==''):                                    
                                 balance_deducted=sum(lsalary)
                                 balance=balance-balance_deducted
                                 dfFINANCE2.loc['SUM','TOTAL']=balance
                                 dfFINANCE3=pd.DataFrame(dfFINANCE2)
                                 dfFINANCE3.to_csv('D://MAJOR/MAJORFINANCE.csv',sep=' ')
                                 print('Salary issued Sucessfully............')
                                 print('----------------------------------')
                                 print('BALANCE UPDATED!!!................')
                                 print()
                                 print('BALANCE DEDUCTED-',balance_deducted)
                                 print('BALANCE LEFT-',balance)
                             break 
                else:
                    inp=input('PRESS ENTER TO ISSUE SALARY OF ALL EMPLOYESS')
                    if(inp==''):
                        balance_deducted=sum(lsalary)
                        balance=balance-balance_deducted
                        dfFINANCE2.loc['SUM','TOTAL']=balance
                        dfFINANCE3=pd.DataFrame(dfFINANCE2)
                        dfFINANCE3.to_csv('D://MAJOR/MAJORFINANCE.csv',sep=' ')
                        print('Salary issued Sucessfully............')
                        print('----------------------------------')
                        print('BALANCE UPDATED!!!................')
                        print()
                        print('BALANCE DEDUCTED-',balance_deducted)
                        print('BALANCE LEFT-',balance)
                dftransac2 = pd.read_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
                dftransac=dftransac2.set_index('Unnamed: 0')
                dtransc=dftransac.to_dict('list')
                datee=date.today()            
                datee2=datee.strftime('%d-%m-%Y')
                if(datee2 not in dtransc.keys()):
                    dftransac[datee2]=0.0              
                dftransac.loc['SALARY',datee2]=-1*balance_deducted
                print(dftransac)
                dftransac.to_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
                dftransac22 = pd.read_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
                dftransac222=dftransac22.set_index('Unnamed: 0')
                dftransac222.to_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
                dftransac222.loc[dt2,'TYPE']='SALARY'
                dftransac222.loc[dt2,'TO/FROM']='ALL EMPLOYEES'
                dftransac222.loc[dt2,'RESULT']='SUCCESSFUL'
                dftransac222.loc[dt2,'TRANSACTIONS']=-1*balance_deducted
                dftransac222.to_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
                print('--------------------------------------------')
                #if(choice.upper()=='P'):    
            if(choice.upper()=='R'):
                nam=input('Enter the name of employee whom you want to remove')
                dfempcontrol2=dfempcontrol2.drop(nam.upper(),axis=0)
                dfempcontrol2.to_csv('D://MAJOR/MAJOREMP.csv',sep=' ')
                print('-----',dfempcontrol2)   
                print('DATA REMOVED Sucessfully!!!!!')
            if(choice.upper()=='X'):
                print('EXITING!!!!........')
    #def product_manager():
        


             
    def main_menu():
        cho=''
        dfadminpass = pd.read_csv('D://MAJOR/MAJOREMPPASSWORD.csv',sep=' ',names=['PASSWORD'])
        dfadminpass3=pd.DataFrame(dfadminpass)
        adminpass3=str((dfadminpass3.loc['ADMIN PASSWORD','PASSWORD']))
        adminpass=input('PLEASE ENTER ADMIN PASSWORD\n-')
        while(adminpass!=adminpass3):
            print('ADMIN PASSWORD ENTERED IS WRONG!!!!')                                
            adminpass=input('ENTER AGAIN- ') 
        print('SUCCESS!!!!!!!.........')
        print()
        print()
        print("                  'WELCOME TO OFFICE'  ")
        print('    -------------~~~~~~~~~~~~~~~~~~~~~----------------')
        print()
        print()
        print()
        while(cho.upper()!='X'):
            print("                        MAIN MENU  ")
            print('                    ------------------')
            print('ENTER THE RESPECTIVE ALPHABET FOR THE SEGMENT YOU WANT TO ENTER')
            cho=input("E for EMPLOYEE\n#B for BANKING \nX - to exit\n-")
            if(cho.upper()=='E'):                
                
                choice=''
                while(choice.upper()!='X'):
                    print()
                    print()
                    print('               WELCOME TO EMPLOYEES SEGMENT \n \nNOTE:- PRESS THE RESPECTIVE ALPHABET FOR THE SEGMENT YOU WANT TO ENTER')
                    print('A- TO MARK ATTENDANCE')
                    print('B- for ATTENDANCE VIEWER/ATTENDANCE UPDATION')
                    print('C- for all employees related task like SALARY ISSUE,DATA EDITING,SALARY CHANGE,etc')
                    print('X- to exit\n')
                    choice=input()
                    if(choice.upper()=='A'):
                        officemajor.attendance()
                    elif(choice.upper()=='B'):
                        officemajor.attendance_viewer()
                    elif(choice.upper()=='C'):
                        officemajor.employees_CONTROL()
                    elif(choice.upper()=='X'):
                        print('EXITING!!!!!!!!!.... ')
                    else:
                        print('WRONG INPUT ENTERED!!!!!')
            elif(cho.upper()=='B'):
                print('WELCOME TO BANKING SEGMENT \n \n NOTE:- PRESS THE RESPECTIVE ALPHABET FOR THE SEGMENT YOU WANT TO ENTER')
                print('A to ADD money')
                print('WORK IN PROGRESS!! \n WILL BE UPDATED SOON!!!!!!!')
            elif(cho.upper()=='X'):
                print('EXITING!!!!!!!!!.... ')
                print('Thank You............')
            else:
                print('WRONG INPUT ENTERED!!!!')               
officemajor.main_menu()       