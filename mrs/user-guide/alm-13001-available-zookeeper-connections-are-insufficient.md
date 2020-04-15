# ALM-13001 Available ZooKeeper Connections Are Insufficient<a name="EN-US_TOPIC_0125375977"></a>

## Description<a name="s3bdc6aaa73e34d828be5a66d5e49ec28"></a>

The system checks ZooKeeper connections every 30 seconds. This alarm is generated when the system detects that the number of used ZooKeeper instance connections exceeds the threshold \(80% of the maximum connections\).

This alarm is cleared when the number of used ZooKeeper instance connections is less than the threshold.

## Attribute<a name="sb1aa6e3f66664878b78f3e32197425c0"></a>

<a name="en-us_topic_0035998718_table11533784"></a>
<table><thead align="left"><tr id="en-us_topic_0035998718_row3757979"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998718_p35960896"><a name="en-us_topic_0035998718_p35960896"></a><a name="en-us_topic_0035998718_p35960896"></a><strong id="af65fb57d51694b6b808a172142cc230e"><a name="af65fb57d51694b6b808a172142cc230e"></a><a name="af65fb57d51694b6b808a172142cc230e"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998718_p27151449"><a name="en-us_topic_0035998718_p27151449"></a><a name="en-us_topic_0035998718_p27151449"></a><strong id="a030e017d5c0d45db995f04c81eb75082"><a name="a030e017d5c0d45db995f04c81eb75082"></a><a name="a030e017d5c0d45db995f04c81eb75082"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998718_p51783759"><a name="en-us_topic_0035998718_p51783759"></a><a name="en-us_topic_0035998718_p51783759"></a><strong id="ac745792e38d040d0b22ce18c4ac197a8"><a name="ac745792e38d040d0b22ce18c4ac197a8"></a><a name="ac745792e38d040d0b22ce18c4ac197a8"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998718_row33734921"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998718_p48174063"><a name="en-us_topic_0035998718_p48174063"></a><a name="en-us_topic_0035998718_p48174063"></a>13001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998718_p9785067"><a name="en-us_topic_0035998718_p9785067"></a><a name="en-us_topic_0035998718_p9785067"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998718_p54392930"><a name="en-us_topic_0035998718_p54392930"></a><a name="en-us_topic_0035998718_p54392930"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sc9508701427c496b8a2df490eca18a09"></a>

<a name="en-us_topic_0035998718_table43751230"></a>
<table><thead align="left"><tr id="en-us_topic_0035998718_row43605354"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998718_p42372785"><a name="en-us_topic_0035998718_p42372785"></a><a name="en-us_topic_0035998718_p42372785"></a><strong id="a153bb2b684724c78a6a99d5d44b8a248"><a name="a153bb2b684724c78a6a99d5d44b8a248"></a><a name="a153bb2b684724c78a6a99d5d44b8a248"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998718_p9643552"><a name="en-us_topic_0035998718_p9643552"></a><a name="en-us_topic_0035998718_p9643552"></a><strong id="a58d587997e7b41e2a6e53b771ae0193c"><a name="a58d587997e7b41e2a6e53b771ae0193c"></a><a name="a58d587997e7b41e2a6e53b771ae0193c"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998718_row42930272"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998718_p54800025"><a name="en-us_topic_0035998718_p54800025"></a><a name="en-us_topic_0035998718_p54800025"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998718_p9617010"><a name="en-us_topic_0035998718_p9617010"></a><a name="en-us_topic_0035998718_p9617010"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998718_row19444226"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998718_p31478446"><a name="en-us_topic_0035998718_p31478446"></a><a name="en-us_topic_0035998718_p31478446"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998718_p66726223"><a name="en-us_topic_0035998718_p66726223"></a><a name="en-us_topic_0035998718_p66726223"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998718_row63665103"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998718_p56599738"><a name="en-us_topic_0035998718_p56599738"></a><a name="en-us_topic_0035998718_p56599738"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998718_p21176078"><a name="en-us_topic_0035998718_p21176078"></a><a name="en-us_topic_0035998718_p21176078"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998718_row56366974"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998718_p2322177"><a name="en-us_topic_0035998718_p2322177"></a><a name="en-us_topic_0035998718_p2322177"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998718_p53878657"><a name="en-us_topic_0035998718_p53878657"></a><a name="en-us_topic_0035998718_p53878657"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s7958a8df7dd5432db04b03bd78bc36a2"></a>

Available ZooKeeper connections are insufficient. When the connection usage reaches 100%, external connections cannot be handled.

## Possible Causes<a name="s6f787b3b269242c1b3eb93f4f9e2e3ef"></a>

-   The number of connections to the ZooKeeper node exceeds the threshold.
-   Connection leakage occurs on some connection processes.
-   The maximum number of connections does not meet the requirement of the actual scenario.

## Procedure<a name="se6005cbc9c094371b4f51bb4d8708f05"></a>

1.  Check the connection status.
    1.  On the MRS Manager portal, choose  **Alarm**  \>  **ALM-13001 Available ZooKeeper Connections Are Insufficient**  \>  **Location**. Check the IP address of the alarm node.
    2.  Obtain the PID of the ZooKeeper process. Log in to the alarm node and run the  **pgrep -f proc\_zookeeper**  command.
    3.  Check whether the PID can be successfully obtained.
        -   If yes, go to  [1.d](#l518565766da1408ab463d47bbb0f2e31).
        -   If no, go to  [2](#l3cd58b159a6b4e0ead17bcdd4b62fa83).

    4.  <a name="l518565766da1408ab463d47bbb0f2e31"></a>Obtain all the IP addresses connected to the ZooKeeper instance and the number of connections. Check 10 IP addresses with the top connections. Run the following command based on the obtained PID and IP address:  **lsof -i|grep $pid | awk '\{print $9\}' | cut -d :** **-f 2 | cut -d \\\> -f 2 | awk '\{a\[$1\]++\} END \{for\(i in a\)\{print i,a\[i\] | "sort -r -g -k 2"\}\}' | head -10**. \(**$pid**  is the PID obtained in the preceding step.\)
    5.  Check whether the node IP addresses and the number of connections are successfully obtained.
        -   If yes, go to  [1.f](#ld4daf2bf853b498686b9dae32e2c0053).
        -   If no, go to  [2](#l3cd58b159a6b4e0ead17bcdd4b62fa83).

    6.  <a name="ld4daf2bf853b498686b9dae32e2c0053"></a>Obtain the ID of the port connected to the process. Run the following command based on the obtained PID and IP address:  **lsof -i|grep $pid | awk '\{print $9\}' |cut -d \\\> -f 2 |grep $IP | cut -d :-f 2**. \(**$pid** and **$IP**  are the PID and IP address obtained in the preceding step.\)
    7.  Check whether the port ID is successfully obtained.
        -   If yes, go to  [1.h](#lc2fee9742bf74c12824e4eed2c09db55).
        -   If no, go to  [2](#l3cd58b159a6b4e0ead17bcdd4b62fa83).

    8.  <a name="lc2fee9742bf74c12824e4eed2c09db55"></a>Obtain the ID of the connected process. Log in to each IP address and run the following command based on the obtained port ID:  **lsof -i|grep $port**. \(**$port**  is the port ID obtained in the preceding step.\)
    9.  Check whether the process ID is successfully obtained.
        -   If yes, go to  [1.j](#en-us_topic_0035998718_stepb6).
        -   If no, go to  [2](#l3cd58b159a6b4e0ead17bcdd4b62fa83).

    10. <a name="en-us_topic_0035998718_stepb6"></a>Check whether connection leakage occurs on the process based on the obtained process ID.
        -   If yes, go to  [1.k](#en-us_topic_0035998718_stepb7).
        -   If no, go to  [2](#l3cd58b159a6b4e0ead17bcdd4b62fa83).

    11. <a name="en-us_topic_0035998718_stepb7"></a>Close the process where connection leakage occurs and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l3cd58b159a6b4e0ead17bcdd4b62fa83).

    12. On the MRS Manager portal, choose  **Service**  \>  **ZooKeeper**  \>  **Service Configuration**  \>  **All**  \>  **quorumpeer**  \>  **Performance** and change the value of **maxCnxns** to **20000**  or more.
    13. Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l3cd58b159a6b4e0ead17bcdd4b62fa83).

2.  <a name="l3cd58b159a6b4e0ead17bcdd4b62fa83"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s4a8c68fa81d847b3ae0702dc6d85b3a7"></a>

N/A

