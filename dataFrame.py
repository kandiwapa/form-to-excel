import tkinter
from tkinter import messagebox
import os
import openpyxl


def enter_data(first_name_entry, last_name_entry, title_combobox, age_spinbox, 
               nationality_combobox, registered_check, numcourses_spinbox, 
               numsemesters_spinbox, terms_check, reg_status_var, accept_var):
    """Collect user information from form widgets"""
    accepted = accept_var.get()
   

    if accepted=="Accepted":
        # User information
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
        
        # Course information
            registration_status = reg_status_var.get()
            num_courses = numcourses_spinbox.get()
            num_semesters = numsemesters_spinbox.get()
        
        # Print or process the data
            print(f"First Name: {firstname}")
            print(f"Last Name: {lastname}")
            print(f"Title: {title}")
            print(f"Age: {age}")
            print(f"Nationality: {nationality}")
            print(f"Completed Courses: {num_courses}")
            print(f"Semesters: {num_semesters}")
            print(f"Registration status: {registration_status}")
            print("--------------------------------------------")


            filepath = "../form-to-excel/data.xlsx"

            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["firstname", "Last Name", "Title", "Age", "Nationality", 
                            "# Courses", "# Semesters", "Registration Status"]
                sheet.append(heading)
                workbook.save(filepath)

            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([firstname, lastname, title, age, nationality, num_courses, num_semesters, registration_status])
            workbook.save(filepath)

        else:
            tkinter.messagebox.showwarning(title="Oopssie Dasi", message=" You have not Entered firstname or Lastname")

    else:
        tkinter.messagebox.showwarning(title="Oopssie Dasi", message=" T&C")


       
