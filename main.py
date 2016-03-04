from Tkinter import*
import tkMessageBox

#sys and os modules have been imported since they are used to restart the program if the user wishes to play again
import sys 
import os


count=0 #count variable used to count click on buttons if buttons have been clicked 9 times and even then here is no winner then there is a tie
bclick=True #a boolean variable used to assign text to the buttons alternately 
r=Tk()#Used to generate the splash screen
def fun():
    r.destroy() # SplashScreen window destroyed
    root=Tk()# Game window created
    root.title("2-PLAYER TIC TAC TOE") #assigned title to Game Window
  
    
    title="WINNER"
    title_draw="Draw"
    #String Variables used in displaying Message(Winner)
    message_draw="Its a Draw!\nPlay Again?"
    message_x="PLAYER X WON THE GAME!\nPlay Again?"
    message_o="PLAYER O WON THE GAME!\nPlay Again?"
    #String Variables used in Message BOX

    def tictactoe(buttons):#Function created which is called whenever the button is pressed
        global bclick
        global count
    
        if count==9:
            if tkMessageBox.askyesno(title_draw,message_draw): #User Prompted TO Play Game Again With YES/NO proceedings
                os.execl(sys.executable, sys.executable, *sys.argv)#IF Condition true The Whole Program Restarts
            else:
                quit()#IF conditions is FALSE Programe/Game quits at that moment

          
        elif(button1.cget("text")== "O" and button2.cget("text")=="O" and button3.cget("text")=="O" or
            button4.cget("text")== "O" and button5.cget("text")=="O" and button6.cget("text")=="O" or
            button7.cget("text")== "O" and button8.cget("text")=="O" and button9.cget("text")=="O" or
            button3.cget("text")== "O" and button5.cget("text")=="O" and button7.cget("text")=="O" or
            button1.cget("text")== "O" and button5.cget("text")=="O" and button9.cget("text")=="O" or
            button1.cget("text")== "O" and button4.cget("text")=="O" and button7.cget("text")=="O" or
            button2.cget("text")== "O" and button5.cget("text")=="O" and button8.cget("text")=="O" or
            button3.cget("text")== "O" and button6.cget("text")=="O" and button9.cget("text")=="O"):
            root.bell()#Bell tune and user O is promped if condition is true
            if tkMessageBox.askyesno(title,message_o):#Message displaying user O won the game
                os.execl(sys.executable, sys.executable, *sys.argv)#Program restarts if user wishes to Play Game Again
            else:
                quit()#Game quits if user Selects No when prompted on playing Again

                '''Conditions OF TIC TAC TOE GAME ie when either buttons 1,2,3 or 4,5,6 or 7,8,9 or 3,5,7 or 1,5,9 or 1,4,7 or 2,5,8 or 3,6,9 have text=O then
                the Player O wins the Game and the user is prompted TO Play further if he wishes
                        Buttons Layout
                           1|2|3
                           4|5|6
                           7|8|9'''  

        elif(button1.cget("text")== "X" and button2.cget("text")=="X" and button3.cget("text")=="X" or
            button4.cget("text")== "X" and button5.cget("text")=="X" and button6.cget("text")=="X" or
            button7.cget("text")== "X" and button8.cget("text")=="X" and button9.cget("text")=="X" or
            button3.cget("text")== "X" and button5.cget("text")=="X" and button7.cget("text")=="X" or
            button1.cget("text")== "X" and button5.cget("text")=="X" and button9.cget("text")=="X" or
            button1.cget("text")== "X" and button4.cget("text")=="X" and button7.cget("text")=="X" or
            button2.cget("text")== "X" and button5.cget("text")=="X" and button8.cget("text")=="X" or
            button3.cget("text")== "X" and button6.cget("text")=="X" and button9.cget("text")=="X"):
            root.bell()#Bell tune and user X is promped if condition is true
            if tkMessageBox.askyesno(title,message_x):#Message displaying user X won the game
                os.execl(sys.executable, sys.executable, *sys.argv)#Program restarts if user wishes to Play Game Again
            else:
                quit()#Game quits if user Selects No when prompted on playing Again
            
        elif buttons["text"]==" " and  bclick==True:#Null Buttons which are assigned text alternately
            buttons["text"]="X"#X assigned to the text part of button
            buttons["fg"]="WHITE"
            buttons["bg"]="RED"
            bclick=False#Assigned False so that next time the below condition is true and O is assigned to the Button
            
        elif buttons["text"]==" " and bclick==False:
            buttons["text"]="O"#O assigned to the text part of button
            buttons["fg"]="WHITE"
            buttons["bg"]="ROYAL BLUE"
       
            bclick=True#Assigned True so that next time the Above condition is true and X is assigned to the Button

            '''The Buttons are assigned Foreground and Background Colours according to the Conditions'''
        count=count+1
        

    #Buttons Created with No text initially
    button1=Button(root,text=" ",bg="white",font=('Helvetica 30 '),height=2,width=4,command=lambda:tictactoe(button1))
    button1.grid(row=1,column=0,sticky=S+N+E+W)


    button2=Button(root,text=" ",font=('Helvetica 30'),bg="white",height=2,width=4,command=lambda:tictactoe(button2))
    button2.grid(row=1,column=1,sticky=S+N+E+W)


    button3=Button(root,text=" ",font=('Helvetica 30'),height=2,bg="white",width=4,command=lambda:tictactoe(button3))
    button3.grid(row=1,column=2,sticky=S+N+E+W)


    button4=Button(root,text=" ",font=('Helvetica 30'),height=2,width=4,bg="white",command=lambda:tictactoe(button4))
    button4.grid(row=2,column=0,sticky=S+N+E+W)

    button5=Button(root,text=" ",font=('Helvetica 30'),height=2,width=4,bg="white",command=lambda:tictactoe(button5))
    button5.grid(row=2,column=1,sticky=S+N+E+W)

    button6=Button(root,text=" ",font=('Helvetica 30'),bg="white",height=2,width=4,command=lambda:tictactoe(button6))
    button6.grid(row=2,column=2,sticky=S+N+E+W)


    button7=Button(root,text=" ",font=('Helvetica 30'),height=2,bg="white",width=4,command=lambda:tictactoe(button7))
    button7.grid(row=3,column=0,sticky=S+N+E+W)

    button8=Button(root,text=" ",font=('Helvetica 30'),height=2,width=4,bg="white",command=lambda:tictactoe(button8))
    button8.grid(row=3,column=1,sticky=S+N+E+W)


    button9=Button(root,text=" ",font=('Helvetica 30'),height=2,bg="white",width=4,command=lambda:tictactoe(button9))
    button9.grid(row=3,column=2,sticky=S+N+E+W)

    root.mainloop()

a=PhotoImage(file="image.gif") #SplashScreen GIF image
lb=Label(r,image=a,compound="center",text="")
lb.after(5000,fun)#Timebound of 5ms
lb.grid()
r.mainloop()
