import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
from Connection import make_connection

cursor = make_connection()
class HotelReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Reservation System")
        self.root.geometry("1300x700")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("breeze")
        self.create_gui()


    def create_gui(self):
        tab_control = ttk.Notebook(self.root)


        self.guest_tab = ttk.Frame(tab_control, padding=10)
        self.room_tab = ttk.Frame(tab_control, padding=10)
        self.booking_tab = ttk.Frame(tab_control, padding=10)
        self.service_tab = ttk.Frame(tab_control, padding=10)

        tab_control.add(self.guest_tab, text='Guests')
        tab_control.add(self.room_tab, text='Rooms')
        tab_control.add(self.booking_tab, text='Bookings')
        tab_control.add(self.service_tab, text='Services')
        tab_control.pack(expand=1, fill='both')


        self.guest_management()
        self.room_management()
        self.service_management()
        self.booking_management()

    def create_title_label(self, frame, text, y=10):
        title_label = ttk.Label(frame, text=text, font=("Helvetica", 20, "bold"), foreground="#333")
        title_label.grid(row=0, column=0, columnspan=2, pady=y)

    def guest_management(self):
        frame = self.guest_tab

        self.create_title_label(frame, "Guest Management", y=30)

        ttk.Label(frame, text="First Name", font=("Helvetica", 12)).grid(row=1, column=0, padx=70, pady=5, sticky="w")
        self.fname = ttk.Entry(frame, width=30)
        self.fname.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Last Name", font=("Helvetica", 12)).grid(row=2, column=0, padx=70, pady=5, sticky="w")
        self.lname = ttk.Entry(frame, width=30)
        self.lname.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Phone", font=("Helvetica", 12)).grid(row=3, column=0, padx=70, pady=5, sticky="w")
        self.phone = ttk.Entry(frame, width=30)
        self.phone.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Email", font=("Helvetica", 12)).grid(row=4, column=0, padx=70, pady=5, sticky="w")
        self.email = ttk.Entry(frame, width=30)
        self.email.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Address", font=("Helvetica", 12)).grid(row=5, column=0, padx=70, pady=5, sticky="w")
        self.address = ttk.Entry(frame, width=30)
        self.address.grid(row=5, column=1, padx=10, pady=5)

        ttk.Button(frame, text="Add Guest", command=self.add_guest).grid(row=7, column=0, pady=20)
        ttk.Button(frame, text="Show Guests", command=self.show_guests).grid(row=7, column=1, pady=20)


        self.guest_table = ttk.Treeview(frame, columns=("ID", "First Name", "Last Name", "Phone", "Email", "Address"), show='headings')
        self.guest_table.heading("ID", text="Guest ID")
        self.guest_table.heading("First Name", text="First Name")
        self.guest_table.heading("Last Name", text="Last Name")
        self.guest_table.heading("Phone", text="Phone")
        self.guest_table.heading("Email", text="Email")
        self.guest_table.heading("Address", text="Address")
        self.guest_table.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def add_guest(self):
        query = "INSERT INTO Guest (f_name, l_name, phone, email, address) VALUES (?, ?, ?, ?, ?)"
        params = (
            self.fname.get(),
            self.lname.get(),
            self.phone.get(),
            self.email.get(),
            self.address.get()
        )
        cursor.execute(query, params)
        messagebox.showinfo("Success", "Guest added successfully!")

    def show_guests(self):
        query = "SELECT * FROM Guest WHERE email = (?)"
        email = self.email.get()
        rows = cursor.execute(query, (email,))
        for item in self.guest_table.get_children():
            self.guest_table.delete(item)
        for row in rows:
            row = (
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )
            self.guest_table.insert("", "end", values=row)

    def room_management(self):
        frame = self.room_tab
        self.create_title_label(frame, "Room Management",y=50)
        ttk.Label(frame, text="Room Type", font=("Helvetica", 12)).grid(row=1, column=0, padx=100, pady=10, sticky="w")
        self.room_type = ttk.Entry(frame, width=30)
        self.room_type.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Status", font=("Helvetica", 12)).grid(row=2, column=0, padx=100, pady=10, sticky="w")
        self.status = ttk.Entry(frame, width=30)
        self.status.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Price", font=("Helvetica", 12)).grid(row=3, column=0, padx=100, pady=10, sticky="w")
        self.room_price = ttk.Entry(frame, width=30)
        self.room_price.grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(frame, text="Add Room", command=self.add_room).grid(row=4, column=0, pady=20)
        ttk.Button(frame, text="Show Rooms", command=self.show_rooms).grid(row=4, column=1, pady=20)

        self.room_table = ttk.Treeview(frame, columns=("Room Number", "Type", "Status", "Price"), show='headings')
        self.room_table.heading("Room Number", text="Room Number")
        self.room_table.heading("Type", text="Type")
        self.room_table.heading("Status", text="Status")
        self.room_table.heading("Price", text="Price")
        self.room_table.grid(row=5, column=0, columnspan=2, padx=230, pady=10)

    def add_room(self):
        query = "INSERT INTO Rooms (room_type, status, price) VALUES (?, ?, ?)"
        params = (self.room_type.get(), self.status.get(), self.room_price.get())
        cursor.execute(query, params)
        messagebox.showinfo("Success", "Room added successfully!")

    def show_rooms(self):
        query = "SELECT * FROM Rooms WHERE status = (?)"
        rows = cursor.execute(query, ('Available',))
        for item in self.room_table.get_children():
            self.room_table.delete(item)
        for row in rows:
            row = (
            row[0],
            row[1],
            row[2],
            f"{int(row[3])}")
            self.room_table.insert("", "end", values=row)

    def service_management(self):
        frame = self.service_tab
        self.create_title_label(frame, "Service Management",y=60)

        ttk.Label(frame, text="Service Name", font=("Helvetica", 12)).grid(row=1, column=0, padx=120, pady=10, sticky="w")
        self.service_name = ttk.Entry(frame, width=30)
        self.service_name.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Price", font=("Helvetica", 12)).grid(row=2, column=0, padx=120, pady=10, sticky="w")
        self.service_price = ttk.Entry(frame, width=30)
        self.service_price.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(frame, text="Add Service", command=self.add_service).grid(row=3, column=0, pady=20)
        ttk.Button(frame, text="Show Services", command=self.show_services).grid(row=3, column=1, pady=20)

        self.service_table = ttk.Treeview(frame, columns=("Service ID", "Name", "Price"), show='headings')
        self.service_table.heading("Service ID", text="Service ID")
        self.service_table.heading("Name", text="Name")
        self.service_table.heading("Price", text="Price")
        self.service_table.grid(row=4, column=0, columnspan=2, padx=300, pady=10)

    def add_service(self):
        query = "INSERT INTO Services (service_name, price) VALUES (?, ?)"
        params = (self.service_id.get(), self.service_name.get(), self.service_price.get())
        cursor.execute(query, params)
        messagebox.showinfo("Success", "Service added successfully!")

    def show_services(self):
        query = "SELECT * FROM Services"
        rows = cursor.execute(query)
        for item in self.service_table.get_children():
            self.service_table.delete(item)
        for row in rows:
            row = (
                row[0],
                row[1],
                f"{int(row[2])}"
            )
            self.service_table.insert("", "end", values=row)

    def booking_management(self):
        frame = self.booking_tab
        self.create_title_label(frame, "Booking Management",y=50)

        ttk.Label(frame, text="Guest email", font=("Helvetica", 12)).grid(row=1, column=0, padx=70, pady=10, sticky="w")
        self.booking_guest_email = ttk.Entry(frame, width=30)
        self.booking_guest_email.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Room Number", font=("Helvetica", 12)).grid(row=2, column=0, padx=70, pady=10, sticky="w")
        self.booking_room_num = ttk.Entry(frame, width=30)
        self.booking_room_num.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Check-Out Date", font=("Helvetica", 12)).grid(row=3, column=0, padx=70, pady=10, sticky="w")
        self.check_out_date = ttk.Entry(frame, width=30)
        self.check_out_date.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Service id", font=("Helvetica", 12)).grid(row=4, column=0, padx=70, pady=10, sticky="w")
        self.service_id = ttk.Entry(frame, width=30)
        self.service_id.grid(row=4, column=1, padx=10, pady=5)


        ttk.Button(frame, text="Add Booking", command=self.add_booking).grid(row=5, column=0, pady=20)
        ttk.Button(frame, text="Show Bookings", command=self.show_bookings).grid(row=5, column=1, pady=20)

        self.booking_table = ttk.Treeview(frame,
                                          columns=("Booking ID", "Check-In", "Check-Out", "Room Number", "Guest ID"),
                                          show='headings'
                                          )
        self.booking_table.heading("Booking ID", text="Booking ID")
        self.booking_table.heading("Check-In", text="Check-In Date")
        self.booking_table.heading("Check-Out", text="Check-Out Date")
        self.booking_table.heading("Room Number", text="Room Number")
        self.booking_table.heading("Guest ID", text="Guest ID")
        self.booking_table.grid(row=6, column=0, columnspan=2, padx=140, pady=10)

    def add_booking(self):
        insert_query = """
        INSERT INTO Billing (cost)
        OUTPUT INSERTED.bill_id
        VALUES (?);
        """
        cursor.execute(insert_query, (0,))
        bill_id = cursor.fetchone()[0]
        print(f"Generated Bill ID: {bill_id}")

        query = "SELECT guest_id from Guest WHERE email = (?)"
        params = (
            self.booking_guest_email.get(),
        )
        cursor.execute(query, params)
        guest_id = cursor.fetchone()[0]
        print(guest_id)


        query = "INSERT INTO Booking (bill_id, guest_id, room_num) OUTPUT INSERTED.booking_id VALUES (?, ?, ?);"
        params = (
            bill_id,
            guest_id,
            self.booking_room_num.get(),
        )
        cursor.execute(query, params)
        booking_id = cursor.fetchone()[0]
        print(f"Generated Booking ID: {booking_id}")

        query = "UPDATE Rooms SET status = (?) WHERE room_num = (?)"
        status = 'Booked'
        params = (
            status,
            self.booking_room_num.get(),
        )
        cursor.execute(query, params)

        query = "INSERT INTO Chossed_services(service_id, booking_id) values(?, ?)"
        params = (
            self.service_id.get(),
            booking_id,
        )
        cursor.execute(query, params)
        print("success")

        query = """
        update Billing 
        set cost = (select price from Rooms where room_num = ?)
        + (select price from Services where service_id = ?) 
        * (select count(service_id) from Chossed_services where booking_id = ?)
        where bill_id = ?;
        update Billing 
        set payment_status = 'Payed'
        where bill_id = ?
"""
        params = (
            self.booking_room_num.get(),
            self.service_id.get(),
            booking_id,
            bill_id,
            bill_id
        )
        cursor.execute(query, params)
        messagebox.showinfo("Success", "Booking added successfully!")

    def show_bookings(self):
        query = "SELECT guest_id from Guest WHERE email = (?)"
        params = (
            self.booking_guest_email.get(),
        )
        cursor.execute(query, params)
        guest_id = cursor.fetchone()[0]
        print(guest_id)
        query = "SELECT * FROM Booking WHERE guest_id = (?)"
        params = (
            guest_id,
        )
        rows = cursor.execute(query, params)
        for item in self.booking_table.get_children():
            self.booking_table.delete(item)
        for row in rows:
            row = (
                row[0],
                row[1],
                row[2],
                row[4],
                row[5]
            )
            self.booking_table.insert("", "end", values=row)

