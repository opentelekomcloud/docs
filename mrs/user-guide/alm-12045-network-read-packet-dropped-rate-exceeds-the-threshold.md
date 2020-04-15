# ALM-12045 Network Read Packet Dropped Rate Exceeds the Threshold<a name="EN-US_TOPIC_0125375900"></a>

## Description<a name="s709634c7f4734dbf8259d8eaddbf4df9"></a>

The system checks the network read packet dropped rate every 30 seconds and compares the actual packet dropped rate with the threshold \(the default threshold is 0.5%\). This alarm is generated when the system detects that the network read packet dropped rate exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Reading** \> **Network Read Packet Rate Information** \> **Read Packet Dropped Rate**.

When the  **hit number** is 1, this alarm is cleared when the network read packet dropped rate is less than or equal to the threshold. When the **hit number**  is greater than 1, this alarm is cleared when the network read packet dropped rate is less than or equal to 90% of the threshold.

Alarm detection is disabled by default. If you want to enable this function, check whether alarm sending can be enabled based on section "Check the system environment."

## Attribute<a name="s3c47b49536fc4fb490aa6730ca915ce8"></a>

<a name="te13fed71a45b41f59af02192892a2011"></a>
<table><thead align="left"><tr id="r82e3eb18ac4941fa9f16baa83366fd1e"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a0091dc6034a44db59d770ce525d2f37d"><a name="a0091dc6034a44db59d770ce525d2f37d"></a><a name="a0091dc6034a44db59d770ce525d2f37d"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a2b3fac25611242478fa751e76658770e"><a name="a2b3fac25611242478fa751e76658770e"></a><a name="a2b3fac25611242478fa751e76658770e"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a1aaf3227c0e740efb87785b2f640f312"><a name="a1aaf3227c0e740efb87785b2f640f312"></a><a name="a1aaf3227c0e740efb87785b2f640f312"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r2ba2dcc4a87747548e602e545f20804e"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="ac1e27943243140309fc12dca691d4611"><a name="ac1e27943243140309fc12dca691d4611"></a><a name="ac1e27943243140309fc12dca691d4611"></a>12045</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a855e297ca2a54230b2a0a162563edae4"><a name="a855e297ca2a54230b2a0a162563edae4"></a><a name="a855e297ca2a54230b2a0a162563edae4"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a53cf754cc8b04e20aa9d18383f8602f1"><a name="a53cf754cc8b04e20aa9d18383f8602f1"></a><a name="a53cf754cc8b04e20aa9d18383f8602f1"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s98ffc627da0743beabb6e7d86f7c3ea2"></a>

<a name="tad1c2a802be14d7eaead9288647279fc"></a>
<table><thead align="left"><tr id="r5e88e2d54d514538ba05fd0efb4ab6e0"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ae911714aa90b401ca5b9630d4e73d4cf"><a name="ae911714aa90b401ca5b9630d4e73d4cf"></a><a name="ae911714aa90b401ca5b9630d4e73d4cf"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="ad7d3561cf71b4ab3b302dd2b9b3cd65a"><a name="ad7d3561cf71b4ab3b302dd2b9b3cd65a"></a><a name="ad7d3561cf71b4ab3b302dd2b9b3cd65a"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r8f84482b78674a1a9978547c92bbc48f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a452b7287b1fc434a9e8ec5159b5a4a8c"><a name="a452b7287b1fc434a9e8ec5159b5a4a8c"></a><a name="a452b7287b1fc434a9e8ec5159b5a4a8c"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a270432141d3a44faa6514e44315135b1"><a name="a270432141d3a44faa6514e44315135b1"></a><a name="a270432141d3a44faa6514e44315135b1"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r76fe1a68de284e59beff46e6f7a12148"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a4cf2b9a11af749baa9f7b8ac6d0cea93"><a name="a4cf2b9a11af749baa9f7b8ac6d0cea93"></a><a name="a4cf2b9a11af749baa9f7b8ac6d0cea93"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a48b4eba2f3f944ad9a9b8dfb85ad43e3"><a name="a48b4eba2f3f944ad9a9b8dfb85ad43e3"></a><a name="a48b4eba2f3f944ad9a9b8dfb85ad43e3"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9b5e9706049f454eb90e8cb345825588"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1a81d98ccc224caa85f985dd049a232e"><a name="a1a81d98ccc224caa85f985dd049a232e"></a><a name="a1a81d98ccc224caa85f985dd049a232e"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af3066c48f1a847d2b26e69107d78e8c6"><a name="af3066c48f1a847d2b26e69107d78e8c6"></a><a name="af3066c48f1a847d2b26e69107d78e8c6"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r4ac26bac5f294fd69834a42087b54410"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a29b0d28324574406bfb388f7f78a786a"><a name="a29b0d28324574406bfb388f7f78a786a"></a><a name="a29b0d28324574406bfb388f7f78a786a"></a>NetworkCardName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0de1bce505cf489d976ed80b2fef5ca3"><a name="a0de1bce505cf489d976ed80b2fef5ca3"></a><a name="a0de1bce505cf489d976ed80b2fef5ca3"></a>Specifies the network port for which the alarm is generated.</p>
</td>
</tr>
<tr id="rd7c7b15920bf40b0822e006fa443f839"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a80613c512b7a49f4b7241a2e3ea040ad"><a name="a80613c512b7a49f4b7241a2e3ea040ad"></a><a name="a80613c512b7a49f4b7241a2e3ea040ad"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a2edafa56b6404e46b36280baf5998082"><a name="a2edafa56b6404e46b36280baf5998082"></a><a name="a2edafa56b6404e46b36280baf5998082"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s9181dadc926a42d09affba75454a3e0c"></a>

The service performance deteriorates or services time out.

Precautions: In SUSE \(kernel: 3.0 or later\) or Red Hat 7.2, because the system kernel modifies the mechanism for counting read and discarded packets, this alarm may be generated even when the network is normal. Services are not adversely affected. You are advised to check whether the alarm is caused by this problem based on section "Check the system environment."

## Possible Causes<a name="se6141f1163f744649ae106bfdea90dbf"></a>

-   An OS exception occurs.
-   The NIC has configured the active/standby bond mode.
-   The alarm threshold is set improperly.
-   The network is abnormal.

## Procedure<a name="sbe03203d0d5d4e96a54eeaa1074c3bf5"></a>

**Check the network packet dropped rate.**

1.  Use PuTTY to log in to any node for which the alarm is not generated in the cluster as user  **omm** and run the **ping** _IP address_ _-c_ **100**  command to check whether network packet loss occurs.

    ```
    # ping 10.10.10.12 -c 5   
    PING 10.10.10.12 (10.10.10.12) 56(84) bytes of data.   
    64 bytes from 10.10.10.11: icmp_seq=1 ttl=64 time=0.033 ms   
    64 bytes from 10.10.10.11: icmp_seq=2 ttl=64 time=0.034 ms   
    64 bytes from 10.10.10.11: icmp_seq=3 ttl=64 time=0.021 ms   
    64 bytes from 10.10.10.11: icmp_seq=4 ttl=64 time=0.033 ms   
    64 bytes from 10.10.10.11: icmp_seq=5 ttl=64 time=0.030 ms     
    --- 10.10.10.12 ping statistics ---   
    5 packets transmitted, 5 received, 0% packet loss, time 4001ms   rtt min/avg/max/mdev = 0.021/0.030/0.034/0.006 ms
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   **IP address**: indicates the value of **HostName** in the alarm location information. To query the value of **OM IP**  and **Business IP**, click **Host**  on MRS Manager.  
    >-   **-c:**  indicates the check times. The default value is **100**.  

    -   If yes, go to  [10](#l33e609ad9e514d48a71f2c309d57e4b1).
    -   If no, go to  [2](#la6b3c8af4c5847ff9a4402a7dfa0a6b2).


**Check the system environment.**

1.  <a name="la6b3c8af4c5847ff9a4402a7dfa0a6b2"></a>Use PuTTY to log in as user  **omm**  to the active OMS node or the node for which the alarm is generated.
2.  Run the  **cat /etc/\*-release**  command to check the OS type.
    -   If EulerOS is used, go to  [4](#l4b91d56748204d7b83757a831fa003ac).

        ```
        # cat /etc/*-release
        EulerOS release 2.0 (SP2)
        EulerOS release 2.0 (SP2)
        ```

    -   If SUSE is used, go to  [5](#l9ab364a3852c4ceaa9ac181f30b1e215).

        ```
        # cat /etc/*-release
        SUSE Linux Enterprise Server 11 (x86_64)
        VERSION = 11
        PATCHLEVEL = 3
        ```

    -   If another OS is used, go to  [10](#l33e609ad9e514d48a71f2c309d57e4b1).

3.  <a name="l4b91d56748204d7b83757a831fa003ac"></a>Run the  **cat /etc/euleros-release**  command to check whether the OS version is

    EulerOS 2.2.

    ```
     # cat  /etc/euleros-release
    EulerOS release 2.0 (SP2)
    ```

    -   If yes, the alarm sending function cannot be enabled. Go to  [6](#la7ffe095a0134e60a54777d3a4d36232).

    -   If no, go to  [10](#l33e609ad9e514d48a71f2c309d57e4b1).

4.  <a name="l9ab364a3852c4ceaa9ac181f30b1e215"></a>Run the  **cat /proc/version**  command to check whether the SUSE kernel version is 3.0 or later.

    ```
    # cat /proc/version
    Linux version 3.0.101-63-default (geeko@buildhost) (gcc version 4.3.4 [gcc-4_3-branch revision 152973] (SUSE Linux) ) #1 SMP Tue Jun 23 16:02:31 UTC 2015 (4b89d0c)
    ```

    -   If yes, the alarm sending function cannot be enabled. Go to  [6](#la7ffe095a0134e60a54777d3a4d36232).
    -   If no, go to  [10](#l33e609ad9e514d48a71f2c309d57e4b1).

5.  <a name="la7ffe095a0134e60a54777d3a4d36232"></a>Log in to MRS Manager and choose  **System** \> **Configuration** \> **Threshold Configuration**.
6.  In the navigation tree of the  **Threshold Configuration** page, choose **Network Reading** \> **Network Read Packet Rate Information**  \> **Read Packet Dropped Rate**. In the area on the right, check whether **Send Alarm**  is selected.
    -   If yes, the alarm sending function has been enabled. Go to  [8](#l65a6c21dcb6e4bdeacb55d1469cc2ed1).
    -   If no, the alarm sending function has been disabled. Go to  [9](#l70f97c17eb4448a0a7e823b6fb873642).

7.  <a name="l65a6c21dcb6e4bdeacb55d1469cc2ed1"></a>In the area on the right, deselect  **Send Alarm** to disable the checking of **Network Read Packet Dropped Rate Exceeds the Threshold**.
8.  <a name="l70f97c17eb4448a0a7e823b6fb873642"></a>On the  **Alarm** page of MRS Manager, search for the **12045**  alarm. If the alarm is not cleared automatically, clear it manually. No further action is required.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The ID of alarm  **Network Read Packet Dropped Rate Exceeds the Threshold**  is 12045.  


**Check whether the NIC has configured the active/standby bond mode.**

1.  <a name="l33e609ad9e514d48a71f2c309d57e4b1"></a>Use PuTTY to log in to the alarm node as user  **omm**. Run the **ls -l /proc/net/bonding**  command to check whether directory **/proc/net/bonding**  exists on the alarm node.
    -   If yes, the NIC has configured the active/standby bond mode, as shown in the following. Go to  [11](#l3d45d33dad56463095cfd08a6437575c).

        ```
        # ls -l /proc/net/bonding/
        total 0
        -r--r--r-- 1 root root 0 Oct 11 17:35 bond0
        ```

    -   If no, the NIC has not configured the active/standby bond mode, as shown in the following. Go to  [13](#l0b574312261e43eda6044ccb7aeabd79).

        ```
        # ls -l /proc/net/bonding/
        ls: cannot access /proc/net/bonding/: No such file or directory
        ```

2.  <a name="l3d45d33dad56463095cfd08a6437575c"></a>Run the  **cat /proc/net/bonding/**_bond0_ command and check whether the value of **Bonding Mode**  is  **fault-tolerance.**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >**bond0** indicates the name of the bond configuration file. Use the file name queried in [10](#l33e609ad9e514d48a71f2c309d57e4b1)  in practice.  

    ```
    # cat /proc/net/bonding/bond0 
    Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)
    
    Bonding Mode: fault-tolerance (active-backup)
    Primary Slave: eth1 (primary_reselect always)
    Currently Active Slave: eth1
    MII Status: up
    MII Polling Interval (ms): 100
    Up Delay (ms): 0
    Down Delay (ms): 0
    
    Slave Interface: eth0
    MII Status: up
    Speed: 1000 Mbps
    Duplex: full
    Link Failure Count: 1
    Slave queue ID: 0
    
    Slave Interface: eth1
    MII Status: up
    Speed: 1000 Mbps
    Duplex: full
    Link Failure Count: 1
    Slave queue ID: 0
    ```

    -   If yes, the NIC has configured the active/standby bond mode. Go to  [12](#l8c7758b3d8844889a7d8e837644ed027).
    -   If no, the NIC has not configured the active/standby bond mode. Go to  [13](#l0b574312261e43eda6044ccb7aeabd79).

3.  <a name="l8c7758b3d8844889a7d8e837644ed027"></a>Check whether the NIC of the  **NetworkCardName**  parameter in the alarm details is the standby NIC.
    -   If yes, manually clear the alarm on the Alarms page because the alarm on the standby cannot be automatically cleared. No further action is required.
    -   If no, go to  [13](#l0b574312261e43eda6044ccb7aeabd79).

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >Method of determining whether an NIC is standby: In the /**proc/net/bonding/**_bond0_  configuration file, check whether the NIC name of the **NetworkCardName** parameter is the same as the **Slave Interface**, but is different from **Currently Active Slave**  \(indicating the current active NIC\). If the answer is yes, the NIC is a standby one.  



**Check whether the threshold is set properly.**

1.  <a name="l0b574312261e43eda6044ccb7aeabd79"></a>Log in to MRS Manager and check whether the alarm threshold is set properly. \(By default, 0.5% is a proper value. However, users can configure the value as required.\)
    -   If yes, go to  [16](#l604d1952f69c465a9b9d1c903335a055).
    -   If no, go to  [14](#l68b3f046148f477c838aa08c0fa16f8a).

2.  <a name="l68b3f046148f477c838aa08c0fa16f8a"></a>Based on actual usage condition, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Reading** \> **Network Read Packet Rate Information** \> **Read Packet Dropped Rate**  to modify the alarm threshold.

    For details, see  [Figure 1](#ff561272bb42947c1ba2f21b0bc6e96b1).

    **Figure  1**  Setting alarm thresholds<a name="ff561272bb42947c1ba2f21b0bc6e96b1"></a>  
    ![](figures/setting-alarm-thresholds.png "setting-alarm-thresholds")

3.  Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [16](#l604d1952f69c465a9b9d1c903335a055).


**Check whether the network is normal.**

1.  <a name="l604d1952f69c465a9b9d1c903335a055"></a>Contact the system administrator to check whether the network is abnormal.
    -   If yes, go to  [17](#l8f82007995bd462dac732af8de9c85bb)  to rectify the network fault.
    -   If no, go to  [18](#l0bed6a1457bc4d6b84d050dd8069e2f3).

2.  <a name="l8f82007995bd462dac732af8de9c85bb"></a>Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [18](#l0bed6a1457bc4d6b84d050dd8069e2f3).


**Collect fault information.**

1.  <a name="l0bed6a1457bc4d6b84d050dd8069e2f3"></a>On MRS Manager, choose  **System** \> **Export Log**.
2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s63525dc70bd542d68b18c32dcbaa56a6"></a>

N/A

