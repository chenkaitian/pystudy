from sklearn.preprocessing import OneHotEncoder

onehot_coder = OneHotEncoder()
onehot_coder.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
c = onehot_coder.transform([[0, 0, 3]])
print(c.toarray())

