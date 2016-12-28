from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from GameModel import *
import random
from PIL import Image, ImageTk
from PIL import *

class Game():

    def __init__(self):
        self.model=GameModel()
        self.master = Tk()
        self.controller = None
        
        #mainframe
    #   self.filename=Image.open('/Users/Catalina/Documents/workspace/Word-Challenge/snowflakes.jpg','r')
    #   self.filename2=ImageTk.PhotoImage(self.filename)
    
        # Color values declared as constants
        self.COLOR_RANDOM_EMPTY = '#F8F8FF' # background color of the labels for the keyword
        self.COLOR_ENTER_EMPTY = '#FFEBCD' # background color of the labels for the letters entered
        self.COLOR_WORD_EMPTY= '#CCFFFF' # background color of the labels for the keyword
        
        self.COLOR_RANDOM_FILLED = '#008B8B'
        self.COLOR_ENTER_FILLED = 'pink'
        self.COLOR_WORD_FILLED = '#191970'
        self.FS = 12 # font size of the letters
        
    #main frame
        s=Style()
        s.theme_use('alt')
        self.master.minsize(width=700,height=600)
    #    self.master.resizable(0, 0)
        self.master.title("Game")
        self.master.configure(background='#23B6C0')
     
     
        self.filename=Image.open('snowflakes.jpg','r')
        self.resized=self.filename.resize((800,700))#resized image-gets the size of the whole frame
        self.resized2=ImageTk.PhotoImage(self.resized)#creates the photo image from the file
        self.back=Label(self.master,image=self.resized2,anchor=CENTER)#sets the image
        self.back.pack(fil=BOTH,expand=YES)
        self.back.bind('<Configure>',self.resize_frame)#binds the Configure to the resize_frame method
       
        # array of labels for letters of the key word
        self.randomlet=[]
        self.randomlet=self.labels(self.master,0.05,6,500,60,150,70,self.COLOR_RANDOM_FILLED,25)

        # array of labels for letters entered
        self.enteredlet=[]
        self.enteredlet=self.labels(self.master,0.05,6,400,60,150,70,self.COLOR_ENTER_EMPTY,25)
    
    

    # LABELS ON VIEW
        #score
        self.score=Label(self.master, text='Score: 0',foreground='white')
    
        self.score.pack()
        self.score.place(x=50,y=550)
        #timer
        self.timer=Label(self.master,text="2:00",background='blue')
        self.timer.pack()
        self.timer.place(x=800,y=550)
        self.timer.configure(foreground='yellow')

        # BUTTONS ON VIEW
        
        bstyle=Style()
        bstyle.configure('B.TButton',background='red')
        
        # Enter button
        self.enter=Button(self.master,text="enter",width=6)
        self.enter.pack()
        self.enter.place(x=400, y=600,anchor=CENTER)
        self.enter.configure(style='B.TButton')

        # Shuffle button
        self.shuffle=Button(self.master,text="shuffle",width=6)
        self.shuffle.pack()
        self.shuffle.configure(style='green.TButton')
        self.shuffle.place(x=500,y=600,anchor=CENTER)

        # New button
        self.getnew=Button(self.master,text="New",width=6)
        self.getnew.pack()
        self.getnew.place(x=600,y=600,anchor=CENTER)

        # Start button
        self.start=Button(self.master,text="Start",width=6, command = self.start_timer)
        self.start.pack()
        self.start.place(x=300,y=600,anchor=CENTER)

        # fields that hold labels for words of each length
        self.words3=[]
        self.words4=[]
        self.words5=[]
        self.words6=[]
    
        # binding keys to buttons
        self.master.bind("<Return>", self.enter_function)
        self.master.bind("<space>", self.shuffle_function)
        self.master.bind("<BackSpace>", self.backspace_function)
        self.master.bind("<Tab>", self.get_new_key)
        self.master.bind("<Key>", self.key)
        
     # resize the image together with the background label and the window   
    def resize_frame(self,event = None):

        self.new_width=self.master.winfo_width()
        self.new_height= self.master.winfo_height()
        self.image=self.resized.resize((self.new_width,self.new_height),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(self.image)
        self.back.configure(image=self.photo)
    
    # This function binds a controller to this view
    def register_controller(self, controller):
        self.controller = controller
        
    
    # Every time a new key is generated, this function is called to generate new blank labels
    # that hold the place for the words that can be formed from the new key
    def create_labels(self):
        label_size=0.014
        # Destroy all the old labels and reset all the fields
        for label in self.words3:
            for l in label:
                l.destroy()
        
        for label in self.words4:
            for l in label:
                l.destroy()
        
        for label in self.words5:
            for l in label:
                l.destroy()
        
        for label in self.words6:
            for l in label:
                l.destroy()
        
        self.words3 = []
        self.words4 = []
        self.words5 = []
        self.words6 = []
        
        # Create label for 3-letter words
        n3 = len(self.controller.model.three)
        if n3 > 10:
            for i in range (0, 10):
                self.words3.append(self.labels(self.master, label_size, 3, i*25 + 30, 15, 200, 65, self.COLOR_WORD_EMPTY, self.FS))
            dif=n3-10
            for i in range (0,dif):
                self.words3.append(self.labels(self.master, label_size, 3, i*25 + 30, 15, 280, 65, self.COLOR_WORD_EMPTY, self.FS))
        else:
            for i in range (0, n3):
                self.words3.append(self.labels(self.master, label_size, 3, i*25 + 30, 15, 200, 65, self.COLOR_WORD_EMPTY, self.FS))
       
        # Create label for 4-letter words
        n4=len(self.controller.model.four)
        if n4 > 10:
            for i in range (0, 10):
                self.words4.append(self.labels(self.master, label_size, 4, i*25 + 30, 15, 400, 65, self.COLOR_WORD_EMPTY, self.FS))
            dif=n4-10
            for i in range (0,dif):
                self.words4.append(self.labels(self.master, label_size, 4, i*25 + 30, 15, 500, 65, self.COLOR_WORD_EMPTY, self.FS))
        else :
            for i in range (0, n4):
                self.words4.append(self.labels(self.master, label_size, 4, i*25 + 30, 15, 400, 65, self.COLOR_WORD_EMPTY, self.FS))
      
        # Create label for 5-letter words
        n5 = len(self.controller.model.five)
        for i in range (0, n5):
            self.words5.append(self.labels(self.master, label_size, 5, i*25 + 30, 15, 600, 65, self.COLOR_WORD_EMPTY, self.FS))

        # Create label for 6-letter words
        n6 = len(self.controller.model.six)
        for i in range (0, n6):
            self.words6.append(self.labels(self.master, label_size, 6, i*25 + 30, 15, 700, 65, self.COLOR_WORD_EMPTY, self.FS))



    # This function is called to display a given 6-character key on the lower section
    def display_curKey(self, key):  
        letters = list(key)
        for i in range (0,6): 
            self.randomlet[i].configure(text=letters[i])
    
         
    # TO-DO: Peer-review this function
    # This function displays a character on the upper level 
    def type_character(self, word, position):
        if len(word) == 3:
            rows = self.words3[position]
            for i in range (0,3):
                key=word[i]
                rows[i].configure(text=key, background = self.COLOR_WORD_FILLED, foreground='white')

        if len(word) == 4:
            rows = self.words4[position]
            for i in range (0,4):
                key=word[i]
                rows[i].configure(text=key, background = self.COLOR_WORD_FILLED, foreground='white')

        if len(word) == 5:
            rows = self.words5[position]
            for i in range (0,5):
                key=word[i]
                rows[i].configure(text=key, background = self.COLOR_WORD_FILLED, foreground='white')
        
        if len(word) == 6:
            rows = self.words6[position]
            for i in range (0,6):
                key=word[i]
                rows[i].configure(text=key, background = self.COLOR_WORD_FILLED, foreground='white')



    # s: size of the label
    # number: how many letters
    # pos: vertical position of the label
    # dist: distance between two adjacent columns
    # start: horizontal position of the first column
    # word: character to be displayed on the label
    # fs: font size
    def labels(self, master, s, number, pos, dist, start, word, color, fs):
        labels=[]
        for i in range (0,number):
            labels.append(Label(master, text = '_', anchor = CENTER, font = ("Times New Roman", fs)))
            labels[i].pack(fill = BOTH, expand = YES)
            prev = start
            labels[0].place(x=prev, y= int(pos),relheight=1.5*s,relwidth=s)
        for i in range (0,number):
            prev=prev+s+dist
            labels[i].place(x=prev,y=int(pos),relheight=1.5*s, relwidth=s)
            labels[i].configure(background=color)
        return labels


    # This function takes the letters entered and forms a word to send to the controller 
    def enter_function(self, event = None):        
        # Get the word input by the player 
        word=[]
        for let in self.enteredlet:
            key=let['text']
            if(key!='_'):
                word.append(key)
        
        # Form the word
        playword=''
        for i in range (0,len(word)):
            playword = playword + word[i]
        
        self.controller.play_word(playword)
      
    

    # This function removes the most recent letter typed in and put it back to the lower section
    def backspace_function(self, event = None):
        for i in range(0, len(self.enteredlet)):
            # if there is a '_' in the entered word
            if self.enteredlet[i]['text'] == "_":
                for let in self.randomlet:
                    if let['text'] == '_':
                        let.configure(text=self.enteredlet[i-1]['text'])
                        let.configure(background = self.COLOR_RANDOM_FILLED)
                        self.enteredlet[i-1]['text'] = '_'
                        self.enteredlet[i-1]['background'] = self.COLOR_ENTER_EMPTY
                        return
            
            # special case: if all six letters have been used
            elif self.enteredlet[i]['text'] != "_" and i == len(self.enteredlet) - 1:
                for let in self.randomlet:
                    if let['text'] == '_':
                        let.configure(text=self.enteredlet[i]['text'])
                        let.configure(background = self.COLOR_RANDOM_FILLED)
                        self.enteredlet[i]['text']='_'
                        self.enteredlet[i]['background'] = self.COLOR_ENTER_EMPTY
                        return
    
    
    # This function shuffles the six letters of the key word and displays the shuffled key on the view
    def shuffle_function(self, event = None):
        key = list(self.controller.get_curKey())
        random.shuffle(key)
        shuffled = ''.join(key)
        self.display_curKey(shuffled)



    # This function signals the controller to generate a new key for the game 
    def get_new_key(self, event = None):
        self.controller.get_new_key()
    
    
    # This function updates the score in the view to the most updated score in the controller
    def update_score(self):
        new_score = self.controller.score
        self.score.configure(text='Score: ' + str(new_score))



    # This function updates the time in the view to the most updated time in the controller
    def update_clock(self, count):
        self.timer['text'] = count
        if count > 0:
            print(count)
            self.master.after(1000, self.update_clock(count-1))



    # Resetting the input area
    def reset_input(self):
        for let in self.enteredlet:
            key = let['text']
            for word in self.randomlet:
                if word['text'] == '_':
                    word.configure(text = key, background = self.COLOR_RANDOM_FILLED, foreground='black')
                    let.configure(text = '_', background = self.COLOR_ENTER_EMPTY)
                    break
        
        
    # This function listens to the key pressed and handles it accordingly
    def key(self, event):
        key = event.keysym
        check = False
        for ran in self.randomlet:
            if ran['text'] == key:
                check = True
                ran.configure(text = "_", background = self.COLOR_RANDOM_EMPTY)
                for let in self.enteredlet:
                    if (let['text'] == "_"):
                        let.configure(text=key, background = self.COLOR_ENTER_FILLED, foreground='black')
                        break
                break
        
        if check == False: # if the letter typed is not part of the keyword
            # Need some type of feedback later
            print("Error", "This letter is not available.\nTry again")
            #messagebox.showerror("Error","This letter is not available.\nTry again")
        
        
    # This function starts the count-down timer 
    def start_timer(self):
        self.controller.start_timer()
        self.start.config(state = DISABLED)
    
    
    # This function displays a time (given in second) on the game view
    def display_time(self, time):
        if time < 0:
            self.timer.configure(text = "Time's Up!")
            print("Your final score is: " + str(self.controller.score))
        else:
            mins = time // 60
            secs = time % 60
            secstr = ""
            if secs < 10:
                secstr = '0' + str(secs)
            else:
                secstr = str(secs)
            self.timer.configure(text = str(mins) + ":" + secstr)


    
def main():
    mygame=Game()
    mygame.master.mainloop()
if __name__ == "__main__": main()