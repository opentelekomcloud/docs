# Adding a Tag to a Specified Cluster<a name="EN-US_TOPIC_0172486217"></a>

## Function<a name="sabc7dbff6adb45cd93f20e092357ae85"></a>

This API is used to add a tag to a specified cluster.

A cluster has a maximum of 10 tags. This API is idempotent. If a tag to be created has the same key as an existing tag, the tag will overwrite the existing one.

## URI<a name="s589e5ad723a343ea8224ae5acfacde33"></a>

-   Format

    POST /v1.1/\{project\_id\}/clusters/\{cluster\_id\}/tags

-   Parameter description

    **Table  1**  URI parameter description

    <a name="t242752ea56bf450f8b80444174e62d69"></a>
    <table><thead align="left"><tr id="r65f89e1a178c4a47a56dd81220c532de"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="aa3ca13de4d274217bd889b319cde8849"><a name="aa3ca13de4d274217bd889b319cde8849"></a><a name="aa3ca13de4d274217bd889b319cde8849"></a><strong id="b11821152456"><a name="b11821152456"></a><a name="b11821152456"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110707061_p388412816227"><a name="en-us_topic_0110707061_p388412816227"></a><a name="en-us_topic_0110707061_p388412816227"></a><strong id="b15596580510"><a name="b15596580510"></a><a name="b15596580510"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a0736051ee1a1415baeb2f55ed1c0d255"><a name="a0736051ee1a1415baeb2f55ed1c0d255"></a><a name="a0736051ee1a1415baeb2f55ed1c0d255"></a><strong id="b144525127519"><a name="b144525127519"></a><a name="b144525127519"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r6f5ab9d702da4458b8f3904ca5532d44"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a8ac9ce258b8d4ab6a6c0b87a91a5077b"><a name="a8ac9ce258b8d4ab6a6c0b87a91a5077b"></a><a name="a8ac9ce258b8d4ab6a6c0b87a91a5077b"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aba45b9aac26445bda5f40178b6133773"><a name="aba45b9aac26445bda5f40178b6133773"></a><a name="aba45b9aac26445bda5f40178b6133773"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a295457bf2fb046afa866835c4b9113a2"><a name="a295457bf2fb046afa866835c4b9113a2"></a><a name="a295457bf2fb046afa866835c4b9113a2"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="r03e757778a544a539934b26ce498f671"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110707061_p288462815221"><a name="en-us_topic_0110707061_p288462815221"></a><a name="en-us_topic_0110707061_p288462815221"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a476657609f5d4ca6b6df423e6c7579c2"><a name="a476657609f5d4ca6b6df423e6c7579c2"></a><a name="a476657609f5d4ca6b6df423e6c7579c2"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110707061_p78845285227"><a name="en-us_topic_0110707061_p78845285227"></a><a name="en-us_topic_0110707061_p78845285227"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="sa272ba477099400b8eaac43b02f930a6"></a>

**Table  2** **tags**  parameter description

<a name="t5d6a85e09aa14d16986a8cf2f3e34375"></a>
<table><thead align="left"><tr id="r1e5c57d68620402c8bb798b3c5642170"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="aa0ecbcc8ff644332b45740923b6b65cd"><a name="aa0ecbcc8ff644332b45740923b6b65cd"></a><a name="aa0ecbcc8ff644332b45740923b6b65cd"></a><strong id="b98906428618"><a name="b98906428618"></a><a name="b98906428618"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0110707061_p359718019240"><a name="en-us_topic_0110707061_p359718019240"></a><a name="en-us_topic_0110707061_p359718019240"></a><strong id="b7655144515619"><a name="b7655144515619"></a><a name="b7655144515619"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0110707061_p35978012418"><a name="en-us_topic_0110707061_p35978012418"></a><a name="en-us_topic_0110707061_p35978012418"></a><strong id="b632122642111"><a name="b632122642111"></a><a name="b632122642111"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="a2688727b75e34fe9bf2e6b7a76b15ffe"><a name="a2688727b75e34fe9bf2e6b7a76b15ffe"></a><a name="a2688727b75e34fe9bf2e6b7a76b15ffe"></a><strong id="b7414174910617"><a name="b7414174910617"></a><a name="b7414174910617"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r920ccc483fe44ace8e1d8ad774de1583"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0110707061_p105973017245"><a name="en-us_topic_0110707061_p105973017245"></a><a name="en-us_topic_0110707061_p105973017245"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0110707061_p15982012410"><a name="en-us_topic_0110707061_p15982012410"></a><a name="en-us_topic_0110707061_p15982012410"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="a8f87a73d2a9046538f9e21249ae5b1ef"><a name="a8f87a73d2a9046538f9e21249ae5b1ef"></a><a name="a8f87a73d2a9046538f9e21249ae5b1ef"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="ad3d3b7688d0f4103884579ec59e1d4ad"><a name="ad3d3b7688d0f4103884579ec59e1d4ad"></a><a name="ad3d3b7688d0f4103884579ec59e1d4ad"></a>Key. A tag key can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="r132299a936a04e58acc72ffd714cc879"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="ae0ae0dc1e3dc4cd58e23a7932f0065e3"><a name="ae0ae0dc1e3dc4cd58e23a7932f0065e3"></a><a name="ae0ae0dc1e3dc4cd58e23a7932f0065e3"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0110707061_p25981800247"><a name="en-us_topic_0110707061_p25981800247"></a><a name="en-us_topic_0110707061_p25981800247"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0110707061_p125981607243"><a name="en-us_topic_0110707061_p125981607243"></a><a name="en-us_topic_0110707061_p125981607243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0110707061_p55984072416"><a name="en-us_topic_0110707061_p55984072416"></a><a name="en-us_topic_0110707061_p55984072416"></a>Tag value. A tag value can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="s77010e865e2a4004801f00406353c065"></a>

**Response parameters**

None.

## Example<a name="s5a73aa4f71334961ba7f8ccde0a863b7"></a>

-   Example request

```
{ 
    "tag": 
        { 
            "key":"DEV", 
            "value":"DEV1" 
        } 
} 
```

-   Example response

    None.


## Status Code<a name="s33965fe40ed14d9d958a455b548fcf23"></a>

[Table 3](#t853eb843894541af90b6f0a45bbc833f)  describes the status code of this API.

**Table  3**  Status code

<a name="t853eb843894541af90b6f0a45bbc833f"></a>
<table><thead align="left"><tr id="r28ded54d02d945a6a8381f42ecc6660a"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="a71689c7f46044c97ad1008854138cf29"><a name="a71689c7f46044c97ad1008854138cf29"></a><a name="a71689c7f46044c97ad1008854138cf29"></a><strong id="b139705541965"><a name="b139705541965"></a><a name="b139705541965"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="ab71bc72c98d446ff8cd1afb6ac2c83b3"><a name="ab71bc72c98d446ff8cd1afb6ac2c83b3"></a><a name="ab71bc72c98d446ff8cd1afb6ac2c83b3"></a><strong id="b09741858563"><a name="b09741858563"></a><a name="b09741858563"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r00b9253346d847fa885b20cac7c83cc1"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="af5fbec93e9a5465580f513eb3541567b"><a name="af5fbec93e9a5465580f513eb3541567b"></a><a name="af5fbec93e9a5465580f513eb3541567b"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1666511011814"><a name="p1666511011814"></a><a name="p1666511011814"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

