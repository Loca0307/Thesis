import unittest
from unittest.mock import patch, mock_open, MagicMock

from user_manager import get_all_users, new_user, get_user_info, delete_user, update_username, add_win, add_played_game, \
    add_fail, find_user, save_user, merge_json_files


class TestUserManager(unittest.TestCase):

    @patch('user_manager.glob.glob', return_value=['user1.json', 'user2.json', 'users.json'])
    @patch('builtins.open', new_callable=mock_open, read_data='[{"username": "user1"}, {"username": "user2"}]')
    def test_get_all_users(self, mock_file, mock_glob):
        users = get_all_users()
        self.assertIn('user1.json', users)
        self.assertIn('user2.json', users)
        self.assertNotIn('users.json', users)

    @patch('user_manager.glob.glob', return_value=['user1.json'])
    @patch('builtins.open', new_callable=mock_open)
    def test_new_user(self, mock_file, mock_glob):
        new_user('user2')
        mock_file.assert_called_with('user2.json', 'w')

    @patch('user_manager.glob.glob', return_value=['user1.json'])
    @patch('builtins.open', new_callable=mock_open,
           read_data='{"username": "user1", "played_games": 0, "nbfail": 0, "nbwin": 0}')
    def test_get_user_info(self, mock_file, mock_glob):
        with patch('builtins.print') as mocked_print:
            get_user_info('user1')
            mocked_print.assert_called_with('User user1 have never played')

    @patch('user_manager.glob.glob', return_value=['user1.json'])
    @patch('os.remove')
    def test_delete_user(self, mock_remove, mock_glob):
        with patch('builtins.print') as mocked_print:
            delete_user('user1')
            mock_remove.assert_called_with('user1.json')
            mocked_print.assert_called_with('User user1 has been successfully deleted')

    @patch('user_manager.glob.glob', return_value=['user1.json'])
    @patch('builtins.open', new_callable=mock_open, read_data='{"username": "user1"}')
    @patch('os.rename')
    def test_update_username(self, mock_rename, mock_file, mock_glob):
        with patch('builtins.print') as mocked_print:
            update_username('user1', 'user2')
            mock_rename.assert_called_with('user1.json', 'user2.json')
            mocked_print.assert_called_with(' The username user1 has been changed to user2')

    @patch('user_manager.glob.glob', return_value=['user1.json'])
    @patch('builtins.open', new_callable=mock_open, read_data='{"username": "user1", "nbwin": 0}')
    def test_add_win(self, mock_file, mock_glob):
        add_win('user1')
        mock_file().write.assert_called()

    @patch('user_manager.glob.glob', return_value=['user1.json'])
    @patch('builtins.open', new_callable=mock_open, read_data='{"username": "user1", "played_games": 0}')
    def test_add_played_game(self, mock_file, mock_glob):
        add_played_game('user1')
        mock_file().write.assert_called()

    @patch('user_manager.glob.glob', return_value=['user1.json'])
    @patch('builtins.open', new_callable=mock_open, read_data='{"username": "user1", "nbfail": 0}')
    def test_add_fail(self, mock_file, mock_glob):
        add_fail('user1')
        mock_file().write.assert_called()

    @patch('user_manager.glob.glob', return_value=['user1.json'])
    def test_find_user(self, mock_glob):
        self.assertTrue(find_user('user1'))
        self.assertFalse(find_user('user2'))

    @patch('builtins.open', new_callable=mock_open)
    def test_save_user(self, mock_file):
        user = MagicMock()
        user.username = 'user1'
        user.played_games = 0
        user.nbfail = 0
        user.nbwin = 0
        user.greatest_score = 0
        save_user(user)
        mock_file.assert_called_with('user1.json', 'w')

    @patch('builtins.open', new_callable=mock_open, read_data='{"username": "user1"}')
    def test_merge_json_files(self, mock_file):
        merge_json_files(['user1.json'])
        mock_file.assert_called_with('users.json', 'w')


if __name__ == '__main__':
    unittest.main()