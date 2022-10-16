import datetime
from tqdm import tqdm
from brownclustering.helpers import EnhancedClusteringHelper


class BrownClustering:
    def __init__(self, corpus, m):
        self.m = m
        self.corpus = corpus
        self.vocabulary = corpus.vocabulary
        self.helper = EnhancedClusteringHelper(corpus)
        self._codes = dict()
        for word in self.vocabulary:
            self._codes[word] = []

    @staticmethod
    def ranks(vocabulary):
        def count(c):
            return c[1]

        counts = sorted(vocabulary.items())
        return sorted(counts, key=count, reverse=True)

    def merge_arg_max(self, _benefit, _helper):
        max_benefit = float('-inf')
        best_merge = None
        for i in range(_benefit.shape[0]):
            for j in range(i + 1, _benefit.shape[1]):
                if max_benefit < _benefit[i, j]:
                    max_benefit = _benefit[i, j]
                    best_merge = (i, j)
        cluster_left = _helper.get_cluster(best_merge[0])
        cluster_right = _helper.get_cluster(best_merge[1])

        for word in cluster_left:
            self._codes[word].append(0)

        for word in cluster_right:
            self._codes[word].append(1)

        _helper.merge_clusters(best_merge[0], best_merge[1])

        return best_merge

    def train(self):

        words = self.ranks(self.vocabulary)
        tops = words[0:self.m]

        for w in tops:
            self.helper.append_cluster([w[0]])

        itr = 0
        for w in tqdm(words[self.m:]):
            itr += 1
            self.helper.append_cluster([w[0]])
            _benefit = self.helper.compute_benefit()
            best_merge = self.merge_arg_max(_benefit, self.helper)


        xxx = self.helper.get_clusters()

        for _ in tqdm(range(len(self.helper.get_clusters()) - 1)):
            itr += 1
            _benefit = self.helper.compute_benefit()
            best_merge = self.merge_arg_max(_benefit, self.helper)

        return xxx