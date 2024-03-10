import unittest
import Functions

# all the tests fail because the functions are not implemented!!!
class TestUserStories(unittest.TestCase):

    def test_User_Sign_up(self):
        """" Test case for the User_Sign_Up function.
        This test checks if the user sign up process was a success or a fail
        Example:
        >>> assertTrue(result)

        Returns: type(Bool)
        """

        is_signed_in = Functions.User_Sign_Up()
        self.assertTrue(is_signed_in)

    def test_Montly_Calander(self):
        """ Test case for the Montly_Calander function.
        This test checks if the montly Calander is not None
        if it is None the function failed
        Example:
        >>> assertIsNotNone(Montly_events)

        Returns: type(string)
        """

        monthly_events = Functions.Monthly_Calander()
        self.assertIsNotNone(monthly_events)



if __name__ == "__main__":
    unittest.main()

