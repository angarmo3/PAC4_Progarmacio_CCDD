import unittest


class TestORFsM(unittest.TestCase):

    def test_format_regex(self):
        # Comprovem format path a cercar
        # Ha de ser un string
        path = "/home/datasci/prog_datasci_2/activities/activity_4/data/tb_functions.pl"
        self.assertTrue(ORFsM(path))
        # No pot ser un integre
        path2 = 12345
        self.assertFalse(ORFsM(path2))


suite = unittest.TestLoader().loadTestsFromTestCase(TestORFsM)
unittest.TextTestRunner(verbosity=2).run(suite)

