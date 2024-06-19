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
        self.show_previous_orders_from_db()

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

        # Create the orders table if it doesn't exist to store the orders
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                order_date TEXT,
                table_number INTEGER,
                payment_method TEXT,
                total_price REAL
            )
        ''')
        self.conn.commit()

    def create_menu_dropdown(self):
        # Create the menu dropdown to select items from
        menu_frame = tk.Frame(self.root, width=20, height=20,border=4,relief="groove",bd=4)
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
        slider_frame = tk.Frame(self.root,border=4,relief="groove",bd=4)
        # left align and create apt spacings
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
        add_button_frame = tk.Frame(self.root,border=4,relief="groove",bd=4)
        add_button_frame.grid(row=3, column=0, padx=20, pady=0, sticky=tk.W)

        add_button = tk.Button(add_button_frame, text="Add to Order", command=self.add_to_order,width=45,fg="white",bg="blue",font=("Arial", 10))
        add_button.grid(row=1, column=1, padx=5,pady=0)

    def create_order_information(self):
        # frame prt
        order_info_frame = tk.Frame(self.root,border=4,relief="groove",bd=4)
        order_info_frame.grid(row=0, column=1, rowspan=5, padx=10, pady=10, sticky=tk.W)

        tk.Label(order_info_frame, text="Order Information",font=("Ariel",15)).grid(row=0, column=0, columnspan=2, pady=10)

        # get date from datetime module
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


        tk.Label(order_info_frame, text="Staged Items",font=("Ariel",8)).grid(row=4, column=0, columnspan=2, pady=10)
        
        # since we cannot provide stlye directly to treeview we need to create a style object
        style = ttk.Style()
        # for heading dark bgcolor
        style.theme_use('clam')

        # configure our style object
        style.configure("Treeview", foreground="green", background="white",font=("Arial", 15),relief="solid",borderwidth=1)

        # get the treeview and provide our style object
        self.staged_items_treeview = ttk.Treeview(order_info_frame, columns=(1, 2, 3, 4), show="headings", height=25, selectmode="browse",style="Treeview") 
        # code to delete the selected item from the treeview
        self.staged_items_treeview.bind("<Delete>", lambda e: self.staged_items_treeview.delete(self.staged_items_treeview.selection()))
        # delete item on click of delete button
        delete_button = tk.Button(order_info_frame, text="Delete Item", command=lambda: self.staged_items_treeview.delete(self.staged_items_treeview.selection()),width=100,fg="white",bg="blue",font=("Arial", 12))
        delete_button.place(x=-20, y=850)
        self.staged_items_treeview.grid(row=5, column=0, columnspan=2, pady=5)

        # put the headings for each column
        self.staged_items_treeview.heading(1, text="Item Name",anchor=tk.W)
        self.staged_items_treeview.heading(2, text="Item ID",anchor=tk.W)
        self.staged_items_treeview.heading(3, text="Item Price",anchor=tk.W)
        self.staged_items_treeview.heading(4, text="Quantity",anchor=tk.W)

        # columns are adjustable

        update_button = tk.Button(order_info_frame, text="Update Order", command=self.update_order,width=90,fg="white",bg="blue",font=("Arial", 12))
        update_button.grid(row=8, column=0, columnspan=2, pady=75)

        # total summary of curr order
        self.total_items_label = tk.Label(order_info_frame, text="Total Items: 0",font=("Arial", 20),pady=20)
        self.total_items_label.place(x=200, y=728)

        self.total_price_label = tk.Label(order_info_frame, text="Total Price: ₹0.00",font=("Arial", 20),pady=20)
        self.total_price_label.place(x=400, y=728)

    def create_pie_chart(self):

        pie_chart_frame = tk.Frame(self.root,border=4,relief="groove",bd=4)
        pie_chart_frame.grid(row=4, column=0, rowspan=5, padx=10, pady=0, sticky=tk.W)

        # pie chart init part using matplotlib
        # create a figure object, which is the window that will contain our pie chart
        self.figure, self.ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(aspect="equal"))

        # create the pie chart
        self.ax.set_title("Pie Chart Title",loc="center")  # Set the title of the pie chart

        # create the canvas that will display the pie chart
        self.pie_chart_canvas = FigureCanvasTkAgg(self.figure, master=pie_chart_frame)

        # display the pie chart on the canvas
        self.pie_chart_canvas.get_tk_widget().pack(anchor="sw", fill=tk.BOTH, expand=1)

        self.update_pie_chart()

    def add_to_order(self):


        # command for add to order button

        # get the item name and quantity from the dropdown and slider
        item_name = self.menu_var.get()
        item_quantity = self.quantity_var.get()


        # check if the item name and quantity are validly enter by the uwer
        if item_name and item_quantity > 0:
            self.cursor.execute('SELECT item_id, item_price, item_quantity FROM menu WHERE item_name = ?',
                                (item_name,))
            
            # fetch item id, price and quantity from the menu table
            item_id, item_price, remaining_quantity = self.cursor.fetchone()

            if item_quantity > remaining_quantity:
                # error if not in stock
                # messagebox pops up on screen
                messagebox.showerror("Error", "Not enough quantity in stock.")
                return
            
            # display in treeview
            self.staged_items_treeview.insert('', tk.END, values=(item_name, item_id, item_price, item_quantity))
            
            # update the total curr at each press of Add button
            self.update_total_labels()

    def update_order(self):
        table_number = self.table_number_var.get()
        payment_method = self.payment_var.get()

        if not table_number or not payment_method:
                messagebox.showerror("Payment incomplete!", "Please enter table number and payment method.")
                return
        
        # update the orders table with the order date, table number, payment method and total price
        self.cursor.execute('INSERT INTO orders (order_date, table_number, payment_method, total_price) VALUES (?, ?, ?, ?)',
                            (datetime.datetime.now(), table_number, payment_method, self.total_price_label.cget("text")[13:]))
        
        # show current sent order dialog box
        messagebox.showinfo("Order Sent!", "Order sent to the kitchen.")
        # give order details in the dialog box
        bill = messagebox.askyesno("Bill", "Do you want to see the bill?")
        if bill:
            # set the title
            # Full printed bill with order details and dishes ordered with quantity, price, and total price
            bill_message = "Order Details:\n\nOrder Date: " + str(datetime.datetime.now()) + "\nTable Number: " + str(table_number) + "\nPayment Method: " + str(payment_method) + "\nTotal Price: " + str(self.total_price_label.cget("text")[13:]) + "\n\nDishes Ordered:\n\n"
            for item in self.staged_items_treeview.get_children():
                item_name = self.staged_items_treeview.item(item, 'values')[0]
                item_quantity = self.staged_items_treeview.item(item, 'values')[3]
                item_price = self.staged_items_treeview.item(item, 'values')[2]
                bill_message += str(item_name) + " " + str(item_quantity) + " " + str(item_price) + " " + "\n"
            bill_message += "\nThank You for your visit!"
            bill = messagebox.showinfo("Bill", bill_message)
        



        # update works ifffff table number and payment method are entered
        if table_number and payment_method:



            self.cursor.execute('SELECT last_insert_rowid()')

            # from treeview get the values of each column
            for item in self.staged_items_treeview.get_children():
                # get the item id and quantity from the treeview
                item_id = self.staged_items_treeview.item(item, 'values')[1]
                quantity = self.staged_items_treeview.item(item, 'values')[3]

                # Update the quantity in the inventory table
                self.cursor.execute('UPDATE menu SET item_quantity = item_quantity - ? WHERE item_id = ?',
                                    (quantity, item_id))
                


            self.conn.commit()

            self.staged_items_treeview.delete(*self.staged_items_treeview.get_children())

            

            # as we have updated the database we need to update the dropdown and pie chart
            self.update_pie_chart()
            self.update_total_labels()

    def update_pie_chart(self):

        # get data from the database
        self.cursor.execute('SELECT item_name, item_quantity FROM menu')
        menu_items = self.cursor.fetchall()

        if not menu_items:
            # if no items in the menu table then return
            return

        # create a list of labels and sizes for the pie chart
        labels = [item[0] for item in menu_items]
        sizes = [item[1] for item in menu_items]

        # clear the pie chart and redraw it with the new data
        self.ax.clear()
        # autopct displays the percentage of each item in the pie chart
        # accuracy of 1 decimal place
        # percentage labels for each
        self.ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        self.ax.axis('equal')
        self.figure.canvas.draw()
        show_previous_orders_button = tk.Button(self.root, text="Show Previous Orders", command=self.show_previous_orders_from_db,width=50,background="blue",fg="white",font=("Arial", 10))
        show_previous_orders_button.place(x=10, y=890)

    def create_previous_orders_section(self):
        # frame prt
        previous_orders_frame = tk.Frame(self.root,border=4,relief="groove",bd=4)
        previous_orders_frame.grid(row=0, column=2, rowspan=1, padx=10, pady=10, sticky=tk.W)

        tk.Label(previous_orders_frame, text="Previous Orders",font=("Ariel",15)).grid(row=0, column=0, columnspan=2, pady=10)

        # get date from datetime module
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")

        tk.Label(previous_orders_frame, text=current_date,font=("Ariel",12)).grid(row=1, column=0, pady=5)
        tk.Label(previous_orders_frame, text="Customer ID: 221080076",font=("Ariel",12)).grid(row=1, column=1, pady=5)


        tk.Label(previous_orders_frame, text="Table Number:",font=("Ariel",12)).grid(row=2, column=0, pady=5)
        self.table_number_var = tk.StringVar()
        table_entry = tk.Entry(previous_orders_frame, textvariable=self.table_number_var)
        table_entry.grid(row=2, column=1, pady=5)


        tk.Label(previous_orders_frame, text="Payment Method:",font=("Ariel",12)).grid(row=3, column=0, pady=5)
        payment_options = ["Cash", "Credit Card", "Debit Card", "UPI", "NEFT", "Net Banking"]
        self.payment_var = tk.StringVar()
        payment_dropdown = ttk.Combobox(previous_orders_frame, textvariable=self.payment_var, values=payment_options, state="readonly")
        payment_dropdown.grid(row=3, column=1, pady=5)


        tk.Label(previous_orders_frame, text="Staged Items",font=("Ariel",8)).grid(row=4, column=0, columnspan=2, pady=10)
        
        # since we cannot provide stlye directly to treeview we need to create a style object
        style = ttk.Style()
        # for heading dark bgcolor
        style.theme_use('clam')

        # configure our style object
        style.configure("Treeview", foreground="green", background="white",font=("Arial", 15),relief="solid",borderwidth=1)

        # get the treeview and provide our style object
        self.staged_items_treeview = ttk.Treeview(previous_orders_frame, columns=(1, 2, 3, 4), show="headings", height=25, selectmode="browse",style="Treeview")


    def show_previous_orders_from_db(self):
        # get the previous orders from the database
        # put summary of each order in our main treeview by changing headings temporarily
        # get from the orders table
        self.cursor.execute('SELECT order_date, table_number, payment_method, total_price FROM orders')
        # fetch all the orders
        orders = self.cursor.fetchall()
        # insert the orders into the treeview
        for order in orders:
            self.staged_items_treeview.insert('', tk.END, values=order)
        # change the headings of the treeview
        self.staged_items_treeview.heading(1, text="Order Date",anchor=tk.W)
        self.staged_items_treeview.heading(2, text="Table Number",anchor=tk.W)
        self.staged_items_treeview.heading(3, text="Payment Method",anchor=tk.W)
        self.staged_items_treeview.heading(4, text="Total Price",anchor=tk.W)
        returnbutton = tk.Button(self.root, text="Return", command=self.return_to_main_treeview,width=50,background="blue",fg="white",font=("Arial", 10))
        returnbutton.place(x=10, y=890)

    def return_to_main_treeview(self):
        # change the headings of the treeview back to normal
        self.staged_items_treeview.heading(1, text="Item Name",anchor=tk.W)
        self.staged_items_treeview.heading(2, text="Item ID",anchor=tk.W)
        self.staged_items_treeview.heading(3, text="Item Price",anchor=tk.W)
        self.staged_items_treeview.heading(4, text="Quantity",anchor=tk.W)
        # delete all the previous orders from the treeview
        self.staged_items_treeview.delete(*self.staged_items_treeview.get_children())
        returnbutton = tk.Button(self.root, text="Show Previous Orders", command=self.show_previous_orders_from_db,width=50,background="blue",fg="white",font=("Arial", 10))
        returnbutton.place(x=10, y=890) 
        
    def create_inventory_section(self):
        inventory_frame = tk.Frame(self.root,border=4,relief="groove",bd=4)
        # sticky nsew to expand the frame in all directions
        inventory_frame.grid(row=2, column=2, rowspan=5, padx=10, pady=10, sticky="nsew")

        tk.Label(inventory_frame, text="Add to Inventory:", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")  

        # tk.W aligns the text to the left
        # labels
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
        new_item_quantity_spinbox.grid(row=3, column=1, pady=5, sticky=tk.W) 



        add_to_inventory_button = tk.Button(inventory_frame, text="Add to Inventory", command=self.add_to_inventory,width=50,background="blue",fg="white",font=("Arial", 10))
        add_to_inventory_button.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.W)  # Update columnspan to 2



    def add_to_inventory(self):
        # on press of add to inventory button

        # get the item name, price and quantity from the entry boxes
        item_name = self.new_item_name_var.get()
        # check if item name already exists
        self.cursor.execute('SELECT item_name FROM menu WHERE item_name = ?', (item_name,))
        if self.cursor.fetchone():
            # if item name already exists then update the quantity
            item_price = self.new_item_price_var.get()
            item_quantity = self.new_item_quantity_var.get()
            self.cursor.execute('UPDATE menu SET item_quantity = item_quantity + ? WHERE item_name = ?',
                                (item_quantity, item_name))
            self.conn.commit()
            # reset the entry boxes
            self.new_item_name_var.set('')
            self.new_item_price_var.set(0.0)
            self.new_item_quantity_var.set(0)
        else:     
            item_price = self.new_item_price_var.get()
            item_quantity = self.new_item_quantity_var.get()

            # check if the item name, price and quantity are valid as entered by the user
            if item_name and item_price and item_quantity:

                # bring in the data from the entry boxes and insert into the menu table
                self.cursor.execute('INSERT INTO menu (item_name, item_price, item_quantity) VALUES (?, ?, ?)',
                                    (item_name, item_price, item_quantity))
                self.conn.commit()
                
                # reset the entry boxes
                self.new_item_name_var.set('')
                self.new_item_price_var.set(0.0)
                self.new_item_quantity_var.set(0)


            # new items!!
            self.update_menu_dropdown()

            # as we changed the database we need to update the pie chart
            self.update_pie_chart()

    def update_total_labels(self):

        # at every instance we check from each dish and update the total items and price
        # therefore starting from 0 each time
        total_items = 0
        total_price = 0.0

        # for all the items in the treeview
        for item in self.staged_items_treeview.get_children():
            # get the price and quantity from the treeview
            item_price = float(self.staged_items_treeview.item(item, "values")[2])
            quantity = int(self.staged_items_treeview.item(item, "values")[3])

            # update the total items and price
            total_items += quantity
            total_price += item_price * quantity

        # confiuure the labels with the new values each time
        self.total_items_label.config(text=f"Total Items: {total_items}")
        self.total_price_label.config(text=f"Total Price: ₹{total_price:.2f}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    app.run()
