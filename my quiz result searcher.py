# Quiz scores list
scores = [78, 85, 92, 67, 88, 95, 73]

# 1. Direct Access (O(1))
def direct_access(index):
    return scores[index]

# 2. Linear Search (O(n))
def linear_search(target):
    for i in range(len(scores)):
        if scores[i] == target:
            return i
    return -1

# 3. Pair Comparison (O(n^2))
def pair_comparison():
    pairs = []
    for i in range(len(scores)):
        for j in range(len(scores)):
            if i != j:
                pairs.append((scores[i], scores[j]))
    return pairs


# --- TESTING ---

print("Direct Access (index 2):", direct_access(2))

print("Linear Search (find 88):", linear_search(88))

print("Pair Comparison (first 5 pairs):")
pairs = pair_comparison()
print(pairs[:5])