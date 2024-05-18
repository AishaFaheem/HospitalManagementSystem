import tkinter as tk
from tkinter import ttk, messagebox, StringVar, IntVar, DoubleVar
import mysqlx
from tkcalendar import DateEntry
from database.db_connection import Database
import mysql.connector


class HospitalApp:
    DATABASE_ERROR = "Database Error"

    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.patient_name = StringVar()
        self.patient_gender = StringVar()
        self.patient_age = IntVar()
        self.patient_blood_group = StringVar()
        self.patient_dob = StringVar()  # Handling this with DateEntry, initialization might be different
        self.patient_address = StringVar()
        self.patient_id = StringVar()
        self.patient_language_pref = StringVar()
        self.patient_access_req = StringVar()
        self.patient_insurance_provider = StringVar()
        self.patient_prescribed_med = StringVar()
        self.patient_weight = DoubleVar()
        self.patient_height = DoubleVar()
        self.patient_additional_notes = StringVar()

        # Initialize database connection
        self.database = Database(host="localhost", user="root", password="4042", database="Mydata")
        if not self.database.connect():
            messagebox.showerror("Database Connection", "Failed to connect to the database.")
            return
        # GUI elements initialization
        self.init_gui()

    def init_gui(self):
        label_title = tk.Label(self.root, bd=10, relief=tk.RIDGE, text="Hospital Management System", fg="#F70059", bg="white", font=("times new roman", 50, "bold"))
        label_title.pack(side=tk.TOP, fill=tk.X)

        data_frame = tk.Frame(self.root, bd=13, relief=tk.RIDGE)
        data_frame.place(x=0, y=108, width=1280, height=305)

        data_frame_left = tk.LabelFrame(data_frame, bd=10, relief=tk.RIDGE, padx=10, font=("arial", 12, "bold"), text="Patient Information")
        data_frame_left.place(x=0, y=1, width=860, height=271)

        data_frame_right = tk.LabelFrame(data_frame, bd=10, relief=tk.RIDGE, padx=10, font=("arial", 12, "bold"), text="Prescription")
        data_frame_right.place(x=860, y=1, width=390, height=270)

        # Patient Information Fields
        self.create_patient_info_fields(data_frame_left)

        # Prescription Text Area
        self.prescription = tk.Text(data_frame_right, font=("arial", 12, "bold"), width=38, height=11.25, padx=2, pady=7)
        self.prescription.grid(row=0, column=0)

        # Buttons Frame
        data_frame2 = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        data_frame2.place(x=0, y=420, width=1277, height=80)

        button_frame = tk.Frame(data_frame2)
        button_frame.place(x=0, y=0)

        button_style = {'bg': '#6070FF', 'fg': 'white', 'activebackground': '#6070FF', 'activeforeground': 'white', 'borderwidth': 0}

        # Buttons
        self.create_buttons(button_frame, button_style)

        # Data Table
        data_frame3 = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        data_frame3.place(x=0, y=505, width=1277, height=140)

        self.create_data_table(data_frame3)

        # Fetch Data from Database
        self.fetch_data()

    def create_patient_info_fields(self, frame):
        fields = [
            ("Patient Name:", self.patient_name),
            ("Gender:", self.patient_gender, ["Male", "Female", "Other"]),
            ("Age:", self.patient_age),
            ("Blood Group:", self.patient_blood_group, ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]),
            ("Date of Birth:", self.patient_dob, DateEntry),
            ("Address:", self.patient_address),
            ("Patient ID:", self.patient_id),
            ("Language Preference:", self.patient_language_pref),
            ("Accessibility Requirements:", self.patient_access_req),
            ("Insurance Provider:", self.patient_insurance_provider),
            ("Prescribed Medicine:", self.patient_prescribed_med),
            ("Weight(kg):", self.patient_weight),
            ("Height(cm):", self.patient_height),
            ("Additional Notes:", self.patient_additional_notes)
        ]

        for i, (label, var, *args) in enumerate(fields):
            row, col = divmod(i, 2)
            col *= 2

            tk.Label(frame, text=label, font=("arial", 12, "bold"), padx=2, pady=6).grid(row=row, column=col, sticky=tk.W)

            if args:
                if args[0] == DateEntry:
                    DateEntry(frame, textvariable=var, font=("arial", 12), width=36, background='darkblue', foreground='white', borderwidth=2).grid(row=row, column=col + 1, sticky=tk.W)
                else:
                    combobox = ttk.Combobox(frame, textvariable=var, state="readonly", font=("times new roman", 12), width=40)
                    combobox["values"] = args[0]
                    combobox.current(0)
                    combobox.grid(row=row, column=col + 1, sticky=tk.W)
            else:
                tk.Entry(frame, textvariable=var, font=("arial", 12), width=38).grid(row=row, column=col + 1, sticky=tk.W)

    def create_buttons(self, frame, style):
        buttons = [
            ("Prescription", self.i_prescription),
            ("Prescription Data", self.i_prescription_data),
            ("Update", self.update_data),
            ("Delete", self.i_delete),
            ("Clear", self.clear_fields),
            ("Exit", self.exit_application)
        ]

        for i, (text, command) in enumerate(buttons):
            tk.Button(frame, text=text, command=command, font=("Arial", 12), width=15, **style).grid(row=0, column=i, padx=10, pady=10)

    def create_data_table(self, frame):
        scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
        scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)

        columns = (
            "PatientName", "Gender", "Age", "DOB", "Address", "BloodGroup", "PatientID",
            "LanguagePreference", "AccessibilityRequirements", "InsuranceProvider",
            "PrescribedMedicine", "Weight", "Height", "AdditionalNotes"
        )

        self.hospital_table = ttk.Treeview(frame, columns=columns, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

        scrollbar_x.configure(command=self.hospital_table.xview)
        scrollbar_y.configure(command=self.hospital_table.yview)

        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.hospital_table.pack(fill=tk.BOTH, expand=1)

        for col in columns:
            self.hospital_table.heading(col, text=col.replace("ID", " ID").replace("DOB", "Date of Birth"))

        self.hospital_table["show"] = "headings"
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

    def i_prescription_data(self):
        if self.patient_name.get() == "" or self.patient_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                query = "INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (
                    self.patient_name.get(), self.patient_gender.get(), self.patient_age.get(), self.patient_dob.get(),
                    self.patient_address.get(), self.patient_blood_group.get(), self.patient_language_pref.get(),
                    self.patient_id.get(), self.patient_access_req.get(), self.patient_prescribed_med.get(),
                    self.patient_weight.get(), self.patient_height.get(), self.patient_insurance_provider.get(),
                    self.patient_additional_notes.get()
                )
                self.database.cursor.execute(query, data)
                self.database.connection.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Data inserted successfully")
            except mysql.connector.Error:
                messagebox.showerror(self.DATABASE_ERROR, "An error occurred while inserting data")

    def fetch_data(self):
        try:
            query = "SELECT * FROM hospital"
            self.database.cursor.execute(query)
            rows = self.database.cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert("", tk.END, values=row)
        except mysql.connector.Error:
            messagebox.showerror(self.DATABASE_ERROR, "An error occurred while fetching data")

    def get_cursor(self, event=None):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content['values']
        self.patient_name.set(row[0])
        self.patient_gender.set(row[1])
        self.patient_age.set(row[2])
        self.patient_dob.set(row[3])
        self.patient_address.set(row[4])
        self.patient_blood_group.set(row[5])
        self.patient_id.set(row[6])
        self.patient_language_pref.set(row[7])
        self.patient_access_req.set(row[8])
        self.patient_insurance_provider.set(row[9])
        self.patient_prescribed_med.set(row[10])
        self.patient_weight.set(row[11])
        self.patient_height.set(row[12])
        self.patient_additional_notes.set(row[13])

    def i_prescription(self):
        self.prescription.insert(tk.END, f"Patient Name: {self.patient_name.get()}\n")
        self.prescription.insert(tk.END, f"Patient ID: {self.patient_id.get()}\n")
        self.prescription.insert(tk.END, f"Patient Gender: {self.patient_gender.get()}\n")
        self.prescription.insert(tk.END, f"Patient Age: {self.patient_age.get()}\n")
        self.prescription.insert(tk.END, f"Patient Blood Group: {self.patient_blood_group.get()}\n")
        self.prescription.insert(tk.END, f"Patient DOB: {self.patient_dob.get()}\n")
        self.prescription.insert(tk.END, f"Patient Address: {self.patient_address.get()}\n")
        self.prescription.insert(tk.END, f"Language Preference: {self.patient_language_pref.get()}\n")
        self.prescription.insert(tk.END, f"Accessibility Requirements: {self.patient_access_req.get()}\n")
        self.prescription.insert(tk.END, f"Insurance Provider: {self.patient_insurance_provider.get()}\n")
        self.prescription.insert(tk.END, f"Prescribed Medicine: {self.patient_prescribed_med.get()}\n")
        self.prescription.insert(tk.END, f"Weight: {self.patient_weight.get()}\n")
        self.prescription.insert(tk.END, f"Height: {self.patient_height.get()}\n")
        self.prescription.insert(tk.END, f"Additional Notes: {self.patient_additional_notes.get()}\n")

    def update_data(self):
        if self.patient_name.get() == "" or self.patient_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                query = "UPDATE hospital SET Name=%s, Gender=%s, Age=%s, DOB=%s, Address=%s, BloodGroup=%s, LanguagePreference=%s, AccessibilityRequirements=%s, InsuranceProvider=%s, PrescribedMedicine=%s, Weight=%s, Height=%s, AdditionalNotes=%s WHERE PatientID=%s"
                data = (
                    self.patient_name.get(), self.patient_gender.get(), self.patient_age.get(), self.patient_dob.get(),
                    self.patient_address.get(), self.patient_blood_group.get(), self.patient_language_pref.get(),
                    self.patient_access_req.get(), self.patient_prescribed_med.get(),
                    self.patient_weight.get(), self.patient_height.get(), self.patient_insurance_provider.get(),
                    self.patient_additional_notes.get(), self.patient_id.get()
                )
                self.database.cursor.execute(query, data)
                self.database.connection.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Data updated successfully")
            except mysql.connector.Error:
                messagebox.showerror(self.DATABASE_ERROR, "An error occurred while updating data")

    def i_delete(self):
        if self.patient_id.get() == "":
            messagebox.showerror("Error", "Patient ID is required to delete")
        else:
            try:
                query = "DELETE FROM hospital WHERE PatientID=%s"
                data = (self.patient_id.get(),)
                self.database.cursor.execute(query, data)
                self.database.connection.commit()
                self.fetch_data()
                self.clear_fields()
                messagebox.showinfo("Success", "Data deleted successfully")
            except mysql.connector.Error:
                messagebox.showerror(self.DATABASE_ERROR, "An error occurred while deleting data")

    def clear_fields(self):
        self.patient_name.set("")
        self.patient_gender.set("")
        self.patient_age.set("")
        self.patient_dob.set("")
        self.patient_address.set("")
        self.patient_blood_group.set("")
        self.patient_id.set("")
        self.patient_language_pref.set("")
        self.patient_access_req.set("")
        self.patient_prescribed_med.set("")
        self.patient_weight.set("")
        self.patient_height.set("")
        self.patient_additional_notes.set("")
        self.patient_insurance_provider.set("")
        self.prescription.delete("1.0", tk.END)

    def exit_application(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create an instance of the application, passing the root window
    app = HospitalApp(root)

    # Start the application's main loop
    root.mainloop()