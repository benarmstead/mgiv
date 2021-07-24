"GTK python minimalist image viewer"

#Dependancies
#
# Found in requirements.txt
# GTK mus also be installed locally


#Used for getting image resolution
from PIL import Image

import sys

import os
from os import listdir
from os.path import isfile, join

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk


class MainWindow(Gtk.Window):
    "Main window which shows the image"

    def __init__(self):
        "Initialises display"
        super().__init__()
        self.display()

    def set_image(self):
        "Sets the image, also called when image is clicked"
        self.image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_scale(all_pictures[img_no], self.width, self.height, True))

    def display(self):
        "Shows the image on the screen"
        
        self.set_icon_from_file("../icon/icon.jpg")
        #Logic to decide what screen resolution to open at
        screen = self.get_screen()

        #gets screen width and heigh
        scrWidth = screen.get_width()
        scrHeight = screen.get_height()

        #gets image width and image height
        imgWidth, imgHeight = Image.open(all_pictures[img_no]).size

        #If image with or height is more than the screens resolution, uses screen resolution
        if imgWidth > scrWidth or imgHeight > scrHeight:
            self.width = scrWidth
            self.height = scrHeight

        #If image < screen resolution, uses the image resolution
        else:
            self.width = imgWidth
            self.height = imgHeight

        #This can be used if needed to be set to a default resolution
        #self.width = 800
        #self.height = 800
        #self.set_default_size(width, height)

        #Sets display title
        self.set_title("MGIV")

        #Creates image module and invokes set_image functions
        self.image = Gtk.Image()
        self.set_image()

        self.connect("key-press-event",self.on_key_press_event)

        #Adds image to screen
        self.add(self.image)

        self.connect("destroy", Gtk.main_quit)


    def on_key_press_event(self, widget, event):
        "Moves to image to left or right depending on keypress"
        global img_no

        #gets keypress value
        value = Gdk.keyval_name(event.keyval)

        #If right arrow pressed and the next image is within the bounds of the array
        if value == "Right" and img_no < len(all_pictures)-1:
            img_no += 1
            self.set_image()
        
        #If left arrow pressed and the left image is within the bounds of the array
        elif value == "Left" and img_no > 0:
            img_no -= 1
            self.set_image()
        
        #Full screen on <F11> and reset the image
        #Doesnt work right now, needs adding
        elif value == "<F11>":
            window.fullscreen()
            self.set_image()

        #This could be added to e.g. loop back to the start if right is pressed after the last image
        #However I personally do not like that functionality, so have not fully implemented it
        #"""
        #elif img_no - 1 <= 0 or img_no + 1 >= len(all_pictures) - 1:
        #    #Maybe set loop back here?
        #    pass
        #"""


def main():
    "Creates the MainWindow and starts the program"
    win = MainWindow()
    win.show_all()
    Gtk.main()



def gen_all_pictures(image_names, add_direc, do_add):
    "Generates the list of images and ensures their directorys are correct"
    def add_back(current):
        "Adds missing directories if the abspath gets it incorrect"
        current = os.path.abspath(current).split("/")
        current.append("/".join(add_direc))

        cur_len = len(current)
        temp = current[cur_len - 1]
        current[cur_len - 1] = current[cur_len - 2]
        current[cur_len - 2] = temp
        return "/".join(current)


    #Stores files ending in an image extension in the array below
    all_pictures = []

    for i in range(len(image_names)):
        current = image_names[i]
        if current.endswith((
            '.jpg',
            '.png',
            '.jpeg',
            '.webp',
            '.tiff',
            '.gif',
            '.psd',
            '.raw',
            '.bmp',
            '.heif',
            '.svg',
            )) == True:
            
            #Modifications to the file names to get the full path
            #Different modifications occur depending on the original path given

            if do_add == 1:
                all_pictures.append(add_back(current))

            elif do_add == 2:
                all_pictures.append(os.path.abspath(current))

            elif do_add == 3:
                all_pictures.append("/".join(add_direc) + "/" + current)
    
    return all_pictures



def start():
    "Starts the program and handles the logic of multiple images and if e.g. no image is specified"
    
    #Creates the global vairbales needed
    global all_pictures_len
    global img_no
    global all_pictures
    
    #Trys to find file in directory and then finds other pictures in the same directory
    try:
        arg1 = sys.argv[1]
        add_direc = arg1.split('/')
        add_direc.pop()

        path = os.path.dirname(os.path.abspath(arg1))
        image_names = [i for i in listdir(path) if isfile(join(path, i))]
        c = 0

    #If no file was specified then trys to find images in current directory
    except IndexError:
        print("You did not pass an image to view, attempting to open first found image anyway...")
        
        #Finds images in current directory
        path = os.getcwd()
        image_names = [i for i in listdir(path) if isfile(join(path, i))]
        print("Found one!")
        c = 1
        add_direc = []
    
    #If file begins with root directy, sets out of scope to 0,
    #so that no further action is taken
    try:
        out_of_scope = sys.argv[1].index("/")

    except:
        out_of_scope = 1

    #If out of scope send flag 3 to gen_all_pictures
    if out_of_scope == 0:
        all_pictures = gen_all_pictures(image_names, add_direc, 3)
        
    #If the length of the directory to add is above 0 send 1 flag throug
    elif len(add_direc) > 0 :
        all_pictures = gen_all_pictures(image_names, add_direc, 1)
    
    else:
        all_pictures = gen_all_pictures(image_names, add_direc, 2)

    #If no file was found adds picture in directory, if fails, no picture was found
    if c == 1:
        try:
            sys.argv.append(all_pictures[0])
        
        except IndexError:
            print("No images in your directory")
            exit()

    all_pictures_len = len(all_pictures)
    
    #Gets the position in the array of the picture to be shown
    img_no = all_pictures.index(os.path.abspath(sys.argv[1]))

    #Starts GUI
    main()

start()
