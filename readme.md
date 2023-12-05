# tg_api_gen

library that generates realistic device_model, app_verion, and system_version (android and ios) for telegram userbots

## installation
```bash
pip install tg_api_gen pyrogram tgcrypto
```

## usage

```python
import tg_api_gen
from pyrogram import Client

async def main():
  client = Client(
      name = 'my_clien_name',
      **tg_api_gen.generate_random(),
  )
  phone = ' # put phone here
  await client.connect()
  code = await client.send_code(
      phone_number = phone
  )
  print(code)
  try:
      user = await client.sign_in(
          phone_number = phone,
          phone_code_hash = code.phone_code_hash,
          phone_code = input('code: '),
      )
  except errors.SessionPasswordNeeded:
      user = await client.check_password(
          password = input('password: ')
      )
 ```

## credits

thanks to:
- [opentele](https://github.com/thedemons/opentele)
- [pyrogram](https://github.com/pyrogram/pyrogram)
- [telethon](https://github.com/LonamiWebs/Telethon)

## license

license is gnu agpl 3 - [gnu.org/licenses/agpl-3.0.en.html](https://gnu.org/licenses/agpl-3.0.en.html)
