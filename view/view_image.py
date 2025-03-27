from config import *
import config as local

class AnotherWindow:
    def __init__(self,root:CTk|CTkFrame|CTkToplevel,path_image:str|list|tuple=""):
        self.root=root
        util_window.clear_window(self,self.root)
        width,height=1000,750
        self.root.maxsize(width,height)
        self.root.geometry(f"{width}x{height-55}-7+0")
        self.load_resources()
        _status_continue = True
        if len(path_image) <= 1:
            if isinstance(path_image[0], str):
                _name , _extention =os.path.splitext(os.path.basename(path_image[0]))
                if _extention == ".pdf":
                    _sub_list_img = self.pdf_to_img(path_image[0],_name)
                    if not _sub_list_img[0] == None:
                       path_image = _sub_list_img
                    else:
                        _status_continue = False
                        alert = mbox(master=self.root,
                        title="Warning",
                        icon="warning",
                        message=f"{_sub_list_img[1]}", option_1="ok")
                        if alert.get() == "ok":
                            pass
        if  _status_continue:
            self.show_visor()
            self.check_file(path_image)
        else:
            root.destroy()

    def load_resources(self):
        self.List_img=[]
        self.scale=1.0
        self.page_number=0  
        self.page_number_total=0
        self.model_page_actual=StringVar() 
        self.limit_max_scale=3.0
        self.limit_min_scale=0.5

    def show_image(self):
            if not self.List_img==[]:
                self.model_page_actual.set(f"{self.page_number+1}")
                ShowImage=self.List_img[self.page_number]
                if os.path.exists(ShowImage):
                    try:
                        self.img=Image.open(ShowImage)
                        canvas_width=self.Image_container.winfo_width()
                        canvas_height=self.Image_container.winfo_height()
                        img_width,img_height=self.img.size
                        img_width=600 if img_width<100 else img_width
                        img_height=400 if img_height<100 else img_height
                        x_offset=(canvas_width-img_width*self.scale)/2
                        y_offset=(canvas_height-img_height*self.scale)/2
                        self.img=self.img.resize((int(img_width*self.scale),int(img_height*self.scale)))
                        self.img=ImageTk.PhotoImage(self.img)
                        self.Image_container.delete("all")
                        self.Image_container.create_image(x_offset,y_offset,image=self.img,anchor=NW)
                        self.Image_container.configure(scrollregion=self.Image_container.bbox("all"))
                        self.Image_container.update_idletasks()
                    except Exception as ex:
                        print(f"Error loading the image: {ex}")
            else:
                self.root.destroy

    def check_file(self,path:str|list|tuple):
        if isinstance(path,str):
            if os.path.exists(path):
                self.List_self.img[0]=path
                self.page_number_total=len(self.List_self.img)
                self.label_page_number_total.configure(text=f"de {self.page_number_total} pag.")
                self.show_image()

        elif isinstance(path,list) or isinstance(path,tuple):
            self.List_img=[route  for route in path if os.path.exists(route)]
            self.page_number_total=len(self.List_img)
            self.label_page_number_total.configure(text=f"de {self.page_number_total} pag.")
            self.show_image()

    def pdf_to_img(self,path,name_document):
        try:
            document=fitz.open(path)
            path_image=[]

            def process_page(page_number):
                #util_window.modify_bar_msg(self.prog_bar_label, f"please wait... \nGenerating page information. {self.page_number+1}")
                page=document.load_page(page_number)
                pix=page.get_pixmap(matrix=fitz.Matrix(2,2))
                img=Image.frombytes("RGB",[pix.width, pix.height],pix.samples)
                image_ubication=os.path.join('C:/temp_image', f"{name_document}{page_number+1}.png")
                img.save(image_ubication)
                return image_ubication
            with ThreadPoolExecutor() as executor:
                futures=[]
                for page_number in range(len(document)):
                    futures.append(executor.submit(process_page, page_number))
                for future in futures:
                    path_image.append(future.result())
        except Exception as ex:
            path_image=[None,ex]
        finally:
            document.close()
            return path_image

    def update_image(self,event=None):
        self.show_image()

    def print_pdf(pdf_path, printer_name):
        sumatra_path = r"C:\Users\joule\OneDrive\Desktop\practica\image_viewer\SumatraPDF-3.5.2-64.exe"
        command = [sumatra_path, "-print-to", printer_name, pdf_path]

        try:
            subprocess.run(command, check=True)
            print("Print job sent successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error printing file: {e}")

    pdf_file = r"C:\Users\joule\OneDrive\Desktop\practica\image_viewer\asset\icon\pdf\test_pdf.pdf"
    printer = "Microsoft print to PDF"
    print_pdf(pdf_file, printer)

    def print_event(self):
        print(self.List_img[0])
        os.startfile(self.List_img[0],"print")

    def zoomin(self):
        if self.scale<=self.limit_max_scale:
            self.scale=self.scale+0.1
            self.show_image()

    def zoomout(self):
        if self.scale>=self.limit_min_scale:
            self.scale=self.scale-0.1
            self.show_image()

    def Event_Zoom_Mouser(self,event):
        if event.state & 0x4:
            if event.delta > 0 and self.scale < self.limit_max_scale:
                self.scale +=0.1
            elif event.delta < 0 and self.scale > self.limit_min_scale:
                self.scale -=0.1
            self.show_image()

    def start_pan(self,event):
        self.canvas.scan_mark(event.x,event.y)

    def pan_image(self,event):
        self.canvas.scan_dragto(event.x,event.y,gain=1)

    def x_MouseSheet(self,event):
        if event.delta:
            self.Image_container.xview_scroll(int(-1*(event.delta/120)),"units")

    def y_MouseSheet(self,event):
        if event.delta:
            self.Image_container.yview_scroll(int(-1*(event.delta/120)),"units")

    def next_img(self):
        if not self.page_number==[0]:
            self.page_number=(self.page_number+1)% len(self.List_img)
            self.show_image()

    def last_img(self):
        if not self.page_number==[0]:
            self.page_number=(self.page_number-1)% len(self.List_img)
            self.show_image()

    def set_number_pages(self,event=None):
        try:
            _actual_number=int(self.model_page_actual.get())
            if _actual_number>self.page_number_total:
                mbox(master=self.root,
                     title="Warning",
                     icon="warning",
                     message=f"Page {_actual_number} doesn't exist")
            else:
                _actual_number=_actual_number-1
                self.page_number=_actual_number
                self.show_image()
        except Exception as ex:
            print("Error",str(ex))
            self.model_page_actual.set("")

    def show_visor(self):
        self.frame_top=CTkFrame(self.root,bg_color="#256CA9",fg_color="#256CA9",corner_radius=0,height=25,border_width=0)
        self.frame_top.pack(fill="x",side=TOP,pady=(0,0),expand=True)

        CTkButton(
            master=self.frame_top,
            image=local._icon_btn_save,
            command=self.root.destroy,
            compound="left",
            text="Save",
            font=("Arial",12),
            width=60
        ).pack(fill="x",side=RIGHT,padx=(0,5))

        CTkButton(
            master=self.frame_top,
            image=local._icon_btn_print,
            command=self.print_event,
            compound="right",
            text="Print",
            font=("Arial",12),
            width=60
        ).pack(fill="x",side=LEFT,padx=(5,0))
        
        self.frame_bottom=CTkFrame(self.root,bg_color="#256CA9",border_width=0,fg_color="#256CA9",corner_radius=0,height=25)
        self.frame_bottom.pack(fill="x",side=BOTTOM,pady=(0,0),expand=True)

        CTkButton(
            master=self.frame_bottom,
            image=local._icon_btn_left,
            command=self.last_img,
            text="",
            font=("Arial",12),
            width=100
        ).pack(fill="x",side=LEFT,padx=(10,0),expand=True)

        CTkButton(
            master=self.frame_bottom,
            image=local._icon_btn_right,
            command=self.next_img,
            text="",
            font=("Arial",12),
            width=100
        ).pack(fill="x",side=RIGHT,padx=(0,10),expand=True)

        CTkButton(
            master=self.frame_bottom,
            image=local._icon_btn_zoomin,
            command=self.zoomin,
            text="",
            font=("Arial",12),
            width=40
        ).pack(fill="x",side=RIGHT,padx=(0,5))

        CTkButton(
            master=self.frame_bottom,
            image=local._icon_btn_zoomout,
            command=self.zoomout,
            text="",
            font=("Arial",12),
            width=40
        ).pack(fill="x",side=RIGHT,padx=(5,2))

        self.label_page_number_total=CTkLabel(self.frame_bottom,
            text="de 0 pag"
            )

        self.label_page_number_total.pack(fill="x",side=RIGHT,padx=(0,10))
        self.txt_number_page=CTkEntry(self.frame_bottom,
            width=60,
            textvariable=self.model_page_actual
            )

        self.txt_number_page.pack(fill="x",side=RIGHT,padx=(0,10))
        self.txt_number_page.bind("<Return>",self.set_number_pages)

        self.Image_container=CTkCanvas(self.root,bd=0,relief="ridge",width=self.root.winfo_screenmmwidth(),height=748)
        self.Image_container.pack_propagate(0)
        self.Image_container.pack(fill="both",side=LEFT,expand=True)
        
        self.scrolly=CTkScrollbar(self.Image_container,command=self.Image_container.yview,button_hover_color="#256CA9",orientation="vertical")
        self.scrolly.pack(side="right",fill="y")
        self.scrollx=CTkScrollbar(self.Image_container,command=self.Image_container.xview,button_hover_color="#256CA9",orientation="horizontal")
        self.scrollx.pack(side="bottom",fill="x")

        self.Image_container.update()
        self.Image_container.bind("<Left>",self.y_MouseSheet)
        self.Image_container.bind("<Right>",self.x_MouseSheet)
        self.Image_container.bind("<Control-Left>",self.last_img)
        self.Image_container.bind("<Control-Right>",self.next_img)
        self.Image_container.bind("<Configure>",self.update_image)
        self.Image_container.bind("<MouseWheel>",self.y_MouseSheet)
        self.Image_container.configure(yscrollcommand=self.scrolly.set)
        self.Image_container.configure(xscrollcommand=self.scrollx.set)
        self.Image_container.bind("<Shift-MouseWheel>",self.x_MouseSheet)
        self.Image_container.bind("<Control-MouseWheel>",self.Event_Zoom_Mouser)
