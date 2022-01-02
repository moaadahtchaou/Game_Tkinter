#2/1/2022
"""tb3 l2ar9m li mora l #
    bach tfhm lcode
"""

from tkinter import *
from title_bar import *
from Frame_2 import *
from tic_tac_toe import *
class app(Tk):
    
    def __init__(self):
        
        super().__init__()
        # self.update_idletasks()
        # self.resizable(False,False)
        # self.withdraw()
        # self.wm_grid()
        # self.tk_focusFollowsMouse()
        # self.wm_iconwindow()
        # self.deiconify()
        # self.attributes("-topmost",1)
        # self.focus_force()
        # self.wm_attributes('-type', 'splash')
        # # # # self.wm_attributes('-fullscreen','true')
        # self.tkraise()
        # tksupport.install(self.win)
        # self.wm_attributes('-type', 'splash')
        """self rah howa root :)
        """
        
        self.overrideredirect(True)#1==> hadi kat7yd titlebar lmuchkil kat7yd 7ta l icon les f taskbar ba9i ml9itch kifach nrj3hom 
        
        self.background() #2==> hhhhh hadi mamnha 7ta fayda rir drtha wsf kat9ad blast lgeometry
        
        self.gamenow="No game"# hadi drtha 3la 9bl bach n3rf wach lgame 5dmat mn 9bl wla la wchnu smit lgame l79ach mazal nawi nzid chi game a5ra 
        
        self.frame_bar() #4==> hadi rat9ad titlebar 
        
        self.frame_left() #19==> hadi rat9ad lframe li fih logo d tic_tac_toe
        
        self.frame_right()#28==> hadi rat9ad lframe li ratkon fih l game whadi li fih rwinaaa
        
    def background(self):
        
        self.geometry("780x420+600+350") #3==> 780x420 dyal size d lwindow li rat9ad w dik +600+350 z3ma lblasa li bari ykon fiha lapp 
        

       
       
        
    def frame_bar(self):
        frame1_bg="#121F2B"#5==>hada rir lbg dlframe
        
        global icon #6==>hadi darori 5sni ndirha bach l image tban 
        
        frame1=Frame(self,bg=frame1_bg)#E1F2FE
        frame1.place(x=0,y=0,height=30,width=780) 
        
        frame1.bind("<B1-Motion>",self.move)#7==> hadi drtha bach mli drt 3la left click f mouse fl title bare wt7rkha yb9a ytr7k 7ta howa

        butt.frame1_bar_edit(frame1,self,frame1_bg)#8==> go to title_bar.py hadi li ray9ad lina dok icon li f title bar 

        
        icon=PhotoImage(file="Image\icontitle.png")#16==> hadi 7ta hiya yla bari dir debug dir l path kaml d licon 
        
        canvas = Canvas(frame1, height=45, width=45, bg=frame1_bg,highlightthickness=0)
        canvas.place(x=0,y=0)
        
        canvas.create_image(20,15,image=icon) #17==> hna sybt l icon li drtha f title bar tswira d l anime 
        
        title=Label(text="Workspace",foreground="white",bg=frame1_bg,font=("blod",13)) #18==> whna 9adit title d l app wa5a ma title ma tal3ba 
        title.place(x=40,y=5)
        
        
        
    def frame_left(self):
        
        frame2_bg="#365E81"
        
        frame2=Frame(self,bg=frame2_bg)
        frame2.place(x=0,y=30,width=155,height=390)
        
        
        canvas_tic_tac_toe=Canvas(frame2,bg="#7D9094",highlightthickness=0)#20==> lcanva li drt fiha logo 
        canvas_tic_tac_toe.place(x=0,y=20,width=155,height=50)

        canvas_tic_tac_toe.bind("<Enter>",lambda event:frame_game(canvas_tic_tac_toe).tic_tac_toe_focus()) #21==> hna yla lmouse d5l l zone dyal lcanvas rat5dm dak lcommand go to frame_2.py wlakin rir function tic_tac_toe_focus

        canvas_tic_tac_toe.bind("<Leave>",lambda event :canvas_tic_tac_toe.config(bg="#7D9094")) #23==> hadi yla 5rjti l mouse kayrj3 lcolor kifma kan  #7D9094  
        
        canvas_tic_tac_toe.bind("<Button-1>",lambda event :self.gamess_tic(self.frame3,self.gamenow)) ##24 ==> mli kat clicke 3la logo d tic tac toe kat5dm lfunction self.gamess_tic hiya l5ra ranchr7ha
        
        
        frame_game(canvas_tic_tac_toe).frame_2_image() #25==> hna kayt9ad logo d tic ... flcanvas go to Frame_2.py
        


    def frame_right(self):
        
        frame3_bg="#243F56"#365E81
        
        self.frame3=Frame(self,bg=frame3_bg) #29 ==> frame 3 drto self. l79ach howa li raybda ytbdl wkda ama hado lframe li 9bl mno mli kat7l l app kayt9ado sf mkytbdlo ma walo machi f7al hada
        self.frame3.place(x=155,y=30,width=625,height=390) 
        

      
    def move(self,e):
        self.geometry("+{}+{}".format(e.x_root,e.y_root)) #30 ==> hadi hiya li kat7rk l app kat7rk bnsba l blasa li fiha l mouse dyalk

        
        
    def gamess_tic(self,fr3,gamenow):
        
        games(fr3,gamenow)#31 ==> hna fach kayna lgame d tec tac toe wmn l2a7san yla randir chi game a5ra ndirha f chi file a5or machi dyal tic_tac_toe.py kanhdr m3a rasi ila bari nzid chi game :)
        
        self.gamenow="tic_tac_toe" #32 ==> hadi ranchr7ha f ltic_tac_toe.py
        
        
        
if __name__ == "__main__": 
    
    root= app() 
    
    root.mainloop()
