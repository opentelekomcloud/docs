# What Can I Do If the Communication Between the Primary NIC and Extension NIC of the BMS is Abnormal?<a name="EN-US_TOPIC_0151841132"></a>

## Cause<a name="section1418611694917"></a>

If two NICs on the same network segment are added to a BMS, communication between the primary NIC and extension NIC is abnormal because the BMS gateway strictly verifies the source MAC addresses. For example, in  [Figure 1](#fig9146815125112), the primary NIC and extension NIC are both on the 172.22.9._X_  network segment. A policy-based route needs to be configured to enable communication between the NICs.

**Figure  1**  Network segment of the NICs<a name="fig9146815125112"></a>  
![](figures/network-segment-of-the-nics.png "network-segment-of-the-nics")

## Solution<a name="section14418919529"></a>

1.  Run the following command to add two routing table names \(**net1**  and  **net2**\) and priorities \(**252**  and  **251**\) to the  **/etc/iproute2/rt\_tables**  file:

    **vi /etc/iproute2/rt\_tables**

    ```
    252     net1
    251     net2
    ```

2.  Run the following command to add the NIC routing information to the  **/etc/rc.local**  file:

    **vi /etc/rc.local**

    For example, the IP address of the primary NIC is 172.22.9.7, that of the extension NIC is 172.22.9.206, and that of the BMS gateway is 172.22.9.1, add the following routes:

    ```
    ip route add 172.22.9.0/24 dev bond0 src 172.22.9.7 table net1
    ip route add default via 172.22.9.1 dev bond0 table net1
    ip route add 172.22.9.0/24 dev bond0.3935 src 172.22.9.206 table net2
    ip route add default via 172.22.9.1 dev bond0.3935 table net2
    ip rule add from 172.22.9.7/32 table net1
    ip rule add from 172.22.9.206/32 table net2
    ```


