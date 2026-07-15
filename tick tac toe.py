import tkinter as tk
import random as r
import json
from json.decoder import JSONDecodeError
##stats_part
def login():
    def login_info():
        global user
        try:
            with open('login.json','r') as f:
                info=json.load(f)
                name_4=name_3.get()
                if not info:
                    login_win.destroy()
                    login()
                elif name_4 in info and info[name_4]==password.get():
                    user=name_4
                    login_win.destroy()
                    game()
                else:
                    login_win.destroy()
                    login()
        except (FileNotFoundError,JSONDecodeError):
            login_win.destroy()
            login()
    def login_2():
        signin_win.destroy()
        login()
    def signin():
        global signin_win
        global password_2
        global password_3
        global name_5
        login_win.destroy()
        signin_win=tk.Toplevel(main_win)
        signin_win.geometry('500x170+440+230')
        signin_win.config(bg='lightgrey')
        signin_win.title('Sign in')
        password_2=tk.Entry(signin_win,font='arial,15',width=26,show='*')
        password_3=tk.Entry(signin_win,font='arial,15',width=26,show='*')
        back_login=tk.Button(signin_win,font='arial,7',width=10,text='log in',bg='grey',fg='white',command=login_2)
        back_login.place(relx=0.25,y=120)
        name_5=tk.Entry(signin_win,font='arial,15',width=26)
        name_5.place(relx=0.25,y=30)
        password_2.place(relx=0.25,y=60)
        password_3.place(relx=0.25,y=90)
        next_bt_2=tk.Button(signin_win,font='arial,15',width=4,text='Next',bg='grey',fg='white',command=signin_info)
        next_bt_2.place(x=320,y=125)


    def signin_info():
        global user
        p=password_2.get()
        p_2=password_3.get()
        name_6=name_5.get()
        if p==p_2:
            password_4=p_2
        else:
            signin_win.destroy()
            signin()
        try:
            with open('login.json','r') as f:
                info_2=json.load(f)
            if name_6 in info_2  :
                raise 
            info_2.update({name_6:password_4})
            with open('login.json','w') as f:
                json.dump(info_2,f)

                user=name_6
                signin_win.destroy()
                game()

            
        except (FileNotFoundError,JSONDecodeError):
            with open('login.json','w') as f:
                json.dump({name_6:password_4},f)
                
                user=name_6
                signin_win.destroy()
                game()
        except:
            signin_win.destroy()
            signin()
            
    login_win=tk.Toplevel(main_win)
    login_win.config(bg='lightgrey')
    login_win.geometry('500x160+440+230')
    login_win.title('log in')
    name_3=tk.Entry(login_win,font='arial,15',width=26)
    name_3.place(relx=0.25,y=30)
    password=tk.Entry(login_win,font='arial,15',width=26,show='*')
    password.place(relx=0.25,y=60)
    create_account=tk.Button(login_win,font='arial,7',width=10,text='sign in',bg='grey',fg='white',command=signin)
    create_account.place(relx=0.25,y=100)
    next_bt=tk.Button(login_win,font='arial,15',width=4,text='Next',bg='grey',fg='white',command=login_info)
    next_bt.place(x=320,y=100)
def game():
    #click
    def click_1():
        global click
        click=1
        game_loop()
    def click_2():
        global click
        click=2
        game_loop()
    def click_3():
        global click
        click=3
        game_loop()
    def click_4():
        global click
        click=4
        game_loop()
    def click_5():
        global click
        click=5
        game_loop()
    def click_6():
        global click
        click=6
        game_loop()
    def click_7():
        global click
        click=7
        game_loop()
    def click_8():
        global click
        click=8
        game_loop()
    def click_9():
        global click
        click=9
        game_loop()
    #game_win
    game_win=tk.Toplevel(main_win)
    game_win.geometry('300x300+550+230')
    game_win.title(f'welcome {user}')
    bt_1=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_1)
    bt_2=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_2)
    bt_3=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_3)
    bt_4=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_4)
    bt_5=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_5)
    bt_6=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_6)
    bt_7=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_7)
    bt_8=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_8)
    bt_9=tk.Button(game_win,width=14,height=7,bg='lightgrey',font='arial,15',command=click_9)
    bt_1.place(relx=0,rely=0)
    bt_2.place(relx=1/3,rely=0)
    bt_3.place(relx=2/3,rely=0)
    bt_4.place(relx=0,rely=1/3)
    bt_5.place(relx=1/3,rely=1/3)
    bt_6.place(relx=2/3,rely=1/3)
    bt_7.place(relx=0,rely=2/3)
    bt_8.place(relx=1/3,rely=2/3)
    bt_9.place(relx=2/3,rely=2/3)
    

        
    #game
    global x,o
    x=[]
    o=[]
    win_cons=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    def place_x():
        global x_1
        global o_1
        if click==1:
            bt_1.config(text='X',state='disabled')
            x.append(1)
        elif click==2:
            bt_2.config(text='X',state='disabled')
            x.append(2)
        elif click==3:
            bt_3.config(text='X',state='disabled')
            x.append(3)
        elif click==4:
            bt_4.config(text='X',state='disabled')
            x.append(4)
        elif click==5:
            bt_5.config(text='X',state='disabled')
            x.append(5)
        elif click==6:
            bt_6.config(text='X',state='disabled')
            x.append(6)
        elif click==7:
            bt_7.config(text='X',state='disabled')
            x.append(7)
        elif click==8:
            bt_8.config(text='X',state='disabled')
            x.append(8)
        elif click==9:
            bt_9.config(text='X',state='disabled')
            x.append(9)
    def chek_x():
        global x
        global o
        for i in win_cons:
            for j in i:
                if j not in x:
                    break
            else:
                game_win.destroy()
                winner=tk.Toplevel(main_win)
                winner.title('game over')
                winner.geometry('300x150+550+230')
                winner.config(bg='lightgrey')
                win_lb=tk.Label(winner,fg='white',bg='grey',text='won the game',width=14)
                win_lb.place(relx=0.5,rely=0.2,anchor='center')

    def chek_o():
        global x
        global o
        for i in win_cons:
            for j in i:
                if j not in o:
                    break
            else:
                game_win.destroy()
                losser=tk.Toplevel(main_win)
                losser.title('game over')
                losser.geometry('300x150+550+230')
                losser.config(bg='lightgrey')
                win_lb=tk.Label(losser,fg='white',bg='grey',text='lost the game',width=14)
                win_lb.place(relx=0.5,rely=0.2,anchor='center')

    def place_o():
        global x
        global o
        loop_2=True
        if len(o)+len(x)==9:
            loop_2=False
        for i in win_cons:
            count=0
            for j in i:
                if j in o:
                    count+=1
            if count==2 and loop_2==True:
                if i[0] not in o and i[0] not in x:
                    loop_2=False
                    if i[0]==1:
                        bt_1.config(text='o',state='disabled')
                        o.append(1)
                    elif i[0]==2:
                        bt_2.config(text='o',state='disabled')
                        o.append(2)
                    elif i[0]==3:
                        bt_3.config(text='o',state='disabled')
                        o.append(3)
                    elif i[0]==4:
                        bt_4.config(text='o',state='disabled')
                        o.append(4)
                    elif i[0]==5:
                        bt_5.config(text='o',state='disabled')
                        o.append(5)
                    elif i[0]==6:
                        bt_6.config(text='o',state='disabled')
                        o.append(6)
                    elif i[0]==7:
                        bt_7.config(text='o',state='disabled')
                        o.append(7)
                    elif i[0]==8:
                        bt_8.config(text='o',state='disabled')
                        o.append(8)
                    elif i[0]==9:
                        bt_9.config(text='o',state='disabled')
                        o.append(9)
                elif i[1] not in o and i[1] not in x:
                    loop_2=False
                    if i[1]==1:
                        bt_1.config(text='o',state='disabled')
                        o.append(1)
                    elif i[1]==2:
                        bt_2.config(text='o',state='disabled')
                        o.append(2)
                    elif i[1]==3:
                        bt_3.config(text='o',state='disabled')
                        o.append(3)
                    elif i[1]==4:
                        bt_4.config(text='o',state='disabled')
                        o.append(4)
                    elif i[1]==5:
                        bt_5.config(text='o',state='disabled')
                        o.append(5)
                    elif i[1]==6:
                        bt_6.config(text='o',state='disabled')
                        o.append(6)
                    elif i[1]==7:
                        bt_7.config(text='o',state='disabled')
                        o.append(7)
                    elif i[1]==8:
                        bt_8.config(text='o',state='disabled')
                        o.append(8)
                    elif i[1]==9:
                        bt_9.config(text='o',state='disabled')
                        o.append(9)

                elif i[2] not in o and i[2] not in x:
                    loop_2=False
                    if i[2]==1:
                        bt_1.config(text='o',state='disabled')
                        o.append(1)
                    elif i[2]==2:
                        bt_2.config(text='o',state='disabled')
                        o.append(2)
                    elif i[2]==3:
                        bt_3.config(text='o',state='disabled')
                        o.append(3)
                    elif i[2]==4:
                        bt_4.config(text='o',state='disabled')
                        o.append(4)
                    elif i[2]==5:
                        bt_5.config(text='o',state='disabled')
                        o.append(5)
                    elif i[2]==6:
                        bt_6.config(text='o',state='disabled')
                        o.append(6)
                    elif i[2]==7:
                        bt_7.config(text='o',state='disabled')
                        o.append(7)
                    elif i[2]==8:
                        bt_8.config(text='o',state='disabled')
                        o.append(8)
                    elif i[2]==9:
                        bt_9.config(text='o',state='disabled')
                        o.append(9)

        for i in win_cons:
            count=0
            for j in i:
                if j in x:
                    count+=1
            if count==2 and loop_2==True:
                if i[0] not in o and i[0] not in x:
                    loop_2=False
                    if i[0]==1:
                        bt_1.config(text='o',state='disabled')
                        o.append(1)
                    elif i[0]==2:
                        bt_2.config(text='o',state='disabled')
                        o.append(2)
                    elif i[0]==3:
                        bt_3.config(text='o',state='disabled')
                        o.append(3)
                    elif i[0]==4:
                        bt_4.config(text='o',state='disabled')
                        o.append(4)
                    elif i[0]==5:
                        bt_5.config(text='o',state='disabled')
                        o.append(5)
                    elif i[0]==6:
                        bt_6.config(text='o',state='disabled')
                        o.append(6)
                    elif i[0]==7:
                        bt_7.config(text='o',state='disabled')
                        o.append(7)
                    elif i[0]==8:
                        bt_8.config(text='o',state='disabled')
                        o.append(8)
                    elif i[0]==9:
                        bt_9.config(text='o',state='disabled')
                        o.append(9)
                elif i[1] not in o and i[1] not in x:
                    loop_2=False
                    if i[1]==1:
                        bt_1.config(text='o',state='disabled')
                        o.append(1)
                    elif i[1]==2:
                        bt_2.config(text='o',state='disabled')
                        o.append(2)
                    elif i[1]==3:
                        bt_3.config(text='o',state='disabled')
                        o.append(3)
                    elif i[1]==4:
                        bt_4.config(text='o',state='disabled')
                        o.append(4)
                    elif i[1]==5:
                        bt_5.config(text='o',state='disabled')
                        o.append(5)
                    elif i[1]==6:
                        bt_6.config(text='o',state='disabled')
                        o.append(6)
                    elif i[1]==7:
                        bt_7.config(text='o',state='disabled')
                        o.append(7)
                    elif i[1]==8:
                        bt_8.config(text='o',state='disabled')
                        o.append(8)
                    elif i[1]==9:
                        bt_9.config(text='o',state='disabled')
                        o.append(9)

                elif i[2] not in o and i[2] not in x:
                    loop_2=False
                    if i[2]==1:
                        bt_1.config(text='o',state='disabled')
                        o.append(1)
                    elif i[2]==2:
                        bt_2.config(text='o',state='disabled')
                        o.append(2)
                    elif i[2]==3:
                        bt_3.config(text='o',state='disabled')
                        o.append(3)
                    elif i[2]==4:
                        bt_4.config(text='o',state='disabled')
                        o.append(4)
                    elif i[2]==5:
                        bt_5.config(text='o',state='disabled')
                        o.append(5)
                    elif i[2]==6:
                        bt_6.config(text='o',state='disabled')
                        o.append(6)
                    elif i[2]==7:
                        bt_7.config(text='o',state='disabled')
                        o.append(7)
                    elif i[2]==8:
                        bt_8.config(text='o',state='disabled')
                        o.append(8)
                    elif i[2]==9:
                        bt_9.config(text='o',state='disabled')
                        o.append(9)
        else:
            while loop_2==True:
                loop_2=False
                random=r.choice([1,2,3,4,5,6,7,8,9])
                if random not in o and random not in x:
                    if random==1:
                        bt_1.config(text='o',state='disabled')
                        o.append(1)
                    elif random==2:
                        bt_2.config(text='o',state='disabled')
                        o.append(2)
                    elif random==3:
                        bt_3.config(text='o',state='disabled')
                        o.append(3)
                    elif random==4:
                        bt_4.config(text='o',state='disabled')
                        o.append(4)
                    elif random==5:
                        bt_5.config(text='o',state='disabled')
                        o.append(5)
                    elif random==6:
                        bt_6.config(text='o',state='disabled')
                        o.append(6)
                    elif random==7:
                        bt_7.config(text='o',state='disabled')
                        o.append(7)
                    elif random==8:
                        bt_8.config(text='o',state='disabled')
                        o.append(8)
                    elif random==9:
                        bt_9.config(text='o',state='disabled')
                        o.append(9)
                else:loop_2=True
        loop_2=True

    def game_loop():
            place_x()
            chek_x()
            place_o()
            chek_o()
            if len(x)+len(o)==9:
                game_win.destroy()
                draw=tk.Toplevel(main_win)
                draw.title('game over')
                draw.geometry('300x150+550+230')
                draw.config(bg='lightgrey')
                win_lb=tk.Label(draw,fg='white',bg='grey',text='draw',width=14)
                win_lb.place(relx=0.5,rely=0.2,anchor='center')
    
def stat():
    ##search
    def search():
        name_2=name.get()
        stat=tk.Toplevel(stats)
        stat.geometry('500x250+440+230')
        stat.config(bg='lightgrey')
        stat.title(f'stat of {name_2}')
        close_2=tk.Button(stat,width='14',bg='red',fg='white',font='arial,15',text='close',command=stat.destroy)
        close_2.place(relx=0.5,rely=0.7,anchor='center')
        

    stats=tk.Toplevel(main_win)
    stats.title('tick tac toe-stats')
    stats.geometry('500x250+440+230')
    stats.config(bg='lightgrey')
    name=tk.Entry(stats,fg='black',width=26,font='arial,15')
    name_txt=tk.Label(stats,bg='grey',fg='white',font='arial,15',text='Name:')
    search=tk.Button(stats,bg='grey',fg='white',font='arial,15',text='search',command=search)
    close=tk.Button(stats,width='14',bg='red',fg='white',font='arial,15',text='close',command=stats.destroy)
    name_txt.place(relx=0.2,rely=0.3,anchor='center')
    name.place(relx=0.5,rely=0.3,anchor='center')
    search.place(relx=0.81,rely=0.3,anchor='center')
    close.place(relx=0.5,rely=0.7,anchor='center')
##main_window
main_win=tk.Tk()
main_win.config(bg='lightgrey')
main_win.geometry('1366x705+0+0')
main_win.title('tick tac toe')
play_bt=tk.Button(main_win,text='play',fg='white',bg='grey',width='30',height='2',command=login)
menu_bt=tk.Button(main_win,text='stats',fg='white',bg='grey',width='15',height='2',command=stat)
quit_bt=tk.Button(main_win,text='quit',fg='white',bg='grey',width='13',height='2',command=main_win.destroy)
play_bt.place(relx=0.5,y=450,anchor='center')
menu_bt.place(x=629,y=500,anchor='center')
quit_bt.place(x=742,y=500,anchor='center')
main_win.mainloop()


