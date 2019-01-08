from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from geopy.geocoders import Nominatim
import json,urllib
from urllib.request import urlopen

def button1__click():
    name1=tbname1.get()
    name2=tbname2.get()
    if(name2!='1733' or name1!='sahib.seehra'):
        messagebox.showinfo("ERROR!!!!","Enter correct Username And Password")
    else:
        messagebox.showinfo("Done","WELCOME")
        win.destroy()
        new_win=Tk()
        new_win.state("zoomed")
        new_win.title("Options")
        canv=Canvas(new_win,height=1080,width=1920)
    
        canv.place(x=0,y=0)

        img=ImageTk.PhotoImage(Image.open("travel.jpg"))
        canv.create_image(960,540,image=img)
        def go__click():
            geolocator = Nominatim(timeout=10)
            l=tbplace.get()
            location = geolocator.geocode(""+l+"")
            new_win1=Tk()
            new_win1.state("zoomed")
            new_win1.config(bg="#9999ff")
            new_win1.title("Near by Restaurants")


        
            a=str(location.latitude)
            b=str(location.longitude)
            json_url=urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+a+","+b+"&radius=5000&type=restaurant&keyword=cruise&key=AIzaSyBDbfy5Rpn-vRIExs9-7d7IrCx9ShKePUA")
            data=json.loads(json_url.read())
            places=data["results"]
            c=len(places)

            l=[]
            for i in range(0,c):
                l.append(places[i])
            #print(len(l))
            
            d=len(l)
            b=[]
            y_value=35
            for i in range(0,d):
                a=l[i]
                b.append(a['name'])
                lbl=Label(new_win1)
                lbl.config(text=b[i],bg="#9999ff",font=('arial',12))
                lbl.place(x=100,y=y_value)
                y_value=y_value+30
            lbl4=Label(new_win1,text="Nearby Restaurants:",bg="#9999ff",font=('arial',15))
            lbl4.place(x=50,y=5)    
                
            lbl2=Label(new_win1,text=location.address,bg="#9999ff",font=('arial',15))#or use config function
            lbl2.place(x=550,y=195)
            lbl3=Label(new_win1,text="Latitude on Globe:",bg="#9999ff",font=('arial',15))
            lbl3.place(x=550,y=225)
            lblName=Label(new_win1)
            lblName.config(text=(location.latitude),bg="#9999ff",font=('arial',15))
            lblName.place(x=750,y=225)
            lbl3=Label(new_win1,text="Longitude on Globe:",bg="#9999ff",font=('arial',15))
            lbl3.place(x=550,y=255)
            lblName=Label(new_win1)
            lblName.config(text=(location.longitude),bg="#9999ff",font=('arial',15))
            lblName.place(x=750,y=255) 
            
            #lbl3=Label(new_win1,text=((location.latitude,  location.longitude)),bg="#9999ff",font=('arial',15))
            #lbl3.place(x=750,y=225)
            
 
            new_win1.mainloop()
        def go__click1():
            try:
             s=tbsource.get()
             d=tbdest.get()
            
             json_url=urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+s+"&destinations="+d+"&key=AIzaSyBeVftIRwl9mhjDGP-dblOPJstXPzkD8Ao")

             data=json.loads(json_url.read()) #reading all data


             routesdata=data["rows"]
             routesfirstdict=routesdata[0]
             legsdict=routesfirstdict['elements']
             legsfirstdict=legsdict[0]
             distdict=legsfirstdict["distance"]
             lbl=Label(new_win,text=distdict["text"],fg="black",bg="white",font=('arial',15))
             lbl.place(x=920,y=240)
            except:
             messagebox.showinfo("ERROR!!","check details or Internet connection")
                
               #print("ok")
        def go__click2():
            geolocator = Nominatim(timeout=10)
            l=tbhotel.get()
            location = geolocator.geocode(""+l+"")
            new_win1=Tk()
            new_win1.state("zoomed")
            new_win1.config(bg="#9999ff")
            new_win1.title("Near by Hotels")


        
            a=str(location.latitude)
            b=str(location.longitude)
            json_url=urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+a+","+b+"&radius=5000&type=hotel&keyword=hotel&key=AIzaSyBDbfy5Rpn-vRIExs9-7d7IrCx9ShKePUA")
            data=json.loads(json_url.read())
            hotels=data["results"]
            c=len(hotels)

            l=[]
            for i in range(0,c):
                l.append(hotels[i])
            #print(len(l))
            
            d=len(l)
            b=[]
            y_value=35
            for i in range(0,d):
                a=l[i]
                b.append(a['name'])
                lbl=Label(new_win1)
                lbl.config(text=b[i],bg="#9999ff",font=('arial',12))
                lbl.place(x=100,y=y_value)
                y_value=y_value+30
            lbl4=Label(new_win1,text="Nearby Hotels:",bg="#9999ff",font=('arial',15))
            lbl4.place(x=50,y=5)    
                
            lbl2=Label(new_win1,text=location.address,bg="#9999ff",font=('arial',15))#or use config function
            lbl2.place(x=550,y=195)
            lbl3=Label(new_win1,text="Latitude on Globe:",bg="#9999ff",font=('arial',15))
            lbl3.place(x=550,y=225)
            lblName=Label(new_win1)
            lblName.config(text=(location.latitude),bg="#9999ff",font=('arial',15))
            lblName.place(x=750,y=225)
            lbl3=Label(new_win1,text="Longitude on Globe:",bg="#9999ff",font=('arial',15))
            lbl3.place(x=550,y=255)
            lblName=Label(new_win1)
            lblName.config(text=(location.longitude),bg="#9999ff",font=('arial',15))
            lblName.place(x=750,y=255)
            new_win1.mainloop()
        lbl=Label(new_win,text="Enter place to know nearby Restaurants:",fg="black",bg="white",font=('arial',15))
        lbl.place(x=360,y=200)
        tbplace=Entry(new_win,width=50,bg="#99bbff")
        tbplace.place(x=360,y=245)
        btn1=Button(new_win,text="GO",bg="#4d88ff",fg="white",height=2,width=8,command=go__click) 
        btn1.place(x=400,y=280)
        lbl=Label(new_win,text="Enter place to know nearby Hotels:",fg="black",bg="white",font=('arial',15))
        lbl.place(x=360,y=450)
        tbhotel=Entry(new_win,width=50,bg="#99bbff")
        tbhotel.place(x=360,y=495)
        btn1=Button(new_win,text="GO",bg="#4d88ff",fg="white",height=2,width=8,command=go__click2)
        btn1.place(x=400,y=530)
        lbl=Label(new_win,text="Enter source and destination to know the distance:",fg="black",bg="white",font=('arial',15))
        lbl.place(x=800,y=70)
        lbl=Label(new_win,text="source:",fg="black",bg="white",font=('arial',15))
        lbl.place(x=800,y=130)
        tbsource=Entry(new_win,width=50,bg="#99bbff")
        tbsource.place(x=900,y=130)
        lbl=Label(new_win,text="destination:",fg="black",bg="white",font=('arial',15))
        lbl.place(x=780,y=190)
        tbdest=Entry(new_win,width=50,bg="#99bbff")
        tbdest.place(x=900,y=190)
        lbl=Label(new_win,text="Kelometers:",fg="black",bg="white",font=('arial',15))
        lbl.place(x=800,y=240)
        btn3=Button(new_win,text="GO",bg="#4d88ff",fg="white",height=2,width=8,command=go__click1) 
        btn3.place(x=1000,y=280)
        new_win.mainloop()
    
def close_window():
    win.destroy()
    


win=Tk()

win.state('zoomed')
win.config(bg='#9999ff')
win.title('python windows app')
canv=Canvas(win,height=1080,width=1920)

canv.place(x=0,y=0)

img=ImageTk.PhotoImage(Image.open("login_bg.jpg"))
canv.create_image(960,540,image=img)
canv2=Canvas(canv,height=200,width=600,bg="white")
canv2.place(x=395,y=200)

btn1=Button(win,text="Login",bg="blue",fg="white",command=button1__click) 
btn1.place(x=625,y=350)
btn2=Button(win,text="cancel",bg="blue",fg="white",command=close_window)
btn2.place(x=685,y=350)
lbl=Label(win,text="Enter Username:",fg="black",bg="white",font=('arial',10))
lbl.place(x=420,y=240)
lbl=Label(win,text="Password",fg="red",bg="white",font=('arial',10))
lbl.place(x=430,y=280)
tbname1=Entry(win,width=50,bg="#99bbff")
tbname1.place(x=590,y=240)
tbname2=Entry(win,width=50,bg="#99bbff",show="*")
tbname2.place(x=590,y=280)
win.mainloop()
