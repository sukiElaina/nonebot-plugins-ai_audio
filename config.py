from pydantic import BaseModel,Field
from dotenv import load_dotenv
import os
import csv

load_dotenv(dotenv_path='.env.prod')

# 从环境变量中读取API_KEY
audio_path_from_env = os.getenv('AUDIO_PATH')
group_id_from_env = os.getenv('GROUP_ID')
message_max_from_env = os.getenv('MESSAGE_MAX')
user_list_path_from_env = os.getenv('USER_LIST_PATH')
api_key_from_env = os.getenv('API_KEY')


class Config(BaseModel):
    """Plugin Config Here"""
    audio_path: str = Field(audio_path_from_env,description="Path to the audio file") # 这里写上你的音频文件路径
    group_id: str = Field(group_id_from_env, description="The ID of the group") # 这里写上你的MiniMax Group ID
    api_key: str = Field(api_key_from_env, description="The API key for authentication") # 这里写上你的MiniMax API Key
    message_max: int = Field(message_max_from_env, description="The maximum number of messages allowed")
    user_list_path:str =Field(user_list_path_from_env,description="Path to the user list file")
    url : str = Field("http://127.0.0.1:5000/tts",description="URL of the TTS API")
def load_user_list_from_csv(file_path):
    user_list = []
    ai_isopen = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_list.append(int(row['使用用户名单']))
            ai_isopen[int(row['使用用户名单'])] = False
    return user_list,ai_isopen