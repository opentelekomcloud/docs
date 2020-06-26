# ALM-14012 HDFS JournalNode Data Is Not Synchronized<a name="EN-US_TOPIC_0125375409"></a>

## Description<a name="se69e5a1639ac449a87443dc99ca491c3"></a>

On the active NameNode, the system checks data synchronization on all JournalNodes in the cluster every 5 minutes. This alarm is generated when data on a JournalNode is not synchronized with that on other JournalNodes.

This alarm is cleared in 5 minutes after data on the JournalNodes is synchronized.

## Attribute<a name="s615a86bdd3a74f4290d0efd40fb59ac6"></a>

<a name="en-us_topic_0035998731_table56187107"></a>
<table><thead align="left"><tr id="en-us_topic_0035998731_row43395070"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998731_p25339754"><a name="en-us_topic_0035998731_p25339754"></a><a name="en-us_topic_0035998731_p25339754"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998731_p39254219"><a name="en-us_topic_0035998731_p39254219"></a><a name="en-us_topic_0035998731_p39254219"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998731_p25475209"><a name="en-us_topic_0035998731_p25475209"></a><a name="en-us_topic_0035998731_p25475209"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998731_row50226059"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998731_p41779002"><a name="en-us_topic_0035998731_p41779002"></a><a name="en-us_topic_0035998731_p41779002"></a>14012</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998731_p28655997"><a name="en-us_topic_0035998731_p28655997"></a><a name="en-us_topic_0035998731_p28655997"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998731_p39434429"><a name="en-us_topic_0035998731_p39434429"></a><a name="en-us_topic_0035998731_p39434429"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sf6435fc40b494916b4c6e2c4894d3326"></a>

<a name="en-us_topic_0035998731_table40072161"></a>
<table><thead align="left"><tr id="en-us_topic_0035998731_row29623216"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998731_p50670335"><a name="en-us_topic_0035998731_p50670335"></a><a name="en-us_topic_0035998731_p50670335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998731_p10656503"><a name="en-us_topic_0035998731_p10656503"></a><a name="en-us_topic_0035998731_p10656503"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998731_row57870399"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998731_p56990719"><a name="en-us_topic_0035998731_p56990719"></a><a name="en-us_topic_0035998731_p56990719"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998731_p52845536"><a name="en-us_topic_0035998731_p52845536"></a><a name="en-us_topic_0035998731_p52845536"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998731_row5847780"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998731_p3908185"><a name="en-us_topic_0035998731_p3908185"></a><a name="en-us_topic_0035998731_p3908185"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998731_p48127554"><a name="en-us_topic_0035998731_p48127554"></a><a name="en-us_topic_0035998731_p48127554"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998731_row30494806"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998731_p54160201"><a name="en-us_topic_0035998731_p54160201"></a><a name="en-us_topic_0035998731_p54160201"></a>IP</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998731_p24900132"><a name="en-us_topic_0035998731_p24900132"></a><a name="en-us_topic_0035998731_p24900132"></a>Specifies the service IP address of the JournalNode instance for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s33269296d55247c4bab120373420f012"></a>

If data on more than half of the JournalNodes is not synchronized, the NameNode cannot work correctly, making the HDFS service unavailable.

## Possible Causes<a name="sa66483ad03934e1796481864b88d67bf"></a>

-   The JournalNode instance has not been started or has been stopped.
-   The JournalNode instance is working incorrectly.
-   The network of the JournalNode is unreachable.

## Procedure<a name="s89ca1bad718c4d73ad326d39aead9a13"></a>

1.  Check whether the JournalNode instance has been started.
    1.  Log in to MRS Manager and click  **Alarm**. In the alarm list, click the alarm.
    2.  In the  **Alarm Details** area, check **Location**  and obtain the IP address of the JournalNode that generated the alarm.
    3.  Choose  **Service**  \>  **HDFS**  \>  **Instance**. In the instance list, click the JournalNode that generated the alarm and check whether  **Operating Status** of the node is **Started**.
        -   If yes, go to  [2.a](#l72d49b4ee25844fbaafaa85cdc355b21).
        -   If no, go to  [1.d](#l37e4e3af71d746acae7bdcaa1ec6778f).

    4.  <a name="l37e4e3af71d746acae7bdcaa1ec6778f"></a>Select the JournalNode instance and choose  **More**  \>  **Start Instance**  to start it.
    5.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l6a38be5e81554664b26a81520b57d164).

2.  Check whether the JournalNode instance is working correctly.
    1.  <a name="l72d49b4ee25844fbaafaa85cdc355b21"></a>Check whether  **Health Status** of the JournalNode instance is **Good**.
        -   If yes, go to  [3.a](#la0a6981de2b84e43857dfd8ba4b84897).
        -   If no, go to  [2.b](#en-us_topic_0035998731_s7).

    2.  <a name="en-us_topic_0035998731_s7"></a>Select the JournalNode instance and choose  **More**  \>  **Start Instance**  to start it.
    3.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l6a38be5e81554664b26a81520b57d164).

3.  Check whether the network of the JournalNode is reachable.
    1.  <a name="la0a6981de2b84e43857dfd8ba4b84897"></a>On the MRS Manager portal, choose  **Service**  \>  **HDFS**  \>  **Instance**  to check the service IP address of the active NameNode.
    2.  Log in to the active NameNode.
    3.  Run the  **ping** _Service IP_ _address of_ _the JournalNode_  command to check whether either a timeout occurs or the network between the active NameNode and the JournalNode is unreachable.
        -   If yes, go to  [3.d](#l33b1e8f3c1e248219af15f7aef721de1).
        -   If no, go to  [4](#l6a38be5e81554664b26a81520b57d164).

    4.  <a name="l33b1e8f3c1e248219af15f7aef721de1"></a>Contact public cloud O&M personnel to rectify the network fault. Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l6a38be5e81554664b26a81520b57d164).

4.  <a name="l6a38be5e81554664b26a81520b57d164"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s79e001738f3e40999b5e5ca8217b83ca"></a>

N/A

