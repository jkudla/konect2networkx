import unittest

import os
import shutil
import konect2networkx as k2n

class TestLoad(unittest.TestCase):

    def test_network_non_existent(self):
        self.assertRaises(k2n.LoadException, k2n.get, 'muhaha', False)

    def test_network_correct_filename(self):
        os.mkdir('muhaha')
        f = open('muhaha/out.muhaha', 'w') # this is correct
        f.write('% sym unweighted\n% 3 3 3\n1 2\n1 3\n2 3\n')
        f.close()

        try:
            k2n.get('muhaha', False)
        except k2n.LoadException:
            self.fail('LoadException raised unexpectedly')
        finally:
            shutil.rmtree('muhaha') # clean up


    def test_network_non_standard_filename(self):
        os.mkdir('muhaha')
        f = open('muhaha/out.muh', 'w') # this is wrong
        f.write('% sym unweighted\n% 3 3 3\n1 2\n1 3\n2 3\n')
        f.close()

        try:
            k2n.get('muhaha', False)
        except k2n.LoadException:
            self.fail('LoadException raised unexpectedly')
        finally:
            shutil.rmtree('muhaha') # clean up


    def test_network_lacking_out_file(self):
        os.mkdir('muhaha')
        self.assertRaises(k2n.LoadException, k2n.get, 'muhaha', False)
        shutil.rmtree('muhaha') # clean up

if __name__ == '__main__':
    unittest.main()
