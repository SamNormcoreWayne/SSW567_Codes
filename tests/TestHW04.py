import unittest
import requests
from src.HW04_SSW567_ZiyuZhang import GithubReader


class TestHW04(unittest.TestCase):
    def test_hw04(self):
        repo = GithubReader()
        dic = repo.get_commits()
        self.assertEqual(set(dic.items()), {('PublicFeeSys', 2), ('SSW540Practice', 3), ('SSW555_TeamPrj', 30), ('SSW565AssignmentG1', 2), ('SSW567_Codes', 1), ('ssw690ossmgmt', 29), ('SSW810Practice', 10), ('Structure', 1)})
        with self.assertRaises(requests.exceptions.MissingSchema):
            GithubReader("IBetThereIsNoUserCalledThisIDLOL")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)