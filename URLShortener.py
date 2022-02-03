from ast import Interactive
from cgitb import text
from turtle import width
import pyshorteners
from tkinter import *

app = Tk()
app.title("UrlShortener")
app.geometry('500x500')


def short(): 
        # sloved by using l = url.get() instead of l = Str(url.get())

        l = url.get()
        typeurl = pyshorteners.Shortener(api_key='a489c6c0fd716e34ae803a957aa37ce1d192cf72')
        short = typeurl.bitly.short(l)
        ans.config(text="The Shortened URL is: " + short)


Lab = Label(app,text = "Enter the URL to shorten:",font='Helvetica 10 bold').place(x = 150,y = 20)  

url = Entry(app, width=40)
url.pack(padx=40,pady=60)

button = Button(app, text="Click to Short URL", command=short, bg="gray").place(x = 195,y = 150)  

ans = Label(app,relief='flat',text='',font='Helvetica 12 bold')
ans.pack(padx=50,pady=60)
app.mainloop()
