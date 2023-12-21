# tg_api_gen

library that generates realistic device_model, app_verion, and system_version (android and ios) for telegram userbots

there is a very high risk to get ban from telegram, please don't use with your main account

## installation
```bash
pip install tg_api_gen pyrogram tgcrypto
```

## how to use

just see what data generated:

```python
import tg_api_gen

print(tg_api_gen.generate_random())
 ```

real code example - [usage.py](usage.py)

## changelog

see [changelog.md](changelog.md)

## credits

thanks to:
- [opentele](https://github.com/thedemons/opentele)
- [pyrogram](https://github.com/pyrogram/pyrogram)
- [telethon](https://github.com/LonamiWebs/Telethon)

## license

license is gnu agpl 3 - [gnu.org/licenses/agpl-3.0.en.html](https://gnu.org/licenses/agpl-3.0.en.html)

