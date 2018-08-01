from iota import *
from iota import TryteString
import paho.mqtt.client as mqtt

api = Iota(
 'http://node06.iotatoken.nl:14265','IIOUUAEPAHHZAXCHGZDGUKTQMPEGS9LQES9CRCE9ABTAKYJWSKSYRKGFTZM9LCDSFNJHPSELJSNJVGHMY'
 )

addresstobeused = object()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("IOTA_Transaction_Receiver_Address/")

def on_message(client,userdata,msg):
    if msg.payload:
        addresstobeused = str(msg.payload)
        print(msg.topic + " " + addresstobeused)
        print("Received the address!")
        transfers = api.get_account_data()
        print(transfers)
        bundle = api.send_transfer(
         depth=100,
         transfers=[
          ProposedTransaction(
           # Recipient of the transfer.
           address=Address(addresstobeused[2:-1]).with_valid_checksum(),
           # Amount of IOTA to transfer.
           # This value may be zero.
           value=0,
           # Optional tag to attach to the transfer.
           tag=Tag('TESTING'),
           # Optional message to include with the transfer.
           # message = TryteString.from_string('Please work!'),
           message=TryteString.from_unicode('Happy Holi!')
          ),
         ],
        )
        print(api.get_node_info())

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("test.mosquitto.org",1883,60)
client.loop_forever()