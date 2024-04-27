'''
I Learnt tkinter today actually in like 2 hours 
everything else like setting up the root window mainlooping it 
creating canvas,title,and shapes and text and importing image were done by me with all that i learned in two hours 
but the values like the coordinates or height and width and shit were taken i am just too lazy uk



alryty guys there was a stupid error of moon where it became way too big to handle and yea it was pretty messed up so 
i had to remove the moon but it is still commented and when i actually find the moon that actually fits it we can do it 
'''
from tkinter import *
from tkinter import font
root=Tk()
root.title("Project 1")
c=Canvas(root,bg='black',width=1200,height=700)
id=c.create_polygon(600,250,700,200,800,250,800,400,600,400,width=2,fill="yellow",outline="red")
id=c.create_line(600,250,800,250,width=2,fill="red")
id=c.create_rectangle(650,275,750,375,fill="red")
x1,y1=0,350
x2,y2=200,450
for i in range(3):
    c.create_arc(x1,y1,x2,y2,start=0,extent=180,fill="Green")
    x1+=200
    x2+=200
c.create_arc(800,350,1000,450,start=0,extent=180,fill="green")
c.create_arc(1000,350,1200,450,start=0,extent=180,fill="green")
# file1=PhotoImage(file="Full_moon.png")
# id=c.create_image(1,1,anchor=NW,image=file1)
id=c.create_text(600,600,text="Yay!! I made my first GUI",fill="magenta",font=('helevetica',30,'underline'),activefill="white")
c.pack()
root.mainloop()
