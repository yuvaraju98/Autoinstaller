#print("hello")
import os
import subprocess
from tkinter import *
import re
root = Tk()
root.geometry("400x700")

class auto:
    def cal(self):
        print(self.name.get())
        open("pp.txt","w")
        
        command="apt-cache search "+self.name.get()+" |column -s'-' >> pp.txt "
        os.system(command)
        fi=open("pp.txt", "r")
        f=fi.readlines()
        i=0
        text=[]
        for x in f:
            i+=1
            Mylabel=Label(root,text=str(i)+" "+x).pack()
            text.insert(i,x)
            self.submitButton= Button(root,text="install"+str(i), command=lambda i=i:self.buttonClick(text[i-1])  )
            self.submitButton.pack()
            
            

    def buttonClick(self,text):
        print(text)
       
        p=re.split(" - ",text)
        print("text")
        print(p[0])
        com2="apt-get install "+p[0]
        
        print(com2)
        c="apt update"
        root2=Tk()

        root2.geometry("200x200")
        self.c=StringVar()
        Mylabel=Label(root2,text="Enter the System password ").pack()
        ent=Entry(root2,textvariable=self.c)
        ent.pack()
        but=Button(root2,text="submit",command=lambda: self.execute(com2,self.c.get()))
        but.pack()
        
        print("Terminal output")
        #os.popen("sudo -S %s"%(c), 'w')
        #os.system(com2)
        
    def execute(self,com,c):
        #os.popen("sudo -S %s"%(c), 'w').write(c)
        print("Submitted")
        
        print(c)
        sudo_password =str(c)
        print(sudo_password)
        command = com.split()
        

        p =subprocess.Popen(['sudo', '-S'] + command, stdin=subprocess.PIPE,universal_newlines=True)
        sudo_prompt = p.communicate(sudo_password + '\n')[1]
        
        #a=os.popen("sudo -S %s"%("apt update"), 'w').write('++')
        #print(a,"a")
        print(p)
        print(sudo_prompt)
    
        
    def __init__(self):
       
        self.name=StringVar()
        lab5= Label(root,text="Software name")
        lab5.pack()
        ent=Entry(root,textvariable=self.name)
        ent.pack()
        but=Button(root,text="submit",command=self.cal)
        but.pack()
        
auto()
root.mainloop()









