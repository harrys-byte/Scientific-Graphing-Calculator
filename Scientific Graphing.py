import math
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mplt


def main():
    print("𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸".center(170))
    print("------ 🆂🅲🅸🅴🅽🆃🅸🅵🅸🅲 🅰🅽🅳 🅶🆁🅰🅿🅷🅸🅽🅶 🅲🅰🅻🅲🆄🅻🅰🆃🅾🆁 ------\n".center(110))
    print("1. Scientific Calculations".center(165))
    print("2. Graphical Visualizations".center(165))

    print("\nTo Exit Program : 2303")

    op=int(input("\nEnter your choice : "))
    
    if op==1:
        a=True
        while a:
            print('\n')
            print('𝕾𝖈𝖎𝖊𝖓𝖙𝖎𝖋𝖎𝖈 𝕮𝖆𝖑𝖈𝖚𝖑𝖆𝖙𝖔𝖗'.center(165))
                
            print('\nAvailable Scientific Operations\n')

            funcs=[
                        'Ceil','Sqrt','Exp','Fabs','Floor','Log','Log10','sin','cos','tan','Degrees','Radians','CopySign',
                       'Factorial','floor','gcd','fmod','frexp','isfinite','isnf','isnan','ldexpnum','modf','trunc',
                        'expm1','log1p','log2','pow','acos','asin','atan','atan2','hypot',
                        'asinh','acosh','atanh','sinh','cosh','tanh','erf','erfc','gamma',
                        'lgamma','Add','Subtract','Multiply','Divide','Remainder'
                        ]
            
            i=1
            for j in funcs:
                if i%6!=0:
                    print(str(i)+'.',j,end='  ||  ')
                else:
                    print('\n')
                    print(str(i)+'.',j,end='  ||  ')
                i+=1

            print("\n\nBack to Home Page : 77")
            
            func=int(input("\nEnter your choice : "))
            print('\n')

            if func in range(1,49) and func not in [44,77]:
                num=float(input("Enter Number : "))
            else:
                pass

            if func==1:
                print(math.ceil(num))
            elif func==2:
                print(math.sqrt(num))
            elif func==3:
                print(math.exp(num))
            elif func==4:
                print(math.fabs(num))
            elif func==5:
                print(math.floor(num))
            elif func==6:
                print(math.log(num))
            elif func==7:
                print(math.log10(num))
            elif func==8:
                print(math.sin(num))
            elif func==9:
                print(math.cos(num))
            elif func==10:
                print(math.tan(num))
            elif func==11:
                print(math.degrees(num))
            elif func==12:
                print(math.radians(num))
            elif func==13:
                y=int(input("Enter Number 2 : "))
                print(math.copysign(num,y))
            elif func==14:
                print(math.factorial(num))
            elif func==15:
                print(math.floor(num))
            elif func==16:
                print(math.gcd(num))
            elif func==17:
                print(math.fmod(num))
            elif func==18:
                print(math.frexp(num))
            elif func==19:
                print(math.isfinite(num))
            elif func==20:
                print(math.isinf(num))
            elif func==21:
                print(math.isnan(num))
            elif func==22:
                i=int(input("Enter Number 2 : "))
                print(math.ldexpnum(num,i))
            elif func==23:
                print(math.modf(num))
            elif func==24:
                print(math.trunc(num))
            elif func==25:
                print(math.expm1(num))
            elif func==26:
                print(math.log1p(num))
            elif func==27:
                print(math.log2(num))
            elif func==28:
                y=int(input("Enter Power Value : "))
                print(math.pow(num,y))
            elif func==29:
                print(math.acos(num))
            elif func==30:
                print(math.asin(num))
            elif func==31:
                print(math.atan(num))
            elif func==32:
                y=float(input("Enter Number 2 : "))
                print(math.atan2(num,y))
            elif func==33:
                n=float(input("Enter Side 2 Value : "))
                print(math.hypot(num.n))
            elif func==34:
                print(math.asinh(num))
            elif func==35:
                print(math.acosh(num))
            elif func==36:
                print(math.atanh(num))
            elif func==37:
                print(math.sinh(num))
            elif func==38:
                print(math.cosh(num))
            elif func==39:
                print(math.tanh(num))
            elif func==40:
                print(math.erf(num))
            elif func==41:
                print(math.erfc(num))
            elif func==42:
                print(math.gamma(num))
            elif func==43:
                print(math.lgamma(num))
            elif func==77:
                a=False
                main()
            elif func in range(44,49):
                pass
            else:
                print('\nInvalid Option. Retry!')
            

            if func==44:
                c=int(input("Enter count of numbers : "))
                L=[]
                
                for i in range(1,c+1):
                    s=float(input(f"Enter Number{i} : "))
                    L.append(s)

                print(sum(L))
                
            elif func==45:
                c=int(input("Enter count of numbers : "))
                r=0
                
                for i in range(1,c+1):
                    s=float(input(f"Enter Number{i} : "))
                    r-=s

                print(r)
                
            elif func==46:
                c=int(input("Enter count of numbers : "))
                r=0
                
                for i in range(1,c+1):
                    s=float(input(f"Enter Number{i} : "))
                    r*=s

                print(r)
                
            elif func==47:
                c=int(input("Enter count of numbers : "))
                r=0
                
                for i in range(1,c+1):
                    s=float(input(f"Enter Number{i} : "))
                    r/=s

                print(r)
                
            elif func==48:
                c=int(input("Enter count of numbers : "))
                r=0
                
                for i in range(1,c+1):
                    s=float(input(f"Enter Number{i} : "))
                    r%=s
                print(r)
                
            else:
                pass
                
    elif op==2:
        def gps():
            print('\n')
            print('𝕲𝖗𝖆𝖕𝖍𝖎𝖓𝖌 𝕮𝖆𝖑𝖈𝖚𝖑𝖆𝖙𝖔𝖗'.center(165))

            print('\nAvailable Graphs\n')
            graphs=['Line Plot','Bargraph','Pie Chart','Histogram','Heatmap']

            j=1
            for i in graphs:
                print(str(j)+'.',i)
                j+=1

            print('\nBack to Home Page : 77\n')
            
            ch=int(input("Enter your choice : "))
            
            if ch==1:
                def linep():
                    print('\nAvailable Line Plots')

                    lineplots=['Simple Line Plot (Using Coordinates)','Line Plot (Using given numerical data)']

                    j=1
                    for i in lineplots:
                        print(str(j)+'.',i)
                        j+=1

                    
                    print('\nBack to Graphical Calculator Home Page : 66')
                    print('Back to Home Page : 77\n')
                    gh=int(input("Enter your choice : "))
                    print('\n')

                    if gh==1:
                        crds=int(input("Enter number of coordinates : "))

                        xcrds=[]
                        ycrds=[]
                            
                        for i in range(1,crds+1):
                            x=float(input(f"Enter X{i} value : "))
                            y=float(input(f"Enter Y{i} value : "))

                            xcrds.append(x)
                            ycrds.append(y)

                        tl=input("\nEnter Graph Title : ")
                        lg=input("Enter Graph Legend : ")
                        xl=input("Enter X Axis Label : ")
                        yl=input("Enter Y Axis Label : ")
                        cl=input("Enter Color : ")

                        print('\nAxis Extremes')
                        
                        axis=[]

                        print('X-Axis')
                        xs=int(input("Start : "))
                        xe=int(input("End : "))

                        axis.extend([xs,xe])

                        print('Y-Axis')
                        ys=int(input("Start : "))
                        ye=int(input("End : "))

                        axis.extend([ys,ye])

                        mplt.plot(xcrds,ycrds,color=cl)

                        mplt.title(tl)
                        mplt.axis(axis)
                        mplt.xlabel(xl)
                        mplt.ylabel(yl)
                        mplt.legend([lg])

                        mplt.show()

                        linep()

                    elif gh==2:
                        count=int(input("Enter the number of value sets : "))
                        print('\n')
                        c1=input("Enter Column 1 Name : ")
                        c2=input("Enter Column 2 Name : ")
                        
                        x=[]
                        y=[]

                        print('\nColumn 1 Entry : ')
                        for i in range(1,count+1):
                            xv=input(f'Enter Value{i} : ')
                            x.append(xv)

                        print('\nColumn 2 Entry : ')
                        for i in range(1,count+1):
                            yv=float(input(f'Enter Value{i} : '))
                            y.append(yv)

                        df=pd.DataFrame()
                        df[c1]=x
                        df[c2]=y

                        tl=input("\nEnter Graph Title : ")
                        cl=input("Enter Color : ")

                        s4=df.plot(x=c1,kind='line',color=cl,marker='o',grid=True,title=tl,figsize=(12,6))

                        mplt.xlabel(c1)
                        mplt.ylabel(c2)
                        mplt.legend(c2)
                        
                        mplt.show()

                        linep()
                        
                    elif gh==66:
                        gps()
                    elif gh==77:
                        main()
                    else:
                        print('Invalid Option. Retry!')
                        linep()
                linep()
            
            elif ch==2:
                def barg():
                    print("\nAvailable Bargraphs\n")
                    bgraphs=['Vertical','Horizontal','Stacked','Grouped']

                    j=1
                    for i in bgraphs:
                        print(str(j)+'.',i)
                        j+=1

                    print('\nBack to Main Screen : 77')
                    print('Back to Graphing Calculator Home Page : 66\n')
                    
                    gh=int(input("Enter your choice : "))
                    print('\n')
                    
                    if gh==1:
                        count=int(input("Enter the number of value sets : "))
                        
                        c1=input("Enter Column 1 Name : ")
                        c2=input("Enter Column 2 Name : ")
                        
                        x=[]
                        y=[]

                        print('\nColumn 1 Entry : ')
                        
                        for i in range(1,count+1):
                            xv=input(f'Enter Value{i} : ')
                            x.append(xv)

                        print('\nColumn 2 Entry : ')

                        for i in range(1,count+1):
                            yv=int(input(f'Enter Value{i} : '))
                            y.append(yv)

                        tl=input("\nEnter Graph Title : ")
                        cl=input("Enter Bar Color : ")
                        
                        df=pd.DataFrame()

                        df[c1]=x
                        df[c2]=y

                        mplt.bar(df[c1],df[c2],color=cl,width=0.4,edgecolor='black')
                            
                        mplt.xlabel(c1)
                        mplt.ylabel(c2)
                        mplt.title(tl)
                        mplt.legend([c2])
                        mplt.xticks(rotation=90)
                        
                        mplt.show()

                        print('\n')
                        barg()
                        
                    elif gh==2:
                        count=int(input("Enter the number of data : "))
                    
                        c1=input("\nEnter Column 1 Name : ")
                        c2=input("Enter Column 2 Name : ")
                        
                        x=[]
                        y=[]

                        print('\nColumn 1 Entry : ')
                        
                        for i in range(1,count+1):
                            xv=input(f'Enter Value{i} : ')
                            x.append(xv)

                        print('\nColumn 2 Entry : ')

                        for i in range(1,count+1):
                            yv=int(input(f'Enter Value{i} : '))
                            y.append(yv)

                        tl=input('\nEnter Graph Title : ')

                        df=pd.DataFrame()

                        df[c1]=x
                        df[c2]=y
                        
                        bar_labels = x
                        bar_colors = ['blue','red']

                        s=mplt.barh(x,y,label=bar_labels,color=bar_colors,edgecolor='black')
                            
                        mplt.xlabel(c1)
                        mplt.ylabel(c2)
                        mplt.title(tl)
                        mplt.legend(title=c1)

                        mplt.show()
                        print('\n')
                        barg()

                    elif gh==3:
                        cls=int(input("Enter the number of columns : "))
                        rws=int(input("Enter the number of rows : "))
                        print('\n')

                        df=pd.DataFrame()
                        
                        pc=''
                        lg=[]
                        for i in range(1,cls+1):
                            if i==1:
                                c=input("Enter Parent Column Name : ")
                                pc=c

                                x=[]
                                for j in range(1,rws+1):
                                    rv=input(f"Enter Value{j} : ")
                                    x.append(rv)

                                df[c]=x
                            else:
                                c=input(f"Enter Column{i} Name : ")
                                lg.append(c)
                                
                                x=[]
                                for j in range(1,rws+1):
                                    rv=float(input(f"Enter Value{j} : "))
                                    x.append(rv)

                                df[c]=x
                        
                        xl=input('\nEnter X-Axis Label : ')
                        yl=input('Enter Y-Axis Label : ')
                        tl=input('Enter Graph Title : ')
                        
                        s4=df.plot(x=pc,kind='bar',stacked=True,edgecolor='black')

                        for i in s4.containers:
                            s4.bar_label(i)

                        mplt.xlabel(xl)
                        mplt.ylabel(yl)
                        mplt.title(tl)
                        mplt.legend(lg)
                        
                        mplt.show()
                        print('\n')
                        barg()

                    elif gh==4:
                        cls=int(input("Enter the number of columns : "))
                        rws=int(input("Enter the number of rows : "))
                        print('\n')

                        df=pd.DataFrame()
                        
                        pc=''
                        lg=[]
                        for i in range(1,cls+1):
                            if i==1:
                                c=input("Enter Parent Column Name : ")
                                pc=c

                                x=[]
                                for j in range(1,rws+1):
                                    rv=input(f"Enter Value{j} : ")
                                    x.append(rv)

                                df[c]=x
                            else:
                                c=input(f"Enter Column{i} Name : ")
                                lg.append(c)
                                
                                x=[]
                                for j in range(1,rws+1):
                                    rv=float(input(f"Enter Value{j} : "))
                                    x.append(rv)

                                df[c]=x

                        xl=input('\nEnter X-Axis Label : ')
                        yl=input('Enter Y-Axis Label : ')
                        tl=input('Enter Graph Title : ')

                        s4=df.plot(x=pc,kind='bar',edgecolor='black')

                        for i in s4.containers:
                            s4.bar_label(i)

                        mplt.xlabel(xl)
                        mplt.ylabel(yl)
                        mplt.title(tl)
                        mplt.legend(lg)

                        mplt.show()
                        barg()

                    elif gh==77:
                        main()
                    elif gh==66:
                        gps()
                    else:
                        print('\nInvalid Option. Retry!')
                        barg()
                barg()

                           
            elif ch==3:
                def piec():
                    print("\nAvailable Pie Charts\n")

                    piecharts=['Single Pie Chart','Nested Pie Chart']

                    j=1
                    for i in piecharts:
                        print(str(j)+'.',i)
                        j+=1

                    print('\nRedirect to Main Screen : 77')
                    print('Redirect to Graphing Calculator Home Page : 66\n')
                    
                    gh=int(input("Enter your choice : "))
                    print('\n')

                    if gh==1:
                        
                        count=int(input("Enter the number of value sets : "))
                        
                        c1=input("\nEnter Column 1 Name : ")
                        c2=input("Enter Column 2 Name : ")
                        
                        x=[]
                        y=[]

                        print('\nColumn 1 Entry : ')
                        
                        for i in range(1,count+1):
                            xv=input(f'Enter Value{i} : ')
                            x.append(xv)

                        print('\nColumn 2 Entry : ')

                        for i in range(1,count+1):
                            yv=int(input(f'Enter Value{i} : '))
                            y.append(yv)

                        tl=input("\nEnter Pie Chart Title : ")
                        
                        df=pd.DataFrame()

                        df[c1]=x
                        df[c2]=y

                        mplt.pie(df[c2],labels=df[c1],autopct='%.2f%%')
                        
                        mplt.title(tl)
                        mplt.show()
                        print('\n')
                        piec()

                    elif gh==2:
                        print("OUTER PIE CHART DATA ENTRY".center(145))
                        
                        count=int(input("Enter the number of divisions : "))
                        
                        c1=input("\nEnter Column 1 Name : ")
                        c2=input("Enter Column 2 Name : ")
                        
                        x=[]
                        y=[]

                        print('\nColumn 1 Entry : ')
                        for i in range(1,count+1):
                            xv=input(f'Enter Value{i} : ')
                            x.append(xv)


                        print('\nColumn 2 Entry : ')
                        for i in range(1,count+1):
                            yv=int(input(f'Enter Value{i} : '))
                            y.append(yv)

                        print("INNER PIE CHART DATA ENTRY".center(145))
                        
                        count=int(input("Enter the number of divisions : "))
                        
                        c3=input("\nEnter Column 1 Name : ")
                        c4=input("\nEnter Column 2 Name : ")
                        
                        h=[]
                        k=[]

                        print('\nColumn 1 Entry : ')
                        for i in range(1,count+1):
                            xv=input(f'Enter Value{i} : ')
                            h.append(xv)

                        print('\nColumn 2 Entry : ')
                        for i in range(1,count+1):
                            yv=int(input(f'Enter Value{i} : '))
                            k.append(yv)

                        tl=input("Enter Pie Chart Title : ")
                        
                        df=pd.DataFrame()
                        df1=pd.DataFrame()
                        
                        df[c1]=x
                        df[c2]=y
                        df1[c3]=h
                        df1[c4]=k

                        mplt.pie(df[c2],radius=1,labels=df[c1],autopct='%.2f%%')
                        mplt.pie(df1[c4],radius=0.7,labels=df1[c3],autopct='%.2f%%')
                        
                        mplt.title(tl)
                        mplt.show()

                        print('\n')
                        piec()
                
                    elif gh==77:
                        main()
                    elif gh==66:
                        gps()
                    else:
                        print('\nInvalid Option. Retry!')
                        piec()
                piec()
                
            elif ch==4:
                def his():
                    count=int(input("\nEnter the number of value sets : "))
                    
                    c1=input("\nEnter Column Name : ")
                    
                    x=[]

                    print('\nColumn Data Entry : ')
                    
                    for i in range(1,count+1):
                        xv=float(input(f'Enter Value{i} : '))
                        x.append(xv)

                    x.sort()
    
                    bn=int(input("\nEnter number of bins : "))
                    cl=input('Enter Bin Color : ').lower()
                    tl=input("Enter Graph Title : ")

                    df=pd.DataFrame()

                    df[c1]=x
                    
                    df.hist(c1,bins=bn,color=cl,edgecolor='black')

                    mplt.title(tl)
                    mplt.xlabel(c1)
                    mplt.ylabel('COUNT')
                    mplt.tight_layout()
                    mplt.show()

                    def red():
                        print('\nRedirect to Main Screen : 77')
                        print('Redirect to Graphing Calculator : 66')
                        print('Redirect to Histogram : 55\n')
                        
                        ans=int(input("Enter your choice : "))

                        if ans==77:
                            main()
                        elif ans==66:
                            gps()
                        elif ans==55:
                            his()
                        else:
                            print('Invalid Option. Retry!')
                            red()
                    red()
                his()
                
            elif ch==5:
                def heat():
                    count=int(input("\nEnter the number of value sets : "))
                    
                    c1=input("\nEnter Column 1 Name : ")
                    c2=input("Enter Column 2 Name : ")
                    c3=input("Enter Column 3 Name : ")
                    
                    x=[]
                    y=[]
                    z=[]
                    
                    print('\nColumn 1 Entry : ')
                    
                    for i in range(1,count+1):
                        xv=input(f'Enter Value{i} : ')
                        x.append(xv)

                    print('\nColumn 2 Entry : ')

                    for i in range(1,count+1):
                        yv=int(input(f'Enter Value{i} : '))
                        y.append(yv)

                    print('\nColumn 3 Entry : ')

                    for i in range(1,count+1):
                        zv=int(input(f'Enter Value{i} : '))
                        z.append(zv)

                    df=pd.DataFrame()

                    df[c1]=x
                    df[c2]=y
                    df[c3]=z

                    df=df.corr()
                    mplt.figure(figsize=(8,6))
                    mplt.title(f'CORRELATION MATRIX BETWEEN {c1}, {c2} and {c3}')
                    sb.heatmap(df,annot=True,cmap='Oranges_r',cbar=True)

                    mplt.show()

                    def red():
                        print('\nRedirect to Main Screen : 77')
                        print('Redirect to Graphing Calculator : 66')
                        print('Redirect to Heatmap : 55\n')
                        
                        ans=int(input("Enter your choice : "))

                        if ans==77:
                            main()
                        elif ans==66:
                            gps()
                        elif ans==55:
                            his()
                        else:
                            print('Invalid Option. Retry!')
                            red()
                    red()
                heat()
                
            elif ch==77:
                main()
                
            else:
                print("Invalid Choice. Retry!\n")
                gps()
        gps()

    elif op==2303:
        print('----𝔓𝔯𝔬𝔤𝔯𝔞𝔪 𝔏𝔞𝔭𝔰𝔢𝔡----'.center(165))
        print('--𝓣𝓱𝓪𝓷𝓴 𝔂𝓸𝓾--'.center(165))
        
    else:
        print("Invalid Choice. Retry!\n")
        main()
main()
