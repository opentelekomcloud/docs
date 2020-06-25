# Creating a Mapping<a name="en-us_topic_0057845590"></a>

## Function Description<a name="section5391497194352"></a>

This interface is used to create a mapping.

## URI<a name="section4532847794352"></a>

-   URI format

    PUT /v3/OS-FEDERATION/mappings/\{id\}


-   URI parameter description

    <a name="table2172204994352"></a>
    <table><thead align="left"><tr id="row2412280694352"><th class="cellrowborder" valign="top" width="20.3020302030203%" id="mcps1.1.5.1.1"><p id="p779028994352"><a name="p779028994352"></a><a name="p779028994352"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.32173217321732%" id="mcps1.1.5.1.2"><p id="p2703368594352"><a name="p2703368594352"></a><a name="p2703368594352"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.95179517951795%" id="mcps1.1.5.1.3"><p id="p4224484094352"><a name="p4224484094352"></a><a name="p4224484094352"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.42444244424442%" id="mcps1.1.5.1.4"><p id="p6638891794352"><a name="p6638891794352"></a><a name="p6638891794352"></a><strong id="b842352706114032_1"><a name="b842352706114032_1"></a><a name="b842352706114032_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row879318694352"><td class="cellrowborder" valign="top" width="20.3020302030203%" headers="mcps1.1.5.1.1 "><p id="p4115944794352"><a name="p4115944794352"></a><a name="p4115944794352"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32173217321732%" headers="mcps1.1.5.1.2 "><p id="p4558092594352"><a name="p4558092594352"></a><a name="p4558092594352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.95179517951795%" headers="mcps1.1.5.1.3 "><p id="p106745194352"><a name="p106745194352"></a><a name="p106745194352"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.42444244424442%" headers="mcps1.1.5.1.4 "><p id="p1935474694352"><a name="p1935474694352"></a><a name="p1935474694352"></a>Mapping ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section2423062694352"></a>

-   Request header parameter description

    <a name="table6334919494352"></a>
    <table><thead align="left"><tr id="row4195230994352"><th class="cellrowborder" valign="top" width="20.07%" id="mcps1.1.5.1.1"><p id="p4269386794352"><a name="p4269386794352"></a><a name="p4269386794352"></a><strong id="b1970987591656"><a name="b1970987591656"></a><a name="b1970987591656"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.2"><p id="p3565117394352"><a name="p3565117394352"></a><a name="p3565117394352"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.740000000000002%" id="mcps1.1.5.1.3"><p id="p206388394352"><a name="p206388394352"></a><a name="p206388394352"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.71%" id="mcps1.1.5.1.4"><p id="p3295687194352"><a name="p3295687194352"></a><a name="p3295687194352"></a><strong id="b5626546891656"><a name="b5626546891656"></a><a name="b5626546891656"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5226086294352"><td class="cellrowborder" valign="top" width="20.07%" headers="mcps1.1.5.1.1 "><p id="p527145094352"><a name="p527145094352"></a><a name="p527145094352"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.2 "><p id="p2433433994352"><a name="p2433433994352"></a><a name="p2433433994352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.740000000000002%" headers="mcps1.1.5.1.3 "><p id="p2492444894352"><a name="p2492444894352"></a><a name="p2492444894352"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.71%" headers="mcps1.1.5.1.4 "><p id="p561442694352"><a name="p561442694352"></a><a name="p561442694352"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row5052983794352"><td class="cellrowborder" valign="top" width="20.07%" headers="mcps1.1.5.1.1 "><p id="p6638498894352"><a name="p6638498894352"></a><a name="p6638498894352"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.2 "><p id="p847497294352"><a name="p847497294352"></a><a name="p847497294352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.740000000000002%" headers="mcps1.1.5.1.3 "><p id="p1538414994352"><a name="p1538414994352"></a><a name="p1538414994352"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.71%" headers="mcps1.1.5.1.4 "><p id="p24112655143038"><a name="p24112655143038"></a><a name="p24112655143038"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table367086394352"></a>
    <table><thead align="left"><tr id="row97994794352"><th class="cellrowborder" valign="top" width="20.16%" id="mcps1.1.5.1.1"><p id="p1226690694352"><a name="p1226690694352"></a><a name="p1226690694352"></a><strong id="b2119053791656"><a name="b2119053791656"></a><a name="b2119053791656"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.2"><p id="p5409532594352"><a name="p5409532594352"></a><a name="p5409532594352"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.53%" id="mcps1.1.5.1.3"><p id="p1964521394352"><a name="p1964521394352"></a><a name="p1964521394352"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.66%" id="mcps1.1.5.1.4"><p id="p4775840194352"><a name="p4775840194352"></a><a name="p4775840194352"></a><strong id="b4224969591656"><a name="b4224969591656"></a><a name="b4224969591656"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4322526694352"><td class="cellrowborder" valign="top" width="20.16%" headers="mcps1.1.5.1.1 "><p id="p1158562394352"><a name="p1158562394352"></a><a name="p1158562394352"></a>rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.2 "><p id="p6602024894352"><a name="p6602024894352"></a><a name="p6602024894352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.3 "><p id="p1170594394352"><a name="p1170594394352"></a><a name="p1170594394352"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.66%" headers="mcps1.1.5.1.4 "><p id="p865731194352"><a name="p865731194352"></a><a name="p865731194352"></a>List of rules used to map federated users into local users.</p>
    <p id="p209205871117"><a name="p209205871117"></a><a name="p209205871117"></a>Example:</p>
    <pre class="screen" id="screen2760136219"><a name="screen2760136219"></a><a name="screen2760136219"></a>"rules": [
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
    <p id="p181118260490"><a name="p181118260490"></a><a name="p181118260490"></a>Under the <strong id="b22234624111139_1"><a name="b22234624111139_1"></a><a name="b22234624111139_1"></a>local</strong> field:</p>
    <a name="ul1298428538"></a><a name="ul1298428538"></a><ul id="ul1298428538"><li><strong id="b110440996011137_1"><a name="b110440996011137_1"></a><a name="b110440996011137_1"></a>user</strong>: indicates a local user.</li><li><strong id="b89718370511135_1"><a name="b89718370511135_1"></a><a name="b89718370511135_1"></a>group</strong>: indicates a local user group.</li></ul>
    <p id="p810254675219"><a name="p810254675219"></a><a name="p810254675219"></a>Under the <strong id="b58771224811133"><a name="b58771224811133"></a><a name="b58771224811133"></a>remote</strong> field:</p>
    <a name="ul465615231208"></a><a name="ul465615231208"></a><ul id="ul465615231208"><li><strong id="b18478154142810"><a name="b18478154142810"></a><a name="b18478154142810"></a>"type": "UserName"</strong> indicates an attribute in an IdP assertion.</li><li><strong id="b1935147144718"><a name="b1935147144718"></a><a name="b1935147144718"></a>"type": "orgPersonType"</strong> indicates an attribute in an IdP assertion.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X PUT -d'{"mapping":{"rules":[{"local":[{"user":{"name":"{0}"}},{"group":{"name":"0cd5e9"}}],"remote":[{"type":"UserName"},{"type":"orgPersonType","not_any_of":["Contractor","Guest"]}]}]}}' https://10.185.190.118:31943/v3/OS-FEDERATION/mappings/ACME
    ```


## Response<a name="section1540149194352"></a>

-   Response body parameter description

    <a name="table5034224694352"></a>
    <table><thead align="left"><tr id="row751467994352"><th class="cellrowborder" valign="top" width="20.080000000000002%" id="mcps1.1.5.1.1"><p id="p470925894352"><a name="p470925894352"></a><a name="p470925894352"></a><strong id="b7788032112155"><a name="b7788032112155"></a><a name="b7788032112155"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.87%" id="mcps1.1.5.1.2"><p id="p4590562694352"><a name="p4590562694352"></a><a name="p4590562694352"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_7"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.47%" id="mcps1.1.5.1.3"><p id="p2736820694352"><a name="p2736820694352"></a><a name="p2736820694352"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_7"><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.58%" id="mcps1.1.5.1.4"><p id="p223220794352"><a name="p223220794352"></a><a name="p223220794352"></a><strong id="b842352706114032_3"><a name="b842352706114032_3"></a><a name="b842352706114032_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4659104494352"><td class="cellrowborder" valign="top" width="20.080000000000002%" headers="mcps1.1.5.1.1 "><p id="p1577819794352"><a name="p1577819794352"></a><a name="p1577819794352"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.87%" headers="mcps1.1.5.1.2 "><p id="p296561294352"><a name="p296561294352"></a><a name="p296561294352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.1.5.1.3 "><p id="p3888798294352"><a name="p3888798294352"></a><a name="p3888798294352"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58%" headers="mcps1.1.5.1.4 "><p id="p6291885394352"><a name="p6291885394352"></a><a name="p6291885394352"></a>Mapping ID.</p>
    </td>
    </tr>
    <tr id="row2939877294352"><td class="cellrowborder" valign="top" width="20.080000000000002%" headers="mcps1.1.5.1.1 "><p id="p3249034194352"><a name="p3249034194352"></a><a name="p3249034194352"></a>rules</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.87%" headers="mcps1.1.5.1.2 "><p id="p1447196694352"><a name="p1447196694352"></a><a name="p1447196694352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.1.5.1.3 "><p id="p1397223994352"><a name="p1397223994352"></a><a name="p1397223994352"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58%" headers="mcps1.1.5.1.4 "><p id="p5800957394352"><a name="p5800957394352"></a><a name="p5800957394352"></a>List of rules used to map federated users into local users.</p>
    <p id="p0615240105917"><a name="p0615240105917"></a><a name="p0615240105917"></a>Example:</p>
    <pre class="screen" id="screen252872812017"><a name="screen252872812017"></a><a name="screen252872812017"></a>"rules": [
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
    <p id="p10716986012"><a name="p10716986012"></a><a name="p10716986012"></a>Under the <strong id="b22234624111139_3"><a name="b22234624111139_3"></a><a name="b22234624111139_3"></a>local</strong> field:</p>
    <a name="ul162003401405"></a><a name="ul162003401405"></a><ul id="ul162003401405"><li><strong id="b149660073611429"><a name="b149660073611429"></a><a name="b149660073611429"></a>user</strong>: indicates a local user.</li><li><strong id="b16090234311431"><a name="b16090234311431"></a><a name="b16090234311431"></a>group</strong>: indicates a local user group.</li></ul>
    <p id="p1520018401018"><a name="p1520018401018"></a><a name="p1520018401018"></a>Under the <strong id="b580642821111553"><a name="b580642821111553"></a><a name="b580642821111553"></a>remote</strong> field:</p>
    <a name="ul1720084016016"></a><a name="ul1720084016016"></a><ul id="ul1720084016016"><li><strong id="b8595194618289"><a name="b8595194618289"></a><a name="b8595194618289"></a>"type": "UserName"</strong> indicates an attribute in an IdP assertion.</li><li><strong id="b1859544614287"><a name="b1859544614287"></a><a name="b1859544614287"></a>"type": "orgPersonType"</strong> indicates an attribute in an IdP assertion.</li></ul>
    </td>
    </tr>
    <tr id="row5232411094352"><td class="cellrowborder" valign="top" width="20.080000000000002%" headers="mcps1.1.5.1.1 "><p id="p1039448994352"><a name="p1039448994352"></a><a name="p1039448994352"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.87%" headers="mcps1.1.5.1.2 "><p id="p3664728594352"><a name="p3664728594352"></a><a name="p3664728594352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.1.5.1.3 "><p id="p1564010594352"><a name="p1564010594352"></a><a name="p1564010594352"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58%" headers="mcps1.1.5.1.4 "><p id="p5888902294352"><a name="p5888902294352"></a><a name="p5888902294352"></a>Resource links of mappings.</p>
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


## Status Codes<a name="section4195895394352"></a>

<a name="table4323206594352"></a>
<table><thead align="left"><tr id="row5614613494352"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p5154300694352"><a name="p5154300694352"></a><a name="p5154300694352"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p1423397194352"><a name="p1423397194352"></a><a name="p1423397194352"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1210098894352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4065597094352"><a name="p4065597094352"></a><a name="p4065597094352"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p479924494352"><a name="p479924494352"></a><a name="p479924494352"></a>The request is successful.</p>
</td>
</tr>
<tr id="row4319319894352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p898815494352"><a name="p898815494352"></a><a name="p898815494352"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5695187094352"><a name="p5695187094352"></a><a name="p5695187094352"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row4280478994352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4463590594352"><a name="p4463590594352"></a><a name="p4463590594352"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5873858694352"><a name="p5873858694352"></a><a name="p5873858694352"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row5888523194352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p497437394352"><a name="p497437394352"></a><a name="p497437394352"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p27106894352"><a name="p27106894352"></a><a name="p27106894352"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row243961594352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6339113094352"><a name="p6339113094352"></a><a name="p6339113094352"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3440788194352"><a name="p3440788194352"></a><a name="p3440788194352"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row4123547694352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5173922994352"><a name="p5173922994352"></a><a name="p5173922994352"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3012798294352"><a name="p3012798294352"></a><a name="p3012798294352"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row20445144495312"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1244574417533"><a name="p1244574417533"></a><a name="p1244574417533"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p0447174455316"><a name="p0447174455316"></a><a name="p0447174455316"></a>A resource conflict occurs.</p>
</td>
</tr>
<tr id="row271638594352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1870065894352"><a name="p1870065894352"></a><a name="p1870065894352"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3835836894352"><a name="p3835836894352"></a><a name="p3835836894352"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row968099794352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4596330594352"><a name="p4596330594352"></a><a name="p4596330594352"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3204018894352"><a name="p3204018894352"></a><a name="p3204018894352"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row1992624494352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p341307694352"><a name="p341307694352"></a><a name="p341307694352"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p802372094352"><a name="p802372094352"></a><a name="p802372094352"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

