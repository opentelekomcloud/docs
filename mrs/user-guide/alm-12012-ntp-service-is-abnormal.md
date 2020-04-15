# ALM-12012 NTP Service Is Abnormal<a name="EN-US_TOPIC_0125375602"></a>

## Description<a name="s85f02e8080d44efaac12ee00b301ef6b"></a>

This alarm is generated when the NTP service on the current node fails to synchronize time with the NTP service on the active OMS node. It is cleared when they succeed in synchronizing time.

## Attribute<a name="s0ba1f2f57d8b442aba45e780f68a33d0"></a>

<a name="tfcd72a4cf9b941059af95232a2316db4"></a>
<table><thead align="left"><tr id="r3f2d162f852142c4816796336bac5558"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035461638_p343074211263"><a name="en-us_topic_0035461638_p343074211263"></a><a name="en-us_topic_0035461638_p343074211263"></a><strong id="en-us_topic_0035461638_b575573101263"><a name="en-us_topic_0035461638_b575573101263"></a><a name="en-us_topic_0035461638_b575573101263"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035461638_p105814441263"><a name="en-us_topic_0035461638_p105814441263"></a><a name="en-us_topic_0035461638_p105814441263"></a><strong id="en-us_topic_0035461638_b52863871263"><a name="en-us_topic_0035461638_b52863871263"></a><a name="en-us_topic_0035461638_b52863871263"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035461638_p214780531263"><a name="en-us_topic_0035461638_p214780531263"></a><a name="en-us_topic_0035461638_p214780531263"></a><strong id="en-us_topic_0035461638_b487076501263"><a name="en-us_topic_0035461638_b487076501263"></a><a name="en-us_topic_0035461638_b487076501263"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r181dcc9600424ec1b122b3d761401f38"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035461638_p646357441263"><a name="en-us_topic_0035461638_p646357441263"></a><a name="en-us_topic_0035461638_p646357441263"></a>12012</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035461638_p298423611263"><a name="en-us_topic_0035461638_p298423611263"></a><a name="en-us_topic_0035461638_p298423611263"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035461638_p433034491263"><a name="en-us_topic_0035461638_p433034491263"></a><a name="en-us_topic_0035461638_p433034491263"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s0662f01fb0964692afd06380558c446c"></a>

<a name="t88b144013a1149dbad386c3b482ad7b1"></a>
<table><thead align="left"><tr id="r6ec98c9311f744848d4ee8060aff4061"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035461638_p668658261263"><a name="en-us_topic_0035461638_p668658261263"></a><a name="en-us_topic_0035461638_p668658261263"></a><strong id="aa076d613dcdb4324bf24114c52b05b08"><a name="aa076d613dcdb4324bf24114c52b05b08"></a><a name="aa076d613dcdb4324bf24114c52b05b08"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035461638_p146874361263"><a name="en-us_topic_0035461638_p146874361263"></a><a name="en-us_topic_0035461638_p146874361263"></a><strong id="en-us_topic_0035461638_b323493561263"><a name="en-us_topic_0035461638_b323493561263"></a><a name="en-us_topic_0035461638_b323493561263"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r79ca526dbdab4ccb8af835dbbbb28a75"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035461638_p356185261263"><a name="en-us_topic_0035461638_p356185261263"></a><a name="en-us_topic_0035461638_p356185261263"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035461638_p549782411263"><a name="en-us_topic_0035461638_p549782411263"></a><a name="en-us_topic_0035461638_p549782411263"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r84d9ee5dfdf141dcadf4a09ca8ebf00c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035461638_p662404731263"><a name="en-us_topic_0035461638_p662404731263"></a><a name="en-us_topic_0035461638_p662404731263"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035461638_p365850281263"><a name="en-us_topic_0035461638_p365850281263"></a><a name="en-us_topic_0035461638_p365850281263"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r02e2d5c522dc45b98b4aa954529798c2"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035461638_p89268291263"><a name="en-us_topic_0035461638_p89268291263"></a><a name="en-us_topic_0035461638_p89268291263"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035461638_p367579931263"><a name="en-us_topic_0035461638_p367579931263"></a><a name="en-us_topic_0035461638_p367579931263"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sd445bf34a04b4e5fa1cf8a7553180e01"></a>

The time on the node is inconsistent with the time on other nodes in the cluster. Therefore, some MRS applications on the node may not run properly.

## Possible Causes<a name="s3883d9fdd4644d27a651b7b7d10c780b"></a>

-   The NTP service on the current node cannot start properly.
-   The current node fails to synchronize time with the NTP service on the active OMS node.
-   The key value authenticated by the NTP service on the current node is inconsistent with that on the active OMS node.
-   The time offset between the node and the NTP service on the active OMS node is large.

## Procedure<a name="sfbdf110a8e9442fca1366f963a8cfdc3"></a>

1.  Check the NTP service on the current node.
    1.  Check whether the  **ntpd** process is running on the node using the following method. Log in to the node and run the **sudo su - root** command to switch the user. Run the following command to check whether the command output contains the **ntpd**  process:

        **ps -ef | grep ntpd | grep -v grep.**

        -   If yes, go to  [2.a](#l9359e283092f411babb2f3f0568b60ad).
        -   If no, go to  [1.b](#la0306044e53b40f6a9d6034e6b9a8f16).

    2.  <a name="la0306044e53b40f6a9d6034e6b9a8f16"></a>Run  **service ntp start**  to start the NTP service.
    3.  Wait 10 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l9359e283092f411babb2f3f0568b60ad).

2.  Check whether the current node can synchronize time properly with the NTP service on the active OMS node.
    1.  <a name="l9359e283092f411babb2f3f0568b60ad"></a>Check whether the node can synchronize time with the NTP service on the active OMS node based on  **Additional Info**  of the alarm.
        -   If yes, go to  [2.b](#l2dc21779eee0455491aab7ddecef6c6d).
        -   If no, go to  [3](#leb527bbacda549838f549d7e3b68ba66).

    2.  <a name="l2dc21779eee0455491aab7ddecef6c6d"></a>Check whether the synchronization with the NTP service on the active OMS node is faulty.

        Log in to the alarm node and run the  **sudo su - root** command to switch the user. Then run the **ntpq -np**  command.

        In the command output, if an asterisk \(\*\) exists before the IP address of the NTP service on the active OMS node, the synchronization is in the normal state. The command output is as follows:

        ```
        remote refid st t when poll reach delay offset jitter ============================================================================== *10.10.10.162 .LOCL. 1 u 1 16 377 0.270 -1.562 0.014
        ```

        If no asterisk \(\*\) exists before the IP address of the NTP service on the active OMS node and the value of  **refid** is **.INIT.**, the synchronization is abnormal. The command output is as follows:

        ```
        remote refid st t when poll reach delay offset jitter ============================================================================== 10.10.10.162 .INIT. 1 u 1 16 377 0.270 -1.562 0.014
        ```

        -   If yes, go to  [2.c](#l18458def85f447a99c388e3a2d3d6bae).
        -   If no, go to  [3](#leb527bbacda549838f549d7e3b68ba66).

    3.  <a name="l18458def85f447a99c388e3a2d3d6bae"></a>Rectify the fault, wait 10 minutes, and then check whether the alarm is cleared.

        -   If yes, no further action is required.
        -   If no, go to  [3](#leb527bbacda549838f549d7e3b68ba66).

        An NTP synchronization failure is usually related to the system firewall. If the firewall can be disabled, disable it and check whether the fault is rectified. If the firewall cannot be disabled, check the firewall configuration policies and ensure that port  **UDP 123**  is enabled. You need to follow specific firewall configuration policies of each system.

3.  <a name="leb527bbacda549838f549d7e3b68ba66"></a>Check whether the key value authenticated by the NTP service on the current node is consistent with that on the active OMS node.

    Run  **cat /etc/ntp/ntpkeys**  to check whether the authentication code with a key value index of 1 is the same as the value of the NTP service on the active OMS node.

    -   If yes, go to  [4.a](#l9644419ea5e94f71a52c97e588835dd7).
    -   If no, go to  [5](#l0c59667bcd894d80ba2170db93a772e4).

4.  Check whether the time offset between the node and the NTP service on the active OMS node is large.
    1.  <a name="l9644419ea5e94f71a52c97e588835dd7"></a>Check whether the time offset is large in  **Additional Info**  of the alarm.
        -   If yes, go to  [4.b](#lab4ad9a736884029ae9ae3d679d2aef6).
        -   If no, go to  [5](#l0c59667bcd894d80ba2170db93a772e4).

    2.  <a name="lab4ad9a736884029ae9ae3d679d2aef6"></a>On the  **Host** page, select the host of the node, and choose **More**  \>  **Stop All Roles**  to stop all the services on the node.

        If the time on the alarm node is earlier than that on the NTP service of the active OMS node, adjust the time on the alarm node to be the same as that on the NTP service of the active OMS node. After doing so, choose  **More**  \>  **Start All Roles**  to start services on the node.

        If the time on the alarm node is later than that on the NTP service of the active OMS node, wait until the time offset is due and adjust the time on the alarm node. After doing so, choose  **More**  \>  **Start All Roles**  to start services on the node.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If you do not wait until the time offset is due, data loss may occur.  

    3.  Wait 10 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [5](#l0c59667bcd894d80ba2170db93a772e4).

5.  <a name="l0c59667bcd894d80ba2170db93a772e4"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## **Related Information**<a name="sa755b5a349a84813a4e7c444ad242ff2"></a>

N/A

