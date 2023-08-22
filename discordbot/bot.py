import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTEyNjM1MjMyODUxNDA5MzEwNg.G-oMmj.rZhN-dCs_JwX5Lttmmn4Dh-sj2ElLQZStBAT0s'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message.lower() == '.have you seen this little fella':
            image_path = "fella.png"
            with open(image_path, 'rb') as f:
                image = discord.File(f)
                await message.channel.send(file=image)
        if user_message[0] == '.':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)
        elif user_message[:2] == 'p.':
            user_message = user_message[2:]
            await send_message(message, user_message, is_private=True)

    client.run(TOKEN)