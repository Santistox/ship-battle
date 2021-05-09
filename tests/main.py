"""
Main Unit Tests file for this project.
Any unit test checks a small component of this project

If you’re using the PyCharm IDE, you can run unittest by following these steps:
1. In the Project tool window, select the tests directory.
2. On the context menu, choose the run command for unittest. For example, choose Run ‘Unittests in my Tests…’.

If you’re using the Microsoft Visual Studio Code IDE, support for unittest execution is built into the Python plugin.
And if you have the Python plugin installed,  you can run unittest by following these steps:
1. Set up the configuration of your tests by opening the 'Command Palette' with Ctrl+Shift+P and typing “Python test”.
2. Choose Debug All Unit Tests, and VSCode will then raise a prompt to configure the test framework.
3. Click on the cog to select the test runner (unittest) and the home directory (.)
4. Once this is set up, you will see the status of your tests at the bottom of the window,
and you can quickly access the test logs and run the tests again by clicking on these icons.

All tests were written by Aleksandr Gerasimov github.com@Santistox
Found a bug? Contact me santistox@inbox.com 
(Please write in subject your letter the name of the project e.g. "[BUG] ShipBattle: timer set incorrectly")
"""
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()