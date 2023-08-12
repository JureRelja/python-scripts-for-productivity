import datetime
import inquirer

#User chooses the date and year
def selectDateYear():
    #Getting the current month, day and year
    currentYear = datetime.datetime.now().year
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month

    dateSelect = [
    inquirer.List('option',
                    message="Datum objave",
                    choices=['Današnji datum', "Odaberi datum"],
                ),
    ]

    dateOption = inquirer.prompt(dateSelect)

    if (dateOption["option"] == "Odaberi datum"):   
        currentYear = int(input("Unesi godinu: (2015-" + str(currentYear) + ") "))
        month = int(input("Unesi mjesec: (1-12) "))
        day = int(input("Unesi dan: (1-31) "))

    return {"year": currentYear, "day": day, "month": month}