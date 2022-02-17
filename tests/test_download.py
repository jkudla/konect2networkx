import unittest
import konect2networkx as k2n

class TestDownload(unittest.TestCase):

    def test_network_non_existent(self):
        self.assertRaises(k2n.RetrieveException, k2n.download_network, 'muhaha')

if __name__ == '__main__':
    unittest.main()
