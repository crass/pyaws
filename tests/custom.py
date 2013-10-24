import unittest
import ecs

class CustomerTest(unittest.TestCase):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");

    def testCustomerContentSearch(self):
        cs = ecs.CustomerContentSearch('Sam', None, 1)
        self.assertEqual(len(cs), 20)
        self.assertNotEqual(cs[0].CustomerId, '')

if __name__ == "__main__" :
    unittest.main()
