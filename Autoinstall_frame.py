#print("hello")
import os
import subprocess
from tkinter import *
import tkinter as tk
import re


root = Tk()
global com2


class auto:
    def __init__(self):
        
        root.geometry("400x200")
        self.name=StringVar()
        lab5= Label(root,text="Software name")
        lab5.pack()
        ent=Entry(root,textvariable=self.name)
        ent.pack()
        but=Button(root,text="submit",command=self.cal)
        but.pack()
    
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
            Mylabel=Label(root,text="\n"+str(i)+" "+x)#.pack()
            text.insert(i,x)
            self.submitButton= Button(root,text="install "+str(i), command=lambda i=i:self.buttonClick(text[i-1])  )
            Mylabel.pack(anchor = tk.W)
            self.submitButton.pack(anchor = tk.E)
            
           

    def buttonClick(self,text):
        
        #print(text)
        p=re.split(" - ",text)
        com2="apt-get -y install "+p[0]
        #print(com2)
        global root
        root.destroy()
        root2=Tk()
        root2.geometry("200x200")
        self.name1=StringVar(root2)
        lab6= Label(root2,text="Enter the password")
        lab6.pack()
        ent1=Entry(root2,textvariable=self.name1)
        ent1.pack()
        but1=Button(root2,text="submit",command=lambda :self.execute(com2,self.name1.get(),root2))#self.execute(self.name1.get()))
        but1.pack()
        
        #os.popen("sudo -S %s"%(c), 'w')
        #os.system(com2)
        
    def execute(self,c,d,root2):
        root2.destroy()
        #os.popen("sudo -S %s"%(c), 'w').write(c)
        #print("here it goes",c)
        #print("Submitted")
        sudo_password =str(d)
        print(sudo_password)
        command = c.split()
        p =subprocess.Popen(['sudo', '-S']+command, stdin=subprocess.PIPE,universal_newlines=True)
        sudo_prompt = p.communicate(sudo_password+'\n' )[1]
        
        #a=os.popen("sudo -S %s"%("apt update"), 'w').write('++')
        #print(a,"a")
        root2=Tk()
        root2.geometry("200x200")
        Mylabel=Label(root2,text="Installation Successfull !!").pack()
        but1=Button(root2,text="OK",command=lambda :root2.destroy())#self.execute(self.name1.get()))
        but1.pack()
        
    
        
   
        
auto()
root.mainloop()









