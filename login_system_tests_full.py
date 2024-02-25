import unittest
from login_system import *
from SystemCreator import *
from SystemManager import *
from SystemExporter import *

class LoginSystem_Tests(unittest.TestCase):
    
    # This will run before every test function
    def setUp(self):
        # Create an instance of the classes
        self.creator = SystemCreator()
        self.manager = SystemManager()
        self.exporter = SystemExporter()

        # Dictionaries for testing
        self.users, self.logged_in = self.creator.init_db('users.csv')
        
    def test_init_db(self):
        # Test total number of users in file
        self.assertEqual(10, len(self.users.keys()))

        # Test for couple of users
        self.assertIn('lbrandon', self.users)
        self.assertIn('chenyunw', self.users)

        # Test their passwords
        self.assertEqual('t39iSd_', self.users['kjain20'])
        self.assertEqual('_.R43sW2', self.users['caizhe'])

    def test_init_db_loggin(self):
        self.assertFalse(bool(self.logged_in))
        
    def test_check_username_password_valid_user(self):
        # Valid users with correct passwords
        self.assertTrue(self.manager.check_username_password(self.users, 'lbrandon', '2w3e4r5T'))
        self.assertTrue(self.manager.check_username_password(self.users, 'chenyunw', '9i8u7y6T'))

        # Valid user with incorrect password
        self.assertFalse(self.manager.check_username_password(self.users, 'chenyun','9i8u7y6T'))
        
    def test_check_username_password_valid_password(self):
        # Wrong passwords for existing users
        self.assertFalse(self.manager.check_username_password(self.users, 'huize', '9i2w6tqw1'))
        self.assertFalse(self.manager.check_username_password(self.users, 'haicao', 'QwertyuiI'))
        
    def test_is_valid_password_length(self):
        # Check password validity
        self.assertTrue(self.manager.is_valid_password('s.34r3T5'))
        self.assertTrue(self.manager.is_valid_password('8i7u6_T4'))
        self.assertFalse(self.manager.is_valid_password('0oiu87H'))
        
    def test_is_valid_password(self):
        # No lowercase char
        self.assertFalse(self.manager.is_valid_password('W2E3R4T5'))

        # No uppercase char
        self.assertFalse(self.manager.is_valid_password('6y5t4r3e_'))

        # No number
        self.assertFalse(self.manager.is_valid_password('sewdRty_'))

    def test_sign_up_valid_cases(self):
        # Successfully sign somebody in
        self.manager.sign_up(self.users, self.logged_in, 'steddy', 'b3rs6eR9')

        # Check if the user is in the database
        self.assertIn('steddy', self.users)
        self.assertEqual(self.users["steddy"],"b3rs6eR9")

        # Don't test logged_in as someone may not put not logged_in users into logged_in

    def test_sign_up_invalid_cases(self):
        # User exists
        self.manager.sign_up(self.users, self.logged_in, 'dingyis', '8d3wTR4_')
        # Check original username and password in db
        self.assertEqual(self.users["dingyis"], "2w9i4oT")

        # No uppercase in password
        self.manager.sign_up(self.users, self.logged_in, 'bryanj', '3267rt_o')
        # Not in the database
        self.assertNotIn("bryanj", self.users)

        # No lowercase in password
        self.manager.sign_up(self.users, self.logged_in, 'bryanj', '3267RT_O')
        # Still not in the database
        self.assertNotIn("bryanj", self.users)

        # No number in password
        self.manager.sign_up(self.users, self.logged_in, 'bryanj', 'REDDrt_o')
        # Still not in the database
        self.assertNotIn("bryanj", self.users)

        # Not enough chars in password
        self.manager.sign_up(self.users, self.logged_in, 'bryanj', '123ascD')
        # Still not in the database
        self.assertNotIn("bryanj", self.users)
        
    def test_log_in(self):
        # Successfully log somebody in
        self.manager.log_in(self.users, self.logged_in, 'caizhe', '_.R43sW2')
        self.assertIn('caizhe', self.logged_in)
        self.assertTrue(self.logged_in['caizhe'])

        # The same user logs in
        self.manager.log_in(self.users, self.logged_in, 'caizhe', '_.R43sW2')
        self.assertIn('caizhe', self.logged_in)
        self.assertTrue(self.logged_in['caizhe'])

        # User doesn't exist
        self.manager.log_in(self.users, self.logged_in, 'william', '9i8u7y65DW3')
        self.assertNotIn('william', self.logged_in)

        # Bad password
        self.manager.log_in(self.users, self.logged_in, 'kjain20', '_t39iSd_')
        self.assertNotIn('kjain20', self.logged_in)

    def test_change_password(self):
        self.manager.change_password(self.users, 'paranyaj', 'bvcxZs43', 'rwt23eWW1')
        self.assertEqual('rwt23eWW1', self.users['paranyaj'])

        # Wrong old password
        self.manager.change_password(self.users, 'paranyaj', 'bvcxZs43', '0o9i8u7Y')
        self.assertEqual('rwt23eWW1', self.users['paranyaj'])

    def test_delete_account(self):
        self.manager.delete_account(self.users, self.logged_in, 'chenyunw', '9i8u7y6T')
        self.assertNotIn('chenyunw', self.users)
        self.assertNotIn('chenyunw', self.logged_in)

        # Bad password
        self.manager.delete_account(self.users, self.logged_in, 'kjain20', 't39iSd')
        self.assertIn('kjain20', self.users)

        # User doesn't exist
        self.manager.delete_account(self.users, self.logged_in, 'sarahq', '1234rftY')
        self.assertNotIn('sarahq', self.users)
        self.assertNotIn('sarahq', self.logged_in)

    def test_get_sign_ups(self):
        names = ["lbrandon", "chenyunw", "dingyis", "caizhe", "chuanrui", "kjain20", "huize", "paranyaj", "caor", "tianshiw"]
        self.assertCountEqual(names, self.manager.get_sign_ups(self.users))

        # Sign up one user
        self.manager.sign_up(self.users, self.logged_in, 'steddy', 'b3rs6eR9')
        names.append("steddy")
        self.assertCountEqual(names, self.manager.get_sign_ups(self.users))

        # Delete one user
        self.manager.delete_account(self.users, self.logged_in, 'steddy', 'b3rs6eR9')
        names = ["lbrandon", "chenyunw", "dingyis", "caizhe", "chuanrui", "kjain20", "huize", "paranyaj", "caor", "tianshiw"]
        self.assertCountEqual(names, self.manager.get_sign_ups(self.users))

    def test_get_log_in(self):
        # Log in
        self.manager.log_in(self.users, self.logged_in, 'caizhe', '_.R43sW2')
        self.manager.log_in(self.users, self.logged_in, 'chenyunw', '9i8u7y6T')
        self.assertCountEqual(["caizhe", "chenyunw"], self.manager.get_log_ins(self.logged_in))

        # Delete 
        self.manager.delete_account(self.users, self.logged_in, 'chenyunw', '9i8u7y6T')
        self.assertCountEqual(["caizhe"], self.manager.get_log_ins(self.logged_in))

    def test_write(self):
        self.exporter.write_users_db(self.users, "output.txt")

if __name__ == '__main__':
    unittest.main()