import unittest
import ecs

class HelpTest(unittest.TestCase):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");

    def testHelp(self):
        el = ecs.Help(HelpType="Operation", About="CartAdd")
        reference = {'AvailableParameters': ['AWSAccessKeyId', 'ContentType', 'LinkCode', 'Marketplace', 'MarketplaceDomain', 'MergeCart', 'Style', 'Validate', 'Version', 'XMLEscaping'],
            'AvailableResponseGroups': ['Request', 'Cart', 'CartSimilarities', 'CartTopSellers', 'CartNewReleases'], 
            'RequiredParameters': ['AssociateTag', 'CartId', 'HMAC', 'Items'], 
            'DefaultResponseGroups': ['Request', 'Cart'] }
        
        for x in ('AvailableParameters', 'AvailableResponseGroups', 
            'RequiredParameters', 'DefaultResponseGroups'):
            self.assertEqual(getattr(el.OperationInformation,x), reference[x])
                

if __name__ == "__main__" :
    unittest.main()
