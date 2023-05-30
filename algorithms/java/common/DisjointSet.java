package algorithms.java.common;

public class DisjointSet {
    private int[] groups;
    private int[] rank;

    public DisjointSet(int size) {
        groups = new int[size];
        for (int i = 0; i < size; i++) {
            groups[i] = i;
        }
        rank = new int[size];
    }

    public int find(int node) {
        int grp = groups[node];
        if (grp != node) {
            groups[node] = find(grp);
        }
        return groups[node];
    }

    public boolean union(int node1, int node2) {
        int grp1 = find(node1);
        int grp2 = find(node2);
        if (grp1 == grp2) {
            return false;
        }
        if (rank[grp1] >= rank[grp2]) {
            groups[grp2] = grp1;
            if (rank[grp1] == rank[grp2]) {
                rank[grp1]++;
            }
        } else {
            groups[grp1] = grp2;
        }
        return true;
    }

    public boolean isConnected(int node1, int node2) {
        return find(node1) == find(node2);
    }
}
