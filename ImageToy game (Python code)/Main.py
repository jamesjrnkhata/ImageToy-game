# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------ MSc Introductory Module for Computing (2019) ---------------------------------- #
# ------------------------------------ IMAGETOY GAME (Graphical User Interface) -------------------------------------- #
# ------------------------------------ Instructor:  Dr Mahvish Nazir ------------------------------------------------- #
# ------------------------------------ Written by:	James J Nkhata --------------------------------------------------- #
# -------------------------------- Student Number:	         --------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------- Main.py (1 of 1) ----------------------------------------------------- #

# ------------------------------------------ Module Imports ---------------------------------------------------------- #
from tkinter import * # used to import all from the tkinter library
from tkinter import messagebox  # used to import messagebox from the tkinter library
from tkinter import filedialog
import image_slicer
from PIL import Image, ImageTk, ImageDraw
import math
import random
# -------------------------------------------------------------------------------------------------------------------- #

# ----------------------------------------- START OF MAIN FUNCTION --------------------------------------------------- #
class ToyGameGUI:

    #RUN THE __INIT__ FUNCTION AND PASS THE ROOT OBJECT AS MASTER
    def __init__(self, master):
        self.passed_value = 0  #  initialise passed_value to 0
        self.image_tile_list = []  #  initialise image_tile_list to blank list
        self.img = []  #  initialise img to blank list

        w, h = 810, 810  # set the width and height for the interface
        master.minsize(width=w, height=h)  # set the gui interface's minimum width and height

        # Set root (master) title
        master.title("ImageToy Game")

        self.top_frame = Frame(master)  # create (top)frame for gui interface
        self.top_frame.grid()  # use grid manager to place the object into the window

        # create Frame object for the bottom section of the gui
        self.bottom_frame = Frame(master, bd=2, relief=SUNKEN)
        self.bottom_frame.grid()  # use grid manager to place the object into the window
        # ------------------------------------------------------------------------------------------------------------ #
        # ------------------------------- define menu and dropdown for the userinterface ----------------------------- #
        imageToymenu = Menu(master)
        master.config(menu=imageToymenu)
        self.sub_menu = Menu(imageToymenu, tearoff=0)
        imageToymenu.add_cascade(label="File", menu=self.sub_menu)
        self.sub_menu.add_command(label="Open", command=self.file_browser)
        self.sub_menu.add_separator()
        self.sub_menu.add_command(label="Exit", command=master.quit)
        # ------------------------------------------------------------------------------------------------------------ #
        # ------------------------------- define Entry widgets for the userinterface --------------------------------- #
        self.difficulty_label = Label(self.top_frame, text="Enter Difficulty")
        self.difficulty_entry = Entry(self.top_frame, width=3)  # entry used to specify game difficulty
        self.difficulty_label.grid(row=0, column=6)
        self.difficulty_entry.grid(row=0, column=7)
        # ------------------------------------------------------------------------------------------------------------ #
        # ------------------------------- define button widgets for the userinterface -------------------------------- #
        self.button_start_game = Button(self.top_frame, text="Start Game", command=self.start_game)
        self.button_start_game.grid(row=0, column=8)

        self.button_reset_game = Button(self.top_frame, text="Reset", command=self.reset_button)
        self.button_reset_game.configure(state="disable")  # disable the button_reset_game button
        self.button_reset_game.grid(row=0, column=9)

        self.Display_label = Label(self.bottom_frame, width=800, height=800)
    # ---------------------------------------------------------------------------------------------------------------- #

    # ----------------------------------- GUI FUNCTION DEFINITIONS --------------------------------------------------- #

    # FUNCTION USED TO BROWSE FOR JPEG AND GIF IMAGES
    def file_browser(self):

        # open file through dialog box that only accepts jpeg and gif images
        # https://stackoverflow.com/questions/44403566/add-multiple-extensions-in-one-filetypes-mac-tkinter-filedialog-askopenfilenam
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=[("jpeg / gif files", "*.gif *.jpg")])
        if self.filename != "":
            self.image = Image.open(self.filename)
            self.square_image = self.image.resize((800, 800))  # resize image to a square grid of 800 x 800
            self.square_image.save('saved_image.gif')
            self.label_image = PhotoImage(file='saved_image.gif')
            self.Display_label.configure(image=self.label_image)
            self.Display_label.grid()

    # FUNCTION USED TO LOOP THROUGH THE IMAGE_TILE_LIST ITERATOR
    # https://stackoverflow.com/questions/49916944/how-to-use-python-tkinter-to-iterate-images#
    def next_img(self):
        try:
            self.img = next(self.images)  # get the next image from the iterated image_tile_list
        except StopIteration:
            return  # if there are no more images, do nothing

    # FUNCTION USED TO INTIALIZEE THE TILE / IMAGE GRIDS RANDOMIZING
    def randomize_tiles(self):
        for _ in range(self.passed_value*2):
            # condition used to prevent random row and column values exceeding the edges of the 4 grid area
            if self.last_blank_row-1 >= 0 and self.last_blank_column-1 >= 0:
                rand_row = self.last_blank_row - 1
                rand_col = self.last_blank_column - 1
                times = random.randint(1, 3)  # generate a random number between 1 - 3 to perform the rotate_grid_area
                self.rotate_grid_area(times, rand_row, rand_col)

            # ADD COMPLEXITY TO THE RANDOMIZING OF THE TILES BY UNCOMMENTING
            # condition used to add more complexity to the randomizing_tiles (NOT FULLY DEBUGGED)
            #elif self.last_blank_row+1 < self.passed_value-1 and self.last_blank_column+1 < self.passed_value-1:
                #rand_row = self.last_blank_row - 1
                #rand_col = self.last_blank_column
                #times = random.randint(1, 3)  # generate a random number between 1 and 3
                #self.rotate_grid_area(times, rand_row, rand_col)

            else:
                pass  # do nothing

    # FUNCTION USED TO RANDOMIZIE INTERNALLY BY ROTATING THE TILES / IMAGE GRIDS
    def rotate_grid_area(self, times, r_row, r_col):

        for _ in range(times):
            # rotate entries in the grid area clockwise starting from first position (row=rand_row, column=rand_col)
            # pos1 is row=0,col=0; pos2 is row=0,col=0+1; pos3 is row=0+1,col=0+1; pos4 is row=0+1,col=0 entries
            # pos1 is relative to rand_row and rand_col
            pos1 = self.buttons[r_row][r_col].value_working  # access number entry in .value_working and assign to pos1
            imag1 = self.buttons[r_row][r_col].image  # access image entry in .image and assign to pos1

            pos2 = self.buttons[r_row][r_col+1].value_working  # access number entry in .value_working and assign to pos2
            imag2 = self.buttons[r_row][r_col+1].image  # access image entry in .image and assign to pos2

            pos3 = self.buttons[r_row+1][r_col+1].value_working  # access number entry in .value_working and assign to pos3
            imag3 = self.buttons[r_row+1][r_col+1].image  # access image entry in .image and assign to pos3

            pos4 = self.buttons[r_row+1][r_col].value_working  # access number entry in .value_working and assign to pos4
            imag4 = self.buttons[r_row+1][r_col].image  # access image entry in .image and assign to pos4

            # tile 4 moved to tile 1
            # condition to check if the value in pos4 belongs to the blank image tile
            if pos4 == self.buttons[self.last][self.last].value_solution:
                self.last_blank_row = r_row  # if true then set the new last_blank_row to rand_row
                self.last_blank_column = r_col  # if true then set the new last_blank_column to rand_column
            self.buttons[r_row][r_col].value_working = pos4  # change the value of pos1 to that of pos4
            self.buttons[r_row][r_col].image = imag4  # change the image of pos1 to that of pos4
            self.buttons[r_row][r_col].configure(image=imag4)  # change the image to new image

            # tile 1 moved to tile 2
            # condition to check if the value in pos1 belongs to the blank image tile
            if pos1 == self.buttons[self.last][self.last].value_solution:
                self.last_blank_row = r_row  # if true then set the new last_blank_row to rand_row
                self.last_blank_column = r_col+1  # if true then set the new last_blank_column to rand_column + 1
            self.buttons[r_row][r_col+1].value_working = pos1  # change the value of pos2 to that of pos1
            self.buttons[r_row][r_col+1].image = imag1  # change the image of pos2 to that of pos1
            self.buttons[r_row][r_col+1].configure(image=imag1)  # change the image to new image

            # tile 2 moved to tile 3
            # condition to check if the value in pos2 belongs to the blank image tile
            if pos2 == self.buttons[self.last][self.last].value_solution:
                self.last_blank_row = r_row+1  # if true then set the new last_blank_row to rand_row + 1
                self.last_blank_column = r_col+1   # if true then set the new last_blank_column to rand_column + 1
            self.buttons[r_row+1][r_col+1].value_working = pos2  # change the value of pos3 to that of pos2
            self.buttons[r_row+1][r_col+1].image = imag2  # change the image of pos3 to that of pos2
            self.buttons[r_row+1][r_col+1].configure(image=imag2)  # change the image to new image

            # tile 3 moved to tile 4
            # condition to check if the value in pos3 belongs to the blank image tile
            if pos3 == self.buttons[self.last][self.last].value_solution:
                self.last_blank_row = r_row+1  # if true then set the new last_blank_row to rand_row + 1
                self.last_blank_column = r_col   # if true then set the new last_blank_column to rand_column
            self.buttons[r_row+1][r_col].value_working = pos3  # change the value of pos4 to that of pos3
            self.buttons[r_row+1][r_col].image = imag3  # change the image of pos4 to that of pos3
            self.buttons[r_row+1][r_col].configure(image=imag3)  # change the image to new image

    # FUNCTION USED TO PROCESS THE SOLUTION OF THE GAME FROM THE BUTTON PRESSES
    def process_solution(self, row, column):
        blank_row = self.last_blank_row  # set the working variable blank_row to self.last_blank_row
        blank_column = self.last_blank_column  # set the working variable blank_row to self.last_blank_row
        #  Check if the button pressed is the blank tile, if it is then do nothing
        if self.buttons[row][column].value_working != self.buttons[blank_row][blank_column].value_working:

            temp = self.buttons[row][column].image  # temporarily hold the image contained in the indexed image
            temp_working_value = self.buttons[row][column].value_working  # hold the value indexed

            blank = self.buttons[blank_row][blank_column].image  # hold the image contained in the indexed image
            blank_working_value = self.buttons[blank_row][blank_column].value_working   # hold the value indexed

            self.buttons[row][column].image = blank  # set the indexed to the image held by blank
            self.buttons[row][column].value_working = blank_working_value  # set the indexed to blank_working_value

            self.buttons[blank_row][blank_column].image = temp  # set the indexed image to that held by temp
            self.buttons[blank_row][blank_column].value_working = temp_working_value   # set the indexed to temp_working

            self.buttons[row][column].configure(image=blank)  #  update the button image
            self.buttons[blank_row][blank_column].configure(image=temp)  #  update the button image

            self.last_blank_row = row  # update the last_blank_row value
            self.last_blank_column = column # update the last_blank_column value

            # Check if the tiles in value_working match those of value_solution
            # condition check when the first entry tile for value_working is the same as value_solution
            if self.buttons[0][0].value_working == self.buttons[0][0].value_solution:
                # condition check when the last entry tile for value_working is the same as value_solution
                if self.buttons[self.last][self.last].value_working == self.buttons[self.last][self.last].value_solution:
                    results = 0  # intialise results to o
                    # start the nested For loops to access the 2 dimensional lists
                    for row in range(self.passed_value):
                        for col in range(self.passed_value):
                            if self.buttons[row][col].value_working == self.buttons[row][col].value_solution:
                                results = results+1  # increment result at the end of each row column loop

                    if results == self.buttons[self.last][self.last].value_solution:
                        self.buttons[self.last][self.last].configure(image=self.solved_image)
                        messagebox.showinfo(title="Success !", message="You Win !")  # display a messagebox for winning
                        self.reset_button()  # run the reset function

    # FUNCTION USED TO START A GAME AFTER SELECTING THE DIFFICULTY
    def start_game(self):
        self.sub_menu.entryconfig(0, state=DISABLED)  # Disable "open" in the dropdown menu to stop images piling up
        value_int = 1  # intitalize to 1
        tiles = []  # intitalize to empty list
        tile_list = []  # intitalize to empty list
        self.image_tile_list = []  # intitalize to empty list
        self.img = []  # intitalize to empty list
        tile_width = 0   # intitalize to 0
        tile_height = 0  # intitalize to o

        # try used to catch exceptions thrown
        try:
            self.passed_value = int(self.difficulty_entry.get())  # - Get the value passed by the player
            # if the value entered is between 2 and 20
            if 1 < self.passed_value <= 20:

                self.Display_label.grid_remove()  # remove Display_label widget from GUI
                self.difficulty_entry.configure(state="disabled")  # disable the difficulty_entry entry
                self.button_start_game.configure(state="disabled")  # disable the button_start_game button
                self.button_reset_game.configure(state="normal")  # enable the button_reset_game button
                """
                ****** How image_slicer.slice Function works ******
                https://pypi.org/project/image_slicer/ 
                Calculate the number of columns and rows required to divide an image into ``n`` parts.                                
                num_columns = int(ceil(sqrt(n)))
                num_rows = int(ceil(n / float(num_columns)))
                The method ceil(x) in Python returns ceiling value of x i.e., the smallest integer not less than x.
                """
                # Number passed for 'n' parts can be between 2 and 9800
                # Slice 'saved_image.gif' into 'n' value returns non-square image grid for some values e.g. 5 gives 2x3
                # so grid_size_value used to calculate the square for the self.passed_value instead e.g. 5^2 gives 5x5
                grid_size_value = math.pow(self.passed_value, 2)  # calculate the square of the passed_value
                tiles = image_slicer.slice('saved_image.gif', grid_size_value, save=False)  # do not save tiled images
                tile_list = tiles[0:]  # remove the first entry of the tiles list as it contains a zero entry

                # loop through tile_list and extract tile.image entries
                for tile in tile_list:
                    overlay = ImageDraw.Draw(tile.image)  # draw overlays over the tiled images
                    overlay.text((5, 5), str(tile.number))  # draw the tile # as a string overlay on the tiled image
                    self.image_tile_list.append(tile.image)  # append images extracted from image_slicer to tile_list

                self.images = iter(self.image_tile_list)  # make an iterator

                tile_width, tile_height = self.image_tile_list[0].size  # save  width & height of tile #1 of the image
                # anonymous functions (lambda) to create the tile (grid) buttons
                # https://github.com/TigerhawkT3/small_scripts/blob/master/memory_tile_gui.py
                self.buttons = [[Button(self.bottom_frame,
                            command=lambda row=row, column=column: self.button_press(row,
                                 column))for column in range(self.passed_value)] for row in range(self.passed_value)]

                for row in range(self.passed_value):

                    for column in range(self.passed_value):
                        self.next_img()
                        button_image = ImageTk.PhotoImage(self.img)
                        self.buttons[row][column].grid(row=row, column=column)  # use grid manager to place buttons
                        self.buttons[row][column].image = button_image  # keep a reference so it's not garbage collected
                        self.buttons[row][column].value_working = value_int  # set value_int to indexed value_working
                        self.buttons[row][column].value_solution = value_int  # set value_int to indexed value_soultion
                        self.buttons[row][column].configure(image=button_image)  # set image to button
                        value_int = value_int + 1  # increment value_int to change the value in the next iteration
                # Replace the last tile entry with a blank tile
                self.last = self.passed_value - 1  # decrement 1 from passed_value and assign to last
                self.solved_image = self.buttons[self.last][self.last].image  # Save the last tile image before replacing it

                temp_blank_image = Image.open('blank_space.jpg')  # open the presaved blank_space image template
                resize_blank = temp_blank_image.resize((tile_width, tile_height))  # resize blank tile to fit grid
                blank_image = ImageTk.PhotoImage(resize_blank)
                self.buttons[self.last][self.last].image = blank_image  #   save the  blank_image to indexed
                self.buttons[self.last][self.last].configure(image=blank_image)  #   update the button image

                self.last_blank_row = self.last  # update the last_blank_row value
                self.last_blank_column = self.last  # update the last_blank_column value

                self.randomize_tiles()  # run randomize_tiles() function

            # if non of the values between 2 - 20 are entered
            else:
                messagebox.showinfo("Error", "An Integer between 2 - 20 must be Entered ")
        # when a wrong data type is inputted display a warning messagebox
        except ValueError:
            messagebox.showwarning("Value Error", "Only Integers between 2 - 20 can be Entered ")

    # FUNCTION USED TO HANDLE BUTTON PRESSES SET BY LAMBDA FUNCTIONS IN START_GAME()
    def button_press(self, row, column):
        # check if the button pressed is immediately left or right of the blank button
        if row == self.last_blank_row and (column == self.last_blank_column-1 or column == self.last_blank_column+1):
            self.process_solution(row, column)  # run the process_solution() function with parameters row and column
        # check if the button pressed is immediately above or below of the blank button
        if column == self.last_blank_column and (row == self.last_blank_row-1 or row == self.last_blank_row + 1):
            self.process_solution(row, column)  # run the process_solution() function with parameters row and column
    # FUNCTION USED TO RESET THE GAME
    def reset_button(self):
        for row in range(self.passed_value):
            for col in range(self.passed_value):
                self.buttons[row][col].grid_remove()

        self.label_image = PhotoImage(file='saved_image.gif') # reload the 'saved_image.gif'
        self.Display_label.configure(image=self.label_image) # configure 'saved_image.gif' to Display_label
        self.Display_label.grid()  # add the Display_label back on to the GUI
        self.sub_menu.entryconfig(0, state=NORMAL)  # Enable "open" in the dropdown menu
        self.difficulty_entry.configure(state="normal")  # enable the difficulty_entry entry
        self.button_start_game.configure(state="normal")  # enable the button_start_game button
        self.button_reset_game.configure(state="disable")  # disable the button_reset_game button


root = Tk()  # create tkinter instance and name it root
toygame_gui = ToyGameGUI(root)  # create instance of ToyGameGUI class and pass root
root.mainloop()  # run the tkinter object root in a loop
