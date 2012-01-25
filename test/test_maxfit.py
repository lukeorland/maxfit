import unittest
import maxfit


class TestMaxFit(unittest.TestCase):

    def setUp(self):
        self.sizes = [748762204, 688863813, 550116117, 487118311, 799159364,
                      505775282, 667940719, 586780646, 766399125, 608674431,
                      730992596, 662242644, 500693160, 901698254, 540512715,
                      977197784, 791194435, 760268820, 800933510, 631138068,
                      630741939, 883749426, 694444540, 510281429, 693505062,
                      793118639, 577261573, 824282484, 700115336, 700115336] 

    def test_bytes_scaled(self):
        b = 5e9
        scale = 1e6
        expected = 5000
        actual = maxfit.bytes_scaled(b, scale)
        self.assertEqual(expected, actual)

    def test_bytes_scaled2(self):
        b = 500000001
        scale = 1e6
        expected = 500.000001
        actual = maxfit.bytes_scaled(b, scale)
        self.assertEqual(expected, actual)

    def test_bytes_to_MB(self):
        self.assertEqual(748.762204, maxfit.bytes_to_MB(748762204))

    def test_truncate(self):
        divisor = 1e6
        self.assertEqual(749, maxfit.truncate(748762204, divisor))
        self.assertEqual(748, maxfit.truncate(748000000, divisor))

    def test_solve_best_fit_files(self):
        file_sizes = self.sizes[:3]

        limit = 700e6
        scaling_divisor = 1e6
        expected = [1]
        actual = maxfit.indices_best_fit_files(file_sizes, limit,
                                               scaling_divisor)
        self.assertEqual(expected, actual)

        limit = 1240e6
        scaling_divisor = 1e6
        expected = [1, 2]
        actual = maxfit.indices_best_fit_files(file_sizes, limit,
                                               scaling_divisor)
        self.assertEqual(expected, actual)
