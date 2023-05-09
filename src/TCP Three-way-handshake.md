## Exp Name - Use network sniffing tools to demonstrate the TCP three-way handshake, Use network sniffing tools to demonstrate the difference between http and https.

<br>

Network Sniffing tool used - Wireshark

<br>

1. Open TCET ERP Webiste (http based)

2. Open Wireshark > Wifi Connection

3. Enter the Username, Password and Captch and press login

4. Go to Wireshark and Stop Capturing packets

5. Search for HTTP request (application/x-www-form-urlencoded)

6. Go to cookie setting and click on cookie

7. In the R.H.S you will see your username and password 

8. Find SYN and ACK words and that shows 3 way handshake 

__This shows that http request are not secure__

<br>

9. For HTTPS, open gmail account and Login

10. Close Packet Capturing 

11. On pannel search tcp.port == 443 

12. Search TSLV and see down side, you will find all giberish 

__This shows that https request are secure__