import tkinter as tk
from tkinter import ttk
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
        menu_frame = tk.Frame(self.root)
        menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.menu_var = tk.StringVar()
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

        self.quantity_var = tk.IntVar()
        quantity_slider = tk.Scale(slider_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.quantity_var, label="Quantity")
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

        self.staged_items_listbox = tk.Listbox(order_info_frame, selectmode=tk.SINGLE, height=30, width=80)
        self.staged_items_listbox.grid(row=5, column=0, columnspan=2, pady=5)

        tk.Label(order_info_frame, text="Item Name").grid(row=6, column=0, padx=5)
        tk.Label(order_info_frame, text="ID").grid(row=6, column=1, padx=5)
        tk.Label(order_info_frame, text="Price").grid(row=6, column=2, padx=5)
        tk.Label(order_info_frame, text="Quantity").grid(row=6, column=3, padx=5)

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
        menu_item = self.menu_var.get()
        quantity = self.quantity_var.get()

        if menu_item and quantity > 0:
            self.cursor.execute('SELECT item_id, item_price FROM menu WHERE item_name = ?', (menu_item,))
            item_details = self.cursor.fetchone()

            if item_details:
                item_id, item_price = item_details
                self.staged_items_listbox.insert(tk.END, (menu_item, item_id, item_price, quantity))
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

            self.conn.commit()

            self.staged_items_listbox.delete(0, tk.END)
            self.update_pie_chart()
            self.update_total_labels()

    def update_pie_chart(self):
        self.cursor.execute('''
            SELECT menu.item_name, SUM(order_items.quantity) 
            FROM menu 
            JOIN order_items ON menu.item_id = order_items.item_id 
            GROUP BY menu.item_name
        ''')
        data = self.cursor.fetchall()

        labels = [item[0] for item in data]
        quantities = [item[1] for item in data]

        self.ax.clear()
        self.ax.pie(quantities, labels=labels, autopct='%1.1f%%', startangle=90)
        self.pie_chart_canvas.draw()

    def update_total_labels(self):
        total_items = 0
        total_price = 0.0

        for item in self.staged_items_listbox.get(0, tk.END):
            _, _, item_price, quantity = item
            total_items += quantity
            total_price += item_price * quantity

        self.total_items_label.config(text=f"Total Items: {total_items}")
        self.total_price_label.config(text=f"Total Price: ${total_price:.2f}")

    def create_inventory_section(self):
        inventory_frame = tk.Frame(self.root)
        inventory_frame.grid(row=0, column=5, rowspan=5, padx=10, pady=10, sticky=tk.W)

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
        new_item_name = self.new_item_name_var.get()
        new_item_price = self.new_item_price_var.get()
        new_item_quantity = self.new_item_quantity_var.get()

        if new_item_name and new_item_price and new_item_quantity > 0:
            self.cursor.execute('INSERT OR IGNORE INTO menu (item_name, item_price) VALUES (?, ?)', (new_item_name, new_item_price))
            self.conn.commit()

            self.update_menu_dropdown()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    app.run()
