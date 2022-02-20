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


#5b
def list_vehicle():
	list_vehicle_query = Tk()
	list_vehicle_query.title("List All Vehicles")
	list_vehicle_query.geometry("800x600")
	c.execute("SELECT DISTINCT VehicleID, Description, Daily FROM Rate, Vehicle")
	result = c.fetchall()

	for index, x in enumerate(result):
		num = 0
		for y in x:
			lookup_label = Label(list_vehicle_query, text = x)
			lookup_label.grid()
			print(x)
			num+=1

def search_vehicles():
	search_vehicles = Tk()
	search_vehicles.title("Search Customers")
	search_vehicles.geometry("800x600")
	def search_now():
		searched = search_box.get()
		sql = "SELECT DISTINCT VehicleID, Description, Daily FROM Rate, Vehicle WHERE VehicleID = %d"
		VehicleID = (searched, )
		result = c.execute(sql, VehicleID)
		result=c.fetchall()

		sql1 = "SELECT DISTINCT VehicleID, Description, Daily FROM Rate, Vehicle WHERE description = %s"
		description = (searched, )
		result = c.execute(sql1, description)
		result=c.fetchall()

		sql1 = "SELECT DISTINCT VehicleID, Description, Daily FROM Rate, Vehicle WHERE description = %s"
		description = (searched, )
		result = c.execute(sql1, description)
		result=c.fetchall()

		if not result:
			result="Record Not Found..."

		searched_label = Label(search_vehicles, text = result)
		searched_label.grid(row=3,column=0, padx=10)

	search_box = Entry(search_vehicles)
	search_box.grid(row=5,column=1,padx=10,pady=10)

	search_box_label = Label(search_vehicles, text="Search Vehicles by VehicleID")
	search_box_label.grid(row=6,column=0,padx=10,pady=10)
	
	search_button = Button(search_vehicles, text = "Search Vehicles", command = search_now)
	search_button.grid(row=7, column=0, padx=10)


list_vehicles_button = Button(root, text="List Vehicles", command=list_vehicle)
list_vehicles_button.grid(row=9, column=0, sticky=W, padx=10)

search_vehicles_button = Button(root, text = "Search Vehicles", command=search_vehicles)
search_vehicles_button.grid(row = 10, column = 1, sticky=W, padx=10)


root.mainloop()

