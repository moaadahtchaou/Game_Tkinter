from tkinter import * 
import tkinter #33 ==>hadi importitha bach nb9a n3rf wach l variable li ran5dm 3lih wwach button wla la 
from tkinter.messagebox import showinfo #34==>hadi rir yla marb7 7ta chi wa7ed
from random import choice #35 ==>hadi kola mra yb9a ytbdl chkon li rayl3b lwl machi dima x wla o
import threading #36 ==> hadi 3la 9bl l time.sleep mli kat5dmha ymkn t7rk l app wcha7l mn haja machi darori tsna time 7ta ysali mohim makatblokach ba9i l app
import time #37 ==> hadi 3la wd time.sleep 

class games():

    def __init__(self,frame3,gamenow):
        self.fr3=frame3 #38 ==> hna lframe frame 3
        self.XX=choice([True,False]) #39 ==> whadi kat5tar ya x li hya True wla O lli hya False
        
        self.player_X=0 #40 ==> hna score d X
        self.player_O=0 #41 ==> hna Score d O
        
        self.image_x=PhotoImage(file=r'C:\Users\moaad\Desktop\Gui_modern\Image\X.png') #42 ==> hadi picture d X l79ach lbutton mli ratdrt 3lih atwli f blasto ya X ya False 3la 7asab self.XX wach False wla True
        
        self.image_o=PhotoImage(file=r'C:\Users\moaad\Desktop\Gui_modern\Image\O.png') #43 ==>hadi picture d O
        
        
        self.listt=[] #45 ==> hadi drtha bach lbutton li drt 3lih kaysift ra9m b7al lbutton lwl kaysift ra9m 1 l wa7d lfunction dik lfunction katchd wa7d wkatzido lhad list bach mli n3awd ndrt 3la nfs lbutton atl9ah deja kayn f list wmaray5dmch l command
        
        self.dic={"1":"None",
                  "2":"None",
                  "3":"None",
                  "4":"None",
                  "5":"None",
                  "6":"None",
                  "7":"None",
                  "8":"None",
                  "9":"None"} ##46 ==> hado drthom bach n3rf lbutton li fih X li hiya True WL BUTTON LI FIH FALSE LI HIYA O 
        
        self.gamenow=gamenow# 47 ==> hadi hiya dik self.gamenow="No game" hadchi mli ylah katdrt 3la lcanvas li fiha logo d tica tac toe 
        
        if self.gamenow!="tic_tac_toe": ##48 ==> had l if kay5dm f awl mra katdrt 3la lcanvas li fiha logo d tic tac
            
            self.tic_tac_toe_edit() ##49 ==> hadi hiya li rat9ad lina kolchi f lframe mn lbdya sir l had lfunction  
             
        else:
            
            self.tic_tac_toe_destroy_all()##100==> hadi drtha bach mli tdrt 3la lcanvas kolchi ytms7 
            
            self.tic_tac_toe_edit() ##101==> whna rayt3awd 3ytttt 


    def tic_tac_toe_edit(self):
        
        self.canvas_game=Canvas(self.fr3,width=317,height=235,highlightthickness=0,bg="#1c2541") ## 50 ==> hadi l canva li 3liha l buttons w kda 
        self.canvas_game.place(x=150,y=150)

        self.canvas_game.create_line(105,0,105,240,fill="black",width=3) #51 ==> hado homa dok l5tota li m9smin l canvas 
        
        self.canvas_game.create_line(209,0,209,240,fill="black",width=3)
        
        self.canvas_game.create_line(0,78,325,78,fill="black",width=3)
        
        self.canvas_game.create_line(0,155,325,155,fill="black",width=3)
        
        
        self.canvas_game.create_line(1,0,317,1,fill="#0C151D",width=4) ##52 ==> whado l 5tota li dayrin b buttons
        
        self.canvas_game.create_line(316,0,316,235,fill="#0C151D",width=4)

        self.canvas_game.create_line(0,234,317,234,fill="#0C151D",width=4)
        
        self.canvas_game.create_line(1,0,1,235,fill="#0C151D",width=4)
        
        
        
        self.label_X=Label(self.fr3,image=self.image_x,bg="#121F2B",bd=0) ##53 ==> hadi label li katkon fo9 mnha lyd 
        self.label_X.place(x=397,y=115)
        
        self.label_O=Label(self.fr3,image=self.image_o,bg="#121F2B",bd=0)##53 ==> wh7a hadi lebel li ratkon fo9 mnha lyd z3ma bach t3rf chkon fihom li raybda rl3b
        self.label_O.place(x=432,y=115)
        
        self.label_hand=Label(self.fr3,text="☟",bg="#243F56",foreground="red",bd=0,font=("blod",30)) ##54 ==> hadi hiya lyd li ratkon fo9 mn label li ratwrik nobtmn

        self.label_score_X=Label(self.fr3,text=f"{self.player_X}",foreground="#f94144",bg="#243F56",bd=0,font=("blod",50))##55 ==> hadi hiya dik label li fih score dyal l X W O 
        self.label_score_X.place(x=237,y=30)
        
        self.label=Label(self.fr3,text="|",foreground="#415a77",bg="#243F56",bd=0,font=("blod",50)) ##56 ==> hada binathom 
        self.label.place(x=295,y=25)
        
        self.label_score_O=Label(self.fr3,text=f"{self.player_O}",foreground="#00b4d8",bg="#243F56",bd=0,font=("blod",50))##55 ==> hadi hiya dik label li fih score dyal l X W O
        self.label_score_O.place(x=337,y=30)
        
        
        
        self.tic_tac_toe_buttons()#56 ==> hadi hiya li kat9ad lbuttons l79ach mafiya manb9a n9ad kola button f blasto mchit drt lbutton 1 w 2 w 3 w 4 w7 bach n3rf l x wl y li kaynin fihom wbch7al bach kaytzado wkda w9adit function :) l79ach aslan button 3ndhom nfs tol wl3rd
        
        
        self.O_X()#66 ==> hadi ratmchi bach tchuf chkon yl3b lwl
        
    
    
    def O_X(self):
        if self.XX:
            self.label_hand.place(x=400,y=60) #67 ==> radi tkon fhad l place yla kant self.XX True y3ni ratkon fo9 X
        else:
            self.label_hand.place(x=437,y=60) # 68 ==> whadi mli tkon self.XX false 
            # self.label_X.config(bg="#121F2B")
            # self.label_O.config(bg="#06d6a0")

        
        
    def tic_tac_toe_buttons(self):
        
        self.w=False ##57 ==> hadi katbyn bli mazal mrb7 7ta chi wa7d drtha bach mli n tchecki wach l lbutton kamlhom 3mro wmarb7 7ta wa7d wla mumkin y3mro w f2a5ir clicke li rat3mr ga3 l buttons yrb7 chi wa7d wnsd9 9aylihom bli kolchi 3mr wt3adlo yarbi tkon fhmti ana wmafhmt
        self.x=153 ##58 ==> hadi dyal z3ma awl button fin raykon
        self.y=153 ##58 ==> hadi dyal z3ma awl button fin raykon
        
        for i in range(9):
            
            self.buttt=Button(self.fr3,bg="#3a506b",highlightthickness=0,bd=0)
            self.buttt.place(x=self.x,y=self.y,width=100.5,height=74) 
            self.x+=104 #59 ==> hna z3ma lbutton 2 rayk7z b 104 3la lwl w 3 7ta howa 
            if i ==2 or i==5 :##60 ==> mn b3d 3arfin bil range kaybda mn 0 y3ni lbutton 3 howa i==2 wl y3ni lbutton 4 raykon fnfs x dyal lbutton lwl dakchi 3lach rj3t lx l 153 wlakin raykon t7t mno y3ni 5as l y tzad bach yji t7t mno 3ad 3wtani mli rawsl lbutton 6 li hiya i==5 5aso x trj3 3wtani lnfs l x dyal lbutton 1 w 4 w y tzad  bach lbutton 7 yji t7tmnho
                self.y+=77
                self.x=153

        self.key=1 #61 ==> hadi drtha bach nb9a n3rf lbutton li kant3aml m3ah l79ach 3ndhom nfs smya self.buttt w lakin lwl li t9ad kaydar f wa7d list li hiya winfo_children y3ni l button 1 raykon sab9 lbutton ra9m 2 ....
        
        for i in self.fr3.winfo_children():
            if isinstance(i, tkinter.Button): ##62 ==> self.fr3.winfo_children() hadi katchof l labels w l buttons wolchi li t9ado flframe 3 wlakin had isinstance kat9oliha z3ma wach i wach mn lclass  Button l79ach aslan f lframe 3 l button li 3ndi fih rir dyawl l game li homa 9               
                    if self.key==1: #63 ==>hadi mli katl9a l button lwl l79ach 9lt bli katrtbo f winfo_children b trtib lwl li tsayb kaytzad l liste y3ni awl button howa hada 
                        i.config(command=lambda :self.tic_tac_toe_text(1)) #64 ==> hna drto bach yb9a y3ti ra9m 1 l function tic_tac_toe_text  sir l #65
                    elif self.key==2:
                        i.config(command=lambda :self.tic_tac_toe_text(2))
                    elif self.key==3:
                        i.config(command=lambda :self.tic_tac_toe_text(3))
                    elif self.key==4:
                        
                        i.config(command=lambda :self.tic_tac_toe_text(4))
                    elif self.key==5:
                        
                        i.config(command=lambda :self.tic_tac_toe_text(5))
                    elif self.key==6:
                        
                        i.config(command=lambda :self.tic_tac_toe_text(6))
                    elif self.key==7:
                        
                        i.config(command=lambda :self.tic_tac_toe_text(7))
                    elif self.key==8:
                        
                        i.config(command=lambda :self.tic_tac_toe_text(8))
                    else:
                        i.config(command=lambda :self.tic_tac_toe_text(9))
                        
                        
                    self.key+=1 ##65 hadi mli ral9a l button ra9m 1 ratzad bach tl9a l buton ra9m 2 .....
    

    
    def tic_tac_toe_text(self,number_but): #69 ==> :]
        
        self.key=1 # 70 ==> hadi 3wtani bach n3rf lbutton wkda b7ala hada howa l id d lbuttons fl2asl katkon smya hiya l id wlakin daba mli l buttons kaytchabho f smya sf daba wlaw f7al f7al y3ni wla hada howa l id
        
        for i in self.fr3.winfo_children():
            
            if isinstance(i,tkinter.Button):# chr7tha
                
                if self.key==number_but: #71 ==> hna had number_but howa ra9m li katsifto l button l had lfunction kola button kaysift ra9m m5talf button 1 kaysift 1 .....
                    #                                     daba mli lbutton 2 kaysift 2 for kat5dm yak w self.fr3.winfo_children() fiha bzf d label wlbuttons wlcanva.. ana bari ri lbutton whadi isinstance(i,tkinter.Button) li kat3tini rir l button mrtbin sf ana bari lbuttons 2 y3ni mli ywli l self.key ==2 3ad 5dm
                    
                    if self.key not in self.listt:##72 ==> hna fach kanchof wach lbuttons feja 5dm wla la l79ach yla faytlih 5dm 5aso my3awdch y5dm
                        
                        if self.XX: ##73 ==> hadi katchof wach lbuttons ratwli fih l image X wla l image  O yla kan True rah X 
                            
                            i.config(image=self.image_x,bg="#1c2541")##74 ==> hadi radir f lbutton 2 X w ratlwno bach ykon m5talf 
                            
                            self.dic[f"{self.key}"]=self.XX ##75  ==> hadi b7ala an9olk hiya lgame mli lbutton 2 ratkon fih X katji hiya l value 2 li fiha None ratrdha True z3ma fiha X
                            
                            self.listt.append(self.key) ##76 ==> whadi ratzid lbutton 2 l list bach yla clicket 3lih my3awdch y5dm ay7bso  line 165
                            
                            if len(self.listt)>=5: ## 77 ==> hadi hiya li katchof wach rb7 chi wa7d wla la katchof awl 7aja wach l3bo 5 dlmrat l79ach maymknch chi wa7ed yrb7 whowa la3b ra mra 5aso 3 d l x ila sb9 y3ni L O raykon lb 2 mrat y3ni 5 flmjmo3
                                
                                self.tic_tac_toe_check()##83
                                
                            self.XX=False## 78 ==> hadi ratwli False bach tji nobt O
                            
                            self.O_X() ##79 ==> bach lhand tmchi 3nd O z3ma nobto
                            
                            
                        else:
                            
                            i.config(image=self.image_o,bg="#1c2541")
                            
                            self.dic[f"{self.key}"]=self.XX
                            self.listt.append(self.key)
                            
                            if len(self.listt)>=5:
                                
                                self.tic_tac_toe_check()
                                
                            self.XX=True
                            self.O_X()
                    else:
                        print("{} is already clicked".format(self.key)) ##80 ==> hadi kat5dm yla drti 3la nfs l button 2 mrat 
                self.key+=1 
                            
        # print(self.dic)
        if self.w==False: ##81 ==> hadi katchouf wach 7ta wa7d mrb7                             
            if len(self.listt) == 9: ##82 ==> hadi katchuf wach ga3 l button 3mro 
                ##83 mli 7ta chi wa7ed mrb7 wga3 les buttons 3mro y3ni ta3adol hadak chrt lwl zdto l79ach momkin ga3 lbuttons y3mro wlakin 2a5ir button 3mr howa li rb77 chi wa7d 
                showinfo(message="game end no one win :( ")
                self.tic_tac_toe_again()##hadi kat3awd l3ba mn lwl wlakin kat5li score 

            
            
            
    def tic_tac_toe_check(self):
        ##83 mli katchof ch7al dyal toro9 bach trb7 fl game 5as ya 1 w 4 w 7 ykono True z3ma x wla 2 w 5 w 8 wla  3 w 6 w 9 y3ni kanzid b 1 fihom kamlin hadchi li kayn f l m=0 
        ##83 3wtani bach trb7 5as lbuttons 1 2 3 wla 4 5 6 wla 7 8 9 kaytzado b 3 hadchi li kaydar f m=1 
        ##83 wkanchof l2a5ir wa7d l3b wach rb7 wla la maknchofoch l x w o kanchofo rir l5r li l3b 
        
        a=1 ##84 ==> hada lbutton 1
        b=4 ##84 ==> hada lbutton 4
        c=7 ##84 ==> hada lbutton 7
        
        for m in range(2):
            
            for i in range(3):

                    if self.dic[str(a)]==self.XX and self.dic[str(b)]==self.XX and self.dic[str(c)]==self.XX :
                        
                        r=[a,b,c]##85 hna kayt5zno fih lbuttons li fihom chrt bli rb7 
                        
                        if self.XX==False:
                            self.if_win("O",r)##86 hna z3ma yla self.xx ==False y3ni rah O lirb7 dakchi 3lach kansift O lfunction if_win
                            
                        else:
                            self.if_win("X",r)## w7ta hna
                            
                    if m==0:
                        a+=1
                        b+=1
                        c+=1
                    else:
                        a+=3
                        b+=3
                        c+=3       
            a=1##84 ==> hada lbutton 1
            b=2##84 ==> hada lbutton 2
            c=3##84 ==> hada lbutton 3
            
        ##83 hado 3wtani toro9 yla bari trb7 5as button 1 w 5 w 9 ykon f7al f7al wla 3 w 5 w 7 mabantch li chi 3ala9a binathom dakchi 3lach drthom b if 
        if self.dic[str(1)]==self.XX and self.dic[str(5)]==self.XX and self.dic[str(9)]==self.XX :
            
                        r=[1,5,9]
                        if self.XX==False:
                            self.if_win("O",r)
                        else:
                            self.if_win("X",r)
        elif self.dic[str(3)]==self.XX and self.dic[str(5)]==self.XX and self.dic[str(7)]==self.XX:
            
                        r=[3,5,7]
                        if self.XX==False:
                            self.if_win("O",r)
                        else:
                            self.if_win("X",r)
                            
                            
    def if_win(self,o_or_x,list):
        
        label_info=Label(self.fr3,text=f"{o_or_x} win 👋",font=('Blod',50),bg="#243F56",foreground="#06d6a0")#87 ==> hadi katwrik chkon li rb7 dik o_or_x hiya li dak str ya "O" wla "X"
        label_info.place(x=135,y=30)
        
        self.key=1  
        for  i in self.fr3.winfo_children():
            if isinstance(i,tkinter.Button):
                
                i.config(state="disabled") #88 ==> hna ga3 lbutton ykono disabled z3ma mt9dch tdrt 3lihom 7ta ysali dak df sleep
                
                if self.key in list: ## 89==> hna bach l buttons ywliw b l green 5asni n3rfhom wrah homa li kaynin f r li katsifto fonction check mohim mli kaywsl dak lbutton kaytlwn wsf
                    
                    i.config(bg="#06d6a0")
                    
                    
                self.key+=1
                
        def sleep():
            
            time.sleep(3) #90 ==> hna katb9a tsna 3 dseconds
            
            label_info.destroy() ##91 ==>  whna dik label li katbyn lik li rb7 kat7yd
            
            self.w=True #92 ==> whna katwli hadi true bach z3ma yla lbuttons 3mro wrb7 chi wa7ed t7sb          
            
            self.tic_tac_toe_again()# 93 
        
        if o_or_x=="X":
            
            self.player_X+=1#90 ==>  yla kant o_or_x y3ni score d lplayer x raytzad 
            
            self.label_score_O.config(text=f"{self.player_O}")
            self.label_score_X.config(text=f"{self.player_X}") #91 ==> han kan3awd n dir update l les score
            
            threading.Thread(target=sleep).start() #92==> hadi kat5dm function sleep
            
        else:
            self.player_O+=1
            
            self.label_score_O.config(text=f"{self.player_O}")
            self.label_score_X.config(text=f"{self.player_X}")
            
            threading.Thread(target=sleep).start()
        
                     
    def tic_tac_toe_again(self):
        
        for  i in self.fr3.winfo_children():
            if isinstance(i,tkinter.Button):
                i.destroy() # ga3 lbutton kaytm7aw
            
        self.dic={"1":"None",
                  "2":"None",
                  "3":"None",
                  "4":"None",
                  "5":"None",
                  "6":"None",
                  "7":"None",
                  "8":"None",
                  "9":"None"} # hadi katrj3 kifma kant bach t3awd l3ba
        
        self.XX=choice([True,False]) 
        
        self.listt.clear()#hadi list katm7a
        
        self.O_X() # kan3awdo nchof chkon yl3b l79ach haf line 325 3awdt drt self.XX ta5d chi 9yma
        
        self.tic_tac_toe_buttons()## saf whna rayt3awd button jdad l79ach hadok tm7aw sf ama label wdakchi rayb9aw
        
    def tic_tac_toe_destroy_all(self):
        for i in self.fr3.winfo_children():
            i.destroy() ##hadi ratm7i kolchi li flframe3 
    
    
    
    
