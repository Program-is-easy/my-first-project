import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Welcome")

label.grid()

print("hello")

count = {
    "i":1
}

def fun():
    if count["i"] %2 == 1:
        print("меня нажали 1 раз")
    else:
        print("меня нажали 2 раз")
    count["i"] = count["i"] + 1  

def fun1():
    fun()


btn = tk.Button(root, text="click me", command=fun1)
btn.grid()


root.mainloop()