from tkinter import *
from PIL import ImageTk, Image

class App:
    def __init__(self):
        self.hunger = 0
        self.clean = 0
        self.current_frame = 0
        self.animation_counter = 1
        self.root = Tk()
        self.label = Label(text="hi!")
        self.root_initialize()
        self.stress_counter()
        self.graphics_dictionary = {}
        self.graphics_get()
        self.feed_frog()
        self.clean_cage()
        self.feed_button = Button()
        self.clean_button = Button()
        self.create_widgets()
        self.update_widgets()
        self.animate()

        # Must be done last.
        self.root.mainloop()

    def root_initialize(self):
        self.root.geometry("850x500")
        # Sizing up grid -- Larger portion to center images, smaller for Buttons
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.title("Kai-Gotchi!! V 0.0")

    def feed_frog(self):
        self.hunger = 0

    def clean_cage(self):
        self.clean = 0

    def create_widgets(self):
        self.feed_button.configure(image=self.graphics_dictionary["Hunger0"], command=self.feed_frog)
        self.feed_button.grid(column=1, row=0, sticky=SW)
        self.clean_button.configure(image=self.graphics_dictionary["Clean0"], command=self.clean_cage)
        self.clean_button.grid(column=1, row=1, sticky=NW)

    def update_widgets(self):
        # Update Hunger Bar
        if self.hunger >= 85:
            hunger_graphic = self.graphics_dictionary["Hunger5"]
        elif self.hunger >= 68:
            hunger_graphic = self.graphics_dictionary["Hunger4"]
        elif self.hunger >= 51:
            hunger_graphic = self.graphics_dictionary["Hunger3"]
        elif self.hunger >= 34:
            hunger_graphic = self.graphics_dictionary["Hunger2"]
        elif self.hunger >= 17:
            hunger_graphic = self.graphics_dictionary["Hunger1"]
        else:
            hunger_graphic = self.graphics_dictionary["Hunger0"]
        self.feed_button.configure(image=hunger_graphic)

        # Update Cleanliness Bar
        if self.clean >= 85:
            clean_graphic = self.graphics_dictionary["Clean5"]
        elif self.clean >= 68:
            clean_graphic = self.graphics_dictionary["Clean4"]
        elif self.clean >= 51:
            clean_graphic = self.graphics_dictionary["Clean3"]
        elif self.clean >= 34:
            clean_graphic = self.graphics_dictionary["Clean2"]
        elif self.clean >= 17:
            clean_graphic = self.graphics_dictionary["Clean1"]
        else:
            clean_graphic = self.graphics_dictionary["Clean0"]
        self.clean_button.configure(image=clean_graphic)

        self.root.after(1000, self.update_widgets)

    def stress_counter(self):
        if self.hunger < 100:
            self.hunger = self.hunger + 1
        if self.clean < 100:
            self.clean = self.clean +1
        self.root.after(1000, self.stress_counter)

    def graphics_get(self):
        # Emotion: Happy
        self.graphics_dictionary["Happy1"] = PhotoImage(file="graphics/happy_1.png")
        self.graphics_dictionary["Happy2"] = PhotoImage(file="graphics/happy_2.png")

        # Emotion: Neutral
        self.graphics_dictionary["Neutral1"] = PhotoImage(file="graphics/neutral_1.png")
        self.graphics_dictionary["Neutral2"] = PhotoImage(file="graphics/neutral_2.png")

        # Emotion: Mad
        self.graphics_dictionary["Mad1"] = PhotoImage(file="graphics/mad_1.png")
        self.graphics_dictionary["Mad2"] = PhotoImage(file="graphics/mad_2.png")

        # Hunger Bar; I messed up my original graphics size
        self.graphics_dictionary["Hunger0"] = ImageTk.PhotoImage(Image.open("graphics/hunger_0.png"))
        self.graphics_dictionary["Hunger1"] = ImageTk.PhotoImage(Image.open("graphics/hunger_1.png"))
        self.graphics_dictionary["Hunger2"] = ImageTk.PhotoImage(Image.open("graphics/hunger_2.png"))
        self.graphics_dictionary["Hunger3"] = ImageTk.PhotoImage(Image.open("graphics/hunger_3.png"))
        self.graphics_dictionary["Hunger4"] = ImageTk.PhotoImage(Image.open("graphics/hunger_4.png"))
        self.graphics_dictionary["Hunger5"] = ImageTk.PhotoImage(Image.open("graphics/hunger_5.png"))

        # Cleanliness Bar; same graphics issue lol
        self.graphics_dictionary["Clean0"] = ImageTk.PhotoImage(Image.open("graphics/clean_0.png"))
        self.graphics_dictionary["Clean1"] = ImageTk.PhotoImage(Image.open("graphics/clean_1.png"))
        self.graphics_dictionary["Clean2"] = ImageTk.PhotoImage(Image.open("graphics/clean_2.png"))
        self.graphics_dictionary["Clean3"] = ImageTk.PhotoImage(Image.open("graphics/clean_3.png"))
        self.graphics_dictionary["Clean4"] = ImageTk.PhotoImage(Image.open("graphics/clean_4.png"))
        self.graphics_dictionary["Clean5"] = ImageTk.PhotoImage(Image.open("graphics/clean_5.png"))
    def animate(self):
        if self.hunger + self.clean >= 150:
            frame1 = self.graphics_dictionary["Mad1"]
            frame2 = self.graphics_dictionary["Mad2"]

            # Tkinter seems unable to equate images with == operator, avoiding with
            # simple counter.

            if self.animation_counter == 1:
                self.current_frame = frame1
                self.animation_counter = 2
            else:
                self.current_frame = frame2
                self.animation_counter = 1

        elif self.hunger + self.clean >= 75:
            frame1 = self.graphics_dictionary["Neutral1"]
            frame2 = self.graphics_dictionary["Neutral2"]

            if self.animation_counter == 1:
                self.current_frame = frame1
                self.animation_counter = 2
            else:
                self.current_frame = frame2
                self.animation_counter = 1

        else:
            frame1 = self.graphics_dictionary["Happy1"]
            frame2 = self.graphics_dictionary["Happy2"]

            if self.animation_counter == 1:
                self.current_frame = frame1
                self.animation_counter = 2
            else:
                self.current_frame = frame2
                self.animation_counter = 1
        self.label.grid(column=0,row=0,rowspan=2, sticky=E)
        self.label.configure(image=self.current_frame)
        self.root.after(1000, self.animate)



# Start

app = App()