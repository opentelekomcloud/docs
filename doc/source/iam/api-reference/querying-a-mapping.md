# Querying a Mapping<a name="en-us_topic_0057845645"></a>

## Function Description<a name="section544449010253"></a>

This interface is used to query the information about a mapping.

## URI<a name="section961061110253"></a>

-   URI format

    GET /v3/OS-FEDERATION/mappings/\{id\}


-   URI parameter description

    <a name="table3295831810253"></a>
    <table><thead align="left"><tr id="row2859289710253"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.1"><p id="p3432335410253"><a name="p3432335410253"></a><a name="p3432335410253"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.360000000000003%" id="mcps1.1.5.1.2"><p id="p2872829510253"><a name="p2872829510253"></a><a name="p2872829510253"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.1.5.1.3"><p id="p4529057710253"><a name="p4529057710253"></a><a name="p4529057710253"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.92%" id="mcps1.1.5.1.4"><p id="p4465811110253"><a name="p4465811110253"></a><a name="p4465811110253"></a><strong id="b842352706114032_1_1"><a name="b842352706114032_1_1"></a><a name="b842352706114032_1_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6053724210253"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p456954510253"><a name="p456954510253"></a><a name="p456954510253"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.2 "><p id="p3458885310253"><a name="p3458885310253"></a><a name="p3458885310253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.3 "><p id="p5023366910253"><a name="p5023366910253"></a><a name="p5023366910253"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.1.5.1.4 "><p id="p4239536110253"><a name="p4239536110253"></a><a name="p4239536110253"></a>Mapping ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1147224210253"></a>

-   Request header parameter description

    <a name="table4034958610253"></a>
    <table><thead align="left"><tr id="row2407090210253"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.1.5.1.1"><p id="p358602710253"><a name="p358602710253"></a><a name="p358602710253"></a><strong id="a3da1b7475f644c07832655d87318eb65"><a name="a3da1b7475f644c07832655d87318eb65"></a><a name="a3da1b7475f644c07832655d87318eb65"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.360000000000003%" id="mcps1.1.5.1.2"><p id="p2203278510253"><a name="p2203278510253"></a><a name="p2203278510253"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.1.5.1.3"><p id="p3982516710253"><a name="p3982516710253"></a><a name="p3982516710253"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.79%" id="mcps1.1.5.1.4"><p id="p461313410253"><a name="p461313410253"></a><a name="p461313410253"></a><strong id="b842352706114032_1_3"><a name="b842352706114032_1_3"></a><a name="b842352706114032_1_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3811960610253"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="p68036610253"><a name="p68036610253"></a><a name="p68036610253"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.2 "><p id="p5510966210253"><a name="p5510966210253"></a><a name="p5510966210253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.3 "><p id="p3469764710253"><a name="p3469764710253"></a><a name="p3469764710253"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.79%" headers="mcps1.1.5.1.4 "><p id="p5904602410253"><a name="p5904602410253"></a><a name="p5904602410253"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row6165217610253"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="p2777034510253"><a name="p2777034510253"></a><a name="p2777034510253"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.2 "><p id="p3480547110253"><a name="p3480547110253"></a><a name="p3480547110253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.3 "><p id="p67087310253"><a name="p67087310253"></a><a name="p67087310253"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.79%" headers="mcps1.1.5.1.4 "><p id="p5434073510253"><a name="p5434073510253"></a><a name="p5434073510253"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://10.185.190.118:31943/v3/OS-FEDERATION/mappings/ACME
    ```


## Response<a name="section3952345110253"></a>

-   Response body parameter description

    <a name="table471214210253"></a>
    <table><thead align="left"><tr id="row5835001710253"><th class="cellrowborder" valign="top" width="20.59%" id="mcps1.1.5.1.1"><p id="p2873092810253"><a name="p2873092810253"></a><a name="p2873092810253"></a><strong id="b6477496310452"><a name="b6477496310452"></a><a name="b6477496310452"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.310000000000002%" id="mcps1.1.5.1.2"><p id="p4550385610253"><a name="p4550385610253"></a><a name="p4550385610253"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.22%" id="mcps1.1.5.1.3"><p id="p6193373710253"><a name="p6193373710253"></a><a name="p6193373710253"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.88%" id="mcps1.1.5.1.4"><p id="p5057677010253"><a name="p5057677010253"></a><a name="p5057677010253"></a><strong id="b842352706114032_3"><a name="b842352706114032_3"></a><a name="b842352706114032_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row307766710253"><td class="cellrowborder" valign="top" width="20.59%" headers="mcps1.1.5.1.1 "><p id="p4796446910253"><a name="p4796446910253"></a><a name="p4796446910253"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p5991676710253"><a name="p5991676710253"></a><a name="p5991676710253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.1.5.1.3 "><p id="p2141997810253"><a name="p2141997810253"></a><a name="p2141997810253"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.88%" headers="mcps1.1.5.1.4 "><p id="p5729667010253"><a name="p5729667010253"></a><a name="p5729667010253"></a>Mapping ID.</p>
    </td>
    </tr>
    <tr id="row4590798210253"><td class="cellrowborder" valign="top" width="20.59%" headers="mcps1.1.5.1.1 "><p id="p2755905710253"><a name="p2755905710253"></a><a name="p2755905710253"></a>rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p1769115310253"><a name="p1769115310253"></a><a name="p1769115310253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.1.5.1.3 "><p id="p1194883210253"><a name="p1194883210253"></a><a name="p1194883210253"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.88%" headers="mcps1.1.5.1.4 "><p id="p2833135010253"><a name="p2833135010253"></a><a name="p2833135010253"></a>List of rules used to map federated users into local users.</p>
    <p id="p6647203593911"><a name="p6647203593911"></a><a name="p6647203593911"></a>Example:</p>
    <pre class="screen" id="screen4220213569"><a name="screen4220213569"></a><a name="screen4220213569"></a> "rules": [
                {
                    "local": [
                        {
                            "user": {
                                "name": "{0}"
                            }
                        },
                        {
                            "group": {
                                "name": "0cd5e9"
                            }
                        }
                    ],
                    "remote": [
                        {
                            "type": "UserName"
                        },
                        {
                            "type": "orgPersonType",
                            "not_any_of": [
                                "Contractor",
                                "Guest"
                            ]
                        }
                    ]
                }
            ]</pre>
    <p id="p13647153563918"><a name="p13647153563918"></a><a name="p13647153563918"></a><strong id="b84235270617449"><a name="b84235270617449"></a><a name="b84235270617449"></a>local</strong>: indicates the information about a federated user in the cloud system.</p>
    <a name="ul14819125213392"></a><a name="ul14819125213392"></a><ul id="ul14819125213392"><li><strong id="b1866852693"><a name="b1866852693"></a><a name="b1866852693"></a>user</strong>: indicates the name of a federated user in the cloud system. <strong id="b842352706114340"><a name="b842352706114340"></a><a name="b842352706114340"></a>{0}</strong> indicates the first attribute of the user information in <strong id="b842352706114418"><a name="b842352706114418"></a><a name="b842352706114418"></a>remote</strong>.</li><li><strong id="b841764726"><a name="b841764726"></a><a name="b841764726"></a>group</strong>: indicates the user group to which a federated user belongs in the cloud system.</li></ul>
    <p id="p281920526391"><a name="p281920526391"></a><a name="p281920526391"></a><strong id="b842352706173126"><a name="b842352706173126"></a><a name="b842352706173126"></a>remote</strong>: indicates the information about a federated user in the IdP. This expression is a combination of assertion attributes and operators. The value of <strong id="b842352706173622"><a name="b842352706173622"></a><a name="b842352706173622"></a>remote</strong> is determined based on the assertion.</p>
    <a name="ul1781965216394"></a><a name="ul1781965216394"></a><ul id="ul1781965216394"><li><strong id="b182381822311435"><a name="b182381822311435"></a><a name="b182381822311435"></a>"type": "UserName" </strong>indicates an attribute in an IdP assertion.</li><li><strong id="b164475247511438"><a name="b164475247511438"></a><a name="b164475247511438"></a>"type": "orgPersonType"</strong> indicates an attribute in an IdP assertion.</li><li><strong id="b5252264151845"><a name="b5252264151845"></a><a name="b5252264151845"></a>not_any_of</strong>: The condition is valid only if the input attributes do not include specified value, and a Boolean value is returned. The returned value cannot be used to replace the placeholder in the <strong id="b23964722415913"><a name="b23964722415913"></a><a name="b23964722415913"></a>local</strong> block.</li></ul>
    </td>
    </tr>
    <tr id="row5365556310253"><td class="cellrowborder" valign="top" width="20.59%" headers="mcps1.1.5.1.1 "><p id="p5113332410253"><a name="p5113332410253"></a><a name="p5113332410253"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p4815861110253"><a name="p4815861110253"></a><a name="p4815861110253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.22%" headers="mcps1.1.5.1.3 "><p id="p853338110253"><a name="p853338110253"></a><a name="p853338110253"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.88%" headers="mcps1.1.5.1.4 "><p id="p2011527610253"><a name="p2011527610253"></a><a name="p2011527610253"></a>Resource links of mappings.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "mapping": {
            "id": "ACME",
            "links": {
                "self": "https://example.com/v3/OS-FEDERATION/mappings/ACME"
            },
            "rules": [
                {
                    "local": [
                        {
                            "user": {
                                "name": "{0}"
                            }
                        },
                        {
                            "group": {
                                "name": "0cd5e9"
                            }
                        }
                    ],
                    "remote": [
                        {
                            "type": "UserName"
                        },
                        {
                            "type": "orgPersonType",
                            "not_any_of": [
                                "Contractor",
                                "Guest"
                            ]
                        }
                    ]
                }
            ]
        }
    }
    ```


## Status Codes<a name="section5627758010253"></a>

<a name="table6219017010253"></a>
<table><thead align="left"><tr id="row323840610253"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p6098437110253"><a name="p6098437110253"></a><a name="p6098437110253"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p4078700810253"><a name="p4078700810253"></a><a name="p4078700810253"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1541333310253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4052047510253"><a name="p4052047510253"></a><a name="p4052047510253"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6093304910253"><a name="p6093304910253"></a><a name="p6093304910253"></a>The request is successful.</p>
</td>
</tr>
<tr id="row1152653710253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6123433610253"><a name="p6123433610253"></a><a name="p6123433610253"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6103414610253"><a name="p6103414610253"></a><a name="p6103414610253"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row1243640810253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p71610410253"><a name="p71610410253"></a><a name="p71610410253"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5800447310253"><a name="p5800447310253"></a><a name="p5800447310253"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row5227821310253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p667687410253"><a name="p667687410253"></a><a name="p667687410253"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p395590710253"><a name="p395590710253"></a><a name="p395590710253"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row3560316710253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6528425810253"><a name="p6528425810253"></a><a name="p6528425810253"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5353351710253"><a name="p5353351710253"></a><a name="p5353351710253"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row1203960910253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3568430910253"><a name="p3568430910253"></a><a name="p3568430910253"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p474788410253"><a name="p474788410253"></a><a name="p474788410253"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row4273096210253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3865592010253"><a name="p3865592010253"></a><a name="p3865592010253"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4412179010253"><a name="p4412179010253"></a><a name="p4412179010253"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row6155179010253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1963911210253"><a name="p1963911210253"></a><a name="p1963911210253"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4726423010253"><a name="p4726423010253"></a><a name="p4726423010253"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row2272489010253"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2877682610253"><a name="p2877682610253"></a><a name="p2877682610253"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4922158710253"><a name="p4922158710253"></a><a name="p4922158710253"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

