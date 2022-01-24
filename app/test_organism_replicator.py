import unittest, io
from unittest import mock
from unittest.mock import patch
from organism_replicator import OrganismReplicator

# unittest.testcase == TestCase is the PARENT class, TestOrganism is the SUBCLASS of test case
# https://docs.python.org/3/library/unittest.html#unittest.TestCase


class TestOrganismReplicator(unittest.TestCase):
    def setUp(self) -> None:
        self.replicator = OrganismReplicator()

    def clear_string_io(self, mock_stdout):
        mock_stdout.truncate(0)
        mock_stdout.seek(0)

    def test_organism_class_can_instantiate(self):
        self.assertIsNotNone(self.replicator)
    
    # https://docs.python.org/3/library/unittest.mock-examples.html?highlight=mock
    # USE TO HELP WITH MOCKING USER INPUT FOR TESTS
    def test_get_user_input_for_variables(self):
        fake_input = unittest.mock.Mock(side_effect=['5', '10', '15'])
        with unittest.mock.patch('builtins.input', fake_input):
            user_input_variables = self.replicator.get_user_input_for_variables()
            self.assertEqual(user_input_variables, {'number_of_days': '5', 'rate_of_replication': '10', 'starting_organisms': '15'})

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_user_input_variables(self, mock_stdout):
        user_input_variables = {'number_of_days': '5', 'rate_of_replication': '10', 'starting_organisms': '15'}
        validate_user_input_variables = self.replicator.validate_user_input_variables(user_input_variables)
        self.assertTrue(validate_user_input_variables)

        user_input_variables = {'number_of_days': 'five', 'rate_of_replication': '$%^&', 'starting_organisms': ',.?'}
        expected_output = 'Wrong input entered for Number of Days, please enter a whole number: \n'
        self.validate_bad_user_input(user_input_variables, expected_output, mock_stdout)

        user_input_variables = {'number_of_days': '5', 'rate_of_replication': '$%^&', 'starting_organisms': ',.?'}
        expected_output = 'Wrong input entered for Rate of Replication, please enter a whole number: \n'
        self.validate_bad_user_input(user_input_variables, expected_output, mock_stdout)

        user_input_variables = {'number_of_days': '5', 'rate_of_replication': '10', 'starting_organisms': '^&*'}
        expected_output = 'Wrong input entered for Starting Organisms, please enter a whole number: \n'
        self.validate_bad_user_input(user_input_variables, expected_output, mock_stdout)
    
    def validate_bad_user_input(self, user_input_variables, expected_output, mock_stdout):
        validate_user_input_variables = self.replicator.validate_user_input_variables(user_input_variables)
        output = mock_stdout.getvalue()
        self.assertEqual(output, expected_output)
        self.clear_string_io(mock_stdout)
        self.assertFalse(validate_user_input_variables)


    def test_convert_input_to_int(self):
        pass

    def test_get_valid_input_int(self):
        pass
    
    def test_calculate_replication_for_each_day(self):
        pass

    def test_calculate_replication_for_total_organisms(self):
        pass

    def test_print_replication_results(self):
        pass


if __name__ == '__main__':
    unittest.main()
