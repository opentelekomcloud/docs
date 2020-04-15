# ALM-13002 ZooKeeper Heap Memory or Direct Memory Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125376115"></a>

## Description<a name="sbee3780c0460425697de224839237d26"></a>

The system checks the memory usage of the ZooKeeper service every 30 seconds. This alarm is generated when the memory usage of a ZooKeeper instance exceeds the threshold \(80% of the maximum memory\).

The alarm is cleared when the memory usage is less than the threshold.

## Attribute<a name="s5e249f893ec745fe9ab05030d72b8a5b"></a>

<a name="en-us_topic_0035998719_table17618432"></a>
<table><thead align="left"><tr id="en-us_topic_0035998719_row61813935"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998719_p40872853"><a name="en-us_topic_0035998719_p40872853"></a><a name="en-us_topic_0035998719_p40872853"></a><strong id="aa6e898ae2a3d48cf8fe7d59c177c9cc2"><a name="aa6e898ae2a3d48cf8fe7d59c177c9cc2"></a><a name="aa6e898ae2a3d48cf8fe7d59c177c9cc2"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998719_p22366803"><a name="en-us_topic_0035998719_p22366803"></a><a name="en-us_topic_0035998719_p22366803"></a><strong id="en-us_topic_0035998719_b290194125113"><a name="en-us_topic_0035998719_b290194125113"></a><a name="en-us_topic_0035998719_b290194125113"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998719_p66880658"><a name="en-us_topic_0035998719_p66880658"></a><a name="en-us_topic_0035998719_p66880658"></a><strong id="a5e5ce6d4ba9e48a6b6c08cc1aa2d30b4"><a name="a5e5ce6d4ba9e48a6b6c08cc1aa2d30b4"></a><a name="a5e5ce6d4ba9e48a6b6c08cc1aa2d30b4"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998719_row48624250"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998719_p46250162"><a name="en-us_topic_0035998719_p46250162"></a><a name="en-us_topic_0035998719_p46250162"></a>13002</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998719_p55275618"><a name="en-us_topic_0035998719_p55275618"></a><a name="en-us_topic_0035998719_p55275618"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998719_p48140083"><a name="en-us_topic_0035998719_p48140083"></a><a name="en-us_topic_0035998719_p48140083"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s13411a84f63a46c4948710d751930cb7"></a>

<a name="en-us_topic_0035998719_table7032652"></a>
<table><thead align="left"><tr id="en-us_topic_0035998719_row1472067"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998719_p52128573"><a name="en-us_topic_0035998719_p52128573"></a><a name="en-us_topic_0035998719_p52128573"></a><strong id="afc3cb70720cb4a74826509fa286c7221"><a name="afc3cb70720cb4a74826509fa286c7221"></a><a name="afc3cb70720cb4a74826509fa286c7221"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998719_p61664867"><a name="en-us_topic_0035998719_p61664867"></a><a name="en-us_topic_0035998719_p61664867"></a><strong id="a5b11450047d443478faf4fe66c349022"><a name="a5b11450047d443478faf4fe66c349022"></a><a name="a5b11450047d443478faf4fe66c349022"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998719_row28798367"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998719_p50966358"><a name="en-us_topic_0035998719_p50966358"></a><a name="en-us_topic_0035998719_p50966358"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998719_p34634354"><a name="en-us_topic_0035998719_p34634354"></a><a name="en-us_topic_0035998719_p34634354"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998719_row43273738"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998719_p15511864"><a name="en-us_topic_0035998719_p15511864"></a><a name="en-us_topic_0035998719_p15511864"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998719_p48501438"><a name="en-us_topic_0035998719_p48501438"></a><a name="en-us_topic_0035998719_p48501438"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998719_row33859762"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998719_p58286192"><a name="en-us_topic_0035998719_p58286192"></a><a name="en-us_topic_0035998719_p58286192"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998719_p23561115"><a name="en-us_topic_0035998719_p23561115"></a><a name="en-us_topic_0035998719_p23561115"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998719_row10723444"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998719_p63292653"><a name="en-us_topic_0035998719_p63292653"></a><a name="en-us_topic_0035998719_p63292653"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998719_p26431238"><a name="en-us_topic_0035998719_p26431238"></a><a name="en-us_topic_0035998719_p26431238"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s8855649aa30d4397bbe5e522bc164028"></a>

If the available memory for the ZooKeeper service is insufficient, a memory overflow occurs and the service breaks down.

## Possible Causes<a name="s7bcd0affebc64a0fa4cc6a861845db38"></a>

-   The memory usage of the ZooKeeper instance on the node is overused
-   The memory is improperly allocated.

## Procedure<a name="s64fd24dfa55d4f4ba44296c11e13d9d6"></a>

1.  Check the memory usage.
    1.  On the MRS Manager portal, choose  **Alarm**  \>  **ALM-13002 ZooKeeper Memory Usage Exceeds the Threshold**  \>  **Location**. Check the IP address of the instance that generated the alarm.
    2.  On the MRS Manager portal, choose  **Service**  \>  **ZooKeeper**  \>  **Instance**  \>  **quorumpeer\(the IP address checked\)**  \>  **Customize**  \>  **Heap and Direct Memory of ZooKeeper**. Check the heap usage.
    3.  Check whether the used heap memory of ZooKeeper reaches 80% of the maximum heap memory specified for ZooKeeper.
        -   If yes, go to  [1.d](#l58315eba47bf48a3a0706c3601f01c41).
        -   If no, go to  [1.f](#l8dbc11497799425680b0d2de50bfcad4).

    4.  <a name="l58315eba47bf48a3a0706c3601f01c41"></a>On the MRS Manager portal, choose  **Service**  \>  **ZooKeeper**  \>  **Service Configuration**  \>  **All**  \>  **quorumpeer**  \>  **System**. Increase the value of **-Xmx** in **GC\_OPTS**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [1.f](#l8dbc11497799425680b0d2de50bfcad4).

    6.  <a name="l8dbc11497799425680b0d2de50bfcad4"></a>On the MRS Manager portal, choose  **Service**  \>  **ZooKeeper**  \>  **Instance**  \>  **quorumpeer\(the IP address checked\)**  \>  **Customize**  \>  **Heap and Direct Memory of ZooKeeper**. Check the direct buffer memory usage.
    7.  Check whether the used direct buffer memory of ZooKeeper reaches 80% of the maximum direct buffer memory specified for ZooKeeper.
        -   If yes, go to  [1.h](#le4128153359348b9a63b5b8a7431c7cf).
        -   If no, go to  [2](#la5054032195349e5b787ac977e4dea2a).

    8.  <a name="le4128153359348b9a63b5b8a7431c7cf"></a>On the MRS Manager portal, choose  **Service**  \>  **ZooKeeper**  \>  **Service Configuration**  \>  **All**  \>  **quorumpeer**  \>  **System**.

        Increase the value of  **-XX:MaxDirectMemorySize** in **GC\_OPTS**  as required.

    9.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#la5054032195349e5b787ac977e4dea2a).

2.  <a name="la5054032195349e5b787ac977e4dea2a"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s318d13a58df84cbb876e97ec0493fe3e"></a>

N/A

