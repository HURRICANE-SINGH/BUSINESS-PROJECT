import pandas as pd
import datetime
from datetime import date
def number_to_word(number):
    def get_word(n):
        words={ 0:"", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninty" }
        if n<=20:
            return words[n]
        else:
            ones=n%10
            tens=n-ones
            return words[tens]+" "+words[ones]
            
    def get_all_word(n):
        d=[100,10,100,100]
        v=["","Hundred And","Thousand","lakh"]
        w=[]
        for i,x in zip(d,v):
            t=get_word(n%i)
            if t!="":
                t+=" "+x
            w.append(t.rstrip(" "))
            n=n//i
        w.reverse()
        w=' '.join(w).strip()
        if w.endswith("And"):
            w=w[:-3]
        return w

    arr=str(number).split(".")
    number=int(arr[0])
    crore=number//10000000
    number=number%10000000
    word=""
    if crore>0:
        word+=get_all_word(crore)
        word+=" crore "
    word+=get_all_word(number).strip()+" Rupees"
    if len(arr)>1:
         if len(arr[1])==1:
            arr[1]+="0"
         word+=" and "+get_all_word(int(arr[1]))+" paisa"
    return word
print('----------------------------------------------------------------------------')
DFDISC=pd.read_csv('D://MAJOR/MAJORPRODUCTDISCOUNT.csv',sep=' ')
DFDISC2=DFDISC.set_index("Unnamed: 0")
discount=float(DFDISC2.loc['DISCOUNT','DISCOUNT'])
dfbill2=pd.read_csv('D://MAJOR/MAJORDETBILL.csv',sep=' ')
dfbill3=dfbill2.set_index('Unnamed: 0')
OWNER=dfbill3.loc['BILL','OWNER']
CN=dfbill3.loc['BILL','CN']
CT=dfbill3.loc['BILL','CT']            
MAIL=dfbill3.loc['BILL','MAIL']
M1=dfbill3.loc['BILL','M1']
M2=dfbill3.loc['BILL','M2']
ADDRESS=dfbill3.loc['BILL','ADDRESS']
GN=dfbill3.loc['BILL','GSTIN']
auth=dfbill3.loc['BILL','AUTH']
deal=dfbill3.loc['BILL','DEAL']
print("                      WELCOME TO ",CN,"'s")
print('                     COME TO BE SERVED WELL ')
print()
print('                                          FOR ANY QUERY CALL AT',M2)
print('----------------------------------------------------------------------------')
print('----------------------------------------------------------------------------')
if(int(discount)>1):
    print('                           SPECIAL  OFFER')
    print('                            SALE ON SALE')
    print('                        GET',discount,'% DISCOUNT')
    print('----------------------------------------------------------------------------')
print()
print()
ans=''
COUNTE=0  
lsale=[]
litem=[]
lprice=[]
lsno=[]
lqty=[]
ltotal=[]
#ltotal2=[]
ldiscount=[]
ldiscount2=[]
GST=[]
SCGST=[]
gst=18
while (ans.upper()!='X'):
    gst2=str(gst/2)
    gst1=0
    dfproduct=pd.read_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
    dfproduct2=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
    dfFINANCE = pd.read_csv('D://MAJOR/MAJORFINANCE.csv',sep=' ',names=['TOTAL'])
    dfFINANCE2=pd.DataFrame(dfFINANCE)
    balance=float(dfFINANCE2.loc['SUM','TOTAL'])
    #print(dfproduct2)
    if("Unnamed: 0"in dfproduct.columns):
        dfproduct3a=dfproduct.set_index("Unnamed: 0")
    else:
        dfproduct3a=pd.read_csv('D://MAJOR/MAJORPRODUCT.csv',sep=' ')
    if("Unnamed: 0"in dfproduct2.columns):
        dfproductpr=dfproduct2.set_index("Unnamed: 0")
    else:
        dfproductpr=pd.read_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ') 
    #print(dfproduct3a)
    #print(dfproductpr)
    DICTPRODUCT=dfproduct3a.to_dict('dict')
    LICTPRODUCT=list(DICTPRODUCT.keys())
    LICTPRODUCT2=list(dfproduct3a.index)
    #print('--------------',LICTPRODUCT2)
    COUNTE=COUNTE+1 
    print('                              MAIN MENU')
    print('                 ----------------------------------------')
    print()
    print('THESE ARE THE CATEGORIES WE ARE HAVING:- ')
    i=0
    while(i<len(LICTPRODUCT)):
        print('PRESS',i,' for ',end='')
        print(LICTPRODUCT[i])
        i=i+1
    cate=int(input("ENTER RESPECTIVE NUMBER FOR CATEGORY YOU WANT:-\n"))
    print('----------')
    print()
    LICTPRODUCT3=[]
    i=0
    for i in range(0,len(LICTPRODUCT2)):
        b=LICTPRODUCT2[i]
        noke=str(dfproduct3a.loc[b,LICTPRODUCT[cate]])
        if(noke!="NaN" and noke!="nan"):
            LICTPRODUCT3.append(LICTPRODUCT2[i])
    print("THESE ARE THE BRANDS OF ",LICTPRODUCT[cate],":-")       
    i=0
    while(i<len(LICTPRODUCT3)):
        print('PRESS',i,' for ',end='')
        print(LICTPRODUCT3[i])
        i=i+1
    print('PRESS B TO GO BACK TO MAIN MENU')
    brn2=input("ENTER RESPECTIVE NUMBER FOR BRAND YOU WANT:-\n")    
    if(brn2.upper()=='B'):
        COUNTE=COUNTE-1
        continue        
    brn=int(brn2)
    print('----------')
    print()
    print("THESE ARE THE ",LICTPRODUCT[cate],"  OF ",LICTPRODUCT3[brn],':-')#USE X,Y,Z
    dfproduct3=str(dfproduct3a.loc[LICTPRODUCT3[brn],LICTPRODUCT[cate]])##
    dfproduct4=dfproduct3.replace('[','')
    dfproduct5=dfproduct4.replace(']','')
    dfproduct6=dfproduct5.replace(', ',',')
    dfproduct7=dfproduct6.replace("'",'')
    #dfproduct8=dfproduct7.replace("nan",'')
    Ldfproduct=list(dfproduct7.split(','))
    lenl=len(Ldfproduct)
    LI=[]
    i=0
    while (i < lenl):
        i=i+1
        if(Ldfproduct[i-1]=='nan'):
            continue
        print('PRESS',i-1,' for ',end='')
        print(Ldfproduct[i-1])
        PK=Ldfproduct[i-1]
        LI.append(PK)
    print('PRESS B TO GO BACK TO MAIN MENU')
    if(len(LI)==1 and LI[0]==''):
        print('PRODUCTS OF THIS BRAND ARE COMING SOON!!!')
        COUNTE=COUNTE-1
        print()
        continue
    print('ENTER RESPECTIVE GIVEN NUMBER FOR THE PRODUCT YOU WANT!!!')
    ch2=input() 
    if(ch2.upper()=='B'):
        COUNTE=COUNTE-1
        continue 
    ch=int(ch2) 
    mp=float(dfproductpr.loc[Ldfproduct[ch],'MP'])
    n=(dfproductpr.loc[Ldfproduct[ch],'QTY'])
    n5=(dfproductpr.loc[Ldfproduct[ch],'SQTY'])
    print('loading!!!!.........')
    print('STOCK LEFT:- ',n)
    print('PRICE/ITEM:- ₹',mp)
    CH12=input('PRESS ENTER TO GO AHEAD OR PRESS B TO GO BACK TO MAIN MENU')
    if(CH12.upper()=='B'):
        COUNTE=COUNTE-1
        continue
    if(n==0):
        print('SORRY!!,Out of stock wait till stock arrives back!!!')
        print("YOU CAN TRY SOMETHING ELSE")
        COUNTE=COUNTE-1
        ans=input('PRESS ENTER TO CONTINUE SHOPPING OR PRESS X TO EXIT')
        continue
   
    print('ENTER - How many ',Ldfproduct[ch],'you want?',end='')
    qty=int(input())
    n1=n-qty
    while(n1<0 or qty==0):
        if(n1<0):
            print('ERROR!! \n Only',n,'left in stock')
        if(qty==0):
            print('ERROR!! \n QTY SHOULD NOT BE ZERO')
        print('AGAIN,Enter - How many ',Ldfproduct[ch],'you want?',end='')
        qty=int(input())
        n1=n-qty
    purccho=input('PRESS ENTER TO PURCHASE OTHERWISE PRESS B')
    if(purccho.upper()=='B'):
        COUNTE=COUNTE-1
        continue
    litem.append(Ldfproduct[ch])
    n5=n5+qty
    sale=qty*float(mp)
    lsale.append(float(sale))
    dfproductpr.loc[Ldfproduct[ch],'QTY']=n1
    dfproductpr.loc[Ldfproduct[ch],'SQTY']=n5
    dfproductpr.to_csv('D://MAJOR/MAJORPRODUCTPRICE.csv',sep=' ')
    balance_added=sum(lsale)
    balance=balance+balance_added
    gst1=(gst*balance_added)/100
    total=((gst*balance_added)/100)+balance_added
    dfFINANCE2.loc['SUM','TOTAL']=balance
    dfFINANCE3=pd.DataFrame(dfFINANCE2)
    dfFINANCE3.to_csv('D://MAJOR/MAJORFINANCE.csv',sep=' ')
    print('Purchase done Sucessfully............')
    print('----------------------------------')
    datee=date.today()
    datee2=datee.strftime('%d-%m-%Y')
    dt=datetime.now()
    dt2=dt.strftime("%d-%m-%Y %H:%M:%S")
    #dftransac2 = pd.read_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
    #dftransac=dftransac2.set_index('Unnamed: 0')
    #dtransc=dftransac.to_dict('list')
    #if(datee2 not in dtransc.keys()):
        #dftransac.loc['EXPORT',datee2]=0    
    #balance2=float(dftransac.loc['EXPORT',datee2])
    #dftransac.loc['EXPORT',datee2]=balance_added+balance2
    #dftransac.to_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
    print('TOTAL till now without GST:- ₹',balance_added)
    discount2=balance_added*discount/100
    total1=total-(balance_added*discount/100)
    dftransac3 = pd.read_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
    dftransac2=dftransac3.set_index('Unnamed: 0')
    dt=datetime.now()
    dt2=dt.strftime("%d-%m-%Y %H:%M:%S")
    dftransac2.loc[dt2,'TRANSACTIONS']=balance_added 
    dftransac2.loc[dt2,'TYPE']='EXPORT'
    dftransac2.loc[dt2,'RESULT']='SUCCESSFUL'
    dftransac2.loc[dt2,'TO/FROM']=Ldfproduct[ch] 
    dftransac2.to_csv('D://MAJOR/MAJORTRANSC2.csv',sep=' ')
    lsno.append(COUNTE)
    GST.append(gst1)
    lprice.append(mp)
    lqty.append(qty)
    ltotal.append(total1)  
    ldiscount.append(discount)
    ldiscount2.append(discount2)
    gst3=gst2+'%'
    SCGST.append(gst3)
    ans=input('PRESS ENTER TO CONTINUE SHOPPING OR PRESS X TO EXIT- ')
print('-----------------------------------------')
dicbill={'ITEM NAME':litem,'PRICE':lprice,'QUANTITY':lqty,'SUM':lsale,'CGST%':SCGST,'SGST%':SCGST,'NET GST(₹)':GST,'DISCOUNT%':ldiscount,'DISCOUNT ':ldiscount2,'TOTAL':ltotal}
dfbill=pd.DataFrame(dicbill,index=lsno)
dfbill.index.name='ITEM NO.'
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
dfbill.to_csv('D://MAJOR/MAJORDETBILLMAIN.csv',sep=' ')
#dfbill2=pd.read_csv('D://MAJOR/MAJORDETBILLMAIN.csv')
if(len(lqty)>0):
    print()
    print('-----------------------------------------')
    cusn=input('ENTER YOUR NAME :-')
    CPN=input('ENTER YOUR PHONE NUMBER :-')
    print()
    print('-----------------------------------------')
    print('PLEASE COLLECT YOUR PURCHASE AND BILL FROM COUNTER')
    print('---------------------------------------------------------------------------')
    print()
    print()
    print()
    print()
    print()
    print('---------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------')
    datee=date.today()            
    stda=datee.strftime('%d-%m-%Y')
    amountt=sum(ltotal)
    print()
    print()
    print()
    print()
    print()
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('                                             BILL/CASH MEMO')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('                                          ',CN,'  STORE')
    print('                                    A CPMPLETE ',CT,' STORE')
    print('                                                                                             PH:',M1)
    print('                                                                                                ',M2)
    print('                                                                                           email:',MAIL)
    if(auth!=''):
        print('AUTH.DEALERS OF ',auth,'')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('                                    ',ADDRESS)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('                                                                                        DATE-',stda)
    print('CUSTOMER NAME -',cusn)
    print('PHONE NUMBER  -',CPN)
    print('GSTIN         -',GN)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('                                          BILL INVOICE')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print(dfbill)
    print("----------------------------------------------------------------------------------------------------------------------------------")
    if(discount==0):
        print('AMOUNT:-                                                                                ₹',amountt)
    else:
        print('AMOUNT:-                                                                                           ₹',amountt)
        dftransac2 = pd.read_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
        dftransac=dftransac2.set_index('Unnamed: 0')
        dtransc=dftransac.to_dict('list')
        if(stda not in dtransc.keys()):
            dftransac[stda]=0 
        balance2=float(dftransac.loc['EXPORT',stda])
        dftransac.loc['EXPORT',stda]=amountt+balance2
        dftransac.to_csv('D://MAJOR/MAJORTRANSC.csv',sep=' ')
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print('AMOUNT IN WORDS-',number_to_word(amountt),end='')
    print(' only')
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print("Thank you ",cusn," for purchasing your product(s) from ",CN)
    print("If in future also if you have any issue or suggestion feel free to contact on given numbers")
else:
    print()
    print("Thank you for choosing ",CN)
print("                                                        CREDITS- HARSAHIBJIT SINGH mail for reviews at harsahibjitsingh@icloud.com")