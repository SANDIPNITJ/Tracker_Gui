from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Registered Now')
root.iconbitmap('logo.png')

root.geometry('350x500')
root.configure(background='#0096DC') 
img=Image.open('logo.png')
resized_img =img.resize((70,70))
img=ImageTk.PhotoImage(resized_img) 
img_label = Label(root,image=img,justify='left') 
img_label.pack(pady=(100,20))
text_label = Label(root,text='Q-DESK',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',50))
email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',14))
email_input=Entry(root,width=50)
email_input.pack(ipady=7,pady=(1,16))

Password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
Password_label.pack(pady=(20,5))
Password_label.config(font=('verdana',14))
Password_input=Entry(root,width=50)
Password_input.pack(ipady=7,pady=(1,16))

login_btn= Button(root,text='Login Here',bg='white',fg='black',width=9,height=1)
login_btn.config(font=('verdana',14))
login_btn.pack(pady=(10,5))
root.mainloop()
