import unittest
class OurTest(unittest.TestCase):
    def setUp(self):
        self.a=1
        self.b=2
        self.result=3
    def test_add(self):
        run_result=self.a+self.b
        self.assertEqual(run_result,self.result,"self.a+self.b不等于3")
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()