import itertools

def find_combinations(numbers, target, num_combinations=3):
    # 初始化一个列表来存储最接近200的组合
    best_combinations = []

    for r in range(1, len(numbers) + 1):
        for combination in itertools.combinations_with_replacement(numbers, r):
            current_sum = sum(combination)
            if current_sum >= target:
                best_combinations.append((combination, current_sum))
    
    # 根据总和对组合进行排序
    best_combinations.sort(key=lambda x: abs(target - x[1]))
    
    # 获取相对最优的组合
    result_combinations = best_combinations[:num_combinations]
    
    return [(list(combination), current_sum) for combination, current_sum in result_combinations]

# 您的数字列表
numbers = [16.2,17,17.7,18.5,18.7,26.7,32.7]

# 目标总和
target = 85

# 获取相对最优的3种组合
best_combinations = find_combinations(numbers, target, num_combinations=10)

for i, (combination, current_sum) in enumerate(best_combinations):
    print(f"相对最优组合 {i + 1}: {combination}")
    print(f"总和: {current_sum}")
    print()
