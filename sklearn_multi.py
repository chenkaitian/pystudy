from sklearn.preprocessing import LabelEncoder

# 原始特征
d = [[1, 2], [1, 4], [1, 3, 4]]
e = set()
# 求d中所有物品类别
for i in d:
    for j in i:
        e.add(j)

# 对d中物品进行Index编码
label_coder = LabelEncoder()
label_coder.fit(list(e))

# 特征[1, 2] 进行编码
f = [0] * len(e)
for i in label_coder.transform([1, 2]):
    f[i] = 1
print(f)
# [1, 2] 转换后为[1, 1, 0, 0]
