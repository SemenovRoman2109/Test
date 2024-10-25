import customtkinter

app = customtkinter.CTk()

width = 1300
height = 800
window_width = app.winfo_screenwidth()
window_height = app.winfo_screenheight()
x = int(window_width/2 - width/2)
y = int(window_height/2 - height/2)

app.geometry(f"{width}x{height}+{x}+{y}")