import tkinter as tk

class Patient:
    def __init__(self):
        self.data = {
            "id": tk.StringVar(),
            "name": tk.StringVar(),
            "gender": tk.StringVar(),
            "age": tk.StringVar(),
            "dob": tk.StringVar(),
            "address": tk.StringVar(),
            "blood_group": tk.StringVar(),
            "language_pref": tk.StringVar(),
            "access_req": tk.StringVar(),
            "insurance_provider": tk.StringVar(),
            "prescribed_med": tk.StringVar(),
            "weight": tk.StringVar(),
            "height": tk.StringVar(),
            "additional_notes": tk.StringVar()
        }
