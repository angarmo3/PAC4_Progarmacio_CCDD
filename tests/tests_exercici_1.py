import unittest


class TestORFs(unittest.TestCase):

    def test_nom_path(self):
        # Comprovem format del path
        # El path ha de ser string
        path = "/home/datasci/prog_datasci_2/activities/activity_4/data/tb_functions.pl"
        self.assertTrue(ORFs(path, "Carbon"))
        # no pot ser un enter
        path2 = 1232434
        self.assertFalse(ORFs(path2, "Carbon"))

    def test_nom_funcio(self):
        # Comprovem format funció a cercar
        path = "/home/datasci/prog_datasci_2/activities/activity_4/data/tb_functions.pl"
        # Ha de reconeixer strings per a func
        self.assertTrue(ORFs(path, "Carbon"))
        # No ha de reconeixer enters per a func
        self.assertFalse(ORFs(path, 12345))
        # No ha de reconeixer símbols per a func
        self.assertFalse(ORFs(path, "%&$"))


suite = unittest.TestLoader().loadTestsFromTestCase(TestORFs)
unittest.TextTestRunner(verbosity=2).run(suite)

