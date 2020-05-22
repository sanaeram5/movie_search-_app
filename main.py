import tkinter as tk
from PIL import Image,ImageTk
import imdb
from urllib.request import urlopen
from io import BytesIO

HEIGHT=500
WIDTH=600

def get_movie():
    l=""
    moviesDB = imdb.IMDb()
    movies = moviesDB.search_movie_advanced(entry.get())
    id = movies[0].getID()
    movie = moviesDB.get_movie(id)
    title = movie['title']
    year = movie['year']
    rating = movie['rating']
    genres=movie['genres']
    directors = movie['directors']
    casting = movie['cast']
    url= movie['cover url']

    l=l+"Titcd le: %s-%s\n"%(title,year)
    l=l+"Rating: %s\n"%(rating)
    gn=' '.join(map(str,genres))
    l=l+"Genres: %s\n"%(gn)
    directStr = ' '.join(map(str, directors))
    l=l+"Director: %s\n"%(directStr)
    l=l+"Cast: "
    i=0
    for c in casting:
        if i==10:
            break
        else:
            l=l+"%s  "%(c)
            i+=1
    label['text']=l
    u = urlopen(url)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im)
    image_label = tk.Label(lower_frame, image=photo, bd=2, width=50, height=70)
    image_label.image=photo
    image_label.place(relx=0.05, rely=0.5,relwidth=0.3, relheight=0.4)


root=tk.Tk()
root.title("Movie Review")
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image= tk.PhotoImage(file='los angeles.png')
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

frame=tk.Frame(root,bg='red',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.78,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=('Courier',13))
entry.place(relwidth=0.70,relheight=1)

button=tk.Button(frame,text="Search Movie",font=('Courier',12),command=get_movie)
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame = tk.Frame(root,bg='#80c1ff',bd=5)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.7,anchor='n')

label=tk.Label(lower_frame,font=('Courier',8),anchor='nw',justify='left',bd=4,wraplength=440)
label.place(relwidth=1,relheight=1)

root.mainloop()