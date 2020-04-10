# Querying the Mapping List<a name="en-us_topic_0057845567"></a>

## Function Description<a name="section35784939102440"></a>

This interface is used to query the mapping list.

## URI<a name="section48981904102440"></a>

URI format

GET /v3/OS-FEDERATION/mappings

## Request<a name="section7527256102440"></a>

-   Request header parameter description

    <a name="table61314561102440"></a>
    <table><thead align="left"><tr id="row46720639102440"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p26275405102440"><a name="p26275405102440"></a><a name="p26275405102440"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p47933064102440"><a name="p47933064102440"></a><a name="p47933064102440"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p57372951102440"><a name="p57372951102440"></a><a name="p57372951102440"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p16697443102440"><a name="p16697443102440"></a><a name="p16697443102440"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10315603102440"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p30257487102440"><a name="p30257487102440"></a><a name="p30257487102440"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p34937408102440"><a name="p34937408102440"></a><a name="p34937408102440"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p11357838102440"><a name="p11357838102440"></a><a name="p11357838102440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p47569696102440"><a name="p47569696102440"></a><a name="p47569696102440"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row25474087102440"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p50135130102440"><a name="p50135130102440"></a><a name="p50135130102440"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p34413767102440"><a name="p34413767102440"></a><a name="p34413767102440"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p36051732102440"><a name="p36051732102440"></a><a name="p36051732102440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p34509161102440"><a name="p34509161102440"></a><a name="p34509161102440"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://10.185.190.118:31943/v3/OS-FEDERATION/mappings
    ```


## Response<a name="section43778671102440"></a>

-   Response body parameter description

    <a name="table5926316102440"></a>
    <table><thead align="left"><tr id="row15113921102440"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p16268089102440"><a name="p16268089102440"></a><a name="p16268089102440"></a><strong id="a3da1b7475f644c07832655d87318eb65"><a name="a3da1b7475f644c07832655d87318eb65"></a><a name="a3da1b7475f644c07832655d87318eb65"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p42646846102440"><a name="p42646846102440"></a><a name="p42646846102440"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p31842487102440"><a name="p31842487102440"></a><a name="p31842487102440"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p29104653102440"><a name="p29104653102440"></a><a name="p29104653102440"></a><strong id="b842352706114032_1"><a name="b842352706114032_1"></a><a name="b842352706114032_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8666663102440"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p30911085102440"><a name="p30911085102440"></a><a name="p30911085102440"></a>mappings</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p20769993102440"><a name="p20769993102440"></a><a name="p20769993102440"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p4647840102440"><a name="p4647840102440"></a><a name="p4647840102440"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p40930780102440"><a name="p40930780102440"></a><a name="p40930780102440"></a>List of mappings.</p>
    </td>
    </tr>
    <tr id="row32832708102440"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p42203666102440"><a name="p42203666102440"></a><a name="p42203666102440"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p63053752102440"><a name="p63053752102440"></a><a name="p63053752102440"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p7080287102440"><a name="p7080287102440"></a><a name="p7080287102440"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p36632366102440"><a name="p36632366102440"></a><a name="p36632366102440"></a>Resource links of mappings.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   mappings parameter description

    <a name="table471214210253"></a>
    <table><thead align="left"><tr id="row5835001710253"><th class="cellrowborder" valign="top" width="20.59%" id="mcps1.1.5.1.1"><p id="p2873092810253"><a name="p2873092810253"></a><a name="p2873092810253"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.310000000000002%" id="mcps1.1.5.1.2"><p id="p4550385610253"><a name="p4550385610253"></a><a name="p4550385610253"></a><strong id="b459260946"><a name="b459260946"></a><a name="b459260946"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.22%" id="mcps1.1.5.1.3"><p id="p6193373710253"><a name="p6193373710253"></a><a name="p6193373710253"></a><strong id="b425003497"><a name="b425003497"></a><a name="b425003497"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.88%" id="mcps1.1.5.1.4"><p id="p5057677010253"><a name="p5057677010253"></a><a name="p5057677010253"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
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
    <a name="ul14819125213392"></a><a name="ul14819125213392"></a><ul id="ul14819125213392"><li><strong id="b85947858"><a name="b85947858"></a><a name="b85947858"></a>user</strong>: indicates the name of a federated user in the cloud system. <strong id="b842352706114340"><a name="b842352706114340"></a><a name="b842352706114340"></a>{0}</strong> indicates the first attribute of the user information in <strong id="b842352706114418"><a name="b842352706114418"></a><a name="b842352706114418"></a>remote</strong>.</li><li><strong id="b1274653324"><a name="b1274653324"></a><a name="b1274653324"></a>group</strong>: indicates the user group to which a federated user belongs in the cloud system.</li></ul>
    <p id="p281920526391"><a name="p281920526391"></a><a name="p281920526391"></a><strong id="b842352706173126"><a name="b842352706173126"></a><a name="b842352706173126"></a>remote</strong>: indicates the information about a federated user in the IdP. This expression is a combination of assertion attributes and operators. The value of <strong id="b842352706173622"><a name="b842352706173622"></a><a name="b842352706173622"></a>remote</strong> is determined based on the assertion.</p>
    <a name="ul1054319873214"></a><a name="ul1054319873214"></a><ul id="ul1054319873214"><li><strong id="b35911621152914"><a name="b35911621152914"></a><a name="b35911621152914"></a>"type": "UserName"</strong> indicates an attribute in an IdP assertion.</li><li><strong id="b118011252134614"><a name="b118011252134614"></a><a name="b118011252134614"></a>"type": "orgPersonType"</strong> indicates an attribute in an IdP assertion.</li><li><strong id="b5252264151845"><a name="b5252264151845"></a><a name="b5252264151845"></a>not_any_of</strong>: The condition is valid only if the input attributes do not include specified value, and a Boolean value is returned. The returned value cannot be used to replace the placeholder in the <strong id="b23964722415913"><a name="b23964722415913"></a><a name="b23964722415913"></a>local</strong> block.</li></ul>
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
        "links": {
            "next": null,
            "previous": null,
            "self": "https://example.com/v3/OS-FEDERATION/mappings"
        },
        "mappings": [
            {
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
                                    "id": "0cd5e9"
                                }
                            }
                        ],
                        "remote": [
                            {
                                "type": "UserName"
                            },
                            {
                                "type": "orgPersonType",
                                "any_one_of": [
                                    "Contractor",
                                    "SubContractor"
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
    ```


## Status Codes<a name="section4712884102440"></a>

<a name="table46199306102440"></a>
<table><thead align="left"><tr id="row47553867102440"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p26658041102440"><a name="p26658041102440"></a><a name="p26658041102440"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p11817687102440"><a name="p11817687102440"></a><a name="p11817687102440"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17708557102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p25107012102440"><a name="p25107012102440"></a><a name="p25107012102440"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p20402083102440"><a name="p20402083102440"></a><a name="p20402083102440"></a>The request is successful.</p>
</td>
</tr>
<tr id="row49401026102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p42060145102440"><a name="p42060145102440"></a><a name="p42060145102440"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p51428573102440"><a name="p51428573102440"></a><a name="p51428573102440"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row60203973102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p44683606102440"><a name="p44683606102440"></a><a name="p44683606102440"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p62602328102440"><a name="p62602328102440"></a><a name="p62602328102440"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row26550042102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3069832102440"><a name="p3069832102440"></a><a name="p3069832102440"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p47329850102440"><a name="p47329850102440"></a><a name="p47329850102440"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row23315473102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p9505124102440"><a name="p9505124102440"></a><a name="p9505124102440"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p31717617102440"><a name="p31717617102440"></a><a name="p31717617102440"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row17023100102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p36693840102440"><a name="p36693840102440"></a><a name="p36693840102440"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p19411057102440"><a name="p19411057102440"></a><a name="p19411057102440"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row40481785102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p57799159102440"><a name="p57799159102440"></a><a name="p57799159102440"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p51220342102440"><a name="p51220342102440"></a><a name="p51220342102440"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row58329902102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p27101584102440"><a name="p27101584102440"></a><a name="p27101584102440"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p47744711102440"><a name="p47744711102440"></a><a name="p47744711102440"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row27049222102440"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p43503383102440"><a name="p43503383102440"></a><a name="p43503383102440"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p34113136102440"><a name="p34113136102440"></a><a name="p34113136102440"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

