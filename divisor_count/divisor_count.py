class DivisorCounter:
    def __init__(self, max_k: int = 10**7):
        self.max_k = max(max_k, 3)
        self.prefix_answers = []
        self._precompute()

    def _precompute(self):
        div_counts = [0] * (self.max_k + 1)
        for i in range(1, self.max_k + 1):
            for j in range(i, self.max_k + 1, i):
                div_counts[j] += 1
        
        self.prefix_answers = [0] * (self.max_k + 1)
        for i in range(2, self.max_k):
            is_valid = 1 if div_counts[i] == div_counts[i+1] else 0
            self.prefix_answers[i] = self.prefix_answers[i-1] + is_valid

    def solve_for_k(self, k: int) -> int:
        if k <= 2:
            return 0
        if k > self.max_k:
            raise ValueError(f"k exceeds precomputed max_k of {self.max_k}")
        return self.prefix_answers[k-1]

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    queries = [int(x) for x in input_data[1:t+1]]
    if not queries:
        return
        
    cache_max_k = max(queries) if queries else 3
    counter = DivisorCounter(max_k=cache_max_k)
    
    for k in queries:
        print(counter.solve_for_k(k))

if __name__ == '__main__':
    main()
