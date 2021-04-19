import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk1
from PIL import ImageTk,Image
from tkinter import filedialog


def browsefunc():

    root = tk1.ThemedTk()
    root.geometry('500x250')
    root.title("Result | Twitter Sentiment Analysis")
    root.iconbitmap('tweet-logo-real-ico.ico')
    root.get_themes()
    root.set_theme('equilux')
    root.resizable(0, 0)
    answer = tk.Text(root, width=55, height=15)

    answer.pack()

    root.configure(background="SeaGreen2")
    filename = filedialog.askopenfilename()
    pathlabel = tk.Label(text=filename)
    pathlabel.pack()
    print(filename)
    print(type(filename))
    with open(filename, mode='r') as f2:
        Input = f2.read()

    print(Input)




    # -> Write your all Logic Here For Analysis In Input there is file content in string format






    # -> when classification done write if else code block like below...

    '''
    if(ans==0):
        My_Ans = "Tweet belongs to Humor Class!"  # -> Change this My_Ans to result 
    elif(ans==1):
        My_Ans = "Tweet belongs to Angry Class!"  # -> Change this My_Ans to result 
    elif(ans==2):
        My_Ans = "Tweet belongs to Sad Class!"  # -> Change this My_Ans to result 
     else:
        ..........   
    '''



    My_Ans = "Tweet belongs to Humor Class!" # -> Change this My_Ans to result

    answer.config(state='normal')
    answer.delete(1.0, tk.END)
    answer.insert(tk.INSERT, My_Ans)
    answer.config(state='disabled')

    root.mainloop()





root=tk1.ThemedTk()
root.geometry('1000x500')
root.title("Twitter Sentiment Analysis")
root.iconbitmap('tweet-logo-real-ico.ico')
root.get_themes()
root.set_theme('equilux')
root.resizable(0,0)

canvas=Canvas(root,width=1000,height=500)
image=ImageTk.PhotoImage(Image.open('bck.png'))  # -> Put Your Image Path Here..
img=canvas.create_image(0,0,anchor=NW,image=image)


w=ttk.Label(canvas,text="Twitter Sentiment Analysis",image=image,font='Helvetica 50 bold',foreground='black',compound='center')

button2 = ttk.Button(canvas, text="Browse-Tweets-Text-File",command=browsefunc)
button2.pack(in_=canvas,side=BOTTOM)
w.pack()
canvas.pack()


root.mainloop()