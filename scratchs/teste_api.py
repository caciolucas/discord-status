import requests
import os, dotenv

dotenv.load_dotenv()

token = os.getenv('USER_TOKEN')

response = requests.patch('https://discord.com/api/v9/users/@me/settings', 
                                                                    json={
                                                                        "custom_status":{
                                                                            "text":"Working...",
                                                                            "expires_at":"2021-07-15T03:00:00.000Z",
                                                                            "emoji_id":"773966697987047514",
                                                                            "emoji_name":"cat_typing"}},
                                                                    headers={"Authorization": token}
                                                                    )