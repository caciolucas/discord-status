import requests


class DiscordAPIClient:
    """Class to store methods to Discord API endpoints"""
    base_url = 'https://discord.com/api/v9/users/@me/'
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': self.token}
    
    
    def change_status(self, status):
        if 'custom_status' in status:
            requests.patch(self.base_url + 'settings', headers=self.headers, json={'custom_status': status.get('custom_status')})
        if 'status' in status:
            requests.patch(self.base_url + 'settings', headers=self.headers, json={'status': status.get('status')})
    
    
