import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime





class RestaurantManagementSystem:
    # initialize the root window, database connection, and cursor, with the UI elements
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("1800x920+70+35")

        self.conn = sqlite3.connect('restaurant.db')
        self.cursor = self.conn.cursor()

        self.create_tables()

        self.create_menu_dropdown()
        self.create_quantity_slider()
        self.create_add_button()
        self.create_order_information()
        self.create_pie_chart()
        self.create_inventory_section()

    def create_tables(self):
        # Create the menu table if it doesn't exist to store curr inventory
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu (
                item_id INTEGER PRIMARY KEY,
                item_name TEXT UNIQUE,
                item_quantity INTEGER DEFAULT 0,
                item_price REAL
            )
        ''')
        self.conn.commit()

    def create_menu_dropdown(self):
        # Create the menu dropdown to select items from
        menu_frame = tk.Frame(self.root, width=20)
        menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # menu_var stores the selected item from the dropdown
        self.menu_var = tk.StringVar()
        menu = tk.Label(text="Restaurant Menu : ", fg="black", font=("Arial", 20))
        menu.place(x=10, y=20)
        # import ttk for the dropdown
        self.menu_dropdown = ttk.Combobox(menu_frame, textvariable=self.menu_var, state="readonly", font=("Arial", 20)  )
        self.menu_dropdown.pack(anchor="sw", fill=tk.BOTH, expand=1,pady=30)

        self.update_menu_dropdown()

    def update_menu_dropdown(self):
        # Update the menu dropdown with the current items in the menu table  from our database
        self.cursor.execute('SELECT item_name FROM menu')
        # fetchall() returns a list of tuples so we need to extract the first element of each tuple
        menu_items = [item[0] for item in self.cursor.fetchall()]
        self.menu_var.set('')
        # set the values of the dropdown to the menu items
        self.menu_dropdown['values'] = menu_items

    def create_quantity_slider(self):
        slider_frame = tk.Frame(self.root)
        slider_frame.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        quantity = tk.Label(text="Quantity : ", fg="black", font=("Arial", 20))
        quantity.place(x=0, y=250)
        # quantity_var stores the quantity selected from the slider
        self.quantity_var = tk.IntVar()

        # Create the slider to select the quantity of the item
        quantity_slider = tk.Spinbox(self.root, from_=1, to=100, width=10, increment=1,
                                     textvariable=self.quantity_var, font=("Arial", 20),state="readonly")

        quantity_slider.grid(row=1, column=0, padx=5)

    def create_add_button(self):
        # Create the add button to add the item to the order curr
        add_button_frame = tk.Frame(self.root)
        add_button_frame.grid(row=3, column=0, padx=20, pady=0, sticky=tk.W)

        add_button = tk.Button(add_button_frame, text="Add to Order", command=self.add_to_order,width=45,fg="white",bg="blue",font=("Arial", 10))
        add_button.grid(row=1, column=1, padx=5,pady=0)

    def create_order_information(self):
        order_info_frame = tk.Frame(self.root)
        order_info_frame.grid(row=0, column=1, rowspan=5, padx=10, pady=10, sticky=tk.W)

        tk.Label(order_info_frame, text="Order Information",font=("Ariel",15)).grid(row=0, column=0, columnspan=2, pady=10)

        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        tk.Label(order_info_frame, text=current_date,font=("Ariel",12)).grid(row=1, column=0, pady=5)
        tk.Label(order_info_frame, text="Customer ID: 221080076",font=("Ariel",12)).grid(row=1, column=1, pady=5)

        tk.Label(order_info_frame, text="Table Number:",font=("Ariel",12)).grid(row=2, column=0, pady=5)
        self.table_number_var = tk.StringVar()
        table_entry = tk.Entry(order_info_frame, textvariable=self.table_number_var)
        table_entry.grid(row=2, column=1, pady=5)

        tk.Label(order_info_frame, text="Payment Method:",font=("Ariel",12)).grid(row=3, column=0, pady=5)
        payment_options = ["Cash", "Credit Card", "Debit Card", "UPI", "NEFT", "Net Banking"]
        self.payment_var = tk.StringVar()
        payment_dropdown = ttk.Combobox(order_info_frame, textvariable=self.payment_var, values=payment_options, state="readonly")
        payment_dropdown.grid(row=3, column=1, pady=5)
        payment_dropdown.grid(row=3, column=1, pady=5)

        tk.Label(order_info_frame, text="Staged Items",font=("Ariel",8)).grid(row=4, column=0, columnspan=2, pady=10)
        entry = tk.Label(text=(""))
        style = ttk.Style()
        # for heading dark bgcolor
        style.theme_use('clam')
        style.configure("Treeview", foreground="green", background="white",font=("Arial", 15),relief="solid",borderwidth=1)
        self.staged_items_treeview = ttk.Treeview(order_info_frame, columns=(1, 2, 3, 4), show="headings", height=25, selectmode="browse",style="Treeview") 
        self.staged_items_treeview.grid(row=5, column=0, columnspan=2, pady=5)
        self.staged_items_treeview.heading(1, text="Item Name",anchor=tk.W)
        self.staged_items_treeview.heading(2, text="Item ID",anchor=tk.W)
        self.staged_items_treeview.heading(3, text="Item Price",anchor=tk.W)
        self.staged_items_treeview.heading(4, text="Quantity",anchor=tk.W)

        update_button = tk.Button(order_info_frame, text="Update Order", command=self.update_order,width=90,fg="white",bg="blue",font=("Arial", 12))
        update_button.grid(row=8, column=0, columnspan=2, pady=75)

        self.total_items_label = tk.Label(order_info_frame, text="Total Items: 0",font=("Arial", 20),pady=20)
        self.total_items_label.place(x=200, y=728)

        self.total_price_label = tk.Label(order_info_frame, text="Total Price: ₹0.00",font=("Arial", 20),pady=20)
        self.total_price_label.place(x=400, y=728)

    def create_pie_chart(self):
        pie_chart_frame = tk.Frame(self.root)
        pie_chart_frame.grid(row=4, column=0, rowspan=5, padx=10, pady=0, sticky=tk.W)

        self.figure, self.ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(aspect="equal"))
        self.ax.set_title("Pie Chart Title",loc="center")  # Set the title of the pie chart
        self.pie_chart_canvas = FigureCanvasTkAgg(self.figure, master=pie_chart_frame)
        self.pie_chart_canvas.get_tk_widget().pack(anchor="sw", fill=tk.BOTH, expand=1)

        self.update_pie_chart()

    def add_to_order(self):
        item_name = self.menu_var.get()
        item_quantity = self.quantity_var.get()

        if item_name and item_quantity > 0:
            self.cursor.execute('SELECT item_id, item_price, item_quantity FROM menu WHERE item_name = ?',
                                (item_name,))
            item_id, item_price, remaining_quantity = self.cursor.fetchone()

            if item_quantity > remaining_quantity:
                messagebox.showerror("Error", "Not enough quantity in stock.")
                return

            self.staged_items_treeview.insert('', tk.END, values=(item_name, item_id, item_price, item_quantity))

            self.update_pie_chart()
            self.update_total_labels()

    def update_order(self):
        table_number = self.table_number_var.get()
        payment_method = self.payment_var.get()

        if table_number and payment_method:
            self.cursor.execute('SELECT last_insert_rowid()')
            order_id = self.cursor.fetchone()[0]

            for item in self.staged_items_treeview.get_children():
                item_id = self.staged_items_treeview.item(item, 'values')[1]
                quantity = self.staged_items_treeview.item(item, 'values')[3]
                # Update the quantity in the inventory table
                self.cursor.execute('UPDATE menu SET item_quantity = item_quantity - ? WHERE item_id = ?',
                                    (quantity, item_id))

            self.conn.commit()

            self.staged_items_treeview.delete(*self.staged_items_treeview.get_children())
            self.update_pie_chart()
            self.update_total_labels()

    def update_pie_chart(self):
        self.cursor.execute('SELECT item_name, item_quantity FROM menu')
        menu_items = self.cursor.fetchall()

        if not menu_items:
            return

        labels = [item[0] for item in menu_items]
        sizes = [item[1] for item in menu_items]

        self.ax.clear()
        self.ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        self.ax.axis('equal')
        self.figure.canvas.draw()

    def create_inventory_section(self):
        inventory_frame = tk.Frame(self.root)
        inventory_frame.grid(row=2, column=2, rowspan=5, padx=10, pady=10, sticky="nsew")  # Update column to 0

        tk.Label(inventory_frame, text="Add to Inventory:", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")  

        tk.Label(inventory_frame, text="Item Name:",font=("Ariel",10)).grid(row=1, column=0, pady=5, sticky=tk.W)  # Update column to 0
        self.new_item_name_var = tk.StringVar()
        new_item_name_entry = tk.Entry(inventory_frame, textvariable=self.new_item_name_var, font=("Arial", 20))
        new_item_name_entry.grid(row=1, column=1, pady=5, sticky=tk.W)  # Update column to 1

        tk.Label(inventory_frame, text="Item Price:",font=("Ariel",10)).grid(row=2, column=0, pady=5, sticky=tk.W)  # Update column to 0
        self.new_item_price_var = tk.DoubleVar()
        new_item_price_entry = tk.Entry(inventory_frame, textvariable=self.new_item_price_var, font=("Arial", 20))
        new_item_price_entry.grid(row=2, column=1, pady=5, sticky=tk.W)  # Update column to 1

        tk.Label(inventory_frame, text="Quantity:",font=("Ariel",10)).grid(row=3, column=0, pady=5, sticky=tk.W)  # Update column to 0
        self.new_item_quantity_var = tk.IntVar()
        new_item_quantity_spinbox = tk.Spinbox(inventory_frame, from_=1, to=100, width=4, increment=1,
                                               textvariable=self.new_item_quantity_var, font=("Arial", 20), state="readonly")
        new_item_quantity_spinbox.grid(row=3, column=1, pady=5, sticky=tk.W)  # Update column to 1

        add_to_inventory_button = tk.Button(inventory_frame, text="Add to Inventory", command=self.add_to_inventory,width=50,background="blue",fg="white",font=("Arial", 10))
        add_to_inventory_button.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.W)  # Update columnspan to 2

    def add_to_inventory(self):
        item_name = self.new_item_name_var.get()
        item_price = self.new_item_price_var.get()
        item_quantity = self.new_item_quantity_var.get()

        if item_name and item_price and item_quantity:
            self.cursor.execute('INSERT INTO menu (item_name, item_price, item_quantity) VALUES (?, ?, ?)',
                                (item_name, item_price, item_quantity))
            self.conn.commit()

            self.new_item_name_var.set('')
            self.new_item_price_var.set(0.0)
            self.new_item_quantity_var.set(0)

            self.update_menu_dropdown()
            self.update_pie_chart()

    def update_total_labels(self):
        total_items = 0
        total_price = 0.0

        for item in self.staged_items_treeview.get_children():
            item_price = float(self.staged_items_treeview.item(item, "values")[2])
            quantity = int(self.staged_items_treeview.item(item, "values")[3])
            total_items += quantity
            total_price += item_price * quantity

        self.total_items_label.config(text=f"Total Items: {total_items}")
        self.total_price_label.config(text=f"Total Price: ₹{total_price:.2f}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    app.run()
