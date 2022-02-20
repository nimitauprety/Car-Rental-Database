from tkinter import *
import sqlite3

root = Tk()
root.title ('Welcom to Team GUI')
root.geometry("400x400")

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

conn.commit()
conn.close()

#5a
#list customers
def list_customers():
	list_customer_query = Tk()
	list_customer_query.title("List All Customer")
	list_customer_query.geometry("800x600")
	c.execute("SELECT CUSTOMER.CustID, Name, RentalBalance FROM CUSTOMER, vRentalInfo ORDER BY RentalBalance")
	result = c.fetchall()

	for index, x in enumerate(result):
		num = 0
		for y in x:
			lookup_label = Label(list_customer_query, text = x)
			lookup_label.grid()
			print(x)
			num+=1

def search_customers():
	search_customers = Tk()
	search_customers.title("Search Customers")
	search_customers.geometry("800x600")
	def search_now():
		searched = search_box.get()
		sql = "SELECT CUSTOMER.CustID, Name, RentalBalance FROM CUSTOMER, vRentalInfo WHERE last_name = %s"
		last_name = (searched, )
		result = c.execute(sql, last_name)
		result = c.fetchall()
		print(result)
		print_result = ''

		for results in result:
			print_result += "$"+result[3]

		sql1 = "SELECT CUSTOMER.CustID, Name, RentalBalance FROM CUSTOMER, vRentalInfo WHERE first_name = %s"
		first_name = (searched, )
		result = c.execute(sql1, first_name)
		result=c.fetchall()

		sql2 = "SELECT CUSTOMER.CustID, Name, RentalBalance FROM CUSTOMER, vRentalInfo WHERE WHERE CusID = %d"
		id = (searched, )
		result = c.execute(sql2, id)
		result = c.fetchall()
		
		if not result:
			result="Record Not Found..."

		searched_label = Label(search_customers, text = result)
		searched_label.grid(row=2,column=0, padx=10)

	search_box = Entry(search_customers)
	search_box.grid(row=0,column=1,padx=10,pady=10)

	search_box_label = Label(search_customers, text="Search Customer by Last Name")
	search_box_label.grid(row=0,column=0,padx=10,pady=10)

	search_button = Button(search_customers, text = "Search Customers", command = search_now)
	search_button.grid(row=1, column=0, padx=10)


list_customers_button = Button(root, text="List Customers", command=list_customers)
list_customers_button.grid(row=24, column=0, sticky=W, padx=10)

search_customers_button = Button(root, text = "Search Customers", command=search_customers)
search_customers_button.grid(row = 25, column = 1, sticky=W, padx=10)


root.mainloop()

