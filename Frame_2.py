from tkinter import *

class frame_game():
    def __init__(self,canvas):
        self.canvas=canvas# hna dik lcanvas li kat3tih katwli f self.canvas bach twli global 3la ga3 lfunction
        
    def frame_2_image(self):
        global image_logo,image_tic,image_tac,image_toe
        
        image_logo=PhotoImage(file='Image\logotictac.png') #}
        image_tic=PhotoImage(file="Image\TIC.png")          #}
        image_tac=PhotoImage(file="Image\TAC.png")          #} 26 ==> hna 5dit kola swra bo7dha bach tji m9ada logo bo7do w smya tic bo7dha wtac bo7dha ...
        image_toe=PhotoImage(file="Image\TOE.png")         #}
        
        
        self.canvas.create_image(25,25,image=image_logo)    #}
        self.canvas.create_image(65,25,image=image_tic)      #} 27 ==> hna kola picture bo7dha 9adithom bach ybano f7al logo wa7d
        self.canvas.create_image(97,25,image=image_tac)      #}
        self.canvas.create_image(135,25,image=image_toe)    #}
    
    def tic_tac_toe_focus(self):
        
        # canvas=Canvas()
        self.canvas.config(cursor="hand2",bg="#8C9EA1")  #22==> hna dik l canvas ratwli bhad lon yla d5lti lmouse chr7t f #21 w7ta l cursor raywli 3la chkl yd
