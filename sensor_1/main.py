from paho.mqtt import client as mqtt_client
import time
import random
import json

broker = 'mqtt'
port = 1883
topic = "test_topic"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# while True:
# 	temp = round(random.uniform(10, 20), 1)
# 	bacteria = round(random.uniform(400, 3000), 1)
# 	print({"sensor_id": 1, "temperature": temp, "bacteria": bacteria})
# 	time.sleep(1)


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    # client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
	msg_count = 0
	while True:
		time.sleep(1)
		temp = round(random.uniform(10, 20), 1)
		bacteria = round(random.uniform(400, 3000), 1)
		msg = {'sensor_id': 1, 'msg_count': msg_count, 'temp': temp, 'bacteria': bacteria}
		result = client.publish(topic, json.dumps(msg))
		# result: [0, 1]
		status = result[0]
		if status == 0:
			print(f"Send `{msg}` to topic `{topic}`")
		else:
			print(f"Failed to send message to topic {topic}")
		msg_count += 1



def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()

