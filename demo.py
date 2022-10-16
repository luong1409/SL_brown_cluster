import unittest
from brownclustering import Corpus
from brownclustering import BrownClustering


class MyTestCase(unittest.TestCase):
    def test_full_something(self):

        data = [['i', 'have', 'a', 'dream', '.'],
                ['this', 'is', 'going', 'to', 'be', 'fun', '!'],
                ['i', 'have', 'a', 'dream', 'too', '.'],
                ['why', 'you', 'also', 'have', 'a', 'dream', '?']]
        corpus = Corpus(data, 0.001)
        clustering = BrownClustering(corpus, 6)
        clusters = clustering.train()
        print("--------------------------------------------Corpus after be clustered--------------------------------------------\n")
        for i, cluster in enumerate(clusters):
            print(f"Cluster: {i + 1}: {cluster}")


if __name__ == '__main__':
    unittest.main()
