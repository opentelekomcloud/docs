# Querying an Identity Provider<a name="en-us_topic_0057845639"></a>

## Function Description<a name="section1157015294151"></a>

This interface is used to query the information about an identity provider.

## URI<a name="section4603296894151"></a>

-   URI format

    GET /v3/OS-FEDERATION/identity\_providers/\{id\}


-   URI parameter description

    <a name="table1251903794151"></a>
    <table><thead align="left"><tr id="row1594222394151"><th class="cellrowborder" valign="top" width="22.21%" id="mcps1.1.5.1.1"><p id="p1625166694151"><a name="p1625166694151"></a><a name="p1625166694151"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.04%" id="mcps1.1.5.1.2"><p id="p4131654194151"><a name="p4131654194151"></a><a name="p4131654194151"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.37%" id="mcps1.1.5.1.3"><p id="p5830552994151"><a name="p5830552994151"></a><a name="p5830552994151"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.379999999999995%" id="mcps1.1.5.1.4"><p id="p2512740594151"><a name="p2512740594151"></a><a name="p2512740594151"></a><strong id="b842352706114032_1"><a name="b842352706114032_1"></a><a name="b842352706114032_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2205395494151"><td class="cellrowborder" valign="top" width="22.21%" headers="mcps1.1.5.1.1 "><p id="p4153987294151"><a name="p4153987294151"></a><a name="p4153987294151"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.2 "><p id="p928644694151"><a name="p928644694151"></a><a name="p928644694151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.37%" headers="mcps1.1.5.1.3 "><p id="p1400462894151"><a name="p1400462894151"></a><a name="p1400462894151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.379999999999995%" headers="mcps1.1.5.1.4 "><p id="p6063308394151"><a name="p6063308394151"></a><a name="p6063308394151"></a>ID of an identity provider.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1233268294151"></a>

-   Request header parameter description

    <a name="table4855072394151"></a>
    <table><thead align="left"><tr id="row279645794151"><th class="cellrowborder" valign="top" width="21.98219821982198%" id="mcps1.1.5.1.1"><p id="p2518650394151"><a name="p2518650394151"></a><a name="p2518650394151"></a><strong id="b20009936163129"><a name="b20009936163129"></a><a name="b20009936163129"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.45174517451745%" id="mcps1.1.5.1.2"><p id="p2684087394151"><a name="p2684087394151"></a><a name="p2684087394151"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.13161316131613%" id="mcps1.1.5.1.3"><p id="p2662712894151"><a name="p2662712894151"></a><a name="p2662712894151"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.43444344434443%" id="mcps1.1.5.1.4"><p id="p931375594151"><a name="p931375594151"></a><a name="p931375594151"></a><strong id="b11975469163129"><a name="b11975469163129"></a><a name="b11975469163129"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1621669994151"><td class="cellrowborder" valign="top" width="21.98219821982198%" headers="mcps1.1.5.1.1 "><p id="p3848422394151"><a name="p3848422394151"></a><a name="p3848422394151"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.45174517451745%" headers="mcps1.1.5.1.2 "><p id="p3021435294151"><a name="p3021435294151"></a><a name="p3021435294151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13161316131613%" headers="mcps1.1.5.1.3 "><p id="p3144341394151"><a name="p3144341394151"></a><a name="p3144341394151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.43444344434443%" headers="mcps1.1.5.1.4 "><p id="p6388850294151"><a name="p6388850294151"></a><a name="p6388850294151"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row3812561394151"><td class="cellrowborder" valign="top" width="21.98219821982198%" headers="mcps1.1.5.1.1 "><p id="p116698194151"><a name="p116698194151"></a><a name="p116698194151"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.45174517451745%" headers="mcps1.1.5.1.2 "><p id="p2741662194151"><a name="p2741662194151"></a><a name="p2741662194151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13161316131613%" headers="mcps1.1.5.1.3 "><p id="p615380594151"><a name="p615380594151"></a><a name="p615380594151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.43444344434443%" headers="mcps1.1.5.1.4 "><p id="p34509161102440"><a name="p34509161102440"></a><a name="p34509161102440"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers/ACME
    ```


## Response<a name="section4269135194151"></a>

-   Response body parameter description

    <a name="table5267050094151"></a>
    <table><thead align="left"><tr id="row6309797094151"><th class="cellrowborder" valign="top" width="21.867813218678133%" id="mcps1.1.5.1.1"><p id="p1066191394151"><a name="p1066191394151"></a><a name="p1066191394151"></a><strong id="b24391346163129"><a name="b24391346163129"></a><a name="b24391346163129"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.608239176082392%" id="mcps1.1.5.1.2"><p id="p5830864594151"><a name="p5830864594151"></a><a name="p5830864594151"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.1.5.1.3"><p id="p2537983894151"><a name="p2537983894151"></a><a name="p2537983894151"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.195580441955805%" id="mcps1.1.5.1.4"><p id="p4250100394151"><a name="p4250100394151"></a><a name="p4250100394151"></a><strong id="b842352706114032_3"><a name="b842352706114032_3"></a><a name="b842352706114032_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2002923794151"><td class="cellrowborder" valign="top" width="21.867813218678133%" headers="mcps1.1.5.1.1 "><p id="p1175549194151"><a name="p1175549194151"></a><a name="p1175549194151"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.608239176082392%" headers="mcps1.1.5.1.2 "><p id="p1267071894151"><a name="p1267071894151"></a><a name="p1267071894151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p1969521394151"><a name="p1969521394151"></a><a name="p1969521394151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.195580441955805%" headers="mcps1.1.5.1.4 "><p id="p5180840994151"><a name="p5180840994151"></a><a name="p5180840994151"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row6362249794151"><td class="cellrowborder" valign="top" width="21.867813218678133%" headers="mcps1.1.5.1.1 "><p id="p5314859494151"><a name="p5314859494151"></a><a name="p5314859494151"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.608239176082392%" headers="mcps1.1.5.1.2 "><p id="p1006885294151"><a name="p1006885294151"></a><a name="p1006885294151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p1027067094151"><a name="p1027067094151"></a><a name="p1027067094151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.195580441955805%" headers="mcps1.1.5.1.4 "><p id="p2661796194151"><a name="p2661796194151"></a><a name="p2661796194151"></a>Identity provider description.</p>
    </td>
    </tr>
    <tr id="row3823506294151"><td class="cellrowborder" valign="top" width="21.867813218678133%" headers="mcps1.1.5.1.1 "><p id="p1003234194151"><a name="p1003234194151"></a><a name="p1003234194151"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.608239176082392%" headers="mcps1.1.5.1.2 "><p id="p731328894151"><a name="p731328894151"></a><a name="p731328894151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p17875329172823"><a name="p17875329172823"></a><a name="p17875329172823"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.195580441955805%" headers="mcps1.1.5.1.4 "><p id="p150721349439"><a name="p150721349439"></a><a name="p150721349439"></a>Whether an identity provider is enabled.</p>
    <a name="ul4939885894312"></a><a name="ul4939885894312"></a><ul id="ul4939885894312"><li><strong id="b5446265494312"><a name="b5446265494312"></a><a name="b5446265494312"></a>true</strong> indicates that the identity provider is enabled.</li><li><strong id="b2040184294312"><a name="b2040184294312"></a><a name="b2040184294312"></a>false</strong> indicates that the identity provider is disabled.</li></ul>
    <p id="p38615584172823"><a name="p38615584172823"></a><a name="p38615584172823"></a>The default value is <strong id="b10631473159329"><a name="b10631473159329"></a><a name="b10631473159329"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row222582054614"><td class="cellrowborder" valign="top" width="21.867813218678133%" headers="mcps1.1.5.1.1 "><p id="p586154154615"><a name="p586154154615"></a><a name="p586154154615"></a>remote_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.608239176082392%" headers="mcps1.1.5.1.2 "><p id="p686224164611"><a name="p686224164611"></a><a name="p686224164611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p58621341134616"><a name="p58621341134616"></a><a name="p58621341134616"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.195580441955805%" headers="mcps1.1.5.1.4 "><p id="p7862114124617"><a name="p7862114124617"></a><a name="p7862114124617"></a>Federated user ID list of an identity provider.</p>
    </td>
    </tr>
    <tr id="row6394731194151"><td class="cellrowborder" valign="top" width="21.867813218678133%" headers="mcps1.1.5.1.1 "><p id="p1234971794151"><a name="p1234971794151"></a><a name="p1234971794151"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.608239176082392%" headers="mcps1.1.5.1.2 "><p id="p6080302794151"><a name="p6080302794151"></a><a name="p6080302794151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="p2609819494151"><a name="p2609819494151"></a><a name="p2609819494151"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.195580441955805%" headers="mcps1.1.5.1.4 "><p id="p3357900294151"><a name="p3357900294151"></a><a name="p3357900294151"></a>Resource links of an identity provider.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "identity_provider": {
            "description": "Stores ACME identities",
            "enabled": false,
            "id": "ACME",
            "remote_ids": [],
            "links": {
                "protocols": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME/protocols",
                "self": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME"
            }
        }
    }
    ```


## Status Codes<a name="section5928057394151"></a>

<a name="table3699709194151"></a>
<table><thead align="left"><tr id="row4643214094151"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p290701894151"><a name="p290701894151"></a><a name="p290701894151"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p3414188094151"><a name="p3414188094151"></a><a name="p3414188094151"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1402886294151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6259603794151"><a name="p6259603794151"></a><a name="p6259603794151"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3711422894151"><a name="p3711422894151"></a><a name="p3711422894151"></a>The request is successful.</p>
</td>
</tr>
<tr id="row6559260394151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1140060294151"><a name="p1140060294151"></a><a name="p1140060294151"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5103355894151"><a name="p5103355894151"></a><a name="p5103355894151"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row5664883894151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2515312794151"><a name="p2515312794151"></a><a name="p2515312794151"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2413740194151"><a name="p2413740194151"></a><a name="p2413740194151"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row1591001994151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1364320194151"><a name="p1364320194151"></a><a name="p1364320194151"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3135750794151"><a name="p3135750794151"></a><a name="p3135750794151"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row1378211494151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4260941394151"><a name="p4260941394151"></a><a name="p4260941394151"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2881046694151"><a name="p2881046694151"></a><a name="p2881046694151"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row5796760594151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6486440994151"><a name="p6486440994151"></a><a name="p6486440994151"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1952577094151"><a name="p1952577094151"></a><a name="p1952577094151"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row4151420294151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p720720894151"><a name="p720720894151"></a><a name="p720720894151"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4691301594151"><a name="p4691301594151"></a><a name="p4691301594151"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row1956395994151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4117680994151"><a name="p4117680994151"></a><a name="p4117680994151"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4698724894151"><a name="p4698724894151"></a><a name="p4698724894151"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row2023205594151"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2818376894151"><a name="p2818376894151"></a><a name="p2818376894151"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p118387394151"><a name="p118387394151"></a><a name="p118387394151"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

