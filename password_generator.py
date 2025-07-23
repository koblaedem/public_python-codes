#date:27/11/24
#author:security eng Edem Adeti
#Aim: this program is aimed at: 1. Generating Random Passwords using ascii characters. [~]
                            #   2. Allow user copy the passwords.[ ]
                            #   3. Store passwords list on the users machine.[ ]

from tkinter import *
#from tkinter import PhotoImage
main=Tk()


#random characters libary
import random
import string


#functions and buttons
def random_strings(lenght):
    characters=string.ascii_letters + string.digits + '!@$^&#)*(%?>"<,"='
    return ''.join(random.choice(characters)for _ in range(lenght))

def generator():
    try:
        lenght=int(p_value.get())
        if lenght <=0:
            raise ValueError
        result = random_strings(lenght)
        result_display.config(text=result)
        copy_button.config(state=NORMAL)
    except ValueError:
        result_display.config(text='Positive Integer Vaules Only! eg: 1,3,2,8')



#copy password
def clipboard():
    main.clipboard_clear()
    main.clipboard_append(result_display.cget('text'))
    #copy_display.config(text='Password copied successfully',foreground='green')

#copy button
copy_button=Button(main, text='copy password' , command=clipboard,state=DISABLED)
#clear button
def clear():
   p_value.delete(0,'end') #fix bug 23/07/2025
erase=Button(main,text='Clear',command=clear)


#exit program button
end = Button(main, text='Exit', command=main.destroy)

#generate button
final=Button(main,text='Generate',command = generator)

#copyright message
copyright_display=Label(main,text='© 2024 _theanalyst200.All rights reserved',font=('Arial',10))

main.resizable(False,False)
main.title('Password Generator v0.1')
main.geometry('400x230')


#user input box
p_lenght=Label(main,text=' Please enter your perferred password lenght ')
p_value=Entry(main,width=4,justify='center')


#default mesage desplayed awaiting users input
result_display=Label(main,text='Pending your desired lenght.....')

#display
p_lenght.pack(pady=(5,5))
p_value.pack(pady=(10,0))
result_display.pack(pady=(20,0))
final.pack(pady=(13,0))
copy_button.pack(pady=(6,3))
#final.pack(side='left',padx=(10,10))
erase.pack(side='right',padx=(10,10))
end.pack(side='left',padx=(10,10))
#end.pack(pady=(13,0))
copyright_display.pack(side='bottom')
p_value.focus_set()


