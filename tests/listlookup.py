import unittest
import ecs
import itertools

class ListLookupTest(unittest.TestCase):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");
        self.ListId = "21RRSXJATPANN"
    
    def testListFull(self):
        wishlist = ecs.ListLookup("WishList", self.ListId, ResponseGroup='ListItems')
        wl = list(wishlist)
        self.assertEqual(wl[0].Item.ASIN, '055277376X')
        self.assertEqual(len(wl),  40)


if __name__ == "__main__" :
    unittest.main()
