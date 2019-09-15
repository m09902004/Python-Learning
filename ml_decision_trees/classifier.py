"""
Chapter 5. Decision trees
建制多個分類器
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from numpy.random import permutation
from numpy import array_split, concatenate
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np


class MushroomProblem:
  """
  Mushrooms classification problem
  蘑菇分類問題
  """

  def __init__(self, data_file):
    """
    Loads data file and prepares data
    載入檔案以及參數
    :param data_file: CSV file name
    """
    self.data_frame = pd.read_csv(data_file)
    for k in self.data_frame.columns[1:]:
      self.data_frame[k], _ = pd.factorize(self.data_frame[k])

    self.classes = np.array(sorted(pd.Categorical(self.data_frame['class']).categories))
    self.features = self.data_frame.columns[self.data_frame.columns != 'class']

  @staticmethod
  def __factorize(data):
    y, _ = pd.factorize(pd.Categorical(data['class']), sort=True)
    return y

  def train(self, X, Y):
    """
    Train classifier. Should be implemented in subclass
    訓練分類器 , 需在子集中實行
    :param X: training input samples
    :param Y: target values
    """
    raise NotImplementedError

  def validation_data(self, folds):
    """
    Performs data splitting, classifier training and prediction for given #folds
    針對已知的折數執行資料分離 , 分類器訓練與預測
    :param folds: number of folds
    :return: list of numpy.array pairs (prediction, expected)
    """
    df = self.data_frame
    response = []

    assert len(df) > folds

    perms = array_split(permutation(len(df)), folds)

    for i in range(folds):
      train_idxs = list(range(folds))
      train_idxs.pop(i)
      train = []
      for idx in train_idxs:
        train.append(perms[idx])

      train = concatenate(train)

      test_idx = perms[i]

      training = df.iloc[train]
      test_data = df.iloc[test_idx]

      y = self.__factorize(training)
      classifier = self.train(training[self.features], y)
      predictions = classifier.predict(test_data[self.features])

      expected = self.__factorize(test_data)
      response.append([predictions, expected])

    return response


class MushroomRegression(MushroomProblem):
  """
  Implementation if mushrooms classification problem with sklearn.DecisionTreeRegressor
  用決策樹回歸處理蘑菇分類問題
  """

  def train(self, X, Y):
    """
    Train classifier.
    訓練分類器
    :param X: training input samples
    :param Y: target values
    :return: regressor
    """
    regressor = DecisionTreeRegressor()
    regressor = regressor.fit(X, Y)
    return regressor

  def validate(self, folds):
    """
    Evaluate classifier using mean squared error
    使用均方差估算分類器
    :param folds: number of folds
    :return: list of MSE per fold
    """
    responses = []

    for y_true, y_pred in self.validation_data(folds):
      responses.append(mean_squared_error(y_true, y_pred))

    return responses


class MushroomClassifier(MushroomProblem):
  """
  Partial implementation of mushrooms classification problem
  部分實作蘑菇分類問題
  """

  def validate(self, folds):
    """
    Evaluate classifier using confusion matrices
    使用混淆矩陣估算分類器
    :param folds: number of folds
    :return: list of confusion matrices per fold
    """
    confusion_matrices = []

    for test, training in self.validation_data(folds):
      confusion_matrices.append(self.confusion_matrix(training, test))

    return confusion_matrices

  @staticmethod
  def confusion_matrix(train, test):
    return pd.crosstab(test, train, rownames=['actual'], colnames=['preds'])


class MushroomForest(MushroomClassifier):
  """
  Implementation of mushrooms classification problem with sklearn.RandomForestClassifier
  使用隨機森林分類處理蘑菇分類問題
  """

  def train(self, X, Y):
    """
    Train classifier.
    訓練分類器
    :param X: training input samples
    :param Y: target values
    :return: classifier
    """
    classifier = RandomForestClassifier(n_jobs=2)
    classifier = classifier.fit(X, Y)
    return classifier


class MushroomTree(MushroomClassifier):
  """
  Implementation of mushrooms classification problem with sklearn.DecisionTreeClassifier
  使用決策樹分類處理蘑菇分類問題
  """

  def train(self, X, Y):
    """
    Train classifier.
    訓練分類器
    :param X: training input samples
    :param Y: target values
    :return: classifier
    """
    classifier = DecisionTreeClassifier()
    classifier = classifier.fit(X, Y)
    return classifier