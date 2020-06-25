# Updating a Protocol<a name="en-us_topic_0057845609"></a>

## Function Description<a name="section1123400102933"></a>

This interface is used to update the information about a protocol.

## URI<a name="section13652882102933"></a>

-   URI format

    PATCH /v3/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols/\{protocol\_id\}


-   URI parameter description

    <a name="table27916130102933"></a>
    <table><thead align="left"><tr id="row45510563102933"><th class="cellrowborder" valign="top" width="20.48795120487951%" id="mcps1.1.5.1.1"><p id="p62476969102933"><a name="p62476969102933"></a><a name="p62476969102933"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.568243175682433%" id="mcps1.1.5.1.2"><p id="p27469765102933"><a name="p27469765102933"></a><a name="p27469765102933"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.698230176982303%" id="mcps1.1.5.1.3"><p id="p10458460102933"><a name="p10458460102933"></a><a name="p10458460102933"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.24557544245575%" id="mcps1.1.5.1.4"><p id="p41828952102933"><a name="p41828952102933"></a><a name="p41828952102933"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32701985102933"><td class="cellrowborder" valign="top" width="20.48795120487951%" headers="mcps1.1.5.1.1 "><p id="p31615134102933"><a name="p31615134102933"></a><a name="p31615134102933"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.568243175682433%" headers="mcps1.1.5.1.2 "><p id="p10689080102933"><a name="p10689080102933"></a><a name="p10689080102933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.698230176982303%" headers="mcps1.1.5.1.3 "><p id="p60509142102933"><a name="p60509142102933"></a><a name="p60509142102933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24557544245575%" headers="mcps1.1.5.1.4 "><p id="p2293473102933"><a name="p2293473102933"></a><a name="p2293473102933"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row20641258102933"><td class="cellrowborder" valign="top" width="20.48795120487951%" headers="mcps1.1.5.1.1 "><p id="p61329219102933"><a name="p61329219102933"></a><a name="p61329219102933"></a>protocol _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.568243175682433%" headers="mcps1.1.5.1.2 "><p id="p1610812102933"><a name="p1610812102933"></a><a name="p1610812102933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.698230176982303%" headers="mcps1.1.5.1.3 "><p id="p63366909102933"><a name="p63366909102933"></a><a name="p63366909102933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24557544245575%" headers="mcps1.1.5.1.4 "><p id="p32445999102933"><a name="p32445999102933"></a><a name="p32445999102933"></a>ID of a protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section10880249102933"></a>

-   Request header parameter description

    <a name="table48596088102933"></a>
    <table><thead align="left"><tr id="row18928895102933"><th class="cellrowborder" valign="top" width="20.22202220222022%" id="mcps1.1.5.1.1"><p id="p56845520102933"><a name="p56845520102933"></a><a name="p56845520102933"></a><strong id="b5000791091710"><a name="b5000791091710"></a><a name="b5000791091710"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.961796179617963%" id="mcps1.1.5.1.2"><p id="p41084373102933"><a name="p41084373102933"></a><a name="p41084373102933"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.7017701770177%" id="mcps1.1.5.1.3"><p id="p39499894102933"><a name="p39499894102933"></a><a name="p39499894102933"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.114411441144114%" id="mcps1.1.5.1.4"><p id="p45374877102933"><a name="p45374877102933"></a><a name="p45374877102933"></a><strong id="b5320245191710"><a name="b5320245191710"></a><a name="b5320245191710"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51486383102933"><td class="cellrowborder" valign="top" width="20.22202220222022%" headers="mcps1.1.5.1.1 "><p id="p9647510102933"><a name="p9647510102933"></a><a name="p9647510102933"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.961796179617963%" headers="mcps1.1.5.1.2 "><p id="p43250874102933"><a name="p43250874102933"></a><a name="p43250874102933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7017701770177%" headers="mcps1.1.5.1.3 "><p id="p13659906102933"><a name="p13659906102933"></a><a name="p13659906102933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.114411441144114%" headers="mcps1.1.5.1.4 "><p id="p32710615102933"><a name="p32710615102933"></a><a name="p32710615102933"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row25960081102933"><td class="cellrowborder" valign="top" width="20.22202220222022%" headers="mcps1.1.5.1.1 "><p id="p22391844102933"><a name="p22391844102933"></a><a name="p22391844102933"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.961796179617963%" headers="mcps1.1.5.1.2 "><p id="p1800055102933"><a name="p1800055102933"></a><a name="p1800055102933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7017701770177%" headers="mcps1.1.5.1.3 "><p id="p11586738102933"><a name="p11586738102933"></a><a name="p11586738102933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.114411441144114%" headers="mcps1.1.5.1.4 "><p id="p9493251143726"><a name="p9493251143726"></a><a name="p9493251143726"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table2294710910289"></a>
    <table><thead align="left"><tr id="row3973971710289"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.1"><p id="p6480052110289"><a name="p6480052110289"></a><a name="p6480052110289"></a><strong id="b392453709177"><a name="b392453709177"></a><a name="b392453709177"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.83%" id="mcps1.1.5.1.2"><p id="p1435081210289"><a name="p1435081210289"></a><a name="p1435081210289"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.57%" id="mcps1.1.5.1.3"><p id="p2156516110289"><a name="p2156516110289"></a><a name="p2156516110289"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.11%" id="mcps1.1.5.1.4"><p id="p194760610289"><a name="p194760610289"></a><a name="p194760610289"></a><strong id="b47738849177"><a name="b47738849177"></a><a name="b47738849177"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2353837910289"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p2756056110289"><a name="p2756056110289"></a><a name="p2756056110289"></a>mapping_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.2 "><p id="p1781297510289"><a name="p1781297510289"></a><a name="p1781297510289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.1.5.1.3 "><p id="p3356491010289"><a name="p3356491010289"></a><a name="p3356491010289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.1.5.1.4 "><p id="p3440322210289"><a name="p3440322210289"></a><a name="p3440322210289"></a>Mapping ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X PATCH -d'{"protocol":{"mapping_id":"ACME"}}' https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers/ACME/protocols/saml
    ```


## Response<a name="section52969420102933"></a>

-   Response body parameter description

    <a name="table42669506102933"></a>
    <table><thead align="left"><tr id="row11704882102933"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.1.5.1.1"><p id="p8571362102933"><a name="p8571362102933"></a><a name="p8571362102933"></a><strong id="b608462891710"><a name="b608462891710"></a><a name="b608462891710"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.7%" id="mcps1.1.5.1.2"><p id="p23191731102933"><a name="p23191731102933"></a><a name="p23191731102933"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_7"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.7%" id="mcps1.1.5.1.3"><p id="p66590924102933"><a name="p66590924102933"></a><a name="p66590924102933"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_7"><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.980000000000004%" id="mcps1.1.5.1.4"><p id="p25155798102933"><a name="p25155798102933"></a><a name="p25155798102933"></a><strong id="b4935261191710"><a name="b4935261191710"></a><a name="b4935261191710"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24353785102933"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="p26499548102933"><a name="p26499548102933"></a><a name="p26499548102933"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.2 "><p id="p66088615102933"><a name="p66088615102933"></a><a name="p66088615102933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.3 "><p id="p51577603102933"><a name="p51577603102933"></a><a name="p51577603102933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.980000000000004%" headers="mcps1.1.5.1.4 "><p id="p17036311102933"><a name="p17036311102933"></a><a name="p17036311102933"></a>ID of a protocol.</p>
    </td>
    </tr>
    <tr id="row19109078102933"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="p4331506102933"><a name="p4331506102933"></a><a name="p4331506102933"></a>mapping_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.2 "><p id="p15307739102933"><a name="p15307739102933"></a><a name="p15307739102933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.3 "><p id="p31967352102933"><a name="p31967352102933"></a><a name="p31967352102933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.980000000000004%" headers="mcps1.1.5.1.4 "><p id="p39218738102933"><a name="p39218738102933"></a><a name="p39218738102933"></a>Mapping ID.</p>
    </td>
    </tr>
    <tr id="row17424325102933"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="p2084212102933"><a name="p2084212102933"></a><a name="p2084212102933"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.2 "><p id="p34603508102933"><a name="p34603508102933"></a><a name="p34603508102933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.1.5.1.3 "><p id="p51420781102933"><a name="p51420781102933"></a><a name="p51420781102933"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.980000000000004%" headers="mcps1.1.5.1.4 "><p id="p4333702102933"><a name="p4333702102933"></a><a name="p4333702102933"></a>Resource links of a protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "protocol": {
            "id": "saml",
            "links": {
                "identity_provider": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME",
                "self": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME/protocols/saml"
            },
            "mapping_id": "ACME"
        }
    }
    ```


## Status Codes<a name="section45441013102933"></a>

<a name="table56843417102933"></a>
<table><thead align="left"><tr id="row30012712102933"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p15110647102933"><a name="p15110647102933"></a><a name="p15110647102933"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p16002927102933"><a name="p16002927102933"></a><a name="p16002927102933"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row21168695102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p36942711102933"><a name="p36942711102933"></a><a name="p36942711102933"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p39569624102933"><a name="p39569624102933"></a><a name="p39569624102933"></a>The request is successful.</p>
</td>
</tr>
<tr id="row20582300102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p56553617102933"><a name="p56553617102933"></a><a name="p56553617102933"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p17440250102933"><a name="p17440250102933"></a><a name="p17440250102933"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row22744526102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p30367297102933"><a name="p30367297102933"></a><a name="p30367297102933"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p43831964102933"><a name="p43831964102933"></a><a name="p43831964102933"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row58943360102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p9682892102933"><a name="p9682892102933"></a><a name="p9682892102933"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p46116755102933"><a name="p46116755102933"></a><a name="p46116755102933"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row12397617102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p64682943102933"><a name="p64682943102933"></a><a name="p64682943102933"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4827005102933"><a name="p4827005102933"></a><a name="p4827005102933"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row43443045102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p29225775102933"><a name="p29225775102933"></a><a name="p29225775102933"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p18477565102933"><a name="p18477565102933"></a><a name="p18477565102933"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row32080361102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p48372473102933"><a name="p48372473102933"></a><a name="p48372473102933"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p25856258102933"><a name="p25856258102933"></a><a name="p25856258102933"></a>A resource conflict occurs.</p>
</td>
</tr>
<tr id="row31379731102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p58730243102933"><a name="p58730243102933"></a><a name="p58730243102933"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p59529215102933"><a name="p59529215102933"></a><a name="p59529215102933"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row66000894102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p44472184102933"><a name="p44472184102933"></a><a name="p44472184102933"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p45477171102933"><a name="p45477171102933"></a><a name="p45477171102933"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row6641360102933"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1079311102933"><a name="p1079311102933"></a><a name="p1079311102933"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p20315362102933"><a name="p20315362102933"></a><a name="p20315362102933"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

