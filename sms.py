from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas


#Font 
f = ('times new roman',18,'bold')

#Functionality Part

def screen_data():
    global screen_window
    screen_window = Toplevel()
    screen_window.title()
    screen_window.resizable(0,0)
    screen_window.grab_set()

    f = ('times new roman',18)
    fe = ('times new roman',15)

    global idEntry,nameEntry,phoneEntry,emailEntry,addressEntry,genEntry,dobEntry

    idLable = Label(screen_window,text='Id',font=f)
    idLable.grid(row=0,column=0,padx=15,pady=10,sticky=W)
    idEntry = Entry(screen_window,font=fe,foreground='brown4',border=3)
    idEntry.grid(row=0,column=1,pady=10)

    nameLable = Label(screen_window,text='Name',font=f)
    nameLable.grid(row=1,column=0,padx=15,pady=10,sticky=W)
    nameEntry = Entry(screen_window,font=fe,foreground='brown4',border=3)
    nameEntry.grid(row=1,column=1,pady=10)

    phoneLable = Label(screen_window,text='Phone',font=f)
    phoneLable.grid(row=2,column=0,padx=15,pady=10,sticky=W)
    phoneEntry = Entry(screen_window,font=fe,foreground='brown4',border=3)
    phoneEntry.grid(row=2,column=1,pady=10)

    emailLable = Label(screen_window,text='Email',font=f)
    emailLable.grid(row=3,column=0,padx=15,pady=10,sticky=W)
    emailEntry = Entry(screen_window,font=fe,foreground='brown4',border=3)
    emailEntry.grid(row=3,column=1,pady=10)

    addressLable = Label(screen_window,text='Address',font=f)
    addressLable.grid(row=4,column=0,padx=15,pady=10,sticky=W)
    addressEntry = Entry(screen_window,font=fe,foreground='brown4',border=3)
    addressEntry.grid(row=4,column=1,pady=10)

    genLable = Label(screen_window,text='Gender',font=f)
    genLable.grid(row=5,column=0,padx=15,pady=10,sticky=W)
    genEntry = Entry(screen_window,font=fe,foreground='brown4',border=3)
    genEntry.grid(row=5,column=1,pady=10)

    dobLable = Label(screen_window,text='D.O.B',font=f)
    dobLable.grid(row=6,column=0,padx=15,pady=10,sticky=W)
    dobEntry = Entry(screen_window,font=fe,foreground='brown4',border=3)
    dobEntry.grid(row=6,column=1,pady=10)


#Exporting Data
def export_data():
    newlist = []
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studentTable.get_children()
    for index in indexing:
        content = studentTable.item(index)
        details = content['values']
        newlist.append(details)

    table = pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'])  
    table.to_csv(url,index=FALSE)
    messagebox.showinfo('Seccess','Data is save succesfully')

#Exit    
def iexit():
    result = messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()





#Update Data
def update_student():
    def update_data():
        
        q = 'update student set name = %s, mobile = %s, email = %s, address = %s, gen = %s, dob = %s, date = %s, time = %s where id = %s'
        mycursor.execute(q,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genEntry.get(),dobEntry.get(),date,curtime,idEntry.get()))
        con.commit()
        
        messagebox.showinfo('Success',f'Id {idEntry.get()} is Modified successfully',parent = screen_window)
        screen_window.destroy()
        show_student()

        
    screen_data()
    update_student_Button = ttk.Button(screen_window,text='UPDATE',command=update_data)
    update_student_Button.grid(row=7,columnspan=2,pady=20)

    indexing = studentTable.focus()
   
    content = studentTable.item(indexing)

    listdata = content['values']

    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    phoneEntry.insert(0,listdata[2])
    emailEntry.insert(0,listdata[3])
    addressEntry.insert(0,listdata[4])
    genEntry.insert(0,listdata[5])
    dobEntry.insert(0,listdata[6])
    



#Fetch all student info
def show_student():
    q = 'select * from student'
    mycursor.execute(q)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
    



#Delete stident
def delete_student():
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    q = 'delete from student where id =%s'
    mycursor.execute(q,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    q = 'select * from student'
    mycursor.execute(q)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
    
    

#Search student from database
def search_student():
    screen_data()
    def search_data():
        
        q = 'select * from student where id = %s or name = %s or email = %s or mobile = %s or address = %s or gen = %s or dob = %s'
        mycursor.execute(q,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)
        
        

    search_student_Button = ttk.Button(screen_window,text='SEARCH',command=search_data)
    search_student_Button.grid(row=7,columnspan=2,pady=20)    
    

#Add student into database
def add_student():
    def add_data():
        if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or emailEntry.get() == ''or dobEntry.get() == '' or genEntry.get() == '' or addressEntry.get() == '':
            messagebox.showerror('Error','All Fields Are Required',parent = screen_window)
        else:
            try:
                    
                q = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(q,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genEntry.get(),dobEntry.get(),date,curtime))
                con.commit()
                result =messagebox.askyesno('Confirm','Data Added Successfully. Do you want to clear the form ?',parent = screen_window)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genEntry.delete(0,END)
                    dobEntry.delete(0,END)
            except:

                messagebox.showerror('Error','Id should be UNIQUE',parent = screen_window)

                return
            
            q = 'select * from student'
            mycursor.execute(q)

            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())

            for data in fetched_data: 
                studentTable.insert('',END,values=data)              
                    
    
    screen_data()
    add_student_Button = ttk.Button(screen_window,text='ADD',command=add_data)
    add_student_Button.grid(row=7,columnspan=2,pady=20)


#Displaying Time
def clock(): 
    global date,curtime
    date = time.strftime('%d/%m/%Y')
    curtime = time.strftime('%H:%H:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {curtime}')
    datetimeLabel.after(1000,clock)

#DataBase confuguration
def connect_database():
    #function to connect to DataBase
    def connect():
        global mycursor,con
        try:
            f = ('times new roman',18,'bold')
            con = pymysql.connect(host=hostnameEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor = con.cursor()

        except:
            messagebox.showerror('Login Filed','Ivalid Details',parent =connectwindow)
            return False
        try:
            query =  'create database studentmanagementsystem;' 
            mycursor.execute(query) 

            query='use studentmanagementsystem;'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gen varchar(20),dob varchar(20),date varchar(50),time varchar(50));'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem;'
            mycursor.execute(query)
        messagebox.showinfo('Login Success','DataBase Connection Is Succesful',parent =connectwindow)

        #Enabled the button to access
        addstudentButton.config(state=NORMAL,command=add_student)
        searchtudentButton.config(state=NORMAL,command=search_student)
        updatestudentButton.config(state=NORMAL,command=update_student)
        showstudentButton.config(state=NORMAL,command=show_student)
        expordataButton.config(state=NORMAL,command=export_data)
        deletestudentButton.config(state=NORMAL,command=delete_student)

    #GUI for connectivity of DataBase
    connectwindow = Toplevel()
    connectwindow.geometry('470x240+730+230')
    connectwindow.resizable(0,0)
    connectwindow.title('DataBase Connectivity')
    connectwindow.grab_set()

    hostnameLabel = Label(connectwindow,text=' Host Name',font=('times new roman',18,),padx=10)
    hostnameLabel.grid(row=0,column=0)
    hostnameEntry = Entry(connectwindow,font=('times new roman',18,),border=4,foreground='royalblue')
    hostnameEntry.grid(row=0,column=1,padx=15,pady=10)

    usernameLabel = Label(connectwindow,text=' User Name',font=('times new roman',18,),padx=10)
    usernameLabel.grid(row=1,column=0)
    usernameEntry = Entry(connectwindow,font=('times new roman',18,),border=4,foreground='royalblue')
    usernameEntry.grid(row=1,column=1,padx=15,pady=10)

    passwordLabel = Label(connectwindow,text='Password',font=('times new roman',18,),padx=5)
    passwordLabel.grid(row=2,column=0)
    passwordEntry = Entry(connectwindow,font=('times new roman',18,),border=4,foreground='royalblue')
    passwordEntry.grid(row=2,column=1,padx=15,pady=10)

    connectButton = ttk.Button(connectwindow,text="CONNECT",command=connect)
    connectButton.grid(row=3,columnspan=2,pady=20)

count = 0
text = ''
def slider(): #For slider
    global text,count
    
    text = text+s[count]
    sliderLabel.config(text=text)
    sliderLabel.after(290,slider)
    count = count + 1
    if count > len(s) -1:
        count = 0
        text = ''


#This is the main wWindow
root = ttkthemes.ThemedTk()
#Applying Themes To Button ---- Using Radiance Theme
root.get_themes()
root.set_theme('radiance')

root.title('Student Managemeny System')
root.geometry('1174x680+0+0')
root.resizable(0,0)
    
#Label Of Date And Time
datetimeLabel = Label(root,font=f,foreground='Dodgerblue4')
datetimeLabel.place(x=5,y=5)  
clock()

#Slider Of Student Management System
s = 'Student Management System'
sliderLabel = Label(root,font =('times new roman',25,'bold'),width=30,foreground='Dodgerblue4')
sliderLabel.place(x=290,y=0)
slider()

connectButton = ttk.Button(root,text='Connect DataBase',command=connect_database)
connectButton.place(x=980,y=0)

#Making left FRAME
leftFrame = Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image = PhotoImage(file='students.png')
logo_Label = Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

#Buttons
addstudentButton = ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED)
addstudentButton.grid(row=1,column=0,pady=20)

searchtudentButton = ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED)
searchtudentButton.grid(row=2,column=0,pady=20)

deletestudentButton = ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED)
deletestudentButton.grid(row=4,column=0,pady=20)

updatestudentButton = ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED)
updatestudentButton.grid(row=5,column=0,pady=20)

showstudentButton = ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED)
showstudentButton.grid(row=6,column=0,pady=20)

expordataButton = ttk.Button(leftFrame,text='Export Data',width=25,state=DISABLED)
expordataButton.grid(row=7,column=0,pady=20)

exitButton = ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=8,column=0,pady=20)

#Making rifgt FRAME
rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)



#Scrool Bar
scrollbarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY = Scrollbar(rightFrame,orient=VERTICAL)


#Treeview For Presenation
studentTable = ttk.Treeview(rightFrame,columns=('Id','Name','Mob No','Email','Address','Gender','D.O.B','Added Date','Added Time')
                            ,xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
                            
scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.config(show='headings')

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mob No',text='Mob No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=60,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=150,anchor=CENTER)
studentTable.column('D.O.B',width=150,anchor=CENTER)
studentTable.column('Added Date',width=150,anchor=CENTER)
studentTable.column('Added Time',width=150,anchor=CENTER)
studentTable.column('Mob No',width=200,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight = 35,font =('arial',13),foreground = 'snow',background = 'gray65',fieldbackground = 'gray70')
style.configure('Treeview.Heading',font =('times new roman',14,'bold'),foreground = 'gray30')

root.mainloop()