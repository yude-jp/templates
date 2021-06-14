import requests
from discord.ext import commands
from pprint import pprint
import aiohttp

TOKEN = ""

AuthB = "Bot " + TOKEN

headers = {
    "Authorization": AuthB
}


def returnNormalUrl(channelId):
    return "https://discordapp.com/api/channels/" + str(channelId) + "/messages"


async def notify_callback(id, token):
    url = "https://discord.com/api/v8/interactions/{0}/{1}/callback".format(id, token)
    json = {
        "type": 6
    }
    async with aiohttp.ClientSession() as s:
        async with s.post(url, json=json) as r:
            if 200 <= r.status < 300:
                return


async def on_socket_response(msg):
    if msg["t"] != "INTERACTION_CREATE":
        return

    pprint(msg)


class MyBot(commands.Bot):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_listener(on_socket_response)


bot = MyBot(command_prefix='.', description='Discord Bot for yude.jp greetings')

@bot.event
async def on_ready():
    print("Ready!")

@bot.event
async def on_message(msg):
    if msg.content == "!welcome":
        normal_url = "https://discordapp.com/api/channels/" + str(msg.channel.id) + "/messages"
        json = {
            "embeds": [
              {
                "title": "yude.jp の Discord サーバーへようこそ!",
                "url": "https://yude.jp",
                "description": "Welcome to yude.jp Discord server!",
                "thumbnail": {
                  "url": "https://cdn.discordapp.com/icons/550309736214691840/2e18e529b75fc216f970b59a067bd737.webp?size=128",
                },
                "color": 573729,
                "fields": [
                  {
                    "name":"💫 概要",
                    "value": "このサーバーの目的は特にありません。"
                  },
                  {
                    "name":"📕 ルール",
                    "value": "1. 過激すぎる発言をしないでください。\n2. チャットスパムを行わないでください。\n3. 商業的な目的で使用しないでください。\n4. 過剰な宣伝行為は控えてください。\n5. その他、日本国の法律に反するような投稿を行わないでください。"
                  },
                  {
                    "name":"👥 GitHub Organization",
                    "value": "[こちら](https://yudejp-github-org.herokuapp.com/) からあなたのアカウントに yude.jp の GitHub Organization の招待を送信することができます。"
                  }
                ]
              }
            ],
            "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "label": "招待リンク",
                            "style": 5,
                            "url": "https://discord.gg/X6srY7X",
                        },
                        {
                            "type": 2,
                            "label": "Twitter (@yudejp)",
                            "style": 5,
                            "url": "https://twitter.com/yudejp",
                        },
                        {
                            "type": 2,
                            "label": "GitHub Organization",
                            "style": 5,
                            "url": "https://github.com/yudejp",
                        },
                        {
                            "type": 2,
                            "label": "LINE オープンチャット",
                            "style": 5,
                            "url": "https://line.me/ti/g2/mi36ZEsJkIo9BLqYg1sQFg",
                        },
                        {
                            "type": 2,
                            "label": "Minecraft マルチプレイ",
                            "style": 5,
                            "url": "https://yude.jp/minecraft",
                        },
                    ]

                }
            ],
        }
        r = requests.post(normal_url, headers=headers, json=json)


bot.run(TOKEN)
