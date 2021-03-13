##BAT MAKER


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as font


defaultCOL = "#676767"


file_paths = []

def dummyFUNC():

  pass


class HoverButton():
    

  def __init__(self,master,x,y,text,height,width,color="#FFF",command=dummyFUNC):

    self.x = x
    self.y = y

    self.myFont = font.Font(size=15,weight="bold")

    self.hButton = Button(master,text=text,width=width,height=height,command=command, bg=defaultCOL, fg="#FFF",activebackground="#90c418")

    self.hButton.pack()
    self.hButton.place(x=self.x,y=self.y)
    
    self.hButton.bind("<Enter>", self.on_enter)
    self.hButton.bind("<Leave>", self.on_leave)

    self.hButton['font'] = self.myFont 

  def on_enter(self,e):

    self.hButton['background']="#A8E51B"
  
  def on_leave(self,e):

    self.hButton['background']=defaultCOL



class Window(Tk):

  def __init__(self):

    super().__init__()


    self.width=500
    self.height=500
    self.myFont = font.Font(size=15,weight="bold")
    

    self.globalColBG = "#252526"
    self.globalColABG = "#A8E51B"

    self.title("EXE executer")
    self.resizable(0,0)
    self.geometry(f"{self.width}x{self.height}")
    self.config(bg="#252526")

    self.title = Label(self,width="10",text="EXE Executer",bg=self.globalColBG, fg="#FFFFFF")
    self.title.pack()
    self.title.place(x=250-60,y=15)

    self.title['font'] = self.myFont 

    ##---- BUTTON CODE

    self.infoButton = HoverButton(self,self.width-50,10,"?",1,2,command=self.info)
    self.FEButton = HoverButton(self,40,200,"File Explorer",1,12,command=self.FE)
    self.manualButton = HoverButton(self,320,200,"Manual",1,12,command=self.Manual)
    self.generateButton = HoverButton(self,175,345,"Generate file",1,12,command=self.GenerateBAT)
      
    ##-----------------------------------------

    ##BUTTON FUNCTIONS -----
    
  def info(self):

    messagebox.askokcancel("------Information------","""--Purpose--\n
The purpose of the software is to help you the user create a batch file that opens all the executables you want in one go. 
\n\n--File Explorer Button---\n
Takes you to the file explorer to choose the file you want to add to the 'myEXEC.bat' file.\n
\n--Manual Button--\n
This will prompt you with an entry field and a go button. This is for you to enter the file path of your EXE file if that is your preferred method\n
\n--Go Button--\n
This button will create the bat file, this bat file is fully editable and is just a simple contigiuous line of start commands.\n
\n--Contact--\n
GitHub: https://github.com/Barnold8\n
Email: bandslover@outlook.com\n
Student Email (subject to change/no longer become active): 142359@student.nottinghamcollege.ac.uk

""")

  def FE(self):

    local_var = filedialog.askopenfilename()
    local_var_list = local_var.split('/')

    file = local_var_list[len(local_var_list)-1].split('.')
    if file[len(file)-1].lower() != "exe":

      messagebox.showerror("ERROR",f"An EXE file was expected but file type '{file[1]}' was given")
    
    else:
      file_paths.append(local_var)
      print(file_paths)

  def Manual(self):


    def getter():


      local_var = _manual_entry.get()
      local_var_list = local_var.split('/')

      if len(local_var_list):
         messagebox.showerror("ERROR","Unepected error!\n\nThe file you are trying to access is either in the same directory as this program or it does not exist.\n\nStill having problems? Click the question mark for contact information")
         return
        
      file = local_var_list[len(local_var_list)-1].split('.')
      if file[len(file)-1].lower() != "exe":

        messagebox.showerror("ERROR",f"An EXE file was expected but file type '{file[1]}' was given")
    
      else:
        file_paths.append(local_var)
        print(file_paths)

    _manual = Tk()
    _manual.title("Manual")
    _manual.resizable(0,0)
    _manual.geometry("350x300")
    _manual.config(bg="#252526")
    EnterButton = HoverButton(_manual,115,200,"Enter",1,12,command=getter)
    _manual_entry = Entry(_manual,width="40")
    _manual_entry.pack()
    _manual_entry.place(x=55,y=100)
    _manual.mainloop()

  def GenerateBAT(self):

    allFILES = file_paths
    if len(allFILES) <= 0:
      messagebox.showerror("ERROR",f"Length error!\n\nThe amount of file paths in the program: {len(allFILES)}, expected at least 1 file path.")

    else:

      f = open("EXECFILE.bat", 'w')
      for i in range(len(allFILES)):
        f.write(f'start "title" "{allFILES[i]}"\n')

      
      f.close()
## ---------------

GUI = Window()


#file_path = filedialog.askopenfilename()
