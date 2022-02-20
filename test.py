from tkinter import *
import sqlite3
import datetime

root = Tk()
root.title ('Welcom to Team GUI')
root.geometry("700x800")

conn = sqlite3.connect('RentalCar.db')
# print = sqlite3.connect("Connected to DB successfully.")

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

#-------------------------------------Task 2 Part 1------------------------------------
def newCust ():
	insertconn1 = sqlite3.connect("RentalCar.db")
	c = insertconn1.cursor()

	#point = SELECT last_insert_rowid()+1
	# execute for insert is two double quotes, just like the string
	c.execute("INSERT INTO customer VALUES (:CustID, :Name, :Phone)",
						{
							'CustID': c.lastrowid,
							'Name': Name.get(),
							'Phone': Phone.get(),
						})
	# if there is another function, since within function, we want to make sure the change is updateed
	CustID.delete(0, END)
	Name.delete(0,END)
	Phone.delete(0,END)

	# commits any changes to the DB if any other connections are open.
	insertconn1.commit()
#-------------------------------------Task 2 Part 2------------------------------------
def newVehicle ():
	insertconn2 = sqlite3.connect("RentalCar.db")
	c = insertconn2.cursor()
	# execute for insert is two double quotes, just like the string
	c.execute("INSERT INTO vehicle VALUES (:VehicleID, :Description, :Year, :Type, :Category)",
						{
							'VehicleID': VehicleID.get(),
							'Description': Description.get(),
							'Year': Year.get(),
							'Type': Type.get(),
							'Category': Category.get(),
						})
	# if there is another function, since within function, we want to make sure the change is updateed
	VehicleID.delete(0,END)
	Description.delete(0,END)
	Year.delete(0,END)
	Type.delete(0,END)
	Category.delete(0,END)

	# commits any changes to the DB if any other connections are open.
	insertconn2.commit()
#-------------------------------------Task 2 Part 3------------------------------------
def newRes ():
	insertconn3 = sqlite3.connect("RentalCar.db")
	c = insertconn3.cursor()
	# execute for insert is two double quotes, just like the string
	c.execute("INSERT INTO RENTAL VALUES (:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate)",
						{
							'CustID': c.lastrowid,
							'VehicleID': rVID.get(),
							'StartDate': rStartD.get(),
							'OrderDate': rOrdD.get(),
							'RentalType': rRenT.get(),
							'Qty': rQty.get(),
							'ReturnDate': rRetD.get(),
							'TotalAmount': rTot.get(),
							'PaymentDate': rPay.get(),
						})
	# if there is another function, since within function, we want to make sure the change is updateed
	
	# commits any changes to the DB if any other connections are open.
	insertconn3.commit()

#-------------------------------------Task 2 Part 4------------------------------------
def retrAndUpdt ():
	#DateTime today = DateTime.Today;
	conn4 = sqlite3.connect("RentalCar.db")
	c = conn4.cursor()
	# execute for insert is two double quotes, just like the string

	c.execute("SELECT RENTAL, TotalAmount, FROM RENTAL, CUSTOMER WHERE CUSTOMER.Name = :Name AND CUSTOMER.CustID = RENTAL.CustID AND RENTAL.VehicleID = :VehicleID AND RENTAL.ReturnDate == DATE(:ReturnDate)",
				{'Name': custN.get(), 
				'VehicleID': returnVID.get(), 
				'ReturnDate': returnDate.get(),
				})

	records = c.fetchall()
	print(records) #console print out

	c.execute("UPDATE RENTAL SET PaymentDate = DATE(:PaymentDate) WHERE VehicleID = :VehicleID AND ReturnDate == DATE(:ReturnDate)", 
				{'VehicleID': returnVID.get(),
				'ReturnDate': returnDate.get(),
				'PaymentDate': todayDate })
				


	# if there is another function, since within function, we want to make sure the change is updateed
	custN.delete(0,END)
	returnVID.delete(0,END)
	returnDate.delete(0,END)

	# commits any changes to the DB if any other connections are open.
	conn4.commit()

#-----------------------------------Task 2 Part 1 GUI------------------------------------------

CustID = Entry(root, width = 30)
CustID.grid(row = 0, column = 1, padx = 20) # pad given on x 20 pixels to both right and left

Name = Entry(root, width = 30)
Name.grid(row = 1, column = 1)

Phone = Entry(root, width = 30)
Phone.grid(row = 2, column = 1)

CustID_label = Label (root, text = 'CustID: ')
CustID_label.grid(row = 0, column = 0)

name_label = Label (root, text = 'Name: ')
name_label.grid(row = 1, column = 0)

phone_label = Label (root, text = 'Phone: ')
phone_label.grid(row = 2, column = 0)

# New Customer button
newCust_btn = Button(root, text = 'Add New Customer', command = newCust)
newCust_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#-----------------------------------Task 2 Part 2 GUI------------------------------------------
VehicleID = Entry(root, width = 30)
VehicleID.grid(row = 4, column = 1, padx = 20) # pad given on x 20 pixels to both right and left

Description = Entry(root, width = 30)
Description.grid(row = 5, column = 1)

Year = Entry(root, width = 30)
Year.grid(row = 6, column = 1)

Type = Entry(root, width = 30)
Type.grid(row = 7, column = 1)

Category = Entry(root, width = 30)
Category.grid(row = 8, column = 1)

vid_l = Label (root, text = 'Vehicle ID: ')
vid_l.grid(row = 4, column = 0)

desc_l = Label (root, text = 'Description: ')
desc_l.grid(row = 5, column = 0)

year_l = Label (root, text = 'Year: ')
year_l.grid(row = 6, column = 0)

type_l = Label (root, text = 'Type: ')
type_l.grid(row = 7 , column = 0)

cat_l = Label (root, text = 'Category: ')
cat_l.grid(row = 8, column = 0)

# New Vehicle button
newVeh_btn = Button(root, text = 'Add New Vehicle', command = newVehicle)
newVeh_btn.grid(row = 9, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#-----------------------------------Task 2 Part 3 GUI------------------------------------------

rCID = Entry(root, width = 30)
rCID.grid(row = 10, column = 1)

rVID = Entry(root, width = 30)
rVID.grid(row = 11, column = 1)

rStartD = Entry(root, width = 30)
rStartD.grid(row = 12, column = 1)

rOrdD = Entry(root, width = 30)
rOrdD.grid(row = 13, column = 1)

rRenT = Entry(root, width = 30)
rRenT.grid(row = 14, column = 1)

rQty = Entry(root, width = 30)
rQty.grid(row = 15, column = 1)

rRetD = Entry(root, width = 30)
rRetD.grid(row = 16, column = 1)

rTot = Entry(root, width = 30)
rTot.grid(row = 17, column = 1)

rPay = Entry(root, width = 30)
rPay.grid(row = 18, column = 1)

rCID_l = Label (root, text = 'CustID: ')
rCID_l.grid(row = 10, column = 0)

rVID_l = Label(root, text = 'VehicleID: ')
rVID_l.grid(row = 11, column = 0)

rStartD_l = Label(root, text = 'StartDate ')
rStartD_l.grid(row = 12, column = 0)

rOrdD_l = Label(root, text = 'OrderDate ')
rOrdD_l.grid(row = 13, column = 0)

rRenT_l = Label(root, text = 'ReturnType ')
rRenT_l.grid(row = 14, column = 0)

rQty_l = Label(root, text = 'Qty ')
rQty_l.grid(row = 15, column = 0)

rRetD_l = Label(root, text = 'ReturnDate ')
rRetD_l.grid(row = 16, column = 0)

rTot_l = Label(root, text = 'TotalAmount ')
rTot_l.grid(row = 17, column = 0)

rPay_l = Label(root, text = 'PaymentDate ')
rPay_l.grid(row = 18, column = 0)

# New Reservation button
newRes_btn = Button(root, text = 'Add New Reservation', command = newRes)
newRes_btn.grid(row = 19, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#-----------------------------------Task 2 Part 4 GUI------------------------------------------
returnDate = Entry(root, width = 30)
returnDate.grid(row = 20, column = 1, padx = 20)

custN = Entry(root, width = 30)
custN.grid(row = 21, column = 1)

returnVID = Entry(root, width = 30)
returnVID.grid(row = 22, column = 1, padx = 20) 

todayDate = Entry(root, width = 30)
todayDate.grid(row = 23, column = 1, padx = 20)

returnDate_l = Label (root, text = 'Return Date: ')
returnDate_l.grid(row = 20, column = 0)

custN_l = Label (root, text = 'Customer Name: ')
custN_l.grid(row = 21, column = 0)

returnVID_l = Label (root, text = 'Vehicle ID: ')
returnVID_l.grid(row = 22, column = 0)

todayDate_l = Label (root, text = 'Todays Date: ')
todayDate_l.grid(row = 23, column = 0)


# New Vehicle button
newVeh_btn = Button(root, text = 'Retrieve Rental', command = retrAndUpdt)
newVeh_btn.grid(row = 24, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

conn.commit()

conn.close()

root.mainloop()
