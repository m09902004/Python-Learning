"""
Chapter 4. Naive Bayesian Classification
EmailObject class
根據電子郵件的 RFC 規格剖析收件訊息
"""
import email
import sys

from bs4 import BeautifulSoup


class EmailObject(object):
  """
  Parses incoming email messages
  剖析收件訊息
  """
  CLRF = "\n\r\n\r"

  def __init__(self, infile, category=None):
    self.category = category
    if sys.version_info > (3, 0):
      # Python 3 code in this block
      self.mail = email.message_from_binary_file(infile)
    else:
      # Python 2 code in this block
      self.mail = email.message_from_file(infile)

  def subject(self):
    """
    Get message subject line
    取得訊息主旨列
    :return: str
    """
    return self.mail.get('Subject')

  def body(self):
    """
    Get message body
    取得訊息文本
    :return: str in Py3, unicode in Py2
    """
    payload = self.mail.get_payload()
    if self.mail.is_multipart():
      parts = [self._single_body(part) for part in list(payload)]
    else:
      parts = [self._single_body(self.mail)]
    decoded_parts = []
    for part in parts:
      if len(part) == 0:
        continue
      if isinstance(part, bytes):
        decoded_parts.append(part.decode('utf-8', errors='ignore'))
      else:
        decoded_parts.append(part)
    return self.CLRF.join(decoded_parts)

  @staticmethod
  def _single_body(part):
    """
    Get text from part.
    從郵件 part 取得文字內容
    :param part: email.Message
    :return: str body or empty str if body cannot be decoded
    """
    content_type = part.get_content_type()
    try:
      body = part.get_payload(decode=True)
    except Exception:
      return ''

    if content_type == 'text/html':
      return BeautifulSoup(body, 'html.parser').text
    elif content_type == 'text/plain':
      return body
    return ''