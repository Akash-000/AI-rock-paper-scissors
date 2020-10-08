from tkinter import *
from PIL import ImageTk, Image


class Game:
    def __init__(self):
        window = Tk()
        window.geometry("600x750")
        window.title("Rock - Paper - Scissors")

        self.frame1 = Frame(window)
        self.label1 = Label(self.frame1, text = "****  Rock - Paper - Scissors  ****", font = "Times 15 italic underline bold")
        self.label1.pack()
        self.frame1.pack()


        self.frame2 = Frame(window)
        canvas = Canvas(self.frame2, width = 537, height = 542)
        image = ImageTk.PhotoImage(Image.open("bgimg_dim.png"))
        canvas.create_image(0,30, anchor = NW, image = image)
        canvas.pack()

        self.labelsep = Label(self.frame2, text = "\n")
        self.labelsep.pack()
        self.frame2.pack()

        self.frame3 = Frame(window)

        
        self.labelchoice = Label(self.frame3, text = "****  Choose Mode To Play  ****\n" , font = "Times 15 italic underline")
        self.labelchoice.pack()

        
        self.btnCpu = Button(self.frame3, text = "vs CPU", font = "Times 15 italic" ,command = self.vsCPU)
        self.btnCpu.pack(side = LEFT)
        #self.btnCpu.pack()
        self.labelsp = Label(self.frame3,text = "                                 ")
        self.labelsp.pack(side = LEFT)
        self.btnPlayer = Button(self.frame3, text = "vs Player", font = "Times 15 italic" ,command = self.vsPLAYER)
        self.btnPlayer.pack()
        #self.btnCpu.pack()
        self.frame3.pack()

        window.mainloop()

    def vsCPU(self):
        import final_game

    def vsPLAYER(self):
        import final_game_extended

Game()
