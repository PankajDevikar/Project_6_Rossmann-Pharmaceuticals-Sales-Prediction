import os
import sys
import unittest
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('C:\Data Science\project-6-Pharmaceutical\Rossmann-Sales\scripts')))
from file_handler import FileHandler


class TestDfHelper(unittest.TestCase):

    def setUp(self):
        self.helper = FileHandler()

    def test_to_csv(self):
        df = pd.DataFrame({'col1': range(1,4), 'col2': range(3,6)})
        self.helper.to_csv(df, 'C:\\Data Science\\project-6-Pharmaceutical\\Rossmann-Sales\\src\\data\\test.csv', False)
        df2 = pd.read_csv('test.csv')
        self.assertEqual(df.shape, df2.shape)

    def test_read_csv(self):
        df = self.helper.read_csv('test.csv')
        df2 = pd.read_csv('C:\\Data Science\\project-6-Pharmaceutical\\Rossmann-Sales\\src\\data\\test.csv')
        self.assertEqual(df.shape, df2.shape)

if __name__ == '__main__':
    unittest.main()