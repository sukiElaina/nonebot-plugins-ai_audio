from pydantic import BaseModel,Field
import csv

class Config(BaseModel):
    """Plugin Config Here"""
    audio_path: str = Field("E:\\Computer\\QQbot-2\\MiniChovy-2\\src\\plugins\\ai_audio\\audios",description="Path to the audio file")
    group_id: str = Field("1810530961268413127", description="The ID of the group")
    api_key: str = Field("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJXdWhhbiBVbml2ZXJzaXR5IiwiVXNlck5hbWUiOiJXdWhhbiBVbml2ZXJzaXR5IiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE4MTA1MzA5NjEyNzI2MDc0OTYiLCJQaG9uZSI6IjE5ODkxNTI2ODkyIiwiR3JvdXBJRCI6IjE4MTA1MzA5NjEyNjg0MTMxMjciLCJQYWdlTmFtZSI6IiIsIk1haWwiOiJBWnl1YW5qdW5AMTYzLmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDI0LTA4LTE0IDExOjUxOjA1IiwiaXNzIjoibWluaW1heCJ9.bjy0RH-QyuQ4GvngFXmhNKzsGzKMErsNV1dHwjSWbRS3MYuzd6z6ug036v2IBNyTmLGDc9IxZuP9NVp36BQAfakr-naxrJ1Fnfy_DuZzRrKY7XVzEKqaovkimmJZqU1bRY80wQJ1CfjpLRlSQWZB2cr3PJG_lJUSa3TBS6Oz_mGaN2qv14CbGzvqPlTEMJuPuhHQmjzfYhXvvn0vfyoN644tw-661f78PhDJ1zN0nY24La3KUH444cYosQ-6R13_bogeVC9NtkZW9pmME-BpOyVgm4mVz2qM-ADdsvbZCZ_1fJ-pN1g6qQ5WfRfSWLXg9KGGkh3T6howOPrs90VYRg", description="The API key for authentication")
    message_max: int = Field(20, description="The maximum number of messages allowed")
    user_list_path:str =Field( "E:\\Computer\\QQbot-2\\MiniChovy-2\\src\\plugins\\ai_test\\whitelist\\ailist.csv",description="Path to the user list file")
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