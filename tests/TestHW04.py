import unittest
from src.HW04_SSW567_ZiyuZhang import GithubReader


class TestHW04(unittest.TestCase):
    def test_hw04(self):
        user = input("Input user name:")
        pwd = input("Input user password")
        repo = GithubReader(user=user, pwd=pwd)
        dic = repo.get_commits()
        self.assertEqual(set(dic.items()), {('PublicFeeSys', 2), ('SSW540Practice', 3), ('SSW555_TeamPrj', 30), ('SSW565AssignmentG1', 2), ('SSW567_Codes', 1), ('ssw690ossmgmt', 1), ('SSW810Practice', 10), ('Structure', 1)})


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)