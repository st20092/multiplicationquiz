from tkinter import *
from tkinter import ttk

#class Data:

    #def answercheck:


    #def runclock1:

    #def runclock2: 
    
class GUI:

    def __init__(self, parent):



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
            
            self.easybutton = Button(self.WelcomeButtonFrame)
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

    def easyscreen(self, parent):

            self.WelcomeButtonFrame.forget()

            #EASY SCREEN FRAME
            self.EasyFrame = Frame(parent)

            #TOP FRAME
            self.TopFrame = Frame(self.EasyFrame)
            self.easytitle = Label(self.TopFrame, text = "Multiplication Quiz - Easy")

            


        #def mediumscreen:



        #def hardscreen:



if __name__ == "__main__":
    root = Tk()
    root.configure(bg = "#9AC5DB")           
    root.geometry("1920x1040")
    GUI(root)
    root.title("Multiplication Quiz")
    root.mainloop()
            
