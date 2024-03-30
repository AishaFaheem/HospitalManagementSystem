from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hospital Management System")
        self.geometry("1540x800+0+0")
        
        self.PID=StringVar()
        self.PName=StringVar()
        self.PGender=StringVar()
        self.PAge=StringVar()
        self.PDOB=StringVar()
        self.PAddress=StringVar()
        self.PBloodGroup=StringVar()
        self.PLangPref=StringVar()
        self.PAccessReq=StringVar()
        self.PPresMed=StringVar()
        self.PWeight=StringVar()
        self.PHeight=StringVar()
        self.PAdditionalNotes=StringVar()
        self.PInsuranceProvider=StringVar()
        # Database connection
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abc",
                database="Mydata"
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        # GUI elements initialization
        self.init_gui()

    def init_gui(self):

        labeltitle = Label(self, bd=10, relief=RIDGE, text="Hospital Management System", fg="#F70059", bg="white", font=("times new roman", 50, "bold"))
        labeltitle.pack(side=TOP, fill=X)
        
        # DataFrame
        DataFrame = Frame(self, bd=13, relief=RIDGE)
        DataFrame.place(x=0, y=108, width=1280, height=305)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                        font=("arial", 12, "bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=1,width=860,height=271)
        
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                        font=("arial", 12, "bold"),text="Prescription")
        DataFrameRight.place(x=860,y=1,width=390,height=270)
        # Patient Name
        labelPatientName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2)
        labelPatientName.grid(row=0, column=0, sticky=W)
        PatientName = Entry(DataFrameLeft,textvariable=self.PName, font=("arial", 12), width=38)
        PatientName.grid(row=0, column=1, sticky=W)

        # Gender
        labelGender = Label(DataFrameLeft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        labelGender.grid(row=1, column=0, sticky=W)
        Gender = ttk.Combobox(DataFrameLeft,textvariable=self.PGender, state="readonly", font=("times new roman", 12), width=40)
        Gender["values"] = ("Male", "Female", "Other")
        Gender.current(0)
        Gender.grid(row=1, column=1, sticky=W)

        # Age
        labelAge = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Age:", padx=2)
        labelAge.grid(row=2, column=0, sticky=W)
        Age = Entry(DataFrameLeft,textvariable=self.PAge, font=("arial", 12), width=38)
        Age.grid(row=2, column=1, sticky=W)

        # Blood Group
        labelBloodGroup = Label(DataFrameLeft, text="Blood Group:", font=("arial", 12, "bold"), padx=2, pady=6)
        labelBloodGroup.grid(row=3, column=0, sticky=W)
        BloodGroup = ttk.Combobox(DataFrameLeft,textvariable=self.PBloodGroup , state="readonly", font=("times new roman", 12), width=40)
        BloodGroup["values"] = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
        BloodGroup.current(0)
        BloodGroup.grid(row=3, column=1, sticky=W)
        
        # Date of Birth
        labelDOB = Label(DataFrameLeft, text="Date of Birth:", font=("arial", 12, "bold"), padx=2, pady=6)
        labelDOB.grid(row=4, column=0, sticky=W)
        DOB = DateEntry(DataFrameLeft,textvariable=self.PDOB, font=("arial", 12), width=36, background='darkblue', foreground='white', borderwidth=2)
        DOB.grid(row=4, column=1, sticky=W)

        # Address
        labelAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address:", padx=2,pady=5.5)
        labelAddress.grid(row=5, column=0, sticky=W)
        Address = Entry(DataFrameLeft,textvariable=self.PAddress, font=("arial", 12), width=38)
        Address.grid(row=5, column=1, sticky=W)

        # Patient ID
        labelPatientID = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient ID:", padx=2, pady=5.5)
        labelPatientID.grid(row=6, column=0, sticky=W)
        PatientID = Entry(DataFrameLeft,textvariable=self.PID, font=("arial", 12), width=38)
        PatientID.grid(row=6, column=1, sticky=W)
        
         # Language Preference
        labelLanguagePreference = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Language Preference:", padx=2, pady=6)
        labelLanguagePreference.grid(row=0, column=2, sticky=W)
        LanguagePreference = Entry(DataFrameLeft,textvariable=self.PLangPref, font=("arial", 12), width=15)
        LanguagePreference.grid(row=0, column=3, sticky=W)
        
         # Accessibility Requirements
        labelAccessibilityRequirements = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Accessibility Requirements:", padx=2, pady=6)
        labelAccessibilityRequirements.grid(row=1, column=2, sticky=W)
        AccessibilityRequirements = Entry(DataFrameLeft,textvariable=self.PAccessReq, font=("arial", 12), width=15)
        AccessibilityRequirements.grid(row=1, column=3, sticky=W)
        
         # Insurance Provider
        labelAccessibilityRequirements = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Insurance Provider:", padx=2, pady=4)
        labelAccessibilityRequirements.grid(row=2, column=2, sticky=W)
        AccessibilityRequirements = Entry(DataFrameLeft,textvariable=self.PInsuranceProvider, font=("arial", 12), width=15)
        AccessibilityRequirements.grid(row=2, column=3, sticky=W)
        
         # Prescribed Medicines
        labelPrescribedMedicine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Prescribed Medicine:", padx=2, pady=6)
        labelPrescribedMedicine.grid(row=3, column=2, sticky=W)
        PrescribedMedicine = Entry(DataFrameLeft,textvariable=self.PPresMed, font=("arial", 12), width=15)
        PrescribedMedicine.grid(row=3, column=3, sticky=W)
        
        # Weight
        labelWeight = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Weight(kg):", padx=2, pady=6)
        labelWeight.grid(row=4, column=2, sticky=W)
        Weight = Entry(DataFrameLeft,textvariable=self.PWeight, font=("arial", 12), width=15)
        Weight.grid(row=4, column=3, sticky=W)
        
        # Height
        labelHeight = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Height(cm):", padx=2, pady=6)
        labelHeight.grid(row=5, column=2, sticky=W)
        Height = Entry(DataFrameLeft,textvariable=self.PHeight, font=("arial", 12), width=15)
        Height.grid(row=5, column=3, sticky=W)
        
         # Additional Notes
        labelAdditionalNotes = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Additional Notes:", padx=2, pady=6)
        labelAdditionalNotes.grid(row=6, column=2, sticky=W)
        AdditionalNotes = Entry(DataFrameLeft,textvariable=self.PAdditionalNotes, font=("arial", 12), width=15)
        AdditionalNotes.grid(row=6, column=3, sticky=W)
        
        
        #DataFrameRight
        self.Prescription=Text(DataFrameRight,font=("arial",12,"bold"),width=38,height=11.25,padx=2,pady=7)
        self.Prescription.grid(row=0,column=0)
        
         # DataFrame2
        DataFrame2 = Frame(self, bd=10, relief=RIDGE)
        DataFrame2.place(x=0, y=420, width=1277, height=80)
        
       
        # ButtonFrame inside DataFrame2
        ButtonFrame = Frame(DataFrame2)
        ButtonFrame.place(x=0, y=0)
        
        # Button Style
        button_style = {'bg': '#6070FF', 'fg': 'white', 'activebackground': '#6070FF', 'activeforeground': 'white', 'borderwidth': 0}
        
        # Prescription Button
        PrescriptionButton = Button(ButtonFrame, command=self.iPrescription,text="Prescription", font=("Arial", 12), width=15, **button_style)
        PrescriptionButton.grid(row=0, column=0, padx=10, pady=10)
        
        # Prescription Data Button
        PrescriptionDataButton = Button(ButtonFrame, text="Prescription Data", font=("Arial", 12), width=15, **button_style)
        PrescriptionDataButton.grid(row=0, column=1, padx=10, pady=10)
        
        
        # Update Button
        UpdateButton = Button(ButtonFrame,command=self.update_data, text="Update", font=("Arial", 12), width=15, **button_style)
        UpdateButton.grid(row=0, column=2, padx=10, pady=10)
        
        # Delete Button
        DeleteButton = Button(ButtonFrame, command=self.iDelete,text="Delete", font=("Arial", 12), width=15, **button_style)
        DeleteButton.grid(row=0, column=3, padx=10, pady=10)
        
        # Clear Button
        ClearButton = Button(ButtonFrame, text="Clear", font=("Arial", 12), width=15, **button_style)
        ClearButton.grid(row=0, column=4, padx=10, pady=10)

        # Exit Button
        ExitButton = Button(ButtonFrame, text="Exit", font=("Arial", 12), width=15, **button_style)
        ExitButton.grid(row=0, column=5, padx=10, pady=10)

        # DataFrame3
        DataFrame3 = Frame(self, bd=10, relief=RIDGE)
        DataFrame3.place(x=0, y=505, width=1277, height=140)
        
        # Scrollbar
        scrollbar_x = ttk.Scrollbar(DataFrame3, orient=HORIZONTAL)
        scrollbar_y = ttk.Scrollbar(DataFrame3, orient=VERTICAL)
        
        # Table Treeview
        self.hospital_table = ttk.Treeview(DataFrame3, columns=("PatientName","Gender","Age","DOB","Address","BloodGroup","PatientID","LanguagePreference","AccessibilityRequirements","InsuranceProvider","PrescribedMedicine","Weight","Height","AdditionalNotes"), xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

         
        # Configure Scrollbars
        scrollbar_x.configure(command=self.hospital_table.xview)
        scrollbar_y.configure(command=self.hospital_table.yview)
        
        # Pack Scrollbars and Treeview
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        self.hospital_table.pack(fill=BOTH, expand=1)
        
        # Set column headings
        self.hospital_table.heading("PatientName", text="Patient Name")
        self.hospital_table.heading("Gender", text="Gender")
        self.hospital_table.heading("Age", text="Age")
        self.hospital_table.heading("DOB", text="Date of Birth")
        self.hospital_table.heading("Address", text="Address")
        self.hospital_table.heading("BloodGroup", text="Blood Group")
        self.hospital_table.heading("PatientID", text="Patient ID")
        self.hospital_table.heading("LanguagePreference", text="Language Preference")
        self.hospital_table.heading("AccessibilityRequirements", text="Accessibility Requirements")
        self.hospital_table.heading("InsuranceProvider", text="Insurance Provider")
        self.hospital_table.heading("PrescribedMedicine", text="Prescribed Medicine")
        self.hospital_table.heading("Weight", text="Weight (kg)")
        self.hospital_table.heading("Height", text="Height (cm)")
        self.hospital_table.heading("AdditionalNotes", text="Additional Notes")
        
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
      # Fetching
        self.fetch_data()
    
    
    # Function to insert data into database
    def iPrescriptionData(self):
        if self.PName.get() == "" or self.PID.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            # Execute SQL query to insert data
            query = "INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (
                self.PName.get(), self.PGender.get(), self.PAge.get(), self.PDOB.get(),
                self.PAddress.get(), self.PBloodGroup.get(), self.PLangPref.get(),
                self.PID.get(), self.PAccessReq.get(), self.PPresMed.get(),
                self.PWeight.get(), self.PHeight.get(), self.PInsuranceProvider.get(),
                self.PAdditionalNotes.get()
            )
            self.cursor.execute(query, data)
            self.connection.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Data inserted successfully")

        # Update method
    def update_data(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="abc", database="Mydata")
            mycursor = connection.cursor()

            # SQL query to update data
            query = "UPDATE hospital SET PatientName=%s, Gender=%s, Age=%s, DOB=%s, Address=%s, BloodGroup=%s, \
                     LanguagePreference=%s, PatientID=%s, AccessibilityRequirements=%s, PrescribedMedicine=%s, \
                     Weight=%s, Height=%s, InsuranceProvider=%s, AdditionalNotes=%s WHERE PatientID=%s"
            
            # Get values from variables
            data = (
                self.PName.get(), self.PGender.get(), self.PAge.get(), self.PDOB.get(),
                self.PAddress.get(), self.PBloodGroup.get(), self.PLangPref.get(),
                self.PID.get(), self.PAccessReq.get(), self.PPresMed.get(),
                self.PWeight.get(), self.PHeight.get(), self.PInsuranceProvider.get(),
                self.PAdditionalNotes.get(), self.PID.get()
            )

            # Execute the update query
            mycursor.execute(query, data)
            connection.commit()
            messagebox.showinfo("Success", "Data updated successfully")
            self.fetch_data()  # Refresh the table with updated data
        except mysql.connector.Error as err:
            messagebox.showerror("Update Error", f"Error: {err}")
        finally:
            if connection.is_connected():
                mycursor.close()
                connection.close()




    # Function to fetch data from the database
    def fetch_data(self):
        try:
            self.hospital_table.delete(*self.hospital_table.get_children())
            self.cursor.execute("SELECT * FROM hospital")
            rows = self.cursor.fetchall()
            for row in rows:
                self.hospital_table.insert("", END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Fetch Data Error", f"Error: {err}")
        finally:
            if self.cursor:
                self.cursor.close()
    def get_cursor(self):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.PName.set(row[0])self.PGender.set(row[1])
        self.PAge.set(row[2])
        self.PDOB.set(row[3])
        self.PAddress.set(row[4])
        self.PBloodGroup.set(row[5])
        self.PLangPref.set(row[6])
        self.PID.set(row[7])
        self.PAccessReq.set(row[8])
        self.PPresMed.set(row[9])
        self.PWeight.set(row[10])
        self.PHeight.set(row[11])
        self.PInsuranceProvider.set(row[12])
        self.PAdditionalNotes.set(row[13])

    def iPrescription(self):
        self.Prescription.delete("1.0", END)  # Clear the prescription area before inserting new data
        self.Prescription.insert(END, "Patient Name:\t\t\t" + self.PName.get() + "\n")
        self.Prescription.insert(END, "Gender:\t\t\t" + self.PGender.get() + "\n")
        self.Prescription.insert(END, "Age:\t\t\t" + self.PAge.get() + "\n")
        self.Prescription.insert(END, "DOB:\t\t\t" + self.PDOB.get() + "\n")
        self.Prescription.insert(END, "Address:\t\t\t" + self.PAddress.get() + "\n")
        self.Prescription.insert(END, "Blood Group:\t\t\t" + self.PBloodGroup.get() + "\n")
        self.Prescription.insert(END, "Patient ID:\t\t\t" + self.PID.get() + "\n")
        self.Prescription.insert(END, "Language Preference:\t\t\t" + self.PLangPref.get() + "\n")
        self.Prescription.insert(END, "Accessibility Requirements:\t\t\t" + self.PAccessReq.get() + "\n")
        self.Prescription.insert(END, "Prescribed Medicine:\t\t\t" + self.PPresMed.get() + "\n")
        self.Prescription.insert(END, "Weight (kg):\t\t\t" + self.PWeight.get() + "\n")
        self.Prescription.insert(END, "Height (cm):\t\t\t" + self.PHeight.get() + "\n")
        self.Prescription.insert(END, "Insurance Provider:\t\t\t" + self.PInsuranceProvider.get() + "\n")
        self.Prescription.insert(END, "Additional Notes:\t\t\t" + self.PAdditionalNotes.get() + "\n")
        
    def iDelete(self):
        # Get the Patient ID to be deleted
        patient_id = self.PID.get()

        if patient_id == "":
            messagebox.showerror("Error", "Please enter Patient ID to delete.")
        else:
            # Open connection to the database
            connection = mysql.connector.connect(host="localhost", user="root", password="abc", database="Mydata")
            cursor = connection.cursor()

        # Execute the delete query
            delete_query = "DELETE FROM hospital WHERE PatientID = %s"
            cursor.execute(delete_query, (patient_id,))

        # Commit the transaction
            connection.commit()

        # Close cursor and connection
            cursor.close()
            connection.close()

        # Show success message
            messagebox.showinfo("Success", f"Record with Patient ID {patient_id} deleted successfully.")

        # Clear the entry fields
            self.clear_fields()

        # Refresh the data in the table
            self.fetch_data()

        
    def clear_fields(self):
    # Clear all entry fields
        self.PName.set("")
        self.PGender.set("")
        self.PAge.set("")
        self.PDOB.set("")
        self.PAddress.set("")
        self.PBloodGroup.set("")
        self.PID.set("")
        self.PLangPref.set("")
        self.PAccessReq.set("")
        self.PPresMed.set("")
        self.PWeight.set("")
        self.PHeight.set("")
        self.PInsuranceProvider.set("")
        self.PAdditionalNotes.set("")

    def exit_application(self):
        # Close the database connection
        if self.connection:
            self.connection.close()
    # Destroy the main window
        self.destroy()
        
        
# Create an instance of the Hospital class
ob = Hospital()
ob.mainloop()