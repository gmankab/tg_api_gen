import pyrogram.errors
import pyrogram.client
import tg_api_gen
import asyncio

async def authorise(client):
    phone = input('phone: ')
    code = await client.send_code(
        phone_number = phone
    )
    print(code)
    try:
        return await client.sign_in(
            phone_number = phone,
            phone_code_hash = code.phone_code_hash,
            phone_code = input('code: '),
        )
    except pyrogram.errors.SessionPasswordNeeded:
        return await client.check_password(
            password = input('password: ')
        )

async def main():
    client = pyrogram.client.Client(
        name = 'my_client_name',
        **tg_api_gen.generate_random(),
    )
    await client.connect()
    try:
        user = await client.get_me()
        print('user already authorised')
    except:
        print('user is not authorised yet, authorising...')
        user = await authorise(client)
    print(user)
    await client.send_message('me', 'hello world')
    await client.stop()

asyncio.run(main())

