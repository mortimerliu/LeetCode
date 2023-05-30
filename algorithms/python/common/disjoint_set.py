class DisjointSet:
    def __init__(self, nodes=None):
        self.groups = {}
        self.counts = {}
        self._ncomps = 0
        if nodes:
            for node in nodes:
                self.insert(node)

    def insert(self, node):
        if node in self.groups:
            return False
        self.groups[node] = node
        self.counts[node] = 1
        self._ncomps += 1
        return True

    def find(self, node):
        # w/ path compression
        grp = self.groups[node]
        if grp != node:
            self.groups[node] = self.find(grp)
        return self.groups[node]

    def union(self, node1, node2):
        # w/ union by count
        grp1, grp2 = self.find(node1), self.find(node2)
        if grp1 == grp2:
            return False
        if self.counts[grp1] < self.counts[grp2]:
            grp1, grp2 = grp2, grp1
        self.groups[grp2] = grp1
        self.counts[grp1] += self.counts[grp2]
        # self._ncomps -= 1
        return True

    @property
    def num_components(self):
        return self._ncomps
