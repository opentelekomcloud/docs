# ALM-14007 HDFS NameNode Memory Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375673"></a>

## Description<a name="en-us_topic_0035998726_section439002"></a>

The system checks the HDFS NameNode memory usage every 30 seconds and compares it with the threshold. This alarm is generated when the HDFS NameNode memory usage exceeds the threshold and is cleared when it is less than or equal to the threshold.

## Attribute<a name="s200beefa1794413c834acdcc8546b8bc"></a>

<a name="en-us_topic_0035998726_table40578897"></a>
<table><thead align="left"><tr id="en-us_topic_0035998726_row57539933"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998726_p30222983"><a name="en-us_topic_0035998726_p30222983"></a><a name="en-us_topic_0035998726_p30222983"></a><strong id="aa763e9bf98784db3833304f62837b100"><a name="aa763e9bf98784db3833304f62837b100"></a><a name="aa763e9bf98784db3833304f62837b100"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998726_p32142578"><a name="en-us_topic_0035998726_p32142578"></a><a name="en-us_topic_0035998726_p32142578"></a><strong id="a77fd39c0d20c4359bd50545277f7d5ba"><a name="a77fd39c0d20c4359bd50545277f7d5ba"></a><a name="a77fd39c0d20c4359bd50545277f7d5ba"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998726_p53412038"><a name="en-us_topic_0035998726_p53412038"></a><a name="en-us_topic_0035998726_p53412038"></a><strong id="a8c8f34bf621341ec8e02acf573fcf775"><a name="a8c8f34bf621341ec8e02acf573fcf775"></a><a name="a8c8f34bf621341ec8e02acf573fcf775"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998726_row31407785"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998726_p61002694"><a name="en-us_topic_0035998726_p61002694"></a><a name="en-us_topic_0035998726_p61002694"></a>14007</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998726_p42271171"><a name="en-us_topic_0035998726_p42271171"></a><a name="en-us_topic_0035998726_p42271171"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998726_p1412808"><a name="en-us_topic_0035998726_p1412808"></a><a name="en-us_topic_0035998726_p1412808"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sba906760d4be4545b7d0ff9ad2d17c35"></a>

<a name="en-us_topic_0035998726_table47328638"></a>
<table><thead align="left"><tr id="en-us_topic_0035998726_row27247099"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998726_p59531373"><a name="en-us_topic_0035998726_p59531373"></a><a name="en-us_topic_0035998726_p59531373"></a><strong id="a9341cb4ad9cf42d2b5ef54d5932bf4c4"><a name="a9341cb4ad9cf42d2b5ef54d5932bf4c4"></a><a name="a9341cb4ad9cf42d2b5ef54d5932bf4c4"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998726_p57311924"><a name="en-us_topic_0035998726_p57311924"></a><a name="en-us_topic_0035998726_p57311924"></a><strong id="a298e506d3fb74a8db09772fefb351067"><a name="a298e506d3fb74a8db09772fefb351067"></a><a name="a298e506d3fb74a8db09772fefb351067"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998726_row11754296"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998726_p12573920"><a name="en-us_topic_0035998726_p12573920"></a><a name="en-us_topic_0035998726_p12573920"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998726_p11854613"><a name="en-us_topic_0035998726_p11854613"></a><a name="en-us_topic_0035998726_p11854613"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998726_row39582655"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998726_p52078514"><a name="en-us_topic_0035998726_p52078514"></a><a name="en-us_topic_0035998726_p52078514"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998726_p57610085"><a name="en-us_topic_0035998726_p57610085"></a><a name="en-us_topic_0035998726_p57610085"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998726_row48728718"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998726_p54712068"><a name="en-us_topic_0035998726_p54712068"></a><a name="en-us_topic_0035998726_p54712068"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998726_p2492560"><a name="en-us_topic_0035998726_p2492560"></a><a name="en-us_topic_0035998726_p2492560"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998726_row22433040"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998726_p5136981"><a name="en-us_topic_0035998726_p5136981"></a><a name="en-us_topic_0035998726_p5136981"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998726_p13442339"><a name="en-us_topic_0035998726_p13442339"></a><a name="en-us_topic_0035998726_p13442339"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s22270f27c09642999794c5a065b399bf"></a>

The HDFS NameNode memory usage is too high, which affects the data read/write performance of the HDFS.

## Possible Causes<a name="s310b1f4c66124d9690ab7d95c1d8677f"></a>

The HDFS NameNode memory is insufficient.

## Procedure<a name="sd8ef22a3660d41fe925f1552b241097e"></a>

1.  Delete unnecessary files.
    1.  Use the client on the cluster node and run the  **hdfs dfs -rm -r** _file or directory_  command to delete unnecessary files.
    2.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l7aed6c1c73cc4abab72badaa3f34750b).

2.  <a name="l7aed6c1c73cc4abab72badaa3f34750b"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sc3ee3c43b23141e7bc241d68b0825d67"></a>

N/A

