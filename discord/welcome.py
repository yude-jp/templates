import discord

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} としてログインしました。'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!welcome'):
        embed=discord.Embed(title="yude.jp の Discord サーバーへようこそ!", url="https://yude.jp", description="Welcome to yude.jp Discord server!", color=0xffa3f0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/550309736214691840/2e18e529b75fc216f970b59a067bd737.webp?size=128")
        embed.add_field(name="💫 概要", value="このサーバーの目的は特にありません。\n招待リンク: [discord.gg/X6srY7X](https://discord.gg/X6srY7X)", inline=False)
        embed.add_field(name="📕 ルール", value="1. 過激すぎる発言をしないでください。\n2. チャットスパムを行わないでください。", inline=False)
        embed.add_field(name="📎 リンク", value="[GitHub Organization](https://github.com/yude-jp), [Twitter](https://twitter.com/yude_jp), [LINE オープンチャット](https://line.me/ti/g2/mi36ZEsJkIo9BLqYg1sQFg)", inline=False)

        await message.channel.send(embed=embed)

client.run('token')