def distance(a, b):
    def min_dist(s1, s2):
        if s1 == len(a) or s2 == len(b):
            return len(a) - s1 + len(b) - s2

        # no change required
        if a[s1] == b[s2]:
            return min_dist(s1 + 1, s2 + 1)

        return 1 + min(
            min_dist(s1, s2 + 1),      
            min_dist(s1 + 1, s2),     
            min_dist(s1 + 1, s2 + 1), 
        )

    return min_dist(0, 0)