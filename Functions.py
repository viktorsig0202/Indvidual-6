def User_Sign_Up(username="", password=""):
    """
    Function to simulate user sign up process.

    Args:
    username(str): name object
    password(str): password object

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


def Reccomendations(user_interest):
    """
    Function to generate Reccomended activities based on user interests.

    Args:
    user_interest(str): one of the user intrests

    Returns:
    str: the activity the system reccomends
    """
    if user_interest:
        if user_interest == "hiking":
            return "Sign up to hiking in hvammsdalur"
        elif user_interest == "river rafting":
            return "attend river rafting at Siglufjörður"
        elif user_interest == "kayaking":
            return "attend kayaking at jökulsárlón"
        else:
            return "Try something new"
    else:
        return "No reccomendations (try again!)"


def Comment_On_Activity(comment: str):
    pass
