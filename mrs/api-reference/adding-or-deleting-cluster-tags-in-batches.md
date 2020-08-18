# Adding or Deleting Cluster Tags in Batches<a name="EN-US_TOPIC_0172486186"></a>

## Function<a name="s4969c1be9a19479d9af7069822fdb764"></a>

This API is used to add or delete tags to or from a specified cluster in batches.

You can add a maximum of 10 tags to a cluster.

This API is idempotent.

-   If a tag to be created has the same key as an existing tag in a cluster, the tag will overwrite the existing one.
-   When tags are being deleted and some tags do not exist, the operation is considered successful by default. The character set of the tags will not be checked. A key and a value can respectively contain up to 36 and 43 Unicode characters. When tags are deleted, the tag structure body cannot be missing, and the key cannot be left blank or set to an empty string.

## URI<a name="s7e1e6a97191e4347941ecfc96abd3c77"></a>

-   Format

    POST /v1.1/\{project\_id\}/clusters/\{cluster\_id\}/tags/action

-   Parameter description

    **Table  1**  URI parameter description

    <a name="tf3254cc0bddd4ce1a9b92cb40f6de853"></a>
    <table><thead align="left"><tr id="r2e84186059434d99b8c742382b0fee81"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="ade38f74c59ce41faa66bfe43bc20a96a"><a name="ade38f74c59ce41faa66bfe43bc20a96a"></a><a name="ade38f74c59ce41faa66bfe43bc20a96a"></a><strong id="b1446111496168"><a name="b1446111496168"></a><a name="b1446111496168"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110707084_p388412816227"><a name="en-us_topic_0110707084_p388412816227"></a><a name="en-us_topic_0110707084_p388412816227"></a><strong id="b19942165271618"><a name="b19942165271618"></a><a name="b19942165271618"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a032b43d71d3246f3991872e84aaadb53"><a name="a032b43d71d3246f3991872e84aaadb53"></a><a name="a032b43d71d3246f3991872e84aaadb53"></a><strong id="b1169245617167"><a name="b1169245617167"></a><a name="b1169245617167"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ree613defae51403cb54596766e6645ce"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a881b5bd84a2f4a0d9afdeb545ba6eef9"><a name="a881b5bd84a2f4a0d9afdeb545ba6eef9"></a><a name="a881b5bd84a2f4a0d9afdeb545ba6eef9"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aa916f1d130ea49498084b3ba255cfd9c"><a name="aa916f1d130ea49498084b3ba255cfd9c"></a><a name="aa916f1d130ea49498084b3ba255cfd9c"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aea751a56ac34435ca4eafc4850a8e492"><a name="aea751a56ac34435ca4eafc4850a8e492"></a><a name="aea751a56ac34435ca4eafc4850a8e492"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="rb0e1b8eddea44717be151f0638fbdeed"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110707084_p288462815221"><a name="en-us_topic_0110707084_p288462815221"></a><a name="en-us_topic_0110707084_p288462815221"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="abdbf690e3661474bbb1052629f8f6f1e"><a name="abdbf690e3661474bbb1052629f8f6f1e"></a><a name="abdbf690e3661474bbb1052629f8f6f1e"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110707084_p78845285227"><a name="en-us_topic_0110707084_p78845285227"></a><a name="en-us_topic_0110707084_p78845285227"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s6d1b0cc8a05a4f2aba89dbb8a107a8c6"></a>

**Table  2**  Request parameter description

<a name="table14432239181616"></a>
<table><thead align="left"><tr id="r77cc1fcfa9db457da93d35e4eb787815"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="a21974b0943aa4cb6a12f14d29817a199"><a name="a21974b0943aa4cb6a12f14d29817a199"></a><a name="a21974b0943aa4cb6a12f14d29817a199"></a><strong id="b6289731687"><a name="b6289731687"></a><a name="b6289731687"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="a89bdd7658a454789ba35ec57206f51df"><a name="a89bdd7658a454789ba35ec57206f51df"></a><a name="a89bdd7658a454789ba35ec57206f51df"></a><strong id="b14395575811"><a name="b14395575811"></a><a name="b14395575811"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="a4c90654eaeb84e0fb1f95bcd07c315ca"><a name="a4c90654eaeb84e0fb1f95bcd07c315ca"></a><a name="a4c90654eaeb84e0fb1f95bcd07c315ca"></a><strong id="b753844833016"><a name="b753844833016"></a><a name="b753844833016"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="a4a95222fe65145f5a74573043ef0929f"><a name="a4a95222fe65145f5a74573043ef0929f"></a><a name="a4a95222fe65145f5a74573043ef0929f"></a><strong id="b27056107814"><a name="b27056107814"></a><a name="b27056107814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row74701412153511"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0110707084_p511118336479"><a name="en-us_topic_0110707084_p511118336479"></a><a name="en-us_topic_0110707084_p511118336479"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0110707084_p91125331476"><a name="en-us_topic_0110707084_p91125331476"></a><a name="en-us_topic_0110707084_p91125331476"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="abc04c3b98e384b05a9b5c16cb5760b14"><a name="abc04c3b98e384b05a9b5c16cb5760b14"></a><a name="abc04c3b98e384b05a9b5c16cb5760b14"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p2803193053319"><a name="p2803193053319"></a><a name="p2803193053319"></a>Operation to be performed. The value can be set to <strong id="b842352706101829"><a name="b842352706101829"></a><a name="b842352706101829"></a>create</strong> or <strong id="b842352706101833"><a name="b842352706101833"></a><a name="b842352706101833"></a>delete</strong> only.</p>
</td>
</tr>
<tr id="row1928473143317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="a53353f8c43234b49bebf1528691aadd3"><a name="a53353f8c43234b49bebf1528691aadd3"></a><a name="a53353f8c43234b49bebf1528691aadd3"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="a1da3b045858d4d998d6f3bf94bbeef19"><a name="a1da3b045858d4d998d6f3bf94bbeef19"></a><a name="a1da3b045858d4d998d6f3bf94bbeef19"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="a8de69057efac4661aa74d763f46fe772"><a name="a8de69057efac4661aa74d763f46fe772"></a><a name="a8de69057efac4661aa74d763f46fe772"></a>List&lt;resource_tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p828412312331"><a name="p828412312331"></a><a name="p828412312331"></a>Tag list. For details about the parameter, see <a href="#table102451749203418">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="table102451749203418"></a>
<table><thead align="left"><tr id="row11245134983416"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p11245549153412"><a name="p11245549153412"></a><a name="p11245549153412"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p15245164911342"><a name="p15245164911342"></a><a name="p15245164911342"></a><strong id="b1440201916"><a name="b1440201916"></a><a name="b1440201916"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p02452491347"><a name="p02452491347"></a><a name="p02452491347"></a><strong id="b1388784780"><a name="b1388784780"></a><a name="b1388784780"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p4245104914346"><a name="p4245104914346"></a><a name="p4245104914346"></a><strong id="b1269291241"><a name="b1269291241"></a><a name="b1269291241"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row624504943418"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4245114911345"><a name="p4245114911345"></a><a name="p4245114911345"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2024534963413"><a name="p2024534963413"></a><a name="p2024534963413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p12245164933414"><a name="p12245164933414"></a><a name="p12245164933414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p182451949113418"><a name="p182451949113418"></a><a name="p182451949113418"></a>Key. A tag key can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row9245164914346"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p17246104915345"><a name="p17246104915345"></a><a name="p17246104915345"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p122465497341"><a name="p122465497341"></a><a name="p122465497341"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p52469499349"><a name="p52469499349"></a><a name="p52469499349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p3246174915343"><a name="p3246174915343"></a><a name="p3246174915343"></a>Tag value. A tag value can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
<p id="p20457145933916"><a name="p20457145933916"></a><a name="p20457145933916"></a>Note:</p>
<a name="ul1592490114013"></a><a name="ul1592490114013"></a><ul id="ul1592490114013"><li>This parameter is mandatory for adding a tag.</li><li>This parameter is optional for deleting a tag.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="s7889c008f458454892786e0168d76047"></a>

**Response parameters**

None.

## Example<a name="s49ceead68c9642a59eb5d3ddc20f81c2"></a>

-   Example request

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

-   Example response

    None.


## Status Code<a name="se40bddf775334160bff30d5c6259c3f3"></a>

[Table 4](#t8387a0fadf974df1925645625284999c)  describes the status code of this API.

**Table  4**  Status code

<a name="t8387a0fadf974df1925645625284999c"></a>
<table><thead align="left"><tr id="r940e742a18ba4bb1b68472e1d18a01d1"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="a7e168e3e863f4836be71177c7b7865f8"><a name="a7e168e3e863f4836be71177c7b7865f8"></a><a name="a7e168e3e863f4836be71177c7b7865f8"></a><strong id="b1359719161283"><a name="b1359719161283"></a><a name="b1359719161283"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="adb382a0290854ac191b3766fa8589fd8"><a name="adb382a0290854ac191b3766fa8589fd8"></a><a name="adb382a0290854ac191b3766fa8589fd8"></a><strong id="b8950181816815"><a name="b8950181816815"></a><a name="b8950181816815"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rfdbdcd9448224fc7859434ea27e4fa60"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="ab74c60350a4644c0843fb5f83c2f8a2c"><a name="ab74c60350a4644c0843fb5f83c2f8a2c"></a><a name="ab74c60350a4644c0843fb5f83c2f8a2c"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110707084_p39771881331"><a name="en-us_topic_0110707084_p39771881331"></a><a name="en-us_topic_0110707084_p39771881331"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

