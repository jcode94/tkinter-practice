import sympy as sp
import tkinter as tk
from io import StringIO
from PIL import Image, ImageTk

x, y = sp.symbols('x,y')
expr = sp.sin(sp.sqrt(x**2 + 20)) + y
# OR
# expr = r'$$\int_0^1 e^x\,dx$$'

f = StringIO()
sp.preview(expr, viewer='StringIO', outputbuffer=f)
f.seek(0)
root = tk.Tk()
img = Image.open(f)
pimg = ImageTk.PhotoImage(img)
lbl = tk.Label(image=pimg)
lbl.pack()
root.mainloop()
