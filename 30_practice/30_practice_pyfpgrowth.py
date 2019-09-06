import pyfpgrowth
# 資料
data = [[1, 2, 5],
        [2, 4],
        [2, 3],
        [1, 2, 4],
        [1, 3],
        [2, 3],
        [1, 3],
        [1, 2, 3, 5],
        [1, 2, 3]]
# 設定支援度和置信度
minS = 0.2
minC = 0.7
# 計算支援值
support = minS*len(data)
# 獲取符合支援度規則資料
patterns = pyfpgrowth.find_frequent_patterns(data, support)
# 獲取符合置信度規則資料
rules = pyfpgrowth.generate_association_rules(patterns, minC)

rules