'''You can upload an image and use Python to add a watermark logo/text.'''
import os
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox, ttk, colorchooser
from PIL import ImageTk, Image, ImageFont, ImageDraw
from os.path import exists

THEME_COLOR = "#375362"
FONTS = ['arial.ttf','calibril.ttf','consola.ttf','constan.ttf','cour.ttf','georgia.ttf','framd.ttf']

class Image_Watermarking_App:

    def __init__(self):
        self.window = Tk()
        self.window.title("Image Watermarking App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.img_uploaded = None
        self.watermark_txt_uploaded = None
        self.color_code = None

        self.label_player = Label(text="Upload image you want to watermark and watermark image.",fg="white",bg=THEME_COLOR)
        self.label_player.grid(row=0,column=0,columnspan=5)

        self.button1 = Button(text='Upload image', command=self.upload_image)
        self.button1.grid(row=1, column=0)

        self.button3 = Button(text='Create watermark', command=self.watermark, bg='crimson',fg='white')
        self.button3.grid(row=1, column=4)

        self.entry_watermark_text_label = Label(text='Watermark text: ',fg="white",bg=THEME_COLOR)
        self.entry_watermark_text_label.grid(row=2,column=0)
        self.entry_watermark_text = Entry(width=40)
        self.entry_watermark_text.grid(row=2,column=1,columnspan=3)

        self.selected_font = StringVar()
        self.font_cb = ttk.Combobox(textvariable=self.selected_font)
        self.selected_font_size = StringVar()
        self.font_size_cb = ttk.Combobox(textvariable=self.selected_font_size)

        self.font_label = Label(text='Select font, text size and color: ', fg="white", bg=THEME_COLOR)
        self.font_label.grid(row=3, column=0)
        self.font_cb['values'] = FONTS
        self.font_cb['state'] = 'readonly'
        self.font_cb.grid(row=3,column=1)
        self.font_size_cb['values'] = [x for x in range(10,30,2)]
        self.font_size_cb['state'] = 'readonly'
        self.font_size_cb.grid(row=3, column=2)
        self.button_color = Button(text="Select color", command=self.choose_color)
        self.button_color.grid(row=3, column=3)
        self.button_save = Button(text='Save image',command=self.save_img, fg='white', bg='crimson')
        self.button_save.grid(row=6,column=2)
        self.save_img = None

        self.window.mainloop()


    def upload_image(self):
        filename = askopenfilename()
        print(filename)
        self.img_uploaded = filename


    # def upload_watermark(self):
    #     filename = askopenfilename()
    #     print(filename)
    #     self.watermark_img_uploaded = filename

    def choose_color(self):
        self.color_code = colorchooser.askcolor(title="Choose text color")[1]
        print(self.color_code)


    def watermark(self):
        if self.img_uploaded is not None:
            image1 = Image.open(self.img_uploaded)
            uploaded_image = ImageTk.PhotoImage(image1)

            label1 = Label(image=uploaded_image)
            label1.image = uploaded_image
            label1.grid(row=5,column=0,columnspan=5)

            width, height = image1.size

            draw = ImageDraw.Draw(image1)
            text = self.entry_watermark_text.get()

            font = ImageFont.truetype(self.font_cb.get(), int(self.font_size_cb.get()))
            textwidth, textheight = draw.textsize(text, font)

            # calculate the x,y coordinates of the text
            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin

            # draw watermark in the bottom right corner
            draw.text((x, y), text, font=font, fill=self.color_code)
            # image1.show()
            edited_image = ImageTk.PhotoImage(image1)
            label1.configure(image=edited_image)
            label1.image = edited_image

            # Save watermarked image
            self.save_img = image1
            # edited_image.save(self.save_path)
            print('done')

        else:
            messagebox.showerror("showerror", "Upload image and watermark image!")


    def save_img(self):
        path = self.img_uploaded.split('.')
        filename=path[0]+'_copyrighted'+'.'+path[1]
        print(filename)
        if exists(filename):
            os.remove(filename)
        self.save_img.save(filename)
        messagebox.showinfo("showinfo", f"Your image successfully saved to the location:\n{filename}.")




app = Image_Watermarking_App()




