# ALM-14003 Number of Lost HDFS Blocks Exceeds the Threshold<a name="EN-US_TOPIC_0125375577"></a>

## Description<a name="s96e9c2103362415b838dc2becef10b40"></a>

The system checks the number of lost blocks every 30 seconds and compares it with the threshold. This alarm is generated when the number of lost blocks exceeds the threshold and is cleared when the number is less than or equal to the threshold.

## Attribute<a name="s405519ff66794c0a8e7e16c32792bc11"></a>

<a name="en-us_topic_0035998723_table47050372"></a>
<table><thead align="left"><tr id="en-us_topic_0035998723_row2854726"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998723_p29906272"><a name="en-us_topic_0035998723_p29906272"></a><a name="en-us_topic_0035998723_p29906272"></a><strong id="en-us_topic_0035998723_b131972125813"><a name="en-us_topic_0035998723_b131972125813"></a><a name="en-us_topic_0035998723_b131972125813"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998723_p6488958"><a name="en-us_topic_0035998723_p6488958"></a><a name="en-us_topic_0035998723_p6488958"></a><strong id="abf9cd167f525408b9bc2096c815bcf56"><a name="abf9cd167f525408b9bc2096c815bcf56"></a><a name="abf9cd167f525408b9bc2096c815bcf56"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998723_p55843593"><a name="en-us_topic_0035998723_p55843593"></a><a name="en-us_topic_0035998723_p55843593"></a><strong id="a18d14436ed804a208ba4fecc39e20a1d"><a name="a18d14436ed804a208ba4fecc39e20a1d"></a><a name="a18d14436ed804a208ba4fecc39e20a1d"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998723_row27037160"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998723_p42526340"><a name="en-us_topic_0035998723_p42526340"></a><a name="en-us_topic_0035998723_p42526340"></a>14003</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998723_p22081476"><a name="en-us_topic_0035998723_p22081476"></a><a name="en-us_topic_0035998723_p22081476"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998723_p43769104"><a name="en-us_topic_0035998723_p43769104"></a><a name="en-us_topic_0035998723_p43769104"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s1194245a1e3a4297b8ae6f82b00d9ad2"></a>

<a name="en-us_topic_0035998723_table55636561"></a>
<table><thead align="left"><tr id="en-us_topic_0035998723_row36019552"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998723_p31902563"><a name="en-us_topic_0035998723_p31902563"></a><a name="en-us_topic_0035998723_p31902563"></a><strong id="ab808ba9d69184bbbb7f565d462cddb4c"><a name="ab808ba9d69184bbbb7f565d462cddb4c"></a><a name="ab808ba9d69184bbbb7f565d462cddb4c"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998723_p33970848"><a name="en-us_topic_0035998723_p33970848"></a><a name="en-us_topic_0035998723_p33970848"></a><strong id="ac719200eaaec4099a48722a8ee128cda"><a name="ac719200eaaec4099a48722a8ee128cda"></a><a name="ac719200eaaec4099a48722a8ee128cda"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998723_row175293"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998723_p14198754"><a name="en-us_topic_0035998723_p14198754"></a><a name="en-us_topic_0035998723_p14198754"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998723_p9248440"><a name="en-us_topic_0035998723_p9248440"></a><a name="en-us_topic_0035998723_p9248440"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998723_row16127101"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998723_p31226782"><a name="en-us_topic_0035998723_p31226782"></a><a name="en-us_topic_0035998723_p31226782"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998723_p46341445"><a name="en-us_topic_0035998723_p46341445"></a><a name="en-us_topic_0035998723_p46341445"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998723_row14419821"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998723_p27154837"><a name="en-us_topic_0035998723_p27154837"></a><a name="en-us_topic_0035998723_p27154837"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998723_p52058165"><a name="en-us_topic_0035998723_p52058165"></a><a name="en-us_topic_0035998723_p52058165"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998723_row65870306"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998723_p33894570"><a name="en-us_topic_0035998723_p33894570"></a><a name="en-us_topic_0035998723_p33894570"></a>NSName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998723_p61105663"><a name="en-us_topic_0035998723_p61105663"></a><a name="en-us_topic_0035998723_p61105663"></a>Specifies the NameService service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998723_row13080057"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998723_p52851724"><a name="en-us_topic_0035998723_p52851724"></a><a name="en-us_topic_0035998723_p52851724"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998723_p53131231"><a name="en-us_topic_0035998723_p53131231"></a><a name="en-us_topic_0035998723_p53131231"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="se4d16722879c4d9f82c6177997cab471"></a>

Data stored in HDFS is lost. HDFS may enter the safe mode and cannot provide write services. Lost block data cannot be restored.

## Possible Causes<a name="sb1b2f702c6724d9997bded442ed564b5"></a>

-   The DataNode instance is abnormal.
-   Data is deleted.

## Procedure<a name="s7f6f03d0a599413ca516999e7450dc10"></a>

1.  Check the DataNode instance.
    1.  On the MRS Manager portal, choose  **Service**  \>  **HDFS**  \>  **Instance**.
    2.  Check whether the status of all DataNode instances is  **Good**.
        -   If yes, go to  [3](#l6bcf4c505ec94e90b2b794529ad6b8fe).
        -   If no, go to  [1.c](#l14b42ab84e0d45f685eb27498f919053).

    3.  <a name="l14b42ab84e0d45f685eb27498f919053"></a>Restart the DataNode instance. Check whether the DataNode instance restarts successfully.
        -   If yes, go to  [2.b](#l6f6dd9fbd92a41088427e97714b3ed3e).
        -   If no, go to  [2.a](#l6857df59edcc43abbec61a9c8ffec2ca).

2.  Delete the damaged file.
    1.  <a name="l6857df59edcc43abbec61a9c8ffec2ca"></a>Use the client on the cluster node. Run the  **hdfs fsck / -delete**  command to delete the lost file. Then rewrite the file and recover the data.
    2.  <a name="l6f6dd9fbd92a41088427e97714b3ed3e"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#l6bcf4c505ec94e90b2b794529ad6b8fe).

3.  <a name="l6bcf4c505ec94e90b2b794529ad6b8fe"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sb61befe1bc6e459f9e3885cc37eefc89"></a>

N/A

