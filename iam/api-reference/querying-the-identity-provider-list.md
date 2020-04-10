# Querying the Identity Provider List<a name="en-us_topic_0057845581"></a>

## Function Description<a name="section6167348094122"></a>

This interface is used to query the identity provider list.

## URI<a name="section6413693994122"></a>

URI format

GET /v3/OS-FEDERATION/identity\_providers

## Request<a name="section463689694122"></a>

-   Request header parameter description

    <a name="table2235968694122"></a>
    <table><thead align="left"><tr id="row6398767794122"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.1"><p id="p1561935894122"><a name="p1561935894122"></a><a name="p1561935894122"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.29%" id="mcps1.1.5.1.2"><p id="p5720848794122"><a name="p5720848794122"></a><a name="p5720848794122"></a><strong id="abf40cec725544c908dfabd5d5b0ab862"><a name="abf40cec725544c908dfabd5d5b0ab862"></a><a name="abf40cec725544c908dfabd5d5b0ab862"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.02%" id="mcps1.1.5.1.3"><p id="p337590594122"><a name="p337590594122"></a><a name="p337590594122"></a><strong id="ac3583127681341c8ac166a75fcda70da"><a name="ac3583127681341c8ac166a75fcda70da"></a><a name="ac3583127681341c8ac166a75fcda70da"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.2%" id="mcps1.1.5.1.4"><p id="p501291694122"><a name="p501291694122"></a><a name="p501291694122"></a><strong id="b842352706114032_1"><a name="b842352706114032_1"></a><a name="b842352706114032_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row339303194122"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p640006694122"><a name="p640006694122"></a><a name="p640006694122"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.29%" headers="mcps1.1.5.1.2 "><p id="p4864334294122"><a name="p4864334294122"></a><a name="p4864334294122"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.02%" headers="mcps1.1.5.1.3 "><p id="p4779662694122"><a name="p4779662694122"></a><a name="p4779662694122"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.2%" headers="mcps1.1.5.1.4 "><p id="p4632152794122"><a name="p4632152794122"></a><a name="p4632152794122"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row1424056594122"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p1263515094122"><a name="p1263515094122"></a><a name="p1263515094122"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.29%" headers="mcps1.1.5.1.2 "><p id="p1681423594122"><a name="p1681423594122"></a><a name="p1681423594122"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.02%" headers="mcps1.1.5.1.3 "><p id="p1977581394122"><a name="p1977581394122"></a><a name="p1977581394122"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.2%" headers="mcps1.1.5.1.4 "><p id="p34509161102440"><a name="p34509161102440"></a><a name="p34509161102440"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers
    ```


## Response<a name="section2767745494122"></a>

-   Response body parameter description

    <a name="table6229981794122"></a>
    <table><thead align="left"><tr id="row4042479894122"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.1"><p id="p5318322594122"><a name="p5318322594122"></a><a name="p5318322594122"></a><strong id="b4606982163018"><a name="b4606982163018"></a><a name="b4606982163018"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.56%" id="mcps1.1.5.1.2"><p id="p1287398194122"><a name="p1287398194122"></a><a name="p1287398194122"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.75%" id="mcps1.1.5.1.3"><p id="p3615950494122"><a name="p3615950494122"></a><a name="p3615950494122"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.2%" id="mcps1.1.5.1.4"><p id="p4323874994122"><a name="p4323874994122"></a><a name="p4323874994122"></a><strong id="b842352706114032_3"><a name="b842352706114032_3"></a><a name="b842352706114032_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1267777094122"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p2026643194122"><a name="p2026643194122"></a><a name="p2026643194122"></a>identity_providers</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.1.5.1.2 "><p id="p3096822994122"><a name="p3096822994122"></a><a name="p3096822994122"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.75%" headers="mcps1.1.5.1.3 "><p id="p2539862794122"><a name="p2539862794122"></a><a name="p2539862794122"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.2%" headers="mcps1.1.5.1.4 "><p id="p4402294694122"><a name="p4402294694122"></a><a name="p4402294694122"></a>List of identity providers.</p>
    </td>
    </tr>
    <tr id="row6066220294122"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p1469129294122"><a name="p1469129294122"></a><a name="p1469129294122"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.56%" headers="mcps1.1.5.1.2 "><p id="p4914401994122"><a name="p4914401994122"></a><a name="p4914401994122"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.75%" headers="mcps1.1.5.1.3 "><p id="p2124263194122"><a name="p2124263194122"></a><a name="p2124263194122"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.2%" headers="mcps1.1.5.1.4 "><p id="p4293155194122"><a name="p4293155194122"></a><a name="p4293155194122"></a>Resource links of an identity provider.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the identity\_providers format

    <a name="table5267050094151"></a>
    <table><thead align="left"><tr id="row6309797094151"><th class="cellrowborder" valign="top" width="20.28%" id="mcps1.1.5.1.1"><p id="p1066191394151"><a name="p1066191394151"></a><a name="p1066191394151"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.6%" id="mcps1.1.5.1.2"><p id="p5830864594151"><a name="p5830864594151"></a><a name="p5830864594151"></a><strong id="abd3882194b5746b084e68cd764115792"><a name="abd3882194b5746b084e68cd764115792"></a><a name="abd3882194b5746b084e68cd764115792"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.84%" id="mcps1.1.5.1.3"><p id="p2537983894151"><a name="p2537983894151"></a><a name="p2537983894151"></a><strong id="a8f5b530973ca4847bb52ba51185b1d73"><a name="a8f5b530973ca4847bb52ba51185b1d73"></a><a name="a8f5b530973ca4847bb52ba51185b1d73"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.28%" id="mcps1.1.5.1.4"><p id="p4250100394151"><a name="p4250100394151"></a><a name="p4250100394151"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2002923794151"><td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.1 "><p id="p1175549194151"><a name="p1175549194151"></a><a name="p1175549194151"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.6%" headers="mcps1.1.5.1.2 "><p id="p1267071894151"><a name="p1267071894151"></a><a name="p1267071894151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.84%" headers="mcps1.1.5.1.3 "><p id="p1969521394151"><a name="p1969521394151"></a><a name="p1969521394151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.28%" headers="mcps1.1.5.1.4 "><p id="p5180840994151"><a name="p5180840994151"></a><a name="p5180840994151"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row6362249794151"><td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.1 "><p id="p5314859494151"><a name="p5314859494151"></a><a name="p5314859494151"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.6%" headers="mcps1.1.5.1.2 "><p id="p1006885294151"><a name="p1006885294151"></a><a name="p1006885294151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.84%" headers="mcps1.1.5.1.3 "><p id="p1027067094151"><a name="p1027067094151"></a><a name="p1027067094151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.28%" headers="mcps1.1.5.1.4 "><p id="p2661796194151"><a name="p2661796194151"></a><a name="p2661796194151"></a>Identity provider description.</p>
    </td>
    </tr>
    <tr id="row3823506294151"><td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.1 "><p id="p1003234194151"><a name="p1003234194151"></a><a name="p1003234194151"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.6%" headers="mcps1.1.5.1.2 "><p id="p731328894151"><a name="p731328894151"></a><a name="p731328894151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.84%" headers="mcps1.1.5.1.3 "><p id="p17875329172823"><a name="p17875329172823"></a><a name="p17875329172823"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.28%" headers="mcps1.1.5.1.4 "><p id="p38615584172823"><a name="p38615584172823"></a><a name="p38615584172823"></a>Whether an identity provider is enabled. <strong id="b842352706184851_1"><a name="b842352706184851_1"></a><a name="b842352706184851_1"></a>true</strong> indicates that the identity provider is enabled. <strong id="b842352706184924_1"><a name="b842352706184924_1"></a><a name="b842352706184924_1"></a>false</strong> indicates that the identity provider is disabled. The default value is <strong id="b602514205184952_1"><a name="b602514205184952_1"></a><a name="b602514205184952_1"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row222582054614"><td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.1 "><p id="p586154154615"><a name="p586154154615"></a><a name="p586154154615"></a>remote_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.6%" headers="mcps1.1.5.1.2 "><p id="p686224164611"><a name="p686224164611"></a><a name="p686224164611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.84%" headers="mcps1.1.5.1.3 "><p id="p58621341134616"><a name="p58621341134616"></a><a name="p58621341134616"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.28%" headers="mcps1.1.5.1.4 "><p id="p7862114124617"><a name="p7862114124617"></a><a name="p7862114124617"></a>Federated user ID list of an identity provider.</p>
    </td>
    </tr>
    <tr id="row6394731194151"><td class="cellrowborder" valign="top" width="20.28%" headers="mcps1.1.5.1.1 "><p id="p1234971794151"><a name="p1234971794151"></a><a name="p1234971794151"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.6%" headers="mcps1.1.5.1.2 "><p id="p6080302794151"><a name="p6080302794151"></a><a name="p6080302794151"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.84%" headers="mcps1.1.5.1.3 "><p id="p2609819494151"><a name="p2609819494151"></a><a name="p2609819494151"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.28%" headers="mcps1.1.5.1.4 "><p id="p3357900294151"><a name="p3357900294151"></a><a name="p3357900294151"></a>Resource links of an identity provider.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "identity_providers": [
            {
                "description": "Stores ACME identities",
                "enabled": true,
                "id": "ACME",
                "remote_ids": [],
                "links": {
                    "protocols": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME/protocols",
                    "self": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME"
                }
            },
            {
                "description": "Stores contractor identities",
                "enabled": false,
                "remote_ids": [],
                "id": "ACME-contractors",
                "links": {
                    "protocols": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME-contractors/protocols",
                    "self": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME-contractors"
                }
            }
        ],
        "links": {
            "next": null,
            "previous": null,
            "self": "https://example.com/v3/OS-FEDERATION/identity_providers"
        }
    }
    ```


## Status Codes<a name="section5044917494122"></a>

<a name="table5985125594122"></a>
<table><thead align="left"><tr id="row267668994122"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1548526794122"><a name="p1548526794122"></a><a name="p1548526794122"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p4634713894122"><a name="p4634713894122"></a><a name="p4634713894122"></a><strong id="b842352706114032_5"><a name="b842352706114032_5"></a><a name="b842352706114032_5"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6313069394122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1331251794122"><a name="p1331251794122"></a><a name="p1331251794122"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p457207394122"><a name="p457207394122"></a><a name="p457207394122"></a>The request is successful.</p>
</td>
</tr>
<tr id="row4114866094122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4470717894122"><a name="p4470717894122"></a><a name="p4470717894122"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6451167294122"><a name="p6451167294122"></a><a name="p6451167294122"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row4373414494122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5280480794122"><a name="p5280480794122"></a><a name="p5280480794122"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4933093794122"><a name="p4933093794122"></a><a name="p4933093794122"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row4132525594122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5901133594122"><a name="p5901133594122"></a><a name="p5901133594122"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1518884094122"><a name="p1518884094122"></a><a name="p1518884094122"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row248183694122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6681104194122"><a name="p6681104194122"></a><a name="p6681104194122"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4298522694122"><a name="p4298522694122"></a><a name="p4298522694122"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row5132271894122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6349947394122"><a name="p6349947394122"></a><a name="p6349947394122"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4318366094122"><a name="p4318366094122"></a><a name="p4318366094122"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row5310862494122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p683132494122"><a name="p683132494122"></a><a name="p683132494122"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1646633994122"><a name="p1646633994122"></a><a name="p1646633994122"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row1397932994122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5858388794122"><a name="p5858388794122"></a><a name="p5858388794122"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4767438194122"><a name="p4767438194122"></a><a name="p4767438194122"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row2641624594122"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5934111994122"><a name="p5934111994122"></a><a name="p5934111994122"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4190132594122"><a name="p4190132594122"></a><a name="p4190132594122"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

