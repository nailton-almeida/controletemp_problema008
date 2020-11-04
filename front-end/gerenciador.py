import json
import paho.mqtt.client as paho
import ssl

class Subs(object):

    def subs_temp(self):
        temp1 = 0

        awshost = "a1oj1gc5wwye8r-ats.iot.us-east-1.amazonaws.com"  # Endpoint
        awsport = 8883  # Port no.
        clientId = "ar_condicionado"  # Thing_Name
        thingName = "ar_condicionado"  # Thing_Name
        caPath = "./Certificado_Ar/rootCA.pem"  # Root_CA_Certificate_Name
        certPath = "./Certificado_Ar/arcond_cert.cert"  # <Thing_Name>.cert.pem
        keyPath = "./Certificado_Ar/arcond-private.pem"  # <Thing_Name>.private.key

        def on_connect(client, userdata, flags, rc):
            client.subscribe("celsius", 0)

        def on_message(client, userdata, msg):
            temp_atual = json.loads(msg.payload)
            self.temperatura = temp_atual["temperature_cofre"]
            self.umidade = temp_atual["umidade"]
            self.temp_ext = temp_atual["temp_externa"]

            mqttc.disconnect()

        mqttc = paho.Client()
        mqttc.on_connect = on_connect
        mqttc.on_message = on_message

        mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED,
                      tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
        mqttc.connect(awshost, awsport, keepalive=60)

        mqttc.loop_forever()
        return self.temperatura, self.umidade, self.temp_ext
