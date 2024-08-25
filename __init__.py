from pathlib import Path
import nonebot
import json
from nonebot import on_regex, on_keyword, on_message, on_command
from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
import requests
from nonebot.typing import T_State
from nonebot.params import CommandArg
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, PrivateMessageEvent, Message, MessageSegment
from .config import Config,load_user_list_from_csv
import random

__plugin_meta__ = PluginMetadata(
    name="Test",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

audio_path = config.audio_path
tts_url = config.url
file_path = 'E:\\Computer\\QQbot-2\\MiniChovy-2\\temp2.wav'


sub_plugins = nonebot.load_plugins(
    str(Path(__file__).parent.joinpath("plugins").resolve())
)

group_id = config.group_id
api_key = config.api_key
message_max = config.message_max

url = f"https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId={group_id}"
headers = {"Authorization":f"Bearer {api_key}", "Content-Type":"application/json"}

# tokens_to_generate/bot_setting/reply_constraints可自行修改
request_body = payload = {
    "model":"abab6.5-chat",
    "tokens_to_generate":5000,
    "reply_constraints":{"sender_type":"BOT", "sender_name":"MiniChovy"},
    "messages":[],
    "bot_setting":[
        {
            "bot_name":"MiniChovy",
            "content":"1.一个QQ聊天机器人2.只能进行聊天内容回复，回复的内容只有简单文本，不存在Markdown等格式的内容。3.回复内容最多5句话。4.说话会以喵结尾。5.别人说话也会以喵结尾，注意辨别",
        }
    ],
}

params = {
        "character": "【崩铁】花火",
        "emotion": "平静",
        "text": '',
        "speed": 0.9,
        "stream": False,
        "save_temp": True,
    }

test_audio = on_command("AI音频", priority=1)
user_list,ai_isopen = load_user_list_from_csv(config.user_list_path)



@test_audio.handle()
async def _(bot: Bot, state: T_State, event:GroupMessageEvent ,message: Message = CommandArg()):
    message_text = str(message)  # 将Message对象中的内容转化为字符串
    user_id = event.user_id
    request_body["messages"].append({"sender_type": "USER", "sender_name": f"{user_id}", "text": message_text})

    # 检查消息数量，如果超过message_max条，移除最早的消息
    if len(request_body["messages"]) > message_max:
        request_body["messages"] = request_body["messages"][-message_max:]

    try:
        response = requests.post(url, headers=headers, json=request_body)
        reply = response.json()["reply"]
        params["text"] = reply
        reply_response = requests.post(tts_url, json=params)
        with open(file_path, 'wb') as f:
            f.write(reply_response.content)
        # await test_audio.send(f"【崩铁】花火：{reply}")
        await test_audio.send(MessageSegment.record(file_path))
        new_messages = response.json()["choices"][0]["messages"]

        # 检查新消息数量，确保总数不超过message_max条
        if len(request_body["messages"]) + len(new_messages) > message_max:
            request_body["messages"] = request_body["messages"][-(message_max - len(new_messages)):]

        request_body["messages"].extend(new_messages)
    except Exception as e:
        await bot.send(event, f"Error: {e}")
