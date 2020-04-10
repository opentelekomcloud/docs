# Obtaining an Unscoped Token in Federated Identity Authentication Mode \(IdP Initiated\)<a name="iam_02_0003"></a>

## Function Description<a name="section42991548164730"></a>

This interface is used to obtain an unscoped token in IdP-initiated federated identity authentication mode.

An unscoped token cannot be used for authentication. If a federated user needs to use a token for authentication, obtain the scoped token based on section  [Obtaining a Scoped Token in Federated Identity Authentication Mode](obtaining-a-scoped-token-in-federated-identity-authentication-mode.md).

## URI<a name="section999597164730"></a>

URI format

POST /v3.0/OS-FEDERATION/tokens

## Request<a name="section30144898164730"></a>

-   Request header parameter description

    <a name="table56458564164645"></a>
    <table><thead align="left"><tr id="row38321014164645"><th class="cellrowborder" valign="top" width="20.76%" id="mcps1.1.5.1.1"><p id="p4891467164645"><a name="p4891467164645"></a><a name="p4891467164645"></a><strong id="b37426530113629_1"><a name="b37426530113629_1"></a><a name="b37426530113629_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.1.5.1.2"><p id="p60664507164645"><a name="p60664507164645"></a><a name="p60664507164645"></a><strong id="b842352706112524_1"><a name="b842352706112524_1"></a><a name="b842352706112524_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.5.1.3"><p id="p14878007164645"><a name="p14878007164645"></a><a name="p14878007164645"></a><strong id="b84235270615026_1"><a name="b84235270615026_1"></a><a name="b84235270615026_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.46%" id="mcps1.1.5.1.4"><p id="p64267944164645"><a name="p64267944164645"></a><a name="p64267944164645"></a><strong id="b14438018113629_1"><a name="b14438018113629_1"></a><a name="b14438018113629_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16522014164645"><td class="cellrowborder" valign="top" width="20.76%" headers="mcps1.1.5.1.1 "><p id="p16994440164645"><a name="p16994440164645"></a><a name="p16994440164645"></a>X-Idp-Id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.2 "><p id="p34372423164645"><a name="p34372423164645"></a><a name="p34372423164645"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.3 "><p id="p32702874164645"><a name="p32702874164645"></a><a name="p32702874164645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.5.1.4 "><p id="p45605165175031"><a name="p45605165175031"></a><a name="p45605165175031"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row27958398103142"><td class="cellrowborder" valign="top" width="20.76%" headers="mcps1.1.5.1.1 "><p id="p50037738103142"><a name="p50037738103142"></a><a name="p50037738103142"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.2 "><p id="p26525003103142"><a name="p26525003103142"></a><a name="p26525003103142"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.3 "><p id="p1041673103142"><a name="p1041673103142"></a><a name="p1041673103142"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.5.1.4 "><p id="p61308811103259"><a name="p61308811103259"></a><a name="p61308811103259"></a>The client must transfer the SAMLResponse parameter to the server by using the form data submitted by the browser. Therefore, the value of this parameter must be:</p>
    <p id="p17266699103142"><a name="p17266699103142"></a><a name="p17266699103142"></a>application/x-www-form-urlencoded</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table58447617102532"></a>
    <table><thead align="left"><tr id="row28600734102532"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.1.5.1.1"><p id="p34958131102532"><a name="p34958131102532"></a><a name="p34958131102532"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.27%" id="mcps1.1.5.1.2"><p id="p13036348102532"><a name="p13036348102532"></a><a name="p13036348102532"></a><strong id="b842352706112524_3"><a name="b842352706112524_3"></a><a name="b842352706112524_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.63%" id="mcps1.1.5.1.3"><p id="p49311266102532"><a name="p49311266102532"></a><a name="p49311266102532"></a><strong id="b84235270615026_3"><a name="b84235270615026_3"></a><a name="b84235270615026_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.480000000000004%" id="mcps1.1.5.1.4"><p id="p34789580102532"><a name="p34789580102532"></a><a name="p34789580102532"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66492578102532"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="p17189774102532"><a name="p17189774102532"></a><a name="p17189774102532"></a>SAMLResponse</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.27%" headers="mcps1.1.5.1.2 "><p id="p50194421102532"><a name="p50194421102532"></a><a name="p50194421102532"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.3 "><p id="p492243151519"><a name="p492243151519"></a><a name="p492243151519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p52716491103542"><a name="p52716491103542"></a><a name="p52716491103542"></a>Response body returned when IdP authentication is successful.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This interface can only be called on the CLI side. The client needs to obtain SAMLResponse in IdP-initiated federated identity authentication mode and obtain an unscoped token by using the form data submitted by the browser.  

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'x-Idp-Id:test_local_idp' -H 'Content-Type:application/x-www-form-urlencoded' -X POST -d 'SAMLResponse=PD94bWwgdmVyc2lvbj0iMS4wIiBl4WXZ1OGNmYmRzWk1ZeWlLKy96anpEbm1rT2FrVVBrUmlSWEpLYUt5NzJtUmtoRFBCNjgwVQpzalU3R2hKNHE4ZG48L3hlbmM6Q2lwaGVyVmFsdWU%2BPC94ZW5jOkNpcGhlckRhdGE%2BPC94ZW5jOkVuY3J5cHRlZERhdGE%2BPC9zYW1sMjpFbmNyeXB0ZWRBc3NlcnRpb24%2BPC9zYW1sMnA6UmVzcG9uc2U%2B' https://iam.example.com/v3.0/OS-FEDERATION/tokens
    ```


## Response<a name="section5167254164730"></a>

-   Response body parameter description

    <a name="table30197476165124"></a>
    <table><thead align="left"><tr id="row25190343165124"><th class="cellrowborder" valign="top" width="20.54%" id="mcps1.1.5.1.1"><p id="p63550324165124"><a name="p63550324165124"></a><a name="p63550324165124"></a><strong id="b84235270616223"><a name="b84235270616223"></a><a name="b84235270616223"></a>Response Item</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.39%" id="mcps1.1.5.1.2"><p id="p47302590165124"><a name="p47302590165124"></a><a name="p47302590165124"></a><strong id="b37426530113629_3"><a name="b37426530113629_3"></a><a name="b37426530113629_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.94%" id="mcps1.1.5.1.3"><p id="p6304564165124"><a name="p6304564165124"></a><a name="p6304564165124"></a><strong id="b84235270615026_5"><a name="b84235270615026_5"></a><a name="b84235270615026_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.13%" id="mcps1.1.5.1.4"><p id="p40907712165124"><a name="p40907712165124"></a><a name="p40907712165124"></a><strong id="b14438018113629_3"><a name="b14438018113629_3"></a><a name="b14438018113629_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31669105165124"><td class="cellrowborder" valign="top" width="20.54%" headers="mcps1.1.5.1.1 "><p id="p27151923165124"><a name="p27151923165124"></a><a name="p27151923165124"></a>X-Subject-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.5.1.2 "><p id="p51822188165124"><a name="p51822188165124"></a><a name="p51822188165124"></a>header</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.1.5.1.3 "><p id="p36847705165124"><a name="p36847705165124"></a><a name="p36847705165124"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0026585112_p51812368"><a name="en-us_topic_0026585112_p51812368"></a><a name="en-us_topic_0026585112_p51812368"></a>Signed unscoped token.</p>
    </td>
    </tr>
    <tr id="row15598896165124"><td class="cellrowborder" valign="top" width="20.54%" headers="mcps1.1.5.1.1 "><p id="p16586493165124"><a name="p16586493165124"></a><a name="p16586493165124"></a>token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.39%" headers="mcps1.1.5.1.2 "><p id="p1328717165124"><a name="p1328717165124"></a><a name="p1328717165124"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.1.5.1.3 "><p id="p40517270165124"><a name="p40517270165124"></a><a name="p40517270165124"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.1.5.1.4 "><p id="p60673407165124"><a name="p60673407165124"></a><a name="p60673407165124"></a>Information of the unscoped token obtained in federated identity authentication mode, including methods and user information.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "token": {
            "expires_at": "2018-03-13T03:00:01.168000Z",
            "methods": ["mapped"],
            "issued_at": "2018-03-12T03:00:01.168000Z",
            "user": {
                "OS-FEDERATION": {
                    "identity_provider": {
                        "id": "test_local_idp"
                    },
                    "protocol": {
                        "id": "saml"
                    },
                    "groups": [{
                        "name": "admin",
                        "id": "45a8c8f1894444e9a016af065e152b91"
                    }]
                },
                "domain": {
                    "name": "hansheng",
                    "id": "c0e20cc993a24ad4aa3251661ef37c87"
                },
                "name": "FederationUser",
                "id": "QNSzD0bycqUXE4hiRNfyFcWfoOs8z6gT"
            }
        }
    }
    ```


## Status Code<a name="section33762092164730"></a>

<a name="table50374951164730"></a>
<table><thead align="left"><tr id="row57231606164730"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p5248518164730"><a name="p5248518164730"></a><a name="p5248518164730"></a><strong id="b842352706104328"><a name="b842352706104328"></a><a name="b842352706104328"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p22476794164730"><a name="p22476794164730"></a><a name="p22476794164730"></a><strong id="b14438018113629_5"><a name="b14438018113629_5"></a><a name="b14438018113629_5"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row27991504164730"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p52719384164730"><a name="p52719384164730"></a><a name="p52719384164730"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p42411696164730"><a name="p42411696164730"></a><a name="p42411696164730"></a>The request is successful, and a token is returned.</p>
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

