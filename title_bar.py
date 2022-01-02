from tkinter import PhotoImage,Button

class butt():    
    def frame1_bar_edit(fr1,self,but_bg):
            global image_destroy,image_fullscreen,image_minimize #hadi 5ask darori dirha hadchi kayn ra f tkinter m3rftch 3lach 
                
            width_row_0=35 #9==> hadi hiya size dlbutton bnsba l x
            height_row_0=20 #10==> whadi size d lbutton bnsba l y
                

            image_destroy=PhotoImage(file="Image\destroy.png") #11==> hna ana drt lpath rir dyal limage direct yla bari dir Debug 5ask tktb lpath kaml b7al r"C:\Users\moaad\Desktop\Gui_modern\Image\destroy.png"
            image_fullscreen=PhotoImage(file=r"Image\fullscreen.png")#12==> had r li drt 9bl mn hadi rir bach t3rf l python bli hada rah path l79ach mli kaykon lpath fih b7al haka \n wla \t wla \f kay5sk darori dir r
            image_minimize=PhotoImage(file="Image\minimize.png")
                
            but_exit=Button(fr1,image=image_destroy,command=self.destroy,bd=0,highlightthickness=0,bg=but_bg,width=width_row_0,height=height_row_0)#13==> hadi fiha l command li howa self.destroy w self howa root
            but_exit.place(x=745,y=1)
                
            but_fullscreen=Button(fr1,image=image_fullscreen,bd=0,highlightthickness=0,bg=but_bg,width=width_row_0,height=height_row_0)#14==> hadi ra dikor m3rftch kifach n9ad l fullscreen
            but_fullscreen.place(x=710,y=1)

            but_minimize=Button(fr1,image=image_minimize,bd=0,highlightthickness=0,bg=but_bg,width=width_row_0,height=height_row_0)#15==> w 7ta hadi :{
            but_minimize.place(x=675,y=1)
