import sys

import tcrutils as tcr
from tcrutils import console

import nekoweb as nw

console.debug(sorted(a := [x for x in globals() if not x.startswith('_')]), len(a))
del a
console.log(f'{tcr.c}Running on Python %s.%s' % sys.version_info[:2])


def test_test():
  console(nw)


if True:  # Test setup
  for k, v in globals().copy().items():  # Decorate each test_... function with the @tcr.test decorator
    if k.startswith('test_'):
      globals()[k] = tcr.test(v)

if True:
  test_test()
