# ALM-14000 HDFS Service Unavailable<a name="EN-US_TOPIC_0125375502"></a>

## Description<a name="sea8779dfca5d4441a782365311a75ef2"></a>

The system checks the service status of NameService every 30 seconds. This alarm is generated when the HDFS service becomes unavailable because all NameService services are abnormal.

This alarm is cleared when the HDFS service recovers because at least one NameService service is in the normal state.

## Attribute<a name="scae398fde77447ddb81ad2a32f62c4df"></a>

<a name="en-us_topic_0035998720_table21421675"></a>
<table><thead align="left"><tr id="en-us_topic_0035998720_row9119245"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998720_p461342"><a name="en-us_topic_0035998720_p461342"></a><a name="en-us_topic_0035998720_p461342"></a><strong id="ad709e98d5ebb41638f2e1af34c0ae2f1"><a name="ad709e98d5ebb41638f2e1af34c0ae2f1"></a><a name="ad709e98d5ebb41638f2e1af34c0ae2f1"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998720_p37368736"><a name="en-us_topic_0035998720_p37368736"></a><a name="en-us_topic_0035998720_p37368736"></a><strong id="ab7951b0c952541a29a8b5878b242cb55"><a name="ab7951b0c952541a29a8b5878b242cb55"></a><a name="ab7951b0c952541a29a8b5878b242cb55"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998720_p6968762"><a name="en-us_topic_0035998720_p6968762"></a><a name="en-us_topic_0035998720_p6968762"></a><strong id="a7f7db1f8757141dc8ea7d74d4a22d811"><a name="a7f7db1f8757141dc8ea7d74d4a22d811"></a><a name="a7f7db1f8757141dc8ea7d74d4a22d811"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998720_row27598869"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998720_p20915929"><a name="en-us_topic_0035998720_p20915929"></a><a name="en-us_topic_0035998720_p20915929"></a>14000</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998720_p16468652"><a name="en-us_topic_0035998720_p16468652"></a><a name="en-us_topic_0035998720_p16468652"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998720_p58892473"><a name="en-us_topic_0035998720_p58892473"></a><a name="en-us_topic_0035998720_p58892473"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sc430b015aac645729313d711da1f9f5c"></a>

<a name="en-us_topic_0035998720_table5560998"></a>
<table><thead align="left"><tr id="en-us_topic_0035998720_row7715150"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998720_p20947391"><a name="en-us_topic_0035998720_p20947391"></a><a name="en-us_topic_0035998720_p20947391"></a><strong id="a593b5999eda04ecdbbb63a31f33a4de1"><a name="a593b5999eda04ecdbbb63a31f33a4de1"></a><a name="a593b5999eda04ecdbbb63a31f33a4de1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998720_p19017142"><a name="en-us_topic_0035998720_p19017142"></a><a name="en-us_topic_0035998720_p19017142"></a><strong id="aebe2de31ae27440abfd9d6974d37f3dd"><a name="aebe2de31ae27440abfd9d6974d37f3dd"></a><a name="aebe2de31ae27440abfd9d6974d37f3dd"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998720_row63993496"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998720_p16090703"><a name="en-us_topic_0035998720_p16090703"></a><a name="en-us_topic_0035998720_p16090703"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998720_p28278595"><a name="en-us_topic_0035998720_p28278595"></a><a name="en-us_topic_0035998720_p28278595"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998720_row53180767"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998720_p12674872"><a name="en-us_topic_0035998720_p12674872"></a><a name="en-us_topic_0035998720_p12674872"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998720_p20031746"><a name="en-us_topic_0035998720_p20031746"></a><a name="en-us_topic_0035998720_p20031746"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998720_row46067993"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998720_p40519951"><a name="en-us_topic_0035998720_p40519951"></a><a name="en-us_topic_0035998720_p40519951"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998720_p60890569"><a name="en-us_topic_0035998720_p60890569"></a><a name="en-us_topic_0035998720_p60890569"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sc12919226dfb4d1cbededcec71e720ac"></a>

HDFS fails to provide services for HDFS service-based upper-layer components, such as HBase and MapReduce. As a result, users cannot read or write files.

## Possible Causes<a name="s0786174fad7c4771954ac432dbe1462b"></a>

-   The ZooKeeper service is abnormal.
-   All NameService services are abnormal.

## Procedure<a name="s1cfb39b6b5644ca3886658d453f47dcc"></a>

1.  Check the ZooKeeper service status.
    1.  Log in to MRS Manager, choose  **Service**, and check whether the health status of the ZooKeeper service is **Good**.
        -   If yes, go to  [1.b](#l3bc915eef4404b5794e4abb89b170078).
        -   If no, go to  [2.a](#l5f3350e8e3e24dae888ab88ce9c4cf77).

    2.  <a name="l3bc915eef4404b5794e4abb89b170078"></a>Rectify the health status. For details, see  [ALM-13000 ZooKeeper Service Unavailable](alm-13000-zookeeper-service-unavailable.md). Check whether the health status of the ZooKeeper service is  **Good**.
        -   If yes, go to  [1.c](#lb6d2e2c965f0453b8324cc6d1dcea481).
        -   If no, go to  [3](#le45fa8ffa707444495322a27ddf06c4e).

    3.  <a name="lb6d2e2c965f0453b8324cc6d1dcea481"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l5f3350e8e3e24dae888ab88ce9c4cf77).

2.  Handle the NameService service exception alarm.
    1.  <a name="l5f3350e8e3e24dae888ab88ce9c4cf77"></a>Log in to MRS Manager. On the  **Alarm**  page, check whether all NameService services have abnormal alarms.
        -   If yes, go to  [2.b](#l1284af3843234186b04d32be41e696a3).
        -   If no, go to  [3](#le45fa8ffa707444495322a27ddf06c4e).

    2.  <a name="l1284af3843234186b04d32be41e696a3"></a>See  [ALM-14010 NameService Service Is Abnormal](alm-14010-nameservice-service-is-abnormal.md)  to handle abnormal NameService services and check whether each alarm is cleared.
        -   If yes, go to  [2.c](#l4f34848495594e8595ec7c6d5c476945).
        -   If no, go to  [3](#le45fa8ffa707444495322a27ddf06c4e).

    3.  <a name="l4f34848495594e8595ec7c6d5c476945"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#le45fa8ffa707444495322a27ddf06c4e).

3.  <a name="le45fa8ffa707444495322a27ddf06c4e"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s9a10d752c273468f887d3024ef79ca3b"></a>

N/A

