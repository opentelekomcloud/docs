# Querying the Protocol List<a name="en-us_topic_0057845644"></a>

## Function Description<a name="section30634034102834"></a>

This interface is used to query the protocol list.

## URI<a name="section52068019102834"></a>

-   URI format

    GET /v3/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols


-   URI parameter description

    <a name="table37148424111357"></a>
    <table><thead align="left"><tr id="row51867099111357"><th class="cellrowborder" valign="top" width="22.06%" id="mcps1.1.5.1.1"><p id="p40485495111357"><a name="p40485495111357"></a><a name="p40485495111357"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.26%" id="mcps1.1.5.1.2"><p id="p58099659111357"><a name="p58099659111357"></a><a name="p58099659111357"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.73%" id="mcps1.1.5.1.3"><p id="p8451968111357"><a name="p8451968111357"></a><a name="p8451968111357"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.95%" id="mcps1.1.5.1.4"><p id="p13520830111357"><a name="p13520830111357"></a><a name="p13520830111357"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21445420111357"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.1.5.1.1 "><p id="p59357426111357"><a name="p59357426111357"></a><a name="p59357426111357"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.1.5.1.2 "><p id="p43222201111357"><a name="p43222201111357"></a><a name="p43222201111357"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.1.5.1.3 "><p id="p11337384111357"><a name="p11337384111357"></a><a name="p11337384111357"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.95%" headers="mcps1.1.5.1.4 "><p id="p45912936111357"><a name="p45912936111357"></a><a name="p45912936111357"></a>ID of an identity provider.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section14876957102834"></a>

-   Request header parameter description

    <a name="table31432374102834"></a>
    <table><thead align="left"><tr id="row45139814102834"><th class="cellrowborder" valign="top" width="21.759999999999998%" id="mcps1.1.5.1.1"><p id="p32446352102834"><a name="p32446352102834"></a><a name="p32446352102834"></a><strong id="a3da1b7475f644c07832655d87318eb65"><a name="a3da1b7475f644c07832655d87318eb65"></a><a name="a3da1b7475f644c07832655d87318eb65"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.47%" id="mcps1.1.5.1.2"><p id="p10908883102834"><a name="p10908883102834"></a><a name="p10908883102834"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.72%" id="mcps1.1.5.1.3"><p id="p11204310102834"><a name="p11204310102834"></a><a name="p11204310102834"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.05%" id="mcps1.1.5.1.4"><p id="p35133889102834"><a name="p35133889102834"></a><a name="p35133889102834"></a><strong id="b842352706114032_1"><a name="b842352706114032_1"></a><a name="b842352706114032_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27272765102834"><td class="cellrowborder" valign="top" width="21.759999999999998%" headers="mcps1.1.5.1.1 "><p id="p61610353102834"><a name="p61610353102834"></a><a name="p61610353102834"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.1.5.1.2 "><p id="p24382726102834"><a name="p24382726102834"></a><a name="p24382726102834"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.1.5.1.3 "><p id="p28843812102834"><a name="p28843812102834"></a><a name="p28843812102834"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.05%" headers="mcps1.1.5.1.4 "><p id="p54647410102834"><a name="p54647410102834"></a><a name="p54647410102834"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row22064642102834"><td class="cellrowborder" valign="top" width="21.759999999999998%" headers="mcps1.1.5.1.1 "><p id="p42405596102834"><a name="p42405596102834"></a><a name="p42405596102834"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.1.5.1.2 "><p id="p12301242102834"><a name="p12301242102834"></a><a name="p12301242102834"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.1.5.1.3 "><p id="p56876549102834"><a name="p56876549102834"></a><a name="p56876549102834"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.05%" headers="mcps1.1.5.1.4 "><p id="p43597732102834"><a name="p43597732102834"></a><a name="p43597732102834"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers/ACME/protocols/
    ```


## Response<a name="section41755392102834"></a>

-   Response body parameter description

    <a name="table18744076102834"></a>
    <table><thead align="left"><tr id="row63415676102834"><th class="cellrowborder" valign="top" width="21.772177217721772%" id="mcps1.1.5.1.1"><p id="p36396095102834"><a name="p36396095102834"></a><a name="p36396095102834"></a><strong id="b508006551079"><a name="b508006551079"></a><a name="b508006551079"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.241724172417243%" id="mcps1.1.5.1.2"><p id="p62402620102834"><a name="p62402620102834"></a><a name="p62402620102834"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.94169416941694%" id="mcps1.1.5.1.3"><p id="p21447449102834"><a name="p21447449102834"></a><a name="p21447449102834"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.04440444044405%" id="mcps1.1.5.1.4"><p id="p59521790102834"><a name="p59521790102834"></a><a name="p59521790102834"></a><strong id="b842352706114032_2"><a name="b842352706114032_2"></a><a name="b842352706114032_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56535700102834"><td class="cellrowborder" valign="top" width="21.772177217721772%" headers="mcps1.1.5.1.1 "><p id="p15988994102834"><a name="p15988994102834"></a><a name="p15988994102834"></a>protocols</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.241724172417243%" headers="mcps1.1.5.1.2 "><p id="p20040177102834"><a name="p20040177102834"></a><a name="p20040177102834"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.94169416941694%" headers="mcps1.1.5.1.3 "><p id="p12641673102834"><a name="p12641673102834"></a><a name="p12641673102834"></a>List of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.04440444044405%" headers="mcps1.1.5.1.4 "><p id="p17342577102834"><a name="p17342577102834"></a><a name="p17342577102834"></a>List of protocols.</p>
    </td>
    </tr>
    <tr id="row21865466102834"><td class="cellrowborder" valign="top" width="21.772177217721772%" headers="mcps1.1.5.1.1 "><p id="p26272350102834"><a name="p26272350102834"></a><a name="p26272350102834"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.241724172417243%" headers="mcps1.1.5.1.2 "><p id="p47685606102834"><a name="p47685606102834"></a><a name="p47685606102834"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.94169416941694%" headers="mcps1.1.5.1.3 "><p id="p37328891102834"><a name="p37328891102834"></a><a name="p37328891102834"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.04440444044405%" headers="mcps1.1.5.1.4 "><p id="p3741316102834"><a name="p3741316102834"></a><a name="p3741316102834"></a>Resource links of a protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   protocols parameter description

    <a name="table33600724102858"></a>
    <table><thead align="left"><tr id="row58807483102858"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.5.1.1"><p id="p65785692102858"><a name="p65785692102858"></a><a name="p65785692102858"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.708229177082295%" id="mcps1.1.5.1.2"><p id="p27040837102858"><a name="p27040837102858"></a><a name="p27040837102858"></a><strong id="b67575779"><a name="b67575779"></a><a name="b67575779"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.328267173282672%" id="mcps1.1.5.1.3"><p id="p42824223102858"><a name="p42824223102858"></a><a name="p42824223102858"></a><strong id="b1050479642"><a name="b1050479642"></a><a name="b1050479642"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.785621437856214%" id="mcps1.1.5.1.4"><p id="p46210066102858"><a name="p46210066102858"></a><a name="p46210066102858"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52027845102858"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.5.1.1 "><p id="p53505888102858"><a name="p53505888102858"></a><a name="p53505888102858"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.708229177082295%" headers="mcps1.1.5.1.2 "><p id="p39009676102858"><a name="p39009676102858"></a><a name="p39009676102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.1.5.1.3 "><p id="p5667184102858"><a name="p5667184102858"></a><a name="p5667184102858"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.785621437856214%" headers="mcps1.1.5.1.4 "><p id="p56388789102858"><a name="p56388789102858"></a><a name="p56388789102858"></a>ID of a protocol.</p>
    </td>
    </tr>
    <tr id="row37737059102858"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.5.1.1 "><p id="p36802972102858"><a name="p36802972102858"></a><a name="p36802972102858"></a>mapping_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.708229177082295%" headers="mcps1.1.5.1.2 "><p id="p28250761102858"><a name="p28250761102858"></a><a name="p28250761102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.1.5.1.3 "><p id="p6610323102858"><a name="p6610323102858"></a><a name="p6610323102858"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.785621437856214%" headers="mcps1.1.5.1.4 "><p id="p65674145102858"><a name="p65674145102858"></a><a name="p65674145102858"></a>Mapping ID.</p>
    </td>
    </tr>
    <tr id="row54196397102858"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.5.1.1 "><p id="p27832061102858"><a name="p27832061102858"></a><a name="p27832061102858"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.708229177082295%" headers="mcps1.1.5.1.2 "><p id="p39804486102858"><a name="p39804486102858"></a><a name="p39804486102858"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.328267173282672%" headers="mcps1.1.5.1.3 "><p id="p2937903102858"><a name="p2937903102858"></a><a name="p2937903102858"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.785621437856214%" headers="mcps1.1.5.1.4 "><p id="p36643552102858"><a name="p36643552102858"></a><a name="p36643552102858"></a>Resource links of a protocol.</p>
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
            "self": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME/protocols"
        },
        "protocols": [
            {
                "id": "saml",
                "links": {
                    "identity_provider": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME",
                    "self": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME/protocols/saml"
                },
                "mapping_id": "ACME"
            }
        ]
    }
    ```


## Status Codes<a name="section49506819102834"></a>

<a name="table50629427102834"></a>
<table><thead align="left"><tr id="row51403085102834"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p2900329102834"><a name="p2900329102834"></a><a name="p2900329102834"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p33600122102834"><a name="p33600122102834"></a><a name="p33600122102834"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row37255400102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p64897434102834"><a name="p64897434102834"></a><a name="p64897434102834"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p22200825102834"><a name="p22200825102834"></a><a name="p22200825102834"></a>The request is successful.</p>
</td>
</tr>
<tr id="row65589700102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p11165521102834"><a name="p11165521102834"></a><a name="p11165521102834"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p31991998102834"><a name="p31991998102834"></a><a name="p31991998102834"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row19492528102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p35390929102834"><a name="p35390929102834"></a><a name="p35390929102834"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p48092966102834"><a name="p48092966102834"></a><a name="p48092966102834"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row30183511102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p28945366102834"><a name="p28945366102834"></a><a name="p28945366102834"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p62873342102834"><a name="p62873342102834"></a><a name="p62873342102834"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row28989168102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p66421287102834"><a name="p66421287102834"></a><a name="p66421287102834"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p11415195102834"><a name="p11415195102834"></a><a name="p11415195102834"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row35627895102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p178384102834"><a name="p178384102834"></a><a name="p178384102834"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p14449178102834"><a name="p14449178102834"></a><a name="p14449178102834"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row62933745102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p64468583102834"><a name="p64468583102834"></a><a name="p64468583102834"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p54572705102834"><a name="p54572705102834"></a><a name="p54572705102834"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row21392299102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p55054663102834"><a name="p55054663102834"></a><a name="p55054663102834"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p30242715102834"><a name="p30242715102834"></a><a name="p30242715102834"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row3748986102834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p35232470102834"><a name="p35232470102834"></a><a name="p35232470102834"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p35257855102834"><a name="p35257855102834"></a><a name="p35257855102834"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

