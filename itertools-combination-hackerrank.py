from itertools import combinations
def print_combinations(s, k):
    s = sorted(s)
    for i in range(1, k + 1):
        for comb in combinations(s, i):
            print(''.join(comb))

if __name__ == "__main__":
    input_str, k = input().split()
    k = int(k)
    print_combinations(input_str, k)