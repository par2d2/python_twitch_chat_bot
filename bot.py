import os
import sys
import random
from twitchio.ext import commands

sys.path.insert(1, './constants/')
from welcomeMessage import  user_welcome_message, hello_message, welcome_message
from botList import known_bot_list

async def get_user_message(user_name):
    try:
        return user_welcome_message[user_name]
    except KeyError:
        return ''


class Bot(commands.Bot):
    chatters = []

    def __init__(self):
        super().__init__(token=os.environ['TMI_TOKEN'], prefix=os.environ['BOT_PREFIX'], initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        print(f'Chat bot is up and running.')

    async def event_message(self, message):
        user_name = message.author.name
        if message.echo or user_name.lower() in known_bot_list:
            return

        if message.first:
            self.chatters.append(user_name)
            await message.channel.send("Hey " + user_name + " Welcome to the Channel and the Chat. First time chatter")
        elif await self.is_first_chat_of_the_day(user_name):
            self.chatters.append(user_name)
            return_message = await get_user_message(user_name)
            if return_message:
                await message.channel.send(return_message + ' ' + os.environ['TWITCH_URL'] + user_name)
            else:
                first_part_of_message = random.choice(hello_message).replace('{user_name}', user_name)
                second_part_of_message = random.choice(welcome_message)
                await message.channel.send(first_part_of_message + second_part_of_message + ' ' + os.environ['TWITCH_URL'] + user_name)
                
        await self.handle_commands(message)

    @commands.command()
    async def lurk(self, ctx: commands.Context):
        await ctx.send(
            ctx.author.name + ' is now lurking in the deep dark depths of this stream! watching waiting .....')

    @commands.command()
    async def gt(self, ctx: commands.Context):
        await ctx.send("Xbox: Par2d2, Playstation: Par_2d2, Chess.com: par_2_d_2, steam: parfoo")

    async def is_first_chat_of_the_day(self, user_name):
        if user_name in self.chatters:
            return False
        return True


bot = Bot()
bot.run()
