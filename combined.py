from tkinter import *
import sqlite3

root = Tk()
root.title ('Welcom to Team GUI')
root.geometry("700x800")

conn = sqlite3.connect('RentalCar.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER (
			CustID int, 
			Name text,
			Phone text)
			''')
print("Created Customer table successfully.")

c.execute('''CREATE TABLE IF NOT EXISTS VEHICLE (
			VehicleID int, 
			Description text,
			Year int,
			Type int,
			Category int)
			''')
print("Created Vehicle table successfully.")

c.execute('''CREATE TABLE IF NOT EXISTS RENTAL (
			CustID int, 
			VehicleID text,
			StartDate text,
			OrderDate text,
			RentalType text,
			Qty int,
			ReturnDate text,
			TotalAmount int,
			PaymentDate text)
			''')
print("Created Rental table successfully.")

c.execute('''CREATE TABLE IF NOT EXISTS RATE (
			Type int, 
			Category int,
			Weekly int,
			Daily int)
			''')
print("Created Rental table successfully.")


#5a
#list customers
def list_customers():
	conn5 = sqlite3.connect("RentalCar.db")
	c = conn5.cursor()
	list_customer = Tk()
	list_customer.title("List Customer Info")
	c.execute("SELECT CUSTOMER.CustID, Name, RentalBalance FROM CUSTOMER, vRentalInfo ORDER BY RentalBalance")
	result = c.fetchall()

	for index, x in enumerate(result):
		ctr = 0
		for y in x:
			lookup = Label(list_customer, text = x)
			lookup.grid(row=index, column = ctr)
			print(x)
			ctr+=1
	conn5.commit()


def search_customers():
	conn6 = sqlite3.connect("RentalCar.db")
	c = conn6.cursor()
	search_customers = Tk()
	search_customers.title("Search Customers")
	def search_now():
		searching = search_box.get()
		sql = "SELECT CUSTOMER.CustID, Name, RentalBalance FROM CUSTOMER, vRentalInfo WHERE Name = %s"
		Name = (searching, )
		result = c.execute(sql, Name)
		result = c.fetchall()
		print(result)
		print_result = ''

		for results in result:
			print_result += "$"+result[3]

		sql1 = "SELECT CUSTOMER.CustID, Name, RentalBalance FROM CUSTOMER, vRentalInfo WHERE Name = %s"
		Name = (searching, )
		result = c.execute(sql1, Name)
		result=c.fetchall()
		print(result)
		print_result = ''

		for results in result:
			print_result += "$"+result[3]

		sql2 = "SELECT CUSTOMER.CustID, Name, RentalBalance FROM CUSTOMER, vRentalInfo WHERE WHERE CusID = %d"
		id = (searching, )
		result = c.execute(sql2, id)
		result = c.fetchall()
		
		if not result:
			result="Not Found"

		searched_label = Label(search_customers, text = result)
		searched_label.grid(row=2,column=0)

	conn6.commit()

	search_box = Entry(search_customers)
	search_box.grid(row=1,column=0)

	search_box_label = Label(search_customers, text="Search Customer by Last Name")
	search_box_label.grid(row=2,column=0)

	search_button = Button(search_customers, text = "Search Customers", command = search_now)
	search_button.grid(row=3, column=0)

list_customers_button = Button(root, text="List Customers", command=list_customers)
list_customers_button.grid(row=4, column=0)

search_customers_button = Button(root, text = "Search Customers", command=search_customers)
search_customers_button.grid(row = 5, column = 0)


def list_vehicle():
	conn7 = sqlite3.connect("RentalCar.db")
	c = conn7.cursor()
	list_vehicle_query = Tk()
	list_vehicle_query.title("List All Vehicles")
	
	c.execute("SELECT DISTINCT VehicleID, Description, Daily FROM Rate, Vehicle")
	result = c.fetchall()

	for index, x in enumerate(result):
		ctr = 0
		for y in x:
			lookup_label = Label(list_vehicle_query, text = x)
			lookup_label.grid()
			print(x)
			ctr+=1
	
	conn7.commit()

def search_vehicles():
	conn8 = sqlite3.connect("RentalCar.db")
	c = conn8.cursor()
	search_vehicles = Tk()
	search_vehicles.title("Search All Vehicles")
	def search():
		searched = search_box.get()
		sql = "SELECT DISTINCT VehicleID, Description, Daily FROM Rate, Vehicle WHERE VehicleID = %d"
		VehicleID = (searched, )
		result = c.execute(sql, VehicleID)
		result=c.fetchall()

		sql1 = "SELECT DISTINCT VehicleID, Description, Daily FROM Rate, Vehicle WHERE description = %s"
		description = (searched, )
		result = c.execute(sql1, description)
		result=c.fetchall()

		if not result:
			result="Not Found"

		searched_label = Label(search_vehicles, text = result)
		searched_label.grid(row=6,column=0)

		conn8.commit()

	search_box = Entry(search_vehicles)
	search_box.grid(row=7,column=1)

	search_box_label = Label(search_vehicles, text="Search Vehicles by VehicleID")
	search_box_label.grid(row=8,column=0)
	
	search_button = Button(search_vehicles, text = "Search Vehicles", command = search)
	search_button.grid(row=9, column=0)


list_vehicles_button = Button(root, text="List Vehicles", command=list_vehicle)
list_vehicles_button.grid(row=9, column=0)

search_vehicles_button = Button(root, text = "Search Vehicles", command=search_vehicles)
search_vehicles_button.grid(row = 10, column = 0)

conn.commit()
conn.close()

root.mainloop()

