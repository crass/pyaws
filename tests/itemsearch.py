import unittest
import ecs

class ItemSearchTest(unittest.TestCase):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");

    def assertIsInteger(self, n, message=None):
        try:
            int(n)
        except :
            fail(message)
            
    def testSmall(self):
        books = ecs.ItemSearch("Python, network", SearchIndex="Books", ResponseGroup='Request,Small')
        titles = ['Twisted Network Programming Essentials', 'Python & XML', 'Perl to Python Migration']
        all_titles = [ book.Title for book in books ]
        for t in titles:
            self.assert_ (t in all_titles )

    def testMedium(self):
        books = ecs.ItemSearch("XML,Python", SearchIndex="Books", ResponseGroup='Request,Medium')
        for book in books:
            self.assertEqual(book.Title, 'Python & XML')
            # EditorialReview
            for review in book.EditorialReviews:
                self.assertEqual(review.Source, 'Product Description')
                break

            # Images 
            for images in book.ImageSets:
                self.assertEqual(images.LargeImage.Height, '500')
                self.assertEqual(images.MediumImage.Height, '160')
                self.assertEqual(images.SmallImage.Height, '75')
                break

            # ItemAttributes
            pass

            # ItemIds
            pass

            # OfferSummary
            self.assertNotEqual(book.OfferSummary.TotalNew, '0')
            self.assertIsInteger(book.OfferSummary.LowestNewPrice.Amount)

            # SalesRank
            self.assertNotEqual(book.SalesRank, '0')
            break

    def testAccessories(self):
        # We have to use Palm Tungsten X
        txs = ecs.ItemSearch('Zen', SearchIndex='Electronics', ResponseGroup='Small,Accessories')
        for tx in txs:
            self.assertEqual(len([x for x in tx.Accessories]), 5)
            break

    def testBrowseNodes(self):
        books = ecs.ItemSearch('XML Python', SearchIndex='Books', ResponseGroup='BrowseNodes')
        for book in books:
            self.assertEqual(book.ASIN, '0596001282')
            nodes = set(['XML', 'Scripting Languages', 'Python', 'Paperback'])
            bn_names = set([ bn.Name for bn in book.BrowseNodes ])
            self.assert_(nodes.issubset(bn_names))
            break

    def testLarge(self):
        # TODO: find Large
        books = ecs.ItemSearch('XML Python', SearchIndex='Books', ResponseGroup='Large')
        for book in books:
            break
    
'''
    def testListmaniaLists(self):
        # TODO: need to find the item with this attributes
        pass

    def testOfferFull(self):
        books = ecs.ItemSearch('XML Python', SearchIndex='Books', MerchantId='All', ResponseGroup='OfferFull')
        book = books[0]
        self.assert_(len(book.Offers) > 10)
        
    def testReviews(self):
        books = ecs.ItemSearch('XML Python', SearchIndex='Books', MerchantId='All', ResponseGroup='Reviews')
        book = books[4]
        self.assert_(len(book.CustomerReviews) > 5)

        # arbitary reviewer
        self.assertEqual(book.CustomerReviews[3].Reviewer.Name, 'M. Bennett') 
        self.assertEqual(book.CustomerReviews[10].Summary, 'Nice followup')


    def testSimilarities(self):
        books = ecs.ItemSearch('XML Python', SearchIndex='Books', MerchantId='All', ResponseGroup='Similarities')
        book = books[0]

        sim = book.SimilarProducts;
        self.assertEqual(len(sim), 5)
        self.assertEqual(sim[0].Title, 'Python Cookbook')
        self.assertEqual(sim[1].Title, 'Programming Python')

    def testSubjects(self):
        books = ecs.ItemSearch('XML Python', SearchIndex='Books', MerchantId='All', ResponseGroup='Subjects')
        book = books[0]
        subs = book.Subjects;
        self.assert_('XML' in subs)
        self.assert_('Computers' in subs)
        self.assert_('Programming Languages - HTML' in subs)

    def testTracks(self):
        cds = ecs.ItemSearch('Gotterdammerung', SearchIndex='Classical', ResponseGroup='Tracks')
        cd = cds[1].Tracks
        self.assertEqual(len(cd.Disc), 2)
        self.assertEqual(cd.Disc[0].Track[5], 'Die Meistersinger von Nurnberg: Overture')
        self.assertEqual(cd.Disc[1].Track[3], 'Parsifal: Prelude to Act 3')

    def testVariationMinimum(self):
        pass

    def testVariationSummary(self):
        pass

    def testVariations(self):
        pass
'''

if __name__ == "__main__" :
    unittest.main()
