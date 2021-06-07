from tkinter import *
from tkinter import messagebox
global root
global root1

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  '''   

def Login_page():
    #methods
    def Login():
      
        uname=e1.get()
        password=e2.get()

        
        
        if (uname =='abcd' and password =='1234' ):
            messagebox.showinfo("Login","Login Success")
        else:
            messagebox.showinfo('','please enter valid username and password')
    

    #def Forgotpassword():
       #  messagebox.showinfo('forgot password','your password is :12345')
    def go_to_createaccount():
        root.destroy()
        create_new_account()


#______________________________________

#LOGIN PAGE
   
    root=Tk()
    root.title("USER LOGIN ")
    root.geometry('600x300')
    global e1
    global e2
  
    e1=StringVar()
    e2=StringVar()


    #labels
    bg=PhotoImage( file="F:/Sample-png-image-1mb1.png")

    label_image=Label(root,image=bg)
    label_image.pack()

    Label(root,text='login or signup',bg='white',fg='black',font=("Times new Roman",20)).place(x=210,y=10)
    Label(root,text='username or email',fg='black',font=('',10)).place(x=240,y=90)
    Label(root,text='password',fg='black',font=('',10)).place(x=240,y=150)

    num1=Entry(root,width=20,textvariable=e1).place(x=240,y=120)
    num2=Entry(root,width=20,show="*",textvariable=e2).place(x=240,y=180)



    #buttons


    LB=Button(root,text='Login', command =Login,bg='orange',fg='white',font=("Times new Roman",12)).place(x=270,y=200)

    #Button(root,text='Forgot Password',command=Forgotpassword,font=("Times new Roman",9),fg='white',bg='red').place(x=245,y=240)
    Button(root,text='create new account',command=go_to_createaccount,bg='light green').place(x=300,y=250)
    


    root.mainloop()



'''________________________________________
_________________________________________

'''

def create_new_account():
    
    def create_account():

        user_name=name.get()
        pass_word=Password.get()
        confirm_password=confirmpass.get()
        user_mail=email.get()

        if (len(user_name)==0 or len(pass_word)==0 or len(confirm_password)==0 or len(user_mail)==0 ):
            
            messagebox.showinfo('create new account','please enter your details')
            
        else:
            if (pass_word != confirm_password):
                messagebox.showinfo('confirm password','passwords not matched, please re-enter confirm password')
           
            else:
                messagebox.showinfo("create new account",'Your Account Created Successfully')
                root1.destroy()
                Login_page()
                
            
            
    def go_to_login():
        root1.destroy()
        Login_page()


#________________________________________

        
    root1=Tk()
    root1.title('create new account')
    root1.geometry('600x300')

    name=StringVar()
    email=StringVar()
    Password=StringVar()
    confirmpass=StringVar()

    bg=PhotoImage( file="F:/Sample-png-image-1mb1.png")

    label_image=Label(root1,image=bg)
    label_image.pack()


    lablename=Label(root1,text="Enter your name").place(x=180,y=90)

    entryname=Entry(root1,textvariable=name).place(x=300,y=90)

    lablepass=Label(root1,text="password").place(x=180,y=130)

    entrypass=Entry(root1,show="*",textvariable=Password).place(x=300,y=130)

    lablecpass=Label(root1,text="confirm password").place(x=180,y=170)

    entrycpass=Entry(root1,show="*",textvariable=confirmpass).place(x=300,y=170)

    lableemail=Label(root1,text="Enter mail").place(x=180,y=210)

    entryemail=Entry(root1,textvariable=email).place(x=300,y=210)


    #button

    Button(root1,text='Create Account', command=create_account,bg='blue').place(x=310,y=240)


    Button(root1,text='already have an account',command=go_to_login,bg='yellow').place(x=310,y=270)
    
    


    root1.mainloop()
create_new_account()
