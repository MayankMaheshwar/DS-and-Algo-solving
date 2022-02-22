import unittest
import assign1

ans = ['abc', 'abk', 'abr', 'acb', 'ack', 'acr', 'akb', 'akc', 'akr', 'arb', 'arc', 'ark', 'bac', 'bak', 'bar', 'bca', 'bck', 'bcr', 'bka', 'bkc', 'bkr', 'bra', 'brc', 'brk', 'cab', 'cak', 'car', 'cba', 'cbk', 'cbr',
       'cka', 'ckb', 'ckr', 'cra', 'crb', 'crk', 'kab', 'kac', 'kar', 'kba', 'kbc', 'kbr', 'kca', 'kcb', 'kcr', 'kra', 'krb', 'krc', 'rab', 'rac', 'rak', 'rba', 'rbc', 'rbk', 'rca', 'rcb', 'rck', 'rka', 'rkb', 'rkc']


class TestMedian(unittest.TestCase):

    def test_subsequences(self):
        self.assertAlmostEqual(input(), ans)
