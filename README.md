# SmartChargingWithIOTA
Smart charging of electric cars using IOTA cryptocurrency'

This use case implementation is to demonstrate the machine-to-machine interaction between an electric car and an EV charging station, in which the entire transaction including payment is performed using IOTA.

The charging station will have a sensor which would detect the car when it is close by. After the car is detected, the user conveys the number of iota tokens he/she wants to pay, or how many kWh of electricity he/she wants from the charging station. This data is sent to the AWS via a mobile app or html based dashboard. The number of minutes that the car needs to be charged for is calculated using the number of tokens and the price/kWh of energy as decided by the station. This number of minutes is sent to the station by the AWS. The IOTA tokens are transferred from the car to the charging station. When the transaction is validated, the station detects an increase in its token balance, the charging would begin for the calculated number of minutes (provided the car is connected to the station).

Platforms used - IOTA ledger, AWS, Raspberry Pis, Restful Webservices, MQTT, Python, Web Application development.
