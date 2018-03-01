from sklearn import tree

#[altura, peso, tamanho do pe]

X = [[180,95, 42], [160,65,36], [180,95, 42], [160,65,36],[180,95, 42], [160,65,36],[180,95, 42], [160,65,36]]

Y= ['male', 'female','male', 'female','male', 'female','male', 'female']


clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[175,80,40]])

print(prediction)

