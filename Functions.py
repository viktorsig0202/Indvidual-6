def User_Sign_Up(username="", password=""):
    """
    Function to simulate user sign up process.

    Args:
    username(str): name object
    password(wtr): password object

    Returns:
    bool: True if the sign-up process is successful, False otherwise.
    """
    if username and password:
        return True
    else:
        return False


def Monthly_Calander():
    """
    Function to generate montly calender event

    Returns:
    List: List containing events for the current month
    """
    import datetime

    schedule = {
        "January": ["Skiing", "Snowmobiling"],
        "February": ["Ice climbing", "Winter hiking"],
        "March": ["Glacier hiking", "Snowshoeing"],
        "April": ["Volcano trekking", "Cave exploration"],
        "May": ["Kayaking", "Whale watching"],
        "June": ["River rafting", "Camping"],
        "July": ["Hiking", "Hot springs visit"],
        "August": ["Rock climbing", "Fishing"],
        "September": ["Mountain biking", "Northern Lights tour"],
        "October": ["Horseback riding", "Geothermal spa"],
        "November": ["ATV tour", "Bird watching"],
        "December": ["Dog sledding", "Ice cave tour"],
    }
    current_date = datetime.datetime.now()

    current_month = current_date.strftime("%B")

    return schedule[current_month]


def Reccomendations(intrests: list):
    pass


def Comment_On_Activity(comment: str):
    pass


Result = Monthly_Calander()
print(Result)
