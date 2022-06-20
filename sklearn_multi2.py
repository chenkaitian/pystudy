from sklearn.preprocessing import MultiLabelBinarizer

y = [[1, 2], [1, 4], [1, 3, 4]]
print(MultiLabelBinarizer().fit_transform(y))
