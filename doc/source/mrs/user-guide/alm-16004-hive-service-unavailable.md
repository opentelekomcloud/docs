# ALM-16004 Hive Service Unavailable<a name="EN-US_TOPIC_0125376060"></a>

## Description<a name="s1697c56f79a4458ba1f3d815d7d3ae38"></a>

The system checks the Hive service status every 30 seconds. This alarm is generated when the Hive service is unavailable and is cleared when the Hive service is in the normal state.

## Attribute<a name="se7e5ad94b0684e458446929d1f0c6e0b"></a>

<a name="en-us_topic_0035998735_table22774600"></a>
<table><thead align="left"><tr id="en-us_topic_0035998735_row4640007"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998735_p40296320"><a name="en-us_topic_0035998735_p40296320"></a><a name="en-us_topic_0035998735_p40296320"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998735_p42776493"><a name="en-us_topic_0035998735_p42776493"></a><a name="en-us_topic_0035998735_p42776493"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998735_p42343927"><a name="en-us_topic_0035998735_p42343927"></a><a name="en-us_topic_0035998735_p42343927"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998735_row7306053"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998735_p54919424"><a name="en-us_topic_0035998735_p54919424"></a><a name="en-us_topic_0035998735_p54919424"></a>16004</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998735_p19288335"><a name="en-us_topic_0035998735_p19288335"></a><a name="en-us_topic_0035998735_p19288335"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998735_p18851291"><a name="en-us_topic_0035998735_p18851291"></a><a name="en-us_topic_0035998735_p18851291"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s29c8f1cbde3142a98c1903dcfcf489a9"></a>

<a name="en-us_topic_0035998735_table50559563"></a>
<table><thead align="left"><tr id="en-us_topic_0035998735_row19612160"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998735_p45081147"><a name="en-us_topic_0035998735_p45081147"></a><a name="en-us_topic_0035998735_p45081147"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998735_p27694303"><a name="en-us_topic_0035998735_p27694303"></a><a name="en-us_topic_0035998735_p27694303"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998735_row28646034"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998735_p38627455"><a name="en-us_topic_0035998735_p38627455"></a><a name="en-us_topic_0035998735_p38627455"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998735_p41816140"><a name="en-us_topic_0035998735_p41816140"></a><a name="en-us_topic_0035998735_p41816140"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998735_row40800942"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998735_p16541999"><a name="en-us_topic_0035998735_p16541999"></a><a name="en-us_topic_0035998735_p16541999"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998735_p64833508"><a name="en-us_topic_0035998735_p64833508"></a><a name="en-us_topic_0035998735_p64833508"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998735_row46630661"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998735_p18987236"><a name="en-us_topic_0035998735_p18987236"></a><a name="en-us_topic_0035998735_p18987236"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998735_p61571180"><a name="en-us_topic_0035998735_p61571180"></a><a name="en-us_topic_0035998735_p61571180"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sfde7e808c2394354a0a2c3e11f157b81"></a>

The system cannot provide data loading, query, and extraction services.

## Possible Causes<a name="s6f063233942446b29d4e8799e19d4b06"></a>

-   The Hive service unavailability may be related to basic services, such as ZooKeeper, HDFS, Yarn, and DBService or caused by the faults of the Hive processes.
    -   The ZooKeeper, HDFS, Yarn, or DBService services are abnormal.
    -   The Hive service process is faulty. If the alarm is caused by a Hive process fault, the alarm report has a delay of about 5 minutes.

-   The network communication between the Hive service and basic services is interrupted.

## Procedure<a name="s209613ebdc7d48eba8bb350230a88925"></a>

1.  Check the HiveServer/MetaStore process status.
    1.  On MRS Manager, choose  **Service**  \>  **Hive**  \>  **Instance**. In the Hive instance list, check whether all HiveSserver/MetaStore instances are in the  **Unknown**  state.
        -   If yes, go to  [1.b](#l8eb07789c80847a3941e81f711018394).
        -   If no, go to  [2](#l42340147e52a435d9d7cc56cc4ce60e0).

    2.  <a name="l8eb07789c80847a3941e81f711018394"></a>Above the Hive instance list, choose  **More**  \>  **Restart Instance**  to restart the HiveServer/MetaStore process.
    3.  In the alarm list, check whether alarm  **ALM-16004 Hive Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l42340147e52a435d9d7cc56cc4ce60e0).

2.  <a name="l42340147e52a435d9d7cc56cc4ce60e0"></a>Check the ZooKeeper service status.
    1.  In the alarm list on MRS Manager, check whether alarm  **ALM-12007 Process Fault**  is generated.
        -   If yes, go to  [2.b](#l032fba0da3884c268b5c5ed218895f6c).
        -   If no, go to  [3](#lfe614e2b28184aea9b211a71a1ae3a90).

    2.  <a name="l032fba0da3884c268b5c5ed218895f6c"></a>In the  **Alarm Details** area of **ALM-12007 Process Fault**, check whether **ServiceName** is **ZooKeeper**.
        -   If yes, go to  [2.c](#l32f0d2faad164150ad572225e7b62a70).
        -   If no, go to  [3](#lfe614e2b28184aea9b211a71a1ae3a90).

    3.  <a name="l32f0d2faad164150ad572225e7b62a70"></a>Rectify the fault by following the steps provided in  **ALM-12007 Process Fault**.
    4.  In the alarm list, check whether alarm  **ALM-16004 Hive Service Unavailable**  is cleared.
        -   If yes, no further action is required.
            -   If no, go to  [3](#lfe614e2b28184aea9b211a71a1ae3a90).


3.  <a name="lfe614e2b28184aea9b211a71a1ae3a90"></a>Check the HDFS service status.
    1.  In the alarm list on MRS Manager, check whether alarm  **ALM-14000 HDFS Service Unavailable**  is generated.
        -   If yes, go to  [3.b](#l849102b75699422f821792bd69ccec73).
        -   If no, go to  [4](#l085a864ba33c4ae683aa78efa1f9994b).

    2.  <a name="l849102b75699422f821792bd69ccec73"></a>Rectify the fault by following the steps provided in  **ALM-14000 HDFS Service Unavailable**.
    3.  In the alarm list, check whether alarm  **ALM-16004 Hive Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l085a864ba33c4ae683aa78efa1f9994b).

4.  <a name="l085a864ba33c4ae683aa78efa1f9994b"></a>Check the Yarn service status.
    1.  In the alarm list on MRS Manager, check whether alarm  **ALM-18000 Yarn Service Unavailable**  is generated.
        -   If yes, go to  [4.b](#l03f7e9572f4d4a6a882904730054eec6).
        -   If no, go to  [4](#l085a864ba33c4ae683aa78efa1f9994b).

    2.  <a name="l03f7e9572f4d4a6a882904730054eec6"></a>Rectify the fault by following the steps provided in  **ALM-18000 Yarn Service Unavailable**.
    3.  In the alarm list, check whether alarm  **ALM-16004 Hive Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l085a864ba33c4ae683aa78efa1f9994b).

5.  Check the DBService service status.
    1.  In the alarm list on MRS Manager, check whether alarm  **ALM-27001 DBService Unavailable**  is generated.
        -   If yes, go to  [5.b](#l62c6dd46628044f1a2c9a5b9b1ba2201).
        -   If no, go to  [6](#l61f2cb5c30c7426d97e76ec9e6451052).

    2.  <a name="l62c6dd46628044f1a2c9a5b9b1ba2201"></a>Rectify the fault by following the steps provided in  [ALM-27001 DBService Unavailable](alm-27001-dbservice-unavailable.md).
    3.  In the alarm list, check whether alarm  **ALM-16004 Hive Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [6](#l61f2cb5c30c7426d97e76ec9e6451052).

6.  <a name="l61f2cb5c30c7426d97e76ec9e6451052"></a>Check the network connection between Hive and ZooKeeper, HDFS, Yarn, and DBService.
    1.  On MRS Manager, choose  **Service**  \>  **Hive**.
    2.  Click  **Instance**.

        The HiveServer instance list is displayed.

    3.  Click  **Host Name** in the row of **HiveServer**.

        The HiveServer host status page is displayed.

    4.  <a name="lf5f8e05d06fc4eed87f66ec612963cbf"></a>Record the IP address under  **Summary**.
    5.  Use the IP address obtained in  [6.d](#lf5f8e05d06fc4eed87f66ec612963cbf)  to log in to the host that runs HiveServer.
    6.  Run the  **ping**  command to check whether the network connection is in the normal state between the host that runs HiveServer and the hosts that run the ZooKeeper, HDFS, Yarn, and DBService services.

        -   If yes, go to  [7](#l0d119779dcc849ff94d54c6a831d5f55).
        -   If no, go to  [6.g](#l5d651ba264b04c0ca646f083bda39a30).

        The methods of obtaining the IP addresses of the hosts that are running ZooKeeper, HDFS, Yarn, and DBService services, as well as the HiveServer IP address, are the same.

    7.  <a name="l5d651ba264b04c0ca646f083bda39a30"></a>Contact public cloud O&M personnel to recover the network.
    8.  In the alarm list, check whether the alarm  **ALM-16004 Hive Service Unavailable**  is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [7](#l0d119779dcc849ff94d54c6a831d5f55).

7.  <a name="l0d119779dcc849ff94d54c6a831d5f55"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sec8020edf7ca4f648d6e4cbe196cb0c1"></a>

N/A

