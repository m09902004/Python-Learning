"""
Chapter 4. Naive Bayesian Classification
Text tokenizer
將標記的單詞萃取放入資料流中
"""
import re


class Tokenizer:
  """
  Splits lines by whitespaces, converts to lower case and builds n-grams.
  以空格分行 , 將字詞改小寫以及建置 n 元語法
  """
  NULL = u'\u0000'

  @staticmethod
  def tokenize(string):
    return re.findall("\w+", string.lower())

  @staticmethod
  def unique_tokenizer(string):
    return set(Tokenizer.tokenize(string))

  @staticmethod
  def ngram(string, ngram):
    tokens = Tokenizer.tokenize(string)

    ngrams = []

    for i in range(len(tokens)):
      shift = i - ngram + 1
      padding = max(-shift, 0)
      first_idx = max(shift, 0)
      last_idx = first_idx + ngram - padding

      ngrams.append(Tokenizer.pad(tokens[first_idx:last_idx], padding))

    return ngrams

  @staticmethod
  def pad(tokens, padding):
    padded_tokens = []

    for i in range(padding):
      padded_tokens.append(Tokenizer.NULL)

    return padded_tokens + tokens