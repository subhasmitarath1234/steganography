#main frame or start page
def main(self, root):
        root.title('ImageSteganography by DataFlair')
        root.geometry('500x600')
        root.resizable(width =False, height=False)
        root.config(bg = '#e3f4f1')
        frame = Frame(root)
        frame.grid()
       
        title = Label(frame,text='DataFlair Image Steganography')
        title.config(font=('Times new roman',25, 'bold'),bg = '#e3f4f1')
        title.grid(pady=10)
        title.grid(row=1)
 
        encode = Button(frame,text="Encode",command= lambda :self.encode_frame1(frame), padx=14,bg = '#e3f4f1' )
        encode.config(font=('Helvetica',14), bg='#e8c1c7')
        encode.grid(row=2)
        decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), padx=14,bg = '#e3f4f1')
        decode.config(font=('Helvetica',14), bg='#e8c1c7')
        decode.grid(pady = 12)
        decode.grid(row=3)
 
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)