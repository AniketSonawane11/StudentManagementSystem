from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameentry.get() =='' or userpsswordentry.get() == '':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameentry.get() == 'Aniket' and userpsswordentry.get() == '1234':
        messagebox.showinfo('Success','Login Successful')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error','Invalid details')

#Main window
window = Tk()

window.geometry('1200x700+0+0')
window.title("Login System Of Student Mangement System")
window.resizable(0,0)

#Font
f = ('times new roman',18,'bold')
    
#Backgrpund Window  
backgroundImage = ImageTk.PhotoImage(file = 'bg.jpg')
bg_Label = Label(window,image=backgroundImage)
bg_Label.place(x=0,y=0)

#Login Frame
login_frame = Frame(window,background='white')
login_frame.place(x=400,y=150)

stuLogoImg= PhotoImage(file='student.png')

stulogolagel = Label(login_frame,image=stuLogoImg,background='white')
stulogolagel.grid(row=0,column=0,columnspan=2)

#LOginUsername
usernameImg = PhotoImage(file='user.png')
usernamelabel = Label(login_frame,image=usernameImg,text='Username',compound=LEFT,font=f,background='white')
usernamelabel.grid(row=1,column=0,pady=10)

usernameentry = Entry(login_frame,font=f,border=4,fg='royalblue')
usernameentry.grid(row=1,column=1,padx=15,pady=10)

#LoginPass
userpasswordImg = PhotoImage(file='pass.png')
userpsswordlabel = Label(login_frame,image=userpasswordImg,text='Password',compound=LEFT,font=f,background='white')
userpsswordlabel.grid(row=2,column=0,pady=10)

userpsswordentry = Entry(login_frame,font=f,border=4,fg='royalblue')
userpsswordentry.grid(row=2,column=1,padx=15)

#LoginButton
loginbutton = Button(login_frame,text='Login',font=('times new roman',14,'bold'),width=15,background='cornflowerblue',
              foreground='white',activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=login)
loginbutton.grid(row=3,column=1)

window.mainloop()