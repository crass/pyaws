import unittest
import ecs
import itertools

class ItemLookupTest(unittest.TestCase):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");
        self.ItemId = "0596009259"
    
    def assertIsInteger(self, n, message=None):
        try:
            int(n)
        except :
            fail(message)
            
    def testSmall(self):
        book = ecs.ItemLookup(self.ItemId, ResponseGroup='Request,Small')
        self.assertNotEqual(book, None)

        self.assertEqual(book.ASIN, '0596009259')
        self.assertEqual(book.Title, 'Programming Python')
        self.assertEqual(book.Manufacturer, "O'Reilly Media, Inc.")
        self.assertEqual(book.ProductGroup, 'Book')
        self.assertEqual(book.Author, 'Mark Lutz')

    def testMedium(self):
        book = ecs.ItemLookup(self.ItemId, ResponseGroup='Request,Medium')

        self.assertEqual(book.ASIN, '0596009259')
        self.assertEqual(book.Title, 'Programming Python')
        self.assertEqual(book.Manufacturer, "O'Reilly Media, Inc.")
        self.assertEqual(book.ProductGroup, 'Book')
        self.assertEqual(book.Author, 'Mark Lutz')

        # EditorialReview
        self.assertEqual(len(book.EditorialReviews), 2)
        self.assertEqual(book.EditorialReviews[0].Source, 'Product Description')
        self.assertEqual(book.EditorialReviews[1].Source, 'Amazon.com')

        # Images 
        self.assertEqual(len(book.ImageSets), 1)
        self.assertEqual(book.ImageSets[0].LargeImage.Height, '500')
        self.assertEqual(book.ImageSets[0].MediumImage.Height, '160')
        self.assertEqual(book.ImageSets[0].SmallImage.Height, '75')

        # ItemAttributes
        pass

        # ItemIds
        pass

        # OfferSummary
        self.assertNotEqual(book.OfferSummary.TotalNew, '0')
        self.assertIsInteger(book.OfferSummary.LowestNewPrice.Amount, 
            'book.OfferSummary.LowestNewPrice.Amount is not integer')

        # SalesRank
        self.assertNotEqual(book.SalesRank, '0')

    def testAccessories(self):
        # We have to use Palm Tungsten X
        tx = ecs.ItemLookup('B000BI7NHY', ResponseGroup='Accessories')
        self.assertNotEqual(tx.Accessories[4].ASIN, '')

    def testBrowseNodes(self):
        book = ecs.ItemLookup(self.ItemId, ResponseGroup='BrowseNodes')
        self.assertEqual(len(book.BrowseNodes), 11)
        bn = book.BrowseNodes[0]
        # iterate all the ancestors
        names = ('Programming', "Web Development", 'Computers & Internet')
        for x in names:
            self.assertEqual(bn.Name, x)
            bn = bn.Ancestors[0]

    def testLarge(self):
        #books = ecs.ItemLookup(self.ItemId, ResponseGroup='Large')
        pass
    
    def testListmaniaLists(self):
        # TODO: need to find the item with this attributes
        pass

    def testOfferFull(self):
        tx = ecs.ItemLookup('B000BI7NHY', MerchantId='All', Condition='All', ResponseGroup='OfferFull')
        self.assertEqual(tx.ASIN, 'B000BI7NHY')
        # expecting 40 in fact
        self.assert_(len(list(tx.Offers)), 20)


    def testReviews(self):
        book = ecs.ItemLookup(self.ItemId, ResponseGroup='Reviews')
        reviews = list(book.CustomerReviews)
        self.assert_(len(reviews) > 4)


    def testSimilarities(self):
        book = ecs.ItemLookup(self.ItemId, ResponseGroup='Similarities')

        sim = book.SimilarProducts;
        self.assertEqual(len(sim), 5)
        self.assertEqual(sim[0].Title, 'Learning Python (Help for Programmers)')
        self.assertEqual(sim[1].Title, 'Python Cookbook')
        self.assertEqual(sim[3].Title, "Python Essential Reference (3rd Edition) (Developer's Library)")

    def testSubjects(self):
        book = ecs.ItemLookup(self.ItemId, ResponseGroup='Subjects')

        subs = book.Subjects;
        self.assertEqual(len(subs), 10)
        self.assertEqual(subs[0], 'Programming languages')
        self.assertEqual(subs[2], 'Computers - Languages / Programming')

    def testTracks(self):
        cd = ecs.ItemLookup('B0000042H4', ResponseGroup='Tracks')
        self.assertEqual(len(cd.Disc), 14)
        self.assertEqual(cd.Disc[13].Track[5], 'Gotterdammerung: Dritter Aufzug, Zweite Szene: Hoiho!')
        self.assertEqual(cd.Disc[4].Track[3], 'Die Walkure: Zweiter Aufzug, Funfte Szene: Zauberfest bezahmt ein Schlaf der Holden Schmerz und Harm')

    def testVariationMinimum(self):
        '''
        shirt = ecs.ItemLookup('B00144402A', ResponseGroup='VariationMinimum')
        self.assertEqual(shirt.Variations[0].ASIN, 'B000EG9PLU')
        self.assertNotEqual(shirt.Variations[5].ASIN, '')
        ''' 
        pass

    def testVariationSummary(self):
        '''
        shirt = ecs.ItemLookup('B000EI6M5A', ResponseGroup='VariationSummary')
        self.assertEqual(shirt.VariationSummary.HighestPrice.Amount, '699') 
        self.assertEqual(shirt.VariationSummary.LowestPrice.Amount, '699') 
        '''
        pass


    def testVariations(self):
        '''
        shirt = ecs.ItemLookup('B000EI6M5A', ResponseGroup='Variations')
        self.assertEqual(shirt.Variations[0].ASIN, 'B000EG9PLU')
        self.assertEqual(shirt.Variations[5].ASIN, 'B000EG5DUM')
        self.assertEqual(shirt.VariationSummary.HighestPrice.Amount, '699') 
        self.assertEqual(shirt.VariationSummary.LowestPrice.Amount, '699') 
        '''
        pass


if __name__ == "__main__" :
    unittest.main()
