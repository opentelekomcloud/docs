# ALM-14006 Number of HDFS Files Exceeds the Threshold<a name="EN-US_TOPIC_0125375297"></a>

## Description<a name="s268d859943c24666ace929064c33a27e"></a>

The system checks the number of HDFS files every 30 seconds and compares it with the threshold. This alarm is generated when the number of HDFS files exceeds the threshold and is cleared when the number is less than or equal to the threshold.

## Attribute<a name="sfa025ca3e8ae46f08a0086f04bb970a8"></a>

<a name="en-us_topic_0035998725_table60344938"></a>
<table><thead align="left"><tr id="en-us_topic_0035998725_row59011071"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998725_p15167431"><a name="en-us_topic_0035998725_p15167431"></a><a name="en-us_topic_0035998725_p15167431"></a><strong id="a7c898b2c312b4b8b98aba74079bd6e39"><a name="a7c898b2c312b4b8b98aba74079bd6e39"></a><a name="a7c898b2c312b4b8b98aba74079bd6e39"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998725_p20602375"><a name="en-us_topic_0035998725_p20602375"></a><a name="en-us_topic_0035998725_p20602375"></a><strong id="aea5d6969ce06476fa74eb3f5a18ea706"><a name="aea5d6969ce06476fa74eb3f5a18ea706"></a><a name="aea5d6969ce06476fa74eb3f5a18ea706"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998725_p58179688"><a name="en-us_topic_0035998725_p58179688"></a><a name="en-us_topic_0035998725_p58179688"></a><strong id="a28aad6a19bc94a6dbe8a0e72714e079c"><a name="a28aad6a19bc94a6dbe8a0e72714e079c"></a><a name="a28aad6a19bc94a6dbe8a0e72714e079c"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998725_row14934289"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998725_p1717931"><a name="en-us_topic_0035998725_p1717931"></a><a name="en-us_topic_0035998725_p1717931"></a>14006</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998725_p4934750"><a name="en-us_topic_0035998725_p4934750"></a><a name="en-us_topic_0035998725_p4934750"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998725_p64170449"><a name="en-us_topic_0035998725_p64170449"></a><a name="en-us_topic_0035998725_p64170449"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s8f0a5a4013c3453d9d6dd9494a9fdffe"></a>

<a name="en-us_topic_0035998725_table30423852"></a>
<table><thead align="left"><tr id="en-us_topic_0035998725_row60888739"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998725_p33040847"><a name="en-us_topic_0035998725_p33040847"></a><a name="en-us_topic_0035998725_p33040847"></a><strong id="a81db3a389dea4325b65a3e45af19cb19"><a name="a81db3a389dea4325b65a3e45af19cb19"></a><a name="a81db3a389dea4325b65a3e45af19cb19"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998725_p59062984"><a name="en-us_topic_0035998725_p59062984"></a><a name="en-us_topic_0035998725_p59062984"></a><strong id="abed70426a51744b598f23a8ece2bf1ac"><a name="abed70426a51744b598f23a8ece2bf1ac"></a><a name="abed70426a51744b598f23a8ece2bf1ac"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998725_row19372405"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998725_p25660991"><a name="en-us_topic_0035998725_p25660991"></a><a name="en-us_topic_0035998725_p25660991"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998725_p65274381"><a name="en-us_topic_0035998725_p65274381"></a><a name="en-us_topic_0035998725_p65274381"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998725_row50598521"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998725_p4839561"><a name="en-us_topic_0035998725_p4839561"></a><a name="en-us_topic_0035998725_p4839561"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998725_p56460178"><a name="en-us_topic_0035998725_p56460178"></a><a name="en-us_topic_0035998725_p56460178"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998725_row38379555"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998725_p21736211"><a name="en-us_topic_0035998725_p21736211"></a><a name="en-us_topic_0035998725_p21736211"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998725_p15802639"><a name="en-us_topic_0035998725_p15802639"></a><a name="en-us_topic_0035998725_p15802639"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998725_row8006030"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998725_p44508680"><a name="en-us_topic_0035998725_p44508680"></a><a name="en-us_topic_0035998725_p44508680"></a>NSName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998725_p48433347"><a name="en-us_topic_0035998725_p48433347"></a><a name="en-us_topic_0035998725_p48433347"></a>Specifies the NameService service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998725_row33246944"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998725_p8647967"><a name="en-us_topic_0035998725_p8647967"></a><a name="en-us_topic_0035998725_p8647967"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998725_p29396722"><a name="en-us_topic_0035998725_p29396722"></a><a name="en-us_topic_0035998725_p29396722"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s9ebdda70baca44b8b1ce702862faf900"></a>

Disk storage space is insufficient, which may result in data import failure. The performance of the HDFS system is affected.

## Possible Causes<a name="s6f0e3990608e40d98b1d153b5e5ae6ef"></a>

The number of HDFS files exceeds the threshold.

## Procedure<a name="s240b001c1ee04824add8fc644c9de094"></a>

1.  Check whether unnecessary files exist in the system.
    1.  Use the client on the cluster node and run the  **hdfs dfs -ls** _file or directory_  command to check whether the files in the directory can be deleted.
        -   If yes, go to  [1.b](#lcede964433fb4561ac6647f01c38a061).
        -   If no, go to  [2.a](#en-us_topic_0035998725_yt16).

    2.  <a name="lcede964433fb4561ac6647f01c38a061"></a>Run the  **hdfs dfs -rm -r** _file or directory_  command. Delete unnecessary files, wait 5 minutes, and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#en-us_topic_0035998725_yt16).

2.  Check the number of files in the system.
    1.  <a name="en-us_topic_0035998725_yt16"></a>On the MRS Manager portal, choose  **System**  \>  **Configure Alarm Threshold**.
    2.  In the navigation tree on the left, choose  **Service**  \>  **HDFS**  \>  **HDFS File**  \>  **Total Number of Files**.
    3.  In the right pane, modify the threshold in the rule based on the number of current HDFS files.

        To check the number of HDFS files, choose  **Service**  \>  **HDFS**, click **Customize** in the **Real-Time Statistics**  area on the right, and select the **HDFS File**  monitoring item.

    4.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#lf347193308534d87ba773348b1181153).

3.  <a name="lf347193308534d87ba773348b1181153"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

        Telephone:

        Germany: 0800 330 44 44

        International: +800 44556600



## Related Information<a name="s914e2908522143f484e053d5160de1e0"></a>

N/A

