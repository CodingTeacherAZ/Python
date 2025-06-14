import tkinter
'''
Widget - Description
Button - A clickable button
Canvas - An area used for drawing or displaying images
Checkbutton - A clickable box that can be selected or unselected
Entry - A single-line text field that the user can type in
Frame - A container for widgets
Label - A single-line display for text
Listbox - A drop-down list that the user can select from
Menu - A drop-down menu
Message - A multiline display for text
Menubutton - An item in a drop-down menu
Text - A multiline text field that the user can type in
TopLevel - An additional window
'''

## BUILDING A BASIC GUI
# Displaying a label
# tkinter Window is a container
'''
window = tkinter.Tk()
label = tkinter.Label(window, text='This is our label.')
label.pack() #every widget has a pack that places it in the parent and tells the paretn to resize itslef.
label.config(text="update a label's text")
window.mainloop()  # mainloop doesn't exit until the widow is destroyed
print("Anybody home?")  # code here won't execute unntil the window is destroyed.
'''

## USING MUTABLE VARIABLES WITH WIDGETS
# Values in tkinter containers are set and retrieved using the set and get methods
# When set is called, it tells the widgets it has been assigned to to update the GUI
# you cannot create a StringVar (or other mutable variables) unti the root Tk window
# has been created.
# StringVar, IntVar, BooleanVar, and DoubleVar
'''
window = tkinter.Tk()
data = tkinter.StringVar()
data.set('Data to display')
label = tkinter.Label(window, textvariable=data)
label.pack()

window.mainloop()
'''


## GROUPINT WIDGETS
# tkinter Frame is a container
# Frames are not directly visible. They are used to organize widgets
'''
window = tkinter.Tk()
frame = tkinter.Frame(window) # puts the frame in the root window
frame.pack()  # places it in the parent, resize the parent
first = tkinter.Label(frame, text='First Label')
first.pack()
second = tkinter.Label(frame, text='Second Label')
second.pack()
third = tkinter.Label(frame, text='Third Label')
third.pack()

window.mainloop()
'''
# use multiple frames to format the window's content and layout

## CREATING BORDERS ON FRAMES
# borderstyles: SUNKEN, RAISED, GROOVE, RIDGE (default FLAT)
'''
window = tkinter.Tk()
frame = tkinter.Frame(window, borderwidth=20, relief=tkinter.SUNKEN)
frame.pack()
frame2 = tkinter.Frame(window, borderwidth=20, relief=tkinter.RAISED)
frame2.pack()
first = tkinter.Label(frame, text='First label in first frame')
first.pack()
second = tkinter.Label(frame2, text='Second label in second frame')
second.pack()
third = tkinter.Label(frame2, text="Third label in second frame")
third.pack()

window.mainloop()
'''

## GETTING INFORMATION FROM THE USER WITH THE ENTRY TYPE
# Entry allows for a single line of text
# Use StringVar so that whenever theuser types, the value will be updated
'''
window = tkinter.Tk()
frame = tkinter.Frame(window,borderwidth=10, relief=tkinter.RIDGE)
frame.pack()
var = tkinter.StringVar()
label = tkinter.Label(frame, textvariable=var)
label.pack()
entry = tkinter.Entry(frame, textvariable=var)
entry.pack()
window.mainloop()
'''

## MODELS, VIEWS, AND CONTROLLERS
# Models: How do we separate the data? << keep track of the current state and possibly save that state to a file or database and reload it later>>
# Views: How do we display the data? <<views don't do anything else>>
# Controllers: How do we modify the data? << converts user input to function calls in the model, can update the models and trigger changes to the views>>

# in the code below:
# the model is kept track of by variable counter which updates itself automatically
# controller is function click which updates the model
# view has four objects: root window, a Frame, a Label, a button

'''
## the controller
def click():
    counter.set(counter.get() + 1)

if __name__=='__main__':
    window = tkinter.Tk()
    ## the model
    counter = tkinter.IntVar()
    counter.set(0)
    # the views
    frame = tkinter.Frame(window, borderwidth=5, relief=tkinter.RIDGE)
    frame.pack()

    button = tkinter.Button(frame, text='Click me', command=click) #command calls the function click
    button.pack()

    label = tkinter.Label(frame, textvariable=counter)
    label.pack()

    # start the machinery!
    windows.mainloop()
'''

## USING LAMBDA

window = tkinter.Tk()

# the model
counter = tkinter.IntVar()
counter.set(0)

# three controllers
def click(var, value):
    var.set(var.get() + value)
up = lambda: click(counter, 1)
down = lambda: click(counter, -1)

def change(widget, colors):
    ''' update the foreground color of a widget to show the RGB value stored in a
        dictionary with keys 'red', 'green', and 'blue'.  Does NOT check the color value.'''

    new_val = '#'
    for name in ("red", "green", "blue"):
        new_val += colors[name].get()
    widget['bg'] = new_val

def cross(text):
    text.insert(tkinter.INSERT, 'X')

# the views
frame = tkinter.Frame(window,borderwidth=10, relief=tkinter.GROOVE)
frame.pack()
button = tkinter.Button(frame, text='UP', font=('Courier', 30, 'bold italic'), fg='purple', command=up)
button.grid(row=0, column=0)
label = tkinter.Label(frame, textvariable=counter, font=("Times", 30, 'bold'), bg='green', fg='white')
label.grid(row=0, column=1)
button = tkinter.Button(frame, text="DOWN", font=("Verdana", 25, 'bold italic'), fg='blue', command=down)
button.grid(row=0, column=2)

frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame, text='Name', font=("Times", 18, 'bold'))
label.grid(row=0, column=0)
entry = tkinter.Entry(frame)
entry.grid(row=1, column=1)



frame = tkinter.Frame(window)
frame.pack()
first = tkinter.Label(frame, text='Enter two characters from 0 - 9 and/or A - F', font=("Verdana", 16))
first.pack()
second = tkinter.Label(frame, text='Then select update to see your color', font=("Verdana", 16))
second.pack()
# Set up text entry widgets for red, green, and blue, storing the
# associated variables in a dictionary for later use
colors = {}
for (name, col) in (('red', '#FF0000'),
                    ('green', '#00FF00'),
                    ('blue', '#0000FF')):
    colors[name] = tkinter.StringVar()
    colors[name].set('00')
    entry = tkinter.Entry(frame, textvariable=colors[name], font=("Verdana", 16), bg= col, fg='white')
    entry.pack()

# Display the current color
current = tkinter.Label(frame, text='       ', font=("Verdana", 16), bg='#FFFFFF')
current.pack()

# Give the user a way to trigger a color update
update = tkinter.Button(frame, text='Update', font=("Verdana", 16), command=lambda: change(current, colors))
update.pack()

frame = tkinter.Frame(window)
frame.pack()

text = tkinter.Text(frame, height=3, width=10)
text.pack()

button = tkinter.Button(frame, text='Add X' ,  font=("Courier", 20), command=lambda: cross(text))
button.pack()

frame = tkinter.Frame(window)
frame.pack()
red = tkinter.IntVar()
green = tkinter.IntVar()
blue = tkinter.IntVar()

for (name, var) in (('R', red), ("G", green), ("B", blue)):
    check = tkinter.Checkbutton(frame, text=name, variable=var)
    check.pack(side='left')

def recolor(widget, r, g, b):
    color = '#'
    for var in (r, g, b):
        color += 'FF' if var.get() else '00'
    widget.config(bg=color)

label = tkinter.Label(frame, text='[       ]')
button = tkinter.Button(frame, text='UPDATE', font=("Courier", 20, 'bold'), command=lambda: recolor(label, red, green, blue))
button.pack(side='left')
label.pack(side='left')
        
tkinter.mainloop()











