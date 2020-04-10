# Generating an AK/SK in Federated Identity Authentication Mode<a name="en-us_topic_0076897091"></a>

## Function Description<a name="section42991548164730"></a>

This interface is used to generate an AK/SK in federated identity authentication mode. This interface has been deprecated.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This interface has been deprecated and is replaced by the /v3.0/OS-CREDENTIAL/securitytokens interface. For details, see  [Obtaining a Temporary AK/SK](obtaining-a-temporary-ak-sk.md).  
>Before obtaining a temporary AK/SK in federated identity authentication mode, you need to establish a relationship of trust between the enterprise IdP and IAM. For details about how to query the metadata file, see  [Querying the Metadata File of Keystone](querying-the-metadata-file-of-keystone.md).  

## URI<a name="section999597164730"></a>

-   URI format

    GET /v3-ext/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols/\{protocol\_id\}/credential


-   URI parameter description

    <a name="table45982210164832"></a>
    <table><thead align="left"><tr id="row34412857164832"><th class="cellrowborder" valign="top" width="19.16%" id="mcps1.1.5.1.1"><p id="p35978026164832"><a name="p35978026164832"></a><a name="p35978026164832"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.21%" id="mcps1.1.5.1.2"><p id="p28538959164832"><a name="p28538959164832"></a><a name="p28538959164832"></a><strong id="ac429376f11ae472b87ff4be326afb9d8_1"><a name="ac429376f11ae472b87ff4be326afb9d8_1"></a><a name="ac429376f11ae472b87ff4be326afb9d8_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.63%" id="mcps1.1.5.1.3"><p id="p29954320164832"><a name="p29954320164832"></a><a name="p29954320164832"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43%" id="mcps1.1.5.1.4"><p id="p10380887164832"><a name="p10380887164832"></a><a name="p10380887164832"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35545481164832"><td class="cellrowborder" valign="top" width="19.16%" headers="mcps1.1.5.1.1 "><p id="p60611728164832"><a name="p60611728164832"></a><a name="p60611728164832"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.21%" headers="mcps1.1.5.1.2 "><p id="p10602964164832"><a name="p10602964164832"></a><a name="p10602964164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.63%" headers="mcps1.1.5.1.3 "><p id="p53533756164832"><a name="p53533756164832"></a><a name="p53533756164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p41266993164832"><a name="p41266993164832"></a><a name="p41266993164832"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row35858619164832"><td class="cellrowborder" valign="top" width="19.16%" headers="mcps1.1.5.1.1 "><p id="p18867054164832"><a name="p18867054164832"></a><a name="p18867054164832"></a>protocol _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.21%" headers="mcps1.1.5.1.2 "><p id="p51836385164832"><a name="p51836385164832"></a><a name="p51836385164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.63%" headers="mcps1.1.5.1.3 "><p id="p37997628164832"><a name="p37997628164832"></a><a name="p37997628164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p57909032164832"><a name="p57909032164832"></a><a name="p57909032164832"></a>ID of a protocol.</p>
    </td>
    </tr>
    <tr id="row167761518163"><td class="cellrowborder" valign="top" width="19.16%" headers="mcps1.1.5.1.1 "><p id="p7777135151615"><a name="p7777135151615"></a><a name="p7777135151615"></a>duration_seconds</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.21%" headers="mcps1.1.5.1.2 "><p id="p2077717513163"><a name="p2077717513163"></a><a name="p2077717513163"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.63%" headers="mcps1.1.5.1.3 "><p id="p1877718517165"><a name="p1877718517165"></a><a name="p1877718517165"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p14777115161610"><a name="p14777115161610"></a><a name="p14777115161610"></a>Validity period of an AK/SK, in seconds. The value is an integer ranging from 900 to 86400. The default value is 900.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section30144898164730"></a>

-   Request header parameter description

    <a name="table56458564164645"></a>
    <table><thead align="left"><tr id="row38321014164645"><th class="cellrowborder" valign="top" width="18.709999999999997%" id="mcps1.1.5.1.1"><p id="p4891467164645"><a name="p4891467164645"></a><a name="p4891467164645"></a><strong id="b666820712613"><a name="b666820712613"></a><a name="b666820712613"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.56%" id="mcps1.1.5.1.2"><p id="p60664507164645"><a name="p60664507164645"></a><a name="p60664507164645"></a><strong id="ac429376f11ae472b87ff4be326afb9d8_3"><a name="ac429376f11ae472b87ff4be326afb9d8_3"></a><a name="ac429376f11ae472b87ff4be326afb9d8_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.27%" id="mcps1.1.5.1.3"><p id="p14878007164645"><a name="p14878007164645"></a><a name="p14878007164645"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.46%" id="mcps1.1.5.1.4"><p id="p64267944164645"><a name="p64267944164645"></a><a name="p64267944164645"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16522014164645"><td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.1.5.1.1 "><p id="p16994440164645"><a name="p16994440164645"></a><a name="p16994440164645"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.2 "><p id="p34372423164645"><a name="p34372423164645"></a><a name="p34372423164645"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.5.1.3 "><p id="p32702874164645"><a name="p32702874164645"></a><a name="p32702874164645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.5.1.4 "><p id="p45605165175031"><a name="p45605165175031"></a><a name="p45605165175031"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row39770204164645"><td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.1.5.1.1 "><p id="p14480401164645"><a name="p14480401164645"></a><a name="p14480401164645"></a>protocol_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.2 "><p id="p32061847164645"><a name="p32061847164645"></a><a name="p32061847164645"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.5.1.3 "><p id="p46872821164645"><a name="p46872821164645"></a><a name="p46872821164645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.5.1.4 "><p id="p27278016175031"><a name="p27278016175031"></a><a name="p27278016175031"></a>ID of a protocol.</p>
    </td>
    </tr>
    <tr id="row47522392164645"><td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.1.5.1.1 "><p id="p22387518164645"><a name="p22387518164645"></a><a name="p22387518164645"></a>Accept</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.2 "><p id="p1449685164645"><a name="p1449685164645"></a><a name="p1449685164645"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.5.1.3 "><p id="p50315689164645"><a name="p50315689164645"></a><a name="p50315689164645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.5.1.4 "><a name="ul53876911451"></a><a name="ul53876911451"></a><ul id="ul53876911451"><li>This parameter is not required when a token is obtained in the WebSSO mode.</li><li>When you obtain a token using the ECP, the value of this parameter is as follows:<p id="p38697902164645"><a name="p38697902164645"></a><a name="p38697902164645"></a>application/vnd.paos+xml</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row45829305164645"><td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.1.5.1.1 "><p id="p25048351164645"><a name="p25048351164645"></a><a name="p25048351164645"></a>PAOS</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.2 "><p id="p15650549164645"><a name="p15650549164645"></a><a name="p15650549164645"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.5.1.3 "><p id="p59734927164645"><a name="p59734927164645"></a><a name="p59734927164645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.46%" headers="mcps1.1.5.1.4 "><a name="ul9899615114516"></a><a name="ul9899615114516"></a><ul id="ul9899615114516"><li>This parameter is not required when a token is obtained in the WebSSO mode.</li><li>When you obtain a token using the ECP, the value of this parameter is as follows:<p id="p60218117164645"><a name="p60218117164645"></a><a name="p60218117164645"></a>urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This interface can be used to obtain a token using the Web Single Sign-On \(WebSSO\) or ECP. The two mechanisms are differentiated based on request headers. For details, see the request header parameter description.  

-   Sample request

    ```
    GET /v3-ext/OS-FEDERATION/identity_providers/idptest/protocols/saml/credential
    ```


## **Response**<a name="section5167254164730"></a>

-   Response body parameter description

    <a name="table30197476165124"></a>
    <table><thead align="left"><tr id="row25190343165124"><th class="cellrowborder" valign="top" width="19.08%" id="mcps1.1.5.1.1"><p id="p63550324165124"><a name="p63550324165124"></a><a name="p63550324165124"></a><strong id="b84235270616223"><a name="b84235270616223"></a><a name="b84235270616223"></a>Response Item</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.32%" id="mcps1.1.5.1.2"><p id="p47302590165124"><a name="p47302590165124"></a><a name="p47302590165124"></a><strong id="b3439863412613"><a name="b3439863412613"></a><a name="b3439863412613"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.07%" id="mcps1.1.5.1.3"><p id="p6304564165124"><a name="p6304564165124"></a><a name="p6304564165124"></a><strong id="b4499812012613"><a name="b4499812012613"></a><a name="b4499812012613"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.53%" id="mcps1.1.5.1.4"><p id="p40907712165124"><a name="p40907712165124"></a><a name="p40907712165124"></a><strong id="b5450417912613"><a name="b5450417912613"></a><a name="b5450417912613"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15598896165124"><td class="cellrowborder" valign="top" width="19.08%" headers="mcps1.1.5.1.1 "><p id="p16586493165124"><a name="p16586493165124"></a><a name="p16586493165124"></a>credential</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p1328717165124"><a name="p1328717165124"></a><a name="p1328717165124"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.07%" headers="mcps1.1.5.1.3 "><p id="p40517270165124"><a name="p40517270165124"></a><a name="p40517270165124"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.53%" headers="mcps1.1.5.1.4 "><p id="p630173981713"><a name="p630173981713"></a><a name="p630173981713"></a>Credential obtained in federation authentication mode, including the AK/SK and security token.</p>
    <p id="p730133916177"><a name="p730133916177"></a><a name="p730133916177"></a>The default validity period of the AK/SK and security token is 900 ms.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "credential": {
            "access": "9KDZ9C4FZWDT4R2FCLYT", 
            "secret": "An7Qo7j7jmKduupYaJDZd1s2oxFkfujkD23fr3uO", 
            "expires_at": "2017-09-14T09:35:22.002000Z", 
            "securitytoken": "gAAAAABZuPvamyED44aYAZgdSvxxareklLGR9V4TwrsGNacjbs_8Z7CUtYdoI39-RzebqX55VkMZ46HpbaETlrSXqP1Wcdq-scxRt7WfCCV0CH987zruTPeb8Hd0Hb0fYZzi-OZO9lfIluQuHp8OUF2KwYliQFGIZMdwrgrHQCOg-49CbzhgGj4H2SCaMKT9VkpF9dquNgvoDG5a_j-_q1pMsoRJMrQyAZwt1vAYEadZ4gEklNprre0KS4D5wefTxsF_BQJfF-wCgeSTc9ggV0zld1t2G0qR5g=="
        }
    }
    ```


## **Status Codes**<a name="section33762092164730"></a>

<a name="table50374951164730"></a>
<table><thead align="left"><tr id="row57231606164730"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p5248518164730"><a name="p5248518164730"></a><a name="p5248518164730"></a><strong id="b1628046712613"><a name="b1628046712613"></a><a name="b1628046712613"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p22476794164730"><a name="p22476794164730"></a><a name="p22476794164730"></a><strong id="b5730084712613"><a name="b5730084712613"></a><a name="b5730084712613"></a>Description</strong></p>
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
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p42411696164730"><a name="p42411696164730"></a><a name="p42411696164730"></a>The request is successful, and an AK/SK is returned.</p>
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

