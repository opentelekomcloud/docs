# Creating a Tag for a VPN Resource<a name="en_topic_0093011486"></a>

## **Function**<a name="en-us_topic_0103470566_section6739112719406"></a>

This interface is used to create a tag for a VPN resource.

## URI<a name="en-us_topic_0103470566_section197391227124012"></a>

POST /v2.0/\{project\_id\}/ipsec-site-connections/\{resource\_id\}/tags

>![](/images/icon-note.gif) **NOTE:**   
>In the URI,  **project\_id**  indicates the project ID, and  **resource\_id**  indicates the target resource ID.  

## Request Message<a name="en-us_topic_0103470566_section074912764017"></a>

[Table 1](#en-us_topic_0103470566_table14751112719406)  describes the request parameters.

**Table  1**  Request parameters

<a name="en-us_topic_0103470566_table14751112719406"></a>
<table><thead align="left"><tr id="en-us_topic_0103470566_row1085714277402"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0103470566_p48571827164012"><a name="en-us_topic_0103470566_p48571827164012"></a><a name="en-us_topic_0103470566_p48571827164012"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24%" id="mcps1.2.5.1.2"><p id="en-us_topic_0103470566_p685711273400"><a name="en-us_topic_0103470566_p685711273400"></a><a name="en-us_topic_0103470566_p685711273400"></a><strong id="b84235270610412"><a name="b84235270610412"></a><a name="b84235270610412"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.3"><p id="en-us_topic_0103470566_p118573278400"><a name="en-us_topic_0103470566_p118573278400"></a><a name="en-us_topic_0103470566_p118573278400"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.4"><p id="en-us_topic_0103470566_p198576274405"><a name="en-us_topic_0103470566_p198576274405"></a><a name="en-us_topic_0103470566_p198576274405"></a><strong id="b842352706151625"><a name="b842352706151625"></a><a name="b842352706151625"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0103470566_row1985711272400"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0103470566_p9857152794012"><a name="en-us_topic_0103470566_p9857152794012"></a><a name="en-us_topic_0103470566_p9857152794012"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0103470566_p6857172715402"><a name="en-us_topic_0103470566_p6857172715402"></a><a name="en-us_topic_0103470566_p6857172715402"></a>List&lt;resource_tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0103470566_p198573277400"><a name="en-us_topic_0103470566_p198573277400"></a><a name="en-us_topic_0103470566_p198573277400"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0103470566_p188571327104019"><a name="en-us_topic_0103470566_p188571327104019"></a><a name="en-us_topic_0103470566_p188571327104019"></a>Specifies the tag.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **resource\_tag**

<a name="table13242848193719"></a>
<table><thead align="left"><tr id="row13343144812379"><th class="cellrowborder" valign="top" width="14.649999999999999%" id="mcps1.1.5.1.1"><p id="p15343174853715"><a name="p15343174853715"></a><a name="p15343174853715"></a><strong id="b84235270617246"><a name="b84235270617246"></a><a name="b84235270617246"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.369999999999997%" id="mcps1.1.5.1.2"><p id="p15643121154020"><a name="p15643121154020"></a><a name="p15643121154020"></a><strong id="b341863433"><a name="b341863433"></a><a name="b341863433"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.990000000000002%" id="mcps1.1.5.1.3"><p id="p13431648163716"><a name="p13431648163716"></a><a name="p13431648163716"></a><strong id="b1385670838"><a name="b1385670838"></a><a name="b1385670838"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.99%" id="mcps1.1.5.1.4"><p id="p11344748183719"><a name="p11344748183719"></a><a name="p11344748183719"></a><strong id="b1398390940"><a name="b1398390940"></a><a name="b1398390940"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row103449487379"><td class="cellrowborder" valign="top" width="14.649999999999999%" headers="mcps1.1.5.1.1 "><p id="p183469482373"><a name="p183469482373"></a><a name="p183469482373"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.1.5.1.2 "><p id="p5569213105916"><a name="p5569213105916"></a><a name="p5569213105916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.990000000000002%" headers="mcps1.1.5.1.3 "><p id="p1434684863710"><a name="p1434684863710"></a><a name="p1434684863710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.99%" headers="mcps1.1.5.1.4 "><p id="p11346184819376"><a name="p11346184819376"></a><a name="p11346184819376"></a>Specifies the tag key.</p>
<p id="p154442255810"><a name="p154442255810"></a><a name="p154442255810"></a>The parameter constraints are as follows:</p>
<a name="ul17240515195820"></a><a name="ul17240515195820"></a><ul id="ul17240515195820"><li>Must be unique for a resource.</li><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul19240161517582"></a><a name="ul19240161517582"></a><ul id="ul19240161517582"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
<tr id="row2346548163714"><td class="cellrowborder" valign="top" width="14.649999999999999%" headers="mcps1.1.5.1.1 "><p id="p1134624816377"><a name="p1134624816377"></a><a name="p1134624816377"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.1.5.1.2 "><p id="p183571615913"><a name="p183571615913"></a><a name="p183571615913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.990000000000002%" headers="mcps1.1.5.1.3 "><p id="p234619483371"><a name="p234619483371"></a><a name="p234619483371"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.99%" headers="mcps1.1.5.1.4 "><p id="p534634813374"><a name="p534634813374"></a><a name="p534634813374"></a>Specifies the tag value.</p>
<p id="p193981434195813"><a name="p193981434195813"></a><a name="p193981434195813"></a>The parameter constraints are as follows:</p>
<a name="ul186515095815"></a><a name="ul186515095815"></a><ul id="ul186515095815"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul1086516509585"></a><a name="ul1086516509585"></a><ul id="ul1086516509585"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="en-us_topic_0103470566_section775782711402"></a>

None

## Example<a name="en-us_topic_0103470566_section775882720405"></a>

-   Example Request

```
POST /v2.0/{project_id}/ipsec-site-connections/{resource_id}/tags
{
    "tag": {
        "key": "key1",
        "value": "value1"
    }
}
```

-   Example Response

    None


## Returned Values<a name="section14121248103610"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

