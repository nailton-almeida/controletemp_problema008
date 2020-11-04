from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import logging
import json
import time

# Read in command-line parameters
useWebsocket = False
host = "a1oj1gc5wwye8r-ats.iot.us-east-1.amazonaws.com"
rootCAPath = "./Certificados/rootCA.pem"
certificatePath = "./Certificados/termometro.crt"
privateKeyPath = "./Certificados/termometro.private.key"

#Configure logging
logger = None
if sys.version_info[0] == 3:
    logger = logging.getLogger("core")  # Python 3
else:
    logger = logging.getLogger("AWSIoTPythonSDK.core")  # Python 2

logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
#myAWSIoTMQTTClient = None

myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub")
myAWSIoTMQTTClient.configureEndpoint(host, 8883)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

thing = "termometro"
topic = "celsius3"

# Publish to the same topic in a loop forever
while True:

     with open('temp_interna.json', 'r') as file:
        tp = file.read()
        tp = json.loads(tp)

     myAWSIoTMQTTClient.publish(topic, json.dumps(tp), 1)
     #print("O dispositivo {} reportou a temperatura {} pelo topico {}.".format(thing, temp, topic))
     time.sleep(1)