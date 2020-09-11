# Registering a Protocol<a name="en-us_topic_0057845575"></a>

## Function Description<a name="section6159829710289"></a>

This interface is used to register a protocol, that is, associate a rule with an identity provider.

## URI<a name="section932889710289"></a>

-   URI format

    PUT /v3/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols/\{protocol\_id\}


-   URI parameter description

    <a name="table6208226610289"></a>
    <table><thead align="left"><tr id="row2710995810289"><th class="cellrowborder" valign="top" width="21.020000000000003%" id="mcps1.1.5.1.1"><p id="p4842300710289"><a name="p4842300710289"></a><a name="p4842300710289"></a><strong id="en-us_topic_0026586105_b842352706143612"><a name="en-us_topic_0026586105_b842352706143612"></a><a name="en-us_topic_0026586105_b842352706143612"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.830000000000002%" id="mcps1.1.5.1.2"><p id="p2994946410289"><a name="p2994946410289"></a><a name="p2994946410289"></a><strong id="en-us_topic_0026586105_b842352706143621"><a name="en-us_topic_0026586105_b842352706143621"></a><a name="en-us_topic_0026586105_b842352706143621"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.1%" id="mcps1.1.5.1.3"><p id="p998748110289"><a name="p998748110289"></a><a name="p998748110289"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.050000000000004%" id="mcps1.1.5.1.4"><p id="p367962710289"><a name="p367962710289"></a><a name="p367962710289"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2961435710289"><td class="cellrowborder" valign="top" width="21.020000000000003%" headers="mcps1.1.5.1.1 "><p id="p4995273610289"><a name="p4995273610289"></a><a name="p4995273610289"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.830000000000002%" headers="mcps1.1.5.1.2 "><p id="p1963982810289"><a name="p1963982810289"></a><a name="p1963982810289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.1%" headers="mcps1.1.5.1.3 "><p id="p4732219910289"><a name="p4732219910289"></a><a name="p4732219910289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p789294810289"><a name="p789294810289"></a><a name="p789294810289"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row392767110289"><td class="cellrowborder" valign="top" width="21.020000000000003%" headers="mcps1.1.5.1.1 "><p id="p4970591510289"><a name="p4970591510289"></a><a name="p4970591510289"></a>protocol _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.830000000000002%" headers="mcps1.1.5.1.2 "><p id="p6675617210289"><a name="p6675617210289"></a><a name="p6675617210289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.1%" headers="mcps1.1.5.1.3 "><p id="p3854081710289"><a name="p3854081710289"></a><a name="p3854081710289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p3479845010289"><a name="p3479845010289"></a><a name="p3479845010289"></a>ID of a protocol. Only SAML is supported.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section10223310289"></a>

-   Request header parameter description

    <a name="table6677115410289"></a>
    <table><thead align="left"><tr id="row5794046110289"><th class="cellrowborder" valign="top" width="21.020000000000003%" id="mcps1.1.5.1.1"><p id="p6266579210289"><a name="p6266579210289"></a><a name="p6266579210289"></a><strong id="b867570882"><a name="b867570882"></a><a name="b867570882"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.830000000000002%" id="mcps1.1.5.1.2"><p id="p4276437110289"><a name="p4276437110289"></a><a name="p4276437110289"></a><strong id="b171831275"><a name="b171831275"></a><a name="b171831275"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.1%" id="mcps1.1.5.1.3"><p id="p4136199810289"><a name="p4136199810289"></a><a name="p4136199810289"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.050000000000004%" id="mcps1.1.5.1.4"><p id="p6198754610289"><a name="p6198754610289"></a><a name="p6198754610289"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5493532610289"><td class="cellrowborder" valign="top" width="21.020000000000003%" headers="mcps1.1.5.1.1 "><p id="p2057645110289"><a name="p2057645110289"></a><a name="p2057645110289"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.830000000000002%" headers="mcps1.1.5.1.2 "><p id="p5607985710289"><a name="p5607985710289"></a><a name="p5607985710289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.1%" headers="mcps1.1.5.1.3 "><p id="p4617454310289"><a name="p4617454310289"></a><a name="p4617454310289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p4915046910289"><a name="p4915046910289"></a><a name="p4915046910289"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row3970104110289"><td class="cellrowborder" valign="top" width="21.020000000000003%" headers="mcps1.1.5.1.1 "><p id="p6166774310289"><a name="p6166774310289"></a><a name="p6166774310289"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.830000000000002%" headers="mcps1.1.5.1.2 "><p id="p2903129010289"><a name="p2903129010289"></a><a name="p2903129010289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.1%" headers="mcps1.1.5.1.3 "><p id="p272426510289"><a name="p272426510289"></a><a name="p272426510289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p28734406143622"><a name="p28734406143622"></a><a name="p28734406143622"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table2294710910289"></a>
    <table><thead align="left"><tr id="row3973971710289"><th class="cellrowborder" valign="top" width="21.28212821282128%" id="mcps1.1.5.1.1"><p id="p6480052110289"><a name="p6480052110289"></a><a name="p6480052110289"></a><strong id="b2028911620"><a name="b2028911620"></a><a name="b2028911620"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.7017701770177%" id="mcps1.1.5.1.2"><p id="p1435081210289"><a name="p1435081210289"></a><a name="p1435081210289"></a><strong id="b158295908"><a name="b158295908"></a><a name="b158295908"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.961796179617963%" id="mcps1.1.5.1.3"><p id="p2156516110289"><a name="p2156516110289"></a><a name="p2156516110289"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.05430543054305%" id="mcps1.1.5.1.4"><p id="p194760610289"><a name="p194760610289"></a><a name="p194760610289"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2353837910289"><td class="cellrowborder" valign="top" width="21.28212821282128%" headers="mcps1.1.5.1.1 "><p id="p2756056110289"><a name="p2756056110289"></a><a name="p2756056110289"></a>mapping_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.7017701770177%" headers="mcps1.1.5.1.2 "><p id="p1781297510289"><a name="p1781297510289"></a><a name="p1781297510289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.961796179617963%" headers="mcps1.1.5.1.3 "><p id="p3356491010289"><a name="p3356491010289"></a><a name="p3356491010289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.05430543054305%" headers="mcps1.1.5.1.4 "><p id="p3440322210289"><a name="p3440322210289"></a><a name="p3440322210289"></a>Mapping ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X PUT -d'{"protocol":{"mapping_id":"ACME"}}' https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers/ACME/protocols/saml
    ```


## **Response**<a name="section5620843410289"></a>

-   Response body parameter description

    <a name="table2033324010289"></a>
    <table><thead align="left"><tr id="row3108680210289"><th class="cellrowborder" valign="top" width="21.150000000000002%" id="mcps1.1.5.1.1"><p id="p3500305410289"><a name="p3500305410289"></a><a name="p3500305410289"></a><strong id="b1203394180"><a name="b1203394180"></a><a name="b1203394180"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.700000000000003%" id="mcps1.1.5.1.2"><p id="p1667515910289"><a name="p1667515910289"></a><a name="p1667515910289"></a><strong id="b1347820047"><a name="b1347820047"></a><a name="b1347820047"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.1%" id="mcps1.1.5.1.3"><p id="p851064410289"><a name="p851064410289"></a><a name="p851064410289"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.050000000000004%" id="mcps1.1.5.1.4"><p id="p1827358210289"><a name="p1827358210289"></a><a name="p1827358210289"></a><strong id="b20601766145329_7"><a name="b20601766145329_7"></a><a name="b20601766145329_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row376516410289"><td class="cellrowborder" valign="top" width="21.150000000000002%" headers="mcps1.1.5.1.1 "><p id="p3654287110289"><a name="p3654287110289"></a><a name="p3654287110289"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.700000000000003%" headers="mcps1.1.5.1.2 "><p id="p718255010289"><a name="p718255010289"></a><a name="p718255010289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.1%" headers="mcps1.1.5.1.3 "><p id="p4491566610289"><a name="p4491566610289"></a><a name="p4491566610289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p1429029010289"><a name="p1429029010289"></a><a name="p1429029010289"></a>ID of a protocol.</p>
    </td>
    </tr>
    <tr id="row6150374710289"><td class="cellrowborder" valign="top" width="21.150000000000002%" headers="mcps1.1.5.1.1 "><p id="p1574760510289"><a name="p1574760510289"></a><a name="p1574760510289"></a>mapping_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.700000000000003%" headers="mcps1.1.5.1.2 "><p id="p48761510289"><a name="p48761510289"></a><a name="p48761510289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.1%" headers="mcps1.1.5.1.3 "><p id="p3949687410289"><a name="p3949687410289"></a><a name="p3949687410289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p4513023810289"><a name="p4513023810289"></a><a name="p4513023810289"></a>Mapping ID.</p>
    </td>
    </tr>
    <tr id="row351895810289"><td class="cellrowborder" valign="top" width="21.150000000000002%" headers="mcps1.1.5.1.1 "><p id="p1660017710289"><a name="p1660017710289"></a><a name="p1660017710289"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.700000000000003%" headers="mcps1.1.5.1.2 "><p id="p243710510289"><a name="p243710510289"></a><a name="p243710510289"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.1%" headers="mcps1.1.5.1.3 "><p id="p6318779710289"><a name="p6318779710289"></a><a name="p6318779710289"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.050000000000004%" headers="mcps1.1.5.1.4 "><p id="p1793792610289"><a name="p1793792610289"></a><a name="p1793792610289"></a>Resource links of a protocol.</p>
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


## **Status Codes**<a name="section2630008410289"></a>

<a name="table4993206110289"></a>
<table><thead align="left"><tr id="row1038470010289"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p3585434210289"><a name="p3585434210289"></a><a name="p3585434210289"></a><strong id="b842352706183230_3"><a name="b842352706183230_3"></a><a name="b842352706183230_3"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p1852057210289"><a name="p1852057210289"></a><a name="p1852057210289"></a><strong id="b20601766145329_9"><a name="b20601766145329_9"></a><a name="b20601766145329_9"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2377140010289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4643521510289"><a name="p4643521510289"></a><a name="p4643521510289"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p315609110289"><a name="p315609110289"></a><a name="p315609110289"></a>The request is successful.</p>
</td>
</tr>
<tr id="row2840482710289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1908962510289"><a name="p1908962510289"></a><a name="p1908962510289"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p275575910289"><a name="p275575910289"></a><a name="p275575910289"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row2480183510289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6279160910289"><a name="p6279160910289"></a><a name="p6279160910289"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5295557210289"><a name="p5295557210289"></a><a name="p5295557210289"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row683810110289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1701532610289"><a name="p1701532610289"></a><a name="p1701532610289"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3606413510289"><a name="p3606413510289"></a><a name="p3606413510289"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row5614175910289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5118860310289"><a name="p5118860310289"></a><a name="p5118860310289"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5263620410289"><a name="p5263620410289"></a><a name="p5263620410289"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row396379610289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5263207910289"><a name="p5263207910289"></a><a name="p5263207910289"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3534001910289"><a name="p3534001910289"></a><a name="p3534001910289"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row4962471510289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6017897410289"><a name="p6017897410289"></a><a name="p6017897410289"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4265873410289"><a name="p4265873410289"></a><a name="p4265873410289"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row4838428810289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2681323710289"><a name="p2681323710289"></a><a name="p2681323710289"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2438860310289"><a name="p2438860310289"></a><a name="p2438860310289"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row1817084010289"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6255191310289"><a name="p6255191310289"></a><a name="p6255191310289"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3354022410289"><a name="p3354022410289"></a><a name="p3354022410289"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

