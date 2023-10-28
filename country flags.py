from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root=Tk()
root.title("Country Flags")
root.geometry("600x400")
root.configure(background="lightblue")

get_input = Entry(root)
show_label = Label(root)

india_map = ImageTk.PhotoImage(Image.open ("India.png"))
america_map = ImageTk.PhotoImage(Image.open ("America.png"))
australia_map = ImageTk.PhotoImage(Image.open ("Australia.png"))
japan_map = ImageTk.PhotoImage(Image.open ("Japan.jpg"))
philippines_map = ImageTk.PhotoImage(Image.open ("Philippines.png"))

maps_dictionary = { "India" : india_map , 
                    "America" : america_map ,
                    "Australia" : australia_map ,
                    "Philippines" : philippines_map,
                    "Japan" : japan_map,
                    "USA" : america_map,
                    "United States of America" : america_map}

def showMaps():
    map_name = get_input.get()
    try :
        show_label['image'] = maps_dictionary[map_name]
    except KeyError : 
        messagebox.showinfo("Error","Sorry! We don't have this flag image in our system")

btn = Button(root , text="Show Map", bg="green", command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()