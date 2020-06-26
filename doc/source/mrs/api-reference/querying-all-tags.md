# Querying All Tags<a name="EN-US_TOPIC_0172486215"></a>

## Function<a name="s2c4189363a344e22a1de70463f225881"></a>

This API is used to query all tag sets of a specified region.

## URI<a name="sf0297651845047eaad627fb833801766"></a>

-   Format

    GET /v1.1/\{project\_id\}/clusters/tags

-   Parameter description

    **Table  1**  URI parameter description

    <a name="t54dd4e66085d4193a9e4dff304acd0f5"></a>
    <table><thead align="left"><tr id="r04d42e12ebb74f5886465a1c665aed00"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="a02b975a6373a4037808781548f2470f4"><a name="a02b975a6373a4037808781548f2470f4"></a><a name="a02b975a6373a4037808781548f2470f4"></a><strong id="b17817781210"><a name="b17817781210"></a><a name="b17817781210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110707085_p388412816227"><a name="en-us_topic_0110707085_p388412816227"></a><a name="en-us_topic_0110707085_p388412816227"></a><strong id="b183210157217"><a name="b183210157217"></a><a name="b183210157217"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="abf58273383de49d9a5c4a0c8465d8c5a"><a name="abf58273383de49d9a5c4a0c8465d8c5a"></a><a name="abf58273383de49d9a5c4a0c8465d8c5a"></a><strong id="b1278611810219"><a name="b1278611810219"></a><a name="b1278611810219"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r19443fe5cf19494eae78e1a5d90d5452"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a6467f31d1dba422f9c238fda74c94488"><a name="a6467f31d1dba422f9c238fda74c94488"></a><a name="a6467f31d1dba422f9c238fda74c94488"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a767b39b559e84c6ba85a8d190cc90ff9"><a name="a767b39b559e84c6ba85a8d190cc90ff9"></a><a name="a767b39b559e84c6ba85a8d190cc90ff9"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a455f9d9051904d85b859ee996a2f4f43"><a name="a455f9d9051904d85b859ee996a2f4f43"></a><a name="a455f9d9051904d85b859ee996a2f4f43"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="sd36cd2850091427daa0a2a98000f4602"></a>

**Request parameters**

None

## Response<a name="sa3b67fdf174846b687d4d5029329b305"></a>

**Table  2**  Response parameter description

<a name="table45211674182"></a>
<table><thead align="left"><tr id="row252312741816"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p452316771818"><a name="p452316771818"></a><a name="p452316771818"></a><strong id="b2288811132113"><a name="b2288811132113"></a><a name="b2288811132113"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p195241731814"><a name="p195241731814"></a><a name="p195241731814"></a><strong id="b11278172314213"><a name="b11278172314213"></a><a name="b11278172314213"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p152487181819"><a name="p152487181819"></a><a name="p152487181819"></a><strong id="b1813061016"><a name="b1813061016"></a><a name="b1813061016"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row105271270182"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p95275716189"><a name="p95275716189"></a><a name="p95275716189"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p15528675188"><a name="p15528675188"></a><a name="p15528675188"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p752897201817"><a name="p752897201817"></a><a name="p752897201817"></a>Key. A tag key can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row1853018771810"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1153016731813"><a name="p1153016731813"></a><a name="p1153016731813"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1353077121812"><a name="p1353077121812"></a><a name="p1353077121812"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p653015761811"><a name="p653015761811"></a><a name="p653015761811"></a>Tag value. A tag value can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="s81c3ed017afc4602b480dc53561c1799"></a>

-   Example request

None

-   Example response

```
{ 
    "tags": [ 
    { 
        "key": "key1", 
        "values": [ 
            "value1", 
            "value2" 
        ] 
        }, 
        { 
        "key": "key2", 
        "values": [ 
            "value1", 
            "value2" 
        ] 
        } 
    ] 
} 

```

## Status Code<a name="s2cffe92837ac4e14a9afda7d5eb8e64e"></a>

[Table 3](#tb472a78155014ba18b372672dd8358e7)  describes the status code of this API.

**Table  3**  Status code

<a name="tb472a78155014ba18b372672dd8358e7"></a>
<table><thead align="left"><tr id="r201b1aef028b40ef962c83fd95b4861f"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="a76d01c2d730241b6811241045aa51c7e"><a name="a76d01c2d730241b6811241045aa51c7e"></a><a name="a76d01c2d730241b6811241045aa51c7e"></a><strong id="b171387571898"><a name="b171387571898"></a><a name="b171387571898"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="ad8353c4c972e4361a19786b6b50cac52"><a name="ad8353c4c972e4361a19786b6b50cac52"></a><a name="ad8353c4c972e4361a19786b6b50cac52"></a><strong id="b307563499"><a name="b307563499"></a><a name="b307563499"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra779cebca1bd45db945a8c7504ed9896"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="a99d8911646c942dea59d9acfe54b2e7c"><a name="a99d8911646c942dea59d9acfe54b2e7c"></a><a name="a99d8911646c942dea59d9acfe54b2e7c"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110707085_p39771881331"><a name="en-us_topic_0110707085_p39771881331"></a><a name="en-us_topic_0110707085_p39771881331"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

