# Batch Creating or Deleting VPN Resource Tags<a name="en_topic_0093011485"></a>

## **Function**<a name="en-us_topic_0103470569_section9716105931810"></a>

This interface is used to add multiple tags to or delete multiple tags from a VPN resource instance at a time.

This API is idempotent.

If there are duplicate keys in the request body when you add tags, an error is reported.

During tag creation, duplicate keys are not allowed. If a key exists in the database, its value will be overwritten.

During tag deletion, if some tags do not exist, the operation is considered to be successful by default. The character set of the tags will not be checked. When you delete tags, the tag structure cannot be missing, and the key cannot be left blank or be an empty string.

## URI<a name="en-us_topic_0103470569_section14718205991814"></a>

POST /v2.0/\{project\_id\}/ipsec-site-connections /\{resource\_id\}/tags/action

>![](/images/icon-note.gif) **NOTE:**   
>In the URI,  **project\_id**  indicates the project ID, and  **resource\_id**  indicates the target resource ID.  

## Request Parameter<a name="en-us_topic_0103470569_section972418597185"></a>

<a name="en-us_topic_0103470569_table2726185911818"></a>
<table><thead align="left"><tr id="en-us_topic_0103470569_row1080816597184"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.1.5.1.1"><p id="en-us_topic_0103470569_p208081359151817"><a name="en-us_topic_0103470569_p208081359151817"></a><a name="en-us_topic_0103470569_p208081359151817"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.2"><p id="en-us_topic_0103470569_p9808135941814"><a name="en-us_topic_0103470569_p9808135941814"></a><a name="en-us_topic_0103470569_p9808135941814"></a><strong id="b84235270610412"><a name="b84235270610412"></a><a name="b84235270610412"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9.900990099009901%" id="mcps1.1.5.1.3"><p id="en-us_topic_0103470569_p080805991816"><a name="en-us_topic_0103470569_p080805991816"></a><a name="en-us_topic_0103470569_p080805991816"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.415841584158414%" id="mcps1.1.5.1.4"><p id="en-us_topic_0103470569_p680845913189"><a name="en-us_topic_0103470569_p680845913189"></a><a name="en-us_topic_0103470569_p680845913189"></a><strong id="b842352706151625"><a name="b842352706151625"></a><a name="b842352706151625"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0103470569_row180885915182"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0103470569_p148081759191815"><a name="en-us_topic_0103470569_p148081759191815"></a><a name="en-us_topic_0103470569_p148081759191815"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0103470569_p080895941818"><a name="en-us_topic_0103470569_p080895941818"></a><a name="en-us_topic_0103470569_p080895941818"></a>List&lt;resource_tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0103470569_p6808115981818"><a name="en-us_topic_0103470569_p6808115981818"></a><a name="en-us_topic_0103470569_p6808115981818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.415841584158414%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0103470569_p180814592186"><a name="en-us_topic_0103470569_p180814592186"></a><a name="en-us_topic_0103470569_p180814592186"></a>Specifies the tag list. A tag list can contain a maximum of 10 keys.</p>
</td>
</tr>
<tr id="en-us_topic_0103470569_row58082596188"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0103470569_p128082059141814"><a name="en-us_topic_0103470569_p128082059141814"></a><a name="en-us_topic_0103470569_p128082059141814"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0103470569_p480816591183"><a name="en-us_topic_0103470569_p480816591183"></a><a name="en-us_topic_0103470569_p480816591183"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0103470569_p1380825915181"><a name="en-us_topic_0103470569_p1380825915181"></a><a name="en-us_topic_0103470569_p1380825915181"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.415841584158414%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0103470569_p1380812595189"><a name="en-us_topic_0103470569_p1380812595189"></a><a name="en-us_topic_0103470569_p1380812595189"></a>Specifies the operation to perform. The value can be <strong id="b842352706101829"><a name="b842352706101829"></a><a name="b842352706101829"></a>create</strong> or <strong id="b842352706101833"><a name="b842352706101833"></a><a name="b842352706101833"></a>delete</strong>.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **resource\_tag**

<a name="table13242848193719"></a>
<table><thead align="left"><tr id="row13343144812379"><th class="cellrowborder" valign="top" width="13.86%" id="mcps1.1.5.1.1"><p id="p15343174853715"><a name="p15343174853715"></a><a name="p15343174853715"></a><strong id="b84235270617246"><a name="b84235270617246"></a><a name="b84235270617246"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.4%" id="mcps1.1.5.1.2"><p id="p15643121154020"><a name="p15643121154020"></a><a name="p15643121154020"></a><strong id="b1190943337"><a name="b1190943337"></a><a name="b1190943337"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.5%" id="mcps1.1.5.1.3"><p id="p14992939103910"><a name="p14992939103910"></a><a name="p14992939103910"></a><strong id="b1349485000"><a name="b1349485000"></a><a name="b1349485000"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.24%" id="mcps1.1.5.1.4"><p id="p11344748183719"><a name="p11344748183719"></a><a name="p11344748183719"></a><strong id="b598537969"><a name="b598537969"></a><a name="b598537969"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row103449487379"><td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.1.5.1.1 "><p id="p183469482373"><a name="p183469482373"></a><a name="p183469482373"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.1.5.1.2 "><p id="p183268532416"><a name="p183268532416"></a><a name="p183268532416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.1.5.1.3 "><p id="p1434684863710"><a name="p1434684863710"></a><a name="p1434684863710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.24%" headers="mcps1.1.5.1.4 "><p id="p11346184819376"><a name="p11346184819376"></a><a name="p11346184819376"></a>Specifies the tag key.</p>
<p id="p6274131875416"><a name="p6274131875416"></a><a name="p6274131875416"></a>The parameter constraints are as follows:</p>
<a name="ul16111181314542"></a><a name="ul16111181314542"></a><ul id="ul16111181314542"><li>Must be unique for a resource.</li><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul1811131315418"></a><a name="ul1811131315418"></a><ul id="ul1811131315418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
<tr id="row2346548163714"><td class="cellrowborder" valign="top" width="13.86%" headers="mcps1.1.5.1.1 "><p id="p1134624816377"><a name="p1134624816377"></a><a name="p1134624816377"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.1.5.1.2 "><p id="p234619483371"><a name="p234619483371"></a><a name="p234619483371"></a>String</p>
<p id="p7712135910409"><a name="p7712135910409"></a><a name="p7712135910409"></a></p>
</td>
<td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.1.5.1.3 "><p id="p1128745714115"><a name="p1128745714115"></a><a name="p1128745714115"></a>(This parameter is mandatory when <strong id="b842352706143922"><a name="b842352706143922"></a><a name="b842352706143922"></a>action</strong> is set to <strong id="b842352706143928"><a name="b842352706143928"></a><a name="b842352706143928"></a>create</strong> and optional when <strong id="b2107046872143949"><a name="b2107046872143949"></a><a name="b2107046872143949"></a>action</strong> is set to <strong id="b1548858455143949"><a name="b1548858455143949"></a><a name="b1548858455143949"></a>delete</strong>.)</p>
</td>
<td class="cellrowborder" valign="top" width="43.24%" headers="mcps1.1.5.1.4 "><p id="p534634813374"><a name="p534634813374"></a><a name="p534634813374"></a>Specifies the tag value list.</p>
<p id="p774211695510"><a name="p774211695510"></a><a name="p774211695510"></a>The parameter constraints are as follows:</p>
<a name="ul2064810351548"></a><a name="ul2064810351548"></a><ul id="ul2064810351548"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul6656163575410"></a><a name="ul6656163575410"></a><ul id="ul6656163575410"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0103470569_section973755901815"></a>

None

## Example<a name="en-us_topic_0103470569_section3739159151817"></a>

-   Example Request

    ```
    POST /v2.0/{project_id}/ipsec-site-connections/{resource_id}/tags/action
    ```


## Request Body<a name="en-us_topic_0103470569_section973915961811"></a>

```
{
    "action": "create",
    "tags": [
        {
            "key": "key1",
            "value": "value1"
        },
        {
            "key": "key",
            "value": "value3"
        }
    ]
}
```

Or

```
{
    "action": "delete",
    "tags": [
        {
            "key": "key1",
            "value": "value1"
        },
        {
            "key": "key2",
            "value": "value3"
        }
    ]
}
```

-   Example Response

    None


## Returned Values<a name="section14121248103610"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

