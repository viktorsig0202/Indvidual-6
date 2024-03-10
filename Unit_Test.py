import unittest
import Functions


# all the tests fail because the functions are not implemented!!!
class TestUserStories(unittest.TestCase):

    def test_User_Sign_up(self):
        """ "
        Test case for the User_Sign_Up function.

        This test checks if the user sign up process was a success or a fail.

        Input: - None

        Example:
        >>> assertTrue(result)

        Returns:
        - Bool
        """
        is_signed_in = Functions.User_Sign_Up()
        self.assertTrue(is_signed_in)

    def test_Montly_Calander(self):
        """
        Test case for the Montly_Calander function.

        This test checks if the montly Calander is not None.
        if it is None, the function failes.

        Input: - None

        Example:
        >>> assertIsNotNone(Montly_events)

        Returns:
        - Monthly_Calander: List containing events for the current month
        """
        monthly_events = Functions.Monthly_Calander()
        self.assertIsNotNone(monthly_events)

    def test_Reccomendation(self):
        """Test case for Reccomendation funciton.
        This test checks if the Reccomendation align with the users preferences.

        Input: - user_interests: A list containing the user_interests

        Example:
        >>> Reccomendation(["hiking"]) = "hiking_activity"
        assertEqual("hiking","hiking activity")
        """


if __name__ == "__main__":
    unittest.main()
