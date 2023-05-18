from tkinter import*
class Tablero(Tk):
    def _init_(self,*args,**kgargs):
        super().__init__(*args,**kgargs)
        self.geometry("640*640+500+150")
        self.tablero=Canvas(self)
        self.tablero.pack(fill="both",expand=1)
if __name__=="_main_":
    app=Tablero()
    app.mainloop()
