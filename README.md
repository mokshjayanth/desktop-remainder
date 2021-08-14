# PyReminder
**A Simple Reminder Application for Windows OS.**

![](https://i.postimg.cc/KjkjX7pd/Xnip2021-08-14-18-14-15.jpg "")

## About this Project
PyReminder is a Reminder Application Mini-Project built using Python. The Application sends a pop-up notification in Windows by referring to Tasks and Time entered by the user in an Excel Sheet.


## Setting up the Application
#### 1. Install the following required python packages
- `Pandas` : _pip install pandas_
- `Plyer` : _pip install plyer_

#### 2. Run your application in the background
Type the following command in command prompt to make your application run in the background.

    pythonw.exe .\desktopReminder.py
    
## Setting the Reminders

- Open `Reminder_Sheet.xlsx` 
- To add a new reminder, enter the name of the task and its details in the Excel sheet.
- Enter the time of the task under the `Time` column of the sheet in `24-hour clock` format.
- Save the Excel sheet and exit.

[_Excel Sheet Format_](https://postimg.cc/94hC0scw).

## Closing the Application

- Kill the process named `Python` in the Windows Task Manager in order to Stop the Application.

[_Reference image_](https://postimg.cc/p9YVJsp5).

## Documentation References
- [`Pandas`](https://pandas.pydata.org/)
- [`Plyer`](https://plyer.readthedocs.io/en/latest/)
- [`Datetime`](https://www.guru99.com/date-time-and-datetime-classes-in-python.html)
