import tkinter 
from tkinter import ttk
import dataFrame
import os
import openpyxl

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack() # packing the frame into the window

#saving user information in a variable
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)


#widgest for user information
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

#user enters input
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

#list from  which user can select
title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=[" ", "Mr.", "Ms.", "Dr.", "Prof."])
title_label.grid(row=1, column=2)
title_combobox.grid(row=1, column=2) # drop down box for title selection


age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox =  tkinter.Spinbox(user_info_frame, from_=18, to=110) # spinbox is a counter
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", 
                                        variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")


registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Accept terms and conditions
accept_var = tkinter.StringVar(value="Not Accepted")

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#Buttons
button = tkinter.Button(frame, text="Enter data", command=lambda: dataFrame.enter_data(
    first_name_entry, last_name_entry, title_combobox, age_spinbox, 
    nationality_combobox, registered_check, numcourses_spinbox, 
    numsemesters_spinbox, terms_check, reg_status_var, accept_var
))
button.grid(row=3, column=0, sticky='news', padx=20, pady=10) 

window.mainloop()