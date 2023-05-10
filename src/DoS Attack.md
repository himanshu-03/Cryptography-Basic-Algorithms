## IP Address of Machines:

1. Windows

    ```bash
    ipconfig
    ```

2. Linux

    ```bash
    ifconfig
    ```

<br />

## Ubuntu/ Linux:

1. Pause the capturing of packets in Wireshark

2. Run the command:

    ```bash
    sudo apt-get install hping3
    ```

3. Start capturing packets in Wireshark

4. Run the command to capture packets in Wireshark:

    ```bash
    sudo hping3 -S --flood {IP Address of Linux}
    ```

5. Pause the Wireshark Packet Capturing again and see the `source` and `destination` 


<br />



The command "hping3 -1 --flood --rand-source -c 10000 192.168.68.107" is a command-line tool used to perform network testing and analysis. Here's a breakdown of what each part of the command means:

hping3: This is the name of the tool being used.
-1: This option specifies the protocol to be used. In this case, it's ICMP (Internet Control Message Protocol), which is commonly used for diagnostic purposes in networking.
--flood: This option tells hping3 to flood the target with packets as quickly as possible, without waiting for a response.
--rand-source: This option tells hping3 to use random source IP addresses for the packets it sends. This can help to obscure the identity of the sender and make it harder to trace the attack back to its source.
-c 10000: This option specifies the number of packets to send. In this case, it's 10,000 packets.
192.168.68.107: This is the IP address of the target host that will receive the packets.
In summary, the hping3 command is being used to flood a target host with 10,000 ICMP packets, using random source IP addresses to try and evade detection. This is often used as a form of Denial of Service (DoS) attack, as the flood of packets can overload the target's network and cause it to slow down or crash. It is important to note that such activities may be illegal and can have severe consequences.





