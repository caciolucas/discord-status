from discord_api_client import DiscordAPIClient
from mqtt_client import MQTTClient
from dotenv import load_dotenv
from os import getenv


class StatusChanger():
    status_options = {
        'working': {
            'custom_status': {'text': 'Working working working...', 'emoji_id': '773966697987047514', 'emoji_name': 'cat_typing'},
            'status': 'online'
        },
        'lunchbreak': {
            'custom_status': {'text': 'Lunch break', 'emoji_id': '804617099484987403', 'emoji_name': 'dogburg1'},
            'status': 'idle'
        },
        'clear' : {
            'custom_status': None,
        },
        'invisible': {
            'status': 'invisible'
        },
        'full_offline': {
            'custom_status': None,
            'status': 'invisible'
        },
        'gameoff': {
            'show_current_game': False
        },
        'gameon': {
            'show_current_game': True
        }
    }

    def __init__(self, mqtt_client, discord_client):
        self.mqtt_client = mqtt_client
        self.discord_client = discord_client
        self.mqtt_client.set_on_connect_callback(self.handle_connect)
        self.mqtt_client.set_on_message_callback(self.handle_message)


    def change_status(self, name):
        if name in self.status_options:
            self.discord_client.change_status(self.status_options[name])
        else:
            print("Não conheço esse status")

    def handle_connect(self, client, userdata, flags, rc):
        print("[Status da conexão] " + str(rc))
        client.subscribe(self.mqtt_client.topic)
        print("[Conectando ao broker] " + str(self.mqtt_client.topic))

    def handle_message(self, client, userdata, msg):
        msg = msg.payload.decode("utf-8")
        print('[Recebeu] ' + msg)
        commands = msg.split(' ')
        if len(commands) > 0:
            if commands[0] == 'status':
                self.change_status(commands[1])
            else:
                print("Não entendi o comando!")

    def run(self):
        self.mqtt_client.connect_broker()
        self.mqtt_client.lets_go()


load_dotenv()

mqtt_client = MQTTClient(getenv('MQTT_BROKER'), getenv('MQTT_TOPIC'), int(getenv('MQTT_PORT')), 60)
discord_client = DiscordAPIClient(getenv('USER_TOKEN'))

sc = StatusChanger(mqtt_client, discord_client)
sc.run()
