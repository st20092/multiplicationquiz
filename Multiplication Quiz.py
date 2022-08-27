from msilib.schema import CompLocator
import random
from random import randint, randrange
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color
from venv import create
import tkinter as tk
import time

class Data:

    def __init__(self):

        self.multichoices = []
        self.questiontimes = []

        self.questionlist = []

    #QUIZ GENERATING FUNCTIONS
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

    def generatemedium(self):
        
        self.qnumber1 = randrange(1,12)
        self.qnumber2 = randrange(1,12)
        self.qanswer = self.qnumber1 * self.qnumber2
    

    #TIME KEEPING FUNCTIONS

    #RESET VARIABLES FUNCTION

    def clearvariables(self):
        self.qnumber1 = None
        self.qnumber2 = None
        self.qanswer = None
        self.questionlist.clear()
        self.questiontimes.clear()

    
class GUI:

    def __init__(self, parent):

        self.data = Data()


        #GUI Functions

        #EASY PROGRESS
        def progresseasy():
            if self.progressbar['value'] < 95:
                if self.sn.get() == self.data.qanswer:
                    self.progressbar['value'] += 5
                    self.results.configure(text = "Correct", fg = "green")
                    createeasy()

                else:
                    self.progressbar['value'] += 5
                    self.results.configure(text = f"Incorrect {self.data.qanswer}", fg = "red")
                    createeasy()

            else:
                finishscreen()
        
        def createeasy():

            self.data.generateeasy()
            createarray()
            self.questiontext.configure(text = f"{self.data.qnumber1} x {self.data.qnumber2} = ")
            self.rb1.configure(text = self.data.multichoices[0], value = self.data.multichoices[0])
            self.rb2.configure(text = self.data.multichoices[1], value = self.data.multichoices[1])
            self.rb3.configure(text = self.data.multichoices[2], value = self.data.multichoices[2])
            self.rb4.configure(text = self.data.multichoices[3], value = self.data.multichoices[3])
            self.sn.set(None)
            self.answerbox.configure(text = "")

        def selectnumber():
            
            self.answerbox.configure(text = f"{self.sn.get()}")

        #MEDIUM PROGRESS
        def progressmedium():
            if self.progressbar['value'] < 95:
                if int(self.entrybox.get()) == self.data.qanswer:
                    self.progressbar['value'] += 5
                    self.results.configure(text = "Correct", fg = "green")
                    createmedium()

                else:
                    self.progressbar['value'] += 5
                    self.results.configure(text = f"Incorrect {self.data.qanswer}", fg = "red")
                    createmedium()
                    
            else:  
                finishscreen()

        def createmedium():
            self.data.generatemedium()
            self.questiontext.configure(text = f"{self.data.qnumber1} x {self.data.qnumber2} = ")
            self.entrybox.delete(0, 'end')

        
        #CREATE ARRAY FUNC
        def createarray():

            self.ArrayFrame2.destroy()

            self.ArrayFrame2 = Frame(self.ArrayFrame)
            self.ArrayFrame2.grid(row = 1, column = 1)

            self.arraynumber1.configure(text = f"{self.data.qnumber1}")
            self.arraynumber2.configure(text = f"{self.data.qnumber2}")

            for y in range(self.data.qnumber2):
                self.arrayrow = Frame(self.ArrayFrame2)
                self.arrayrow.grid()

                for x in range(self.data.qnumber1):
                    self.arraycircle = Label(self.arrayrow, text = "O")
                    self.arraycircle.pack(side=tk.LEFT)

        #TIME KEEPING


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

            self.mediumbutton = Button(self.WelcomeButtonFrame, command = mediumscreen)
            self.mediumlabel = Label(self.mediumbutton, text = "Medium")
            self.mediumyrlvl = Label(self.mediumbutton, text = "Year 3 - 4")
            self.mediumpb = Label(self.mediumbutton, text = "Your Best Time:\n18 Seconds")
                                     
            self.hardbutton = Button(self.WelcomeButtonFrame)
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
            self.QuizFrame = Frame(parent)
            self.QuizFrame.grid(row = 1, column = 0)


            #EASY OP FRAME
            self.TopFrame = Frame(parent)
            self.TopFrame.grid(row = 0, column = 0)
            self.progressbar = ttk.Progressbar(self.TopFrame, orient="horizontal", mode="determinate", length=150)
            self.progressbar.grid(row = 0)
            self.easytitle = Label(self.TopFrame, text = "Multiplication Quiz - Easy")
            self.easytitle.grid(row = 1)


            #EASY MIDDLE LEFT FRAME
            self.MiddleLeftFrame = Frame(self.QuizFrame)
            self.MiddleLeftFrame.grid(row = 1, column = 0)
            self.infobutton = Button(self.MiddleLeftFrame, text = "info")
            self.infobutton.grid(row = 0, column = 0)
            self.questiontext = Label(self.MiddleLeftFrame, text = f"{self.data.qnumber1} x {self.data.qnumber2} = ")
            self.questiontext.grid(row = 1, column = 2)
            self.answerbox = Label(self.MiddleLeftFrame, text = "")
            self.answerbox.grid(row = 1, column = 3)
            self.results = Label(self.MiddleLeftFrame, text = "")
            self.results.grid(row = 1, column = 4)

            #EASY RADIOBUTTONS
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


            #EASY MIDDLE RIGHT FRAME
            self.MiddleRightFrame = Frame(self.QuizFrame)
            self.MiddleRightFrame.grid(row = 1, column = 1)

            self.ArrayFrame = Frame(self.MiddleRightFrame)
            self.ArrayFrame.grid()

            self.arraynumber1 = Label(self.ArrayFrame, text = self.data.qnumber1)
            self.arraynumber1.grid(row = 0, column = 1)
            self.arraynumber2 = Label(self.ArrayFrame, text = self.data.qnumber2)
            self.arraynumber2.grid(row=1, column = 0)

            self.ArrayFrame2 = Frame(self.ArrayFrame)
            self.ArrayFrame2.grid(row = 1, column = 1)

            for y in range(self.data.qnumber2):
                self.arrayrow = Frame(self.ArrayFrame2)
                self.arrayrow.grid()

                for x in range(self.data.qnumber1):
                    self.arraycircle = Label(self.arrayrow, text = "O")
                    self.arraycircle.pack(side=tk.LEFT)

            #EASY BOTTOM FRAME
            self.BottomFrame = Frame(self.QuizFrame)
            self.BottomFrame.grid(row = 2)
            
            self.submitbutton = Button(self.BottomFrame, command = progresseasy, text = "progress")
            self.submitbutton.grid()
        
            


        def mediumscreen():

            #MEDIUM FRAME FUNCTIONS
            self.WelcomeFrame.grid_forget()

            self.data.generatemedium()

            #MEDIUM FRAME
            self.QuizFrame = Frame(parent)
            self.QuizFrame.grid(row = 1, column = 0)

            #MEDIUM TOP FRAME
            self.TopFrame = Frame(parent)
            self.TopFrame.grid(row = 0, column = 0)
            self.progressbar = ttk.Progressbar(self.TopFrame, orient="horizontal", mode="determinate", length=150)
            self.progressbar.grid(row = 0)
            self.mediumtitle = Label(self.TopFrame, text = "Multiplication Quiz - Medium")
            self.mediumtitle.grid(row = 1)

            #MEDIUM MIDDLE FRAME
            self.MiddleFrame = Frame(self.QuizFrame)
            self.MiddleFrame.grid(row = 1, column = 0)
            self.infobutton = Button(self.MiddleFrame, text = "info")
            self.infobutton.grid(row = 0, column = 0)
            self.questiontext = Label(self.MiddleFrame, text = f"{self.data.qnumber1} x {self.data.qnumber2} = ")
            self.questiontext.grid(row = 1, column = 2)
            self.entrybox = Entry(self.MiddleFrame, text = "")
            self.entrybox.grid(row = 1, column = 3)
            self.results = Label(self.MiddleFrame, text = "hi")
            self.results.grid(row = 1, column = 4)

            #MEDIUM BOTTOM FRAME
            self.BottomFrame = Frame(self.QuizFrame)
            self.BottomFrame.grid(row = 2)
            
            self.submitbutton = Button(self.BottomFrame, command = progressmedium, text = "progress")
            self.submitbutton.grid()



        #def hardscreen():
            
            #HARD SCREEN FUNCTIONS
            #self.WelcomeFrame.grid_forget()

            #HARD SCREEN

        def finishscreen():
            
            #FINISH SCREEN FUNCTIONS
            self.QuizFrame.grid_forget()

            self.progressbar.grid_forget()

            #FINISH FRAME
            self.FinishFrame = Frame(parent)
            self.FinishFrame.grid(row = 1)

            #TEXT FRAME
            self.TextFrame = Frame(self.FinishFrame)
            self.TextFrame.grid(row = 0)

            self.bigtext = Label(self.TextFrame, text = "HI 1")
            self.bigtext.grid()
            self.scorelabel = Label(self.TextFrame, text = "HI 2")
            self.scorelabel.grid()
            self.timelabel = Label(self.TextFrame, text = "HI 3")
            self.timelabel.grid()
            self.smalltext = Label(self.TextFrame, text = "HI 4")
            self.smalltext.grid()

            #BUTTON FRAME
            self.ButtomFrame = Frame(self.FinishFrame)
            self.ButtomFrame.grid()

            self.menubutton = Button(self.ButtomFrame, text = "Back to Menu")
            self.menubutton.grid(row = 0, column = 0)

            self.resultbutton = Button(self.ButtomFrame,text = "View Results", command = resultscreen)
            self.resultbutton.grid(row = 0, column = 1)
            

        def resultscreen():

            #RESULT SCREEN FUNCTIONS
            self.FinishFrame.grid_forget()

            #RESULTS FRAME
            self.ResultsFrame = Frame(parent)
            self.ResultsFrame.grid(row = 1)

            self.resulttitle = Label(self.ResultsFrame, text = "Your Results")
            self.resulttitle.grid(columnspan=2)

            #INFO FRAME
            self.InfoFrame = Frame(self.ResultsFrame)
            self.InfoFrame.grid(row = 1, column=0)
            self.avgtitle = Label(self.InfoFrame, text = "Average Time to Answer:")
            self.avgtitle.grid()
            self.avglabel = Label(self.InfoFrame, text = "hi")#f"{}")
            self.avglabel.grid()

            self.fasttitle = Label(self.InfoFrame, text = "Fastest Answer:")
            self.fasttitle.grid()
            self.fastlabel = Label(self.InfoFrame, text = "hi")#f"{}")
            self.fastlabel.grid()
            self.fastquestion = Label(self.InfoFrame, text = "hi")#f"{}")
            self.fastquestion.grid()

            self.slowtitle = Label(self.InfoFrame, text = "Slowest Answer:")
            self.slowtitle.grid()
            self.slowlabel = Label(self.InfoFrame, text = "hi")#f"{}")
            self.slowlabel.grid()
            self.slowquestion = Label(self.InfoFrame, text = "hi")#f"{}")
            self.slowquestion.grid()

            #TABLE FRAME
            self.TableFrame = Frame(self.ResultsFrame)
            self.TableFrame.grid(row = 1, column=1)

            #BUTTON FRAME
            self.menubutton = Button(self.ResultsFrame, text = "Back to Menu")
            self.menubutton.grid(row = 2, column = 0, columnspan=2)

        welcomescreen()

if __name__ == "__main__":
    root = Tk()
    root.configure(bg = "#9AC5DB")           
    root.geometry("1920x1040")
    GUI(root)
    root.title("Multiplication Quiz")
    root.mainloop()
            
