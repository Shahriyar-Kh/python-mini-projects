from tkinter import *
from PIL import Image,ImageTk
from random import randint

#Step1 Create the window
root=Tk()
root.title("Rock Paper Scissor Game")
root.configure(background="Black")

#Step2 upload picture
user_rock=ImageTk.PhotoImage(Image.open(r"Rock_Paper_Scissor_Game\Rock_user.png"))
user_paper=ImageTk.PhotoImage(Image.open(r"Rock_Paper_Scissor_Game\Paper_user.png"))
user_scissor=ImageTk.PhotoImage(Image.open(r"Rock_Paper_Scissor_Game\Scissor_user.png"))
comp_rock=ImageTk.PhotoImage(Image.open(r"Rock_Paper_Scissor_Game\Rock_comp.png"))
comp_paper=ImageTk.PhotoImage(Image.open(r"Rock_Paper_Scissor_Game\Paper_comp.png"))
comp_scissor=ImageTk.PhotoImage(Image.open(r"Rock_Paper_Scissor_Game\Scissor_comp.png"))

#User and computer indicator
Label(root,text="USER",font="Halvetica 14",bg="Black",fg="White").grid(row=0,column=3)
Label(root,text="COMPUTER",font="Halvetica 14",bg="Black",fg="White").grid(row=0,column=1)

#Step4 insert picture
user_lbl=Label(root,image=user_rock,bg="Black")
user_lbl.grid(row=1,column=4)
comp_lbl=Label(root,image=comp_rock,bg="Black")
comp_lbl.grid(row=1,column=0)

#Step 5 Score Labels
u_score=Label(root,text=0,font=100,bg="black",fg="White")
u_score.grid(row=1,column=3)
c_score=Label(root,text=0,font=100,bg="black",fg="White")
c_score.grid(row=1,column=1)


#Step 6 buttons
btn_rock=Button(root,text="Rock",font="Lucida 15",bg="#e67e22",fg="Black",width=15,command=lambda:updateChoice("rock"))
btn_rock.grid(row=2,column=1)
btn_paper=Button(root,text="Paper",font="Lucida 15",bg="#9b59b6",fg="Black",width=15,command=lambda:updateChoice("paper"))
btn_paper.grid(row=2,column=2)
btn_scissor=Button(root,text="Scissor",font="Lucida 15",bg="#ff1493",fg="Black",width=15,command=lambda:updateChoice("scissor"))
btn_scissor.grid(row=2,column=3)

#step 7 Message
msg=Label(root,font=60,bg="Black",fg="Blue",pady=20)
msg.grid(row=3,column=2)

choices=["rock","paper","scissor"]
#step 8 update choice function
def updateChoice(pressed):
    #for computer
    comp_choice=choices[randint(0,2)]
    if comp_choice=="rock":
        comp_lbl.configure(image=comp_rock)
    elif comp_choice=="paper":
        comp_lbl.configure(image=comp_paper)
    else:
        comp_lbl.configure(image=comp_scissor)

    #for user 
    if pressed=="rock":
        user_lbl.configure(image=user_rock)
    elif pressed=="paper":
        user_lbl.configure(image=user_paper)
    else:
        user_lbl.configure(image=user_scissor)
    checkWinner(pressed,comp_choice)
#update the message when the winner function send
def updateMessage(coming_msg):
    msg["text"]=coming_msg

#update the user score when the user when
def userScoreUpdate():
    score=int(u_score["text"])
    score+=1
    u_score["text"]=str(score)
#update the computer score when comp is winner
def compScoreUpdate():
    score=int(c_score["text"])
    score+=1
    c_score["text"]=str(score)

def checkWinner(palyer,computer):
    if palyer==computer:
        updateMessage("Its a Tie!!!")
    elif palyer=="rock":
        if computer=="paper":
            updateMessage("You Loose")
            compScoreUpdate()
        else:
            updateMessage("Congratulation You Win")
            userScoreUpdate()
    elif palyer=="paper":
        if computer=="scissor":
            updateMessage("You Loose")
            compScoreUpdate()
        else:
            updateMessage("Congratulation You Win")
            userScoreUpdate()
    elif palyer=="scissor":
        if computer=="rock":
            updateMessage("You Loose")
            compScoreUpdate()
        else:
            updateMessage("Congratulation You Win")
            userScoreUpdate()
    else:
        pass

root.mainloop()
