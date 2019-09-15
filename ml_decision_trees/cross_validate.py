from classifier import MushroomTree, MushroomForest, MushroomRegression

data = './data/agaricus-lepiota.data'
folds = 5

print("Calculating score for decision tree")
tree = MushroomTree(data)
print(tree.validate(folds))
print()

print("Calculating score for random forest method")
forest = MushroomForest(data)
print(forest.validate(folds))
print()

print("Calculating score for regression tree")
regression = MushroomRegression(data)
print(regression.validate(folds))
print()

