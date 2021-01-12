import unittest


class TestORFspatrons(unittest.TestCase):

    def test_format_regex(self):
        # Comprovem format funció a cercar
        path = "/home/datasci/prog_datasci_2/activities/activity_4/data/tb_functions.pl"
        # Ha de ser un string
        self.assertTrue(ORFspatrons(path, "protein"))
        # No pot ser un integre
        self.assertFalse(ORFspatrons(path, 12345))


suite = unittest.TestLoader().loadTestsFromTestCase(TestORFspatrons)
unittest.TextTestRunner(verbosity=2).run(suite)

