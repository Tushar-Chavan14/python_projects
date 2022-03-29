from tkinter import *
import wikipedia
from PIL import Image, ImageTk
import pywhatkit as kit
import wheater
root = Tk()

adm_cret = {"Uniform fee":"3500 per boy & 3800 per girl (2 pairs)", "Hostel fee":"52500 for both boys and girls","Admission processing fee":"1000", "Van fees":{"within ring road":"1000","outside the ringroad":"1200"}}

administrotion = {"secretary":"Shri.Basavaraj Deshmuk \n Cell:1234567890", "vice chancellor":"Dr.Niranjan Nisty \n Cell:1234567890","pro vice chancellor":"Dr.V.D. Mytri \n Cell:1234567890" ,"registrar":"Dr.Anilkumar.G.Bidve \n Cell:1234567890","registrar evaluation":"Dr.Lingraj Shastri \n Cell:1234567890","dean":"Dr.Lakxmi.B.Patil \n Cell:1234567890 \n Dr.Basvaraj S Mathpati \n Cell:1234567890"}

courses={"eng":["mechanical","civil","computer science","electoncis"]}

def clear() :
    a.delete(0, END)
def send():
    command = a.get()
    
    send="you:"+command
    text.insert(END, "\n"+send)
    if (command=='hi'):
        text.insert(END, "\n"+ "bot: hello! Welcome to Sharanbasva University how may I help  you")
    elif (command=='hello'):
        text.insert(END, "\n"+ "bot: hi")
    elif ('how' in command):
        text.insert(END, "\n"+ "bot: I am fine. How are you")
    elif (command=='i am fine'):
        text.insert(END, "\n"+ "bot: Nice to hear that")
    elif ('say something about ' in command):
        command = command.replace('say something about ','')
        text.insert(END, "\n"+ "bot: Ok")
        text.insert(END,"\n"+wikipedia.summary(command,sentences=2))
    elif (command== "can you tell me about todays whether" or command=="today" or command=="whether right now"):
        text.insert(END,"\n"+ "bot: "+wheater.forecast())
    elif ('play' in command):
        command = command.replace('play','')
        kit.playonyt(command)
        text.insert(END, "\n"+ "bot: playing")  
    elif('admission' in command or 'admission criteria' in command):
        text.insert(END ,"\n"+"""bot: The eligible student for admission In university for any course offererd by university has to following fee structure""",END)
        for i in adm_cret.items():
            text.insert(END,"\n")
            text.insert(END, i)
    elif('timing' in command):
        text.insert(END,"\n"+"bot: Our university Timming is from morning 10 AM to evening 5 AM")
    elif('chancelor' in command or'president' in command):
        text.insert(END,"\n"+"""bot: Poojya Dr.sharnbaswaappa Appa
        Mahadasoha Peetadipati""")
    elif("vice chancellor" in command or "secretary" in command or "registrar" in command or "dean" in command or "registrar evaluation" in command or "pro vice chancellor" in command or "administration" in command):
        if "vice chancellor" in command:
            text.insert(END,"\n"+"bot: "+administrotion.get("vice chancellor"))
        elif "secretary" in command:
            text.insert(END,"\n"+"bot: "+administrotion.get("secretary"))
        elif "registrar" in command:
            text.insert(END,"\n"+"bot: "+administrotion.get("registrar"))
        elif "pro vice chancellor" in command:
            text.insert(END,"\n"+"bot: "+administrotion.get("pro vice chancellor"))
        elif command == "registrar evaluation":
            text.insert(END,"\n"+"bot: "+administrotion.get("registrar evaluation")) 
        elif "dean" in command:
            text.insert(END,"\n"+"bot: "+administrotion.get("dean"))
        elif "administration" in command:
            for j in administrotion.items():
                text.insert(END,"\n")
                text.insert(END,j)
    elif("campus"in command):
        text.insert(END,"\n"+"bot: Yes we do have campus selection in our university, \n around 18-19 certified companies approach to our unversity and students get \nseleced on the basis of their perfomance")

    elif "course" in command:
        text.insert(END ,"\n"+"bot: " + str(courses))

    else:
        text.insert(END,"\n"+ "bot: Sorry I cant help you ! ask me again.")

file = 'header.ppm'

image = Image.open(file)

zoom = 0.15

#multiple image size by zoom
pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])

img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y))) 
label = Label(root, image=img)
label.image = img
label.pack()

text = Text(root,bg='white')
text.pack(padx=0,pady=0,expand=2)
a=Entry(root,width=100)
a.pack(anchor= SW,padx=1,pady=1)
Button(root,text='send',bg='white',width=20,command=send).pack(anchor=SE,padx=1,pady=1,fill=BOTH)
Button(root, text = "Clear", bg = 'white',width = 20, command = clear).pack(anchor=SE,padx = 2, pady =1,fill=BOTH)
root.title('Sharanbasv_university HelplineBot')

root.mainloop()