# ALM-19000 HBase Service Unavailable<a name="EN-US_TOPIC_0125375547"></a>

## Description<a name="sc72d81843bec436dbb2886d13a47e571"></a>

The alarm module checks the HBase service status every 30 seconds. This alarm is generated when the HBase service is unavailable and is cleared when the HBase service recovers.

## Attribute<a name="sdec1053a085940e283a1b3fd9ef79e6c"></a>

<a name="en-us_topic_0035998740_table57434139"></a>
<table><thead align="left"><tr id="en-us_topic_0035998740_row461342"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998740_p37368736"><a name="en-us_topic_0035998740_p37368736"></a><a name="en-us_topic_0035998740_p37368736"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998740_p6968762"><a name="en-us_topic_0035998740_p6968762"></a><a name="en-us_topic_0035998740_p6968762"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998740_p27598869"><a name="en-us_topic_0035998740_p27598869"></a><a name="en-us_topic_0035998740_p27598869"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998740_row20915929"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998740_p16468652"><a name="en-us_topic_0035998740_p16468652"></a><a name="en-us_topic_0035998740_p16468652"></a>19000</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998740_p58892473"><a name="en-us_topic_0035998740_p58892473"></a><a name="en-us_topic_0035998740_p58892473"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998740_p5560998"><a name="en-us_topic_0035998740_p5560998"></a><a name="en-us_topic_0035998740_p5560998"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sc122ac2693094233a8e5f70857355dbc"></a>

<a name="en-us_topic_0035998740_table47787675"></a>
<table><thead align="left"><tr id="en-us_topic_0035998740_row20947391"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998740_p19017142"><a name="en-us_topic_0035998740_p19017142"></a><a name="en-us_topic_0035998740_p19017142"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998740_p63993496"><a name="en-us_topic_0035998740_p63993496"></a><a name="en-us_topic_0035998740_p63993496"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998740_row16090703"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998740_p28278595"><a name="en-us_topic_0035998740_p28278595"></a><a name="en-us_topic_0035998740_p28278595"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998740_p8864859"><a name="en-us_topic_0035998740_p8864859"></a><a name="en-us_topic_0035998740_p8864859"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998740_row12674872"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998740_p20031746"><a name="en-us_topic_0035998740_p20031746"></a><a name="en-us_topic_0035998740_p20031746"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998740_p11958757"><a name="en-us_topic_0035998740_p11958757"></a><a name="en-us_topic_0035998740_p11958757"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998740_row40519951"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998740_p60890569"><a name="en-us_topic_0035998740_p60890569"></a><a name="en-us_topic_0035998740_p60890569"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998740_p33189039"><a name="en-us_topic_0035998740_p33189039"></a><a name="en-us_topic_0035998740_p33189039"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s0c67ed091d4542dab2fe5d4f6c3ecb00"></a>

Operations such as reading or writing data and creating tables cannot be performed.

## Possible Causes<a name="s6b1a65c4d25948cfaa20c84d38b2cc45"></a>

-   The ZooKeeper service is abnormal.
-   The HDFS service is abnormal.
-   The HBase service is abnormal.
-   The network is abnormal.

## Procedure<a name="s27ef7880fec444fdbbd4f80981f445da"></a>

1.  Check the ZooKeeper service status.
    1.  In the service list on MRS Manager, check whether the health status of ZooKeeper is  **Good**.
        -   If yes, go to  [2.a](#ldff8b5b6354f47708698e34df0e16312).
        -   If no, go to  [1.b](#l91de50db130a4295adeae906d69d2bdb).

    2.  <a name="l91de50db130a4295adeae906d69d2bdb"></a>In the alarm list, check whether alarm  **ALM-13000 ZooKeeper Service Unavailable**  exists.
        -   If yes, go to  [1.c](#lb546abf6e89a4fd29180bdda0ea6a3cc).
        -   If no, go to  [2.a](#ldff8b5b6354f47708698e34df0e16312).

    3.  <a name="lb546abf6e89a4fd29180bdda0ea6a3cc"></a>Rectify the fault by following the steps provided in  **ALM-13000 ZooKeeper Service Unavailable**.
    4.  Wait several minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#ldff8b5b6354f47708698e34df0e16312).

2.  Check the HDFS service status.
    1.  <a name="ldff8b5b6354f47708698e34df0e16312"></a>In the alarm list, check whether alarm  **ALM-14000 HDFS Service Unavailable**  exists.
        -   If yes, go to  [2.b](#en-us_topic_0035998740_alm).
        -   If no, go to  [3](#ld370a3380623480a9c1127a51f69f7a4).

    2.  <a name="en-us_topic_0035998740_alm"></a>Rectify the fault by following the steps provided in  **ALM-14000 HDFS Service Unavailable**.
    3.  Wait several minutes and check whether the alarm is cleared.

3.  <a name="ld370a3380623480a9c1127a51f69f7a4"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sd0756c1e5a284a5995215bf65a6fbc35"></a>

N/A

