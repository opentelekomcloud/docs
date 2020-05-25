# Updating a Mapping<a name="en-us_topic_0057845568"></a>

## Function Description<a name="section3117386102532"></a>

This interface is used to update the information about a mapping.

## URI<a name="section57982316102532"></a>

-   URI format

    PATCH /v3/OS-FEDERATION/mappings/\{id\}


-   URI parameter description

    <a name="table39449429102532"></a>
    <table><thead align="left"><tr id="row37771956102532"><th class="cellrowborder" valign="top" width="20.61793820617938%" id="mcps1.1.5.1.1"><p id="p39629605102532"><a name="p39629605102532"></a><a name="p39629605102532"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.63833616638336%" id="mcps1.1.5.1.2"><p id="p55881438102532"><a name="p55881438102532"></a><a name="p55881438102532"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.03829617038296%" id="mcps1.1.5.1.3"><p id="p30102664102532"><a name="p30102664102532"></a><a name="p30102664102532"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.7054294570543%" id="mcps1.1.5.1.4"><p id="p22396747102532"><a name="p22396747102532"></a><a name="p22396747102532"></a><strong id="b842352706114032_1"><a name="b842352706114032_1"></a><a name="b842352706114032_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2197198102532"><td class="cellrowborder" valign="top" width="20.61793820617938%" headers="mcps1.1.5.1.1 "><p id="p43755321102532"><a name="p43755321102532"></a><a name="p43755321102532"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.63833616638336%" headers="mcps1.1.5.1.2 "><p id="p54520117102532"><a name="p54520117102532"></a><a name="p54520117102532"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.03829617038296%" headers="mcps1.1.5.1.3 "><p id="p54053353102532"><a name="p54053353102532"></a><a name="p54053353102532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.7054294570543%" headers="mcps1.1.5.1.4 "><p id="p16245502102532"><a name="p16245502102532"></a><a name="p16245502102532"></a>Mapping ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section40817308102532"></a>

-   Request header parameter description

    <a name="table37991568102532"></a>
    <table><thead align="left"><tr id="row11339356102532"><th class="cellrowborder" valign="top" width="20.45204520452045%" id="mcps1.1.5.1.1"><p id="p46072632102532"><a name="p46072632102532"></a><a name="p46072632102532"></a><strong id="b23760327204310"><a name="b23760327204310"></a><a name="b23760327204310"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.04170417041704%" id="mcps1.1.5.1.2"><p id="p40895672102532"><a name="p40895672102532"></a><a name="p40895672102532"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.84168416841684%" id="mcps1.1.5.1.3"><p id="p24215108102532"><a name="p24215108102532"></a><a name="p24215108102532"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.664566456645666%" id="mcps1.1.5.1.4"><p id="p15266757102532"><a name="p15266757102532"></a><a name="p15266757102532"></a><strong id="b34823772204310"><a name="b34823772204310"></a><a name="b34823772204310"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28647843102532"><td class="cellrowborder" valign="top" width="20.45204520452045%" headers="mcps1.1.5.1.1 "><p id="p38773957102532"><a name="p38773957102532"></a><a name="p38773957102532"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04170417041704%" headers="mcps1.1.5.1.2 "><p id="p53682836102532"><a name="p53682836102532"></a><a name="p53682836102532"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.84168416841684%" headers="mcps1.1.5.1.3 "><p id="p53342455102532"><a name="p53342455102532"></a><a name="p53342455102532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.664566456645666%" headers="mcps1.1.5.1.4 "><p id="p25771607102532"><a name="p25771607102532"></a><a name="p25771607102532"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row30617873102532"><td class="cellrowborder" valign="top" width="20.45204520452045%" headers="mcps1.1.5.1.1 "><p id="p64128630102532"><a name="p64128630102532"></a><a name="p64128630102532"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04170417041704%" headers="mcps1.1.5.1.2 "><p id="p27036556102532"><a name="p27036556102532"></a><a name="p27036556102532"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.84168416841684%" headers="mcps1.1.5.1.3 "><p id="p42477434102532"><a name="p42477434102532"></a><a name="p42477434102532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.664566456645666%" headers="mcps1.1.5.1.4 "><p id="p39463197143145"><a name="p39463197143145"></a><a name="p39463197143145"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table58447617102532"></a>
    <table><thead align="left"><tr id="row28600734102532"><th class="cellrowborder" valign="top" width="20.432043204320433%" id="mcps1.1.5.1.1"><p id="p34958131102532"><a name="p34958131102532"></a><a name="p34958131102532"></a><strong id="b37629484204310"><a name="b37629484204310"></a><a name="b37629484204310"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.92169216921692%" id="mcps1.1.5.1.2"><p id="p13036348102532"><a name="p13036348102532"></a><a name="p13036348102532"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.11171117111711%" id="mcps1.1.5.1.3"><p id="p49311266102532"><a name="p49311266102532"></a><a name="p49311266102532"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.53455345534553%" id="mcps1.1.5.1.4"><p id="p34789580102532"><a name="p34789580102532"></a><a name="p34789580102532"></a><strong id="b10278232204310"><a name="b10278232204310"></a><a name="b10278232204310"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66492578102532"><td class="cellrowborder" valign="top" width="20.432043204320433%" headers="mcps1.1.5.1.1 "><p id="p17189774102532"><a name="p17189774102532"></a><a name="p17189774102532"></a>rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.92169216921692%" headers="mcps1.1.5.1.2 "><p id="p50194421102532"><a name="p50194421102532"></a><a name="p50194421102532"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11171117111711%" headers="mcps1.1.5.1.3 "><p id="p492243151519"><a name="p492243151519"></a><a name="p492243151519"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.53455345534553%" headers="mcps1.1.5.1.4 "><p id="p322607102532"><a name="p322607102532"></a><a name="p322607102532"></a>List of rules used to map federated users into local users.</p>
    <p id="p39162214016"><a name="p39162214016"></a><a name="p39162214016"></a>Example:</p>
    <pre class="screen" id="screen163912251547"><a name="screen163912251547"></a><a name="screen163912251547"></a>"rules": [
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
                            "any_one_of": [
                                "Contractor",
                                "SubContractor"
                            ]
                        }
                    ]
                }
            ]</pre>
    <p id="p136024853311"><a name="p136024853311"></a><a name="p136024853311"></a>Under the <strong id="b1707890328142453_1"><a name="b1707890328142453_1"></a><a name="b1707890328142453_1"></a>local</strong> field:</p>
    <a name="ul26074810331"></a><a name="ul26074810331"></a><ul id="ul26074810331"><li><strong id="b1011945538142452_1"><a name="b1011945538142452_1"></a><a name="b1011945538142452_1"></a>user</strong>: indicates a local user.</li><li><strong id="b1594267902142450_1"><a name="b1594267902142450_1"></a><a name="b1594267902142450_1"></a>group</strong>: indicates a local user group.</li></ul>
    <p id="p36024873319"><a name="p36024873319"></a><a name="p36024873319"></a>Under the <strong id="b101613159142448"><a name="b101613159142448"></a><a name="b101613159142448"></a>remote</strong> field:</p>
    <a name="ul136225917201"></a><a name="ul136225917201"></a><ul id="ul136225917201"><li><strong id="b35911621152914"><a name="b35911621152914"></a><a name="b35911621152914"></a>"type": "UserName" </strong>indicates an attribute in an IdP assertion.</li><li><strong id="b118011252134614"><a name="b118011252134614"></a><a name="b118011252134614"></a>"type": "orgPersonType"</strong> indicates an attribute in an IdP assertion.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X PATCH -d'{"mapping":{"rules":[{"local":[{"user":{"name":"{0}"}},{"group":{"name":"0cd5e9"}}],"remote":[{"type":"UserName"},{"type":"orgPersonType","any_one_of":["Contractor","SubContractor"]}]}]}}' https://10.185.190.118:31943/v3/OS-FEDERATION/mappings/ACME
    ```


## Response<a name="section11865670102532"></a>

-   Response body parameter description

    <a name="table4378847102532"></a>
    <table><thead align="left"><tr id="row22353682102532"><th class="cellrowborder" valign="top" width="20.287971202879714%" id="mcps1.1.5.1.1"><p id="p65817845102532"><a name="p65817845102532"></a><a name="p65817845102532"></a><strong id="b40561463204310"><a name="b40561463204310"></a><a name="b40561463204310"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.25827417258274%" id="mcps1.1.5.1.2"><p id="p29645208102532"><a name="p29645208102532"></a><a name="p29645208102532"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_7"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.728327167283272%" id="mcps1.1.5.1.3"><p id="p52451619102532"><a name="p52451619102532"></a><a name="p52451619102532"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_7"><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.72542745725428%" id="mcps1.1.5.1.4"><p id="p20722751102532"><a name="p20722751102532"></a><a name="p20722751102532"></a><strong id="b842352706114032_3"><a name="b842352706114032_3"></a><a name="b842352706114032_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row821267102532"><td class="cellrowborder" valign="top" width="20.287971202879714%" headers="mcps1.1.5.1.1 "><p id="p66522696102532"><a name="p66522696102532"></a><a name="p66522696102532"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.25827417258274%" headers="mcps1.1.5.1.2 "><p id="p19629318102532"><a name="p19629318102532"></a><a name="p19629318102532"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.3 "><p id="p46470900102532"><a name="p46470900102532"></a><a name="p46470900102532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.72542745725428%" headers="mcps1.1.5.1.4 "><p id="p6046522102532"><a name="p6046522102532"></a><a name="p6046522102532"></a>Mapping ID.</p>
    </td>
    </tr>
    <tr id="row54418702102532"><td class="cellrowborder" valign="top" width="20.287971202879714%" headers="mcps1.1.5.1.1 "><p id="p45838732102532"><a name="p45838732102532"></a><a name="p45838732102532"></a>rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.25827417258274%" headers="mcps1.1.5.1.2 "><p id="p21949815102532"><a name="p21949815102532"></a><a name="p21949815102532"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.3 "><p id="p29505641102532"><a name="p29505641102532"></a><a name="p29505641102532"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.72542745725428%" headers="mcps1.1.5.1.4 "><p id="p2262822114330"><a name="p2262822114330"></a><a name="p2262822114330"></a>List of rules used to map federated users into local users.</p>
    <p id="p41146690102532"><a name="p41146690102532"></a><a name="p41146690102532"></a>Example:</p>
    <pre class="screen" id="screen15348185914710"><a name="screen15348185914710"></a><a name="screen15348185914710"></a>"rules": [
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
                            "any_one_of": [
                                "Contractor",
                                "SubContractor"
                            ]
                        }
                    ]
                }
            ]</pre>
    <p id="p18161201318483"><a name="p18161201318483"></a><a name="p18161201318483"></a>Under the <strong id="b1707890328142453_3"><a name="b1707890328142453_3"></a><a name="b1707890328142453_3"></a>local</strong> field:</p>
    <a name="ul1716181312489"></a><a name="ul1716181312489"></a><ul id="ul1716181312489"><li><strong id="b1011945538142452_3"><a name="b1011945538142452_3"></a><a name="b1011945538142452_3"></a>user</strong>: indicates a local user.</li><li><strong id="b1594267902142450_3"><a name="b1594267902142450_3"></a><a name="b1594267902142450_3"></a>group</strong>: indicates a local user group.</li></ul>
    <p id="p191611413174813"><a name="p191611413174813"></a><a name="p191611413174813"></a>Under the <strong id="b1346519901142521"><a name="b1346519901142521"></a><a name="b1346519901142521"></a>remote</strong> field:</p>
    <a name="ul2016191317488"></a><a name="ul2016191317488"></a><ul id="ul2016191317488"><li><strong id="b1056018715306"><a name="b1056018715306"></a><a name="b1056018715306"></a>"type": "UserName"</strong> indicates an attribute in an IdP assertion.</li><li><strong id="b155606763015"><a name="b155606763015"></a><a name="b155606763015"></a>"type": "orgPersonType"</strong> indicates an attribute in an IdP assertion.</li></ul>
    </td>
    </tr>
    <tr id="row34775890102532"><td class="cellrowborder" valign="top" width="20.287971202879714%" headers="mcps1.1.5.1.1 "><p id="p65383678102532"><a name="p65383678102532"></a><a name="p65383678102532"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.25827417258274%" headers="mcps1.1.5.1.2 "><p id="p61586591102532"><a name="p61586591102532"></a><a name="p61586591102532"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.1.5.1.3 "><p id="p22458013102532"><a name="p22458013102532"></a><a name="p22458013102532"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.72542745725428%" headers="mcps1.1.5.1.4 "><p id="p7159775102532"><a name="p7159775102532"></a><a name="p7159775102532"></a>Resource links of mappings.</p>
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
                            "any_one_of": [
                                "Contractor",
                                "SubContractor"
                            ]
                        }
                    ]
                }
            ]
        }
    }
    ```


## Status Codes<a name="section60182107102532"></a>

<a name="table42912532102532"></a>
<table><thead align="left"><tr id="row45648486102532"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p6539877102532"><a name="p6539877102532"></a><a name="p6539877102532"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p59968053102532"><a name="p59968053102532"></a><a name="p59968053102532"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row25574142102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p58239591102532"><a name="p58239591102532"></a><a name="p58239591102532"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p19786392102532"><a name="p19786392102532"></a><a name="p19786392102532"></a>The request is successful.</p>
</td>
</tr>
<tr id="row43859803102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p62983180102532"><a name="p62983180102532"></a><a name="p62983180102532"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1363994102532"><a name="p1363994102532"></a><a name="p1363994102532"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row12275951102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p54827987102532"><a name="p54827987102532"></a><a name="p54827987102532"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p11881926102532"><a name="p11881926102532"></a><a name="p11881926102532"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row39828478102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4881294102532"><a name="p4881294102532"></a><a name="p4881294102532"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p59840514102532"><a name="p59840514102532"></a><a name="p59840514102532"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row1693717102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2973403102532"><a name="p2973403102532"></a><a name="p2973403102532"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p39519097102532"><a name="p39519097102532"></a><a name="p39519097102532"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row20127561102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p19719776102532"><a name="p19719776102532"></a><a name="p19719776102532"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p53797986102532"><a name="p53797986102532"></a><a name="p53797986102532"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row14419832102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p27155720102532"><a name="p27155720102532"></a><a name="p27155720102532"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p52129721102532"><a name="p52129721102532"></a><a name="p52129721102532"></a>A resource conflict occurs.</p>
</td>
</tr>
<tr id="row66514309102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p18949962102532"><a name="p18949962102532"></a><a name="p18949962102532"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p58551939102532"><a name="p58551939102532"></a><a name="p58551939102532"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row57205407102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3126370102532"><a name="p3126370102532"></a><a name="p3126370102532"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p51909389102532"><a name="p51909389102532"></a><a name="p51909389102532"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row64531321102532"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p59654549102532"><a name="p59654549102532"></a><a name="p59654549102532"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p180268102532"><a name="p180268102532"></a><a name="p180268102532"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

