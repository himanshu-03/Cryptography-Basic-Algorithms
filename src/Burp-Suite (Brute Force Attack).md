## Burp-Suite Installation 

Download Burpsuite from below site. 
> https://portswigger.net/burp/releases


1) Install burpsuite community version

2) Go to Proxy setting in burpsuite

        Proxy - > Proxy Setting - > Edit - > Blind to port -> Write port no = 8081
        (Here we are using 127.0.0.1:8081)

3) Go to mozilla browser

        Go to setting -> Network setting  -> Go to Manual Proxy Setting -> 
        HTTP Proxy : 127.0.0.1 -> Port: 8081

        Check the box- Also use the proxy for HTTPS

4) Check for browser is setup for Bursuite

    > http://burp

    Click on CA Certificate and Download the certificate

5)      Go to Mozilla Browser - > Settings - > View Certificate - > 
        Authories Tab - > Import - > Import cacert Certicate - > ok

<br />


## Website for Attack:

> http://testfire.net/login.jsp

> Username : admin

> Password: admin

<br />

## Steps to perform Brute Force Attack

1. Intercept ON
2. Login on Website with wrong username and password
3. Head back to Burp-Suite
4. Right Click > Send to Intruder
5. Attack Type > Cluster Bomb
6. Selecting `username` and `password` and clicking on `$Add$` button
7. Head over to **Payloads**
8. Set `Payload set` to 1
9. In `Payload Settings`, add 5 random entries consisting one with original **Username**
10. Set `Payload set` to 2
11. In `Payload Settings`, add 5 random entries consisting one with the original **Password**
12. Click on **Start Attack** button.
