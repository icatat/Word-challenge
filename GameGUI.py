from tkinter import *
from tkinter.ttk import *


class Game():
    
    def __init__(self,master):
        self.master = master

    #main frame
        s=Style()
        s.theme_use('alt')
        master.minsize(width=800,height=600)
        master.resizable(0, 0)
        master.title("Game")
        master.configure(background='#23B6C0')
    
        
#score
        
        self.score=Label(master, text='',foreground='blue',background='red')
        self.score.pack()
        self.score.place(x=50,y=50)
        
        

#timer
        self.timer=Label(master,text="10",background='blue')
        self.timer.pack()
        self.timer.place(x=650,y=50)
        self.timer.configure(foreground='yellow')
        
        self.time_remaining = 0
        
        


#buttons
        
        bstyle=Style()
        bstyle.configure('B.TButton',background='red')
        
        self.enter=Button(master,text="enter",width=5,command=self.enter)
        self.enter.pack()
        self.enter.place(x=250, y=550,anchor=CENTER)
        self.enter.configure(style='B.TButton')
       
        
        self.shuffle=Button(master,text="shuffle",width=5, command=self.shuffle)
        self.shuffle.pack()
        self.shuffle.configure(style='green.TButton')
        self.shuffle.place(x=350,y=550,anchor=CENTER)
        
        self.getnew=Button(master,text="New",width=5,command=self.generate)
        self.getnew.pack()
        self.getnew.place(x=450,y=550,anchor=CENTER)

        self.start=Button(master,text="Start",width=5,command=self.start_timer)
        self.start.pack()
        self.start.place(x=150,y=550,anchor=CENTER)

#labels for letter
        
        self.labels(master,20,6,400,60,60,65)
        self.labels(master,20,6,300,60,60,65)

#labels for words
        self.words3=[]
        for i in range (0, 10):
                self.words3.append(self.labels(master,1,3,i*25+30,15,120,65))
        words4=[]
        for i in range (0, 10):
                words4.append(self.labels(master,1,4,i*25+30,15,240,65))

        words5=[]
        for i in range (0, 10):
                words5.append(self.labels(master,1,5,i*25+30,15,360,65))

        words6=[]
        for i in range (0, 10):
            words6.append(self.labels(master,1,6,i*25+30,15,480,65))
            
        

    def labels(self,master,s, number,pos,dist,start,word):
        labels=[]
        for i in range (0,number):
            labels.append(Label(master,text=chr(word),padding=s))
            labels[i].pack()
            prev=start
            labels[0].place(x=prev, y= int(pos))
        for i in range (0,number):
            prev=prev+s+dist
            labels[i].place(x=prev,y=int(pos))
            labels[i].configure(padding=s)
        return labels    
            
            
    
    def enter(self):
        print("enter")


    def shuffle(self):
        print("shuffle")


    def generate(self):
        print("generate")

    def getscore(self,nr):
        self.score.configure(text='Score'+str(nr))

    def start_timer(self):
        self.update_clock(120)
        
    def update_clock(self, remaining = None):
        if remaining is not None:
            self.time_remaining = remaining

        if self.time_remaining <= 0:
            self.timer.configure(text = "Time's Up")
        else:
            self.timer.configure(text = "%d" % self.time_remaining)
            self.time_remaining -= 1
            self.master.after(1000, self.update_clock)

    
        
   
        
def main():
    root=Tk()
    mygame=Game(root)
    root.mainloop()
if __name__ == "__main__": main()
        
        
