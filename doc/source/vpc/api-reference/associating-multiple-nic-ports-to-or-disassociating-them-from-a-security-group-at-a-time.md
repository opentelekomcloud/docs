# Associating Multiple NIC Ports to or Disassociating Them from a Security Group at a Time<a name="vpc_sg01_0009"></a>

## Function<a name="section19171415101615"></a>

This API is used to associate multiple NIC ports to or disassociate them from a specified security group at a time.

Restrictions

-   A maximum of 20 ports can be associated to or disassociated from a security group at a time. Therefore, the  **ports**  can contain a maximum of 20 values.
-   No error message is displayed if a port is repeatedly associated with a security group.

## URI<a name="section1173915101614"></a>

POST /v2.0/\{project\_id\}/security-groups/\{security\_group\_id\}/instance/action

[Table 1](#table7179415121614)  describes the parameters.

**Table  1**  Parameter description

<a name="table7179415121614"></a>
<table><thead align="left"><tr id="row67501815151611"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p117501155166"><a name="p117501155166"></a><a name="p117501155166"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p15750121513169"><a name="p15750121513169"></a><a name="p15750121513169"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16750141512163"><a name="p16750141512163"></a><a name="p16750141512163"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row57502152163"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12750191511167"><a name="p12750191511167"></a><a name="p12750191511167"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15750141581618"><a name="p15750141581618"></a><a name="p15750141581618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row1475016159162"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1475041510165"><a name="p1475041510165"></a><a name="p1475041510165"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6750315121612"><a name="p6750315121612"></a><a name="p6750315121612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p197508154161"><a name="p197508154161"></a><a name="p197508154161"></a>Specifies the security group ID, which uniquely identifies the security group.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section720601541612"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table1022441561614"></a>
    <table><thead align="left"><tr id="row975131518166"><th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.1"><p id="p11751131519166"><a name="p11751131519166"></a><a name="p11751131519166"></a><strong id="b252372732"><a name="b252372732"></a><a name="b252372732"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p197511815141617"><a name="p197511815141617"></a><a name="p197511815141617"></a><strong id="b832160256"><a name="b832160256"></a><a name="b832160256"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p11751171520163"><a name="p11751171520163"></a><a name="p11751171520163"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.03479652034796%" id="mcps1.2.5.1.4"><p id="p1975111511162"><a name="p1975111511162"></a><a name="p1975111511162"></a><strong id="b403087497"><a name="b403087497"></a><a name="b403087497"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row175311156169"><td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.1 "><p id="p1175310154166"><a name="p1175310154166"></a><a name="p1175310154166"></a>ports</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p11753315161614"><a name="p11753315161614"></a><a name="p11753315161614"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1975321591618"><a name="p1975321591618"></a><a name="p1975321591618"></a>Array of <a href="#table425751511619">Port</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.03479652034796%" headers="mcps1.2.5.1.4 "><p id="p177531515171617"><a name="p177531515171617"></a><a name="p177531515171617"></a>Specifies the port list. A maximum of 20 ports are supported. For details, see <a href="#table425751511619">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row19753121514169"><td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.1 "><p id="p117534152161"><a name="p117534152161"></a><a name="p117534152161"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p187531415131610"><a name="p187531415131610"></a><a name="p187531415131610"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p475315153160"><a name="p475315153160"></a><a name="p475315153160"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.03479652034796%" headers="mcps1.2.5.1.4 "><p id="p137531515151616"><a name="p137531515151616"></a><a name="p137531515151616"></a>Specifies the operation. The value can be <strong id="b842352706143633"><a name="b842352706143633"></a><a name="b842352706143633"></a>add</strong> (associate) or <strong id="b842352706143640"><a name="b842352706143640"></a><a name="b842352706143640"></a>remove</strong> (disassociate). The values are case-insensitive.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of field  **Port**

    <a name="table425751511619"></a>
    <table><thead align="left"><tr id="row12753515131613"><th class="cellrowborder" valign="top" width="15.46154615461546%" id="mcps1.2.5.1.1"><p id="p16753115161610"><a name="p16753115161610"></a><a name="p16753115161610"></a><strong id="b138911397"><a name="b138911397"></a><a name="b138911397"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.46154615461546%" id="mcps1.2.5.1.2"><p id="p2075351510161"><a name="p2075351510161"></a><a name="p2075351510161"></a><strong id="b439541327"><a name="b439541327"></a><a name="b439541327"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.682268226822682%" id="mcps1.2.5.1.3"><p id="p13753141511167"><a name="p13753141511167"></a><a name="p13753141511167"></a><strong id="b93486284"><a name="b93486284"></a><a name="b93486284"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.39463946394639%" id="mcps1.2.5.1.4"><p id="p27534153168"><a name="p27534153168"></a><a name="p27534153168"></a><strong id="b998381387"><a name="b998381387"></a><a name="b998381387"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9753121514167"><td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.1 "><p id="p14753141531614"><a name="p14753141531614"></a><a name="p14753141531614"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.46154615461546%" headers="mcps1.2.5.1.2 "><p id="p0753715121618"><a name="p0753715121618"></a><a name="p0753715121618"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.682268226822682%" headers="mcps1.2.5.1.3 "><p id="p1075571551616"><a name="p1075571551616"></a><a name="p1075571551616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.39463946394639%" headers="mcps1.2.5.1.4 "><p id="p1175521531616"><a name="p1175521531616"></a><a name="p1175521531616"></a>Specifies the port ID, which uniquely identifies the port.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v1/{project_id}/security-groups/0c4a2336-b036-4fa2-bc3c-1a291ed4c431/instance/action
    
    {
        "ports": [
            {
                "id": "b9ac5247-c4ca-4c9b-b8fa-7d19132e560a"
            },
            {
                "id": "aa2f8625-0042-4627-a05c-61500b604cc3"
            }
        ],
        "action": "add"
    }
    ```


## Response Message<a name="section2265151517164"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table18277615121617"></a>
    <table><thead align="left"><tr id="row57551715151620"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.1"><p id="p17551415191614"><a name="p17551415191614"></a><a name="p17551415191614"></a><strong id="b232021943"><a name="b232021943"></a><a name="b232021943"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p3755141514168"><a name="p3755141514168"></a><a name="p3755141514168"></a><strong id="b1480938603"><a name="b1480938603"></a><a name="b1480938603"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.120000000000005%" id="mcps1.2.4.1.3"><p id="p13755121501610"><a name="p13755121501610"></a><a name="p13755121501610"></a><strong id="b647462150"><a name="b647462150"></a><a name="b647462150"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14755815121614"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p137553158163"><a name="p137553158163"></a><a name="p137553158163"></a>fail</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p2755121511617"><a name="p2755121511617"></a><a name="p2755121511617"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p1222855185215"><a name="p1222855185215"></a><a name="p1222855185215"></a>Specifies the failed ports. For details, see <a href="#table728810252119">Table 5</a>.</p>
    <p id="p9755191514163"><a name="p9755191514163"></a><a name="p9755191514163"></a>If all ports are associated with or disassociated from the security group successfully, the <strong id="b842352706151212"><a name="b842352706151212"></a><a name="b842352706151212"></a>fail</strong> list in the response body is blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **fail**  objects

    <a name="table728810252119"></a>
    <table><thead align="left"><tr id="row628819213214"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.4.1.1"><p id="p1428715213216"><a name="p1428715213216"></a><a name="p1428715213216"></a><strong id="b598474802"><a name="b598474802"></a><a name="b598474802"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.2"><p id="p32878212116"><a name="p32878212116"></a><a name="p32878212116"></a><strong id="b413952671"><a name="b413952671"></a><a name="b413952671"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.239999999999995%" id="mcps1.2.4.1.3"><p id="p1828719212217"><a name="p1828719212217"></a><a name="p1828719212217"></a><strong id="b1861543133"><a name="b1861543133"></a><a name="b1861543133"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row328818272110"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.1 "><p id="p1288122152110"><a name="p1288122152110"></a><a name="p1288122152110"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p2028820216213"><a name="p2028820216213"></a><a name="p2028820216213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p192887242110"><a name="p192887242110"></a><a name="p192887242110"></a>Specifies the ID of the failed port, which uniquely identifies the port.</p>
    </td>
    </tr>
    <tr id="row1328816212217"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.1 "><p id="p1828816210216"><a name="p1828816210216"></a><a name="p1828816210216"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p228817212116"><a name="p228817212116"></a><a name="p228817212116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p11288222213"><a name="p11288222213"></a><a name="p11288222213"></a>Specifies the error code.</p>
    </td>
    </tr>
    <tr id="row132886218216"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.1 "><p id="p122889219214"><a name="p122889219214"></a><a name="p122889219214"></a>error_msg</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p19288152122111"><a name="p19288152122111"></a><a name="p19288152122111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p128819211218"><a name="p128819211218"></a><a name="p128819211218"></a>Specifies the error message.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response 1

    Multiple NIC ports are successfully associated to or disassociated from a security group at a time.

    ```
    {
        "fail": []
    }
    ```

-   Example normal response 2

    Some NIC ports fail to be associated to or disassociated from a security group at a time.

    ```
    {
        "fail": [
            {
                "id": "99d9d709-8478-4b46-9f3f-2206b1023fd3",
                "error_code": "VPC.0608",
                "error_msg": "{\"NeutronError\":{\"message\":\"Port 99d9d709-8478-4b46-9f3f-2206b1023fd3 could not be found.\",\"type\":\"PortNotFound\",\"detail\":\"\"}}"
            },
            {
                "id": "aa2f8625-0042-4627-a05c-61500b604cc3",
                "error_code": "VPC.0607",
                "error_msg": "An instance must belong to at least one security group"
            }
        ]
    }
    ```


-   Example abnormal response

    ```
    {
        "code": "VPC.0606",
        "message": "Request is invalid"
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section1634901513167"></a>

See  [Error Codes](error-codes.md).

