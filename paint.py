from tkinter import *
import tkinter.font
from tkcolorpicker import askcolor

class PaintApp:
    drawing_tool = "pencil"
    left_but = "up"
    fill_color = "black"
    outline_color = "black"
    text = "Hello"
    font_family = "Helvetica"
    font_size = 12
    font_weight = "normal"
    font_slant = "roman"
    font_underline = 0
    font_overstrike = 0
    width = 2
    brush_size = 5
    x_pos, y_pos = None, None
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    def left_but_down(self, event=None):
        self.left_but = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    def left_but_up(self, event=None):
        self.left_but = "up"
        self.x_pos = None
        self.y_pos = None
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool == "eraser":
            self.pencil_draw(event)

        elif self.drawing_tool == "pencil":
            self.pencil_draw(event)

        elif self.drawing_tool == "line":
            self.line_draw(event)

        elif self.drawing_tool == "arc":
            self.arc_draw(event)

        elif self.drawing_tool == "pieslice":
            self.pieslice_draw(event)

        elif self.drawing_tool == "chord":
            self.chord_draw(event)

        elif self.drawing_tool == "oval":
            self.oval_draw(event)

        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)

        elif self.drawing_tool == "text":
            self.text_draw(event)

    def motion(self, event=None):
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)
        elif self.drawing_tool == "eraser":
            self.fill_color = "white"
            self.pencil_draw(event)

    def pencil_draw(self, event=None):
        if self.left_but == "down":
            if None not in (self.x_pos, self.y_pos):
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE,
                                        fill=self.fill_color, width=self.brush_size)
            self.x_pos = event.x
            self.y_pos = event.y

    def line_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,
                                    self.y2_line_pt, smooth=TRUE, fill=self.fill_color)

    def arc_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
            event.widget.create_arc(coords, start=0, extent=150, style=ARC, fill=self.fill_color)

    def pieslice_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
            event.widget.create_arc(coords, start=0, extent=150, style=PIESLICE,
                                    fill=self.fill_color, outline=self.outline_color)

    def chord_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
            event.widget.create_arc(coords, start=0, extent=150, style=CHORD, fill=self.fill_color,
                                    outline=self.outline_color)

    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
            event.widget.create_oval(coords, fill=self.fill_color, outline=self.outline_color,
                                    width=self.width)

    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt
            event.widget.create_rectangle(coords, fill=self.fill_color, outline=self.outline_color,
                                        width=self.width)

    def text_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt):
            text_font = tkinter.font.Font(family=self.font_family, size=self.font_size,
                                weight=self.font_weight, slant=self.font_slant, underline=self.font_underline,
                                overstrike=self.font_overstrike)
            event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill=self.fill_color,
                                     font=text_font, text=self.text)


    @staticmethod
    def quit_app(event=None):
        root.quit()

    def set_tool(self, value):
        self.drawing_tool = value

    def set_fill_color(self, event=None):
         color = askcolor((255, 255, 0), root)
         self.fill_color = color[1]

    def set_outline_color(self, event=None):
         color = askcolor((255, 255, 0), root)
         self.outline_color = color[1]

    def set_width(self, event=None):
         top = Toplevel()
         label = Label(top, text="Enter width: ")
         label.grid(row=0, column=1, sticky=E, pady=4)

         entry = Entry(top)
         entry.grid(row=0, column=3, sticky=E, pady=4)

         button=Button(top, text="Set Size",command=lambda value=entry.get:
                        self.width_button_press(value))
         button.grid(row=0, column=7, sticky=E, pady=4)

    def width_button_press(self, value):
        self.width = value()

    def set_text(self):
        top = Toplevel()
        label = Label(top, text="Enter text: ")
        label.pack()

        entry = Entry(top)
        entry.pack()

        button=Button(top, text="Set Text",command=lambda value=entry.get:
                        self.text_button_press(value))
        button.pack()

    def text_button_press(self, value):
        self.text = value()



    def set_font_size(self):
        top = Toplevel()
        label = Label(top, text="Enter text size: ")
        label.pack()

        entry = Entry(top)
        entry.pack()

        button=Button(top, text="Set Text Size",command=lambda value=entry.get:
                        self.font_size_button_press(value))
        button.pack()

    def font_size_button_press(self, value):
        self.font_size = value()

    def set_font_weight(self):
        if self.font_weight == "normal":
            self.font_weight = "bold"
        else:
            self.font_weight = "normal"

    def set_font_slant(self):
        if self.font_slant == "roman":
            self.font_slant = "italic"
        else:
            self.font_slant = "roman"

    def set_font_underline(self):
        if self.font_underline == 0:
            self.font_underline = 1
        else:
            self.font_underline = 0

    def set_font_overstrike(self):
        if self.font_overstrike == 0:
            self.font_overstrike = 1
        else:
            self.font_overstrike = 0

    def set_font_family(self, value):
        self.font_family = value

    def set_brush_width(self):
        top = Toplevel()
        label = Label(top, text="Enter brush size: ")
        label.pack()

        entry = Entry(top)
        entry.pack()

        button=Button(top, text="Set Brush Size",command=lambda value=entry.get:
                        self.brush_size_button_press(value))
        button.pack()

    def brush_size_button_press(self, value):
        self.brush_size = value()


    def __init__(self, root):

        menubar = Menu(root)

        file_menu = Menu(root, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Exit", command=self.quit_app)

        menubar.add_cascade(label="File", menu=file_menu)

        options_menu = Menu(root, tearoff=0)
        options_menu.add_command(label="eraser", command=lambda value="eraser": self.set_tool(value))
        options_menu.add_separator()
        options_menu.add_command(label="pencil", command=lambda value="pencil": self.set_tool(value))
        options_menu.add_command(label="line", command=lambda value="line": self.set_tool(value))
        options_menu.add_command(label="arc", command=lambda value="arc": self.set_tool(value))
        options_menu.add_separator()
        options_menu.add_command(label="pieslice", command=lambda value="pieslice": self.set_tool(value))
        options_menu.add_command(label="chord", command=lambda value="chord": self.set_tool(value))
        options_menu.add_separator()
        options_menu.add_command(label="oval", command=lambda value="oval": self.set_tool(value))
        options_menu.add_command(label="rectangle", command=lambda value="rectangle": self.set_tool(value))
        options_menu.add_separator()
        options_menu.add_command(label="text", command=lambda value="text": self.set_tool(value))

        menubar.add_cascade(label="Tools", menu=options_menu)

        color_menu = Menu(root, tearoff=0)
        color_menu.add_command(label="Select Fill Color", command=self.set_fill_color)
        color_menu.add_command(label="Select Outline Color", command=self.set_outline_color)
        color_menu.add_separator()
        color_menu.add_command(label="Set Outline Size", command=self.set_width)

        menubar.add_cascade(label="Color", menu=color_menu)

        text_menu = Menu(root, tearoff=0)
        font_menu = Menu(root, tearoff=0)
        font_menu.add_command(label="Arial Black", command=lambda value="Arial Black": self.set_font_family(value))
        font_menu.add_command(label="Courier New", command=lambda value="Courier New": self.set_font_family(value))
        font_menu.add_command(label="DejaVu Sans", command=lambda value="DejaVu Sans": self.set_font_family(value))
        font_menu.add_command(label="Edwardian Script ITC", command=lambda value="Edwardian Script ITC": self.set_font_family(value))
        font_menu.add_command(label="Garamond", command=lambda value="Garamond": self.set_font_family(value))
        font_menu.add_command(label="Georgia", command=lambda value="Georgia": self.set_font_family(value))
        font_menu.add_command(label="Papyrus", command=lambda value="Papyrus": self.set_font_family(value))
        font_menu.add_command(label="Rockwell", command=lambda value="Rockwell": self.set_font_family(value))
        font_menu.add_command(label="Small Fonts", command=lambda value="Small Fonts": self.set_font_family(value))
        font_menu.add_command(label="Wide Latin", command=lambda value="Wide Latin": self.set_font_family(value))
        text_menu.add_cascade(label="Font Family", menu=font_menu)

        text_menu.add_command(label="Change Text", command=self.set_text)
        text_menu.add_command(label="Set Font Size", command=self.set_font_size)
        text_menu.add_command(label="Bold", command=self.set_font_weight)
        text_menu.add_command(label="Italic", command=self.set_font_slant)
        text_menu.add_command(label="Underline", command=self.set_font_underline)
        text_menu.add_command(label="Strike Out", command=self.set_font_overstrike)

        menubar.add_cascade(label="Text", menu=text_menu)

        brush_menu = Menu(root, tearoff=0)

        brush_menu.add_command(label="Set Brush Width", command=self.set_brush_width)

        menubar.add_cascade(label="Pencil Properties", menu=brush_menu)

        root.config(menu=menubar)

        drawing_area = Canvas(root)
        drawing_area.config(background="white")
        drawing_area.pack(anchor=W, fill=BOTH, expand=True, side=LEFT)
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)


root = Tk()
root.geometry("1000x1000")
paint_app = PaintApp(root)
root.mainloop()
