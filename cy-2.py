#frame for encode page
def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root)
        label1= Label(F2,text='Select the Image in which \n you want to hide text :')
        label1.config(font=('Times new roman',25, 'bold'),bg = '#e3f4f1')
        label1.grid()
 
        button_bws = Button(F2,text='Select',command=lambda : self.encode_frame2(F2))
        button_bws.config(font=('Helvetica',18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
        button_back.config(font=('Helvetica',18),bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        F2.grid()
 
#frame for decode page
def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        lablel1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman',25,'bold'),bg = '#e3f4f1')
        label1.grid()
        label1.config(bg = '#e3f4f1')
        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
        button_bws.config(font=('Helvetica',18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.config(font=('Helvetica',18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()