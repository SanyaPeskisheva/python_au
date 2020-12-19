import unittest
from generator.generator_md import *

class TestLeetCodeSolution(unittest.TestCase):
    def test_title(self):
        in_txt = read_all_lines_from('src.txt')
        text = LeetCodeSolution(in_txt[0],in_txt[1],in_txt[3:])
        res = text.get_md_title()
        self.assertEqual(res, '## Valid Anagram\n')
    def test_link(self):
        in_txt = read_all_lines_from('src.txt')
        text = LeetCodeSolution(in_txt[0], in_txt[1], in_txt[3:])
        res = text.get_md_solution_link()
        self.assertEqual(res, '+ [Valid Anagram](#valid-anagram)')
    def test_sol(self):
        in_txt = read_all_lines_from('src.txt')
        text = LeetCodeSolution(in_txt[0], in_txt[1], in_txt[3:])
        res = text.get_md_formatted_solution()
        self.assertEqual(res, '## Valid Anagram\n\n+ [Valid Anagram](#valid-anagram)\n\nhttps://leetcode.com/problems/valid-anagram/\n\n``` python\ndef Valid Anagram(self, s: str, t: str) -> bool:\n    first = []\n```\n')
