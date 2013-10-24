import unittest
import ecs

class BrowseNodeLookupTest(unittest.TestCase):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");

    def testBrowserNodeLookup(self):
        bnl = [x for x in ecs.BrowseNodeLookup('1065852', ResponseGroup='NewReleases,BrowseNodeInfo,TopSellers')]
        self.assertEqual(len(bnl), 1)
        self.assertEqual(bnl[0].Name, 'Plasma TVs')
        children = [x for x in bnl[0].Children]
        self.assertEqual(len(children), 2)
        self.assertEqual(children[0].BrowseNodeId, '13005341')
        self.assertEqual(children[1].BrowseNodeId, '11091111')

        '''self.assertEqual(bnl[0].Ancestors[0].Ancestors[0].Name, 'TVs & HDTVs')
        self.assertNotEqual(bnl[0].TopSellers[0].ASIN, '')
        self.assertNotEqual(bnl[0].NewReleases[1].ASIN, '')'''

if __name__ == "__main__" :
    unittest.main()

