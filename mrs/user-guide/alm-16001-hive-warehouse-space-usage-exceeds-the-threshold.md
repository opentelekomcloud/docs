# ALM-16001 Hive Warehouse Space Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375468"></a>

## Description<a name="s9d96a1c283c84f1da96e254c693fa15a"></a>

The system checks the usage of Hive data warehouse space every 30 seconds. The indicator  **Percentage of HDFS Space Used by Hive to the Available Space**  can be viewed on the Hive service monitoring page. This alarm is generated when the usage of Hive warehouse space exceeds the specified threshold and is cleared when the usage is less than or equal to the threshold.

You can reduce the warehouse space usage by expanding the warehouse capacity or releasing used space.

## Attribute<a name="s50585795cda24636b50685ac4b128bbd"></a>

<a name="en-us_topic_0035998733_table42586845"></a>
<table><thead align="left"><tr id="en-us_topic_0035998733_row65610739"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998733_p12869603"><a name="en-us_topic_0035998733_p12869603"></a><a name="en-us_topic_0035998733_p12869603"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998733_p35804895"><a name="en-us_topic_0035998733_p35804895"></a><a name="en-us_topic_0035998733_p35804895"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998733_p14515408"><a name="en-us_topic_0035998733_p14515408"></a><a name="en-us_topic_0035998733_p14515408"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998733_row34897438"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998733_p8120240"><a name="en-us_topic_0035998733_p8120240"></a><a name="en-us_topic_0035998733_p8120240"></a>16001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998733_p53759727"><a name="en-us_topic_0035998733_p53759727"></a><a name="en-us_topic_0035998733_p53759727"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998733_p59570626"><a name="en-us_topic_0035998733_p59570626"></a><a name="en-us_topic_0035998733_p59570626"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s063694c82bc545938fba15fd9f7882c6"></a>

<a name="en-us_topic_0035998733_table60491410"></a>
<table><thead align="left"><tr id="en-us_topic_0035998733_row20888703"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998733_p14263389"><a name="en-us_topic_0035998733_p14263389"></a><a name="en-us_topic_0035998733_p14263389"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998733_p14483900"><a name="en-us_topic_0035998733_p14483900"></a><a name="en-us_topic_0035998733_p14483900"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998733_row32345284"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998733_p2722332"><a name="en-us_topic_0035998733_p2722332"></a><a name="en-us_topic_0035998733_p2722332"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998733_p19182316"><a name="en-us_topic_0035998733_p19182316"></a><a name="en-us_topic_0035998733_p19182316"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998733_row38423121"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998733_p25265097"><a name="en-us_topic_0035998733_p25265097"></a><a name="en-us_topic_0035998733_p25265097"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998733_p33206990"><a name="en-us_topic_0035998733_p33206990"></a><a name="en-us_topic_0035998733_p33206990"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998733_row30427456"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998733_p48704899"><a name="en-us_topic_0035998733_p48704899"></a><a name="en-us_topic_0035998733_p48704899"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998733_p52782726"><a name="en-us_topic_0035998733_p52782726"></a><a name="en-us_topic_0035998733_p52782726"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998733_row5282487"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998733_p25228285"><a name="en-us_topic_0035998733_p25228285"></a><a name="en-us_topic_0035998733_p25228285"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998733_p30225241"><a name="en-us_topic_0035998733_p30225241"></a><a name="en-us_topic_0035998733_p30225241"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s3e552d0aed9d4b47857dce7942617a97"></a>

The system fails to write data, which causes data loss.

## Possible Causes<a name="s38d00c938dfb454e9c180316f7fc8826"></a>

-   The maximum available capacity of the HDFS for Hive is too small.
-   The system disk space is insufficient.
-   Data nodes break down.

## Procedure<a name="s5ab78f71b4f144d490c33700696ef9bd"></a>

1.  Expand the system configuration.
    1.  Analyze the cluster HDFS capacity usage and increase the maximum available capacity of the HDFS for Hive.

        Log in to MRS Manager, choose  **Service**  \>  **Hive**  \>  **Service Configuration**, and set **Type** to **All**. Increase the value of the **hive.metastore.warehouse.size.percent**  configuration item. Suppose the value of the configuration item is A, total HDFS storage space is B, the threshold is C, and HDFS space used by Hive is D. Adjust the value of the configuration item according to A x B x C \> D. The total HDFS storage space can be viewed on the HDFS monitoring page, and HDFS space used by Hive can be viewed on the Hive service monitoring page.

    2.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#en-us_topic_0035998733_s332).

2.  Expand the system capacity.
    1.  <a name="en-us_topic_0035998733_s332"></a>Add nodes.
    2.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#en-us_topic_0035998733_expand).

3.  Check whether data nodes are in the normal state.
    1.  <a name="en-us_topic_0035998733_expand"></a>Log in to MRS Manager and click  **Alarm**.
    2.  Check whether alarm  **ALM-12006 Node Fault**, **ALM-12007 Process Fault**, or **ALM-14002 DataNode Disk Usage Exceeds the Threshold**  exists.
        -   If yes, go to  [3.c](#l34f26c7ac3604253aba4238e84fe062a).
        -   If no, go to  [4](#l9d13cfc6d3f846e9b573a1769447e7b5).

    3.  <a name="l34f26c7ac3604253aba4238e84fe062a"></a>Follow the procedures in  **ALM-12006 Node Fault**, **ALM-12007 Process Fault**, or **ALM-14002 DataNode Disk Usage Exceeds the Threshold**  to handle the alarm.
    4.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l9d13cfc6d3f846e9b573a1769447e7b5).

4.  <a name="l9d13cfc6d3f846e9b573a1769447e7b5"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s9e972235a89a42389e53b0d2ec45dd78"></a>

N/A

