import asyncio
import sys

import tcrutils as tcr
from colored import Back, Fore, Style
from tcrutils import asshole, console, rashole

import nekoweb as nkw

console.debug(sorted(a := [x for x in globals() if not x.startswith('_')]), len(a))
console.log(f'{Style.reset}Running on Python %s.%s' % sys.version_info[:2])
tcr.WarningCatcher()

NCL = nkw.Client(api_key=tcr.get_token('API_KEY.txt'))


async def test_client():
  console(NCL)

  console(await NCL.site_info('asdfsdgsdfirc'))


if True:  # Test setup
  for k, v in globals().copy().items():  # Decorate each test_... function with the @tcr.test decorator
    if k.startswith('test_'):
      globals()[k] = tcr.test(v)


async def main():  # Tests
  await test_client()
  pass


if __name__ == '__main__':
  asyncio.run(main())
