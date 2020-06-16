# ALM-14004 Number of Damaged HDFS Blocks Exceeds the Threshold<a name="EN-US_TOPIC_0125375760"></a>

## Description<a name="sb99dd62dcb954b7a8b97efa511d12ea0"></a>

The system checks the number of damaged blocks every 30 seconds and compares it with the threshold. This alarm is generated when the number of damaged blocks exceeds the threshold and is cleared when the number is less than or equal to the threshold.

## Attribute<a name="s730a800bc15a4abda5b9e71d734a1c3f"></a>

<a name="en-us_topic_0035998724_table32368095"></a>
<table><thead align="left"><tr id="en-us_topic_0035998724_row53402119"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998724_p30604389"><a name="en-us_topic_0035998724_p30604389"></a><a name="en-us_topic_0035998724_p30604389"></a><strong id="a8c20efcba569440ca2924180256c1c08"><a name="a8c20efcba569440ca2924180256c1c08"></a><a name="a8c20efcba569440ca2924180256c1c08"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998724_p63036484"><a name="en-us_topic_0035998724_p63036484"></a><a name="en-us_topic_0035998724_p63036484"></a><strong id="a9fc7c822998c4f5896977496a2a09129"><a name="a9fc7c822998c4f5896977496a2a09129"></a><a name="a9fc7c822998c4f5896977496a2a09129"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998724_p5681612"><a name="en-us_topic_0035998724_p5681612"></a><a name="en-us_topic_0035998724_p5681612"></a><strong id="a216dd7ebd8ea4ad8860ac9046fce99b8"><a name="a216dd7ebd8ea4ad8860ac9046fce99b8"></a><a name="a216dd7ebd8ea4ad8860ac9046fce99b8"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998724_row57557412"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998724_p31638772"><a name="en-us_topic_0035998724_p31638772"></a><a name="en-us_topic_0035998724_p31638772"></a>14004</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998724_p12603749"><a name="en-us_topic_0035998724_p12603749"></a><a name="en-us_topic_0035998724_p12603749"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998724_p14270750"><a name="en-us_topic_0035998724_p14270750"></a><a name="en-us_topic_0035998724_p14270750"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s11ed7e7b9cda4894aedc8c845e18829d"></a>

<a name="en-us_topic_0035998724_table15080136"></a>
<table><thead align="left"><tr id="en-us_topic_0035998724_row66592127"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998724_p25253189"><a name="en-us_topic_0035998724_p25253189"></a><a name="en-us_topic_0035998724_p25253189"></a><strong id="a0fd808a3449d488facbf03ba71581503"><a name="a0fd808a3449d488facbf03ba71581503"></a><a name="a0fd808a3449d488facbf03ba71581503"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998724_p32242465"><a name="en-us_topic_0035998724_p32242465"></a><a name="en-us_topic_0035998724_p32242465"></a><strong id="ab44b40f2119d4949b7c4db32fe9a9e77"><a name="ab44b40f2119d4949b7c4db32fe9a9e77"></a><a name="ab44b40f2119d4949b7c4db32fe9a9e77"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998724_row61502840"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998724_p15674164"><a name="en-us_topic_0035998724_p15674164"></a><a name="en-us_topic_0035998724_p15674164"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998724_p61647805"><a name="en-us_topic_0035998724_p61647805"></a><a name="en-us_topic_0035998724_p61647805"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998724_row17959338"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998724_p45420240"><a name="en-us_topic_0035998724_p45420240"></a><a name="en-us_topic_0035998724_p45420240"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998724_p55160823"><a name="en-us_topic_0035998724_p55160823"></a><a name="en-us_topic_0035998724_p55160823"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998724_row26685362"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998724_p14030717"><a name="en-us_topic_0035998724_p14030717"></a><a name="en-us_topic_0035998724_p14030717"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998724_p62746268"><a name="en-us_topic_0035998724_p62746268"></a><a name="en-us_topic_0035998724_p62746268"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998724_row27845503"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998724_p40893240"><a name="en-us_topic_0035998724_p40893240"></a><a name="en-us_topic_0035998724_p40893240"></a>NSName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998724_p24018105"><a name="en-us_topic_0035998724_p24018105"></a><a name="en-us_topic_0035998724_p24018105"></a>Specifies the NameService service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998724_row14836356"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998724_p60894213"><a name="en-us_topic_0035998724_p60894213"></a><a name="en-us_topic_0035998724_p60894213"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998724_p33484259"><a name="en-us_topic_0035998724_p33484259"></a><a name="en-us_topic_0035998724_p33484259"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sc741354815de4a7bbc89926aa68e0eca"></a>

Data is damaged and HDFS fails to read files.

## Possible Causes<a name="se6c224737180497aaa7fe2b97c99a9aa"></a>

-   The DataNode instance is abnormal.
-   Data verification information is damaged.

## Procedure<a name="s2c7ca743c44f4258aefc3da002b13fa3"></a>

Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s282c369c582447d394ad537902156360"></a>

N/A

