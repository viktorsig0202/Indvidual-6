import unittest
import Functions


class TestUserStories(unittest.TestCase):

    def test_User_Sign_up(self):
        """
        Test case for the User_Sign_Up function.
        This test checks if the user sign up process was a success or a fail.

        Example:
        >>> assertTrue(result)

        Returns:
        Bool: True if the signup procces is successful and False if it fails
        """
        is_signed_in = Functions.User_Sign_Up()
        is_signed_in2 = Functions.User_Sign_Up("John05", "password123")
        self.assertTrue(is_signed_in)
        self.assertTrue(is_signed_in2)

    def test_Montly_Calander(self):
        """
        Test case for the Montly_Calander function.
        This test checks if the montly Calander is not None.
        if it is None, the function failed.

        Example:
        >>> assertIsNotNone(Montly_events)

        Returns:
        List: List containing events for the current month
        """
        monthly_events = Functions.Monthly_Calander()
        self.assertIsNotNone(monthly_events)

    def test_Reccomendation(self):
        """
        Test case for Reccomendation funciton.
        This test checks if the Reccomendation align with the users preferences.

        Args:
        user_interest(str): one of the user's interests

        Example:
        >>> Reccomendation("hiking") = "hiking_activity"
        assertTrue("hiking" in "hiking activity")

        Returns:
        Str: an activity that the system reccomends to the user
        """
        interest1 = "hiking"
        interest2 = "river rafting"
        result1 = Functions.Reccomendations(interest1)
        result2 = Functions.Reccomendations(interest2)
        self.assertTrue(interest1 in result1)
        self.assertTrue(interest2 in result2)

    def test_Comment_On_Activity(self):
        """
        Test case for Comment_On_Activity function.
        this checks if the comment matched the comment on the activity

        Args:
        comment(string): the comment the user wants to post on the activity

        Example:
        >>> comment = "string" -> Result = Comment_On_Activity(comment)
        assertisNotNone(Result)

        Returns:
        string: the comment which is posted on the activity
        """
        self.assertIsNotNone(Functions.Comment_On_Activity("i loved it"))
        self.assertIsNotNone(Functions.Comment_On_Activity("expensive!"))
        self.assertIsNotNone(Functions.Comment_On_Activity(""))


if __name__ == "__main__":
    unittest.main()
