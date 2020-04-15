# ALM-14002 DataNode Disk Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375630"></a>

## Description<a name="sd1f1b83827794a3d9250f2bc92fce9c4"></a>

The system checks the DataNode disk usage every 30 seconds and compares it with the threshold. This alarm is generated when the value of  **Percentage of DataNode Capacity**  exceeds the threshold and is cleared when the value is less than or equal to the threshold.

## Attribute<a name="s90f629fdfd394ce592bae925cc14b759"></a>

<a name="en-us_topic_0035998722_table11766267"></a>
<table><thead align="left"><tr id="en-us_topic_0035998722_row7304143"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998722_p54764719"><a name="en-us_topic_0035998722_p54764719"></a><a name="en-us_topic_0035998722_p54764719"></a><strong id="a6cec5e49cfdb4caaad71de0828f330a5"><a name="a6cec5e49cfdb4caaad71de0828f330a5"></a><a name="a6cec5e49cfdb4caaad71de0828f330a5"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998722_p6757235"><a name="en-us_topic_0035998722_p6757235"></a><a name="en-us_topic_0035998722_p6757235"></a><strong id="a6662095087b34f04a5f080689edda5e4"><a name="a6662095087b34f04a5f080689edda5e4"></a><a name="a6662095087b34f04a5f080689edda5e4"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998722_p10465156"><a name="en-us_topic_0035998722_p10465156"></a><a name="en-us_topic_0035998722_p10465156"></a><strong id="a7af3e8f387a448929a8332fe57b84cbd"><a name="a7af3e8f387a448929a8332fe57b84cbd"></a><a name="a7af3e8f387a448929a8332fe57b84cbd"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998722_row42371273"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998722_p9521066"><a name="en-us_topic_0035998722_p9521066"></a><a name="en-us_topic_0035998722_p9521066"></a>14002</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998722_p33008913"><a name="en-us_topic_0035998722_p33008913"></a><a name="en-us_topic_0035998722_p33008913"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998722_p56476259"><a name="en-us_topic_0035998722_p56476259"></a><a name="en-us_topic_0035998722_p56476259"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s3cbaf15fd1e04603be50c9b4559e86f5"></a>

<a name="en-us_topic_0035998722_table11174282"></a>
<table><thead align="left"><tr id="en-us_topic_0035998722_row15876907"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998722_p10961125"><a name="en-us_topic_0035998722_p10961125"></a><a name="en-us_topic_0035998722_p10961125"></a><strong id="a19e40f10589a454f9bbd37bb28ecdcaf"><a name="a19e40f10589a454f9bbd37bb28ecdcaf"></a><a name="a19e40f10589a454f9bbd37bb28ecdcaf"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998722_p15435960"><a name="en-us_topic_0035998722_p15435960"></a><a name="en-us_topic_0035998722_p15435960"></a><strong id="aaa4a8d6378d146a9a0ec3858f1caf7f7"><a name="aaa4a8d6378d146a9a0ec3858f1caf7f7"></a><a name="aaa4a8d6378d146a9a0ec3858f1caf7f7"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998722_row42353227"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998722_p8059334"><a name="en-us_topic_0035998722_p8059334"></a><a name="en-us_topic_0035998722_p8059334"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998722_p48826322"><a name="en-us_topic_0035998722_p48826322"></a><a name="en-us_topic_0035998722_p48826322"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998722_row36783718"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998722_p26691149"><a name="en-us_topic_0035998722_p26691149"></a><a name="en-us_topic_0035998722_p26691149"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998722_p14499481"><a name="en-us_topic_0035998722_p14499481"></a><a name="en-us_topic_0035998722_p14499481"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998722_row63386473"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998722_p34030663"><a name="en-us_topic_0035998722_p34030663"></a><a name="en-us_topic_0035998722_p34030663"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998722_p5020285"><a name="en-us_topic_0035998722_p5020285"></a><a name="en-us_topic_0035998722_p5020285"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998722_row45182569"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998722_p35909463"><a name="en-us_topic_0035998722_p35909463"></a><a name="en-us_topic_0035998722_p35909463"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998722_p22985394"><a name="en-us_topic_0035998722_p22985394"></a><a name="en-us_topic_0035998722_p22985394"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s8f35e3f6e26a48f882d59b056c8abbde"></a>

The performance of writing data to HDFS is affected.

## Possible Causes<a name="sc02ea157382f41328f86cc1a25b31f84"></a>

-   The disk space configured for the HDFS cluster is insufficient.
-   Data skew occurs among DataNodes.

## Procedure<a name="s976254185eec450f8428526be933fd94"></a>

1.  Check the cluster disk capacity.
    1.  Log in to MRS Manager. On the  **Alarm**  page, check whether alarm  **ALM-14001 HDFS Disk Usage Exceeds the Threshold**  exists.
        -   If yes, go to  [1.b](#en-us_topic_0035998722_yt2).
        -   If no, go to  [2.a](#en-us_topic_0035998722_li64268160).

    2.  <a name="en-us_topic_0035998722_yt2"></a>Follow the procedures in  **ALM-14001 HDFS Disk Usage Exceeds the Threshold**  to handle the alarm and check whether the alarm is cleared.
        -   If yes, go to  [1.c](#en-us_topic_0035998722_yt3).
        -   If no, go to  [3](#leb265d6ca84e4b8a9a63301c0cae3636).

    3.  <a name="en-us_topic_0035998722_yt3"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#en-us_topic_0035998722_li64268160).

2.  Check the balance status of DataNodes.
    1.  <a name="en-us_topic_0035998722_li64268160"></a>Use the client on the cluster node and run the  **hdfs dfsadmin -report** command to view the value of **DFS Used%**  on the DataNode that generated the alarm. Compare this value with those on other DataNodes and check whether the difference between the values is greater than 10.
        -   If yes, go to  [2.b](#en-us_topic_0035998722_step17).
        -   If no, go to  [3](#leb265d6ca84e4b8a9a63301c0cae3636).

    2.  <a name="en-us_topic_0035998722_step17"></a>If data skew occurs, use the client on the cluster node and run the  **hdfs balancer -threshold 10**  command.
    3.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#leb265d6ca84e4b8a9a63301c0cae3636).

3.  <a name="leb265d6ca84e4b8a9a63301c0cae3636"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s506a7323022a48b0a3c2b32d8411e766"></a>

N/A

