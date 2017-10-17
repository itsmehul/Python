from tkinter import*

class BuckyButton:
    #An Object is created automatically when the function is called
    #We call the main window master; ie Master=Root
    def _init_(self, master):
        frame=Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Works bruv")

root=Tk()
b= BuckyButton(root)
root.mainloop()
