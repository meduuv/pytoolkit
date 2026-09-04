import unittest
from pytoolkit import coalesce, ensure_list
class Tests(unittest.TestCase):
    def test_coalesce(self): self.assertEqual(coalesce(None,None,3),3)
    def test_list(self): self.assertEqual(ensure_list(4),[4]); self.assertEqual(ensure_list((1,2)),[1,2])
if __name__=="__main__": unittest.main()
