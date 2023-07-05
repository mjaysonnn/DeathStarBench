import sys
sys.path.append('../gen-py')

from media_service import ComposeReviewService
from media_service.ttypes import ServiceException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import random
import string

def compose_review():
  socket = TSocket.TSocket("ath-8.ece.cornell.edu", 9090)
  transport = TTransport.TFramedTransport(socket)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = ComposeReviewService.Client(protocol)

  transport.open()
  for _ in range(100):
    req_id = random.getrandbits(63)
    unique_id = random.getrandbits(63)
    text = ''.join(random.choices(string.ascii_lowercase + string.digits, k=128))
    user_id = random.randint(0,5)
    movie_id = f"movie_id_{random.randint(0, 5)}"
    rating = random.randint(0, 10)
    client.UploadUniqueId(req_id, unique_id, {})
    client.UploadUserId(req_id, user_id, {})
    client.UploadRating(req_id, rating, {})
    client.UploadText(req_id, text, {})
    client.UploadMovieId(req_id, movie_id, {})
  transport.close()


if __name__ == '__main__':
  try:
    compose_review()
  except ServiceException as se:
    print(f'{se.message}')
  except Thrift.TException as tx:
    print(f'{tx.message}')