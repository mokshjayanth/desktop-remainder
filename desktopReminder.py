import pandas as pd
from datetime import datetime
from plyer import notification
import time

def notifyMe(title, message,icon):
    notification.notify(
        title=title, 
        message=message, 
        app_icon = icon,
        timeout=10)

icon = "Bell.ico"

if __name__ == '__main__':
    notifyMe("Hello!","This is Python Desktop Reminder App.\nPlease Enter the Reminders in the Excel Sheet. Happy Working :)",icon)
    
    df = pd.read_excel("Reminder_Sheet.xlsx")
    df["Heading"] = df.loc[:,"Heading"].astype(str)
    df["Message"] = df.loc[:,"Message"].astype(str)
    number_of_rows = len(df.index)
    
    while True:
    #checks for new notifications once for every minute.
        if datetime.now().strftime("%S")=='00':
            df = pd.read_excel("Reminder_Sheet.xlsx")
            number_of_rows = len(df.index) 
            for index in range(0,number_of_rows):
                now = datetime.now().strftime("%H:%M:%S")
                x = df['Time'][index].strftime("%H:%M:%S")
                if x==now:
                    if df["Message"][index]=="nan":
                        df["Message"][index]=""
                    if df["Heading"][index]=="nan":
                        df["Heading"][index]=""
                    notifyMe(df['Heading'][index], df['Message'][index], icon)
            time.sleep(60) #Sleep for 60 seconds