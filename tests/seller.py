import unittest, os
import ecs

class SellerTest(unittest.TestCase):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");

    def testSellerLookup(self):
        # TODO: We need another SellerId here
        sellers = ecs.SellerLookup(['A3ENSIQ3ZA4FFN'])
        for s in sellers:
            self.assertEqual(s.Nickname, 'abebooks')
            break
'''
    def testSellerListingSearch(self):
        sl = ecs.SellerListingSearch('A3ENSIQ3ZA4FFN', Title='Paperback')
        for s in sl:
            self.assertNotEqual(s, None)

    def testSellerListingLookup(self):
        sellerId = 'A3ENSIQ3ZA4FFN'
        sl = ecs.SellerListingSearch(sellerId, Title='Paperback')
        for s in sl:
            id = s.ListingId
            sll = ecs.SellerListingLookup(sellerId, id)
            for x in sll:
                for y in ['ASIN', 'Condition', 'EndDate', 'ExchangeId', 'ListingId', 'Price', 'Quantity', 'Seller', 'StartDate', 'Status', 'SubCondition', 'Title']:
                    self.assertNotEqual(getattr(x, y), None)
            break
'''      

if __name__ == "__main__" :
    unittest.main()
