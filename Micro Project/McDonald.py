
import pyfiglet
from pyfiglet import *
from termcolor import *
import time
import datetime
from tabulate import tabulate
import mysql.connector
import sys


class Customer():
    invoice_no = 0
    date = ""
    time = ""
    customer_name = ""
    customer_contact = ""
    customer_address = ""
    quantity = 0
    sub_total = 0
    gst = 0
    total = 0
    products_brought = [["Product Name","Rate","Quantity","Sub Total"]]


class Seller():
    seller_name = ""
    seller_contact = ""
    seller_address = ""
    seller_gstin = ""


class Main():

    def Main_Window(self, mycursor, mydb):
        print('\033c')
        print('\x1bc')
        print(colored(pyfiglet.figlet_format("Welcome To"), "red"))
        print(colored(pyfiglet.figlet_format("Mc  D o n a l d 's"), "yellow"))
        ch1 = 0
        ch1 = int(input("Press\n  1 Add Items\n  2 Create Invoice\n  3 Records\n  4 Exit\n      Your Choice : "))
        if ch1 == 1:
            self.Win11(mycursor, mydb)
        elif ch1 == 2:
            self.Win21(mycursor, mydb)
        elif ch1 == 3:
            self.Win31(mycursor, mydb)
        elif ch1 == 4:
            sys.exit()
        else:
            print("Invalid Choice!\nChoose Correct One.")
            self.Main_Window(mycursor, mydb)




    def Win111(self, mycursor, mydb):
        print('\033c')
        print('\x1bc')
        print("Enter Item Details To Add It : ")
        item_to_add_Name = ""
        item_to_add_Rate = ""
        item_to_add_Name = input("Name : ")
        item_to_add_Rate = input("Rate : ")
        try:
            sql = "INSERT INTO item_info (item_name, item_rate) VALUES (%s, %s)"
            val = (item_to_add_Name, item_to_add_Rate)
            mycursor.execute(sql, val)
            mydb.commit()
            self.Win1111_1121_1131("Item Added Successfully !", mycursor, mydb)
        except Exception as e:
            print(colored(f"Error Occured : {e}", "red" ))
            print(colored("Contact To Adminstrator.", "red"))
            self.Win1111_1121_1131("Failed To Add Item !", mycursor, mydb)

    def Win112(self, mycursor, mydb):
        print('\033c')
        print('\x1bc')
        print("Enter Item Details To Modify It : ")
        item_to_modify_Name = ""
        item_to_modify_Rate = ""
        item_to_modify_Name = input("Name : ")
        item_to_modify_Rate = input("Rate : ")
        try:
            sql = "UPDATE item_info SET item_rate = %s WHERE item_name = %s"
            val = (item_to_modify_Rate, item_to_modify_Name)
            mycursor.execute(sql, val)
            mydb.commit()
            self.Win1111_1121_1131("Item Modified Successfully !", mycursor, mydb)
        except Exception as e:
            print(colored(f"Error Occured : {e}", "red" ))
            print(colored("Contact To Adminstrator.", "red"))
            self.Win1111_1121_1131("Failed To Modify Item !", mycursor, mydb)

    def Win113(self, mycursor, mydb):
        print('\033c')
        print('\x1bc')
        print("Enter Item Details To Delete It : ")
        item_to_delete_Name = ""
        item_to_delete_Name = input("Name : ")
        try:
            sql = "DELETE FROM item_info WHERE item_name= %s"
            val = (item_to_delete_Name, )
            mycursor.execute(sql, val)
            mydb.commit()
            self.Win1111_1121_1131("Item Deleted Successfully !", mycursor, mydb)
        except Exception as e:
            print(colored(f"Error Occured : {e}", "red" ))
            print(colored("Contact To Adminstrator.", "red"))
            self.Win1111_1121_1131("Failed To Delete Item !", mycursor, mydb)

    def Win1111_1121_1131(self, whats_done, mycursor, mydb):
        print(whats_done)
        print("Redirecting To Privious Window....")
        time.sleep(2)
        self.Win11(mycursor, mydb)

    def Win11(self, mycursor, mydb):
        print('\033c')
        print('\x1bc')
        try:
            mycursor.execute("SELECT * FROM item_info")
            myresult = mycursor.fetchall()
            available_items = []
            available_items.clear()
            available_items.append(["Item Name", "Rate"])
            for x in myresult:
                available_items.append(list(x))
            print("\nAvailable Items In Database : ")
            print(tabulate(available_items, headers='firstrow', showindex=range(1,len(available_items))))
        except Exception as e:
                print(colored(f"Error Occured : {e}", "red" ))
                print(colored("Contact To Adminstrator.", "red"))

        ch11 = 0
        ch11 = int(input("\nPress\n 1 To Add Item\n 2 To Modify Item\n 3 To Delete Item\n 4 To Return Main Menu\n      Your Choice : "))
        if ch11 == 1:
            self.Win111(mycursor, mydb)
        elif ch11 == 2:
            self.Win112(mycursor, mydb)
        elif ch11 == 3:
            self.Win113(mycursor, mydb)
        elif ch11 == 4:
            self.Main_Window(mycursor, mydb)
        else:
            print("Invalid Choice!\nChoose Correct One.")
            self.Win11(mycursor, mydb)




    def Win211(self, Temp_Cust, mycursor, mydb):
        temp_lis = []
        temp_lis.clear()
        print("\nEnter Purchase Item Details : ")
        temp_lis.append(input("Item Name : "))
        try:
            mycursor.execute("SELECT item_rate FROM item_info WHERE item_name = %s", (temp_lis[0],))
            temp_lis.append(mycursor.fetchone()[0])
            print("    Price : ", temp_lis[1])
        except:
            print(colored("Item is not in database. Enter rate manually !", "red"))
            temp_lis.append(input("    Price : "))
        temp_lis.append(input(" Quantity : "))
        temp_lis.append(int(temp_lis[-1]) * int(temp_lis[-2]))
        Temp_Cust.products_brought.append(temp_lis)
        print("Item Added Successfully !")
        self.Win2111(Temp_Cust, mycursor, mydb)

    def Win2111(self, Temp_Cust, mycursor, mydb):
        ch211 = 0
        ch211 = int(input("\nPress\n  1 To Add More Items In Bill\n  2 To Submit Bill\n  3 To Cancel\n      Your Choice : "))
        if ch211 == 1:
            self.Win211(Temp_Cust, mycursor, mydb)
        elif ch211 == 2:
            self.Win212(Temp_Cust, mycursor, mydb)
        elif ch211 == 3:
            self.Win213_2124(Temp_Cust, mycursor, mydb)
        else:
            print("Invalid Choice!\nChoose Correct One.")
            self.Win2111(Temp_Cust, mycursor, mydb)

    def Win212(self, Temp_Cust, mycursor, mydb):
        print('\033c')
        print('\x1bc')
        print("Invoice No. : ",Temp_Cust.invoice_no)
        print("Date & Time : {0} {1}".format(Temp_Cust.date, Temp_Cust.time))

        print("\nSeller Details : ")
        print("   Name : ", Seller.seller_name)
        print("Contact : ", Seller.seller_contact)
        print("Address : ", Seller.seller_address)
        print("  GSTIN : ", Seller.seller_gstin)

        print("\nCustomer Details : ")
        print("   Name : ", Temp_Cust.customer_name)
        print("Contact : ", Temp_Cust.customer_contact)
        print("Address : ", Temp_Cust.customer_address)
        print("")
        
        print(tabulate(Temp_Cust.products_brought, headers='firstrow', tablefmt='fancy_grid', showindex=range(1,len(Temp_Cust.products_brought))))

        Temp_Cust.quantity = 0
        Temp_Cust.sub_total = 0
        Temp_Cust.gst = 0
        Temp_Cust.tota = 0
        for i in range(1, len(Temp_Cust.products_brought)):
            Temp_Cust.quantity += int(Temp_Cust.products_brought[i][2])
            Temp_Cust.sub_total += int(Temp_Cust.products_brought[i][3])
        Temp_Cust.gst = (Temp_Cust.sub_total*5.0)//100
        Temp_Cust.total = Temp_Cust.sub_total + Temp_Cust.gst
        print("\n Quantity :",Temp_Cust.quantity)
        print("Sub Total :",Temp_Cust.sub_total)
        print("  GST(5%) :",Temp_Cust.gst)
        print(colored("    Total : {0}".format(Temp_Cust.total), "yellow"))

        ch212 = 0
        ch212 = int(input("\nPress :\n  1 To Add Items In Bill\n  2 To Delete Items From Bill\n  3 To Save/Printout Bill\n  4 To Cancel\n      Your Choice : "))
        if ch212 == 1 :
            self.Win211(Temp_Cust, mycursor, mydb)
        elif ch212 == 2:
            self.Win2122(Temp_Cust, mycursor, mydb)
        elif ch212 == 3:
            self.Win2123(Temp_Cust, mycursor, mydb)
        elif ch212 == 4:
            self.Win213_2124(Temp_Cust, mycursor, mydb)
        else:
            print("Invalid Choice!\nChoose Correct One.")
            time.sleep(2)
            self.Win212(Temp_Cust, mycursor, mydb)            

    def Win2122(self, Temp_Cust, mycursor, mydb):
        print("\nTo Delete Item Enter")
        item_to_del = ""
        item_to_del = input("Item Name/Index : ")
        try:
            item_to_del = int(item_to_del)
            if item_to_del>len(Temp_Cust.products_brought):
                print("Can't Delete Item, Invalid Index Entered !\n Redirecting To Preview....")
                time.sleep(2)
            else:
                del Temp_Cust.products_brought[item_to_del]
                print("Item Deleted Successfully !\n Redirecting To Preview....")
                time.sleep(2)
        except:
            for i in Temp_Cust.products_brought:
                if item_to_del in i:
                    Temp_Cust.products_brought.remove(i)
                    break
            print("Item Deleted Successfully !\n Redirecting To Preview....")
            time.sleep(2)  
        finally:
            self.Win212(Temp_Cust, mycursor, mydb)

    def Win2123(self, Temp_Cust, mycursor, mydb):
        try:
            sql = "INSERT INTO customer_info (invoice_no, date, time, name, contact, address, quantity, sub_total, gst, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (Temp_Cust.invoice_no, Temp_Cust.date, Temp_Cust.time, Temp_Cust.customer_name, Temp_Cust.customer_contact, Temp_Cust.customer_address, Temp_Cust.quantity, Temp_Cust.sub_total, Temp_Cust.gst, Temp_Cust.total)
            mycursor.execute(sql, val)
            Temp_Cust.invoice_no = "invoiceno" + str(Temp_Cust.invoice_no)
            sql = "CREATE TABLE {0} (srno INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(50), rate INT, quantity INT, sub_total INT)"
            mycursor.execute(sql.format(Temp_Cust.invoice_no))
            for i in range(1, len(Temp_Cust.products_brought)):
                sql = "INSERT INTO {0} (product_name, rate, quantity, sub_total) VALUES (%s, %s, %s, %s)"
                val = (Temp_Cust.products_brought[i][0], Temp_Cust.products_brought[i][1], Temp_Cust.products_brought[i][2], Temp_Cust.products_brought[i][3])
                mycursor.execute(sql.format(Temp_Cust.invoice_no), val)
            mydb.commit()
            print("\nBill Submitted Successfully !\nRedirecting To Main Window....")
        except Exception as e:
            print(colored(f"Error Occured : {e}", "red" ))
            print(colored("Contact To Adminstrator.", "red"))
            print("\nRedirecting To Main Window....")

        Temp_Cust.invoice_no = 0
        Temp_Cust.date = ""
        Temp_Cust.time = ""
        Temp_Cust.customer_name = ""
        Temp_Cust.customer_contact = ""
        Temp_Cust.customer_address = ""
        Temp_Cust.quantity = 0
        Temp_Cust.sub_total = 0
        Temp_Cust.gst = 0
        Temp_Cust.total = 0
        Temp_Cust.products_brought.clear()
        Temp_Cust.products_brought.append(["Product Name","Rate","Quantity","Sub Total"])
        del Temp_Cust
        time.sleep(2)  
        self.Main_Window(mycursor, mydb)

    def Win213_2124(self, Temp_Cust, mycursor, mydb):
        Temp_Cust.invoice_no = 0
        Temp_Cust.date = ""
        Temp_Cust.time = ""
        Temp_Cust.customer_name = ""
        Temp_Cust.customer_contact = ""
        Temp_Cust.customer_address = ""
        Temp_Cust.quantity = 0
        Temp_Cust.sub_total = 0
        Temp_Cust.gst = 0
        Temp_Cust.total = 0
        Temp_Cust.products_brought.clear()
        Temp_Cust.products_brought.append(["Product Name","Rate","Quantity","Sub Total"])
        del Temp_Cust
        print("\nBill Discarded Successfully !\n Redirecting To Main Window....")
        time.sleep(2)  
        self.Main_Window(mycursor, mydb)

    def Win21(self, mycursor, mydb):
        print('\033c')
        print('\x1bc')
        print("")
        Temp_Cust = Customer()
        sql = "SELECT invoice_no FROM customer_info"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            Temp_Cust.invoice_no = 1
        else:
            Temp_Cust.invoice_no = int(list(myresult[-1])[0])+1
        print("\nInvoice No. : ", Temp_Cust.invoice_no)
        Temp_Cust.date = str(datetime.datetime.now())[:-16]
        Temp_Cust.time = str(datetime.datetime.now())[11:-10]
        print("Date & Time : {0} {1}".format(Temp_Cust.date, Temp_Cust.time)) 
        print("\nEnter Customer Details : ")
        Temp_Cust.customer_name = ""
        Temp_Cust.customer_contact = ""
        Temp_Cust.customer_address = ""
        Temp_Cust.customer_name = input("   Name : ")
        Temp_Cust.customer_contact = input("Contact : ")
        Temp_Cust.customer_address = input("Address : ")
        self.Win211(Temp_Cust, mycursor, mydb)
    



    def Win312(self, mycursor, mydb, inv_to_see):
        try:
            mycursor.execute("SELECT * FROM seller_info")
            info_seller = mycursor.fetchone()
            sql = "SELECT * FROM customer_info WHERE invoice_no = %s"
            mycursor.execute(sql, (inv_to_see, ))
            info_cust = mycursor.fetchone()
            inv_to_see = "invoiceno"+str(inv_to_see)
            sql = "SELECT * FROM {0}"
            mycursor.execute(sql.format(inv_to_see))
            info_invoice = [["Sr No", "Product Name", "Rate", "Quantity", "Sub Total"]]
            for x in mycursor.fetchall():
                info_invoice.append(list(x))
        except Exception as e:
            print(colored(f"Error Occured : {e}", "red" ))
            print(colored("Contact To Adminstrator.", "red"))
            print("\nRedirecting To Main Window....")
            time.sleep(2)  
            self.Main_Window(mycursor, mydb)

        print('\033c')
        print('\x1bc')
        print(" Invoice No :", info_cust[0])
        print("Date & Time : " + info_cust[1] + " " + info_cust[2])
        print("\nSeller Details : ")
        print("   Name : ", info_seller[0])
        print("Contact : ", info_seller[1])
        print("Address : ", info_seller[2])
        print("  GSTIN : ", info_seller[3])
        print("\nCustomer Details : ")
        print("   Name : ", info_cust[3])
        print("Contact : ", info_cust[4])
        print("Address : ", info_cust[5])
        print("")
        # print(tabulate(info_invoice, headers='firstrow', tablefmt='fancy_grid', showindex=range(1,len(Temp_Cust.products_brought))))
        print(tabulate(info_invoice, headers='firstrow', tablefmt='fancy_grid'))
        print(colored("\n Quantity : {0}".format(info_cust[6]), "yellow"))
        print("Sub Total :",info_cust[7])
        print("  GST(5%) :",info_cust[8])
        print(colored("    Total : {0}".format(info_cust[9]), "yellow"))
        a = input("\n Enter any key to return main window : ")
        self.Main_Window(mycursor, mydb)

    def Win311(self, mycursor, mydb, inv_to_see):
        try:
            sql = "SELECT * FROM customer_info WHERE name = %s"
            mycursor.execute(sql, (inv_to_see, ))
            myresult = []
            myresult.clear()
            myresult.append(["Invoice No", "Date", "Time", "Name", "Contact", "Address", "Quantity", "Sub Total", "GST(5%)", "Total"])
            for x in mycursor.fetchall():
                myresult.append(list(x))
            print("Available Invoices : ")
            print(tabulate(myresult, headers='firstrow', tablefmt='fancy_grid'))
            inv_to_see = 0
            inv_to_see = int(input("\nEnter Invoice No To See It : "))
            self.Win312(mycursor, mydb, inv_to_see)
        except Exception as e:
            print(colored(f"Error Occured : {e}", "red" ))
            print(colored("Contact To Adminstrator.", "red"))
            print("\nRedirecting To Main Window....")
            time.sleep(2)  
            self.Main_Window(mycursor, mydb)

    def Win31(self, mycursor, mydb):
        print('\033c')
        print('\x1bc')
        sql = "SELECT invoice_no FROM customer_info"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        myresult.sort()
        if len(myresult) == 0:
            invoice_enrolled = 0
        else:
            invoice_enrolled = myresult[-1][0]
        print("\nInvoices Enrolled : ", invoice_enrolled)
        inv_to_see = ""
        inv_to_see = input("Enter Invoice No/Name Of Customers : ")
        try:
            inv_to_see = int(inv_to_see)
            self.Win312(mycursor, mydb, inv_to_see)
        except:
            self.Win311(mycursor, mydb, inv_to_see)




    def __init__(self):
        # Connect to host
        mydb = mysql.connector.connect(host="localhost", user="main", password="5GL60GkAD(Szl.zV")
        # Creating cursor
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        present_or_not = 0
        for x in mycursor:
            if x[0] == "mcdonald":
                present_or_not = 1
                break
        if present_or_not == 1:
            mydb = mysql.connector.connect(host="localhost", user="main", password="5GL60GkAD(Szl.zV", database="mcdonald")
            mycursor = mydb.cursor()
            sql = "SELECT * FROM seller_info"
            mycursor.execute(sql)
            myresult = list(mycursor.fetchone())
            Seller.seller_name = myresult[0]
            Seller.seller_contact = myresult[1]
            Seller.seller_address = myresult[2]
            Seller.seller_gstin = myresult[3]
        else:
            # Create Database
            mycursor.execute("CREATE DATABASE mcdonald")
            mydb = mysql.connector.connect(host="localhost", user="main", password="5GL60GkAD(Szl.zV", database="mcdonald")
            mycursor = mydb.cursor()

            mycursor.execute("CREATE TABLE seller_info (seller_name VARCHAR(50), seller_contact INT(10), seller_address VARCHAR(50), seller_gstin VARCHAR(15))")
            mycursor.execute("CREATE TABLE item_info (item_name VARCHAR(50), item_rate INT(10))")
            mycursor.execute("CREATE TABLE customer_info (invoice_no INT, date VARCHAR(20), time VARCHAR(20), name VARCHAR(50), contact VARCHAR(20), address VARCHAR(50), quantity INT, sub_total INT, gst INT, total INT)")
            
            print(colored("It's One Time Setup\nEnter Information Carefully !\n Information Can't Changed !"), "red")
            print("\nPlease Enter Info Of Franchise & Franchise Owner :")
            Seller.seller_name = ""
            Seller.seller_contact = ""
            Seller.seller_address = ""
            Seller.seller_gstin = ""
            Seller.seller_name = input("    Name :")
            Seller.seller_contact = input(" Contact :")
            Seller.seller_address = input(" Address :")
            Seller.seller_gstin = input("   GSTIN :").upper()
            sql = "INSERT INTO seller_info (seller_name, seller_contact, seller_address, seller_gstin) VALUES (%s, %s, %s, %s)"
            val = (Seller.seller_name, Seller.seller_contact, Seller.seller_address, Seller.seller_gstin)
            mycursor.execute(sql, val)
            
        mydb.commit()
        self.Main_Window(mycursor, mydb)


A=Main()
