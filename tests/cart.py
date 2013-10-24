import unittest
import ecs
import itertools


class CartTest( unittest.TestCase ):
    def setUp(self):
        # prepare the python books to add 
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");
        iter = ecs.ItemSearch("python", SearchIndex="Books")
        self.books = [x for x in itertools.islice(iter, 0, 9)]
        self.cart = None

    def testCartCreate(self):
        items = (self.books[0], self.books[1], self.books[2])
        qs = (1, 3, 5)

        self.cart = ecs.CartCreate(items, qs)
        for i in range(3):
            self.assertEqual(self.books[i].ASIN, self.cart.CartItems[i].ASIN)
            self.assertEqual(qs[i], int(self.cart.CartItems[i].Quantity))

    def testCartAdd(self):
        self.testCartCreate() 

        l = []
        for x in self.cart.CartItems:
            z = (x.ASIN, int(x.Quantity))
            l.append(z)
            
        items = (self.books[5], self.books[8])
        qs = (5, 8)
        z = (self.books[5].ASIN, 5)
        l.append(z)
        z = (self.books[8].ASIN, 8)
        l.append(z)

        self.cart = ecs.CartAdd(self.cart, items, qs)

        # check the item
        for item in self.cart.CartItems:
            self.assert_( (item.ASIN, int(item.Quantity)) in l)

    def testCartGet(self):
        self.testCartCreate() 

        cart = ecs.CartGet(self.cart)
        for i in range(len(cart.CartItems)):
            self.assertEqual(self.cart.CartItems[i].ASIN, cart.CartItems[i].ASIN)
            self.assertEqual(self.cart.CartItems[i].Quantity, cart.CartItems[i].Quantity)

    def testCartModify(self):
        self.testCartCreate()

        cart = ecs.CartModify(self.cart, (self.cart.CartItems[1], self.cart.CartItems[2]), (10, 'SaveForLater'))
        # Item 0 is the same
        self.assertEqual(self.cart.CartItems[0].Title, cart.CartItems[0].Title)
        self.assertEqual(self.cart.CartItems[0].Quantity, cart.CartItems[0].Quantity)
        # Item 1: Quantity is different
        self.assertEqual(self.cart.CartItems[1].Title, cart.CartItems[1].Title)
        self.assertEqual(10, int(cart.CartItems[1].Quantity))
        
        # Item 2: saved for later
        self.assertEqual(2, len(cart.CartItems))
        self.assertEqual(cart.SavedForLaterItems[0].Title, self.cart.CartItems[2].Title)
        self.assertEqual(cart.SavedForLaterItems[0].Quantity, self.cart.CartItems[2].Quantity)

    def testCartClear(self):
        self.testCartCreate()

        cart = ecs.CartModify(self.cart, (self.cart.CartItems[1], self.cart.CartItems[2]), (10, 'SaveForLater'))
        cart = ecs.CartClear(cart)
        self.failIf(hasattr(cart, 'CartItems'))
        self.failUnless(hasattr(cart, 'SavedForLaterItems'))


if __name__ == "__main__" :
    unittest.main()
