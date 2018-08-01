import paho.mqtt.publish as publish

from iota import *
from iota.crypto.addresses import AddressGenerator

def check_if_already_used(api, address):
 transfers = api.get_account_data()
 print(transfers)
 addresses = transfers['addresses']  # get that one item out of the dictionary.  so now we have a list of bundles.
 for currentAddress in addresses:
  if currentAddress == address:
   print('True That')
   return True
 print('False That')
 return False


api = Iota('http://node06.iotatoken.nl:14265','JH9XBWVXAJVXVRKRQZDPETYCCHREOHJADCBBQMOEFXFWXZEEMMYGLQ9KLJRSVU9FODWCR99EVWQWNSHW9')
addresstobeused = object()

generator = AddressGenerator(seed=b'JH9XBWVXAJVXVRKRQZDPETYCCHREOHJADCBBQMOEFXFWXZEEMMYGLQ9KLJRSVU9FODWCR99EVWQWNSHW9')
iterator = generator.create_iterator(start=0)
for address in iterator:
 if check_if_already_used(api, address):
  print('Inside true')
  addresstobeused = iterator.__next__().with_valid_checksum()
  break
 else:
  addresstobeused = address
  break

print(addresstobeused)
# print (api.were_addresses_spent_from(['FRGLJMPWMXIBNMGGLMPTYDIJCBZURAACTAIGFUZKEBZSJTULWZQLQGRTPTEEYFSMXFHNFQ9ILJLACLBZC'])['states'][0])

# accountData = api.get_account_data()
# bundles = accountData['bundles']
#
# for bundle in bundles:
#     transactions = bundle.transactions
#     for t in transactions:
#         print(t)
#         print("tag: %s" % t.tag)
#         message = t.signature_message_fragment
#         try:
#             print("message: %s" % (message.decode()));
#         except:
#             pass

publish.single("IOTA_Transaction_Receiver_Address/", str(addresstobeused), hostname="test.mosquitto.org")
print("Done")

