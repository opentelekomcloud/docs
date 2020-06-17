# Querying an SSH Key Pair \(Native OpenStack API\)<a name="EN-US_TOPIC_0060384659"></a>

## Function<a name="section59539732104217"></a>

This interface is used to query a specified SSH key pair based on the key pair name.

## URI<a name="section52138884104217"></a>

GET /v2.1/\{project\_id\}/os-keypairs/\{keypair\_name\}

[Table 1](#table1179423205514)  lists the parameters.

**Table  1**  Parameter description

<a name="table1179423205514"></a>
<table><thead align="left"><tr id="row679693215558"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p17653616104217"><a name="p17653616104217"></a><a name="p17653616104217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p20656767104217"><a name="p20656767104217"></a><a name="p20656767104217"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p62585419104217"><a name="p62585419104217"></a><a name="p62585419104217"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row379623265513"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p50904119104217"><a name="p50904119104217"></a><a name="p50904119104217"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29593000104217"><a name="p29593000104217"></a><a name="p29593000104217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48222838104217"><a name="p48222838104217"></a><a name="p48222838104217"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row1579623216550"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p56513487104217"><a name="p56513487104217"></a><a name="p56513487104217"></a>keypair_name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14189698104217"><a name="p14189698104217"></a><a name="p14189698104217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8514927104217"><a name="p8514927104217"></a><a name="p8514927104217"></a>Specifies the key pair name.</p>
<p id="p7466161413561"><a name="p7466161413561"></a><a name="p7466161413561"></a>You can obtain the key pair name by calling the <a href="querying-ssh-key-pairs-(native-openstack-api).md">Querying SSH Key Pairs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section18620476104217"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/os-keypairs/keypair-test
    ```


## Response Message<a name="section18336671104217"></a>

-   Response parameters

    <a name="table47814565104217"></a>
    <table><thead align="left"><tr id="row50677205104217"><th class="cellrowborder" valign="top" width="23.45765423457654%" id="mcps1.1.4.1.1"><p id="p19987085"><a name="p19987085"></a><a name="p19987085"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.376962303769623%" id="mcps1.1.4.1.2"><p id="p4546697"><a name="p4546697"></a><a name="p4546697"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.16538346165384%" id="mcps1.1.4.1.3"><p id="p32738149"><a name="p32738149"></a><a name="p32738149"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33037343104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.1.4.1.1 "><p id="p58779125104217"><a name="p58779125104217"></a><a name="p58779125104217"></a>keypair</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.1.4.1.2 "><p id="p63488655104217"><a name="p63488655104217"></a><a name="p63488655104217"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.1.4.1.3 "><p id="p42307413104217"><a name="p42307413104217"></a><a name="p42307413104217"></a>Specifies the SSH key pair. For details, see <a href="#table39136185104217">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **keypair**  field data structure description

    <a name="table39136185104217"></a>
    <table><thead align="left"><tr id="row60401722104217"><th class="cellrowborder" valign="top" width="23.45765423457654%" id="mcps1.2.4.1.1"><p id="p2384624132419"><a name="p2384624132419"></a><a name="p2384624132419"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.376962303769623%" id="mcps1.2.4.1.2"><p id="p23851124102419"><a name="p23851124102419"></a><a name="p23851124102419"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.16538346165384%" id="mcps1.2.4.1.3"><p id="p1388224162411"><a name="p1388224162411"></a><a name="p1388224162411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52495862104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p24306447104217"><a name="p24306447104217"></a><a name="p24306447104217"></a>public_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p22665160104217"><a name="p22665160104217"></a><a name="p22665160104217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p23938633104217"><a name="p23938633104217"></a><a name="p23938633104217"></a>Specifies information about the public key in the key pair.</p>
    </td>
    </tr>
    <tr id="row14121108104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p2959125104217"><a name="p2959125104217"></a><a name="p2959125104217"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p38362611104217"><a name="p38362611104217"></a><a name="p38362611104217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p20363797104217"><a name="p20363797104217"></a><a name="p20363797104217"></a>Specifies the key pair name.</p>
    </td>
    </tr>
    <tr id="row49056452104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p14149639104217"><a name="p14149639104217"></a><a name="p14149639104217"></a>fingerprint</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p5270148104217"><a name="p5270148104217"></a><a name="p5270148104217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p24228833104217"><a name="p24228833104217"></a><a name="p24228833104217"></a>Specifies fingerprint information about the key pair.</p>
    </td>
    </tr>
    <tr id="row16732907104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p13188220104217"><a name="p13188220104217"></a><a name="p13188220104217"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p61612865104217"><a name="p61612865104217"></a><a name="p61612865104217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p24586146104217"><a name="p24586146104217"></a><a name="p24586146104217"></a>Specifies the time when the key pair was created.</p>
    <p id="p8768130115818"><a name="p8768130115818"></a><a name="p8768130115818"></a>The timestamp format is ISO 8601, for example, <strong id="b127321289367"><a name="b127321289367"></a><a name="b127321289367"></a>2019-05-07T12:06:13.681238</strong>.</p>
    </td>
    </tr>
    <tr id="row19948729104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p5234385104217"><a name="p5234385104217"></a><a name="p5234385104217"></a>deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p21332025104217"><a name="p21332025104217"></a><a name="p21332025104217"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p50172441104217"><a name="p50172441104217"></a><a name="p50172441104217"></a>Specifies the deleted key pair.</p>
    <a name="ul1594190135612"></a><a name="ul1594190135612"></a><ul id="ul1594190135612"><li><strong id="b968419312363"><a name="b968419312363"></a><a name="b968419312363"></a>true</strong>: indicates that the key has been deleted.</li><li><strong id="b1992713710367"><a name="b1992713710367"></a><a name="b1992713710367"></a>false</strong>: indicates that the key is not deleted.</li></ul>
    </td>
    </tr>
    <tr id="row48898790104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p1379054104217"><a name="p1379054104217"></a><a name="p1379054104217"></a>deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p44594563104217"><a name="p44594563104217"></a><a name="p44594563104217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p55389836104217"><a name="p55389836104217"></a><a name="p55389836104217"></a>Specifies the time when the key pair was deleted.</p>
    <p id="p03819116010"><a name="p03819116010"></a><a name="p03819116010"></a>The timestamp format is ISO 8601, for example, <strong id="b1735746163617"><a name="b1735746163617"></a><a name="b1735746163617"></a>2019-05-07T12:06:13.681238</strong>.</p>
    </td>
    </tr>
    <tr id="row28746480104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p46763523104217"><a name="p46763523104217"></a><a name="p46763523104217"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p29748990104217"><a name="p29748990104217"></a><a name="p29748990104217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p60857994104217"><a name="p60857994104217"></a><a name="p60857994104217"></a>Specifies the key pair ID.</p>
    </td>
    </tr>
    <tr id="row10851038104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p6518853104217"><a name="p6518853104217"></a><a name="p6518853104217"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p58265105104217"><a name="p58265105104217"></a><a name="p58265105104217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p21853098104217"><a name="p21853098104217"></a><a name="p21853098104217"></a>Specifies the time when the key pair was updated.</p>
    <p id="p63535230013"><a name="p63535230013"></a><a name="p63535230013"></a>The timestamp format is ISO 8601, for example, <strong id="b178515518369"><a name="b178515518369"></a><a name="b178515518369"></a>2019-05-07T12:06:13.681238</strong>.</p>
    </td>
    </tr>
    <tr id="row62460159104217"><td class="cellrowborder" valign="top" width="23.45765423457654%" headers="mcps1.2.4.1.1 "><p id="p26108085104217"><a name="p26108085104217"></a><a name="p26108085104217"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.376962303769623%" headers="mcps1.2.4.1.2 "><p id="p34380140104217"><a name="p34380140104217"></a><a name="p34380140104217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.16538346165384%" headers="mcps1.2.4.1.3 "><p id="p33327947104217"><a name="p33327947104217"></a><a name="p33327947104217"></a>Specifies information about the user to which the key pair belongs.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "keypair": {
            "created_at": "2019-05-07T12:06:13.681238",
            "deleted": false,
            "deleted_at": null,
            "fingerprint": "9d:00:f4:d7:26:6e:52:06:4c:c1:d3:1d:fd:06:66:01",
            "id": 1,
            "name": "keypair-3582d8b7-e588-4aad-b7f7-f4e76f0e4314",
            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYJrTVpcMwFqQy/oMvtUSRofZdSRHEwrsX8AYkRvn2ZnCXM+b6+GZ2NQuuWj+ocznlnwiGFQDsL/yeE+/kurqcPJFKKp60mToXIMyzioFxW88fJtwEWawHKAclbHWpR1t4fQ4DS+/sIbX/Yd9btlVQ2tpQjodGDbM9Tr9/+/3i6rcR+EoLqmbgCgAiGiVV6VbM2Zx79yUwd+GnQejHX8BlYZoOjCnt3NREsITcmWE9FVFy6TnLmahs3FkEO/QGgWGkaohAJlsgaVvSWGgDn2AujKYwyDokK3dXyeX3m2Vmc3ejiqPa/C4nRrCOlko5nSgV/9IXRx1ERImsqZnE9usB Generated-by-Nova",
            "updated_at": null,
            "user_id": "fake"
        }
    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

