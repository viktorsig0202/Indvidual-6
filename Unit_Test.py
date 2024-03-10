import unittest
import Functions

class TestUserStories(unittest.TestCase):

    def test_User_Sign_up(self):
        """" Test case for the User_Sign_Up function.
        This tests checks if the user sign up process was a success or a fail
        Example:
        >>> assertTrue(result)

        Returns: Bool
        """
        result = Functions.User_Sign_Up()
        self.assertTrue(result)



if __name__ == "__main__":
    unittest.main()