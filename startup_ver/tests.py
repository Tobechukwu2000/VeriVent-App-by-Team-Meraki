import unittest
import verify
class Unit(unittest.TestCase):

    def setUp(self):
        pass

    def test_verify_func(self):
        v=verify.verify_startup({'rcNumber':'RC09098','companyName':'seamfix',"verificationType":'RC-VERIFICATION'})
        print(type(v))
        self.assertTrue(type(v)=='dict')

if __name__=='__main__':
    unittest.main()