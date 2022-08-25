from msilib.schema import CompLocator
import random
from random import randint, randrange
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color
from venv import create

class Data:

    def __init__(self):

        #question = []
        #questiontimer = []

        self.qnumber1 = None
        self.qnumber2 = None
        self.qanswer = None
        self.multichoices = []

    def generateeasy(self):

        self.multichoices.clear()

        self.qnumber1 = randrange(1, 10)
        self.qnumber2 = randrange(1, 10)
        self.qanswer = self.qnumber1 * self.qnumber2
        self.multichoices.append(self.qanswer)

        for n in range(3):
            self.qdummy = randint(self.qanswer - 15, self.qanswer + 15)
            self.multichoices.append(self.qdummy)

        random.shuffle(self.multichoices)
            
    def answercheck(self):

        if self.gui.selectedanswer == self.qanswer:
            self.generateeasy()

    #def runclock1:

    #def runclock2: 
    
class GUI:

    def __init__(self, parent):

        self.data = Data()

        def progress():
            if self.progressbar['value'] < 100:
                if self.sn.get() == self.data.qanswer:
                    self.progressbar['value'] += 5
                    #self.results.configure(text = "Correct", color = "Green")
                    createeasy()
                else:
                    self.easytitle.configure(bg="red")
                    #self.results.configure(text = f"Incorrect {self.data.qanswer}", color = "Red")
            else:
                self.submitbutton.grid_forget()

        def createeasy():

            self.data.generateeasy()
            self.questiontext.configure(text = f"{self.data.qnumber1} x {self.data.qnumber2} = ")
            self.rb1.configure(text = self.data.multichoices[0], value = self.data.multichoices[0])
            self.rb2.configure(text = self.data.multichoices[1], value = self.data.multichoices[1])
            self.rb3.configure(text = self.data.multichoices[2], value = self.data.multichoices[2])
            self.rb4.configure(text = self.data.multichoices[3], value = self.data.multichoices[3])
            self.answerbox.configure(text = "")

        def selectnumber():
                
                self.answerbox.configure(text = f"{self.sn.get()}")

        def welcomescreen():

            #WELCOME SCREEN FRAME
            self.WelcomeFrame = Frame(parent, bg = "#9AC5DB")

            self.TitleFrame = Frame(self.WelcomeFrame, bg = "#9AC5DB")
            self.welcometitle = Label(self.TitleFrame, bg = "#9AC5DB", text = "Multiplication", font = ("Ubuntu"))
            self.welcometitle2 = Label(self.TitleFrame, bg = "#9AC5DB", text = "Quizzes", font = ("Ubuntu",))
            self.welcometext = Label(self.TitleFrame, bg = "#9AC5DB", text = "All quizzes are 20 questions long. Do your best and good luck!", font = ("Ubuntu"))

            self.WelcomeFrame.grid(row = 0)

            self.TitleFrame.grid()
            self.welcometitle.grid(row=0)
            self.welcometitle2.grid(row=1)
            self.welcometext.grid(row=2)

            #WELCOME BUTTON FRAME
            self.WelcomeButtonFrame = Frame(self.WelcomeFrame)
            self.WelcomeButtonFrame.grid(row = 1)
            
            self.easybutton = Button(self.WelcomeButtonFrame, command = easyscreen)
            self.easylabel = Label(self.easybutton, text = "Easy")
            self.easyyrlvl = Label(self.easybutton, text = "Year 1 - 2")
            self.easypb = Label(self.easybutton, text = "Your Best Time:\n18 Seconds")

            self.mediumbutton = Button(self.WelcomeButtonFrame)
            self.mediumlabel = Label(self.mediumbutton, text = "Medium")
            self.mediumyrlvl = Label(self.mediumbutton, text = "Year 3 - 4")
            self.mediumpb = Label(self.mediumbutton, text = "Your Best Time:\n18 Seconds")
                                     
            self.hardbutton= Button(self.WelcomeButtonFrame)
            self.hardlabel = Label(self.hardbutton, text = "Hard")
            self.hardyrlvl = Label(self.hardbutton, text = "Year 5 - 6")
            self.hardpb = Label(self.hardbutton, text = "Your Best Time:\n18 Seconds")

            self.easybutton.grid(row = 0)
            self.easylabel.grid(column = 0)
            self.easyyrlvl.grid(column = 0, row = 1)
            self.easypb.grid(column = 1, row = 0, rowspan = 2)

            self.mediumbutton.grid(row = 1)
            self.mediumlabel.grid(column = 0)
            self.mediumyrlvl.grid(column = 0, row = 1)
            self.mediumpb.grid(column = 1, row = 0, rowspan = 2)

            self.hardbutton.grid(row = 2)
            self.hardlabel.grid(column = 0)
            self.hardyrlvl.grid(column = 0, row = 1)
            self.hardpb.grid(column = 1, row = 0, rowspan = 2)

        def easyscreen():
            
            #EASY FRAME FUNCTIONS
            self.WelcomeFrame.grid_forget()

            self.data.generateeasy()

            self.sn = IntVar()
            self.sn.set(None)
        

            #EASY SCREEN FRAME
            self.EasyFrame = Frame(parent)
            self.EasyFrame.grid()


            #TOP FRAME
            self.TopFrame = Frame(self.EasyFrame)
            self.TopFrame.grid(row = 0, column = 0)
            self.progressbar = ttk.Progressbar(self.TopFrame, orient="horizontal", mode="determinate", length=150)
            self.progressbar.grid(row = 0)
            self.easytitle = Label(self.TopFrame, text = "Multiplication Quiz - Easy")
            self.easytitle.grid(row = 1)


            #MIDDLE LEFT FRAME
            self.MiddleLeftFrame = Frame(self.EasyFrame)
            self.MiddleLeftFrame.grid(row = 1, column = 0)
            self.infobutton = Button(self.MiddleLeftFrame, text = "info")
            self.infobutton.grid(row = 0, column = 0)
            self.questiontext = Label(self.MiddleLeftFrame, text = f"{self.data.qnumber1} x {self.data.qnumber2} = ")
            self.questiontext.grid(row = 1, column = 2)
            self.answerbox = Label(self.MiddleLeftFrame, text = "")
            self.answerbox.grid(row = 1, column = 3)
            self.results = Label(self.MiddleLeftFrame, text = "")
            self.results.grid(row = 1, column = 4)

            #RADIOBUTTONS
            self.RbFrame = Frame(self.MiddleLeftFrame)
            self.RbFrame.grid(row = 2)

            self.rb1 = Radiobutton(self.RbFrame, text = self.data.multichoices[0], value = self.data.multichoices[0], variable = self.sn, command = selectnumber)
            self.rb1.grid(row = 0, column = 0, sticky = W)
            self.rb2 = Radiobutton(self.RbFrame, text = self.data.multichoices[1], value = self.data.multichoices[1], variable = self.sn, command = selectnumber)
            self.rb2.grid(row = 0, column = 1, sticky = W)
            self.rb3 = Radiobutton(self.RbFrame, text = self.data.multichoices[2], value = self.data.multichoices[2], variable = self.sn, command = selectnumber)
            self.rb3.grid(row = 1, column = 0, sticky = W)
            self.rb4 = Radiobutton(self.RbFrame, text = self.data.multichoices[3], value = self.data.multichoices[3], variable = self.sn, command = selectnumber)
            self.rb4.grid(row = 1, column = 1, sticky = W)


            #MIDDLE RIGHT FRAME
            #self.MiddleRightFrame = Frame(self.EasyFrame)

            #self.ArrayFrame = Frame(self.MiddleRightFrame)
            
            #for y in range(self.qnumber2):
                #self.arrayrow = Frame(self.ArrayFrame)
                #self.arrayrow.grid()

                #for x in range(self.qnumber1):
                    #self.arraycircle = Label(self.arrowrow, text = "O")

            #BOTTOM FRAME
            self.BottomFrame = Frame(self.EasyFrame)
            self.BottomFrame.grid(row = 2)
            
            self.submitbutton = Button(self.BottomFrame, command = progress, text = "progress")
            self.submitbutton.grid()
        
            


        def mediumscreen():

            self.WelcomeFrame.grid_forget()





        #def hardscreen:

        welcomescreen()

if __name__ == "__main__":
    root = Tk()
    root.configure(bg = "#9AC5DB")           
    root.geometry("1920x1040")
    GUI(root)
    root.title("Multiplication Quiz")
    root.mainloop()
            
