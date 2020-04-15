# ALM-38001 Insufficient Kafka Disk Space<a name="EN-US_TOPIC_0125375342"></a>

## Description<a name="s595369d2c4b14ad4a473ed853903d229"></a>

The system checks the Kafka disk usage every 60 seconds and compares it with the threshold. This alarm is generated when the disk usage exceeds the threshold.

To modify the threshold, users can choose  **System**  \>  **Threshold Configuration**  on MRS Manager.

This alarm is cleared when the Kafka disk usage is lower than or equal to the threshold.

## Attribute<a name="sfcd5e481c72443f49b27f4778d7c2b63"></a>

<a name="tbc818601a6534c9d92034ec288c9f98e"></a>
<table><thead align="left"><tr id="rf3b6676b22454ef4bb2e08e3a358f86a"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a9b798430324e4e3d9e24a43126b58484"><a name="a9b798430324e4e3d9e24a43126b58484"></a><a name="a9b798430324e4e3d9e24a43126b58484"></a><strong id="a4bfc6539dbce446f905f691163ce63ed"><a name="a4bfc6539dbce446f905f691163ce63ed"></a><a name="a4bfc6539dbce446f905f691163ce63ed"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ab8ed3753e3514bfa8aff6622f7429ff6"><a name="ab8ed3753e3514bfa8aff6622f7429ff6"></a><a name="ab8ed3753e3514bfa8aff6622f7429ff6"></a><strong id="a219dff9fc2da4343acb4fb6dfd4126ec"><a name="a219dff9fc2da4343acb4fb6dfd4126ec"></a><a name="a219dff9fc2da4343acb4fb6dfd4126ec"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a73ba98140ac8456bad0624d67947ee22"><a name="a73ba98140ac8456bad0624d67947ee22"></a><a name="a73ba98140ac8456bad0624d67947ee22"></a><strong id="ad517aae76e704be8a1016f7d53b65696"><a name="ad517aae76e704be8a1016f7d53b65696"></a><a name="ad517aae76e704be8a1016f7d53b65696"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2096438469af46fdafe1a6289cb620b6"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a93bc4f79b80f47b19f5e05ee607fc7f4"><a name="a93bc4f79b80f47b19f5e05ee607fc7f4"></a><a name="a93bc4f79b80f47b19f5e05ee607fc7f4"></a>38001</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="ae8b1557c67f64b7c8b51cc7e04f604be"><a name="ae8b1557c67f64b7c8b51cc7e04f604be"></a><a name="ae8b1557c67f64b7c8b51cc7e04f604be"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a8850739f45ec4b3bb56b75586177edc5"><a name="a8850739f45ec4b3bb56b75586177edc5"></a><a name="a8850739f45ec4b3bb56b75586177edc5"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s95814776d80441afabedbaa1b0608043"></a>

<a name="t4ea093af9f914775b8104ff9bf0ea6ab"></a>
<table><thead align="left"><tr id="rdb79cacbcb954c5291519d2ca3bf1b0f"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="afa6e76e513364104a0b6a0a3f804848f"><a name="afa6e76e513364104a0b6a0a3f804848f"></a><a name="afa6e76e513364104a0b6a0a3f804848f"></a><strong id="a937e0b4db7e54ba88b0e6c6152052209"><a name="a937e0b4db7e54ba88b0e6c6152052209"></a><a name="a937e0b4db7e54ba88b0e6c6152052209"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a6c24b763697e49a6a0de968aa48d1e6c"><a name="a6c24b763697e49a6a0de968aa48d1e6c"></a><a name="a6c24b763697e49a6a0de968aa48d1e6c"></a><strong id="a8e658f4cc30a4f60a6d7f48e5d1bf61c"><a name="a8e658f4cc30a4f60a6d7f48e5d1bf61c"></a><a name="a8e658f4cc30a4f60a6d7f48e5d1bf61c"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2f1282ef79a444a18057f4d2364776e3"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a6df290b880bc4a6cac2263416fcd2dd7"><a name="a6df290b880bc4a6cac2263416fcd2dd7"></a><a name="a6df290b880bc4a6cac2263416fcd2dd7"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9aef2dfcc94c42628a979c1d4f16f41b"><a name="a9aef2dfcc94c42628a979c1d4f16f41b"></a><a name="a9aef2dfcc94c42628a979c1d4f16f41b"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="re3329b3abcbc4802a2e45d8343105f49"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab0d9d47483a54efb98f6df62279b7c76"><a name="ab0d9d47483a54efb98f6df62279b7c76"></a><a name="ab0d9d47483a54efb98f6df62279b7c76"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5c77b5b7b27b4b0e9b8525cacb76e9e2"><a name="a5c77b5b7b27b4b0e9b8525cacb76e9e2"></a><a name="a5c77b5b7b27b4b0e9b8525cacb76e9e2"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rd918be28113249f0ade568eba055f7a9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a362b37c369c2445cb259061f932649f1"><a name="a362b37c369c2445cb259061f932649f1"></a><a name="a362b37c369c2445cb259061f932649f1"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a94289fe775b54bb7b9c22ef70e84b201"><a name="a94289fe775b54bb7b9c22ef70e84b201"></a><a name="a94289fe775b54bb7b9c22ef70e84b201"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r3d9995551e7b4e03a520a897035cb411"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a87b8524abadf4784b2098f151488ab20"><a name="a87b8524abadf4784b2098f151488ab20"></a><a name="a87b8524abadf4784b2098f151488ab20"></a>PartitionName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af4f40d6dee7f4331994a197ee449f957"><a name="af4f40d6dee7f4331994a197ee449f957"></a><a name="af4f40d6dee7f4331994a197ee449f957"></a>Specifies the disk partition where the alarm is generated.</p>
</td>
</tr>
<tr id="r9d022f048db14cc8a1441c451a252602"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ada8fdfee6d4a42308746b889b32a5f7e"><a name="ada8fdfee6d4a42308746b889b32a5f7e"></a><a name="ada8fdfee6d4a42308746b889b32a5f7e"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a8661f3c61f9849daa8ebaf1ad60feed5"><a name="a8661f3c61f9849daa8ebaf1ad60feed5"></a><a name="a8661f3c61f9849daa8ebaf1ad60feed5"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s04a940dafbe7480bab452f4dbd3fb8ea"></a>

Kafka fails to write data to the disks.

## Possible Causes<a name="sb28a0696fe314fcb8fa0df448ebb43dc"></a>

-   The Kafka disk configurations \(such as disk count and disk size\) are insufficient for the data volume.
-   The data retention period is long and historical data occupies a large space.
-   Services are improperly planned. As a result, data is unevenly distributed and some disks are full.

## Procedure<a name="s5a71418a49f443e9a4f604556c90ed91"></a>

1.  Log in to MRS Manager and click  **Alarm**.
2.  <a name="l6c8039483a0f4d7d84197219bedc5695"></a>In the alarm list, click the alarm and view the  **HostName** and **PartitionName** of the alarm in **Location** of **Alarm Details**.
3.  In  **Hosts**, click the host obtained in [2](#l6c8039483a0f4d7d84197219bedc5695).
4.  Check whether the  **Disk** area contains the **PartionName**  of the alarm.
    -   If yes, go to  [5](#l1c6adc842a9943a594e8209064baeda5).
    -   If no, manually clear the alarm and no further action is required.

5.  <a name="l1c6adc842a9943a594e8209064baeda5"></a>In the  **Disk**  area, check whether the usage of the alarmed partition has reached 100%.
    -   If yes, go to  [6](#l2c1404f7fd514210a01e391c7aadd7eb).
    -   If no, go to  [8](#lcf02356974b94364948efd685b6286e8).

6.  <a name="l2c1404f7fd514210a01e391c7aadd7eb"></a>In  **Instance**, choose **Broker \> Instance Configuration**. On the **Instance Configuration** page that is displayed, set **Type** to **All** and query data directory parameter **log.dirs**.
7.  Choose  **Service \> Kafka \> Instance**. On the **Kafka Instance** page that is displayed, stop the Broker instance corresponding to that in [2](#l6c8039483a0f4d7d84197219bedc5695). Then log in to the alarm node and manually delete the data directory queried in [6](#l2c1404f7fd514210a01e391c7aadd7eb). After all subsequent operations are complete, start the Broker instance.
8.  <a name="lcf02356974b94364948efd685b6286e8"></a>Choose  **Service \> Kafka \> Service Configuration**. The **Kafka Configuration**  page is displayed.
9.  Check whether  **disk.adapter.enable** is **true**.
    -   If yes, go to  [11](#l16dc901e65e9434c87485a8789e09687).
    -   If no, change the value to  **true** and go to [10](#l9e847a7d9f6d46eabef5d61ecd8c2109).

10. <a name="l9e847a7d9f6d46eabef5d61ecd8c2109"></a>Check whether the  **adapter.topic.min.retention.hours**  parameter, indicating the minimum data retention period, is properly configured.

    -   If yes, go to  [11](#l16dc901e65e9434c87485a8789e09687).
    -   If no, set it to a proper value and go to  [11](#l16dc901e65e9434c87485a8789e09687).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the retention period cannot be adjusted for certain topics, the topics can be added to  **disk.adapter.topic.blacklist**.  

11. <a name="l16dc901e65e9434c87485a8789e09687"></a>Wait 10 minutes and check whether the disk usage is reduced.
    -   If yes, wait until the alarm is cleared.
    -   If no, go to  [12](#lf58791cd0e634b6d8f6d836e68e33a7c).

12. <a name="lf58791cd0e634b6d8f6d836e68e33a7c"></a>Go to the  **Kafka Topic Monitor**  page and query the data retention period configured for Kafka. Determine whether the retention period needs to be shortened based on service requirements and data volume.
    -   If yes, go to  [13](#lbe835c376c254092b8fcfd7b8b4e9b8d).
    -   If no, go to  [14](#lea1ec096dfce4a8e812e58f6ba22fb2e).

13. <a name="lbe835c376c254092b8fcfd7b8b4e9b8d"></a>Find the topics with great data volumes based on the disk partition obtained in  [2](#l6c8039483a0f4d7d84197219bedc5695). Log in to the Kafka client and manually shorten the data retention period for these topics using the following command:

    **kafka-topics.sh --zookeeper** _ZooKeeper address:24002/kafka_ **--alter --topic** _Topic name_ **--config retention.ms=**_Retention period_

14. <a name="lea1ec096dfce4a8e812e58f6ba22fb2e"></a>Check whether partitions are properly configured for topics. For example, if the number of partitions for a topic with a large data volume is smaller than the number of disks, data may be unevenly distributed to the disks and the usage of some disks will reach the upper limit.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To identify topics with great data volumes, log in to the relevant nodes that are obtained in  [2](#l6c8039483a0f4d7d84197219bedc5695), go to the data directory \(the directory before **log.dirs** in [6](#l2c1404f7fd514210a01e391c7aadd7eb)  is modified\), and check the disk space occupied by the partitions of the topics.  

    -   If the partitions are improperly configured, go to  [15](#lc471287d8ab846679323707fbdf68e1d).
    -   If the partitions are properly configured, go to  [16](#lcece5e40c8744dee9703e45f501588dd).

15. <a name="lc471287d8ab846679323707fbdf68e1d"></a>On the Kafka client, add partitions to the topics.

    **kafka-topics.sh --zookeeper** _ZooKeeper address:24002/kafka_ **--alter --topic** _Topic name_ **--partitions=**_Number of new partitions_

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >It is advised to set the number of new partitions to a multiple of the number of Kafka disks.  
    >This operation may not quickly clear the alarm. Data will be gradually balanced among the disks.  

16. <a name="lcece5e40c8744dee9703e45f501588dd"></a>Check whether the cluster capacity needs to be expanded.
    -   If yes, add nodes to the cluster and go to  [17](#lc512eb7a0b504e21abf9512f38706b4a).
    -   If no, go to  [17](#lc512eb7a0b504e21abf9512f38706b4a).

17. <a name="lc512eb7a0b504e21abf9512f38706b4a"></a>Wait a moment and then check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [18](#lc2eca22648464b3787d6aeb410be13d5).

18. <a name="lc2eca22648464b3787d6aeb410be13d5"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="sf9615f38b6f9446d96549b8ae6cb7115"></a>

N/A

