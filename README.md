# Employee-Management-System
Employee Management System Using Python Tkinter
This is a GUI-based Employee Management System implemented using the Tkinter library in Python. It includes functionalities such as adding employees, searching employees, deleting employees, updating employee information, and exporting employee data.
Here is a breakdown of the code:
The required libraries are imported at the beginning of the code: sqlite3, tkinter, time and pandas.
Several functions are defined to handle different actions in the Employee Management System:
clock(): Updates the date and time displayed on the GUI.
add_employee(): Opens a new window to add an employee to the database.
search_employee(): Opens a new window to search for employees based on specified criteria.
delete_employee(): Deletes the selected employee from the database.
update_employee(): Opens a new window to update the information of a selected employee.
show_employee(): Retrieves and displays all employees' data from the database.
export_data(): Allows exporting employee data to a CSV file.
iexit(): Exits the application after confirming with the user.
A connection to the SQLite database is established, and a table named "Employees" is created to store employee information.
The GUI elements are created using the Tkinter library. The main window is created with a fixed size of 1280x700 pixels. The title and date/time label are displayed at the top.
The left frame of the window contains a logo image.
Other GUI elements, such as buttons and labels, are placed in the main window using various layouts and grid configurations.
Overall, this code provides the basic structure and functionality of an Employee Management System using Tkinter and SQLite. However, there are a few areas where improvements and error handling could be added, such as proper exception handling, input validation, and data formatting.
