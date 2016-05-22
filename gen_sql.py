from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import PhotoImage
import os
import csv


class Window():

    def __init__(self, root):

        self.f = Frame(root)
        self.f.grid(row=3, column=2, rowspan=4, columnspan=5)
        self.f.pack()
        root.title("Generardo de Archivo SQL")
        self.l1=Label(self.f, text="Nombre de la base de datos :").grid(row=0,sticky=(W,E))
        self.l2=Label(self.f, text="Archivo :").grid(row=1,sticky=(W,E),padx=5,pady=2)
        self.l3=Label(self.f, text="Nombre de la tabla que deseas crear :").grid(row=3,sticky=(W,E),padx=5,pady=2)
        self.e1 = Entry(self.f, width = 20)
        self.e2 = Entry(self.f, width = 20)
        self.e3 = Entry(self.f, width = 20)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=3, column=1)
        
        #Code for menu:
        
        menubar = Menu(root)
        iniciomenu = Menu(menubar, tearoff=0)
        iniciomenu.add_command(label="Cargar Archivo", command=lambda: self.uploadFile())
        iniciomenu.add_command(label="Abrir Archivo", command=lambda: self.onOpen())
        iniciomenu.add_command(label="Actualizar Campos", command=lambda: self.OK())
        iniciomenu.add_separator()
        iniciomenu.add_command(label="Salir", command=root.destroy)
        menubar.add_cascade(label="Inicio", menu=iniciomenu)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="About me ", command=lambda: self.aboutme())
        menubar.add_cascade(label="Ayuda", menu=filemenu)
        root.config(menu=menubar)
        self.b = Button(self.f, width = 15, text = "Procesar", command = lambda: self.eject()).grid(row=8, column=0, sticky=(W,E),padx=5,pady=2)
        self.f.pack()

    def OK(self):
        self.newWindow=Toplevel()
        self.app=Window2(self.newWindow)
        #print (self.cabecera)

    def uploadFile(self):
        self.e2.delete(0,END)
        self.filename=askopenfilename()
        self.e2.insert(0,self.filename)
        print (self.filename)

    def abrir_archivo (self):
        name=self.e2.get()
        print (name)
        f=open(name,encoding="utf-8-sig")
        red=f.readlines()
        for x in red:
            cabecera=(x)
            break
        self.cabecera= cabecera.rsplit(";")
        cabecera=[x.rsplit("\n")[0] for x in cabecera]
        return self
                             
    def aboutme(self):
        top = Toplevel()
        top.geometry('100x100')
        to.pack()
        top.title("Acerca de mi")
        msg = Message(top, text="Esta Aplicacion")
        msg.pack()
        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()

    def onOpen(self):
        os.system('salida.sql')
        
                             
    def eject(self):
        if self.e1.get()=="":
             messagebox.showinfo("Mensaje", "Te Falta Asignar el Esquema de la Base de datos")
        else:
            if self.e3.get()=="":
                messagebox.showinfo("Mensaje", "Te Falta Asignar el Nombre de la BD que crearas")
            else:
                self.abrir_archivo()
                print (self.cabecera)
                sal=open('salida.sql','w')
                sal.truncate()
                sal.write("raiserror('Oh no a fatal error', 20, -1) with log;")
                for x in range(2):
                    sal.write("\n")
                self.db=self.e1.get()
                self.tablacrear=self.e2.get()
                sal.write("USE "+self.db+";")
                for x in range(2):
                    sal.write("\n")
                sal.write("--Generar código para crear la tabla mediante el wizard")
                sal.write("\n")
                sal.write("--drop table [dbo]."+self.tablacrear+"\n")
                sal.write("CREATE TABLE [dbo]."+self.tablacrear+"(\n")
                for x in range(len(self.cabecera)):
                    if x<len(self.cabecera)-1:
                        sal.write(self.cabecera[x]+" varchar (50),\n")
                    else:
                        sal.write(self.cabecera[x]+" varchar (50)\n")
                sal.write(");\n")
                sal.write("\n")
                sal.write("--Adaptar TABLA y file\n")
                sal.write("BULK INSERT ["+self.tablacrear+"]\n"+ "FROM '"+self.e2.get()+"'\n"+"WITH(\n"+ "DATAFILETYPE = \'char\'"+",--FIELDTERMINATOR = \'"+"\\t"+"\',\nFIELDTERMINATOR = \';\',KEEPNULLS,FIRSTROW = 2)")
                messagebox.showinfo("Mensaje", "Se ha creado exitosamente tu archivo")

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Open...', command=self.notdone)
        pulldown.add_command(label='Quit',    command=self.quit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)
    

    def newWindow(self):
        master = Tk()
        def var_states():
            print(box_vars[0].get(), box_vars[1].get())

        premadeList=["male","famale"]
        box_vars=[]
        box_num=0
        for checkBoxName in range(len(premadeList)):
            box_vars.append(IntVar())
            c = Checkbutton(master, text=premadeList[checkBoxName],variable=box_vars[box_num])
            c.pack()
            box_num+=1
        Button(master, text='Quit', command=master.quit).pack()
        Button(master, text='Show', command=lambda: var_states()).pack()
        master.mainloop()

        """def done(newWindow):

            newWindow.destroy()
        def chkbox_checked(text):
            return lambda : j.append(text)

        def seleccionados():
            print (box_vars[0].get())
           
            
        
        master = Tk()
        premadeList=(self.cabecera)
        boxes=[]
        box_vars=[]
        box_num=0     #<- Count the number of vars
        for checkBoxName in range(len(premadeList)):
            box_vars.append(IntVar())
            c = Checkbutton(master, text=premadeList[checkBoxName],variable=box_vars[box_num])
            c.pack()
            box_num+=1
        button = Button(master, text="Datos Actualizar", command=lambda: seleccionados()).pack()
        
        
        
        print ((box_vars[0].get()))
        box_vars.append(IntVar())
        chk=Checkbutton(newWindow, text="prueba",variable=box_vars[0])
        chk.pack()
        print (box_vars[0].get())
        
        mainloop()"""
class Window2():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
        
root= Tk()
root.geometry('{}x{}'.format(400,130))
#root.wm_iconbitmap(bitmap=r"logo.ico")
w = Window(root)
w.f.mainloop() 
