import unittest
import Functions


# all the tests fail because the functions are not implemented!!!
class TestUserStories(unittest.TestCase):

    def test_User_Sign_up(self):
        """
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
        """
        Test case for Reccomendation funciton.
        This test checks if the Reccomendation align with the users preferences.

        Input: - user_interests: A list containing the user_interests

        Example:
        >>> Reccomendation(["hiking"]) = "hiking_activity"
        assertEqual("hiking","hiking activity")

        Returns:
        - Activity: a string that the system reccomends to the user
        """
        interests = ["climbing"]
        result = Functions(interests)
        self.assertEqual(interests, result)

    def test_Comment_On_Activity(self):
        """
        Test case for Comment_On_Activity funciton.
        this checks if the comment matched the comment on the activity

        Input: - comment: string

        Example:
        >>> comment = "string" -> Result = Comment_On_Activity(comment)
        assertEqual(comment,Result)

        Returns:
        -comment_on_activity: a string comment on the on the activity
        """
        comment = "I Really Liked it!"
        comment_on_activity = Functions.Comment_On_Activity(comment)
        self.assertEqual(comment, comment_on_activity)


if __name__ == "__main__":
    unittest.main()
