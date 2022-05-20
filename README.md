# ADVP_Python_Proj
>_Python course project_
[Test]("main/Alert.py")
Introduction:

Because of the rise in crime and theft in our communities, a home security system is becoming increasingly vital. They can offer us live or recorded video footage from within our property. Indeed, the installation of surveillance devices has resulted in the arrest of many criminals due to undeniable video evidence. This is why many individuals invest in security cameras to secure their homes and business.
What is the surveillance system? 
It is a system used for: 
	1. The detection and tracking of moving objects.
	2. An extra measure of security.
	3. Improved the security of people, buildings, and valuables.

Some applications of Surveillance Systems:
	* Banks.
	* Hospitals.
	* Schools and universities.
	* Car park.
	* Shops.

System Overview:

Our system is based on server-client programming :
You need to log in first to be able to use this application.
The data will be transformed as HMAC (hash-based message authentication code).
The HMAC will be generated by the server for the client.

The main libraries used in this app:
	* Opencv.
	* Pyqt5.
	* Pandas.
	* Plotly.
	* Threading.
	* Winsound.
	* Socket.
	* SQLite.
	* HashLib.
	* datetime.
	* Cipherdome.

The main features of the app are:
	* Movement detection with timeline.
	* Clients alert.
	* All data are saved in SQL. 
	* An encrypted video is transferred between the server and the client using AES using CBC mode.
	* The application will auto-reconnect in case the connection was lost.
	* Notify the client by sending an email when an object is detected.
