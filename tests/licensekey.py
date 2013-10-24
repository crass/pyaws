import unittest, os
import ecs

class LicenseKeyTest( unittest.TestCase ):
    def testSetLicenseKeyFromEnv(self):
        os.environ['AWS_LICENSE_KEY'] = "FAKE-KEY"
        ecs.setLicenseKey()
        self.assertEqual( ecs.getLicenseKey(), "FAKE-KEY" )
        del os.environ['AWS_LICENSE_KEY']

if __name__ == "__main__" :
    unittest.main()

