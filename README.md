# ADVP_Python_Proj with [DR.Ali Komaty](https://github.com/AKomaty)
>_Python course project_

[![* welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

## Introduction:

Because of the rise in crime and theft in our communities, a home security system is becoming increasingly vital. They can offer us live or recorded video footage from within our property. Indeed, the installation of surveillance devices has resulted in the arrest of many criminals due to undeniable video evidence. This is why many individuals invest in security cameras to secure their homes and business.
What is the surveillance system? 

### It is a system used for: 
	1. The detection and tracking of moving objects.
	2. An extra measure of security.
	3. Improved the security of people, buildings, and valuables.

### Some applications of Surveillance Systems:
	* Banks.
	* Hospitals.
	* Schools and universities.
	* Car park.
	* Shops.

## System Overview:

### Our system is based on **`server-client`** programming: ([Server](#how-to-run-the-program)/[Client](#how-to-run-the-program))
    - You need to log in first to be able to use this application.
    - The data will be transformed as HMAC (hash-based message authentication code).
    - The HMAC will be generated by the server for the client.

### The main libraries used in this app:
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

### The main features of the app are:
	* Movement detection with timeline.
	* Clients alert.
	* All data are saved in SQL. 
	* An encrypted video is transferred between the server and the client using AES using CBC mode.
	* The application will auto-reconnect in case the connection was lost.
	* Notify the client by sending an email when an object is detected.
	
## Package to install:
   `pip install -r requirements.txt`
   
  
	
## How to run the program:
>If your `FireWall` is ON, you should `Allow` this app is in the `Firewall Settings`, or turn it off

1. Open `Server.py` [Server](https://github.com/AHazimy/ADVP_Python_Proj/edit/main/Server.py):
  
  ![Server](https://github.com/AHazimy/ADVP_Python_Proj/blob/main/ScreenShots/Run_camera_and_server.png)
  
  :point_right: Press `Open Camera`
  :point_right: Press `Run Server`
  
  >Now your server is up, and available to accept clients' connections

  ### You should export the `Password` for the client:
  
  ![Server](https://github.com/AHazimy/ADVP_Python_Proj/blob/main/ScreenShots/Export_pass_to_client.png)
  
  :point_right: Go to `Password` tab :point_right: Write your `Username` and `Password` :point_right: Press `Apply Hash Function` :point_right:Export the `Password` file (.db) to the [PasswordDB](https://github.com/AHazimy/ADVP_Python_Proj/blob/main/PasswordDB) folder by pressing `Export`
  
2. Open `Alert.py` [Client](https://github.com/AHazimy/ADVP_Python_Proj/edit/main/Alert.py):
  >You can run `Alert.py` on the same machine with the server using LoopBackIP `127.0.0.1` (in [AlertConfig.ini](https://github.com/AHazimy/ADVP_Python_Proj/edit/main/AlertConfig.ini)), or on another machine

  ![Client_Login](https://github.com/AHazimy/ADVP_Python_Proj/blob/main/ScreenShots/Login.png)
  
  :point_right:Enter your `Username` and `Password`
  
  ![Client](https://github.com/AHazimy/ADVP_Python_Proj/blob/main/ScreenShots/Client.png)
  
  >Now your `Client` app is running
  
  ### Explaination:
   :diamond_shape_with_a_dot_inside: `Connection Status`: if the client is connected to server (Ping has a reply) :arrow_right: `Scanning`, if no :arrow_right: `Reconnecting`
   
   >On the same machine the ping always has a reply, so `Connection Status` is always `Scanning`
      
   :diamond_shape_with_a_dot_inside: `Email Notification`: if check box is checked, when a movement's detected you will receive an email contain the time of the movement. (Find the email in [AlertConfig.ini](https://github.com/AHazimy/ADVP_Python_Proj/edit/main/AlertConfig.ini))
   
   :diamond_shape_with_a_dot_inside: `Theme`: `Dark` or `Light` theme, the last theme will be loaded when the app is relaunched
   
   :diamond_shape_with_a_dot_inside: `Pause Duration`: the duration of the mute of the app, (the time of detection + duration value), you can change this value by checking the check box, or in [AlertConfig.ini](https://github.com/AHazimy/ADVP_Python_Proj/edit/main/AlertConfig.ini)
   
   :diamond_shape_with_a_dot_inside: `Alert Sound`: choose the alert sound of the detection, you can test it by pressing `:arrow_forward:`, if you want to add a sound :arrow_right: import any (.wav) to  [Sound_Folder](https://github.com/AHazimy/ADVP_Python_Proj/edit/main/Sound)
   
   :diamond_shape_with_a_dot_inside: `Date/Time of last detection`: the datetime of the last detection of the movements
   
   :diamond_shape_with_a_dot_inside: `Live Video Streaming`: the `Live ENCRYPTED Video` captured by the camera of the `Server`
   
   :diamond_shape_with_a_dot_inside: `Stop`: after detect a movement, press `Stop` button to mute the sound for the same duration in `Pause Duration`
   
   :diamond_shape_with_a_dot_inside: `SQL`: by pressing `Open SQL Data` button you'll get the window below:
   
   ![SQL](https://github.com/AHazimy/ADVP_Python_Proj/blob/main/ScreenShots/SQL.png)
    
   :small_blue_diamond:`The comboBox list` is for three dataframe: :white_medium_small_square:App_Running :white_medium_small_square:Connection_Between_Server_And_Client :white_medium_small_square:Detection_Time, (Saved using `SQLite` Database)
   
   :small_blue_diamond:`Export Timeline` button is to export a timeline graph of this three dataframe using `Plotly` lib
   
   :small_blue_diamond:`Export Excel` button is to export an excel for the `Detection` dataframe
     
      

  
  
_@BY-[Aly](https://github.com/AHazimy)-&-[Fatima](https://github.com/hazimyfatima)-HZ:copyright::+1:_
