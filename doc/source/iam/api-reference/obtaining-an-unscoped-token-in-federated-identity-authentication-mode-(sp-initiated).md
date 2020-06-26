# Obtaining an Unscoped Token in Federated Identity Authentication Mode \(SP Initiated\)<a name="en-us_topic_0057845629"></a>

## Function Description<a name="section42991548164730"></a>

This interface is used to obtain an unscoped token in SP-initiated federated identity authentication mode.

An unscoped token cannot be used for authentication. If a federated user needs to use a token for authentication, obtain the scoped token based on section  [Obtaining a Scoped Token in Federated Identity Authentication Mode](obtaining-a-scoped-token-in-federated-identity-authentication-mode.md).

## URI<a name="section999597164730"></a>

-   URI format

    GET /v3/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols/\{protocol\_id\}/auth


-   URI parameter description

    <a name="table45982210164832"></a>
    <table><thead align="left"><tr id="row34412857164832"><th class="cellrowborder" valign="top" width="17.16828317168283%" id="mcps1.1.5.1.1"><p id="p35978026164832"><a name="p35978026164832"></a><a name="p35978026164832"></a><strong id="b37426530113629_1"><a name="b37426530113629_1"></a><a name="b37426530113629_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.538046195380463%" id="mcps1.1.5.1.2"><p id="p28538959164832"><a name="p28538959164832"></a><a name="p28538959164832"></a><strong id="b842352706112524_1"><a name="b842352706112524_1"></a><a name="b842352706112524_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.308169183081695%" id="mcps1.1.5.1.3"><p id="p29954320164832"><a name="p29954320164832"></a><a name="p29954320164832"></a><strong id="b84235270615026_1"><a name="b84235270615026_1"></a><a name="b84235270615026_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.98550144985502%" id="mcps1.1.5.1.4"><p id="p10380887164832"><a name="p10380887164832"></a><a name="p10380887164832"></a><strong id="b14438018113629_1"><a name="b14438018113629_1"></a><a name="b14438018113629_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35545481164832"><td class="cellrowborder" valign="top" width="17.16828317168283%" headers="mcps1.1.5.1.1 "><p id="p60611728164832"><a name="p60611728164832"></a><a name="p60611728164832"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.538046195380463%" headers="mcps1.1.5.1.2 "><p id="p10602964164832"><a name="p10602964164832"></a><a name="p10602964164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.308169183081695%" headers="mcps1.1.5.1.3 "><p id="p53533756164832"><a name="p53533756164832"></a><a name="p53533756164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.98550144985502%" headers="mcps1.1.5.1.4 "><p id="p41266993164832"><a name="p41266993164832"></a><a name="p41266993164832"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row35858619164832"><td class="cellrowborder" valign="top" width="17.16828317168283%" headers="mcps1.1.5.1.1 "><p id="p18867054164832"><a name="p18867054164832"></a><a name="p18867054164832"></a>protocol _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.538046195380463%" headers="mcps1.1.5.1.2 "><p id="p51836385164832"><a name="p51836385164832"></a><a name="p51836385164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.308169183081695%" headers="mcps1.1.5.1.3 "><p id="p37997628164832"><a name="p37997628164832"></a><a name="p37997628164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.98550144985502%" headers="mcps1.1.5.1.4 "><p id="p57909032164832"><a name="p57909032164832"></a><a name="p57909032164832"></a>ID of a protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section30144898164730"></a>

-   Request header parameter description

    <a name="table56458564164645"></a>
    <table><thead align="left"><tr id="row38321014164645"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.1.5.1.1"><p id="p4891467164645"><a name="p4891467164645"></a><a name="p4891467164645"></a><strong id="b37426530113629_3"><a name="b37426530113629_3"></a><a name="b37426530113629_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.2"><p id="p60664507164645"><a name="p60664507164645"></a><a name="p60664507164645"></a><strong id="b842352706112524_3"><a name="b842352706112524_3"></a><a name="b842352706112524_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.61%" id="mcps1.1.5.1.3"><p id="p14878007164645"><a name="p14878007164645"></a><a name="p14878007164645"></a><strong id="b84235270615026_3"><a name="b84235270615026_3"></a><a name="b84235270615026_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.92%" id="mcps1.1.5.1.4"><p id="p64267944164645"><a name="p64267944164645"></a><a name="p64267944164645"></a><strong id="b14438018113629_3"><a name="b14438018113629_3"></a><a name="b14438018113629_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47522392164645"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.1.5.1.1 "><p id="p22387518164645"><a name="p22387518164645"></a><a name="p22387518164645"></a>Accept</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.2 "><p id="p1449685164645"><a name="p1449685164645"></a><a name="p1449685164645"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.3 "><p id="p50315689164645"><a name="p50315689164645"></a><a name="p50315689164645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.92%" headers="mcps1.1.5.1.4 "><a name="ul2066821281118"></a><a name="ul2066821281118"></a><ul id="ul2066821281118"><li>This parameter is not required when a token is obtained in the WebSSO mode.</li><li>When you obtain a token using the Enhanced Client Proxy (ECP), the value of this parameter is as follows:<p id="p585112176116"><a name="p585112176116"></a><a name="p585112176116"></a>application/vnd.paos+xml</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row45829305164645"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.1.5.1.1 "><p id="p25048351164645"><a name="p25048351164645"></a><a name="p25048351164645"></a>PAOS</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.2 "><p id="p15650549164645"><a name="p15650549164645"></a><a name="p15650549164645"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.3 "><p id="p59734927164645"><a name="p59734927164645"></a><a name="p59734927164645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.92%" headers="mcps1.1.5.1.4 "><a name="ul10681123417114"></a><a name="ul10681123417114"></a><ul id="ul10681123417114"><li>This parameter is not required when a token is obtained in the WebSSO mode.</li><li>When you obtain a token using the ECP, the value of this parameter is as follows:<p id="p60218117164645"><a name="p60218117164645"></a><a name="p60218117164645"></a>urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >1.  This interface can be used to obtain tokens through WebSSO and ECP. Different request headers are used to determine the method of obtaining a token. For details, see the parameter description of Request Header.  
    >2.  You are not advised to obtain a token by directly calling this interface. You are advised to obtain a token using OpenStackClient.  

-   Sample request

    ```
    GET /v3/OS-FEDERATION/identity_providers/idptest/protocols/saml/auth
    ```


## Response<a name="section5167254164730"></a>

-   Response body parameter description

    <a name="table30197476165124"></a>
    <table><thead align="left"><tr id="row25190343165124"><th class="cellrowborder" valign="top" width="16.951695169516952%" id="mcps1.1.5.1.1"><p id="p63550324165124"><a name="p63550324165124"></a><a name="p63550324165124"></a><strong id="b84235270616223"><a name="b84235270616223"></a><a name="b84235270616223"></a>Response Item</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.51195119511951%" id="mcps1.1.5.1.2"><p id="p47302590165124"><a name="p47302590165124"></a><a name="p47302590165124"></a><strong id="b37426530113629_5"><a name="b37426530113629_5"></a><a name="b37426530113629_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.941894189418942%" id="mcps1.1.5.1.3"><p id="p6304564165124"><a name="p6304564165124"></a><a name="p6304564165124"></a><strong id="b84235270615026_5"><a name="b84235270615026_5"></a><a name="b84235270615026_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.594459445944594%" id="mcps1.1.5.1.4"><p id="p40907712165124"><a name="p40907712165124"></a><a name="p40907712165124"></a><strong id="b14438018113629_5"><a name="b14438018113629_5"></a><a name="b14438018113629_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31669105165124"><td class="cellrowborder" valign="top" width="16.951695169516952%" headers="mcps1.1.5.1.1 "><p id="p27151923165124"><a name="p27151923165124"></a><a name="p27151923165124"></a>X-Subject-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.51195119511951%" headers="mcps1.1.5.1.2 "><p id="p51822188165124"><a name="p51822188165124"></a><a name="p51822188165124"></a>header</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.941894189418942%" headers="mcps1.1.5.1.3 "><p id="p36847705165124"><a name="p36847705165124"></a><a name="p36847705165124"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.594459445944594%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0026585112_p51812368"><a name="en-us_topic_0026585112_p51812368"></a><a name="en-us_topic_0026585112_p51812368"></a>Signed unscoped token.</p>
    </td>
    </tr>
    <tr id="row15598896165124"><td class="cellrowborder" valign="top" width="16.951695169516952%" headers="mcps1.1.5.1.1 "><p id="p16586493165124"><a name="p16586493165124"></a><a name="p16586493165124"></a>token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.51195119511951%" headers="mcps1.1.5.1.2 "><p id="p1328717165124"><a name="p1328717165124"></a><a name="p1328717165124"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.941894189418942%" headers="mcps1.1.5.1.3 "><p id="p40517270165124"><a name="p40517270165124"></a><a name="p40517270165124"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.594459445944594%" headers="mcps1.1.5.1.4 "><p id="p60673407165124"><a name="p60673407165124"></a><a name="p60673407165124"></a>Information of the unscoped token obtained in federated identity authentication mode, including methods and user information.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "token": {
            "issued_at": "2017-05-23T06:54:51.763000Z",
            "expires_at": "2017-05-24T06:54:51.763000Z",
            "methods": [
                "mapped"
            ],
            "user": {
                "domain": {
                    "id": "e31ac82d778b4d128cb6fed37fd72cdb",
                    "name": "exampledomain"
                },
                "id": "RMQTgtjjSNGDcKy7oUmI3AZg7GgsWG0Z",
                "name": "exampleuser",
                "OS-FEDERATION": {
                    "identity_provider": {
                        "id": "exampleuser"
                    },
                    "protocol": {
                        "id": "saml"
                    },
                    "groups": [
                        {
                            "id": "b40189e26ea44f959877621b4b298db5"
                        }
                    ]
                }
            }
        }
    }
    ```


## Status Code<a name="section33762092164730"></a>

<a name="table50374951164730"></a>
<table><thead align="left"><tr id="row57231606164730"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p5248518164730"><a name="p5248518164730"></a><a name="p5248518164730"></a><strong id="b842352706104328"><a name="b842352706104328"></a><a name="b842352706104328"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p22476794164730"><a name="p22476794164730"></a><a name="p22476794164730"></a><strong id="b14438018113629_7"><a name="b14438018113629_7"></a><a name="b14438018113629_7"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8681019164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p32073904164730"><a name="p32073904164730"></a><a name="p32073904164730"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p47849409164730"><a name="p47849409164730"></a><a name="p47849409164730"></a>The request is successful. You need to further obtain user information.</p>
</td>
</tr>
<tr id="row27991504164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p52719384164730"><a name="p52719384164730"></a><a name="p52719384164730"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p42411696164730"><a name="p42411696164730"></a><a name="p42411696164730"></a>The request is successful, and a token is returned.</p>
</td>
</tr>
<tr id="row46160945164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p48049093164730"><a name="p48049093164730"></a><a name="p48049093164730"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p66771325164730"><a name="p66771325164730"></a><a name="p66771325164730"></a>The system switches to the identity provider authentication page if the request does not carry user information of the identity provider.</p>
</td>
</tr>
<tr id="row64071018164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p22370004164730"><a name="p22370004164730"></a><a name="p22370004164730"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p31063164730"><a name="p31063164730"></a><a name="p31063164730"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row279569164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p22645099164730"><a name="p22645099164730"></a><a name="p22645099164730"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p22313713164730"><a name="p22313713164730"></a><a name="p22313713164730"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row66605697164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p26352373164730"><a name="p26352373164730"></a><a name="p26352373164730"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p54167498164730"><a name="p54167498164730"></a><a name="p54167498164730"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row17745440164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p28094569164730"><a name="p28094569164730"></a><a name="p28094569164730"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p61067622164730"><a name="p61067622164730"></a><a name="p61067622164730"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row12737692164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p25120131164730"><a name="p25120131164730"></a><a name="p25120131164730"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p21464722164730"><a name="p21464722164730"></a><a name="p21464722164730"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row58964777164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p11417608164730"><a name="p11417608164730"></a><a name="p11417608164730"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p52411044164730"><a name="p52411044164730"></a><a name="p52411044164730"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row1937348164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p22707461164730"><a name="p22707461164730"></a><a name="p22707461164730"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p27365047164730"><a name="p27365047164730"></a><a name="p27365047164730"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

