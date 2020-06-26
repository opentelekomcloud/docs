# Querying Tags of a Specified Cluster<a name="EN-US_TOPIC_0172486212"></a>

## Function<a name="s2dea9a4d93f74e39ba20cbedd4b7e8be"></a>

This API is used to query tags of a specified cluster.

## URI<a name="s61128a85a7bf43eea9d5e251476421e3"></a>

-   Format

    GET /v1.1/\{project\_id\}/clusters/\{cluster\_id\}/tags

-   Parameter description

    **Table  1**  URI parameter description

    <a name="t10d6a27e439748119bac5dba8ff725ee"></a>
    <table><thead align="left"><tr id="rc00b1d4d619d49578b746b159f6b14ef"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="aba577efd88e64045a07aecffdf6aa549"><a name="aba577efd88e64045a07aecffdf6aa549"></a><a name="aba577efd88e64045a07aecffdf6aa549"></a><strong id="b0460104191416"><a name="b0460104191416"></a><a name="b0460104191416"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110707083_p388412816227"><a name="en-us_topic_0110707083_p388412816227"></a><a name="en-us_topic_0110707083_p388412816227"></a><strong id="b390913091411"><a name="b390913091411"></a><a name="b390913091411"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="acb15181715474e73ac583c8ce5d0781e"><a name="acb15181715474e73ac583c8ce5d0781e"></a><a name="acb15181715474e73ac583c8ce5d0781e"></a><strong id="b1806105611137"><a name="b1806105611137"></a><a name="b1806105611137"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r46543c343acf45a5838026f8b399eb51"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a0b1454912a70443c8c7e81db3de6e78a"><a name="a0b1454912a70443c8c7e81db3de6e78a"></a><a name="a0b1454912a70443c8c7e81db3de6e78a"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a216bc5b881df408a8c8ae8bf39ba85a0"><a name="a216bc5b881df408a8c8ae8bf39ba85a0"></a><a name="a216bc5b881df408a8c8ae8bf39ba85a0"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a748e1bc3a75c4d91a7fc3722e0b9e6a8"><a name="a748e1bc3a75c4d91a7fc3722e0b9e6a8"></a><a name="a748e1bc3a75c4d91a7fc3722e0b9e6a8"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="rbc810e17a79b41bd8c797bf23c58abcb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110707083_p288462815221"><a name="en-us_topic_0110707083_p288462815221"></a><a name="en-us_topic_0110707083_p288462815221"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ae2a3892ba1744cbaad8fe0694bec9afa"><a name="ae2a3892ba1744cbaad8fe0694bec9afa"></a><a name="ae2a3892ba1744cbaad8fe0694bec9afa"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110707083_p78845285227"><a name="en-us_topic_0110707083_p78845285227"></a><a name="en-us_topic_0110707083_p78845285227"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s7d33ebe92ff14e34987ea021c259c478"></a>

**Request parameters**

None.

## Response<a name="s7761860ece7c49d0b77a9177c2ccbc06"></a>

**Table  2**  Parameter description

<a name="table16429741613"></a>
<table><thead align="left"><tr id="row6447741616"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p144437171619"><a name="p144437171619"></a><a name="p144437171619"></a><strong id="b13466107133"><a name="b13466107133"></a><a name="b13466107133"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p847075161"><a name="p847075161"></a><a name="p847075161"></a><strong id="b169551111151315"><a name="b169551111151315"></a><a name="b169551111151315"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p1548378165"><a name="p1548378165"></a><a name="p1548378165"></a><strong id="b611215481975"><a name="b611215481975"></a><a name="b611215481975"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row124947121617"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18491073163"><a name="p18491073163"></a><a name="p18491073163"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p0492712166"><a name="p0492712166"></a><a name="p0492712166"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p164907111612"><a name="p164907111612"></a><a name="p164907111612"></a>Key. A tag key can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row17501761611"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p115087181618"><a name="p115087181618"></a><a name="p115087181618"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p35027201610"><a name="p35027201610"></a><a name="p35027201610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p35027151611"><a name="p35027151611"></a><a name="p35027151611"></a>Tag value. A tag value can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="s936b4472ffcd469cabb7f86045e4a8d9"></a>

-   Example request

    None.

-   Example response

    ```
    { 
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


## Status Code<a name="s90bcfddb775445708aada537153df78f"></a>

[Table 3](#t8879ab801c3841179c9f683931ddb28e)  describes the status code of this API.

**Table  3**  Status code

<a name="t8879ab801c3841179c9f683931ddb28e"></a>
<table><thead align="left"><tr id="r36d47cc57e1642c4b85707586a41e0eb"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="a75d57993e25f418f98e400b75d8c69f0"><a name="a75d57993e25f418f98e400b75d8c69f0"></a><a name="a75d57993e25f418f98e400b75d8c69f0"></a><strong id="b136541145578"><a name="b136541145578"></a><a name="b136541145578"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="adb28f2a54c104798b44f849c0c35cc7c"><a name="adb28f2a54c104798b44f849c0c35cc7c"></a><a name="adb28f2a54c104798b44f849c0c35cc7c"></a><strong id="b1874746292"><a name="b1874746292"></a><a name="b1874746292"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="reded02762a3e4e20bdb2ff58a490425b"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="af56600e03d6442c2801caf1ce7308bb9"><a name="af56600e03d6442c2801caf1ce7308bb9"></a><a name="af56600e03d6442c2801caf1ce7308bb9"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110707083_p39771881331"><a name="en-us_topic_0110707083_p39771881331"></a><a name="en-us_topic_0110707083_p39771881331"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

