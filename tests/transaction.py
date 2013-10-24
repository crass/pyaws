import unittest
import ecs

class TransactionLookpuTest(unittest.TestCase):
    def setUp(self):
        ecs.setLicenseKey("1MGVS72Y8JF7EC7JDZG2");

    def testTransactionLookup(self):
        el = ecs.TransactionLookup("104-1867480-8536729")
        for t in el:
            self.assertEqual(t.SellerId, "ATVPDKIKX0DER")
            self.assertEqual(t.TransactionDateEpoch, "1087249913")

            self.assertEqual(t.Totals.Total.Amount, "3090")
            self.assertEqual(t.Totals.Subtotal.Amount, "3157")
            self.assertEqual(t.Totals.Tax.Amount, "249")
            self.assertEqual(t.Totals.ShippingCharge.Amount, "498")

            for item in t.TransactionItems:
                self.assertEqual(item.TotalPrice.Amount, "2037")
                break

            for shipping in t.Shipments:
                self.assertEqual(shipping.DeliveryMethod, "Mail")
                break

if __name__ == "__main__" :
    unittest.main()
