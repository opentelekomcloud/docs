# Querying Tags of a Tenant's Resources<a name="vpcep_06_0503"></a>

## Function<a name="section20272125217516"></a>

This API is used to obtain tags of resources of a tenant based on the tenant ID and resource type.

## URI<a name="section11275852457"></a>

Format

GET  /v1/\{project\_id\}/\{resource\_type\}/tags

[Table 1](#table943516221477)  describes the required parameters.

**Table  1**  Parameter description

<a name="table943516221477"></a>
<table><thead align="left"><tr id="row1343613226474"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.1"><p id="p9436922104719"><a name="p9436922104719"></a><a name="p9436922104719"></a><strong id="b1980532918211"><a name="b1980532918211"></a><a name="b1980532918211"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.5.1.2"><p id="p194362228474"><a name="p194362228474"></a><a name="p194362228474"></a><strong id="b1460393016218"><a name="b1460393016218"></a><a name="b1460393016218"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.3"><p id="p1243612224474"><a name="p1243612224474"></a><a name="p1243612224474"></a><strong id="b176571932132113"><a name="b176571932132113"></a><a name="b176571932132113"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.709999999999994%" id="mcps1.2.5.1.4"><p id="p1343632294715"><a name="p1343632294715"></a><a name="p1343632294715"></a><strong id="b676223316215"><a name="b676223316215"></a><a name="b676223316215"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1143672204713"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p114361222479"><a name="p114361222479"></a><a name="p114361222479"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.2 "><p id="p11436222134717"><a name="p11436222134717"></a><a name="p11436222134717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="p11436022124715"><a name="p11436022124715"></a><a name="p11436022124715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.5.1.4 "><p id="p204361922164712"><a name="p204361922164712"></a><a name="p204361922164712"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row12436162264715"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p2436202244718"><a name="p2436202244718"></a><a name="p2436202244718"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.2 "><p id="p7436162254718"><a name="p7436162254718"></a><a name="p7436162254718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.3 "><p id="p3437152214478"><a name="p3437152214478"></a><a name="p3437152214478"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.5.1.4 "><p id="p143713224476"><a name="p143713224476"></a><a name="p143713224476"></a>Specifies the resource type. The value is <strong id="b19928243192119"><a name="b19928243192119"></a><a name="b19928243192119"></a>endpoint_service</strong> or <strong id="b7929043122119"><a name="b7929043122119"></a><a name="b7929043122119"></a>endpoint</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section5371135214516"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table72968529518"></a>
    <table><thead align="left"><tr id="row13746552252"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.1"><p id="p197462521954"><a name="p197462521954"></a><a name="p197462521954"></a><strong id="b13821155172117"><a name="b13821155172117"></a><a name="b13821155172117"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.2"><p id="p1074614520518"><a name="p1074614520518"></a><a name="p1074614520518"></a><strong id="b15520175311211"><a name="b15520175311211"></a><a name="b15520175311211"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.3"><p id="p14747175211514"><a name="p14747175211514"></a><a name="p14747175211514"></a><strong id="b1070812544219"><a name="b1070812544219"></a><a name="b1070812544219"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p107471852755"><a name="p107471852755"></a><a name="p107471852755"></a><strong id="b1654013557212"><a name="b1654013557212"></a><a name="b1654013557212"></a>Example</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1674715219512"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p20747752255"><a name="p20747752255"></a><a name="p20747752255"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p974716526517"><a name="p974716526517"></a><a name="p974716526517"></a>Specifies the MIME type of the entity sending the request.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p4747952453"><a name="p4747952453"></a><a name="p4747952453"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p1747145212513"><a name="p1747145212513"></a><a name="p1747145212513"></a>application/json</p>
    </td>
    </tr>
    <tr id="row87473527511"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p374795217512"><a name="p374795217512"></a><a name="p374795217512"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p8747652659"><a name="p8747652659"></a><a name="p8747652659"></a>Specifies the user token.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p207471452752"><a name="p207471452752"></a><a name="p207471452752"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p1974711521653"><a name="p1974711521653"></a><a name="p1974711521653"></a>None</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    GET https://127.0.0.1:7443/v1/\{project\_id\}/endpoint\_service/tags

    or https://127.0.0.1:7443/v1/\{project\_id\}/endpoint/tags GET /v1/\{project\_id\}/\{resource\_type\}/tags


## Response<a name="section1743165217514"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table124997528515"></a>
    <table><thead align="left"><tr id="row1374816521452"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.5.1.1"><p id="p12748115220515"><a name="p12748115220515"></a><a name="p12748115220515"></a><strong id="b511165414238"><a name="b511165414238"></a><a name="b511165414238"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.2"><p id="p574816523510"><a name="p574816523510"></a><a name="p574816523510"></a><strong id="b2411755142315"><a name="b2411755142315"></a><a name="b2411755142315"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.5.1.3"><p id="p47482520515"><a name="p47482520515"></a><a name="p47482520515"></a><strong id="b148145672313"><a name="b148145672313"></a><a name="b148145672313"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.630000000000003%" id="mcps1.2.5.1.4"><p id="p97481352054"><a name="p97481352054"></a><a name="p97481352054"></a><strong id="b635614576239"><a name="b635614576239"></a><a name="b635614576239"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row107488520520"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.1 "><p id="p1474817529515"><a name="p1474817529515"></a><a name="p1474817529515"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.2 "><p id="p1274865214513"><a name="p1274865214513"></a><a name="p1274865214513"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p774810524514"><a name="p774810524514"></a><a name="p774810524514"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.5.1.4 "><p id="p1774811521655"><a name="p1774811521655"></a><a name="p1774811521655"></a>Lists the tags.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Data structure of the  **resource\_tag**  field

    <a name="table144649521456"></a>
    <table><thead align="left"><tr id="row1974875215510"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.5.1.1"><p id="p57487522519"><a name="p57487522519"></a><a name="p57487522519"></a><strong id="b3852101922414"><a name="b3852101922414"></a><a name="b3852101922414"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.5.1.2"><p id="p97488522056"><a name="p97488522056"></a><a name="p97488522056"></a><strong id="b4444821102411"><a name="b4444821102411"></a><a name="b4444821102411"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.5.1.3"><p id="p177481352457"><a name="p177481352457"></a><a name="p177481352457"></a><strong id="b73104233246"><a name="b73104233246"></a><a name="b73104233246"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.5.1.4"><p id="p1174810524515"><a name="p1174810524515"></a><a name="p1174810524515"></a><strong id="b19310192418245"><a name="b19310192418245"></a><a name="b19310192418245"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4748952551"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.1 "><p id="p4748552253"><a name="p4748552253"></a><a name="p4748552253"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.5.1.2 "><p id="p1574825213511"><a name="p1574825213511"></a><a name="p1574825213511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.3 "><p id="p107481452555"><a name="p107481452555"></a><a name="p107481452555"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.5.1.4 "><p id="p3748852459"><a name="p3748852459"></a><a name="p3748852459"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row177481152358"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.1 "><p id="p77481952952"><a name="p77481952952"></a><a name="p77481952952"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.5.1.2 "><p id="p107499521154"><a name="p107499521154"></a><a name="p107499521154"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.3 "><p id="p1874910523511"><a name="p1874910523511"></a><a name="p1874910523511"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.5.1.4 "><p id="p1674965220511"><a name="p1674965220511"></a><a name="p1674965220511"></a>Lists the tag values.</p>
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
                    "*value1",
                    "value2"
                ]
            }
        ]
    }
    ```


## Status Code<a name="section652619523510"></a>

For details about status codes, see  [Status Code](status-code.md).

