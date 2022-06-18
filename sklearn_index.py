from sklearn.preprocessing import LabelEncoder

a = [1, 200, 10000, 30000, 100000]
label_coder = LabelEncoder()
label_coder.fit(a)
b = label_coder.transform(a)
print(b)
