import unittest
import os
import requests
import json
from unittest import mock
from src.HW05_SSW567_ZiyuZhang import GithubReader


def mocked_requests_get(*args, **kwargs):
    rep_dir = os.path.join(os.getcwd(), "docs", "GitRepoResponse.json")
    cmt_dir = os.path.join(os.getcwd(), "docs", "GitCommitResponse.json")
    fp_rep = open(rep_dir, 'r')
    fp_cmt = open(cmt_dir, 'r')

    class MockResponse():
        def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
                self.text = json.dumps(json_data)

        def json(self):
            return json.dumps(self.json_data, indent=4)

    if args[0].startswith("https://api.github.com/users/"):
        return MockResponse(json.load(fp_rep), 200)
    elif args[0].startswith("https://api.github.com/repos/"):
        return MockResponse(json.load(fp_cmt), 200)

    return MockResponse(None, 400)


class TestHW04(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_hw05(self, mockedReq):
        repo = GithubReader()
        dic = repo.get_commits()
        self.assertEqual(set(dic.items()), {('PublicFeeSys', 2), ('SSW540Practice', 3), ('SSW555_TeamPrj', 30), ('SSW565AssignmentG1', 2), ('SSW567_Codes', 1), ('ssw690ossmgmt', 29), ('SSW810Practice', 10), ('Structure', 1)})


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
