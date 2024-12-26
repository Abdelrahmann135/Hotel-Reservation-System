import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
from GUI import HotelReservationApp

if __name__ == '__main__':
    root = tk.Tk()
    app = HotelReservationApp(root)
    root.mainloop()
