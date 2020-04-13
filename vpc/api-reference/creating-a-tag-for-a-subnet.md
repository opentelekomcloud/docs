# Creating a Tag for a Subnet<a name="subnet_tag_0001"></a>

## Function<a name="section8853142018214"></a>

This API is used to create a tag for a subnet.

## URI<a name="section1285422052116"></a>

POST /v2.0/\{project\_id\}/subnets/\{subnet\_id\}/tags

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b01161917957"><a name="b01161917957"></a><a name="b01161917957"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b109813171151"><a name="b109813171151"></a><a name="b109813171151"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b1672919251512"><a name="b1672919251512"></a><a name="b1672919251512"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8478608"><a name="p8478608"></a><a name="p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15678685"><a name="p15678685"></a><a name="p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43913021"><a name="p43913021"></a><a name="p43913021"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>Specifies the subnet ID, which uniquely identifies the subnet.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section086217203216"></a>

-   Request parameter

**Table  2**  Request parameter

<a name="table886222062114"></a>
<table><thead align="left"><tr id="row10925202010216"><th class="cellrowborder" valign="top" width="18.709999999999997%" id="mcps1.2.5.1.1"><p id="p13925152072110"><a name="p13925152072110"></a><a name="p13925152072110"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.5%" id="mcps1.2.5.1.2"><p id="p1592542016218"><a name="p1592542016218"></a><a name="p1592542016218"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.3"><p id="p49254209219"><a name="p49254209219"></a><a name="p49254209219"></a><strong id="b1219274019516"><a name="b1219274019516"></a><a name="b1219274019516"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.05%" id="mcps1.2.5.1.4"><p id="p692592042113"><a name="p692592042113"></a><a name="p692592042113"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1492522018213"><td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.2.5.1.1 "><p id="p89251820152120"><a name="p89251820152120"></a><a name="p89251820152120"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="12.5%" headers="mcps1.2.5.1.2 "><p id="p139251120182115"><a name="p139251120182115"></a><a name="p139251120182115"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p1192502015218"><a name="p1192502015218"></a><a name="p1192502015218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.05%" headers="mcps1.2.5.1.4 "><p id="p188571327104019"><a name="p188571327104019"></a><a name="p188571327104019"></a>Specifies the <strong id="b783915421755"><a name="b783915421755"></a><a name="b783915421755"></a>tag</strong> objects. For details, see <a href="#table13242848193719">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  objects

<a name="table13242848193719"></a>
<table><thead align="left"><tr id="row13343144812379"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="p15343174853715"><a name="p15343174853715"></a><a name="p15343174853715"></a><strong id="b42894468513"><a name="b42894468513"></a><a name="b42894468513"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.2.5.1.2"><p id="p13431648163716"><a name="p13431648163716"></a><a name="p13431648163716"></a><strong id="b135932471453"><a name="b135932471453"></a><a name="b135932471453"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.24%" id="mcps1.2.5.1.3"><p id="p118573278400"><a name="p118573278400"></a><a name="p118573278400"></a><strong id="b1440914818516"><a name="b1440914818516"></a><a name="b1440914818516"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.699999999999996%" id="mcps1.2.5.1.4"><p id="p11344748183719"><a name="p11344748183719"></a><a name="p11344748183719"></a><strong id="b1244974918519"><a name="b1244974918519"></a><a name="b1244974918519"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row103449487379"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p183469482373"><a name="p183469482373"></a><a name="p183469482373"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p1434684863710"><a name="p1434684863710"></a><a name="p1434684863710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.3 "><p id="p298018911544"><a name="p298018911544"></a><a name="p298018911544"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="56.699999999999996%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"><li>Specifies the tag key.</li><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a VPC must be unique.</li></ul>
</td>
</tr>
<tr id="row2346548163714"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p1134624816377"><a name="p1134624816377"></a><a name="p1134624816377"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.2 "><p id="p234619483371"><a name="p234619483371"></a><a name="p234619483371"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.3 "><p id="p209805915417"><a name="p209805915417"></a><a name="p209805915417"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="56.699999999999996%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"><li>Specifies the tag value.</li><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul7895160105919"></a><a name="ul7895160105919"></a><ul id="ul7895160105919"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

-   Example request

```
POST https://{Endpoint}/v2.0/{project_id}/subnets/{subnet_id}/tags

{
    "tag": {
        "key": "key1",
        "value": "value1"
    }
}
```

## Response Message<a name="section686818208212"></a>

-   Response parameter

    None

-   Example response

    None


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

