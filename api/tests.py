from django.test import TestCase
from api.models import Account
# Create your tests here.

class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(address="53S7TO35ACZJKAA7NRDKRIZ5EAQGIVYVHQXLBWOALGCSUBIX4AWD5TCS6E", first_name="Natnael", last_name='Melese')
        Account.objects.create(address="ORIQFXKICNADY4U6H6O4T4ZNN7NNRVI4WD7J3ZF3V2URHYV6FZIIH5D7NY", first_name="Jhon", last_name='Doe')

    def test_accounts(self):
        nat = Account.objects.get(address="53S7TO35ACZJKAA7NRDKRIZ5EAQGIVYVHQXLBWOALGCSUBIX4AWD5TCS6E")
        jhon = Account.objects.get(address="ORIQFXKICNADY4U6H6O4T4ZNN7NNRVI4WD7J3ZF3V2URHYV6FZIIH5D7NY")
        self.assertEqual(nat.first_name, 'Natnael')
        self.assertEqual(jhon.first_name, 'Jhon')

