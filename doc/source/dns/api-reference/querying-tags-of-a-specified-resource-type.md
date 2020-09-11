# Querying Tags of a Specified Resource Type<a name="dns_api_67005"></a>

## Function<a name="section2763065016101"></a>

Query all tags of a resource type.

## URI<a name="section53701671161015"></a>

GET /v2/\{project\_id\}/\{resource\_type\}/tags

For details, see  [Table 1](#table6099729418149).

**Table  1**  Parameters in the URI

<a name="table6099729418149"></a>
<table><thead align="left"><tr id="row3442661918149"><th class="cellrowborder" valign="top" width="22.64%" id="mcps1.2.5.1.1"><p id="p3709279118149"><a name="p3709279118149"></a><a name="p3709279118149"></a><strong id="b67491352133415"><a name="b67491352133415"></a><a name="b67491352133415"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.37%" id="mcps1.2.5.1.2"><p id="p5172606218149"><a name="p5172606218149"></a><a name="p5172606218149"></a><strong id="b12453253183413"><a name="b12453253183413"></a><a name="b12453253183413"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.3"><p id="p2906151418149"><a name="p2906151418149"></a><a name="p2906151418149"></a><strong id="b13154544345"><a name="b13154544345"></a><a name="b13154544345"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.64%" id="mcps1.2.5.1.4"><p id="p517246718149"><a name="p517246718149"></a><a name="p517246718149"></a><strong id="b1652975517341"><a name="b1652975517341"></a><a name="b1652975517341"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1631668818149"><td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.1 "><p id="p4658337018149"><a name="p4658337018149"></a><a name="p4658337018149"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p1515661618149"><a name="p1515661618149"></a><a name="p1515661618149"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="p1972638718149"><a name="p1972638718149"></a><a name="p1972638718149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.64%" headers="mcps1.2.5.1.4 "><p id="p5433349018149"><a name="p5433349018149"></a><a name="p5433349018149"></a>Project ID. You can obtain it in <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row1923936518149"><td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.1 "><p id="p1488470218149"><a name="p1488470218149"></a><a name="p1488470218149"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p6481017518149"><a name="p6481017518149"></a><a name="p6481017518149"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="p1513281718149"><a name="p1513281718149"></a><a name="p1513281718149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.64%" headers="mcps1.2.5.1.4 "><p id="p1779865118149"><a name="p1779865118149"></a><a name="p1779865118149"></a>Resource type, which can be <strong id="b1147611553514"><a name="b1147611553514"></a><a name="b1147611553514"></a>DNS-public_zone</strong>, <strong id="b1347615143517"><a name="b1347615143517"></a><a name="b1347615143517"></a>DNS-private_zone</strong>, <strong id="b9477105183520"><a name="b9477105183520"></a><a name="b9477105183520"></a>DNS-public_recordset</strong>, <strong id="b144779523516"><a name="b144779523516"></a><a name="b144779523516"></a>DNS-private_recordset</strong>, or <strong id="b184781853350"><a name="b184781853350"></a><a name="b184781853350"></a>DNS-ptr_record</strong></p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section44958995161021"></a>

None

-   Parameter description

    None

-   Example request

    Query tags of all private zones in a project:

    ```
    GET https://{DNS_Endpoint}/v2/{project_id}/DNS-private_zone/tags
    ```


## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  2**  Parameter in the response

    <a name="t593ae00046564bbcb49e84485ef14071"></a>
    <table><thead align="left"><tr id="rf54583b8c8e0499691d7d9ff9f06f37a"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="a86661040859b40a8b253c065971cf8ae"><a name="a86661040859b40a8b253c065971cf8ae"></a><a name="a86661040859b40a8b253c065971cf8ae"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.2"><p id="a5cfaf558b8724bd999608631ffa7f08f"><a name="a5cfaf558b8724bd999608631ffa7f08f"></a><a name="a5cfaf558b8724bd999608631ffa7f08f"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.09%" id="mcps1.2.4.1.3"><p id="acc90819224564ea5a481fc9816ae6a22"><a name="acc90819224564ea5a481fc9816ae6a22"></a><a name="acc90819224564ea5a481fc9816ae6a22"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r30b7bae25edb4cfc8fd03903cbe75b5a"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="a0c6dfa6d8f3f4730a43d1c0f2e94cbe0"><a name="a0c6dfa6d8f3f4730a43d1c0f2e94cbe0"></a><a name="a0c6dfa6d8f3f4730a43d1c0f2e94cbe0"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.2 "><p id="p10265887147"><a name="p10265887147"></a><a name="p10265887147"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.09%" headers="mcps1.2.4.1.3 "><p id="add06d19cb36743c8b9be66895278d027"><a name="add06d19cb36743c8b9be66895278d027"></a><a name="add06d19cb36743c8b9be66895278d027"></a>Tag list. For details, see <a href="#table19530794112436">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **tag**  field

    <a name="table19530794112436"></a>
    <table><thead align="left"><tr id="row15361836112436"><th class="cellrowborder" valign="top" width="18.011801180118013%" id="mcps1.2.4.1.1"><p id="p58707511112436"><a name="p58707511112436"></a><a name="p58707511112436"></a><strong id="b1215310182812"><a name="b1215310182812"></a><a name="b1215310182812"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.28192819281928%" id="mcps1.2.4.1.2"><p id="p42210623112436"><a name="p42210623112436"></a><a name="p42210623112436"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.70627062706271%" id="mcps1.2.4.1.3"><p id="p63617265112436"><a name="p63617265112436"></a><a name="p63617265112436"></a><strong id="b228181142817"><a name="b228181142817"></a><a name="b228181142817"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35684479112436"><td class="cellrowborder" valign="top" width="18.011801180118013%" headers="mcps1.2.4.1.1 "><p id="p13313439112530"><a name="p13313439112530"></a><a name="p13313439112530"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.28192819281928%" headers="mcps1.2.4.1.2 "><p id="p35653193112436"><a name="p35653193112436"></a><a name="p35653193112436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.70627062706271%" headers="mcps1.2.4.1.3 "><p id="p48921437201850"><a name="p48921437201850"></a><a name="p48921437201850"></a>Tag key. The key contains 36 Unicode characters at most and cannot be blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row20048002112436"><td class="cellrowborder" valign="top" width="18.011801180118013%" headers="mcps1.2.4.1.1 "><p id="p66095544112533"><a name="p66095544112533"></a><a name="p66095544112533"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.28192819281928%" headers="mcps1.2.4.1.2 "><p id="p60123528112436"><a name="p60123528112436"></a><a name="p60123528112436"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.70627062706271%" headers="mcps1.2.4.1.3 "><p id="p61714725112922"><a name="p61714725112922"></a><a name="p61714725112922"></a>Tag value, which contains 43 Unicode characters at most and can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

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


## Returned Value<a name="section9249181042119"></a>

If the API call returns a code of 2_xx_, for example, 200, 202, or 204, the request is successful.

For details, see  [Status Code](status-code.md).

