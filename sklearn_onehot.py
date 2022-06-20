from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

onehot_coder = OneHotEncoder()
onehot_coder.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
c = onehot_coder.transform([[0, 0, 3]])
print(c.toarray())


enc = OrdinalEncoder()
X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
enc.fit(X)
print(enc.transform([['female', 'from US', 'uses Safari']]))