import requests


class DiscordAPIClient:
    """Class to store methods to Discord API endpoints"""
    base_url = 'https://discord.com/api/v9/users/@me/'
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': self.token}
    
    
    def change_status(self, status):
        """Loop trough for each option in status and send PATCH request to settings with payload with option name as key and its value as value"""
        for option in status:
            response = requests.patch(self.base_url + 'settings', headers=self.headers, json={option: status.get(option)})
            print(f'[Mudando {option}] {response.status_code} - {response.text}') 

            
    
    
