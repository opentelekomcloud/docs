# Deleting a Mapping<a name="en-us_topic_0057845648"></a>

## Function Description<a name="section31686124102610"></a>

This interface is used to delete the information about a mapping.

## URI<a name="section13735511102610"></a>

-   URI format

    DELETE /v3/OS-FEDERATION/mappings/\{id\}


-   URI parameter description

    <a name="table36060471102610"></a>
    <table><thead align="left"><tr id="row28531275102610"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p29331927102610"><a name="p29331927102610"></a><a name="p29331927102610"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p27075847102610"><a name="p27075847102610"></a><a name="p27075847102610"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p45659971102610"><a name="p45659971102610"></a><a name="p45659971102610"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95"><a name="a703d34a49a2f4162bc1a1a439f655f95"></a><a name="a703d34a49a2f4162bc1a1a439f655f95"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p7470196102610"><a name="p7470196102610"></a><a name="p7470196102610"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1106178102610"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p22491604102610"><a name="p22491604102610"></a><a name="p22491604102610"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p9880659102610"><a name="p9880659102610"></a><a name="p9880659102610"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p62135910102610"><a name="p62135910102610"></a><a name="p62135910102610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p66952822102610"><a name="p66952822102610"></a><a name="p66952822102610"></a>Mapping ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section54469482102610"></a>

-   Request header parameter description

    <a name="table19573280102610"></a>
    <table><thead align="left"><tr id="row50848928102610"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p25122480102610"><a name="p25122480102610"></a><a name="p25122480102610"></a><strong id="b525474899174"><a name="b525474899174"></a><a name="b525474899174"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p21655009102610"><a name="p21655009102610"></a><a name="p21655009102610"></a><strong id="b550672989174"><a name="b550672989174"></a><a name="b550672989174"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p9225306102610"><a name="p9225306102610"></a><a name="p9225306102610"></a><strong id="b129599929174"><a name="b129599929174"></a><a name="b129599929174"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p9052356102610"><a name="p9052356102610"></a><a name="p9052356102610"></a><strong id="b525938479174"><a name="b525938479174"></a><a name="b525938479174"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62152263102610"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1168522102610"><a name="p1168522102610"></a><a name="p1168522102610"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p27541429102610"><a name="p27541429102610"></a><a name="p27541429102610"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p16263281102610"><a name="p16263281102610"></a><a name="p16263281102610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p42257381102610"><a name="p42257381102610"></a><a name="p42257381102610"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row44772116102610"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p2662800102610"><a name="p2662800102610"></a><a name="p2662800102610"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p14360281102610"><a name="p14360281102610"></a><a name="p14360281102610"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p22332118102610"><a name="p22332118102610"></a><a name="p22332118102610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p65565303143313"><a name="p65565303143313"></a><a name="p65565303143313"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X DELETE https://10.185.190.118:31943/v3/OS-FEDERATION/mappings/ACME
    ```


## Response<a name="section1073914502496"></a>

No response body.

## Status Codes<a name="section22380814102610"></a>

<a name="table906649102610"></a>
<table><thead align="left"><tr id="row50963380102610"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p34393077102610"><a name="p34393077102610"></a><a name="p34393077102610"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p34375847102610"><a name="p34375847102610"></a><a name="p34375847102610"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row32980209102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p54151292102610"><a name="p54151292102610"></a><a name="p54151292102610"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p24178544102610"><a name="p24178544102610"></a><a name="p24178544102610"></a>The request is successful.</p>
</td>
</tr>
<tr id="row16280304102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p43636243102610"><a name="p43636243102610"></a><a name="p43636243102610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p44874803102610"><a name="p44874803102610"></a><a name="p44874803102610"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row1220045102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p31714802102610"><a name="p31714802102610"></a><a name="p31714802102610"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p18762184102610"><a name="p18762184102610"></a><a name="p18762184102610"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row34641933102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p54533166102610"><a name="p54533166102610"></a><a name="p54533166102610"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p55110357102610"><a name="p55110357102610"></a><a name="p55110357102610"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row26231165102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p44349605102610"><a name="p44349605102610"></a><a name="p44349605102610"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p35548229102610"><a name="p35548229102610"></a><a name="p35548229102610"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row51498610102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p10637882102610"><a name="p10637882102610"></a><a name="p10637882102610"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p56362127102610"><a name="p56362127102610"></a><a name="p56362127102610"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row37497097102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p17366044102610"><a name="p17366044102610"></a><a name="p17366044102610"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p64472303102610"><a name="p64472303102610"></a><a name="p64472303102610"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row43379816102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p24104190102610"><a name="p24104190102610"></a><a name="p24104190102610"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6282410102610"><a name="p6282410102610"></a><a name="p6282410102610"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row56541690102610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p16474207102610"><a name="p16474207102610"></a><a name="p16474207102610"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p59342413102610"><a name="p59342413102610"></a><a name="p59342413102610"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

