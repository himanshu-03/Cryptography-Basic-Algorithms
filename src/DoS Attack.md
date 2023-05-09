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





