import random

for i in range(5):
    random_set = set(random.sample(range(1, 46), 7))
    good = sorted(random_set)
    print(f"today's your luck is:{good}")
    assert len(random_set)==7