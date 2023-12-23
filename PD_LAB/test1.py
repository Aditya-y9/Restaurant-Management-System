import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("1400x800+260+60")

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
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu (
                item_id INTEGER PRIMARY KEY,
                item_name TEXT UNIQUE,
                item_quantity INTEGER DEFAULT 0,
                item_price REAL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_id TEXT,
                table_number INTEGER,
                payment_method TEXT,
                order_date TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_items (
                order_id INTEGER,
                item_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (item_id) REFERENCES menu(item_id)
            )
        ''')
        self.conn.commit()

    def create_menu_dropdown(self):
        menu_frame = tk.Frame(self.root, width=20)
        menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.menu_var = tk.StringVar()
        menu = tk.Label(text="Restaurant Menu : ", fg="black")
        menu.place(x=10, y=20)
        self.menu_dropdown = ttk.Combobox(menu_frame, textvariable=self.menu_var, state="readonly")
        self.menu_dropdown.grid(row=0, column=0, padx=5)

        self.update_menu_dropdown()

    def update_menu_dropdown(self):
        self.cursor.execute('SELECT item_name FROM menu')
        menu_items = [item[0] for item in self.cursor.fetchall()]
        self.menu_var.set('')
        self.menu_dropdown['values'] = menu_items

    def create_quantity_slider(self):
        slider_frame = tk.Frame(self.root)
        slider_frame.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        quantity = tk.Label(text="Quantity", fg="black")
        quantity.place(x=170, y=20)
        self.quantity_var = tk.IntVar()
        quantity_slider = tk.Spinbox(self.root, from_=1, to=100, width=4, increment=1,
                                     textvariable=self.quantity_var, font=("Arial", 20))

        quantity_slider.grid(row=0, column=0, padx=5)

    def create_add_button(self):
        add_button_frame = tk.Frame(self.root)
        add_button_frame.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        add_button = tk.Button(add_button_frame, text="Add to Order", command=self.add_to_order)
        add_button.grid(row=0, column=0, padx=5)

    def create_order_information(self):
        order_info_frame = tk.Frame(self.root)
        order_info_frame.grid(row=0, column=1, rowspan=5, padx=10, pady=10, sticky=tk.W)

        tk.Label(order_info_frame, text="Order Information").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(order_info_frame, text="Customer ID: 001").grid(row=1, column=0, pady=5)

        tk.Label(order_info_frame, text="Table Number:").grid(row=2, column=0, pady=5)
        self.table_number_var = tk.StringVar()
        table_entry = tk.Entry(order_info_frame, textvariable=self.table_number_var)
        table_entry.grid(row=2, column=1, pady=5)

        tk.Label(order_info_frame, text="Payment Method:").grid(row=3, column=0, pady=5)
        payment_options = ["Cash", "Credit Card", "Debit Card"]
        self.payment_var = tk.StringVar()
        payment_dropdown = ttk.Combobox(order_info_frame, textvariable=self.payment_var, values=payment_options)
        payment_dropdown.grid(row=3, column=1, pady=5)

        tk.Label(order_info_frame, text="Staged Items").grid(row=4, column=0, columnspan=2, pady=10)
        entry = tk.Label(text=(""))
        self.staged_items_listbox = tk.Listbox(order_info_frame, selectmode=tk.SINGLE, font=("Arial", 35))
        self.staged_items_listbox.grid(row=5, column=0, columnspan=2, pady=5)

        tk.Label(order_info_frame, text="Item Name").grid(row=4, column=0, padx=5)
        tk.Label(order_info_frame, text="ID").grid(row=4, column=1, padx=5)
        tk.Label(order_info_frame, text="Price").grid(row=4, column=2, padx=5)
        tk.Label(order_info_frame, text="Quantity").grid(row=4, column=3, padx=5)

        update_button = tk.Button(order_info_frame, text="Update Order", command=self.update_order)
        update_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.total_items_label = tk.Label(order_info_frame, text="Total Items: 0")
        self.total_items_label.grid(row=8, column=0, columnspan=2, pady=5)

        self.total_price_label = tk.Label(order_info_frame, text="Total Price: $0.00")
        self.total_price_label.grid(row=8, column=2, columnspan=2, pady=5)

    def create_pie_chart(self):
        pie_chart_frame = tk.Frame(self.root)
        pie_chart_frame.grid(row=4, column=0, rowspan=5, padx=10, pady=10, sticky=tk.W)

        self.figure, self.ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(aspect="equal"))
        self.pie_chart_canvas = FigureCanvasTkAgg(self.figure, master=pie_chart_frame)
        self.pie_chart_canvas.get_tk_widget().pack(anchor="sw", fill=tk.BOTH, expand=1)

        self.update_pie_chart()

    def add_to_order(self):
        item_name = self.menu_var.get()
        item_quantity = self.quantity_var.get()

        if item_name and item_quantity > 0:
            self.cursor.execute('SELECT item_id, item_price, item_quantity FROM menu WHERE item_name = ?', (item_name,))
            item_id, item_price, remaining_quantity = self.cursor.fetchone()

            if item_quantity > remaining_quantity:
                messagebox.showerror("Error", "Not enough quantity in stock.")
                return

            self.staged_items_listbox.insert(tk.END, (item_name, item_id, item_price, item_quantity))

            self.update_pie_chart()
            self.update_total_labels()

    def update_order(self):
        table_number = self.table_number_var.get()
        payment_method = self.payment_var.get()

        if table_number and payment_method:
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute('INSERT INTO orders (customer_id, table_number, payment_method, order_date) VALUES (?, ?, ?, ?)',
                                ('001', table_number, payment_method, order_date))
            self.conn.commit()

            self.cursor.execute('SELECT last_insert_rowid()')
            order_id = self.cursor.fetchone()[0]

            for item in self.staged_items_listbox.get(0, tk.END):
                _, item_id, _, quantity = item
                self.cursor.execute('INSERT INTO order_items (order_id, item_id, quantity) VALUES (?, ?, ?)',
                                    (order_id, item_id, quantity))

                # Update the quantity in the inventory table
                self.cursor.execute('UPDATE menu SET item_quantity = item_quantity - ? WHERE item_id = ?',
                                    (quantity, item_id))

            self.conn.commit()

            self.staged_items_listbox.delete(0, tk.END)
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
        inventory_frame.grid(row=4, column=5, rowspan=5, padx=10, pady=10, sticky=tk.W)

        tk.Label(inventory_frame, text="Add to Inventory").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(inventory_frame, text="Item Name:").grid(row=1, column=0, pady=5)
        self.new_item_name_var = tk.StringVar()
        new_item_name_entry = tk.Entry(inventory_frame, textvariable=self.new_item_name_var)
        new_item_name_entry.grid(row=1, column=5, pady=5)

        tk.Label(inventory_frame, text="Item Price:").grid(row=2, column=0, pady=5)
        self.new_item_price_var = tk.DoubleVar()
        new_item_price_entry = tk.Entry(inventory_frame, textvariable=self.new_item_price_var)
        new_item_price_entry.grid(row=2, column=5, pady=5)

        tk.Label(inventory_frame, text="Quantity:").grid(row=3, column=0, pady=5)
        self.new_item_quantity_var = tk.IntVar()
        new_item_quantity_entry = tk.Entry(inventory_frame, textvariable=self.new_item_quantity_var)
        new_item_quantity_entry.grid(row=3, column=5, pady=5)

        add_to_inventory_button = tk.Button(inventory_frame, text="Add to Inventory", command=self.add_to_inventory)
        add_to_inventory_button.grid(row=4, column=5, columnspan=2, pady=10)

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

        for item in self.staged_items_listbox.get(0, tk.END):
            _, _, item_price, quantity = item
            total_items += quantity
            total_price += item_price * quantity

        self.total_items_label.config(text=f"Total Items: {total_items}")
        self.total_price_label.config(text=f"Total Price: ${total_price:.2f}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    app.run()
