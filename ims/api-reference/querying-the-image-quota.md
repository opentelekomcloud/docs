# Querying the Image Quota<a name="EN-US_TOPIC_0093967372"></a>

## Function<a name="section4688667014416"></a>

This extension API is used to query the quota of private images of a tenant in the current region.

## URI<a name="section58030181144720"></a>

GET /v1/cloudimages/quota

## Request<a name="section16881426144740"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/cloudimages/quota
    ```


## Response<a name="section28921683144828"></a>

-   Response parameters

    <a name="table30935819144853"></a>
    <table><thead align="left"><tr id="row17974559144853"><th class="cellrowborder" valign="top" width="30.486951304869514%" id="mcps1.1.4.1.1"><p id="p46653204144853"><a name="p46653204144853"></a><a name="p46653204144853"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.078292170782923%" id="mcps1.1.4.1.2"><p id="p8147776144853"><a name="p8147776144853"></a><a name="p8147776144853"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.1.4.1.3"><p id="p55990086144853"><a name="p55990086144853"></a><a name="p55990086144853"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38903117144853"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p64144764144853"><a name="p64144764144853"></a><a name="p64144764144853"></a>quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p14115701144853"><a name="p14115701144853"></a><a name="p14115701144853"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p2521102144853"><a name="p2521102144853"></a><a name="p2521102144853"></a>Specifies the quota information.</p>
    <p id="p15441192583115"><a name="p15441192583115"></a><a name="p15441192583115"></a>For details, see <a href="#table147763014020">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Description of parameter resources

    <a name="table147763014020"></a>
    <table><thead align="left"><tr id="row17776405010"><th class="cellrowborder" valign="top" width="26.097390260973903%" id="mcps1.2.4.1.1"><p id="p57772001105"><a name="p57772001105"></a><a name="p57772001105"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.467853214678534%" id="mcps1.2.4.1.2"><p id="p1477730605"><a name="p1477730605"></a><a name="p1477730605"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.2.4.1.3"><p id="p15777801503"><a name="p15777801503"></a><a name="p15777801503"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row157772001800"><td class="cellrowborder" valign="top" width="26.097390260973903%" headers="mcps1.2.4.1.1 "><p id="p167776019017"><a name="p167776019017"></a><a name="p167776019017"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.467853214678534%" headers="mcps1.2.4.1.2 "><p id="p27772001005"><a name="p27772001005"></a><a name="p27772001005"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.2.4.1.3 "><p id="p1577710017013"><a name="p1577710017013"></a><a name="p1577710017013"></a>Specifies the resources to be queried.</p>
    <p id="p1710610712410"><a name="p1710610712410"></a><a name="p1710610712410"></a>For details, see <a href="#table29581211801">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Description of ResourceInfo parameters

    <a name="table29581211801"></a>
    <table><thead align="left"><tr id="row1895813111011"><th class="cellrowborder" valign="top" width="25.987401259874016%" id="mcps1.2.4.1.1"><p id="p109581111016"><a name="p109581111016"></a><a name="p109581111016"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.57784221577842%" id="mcps1.2.4.1.2"><p id="p4958121607"><a name="p4958121607"></a><a name="p4958121607"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.2.4.1.3"><p id="p11959017013"><a name="p11959017013"></a><a name="p11959017013"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row995951409"><td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.1 "><p id="p119591518018"><a name="p119591518018"></a><a name="p119591518018"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.57784221577842%" headers="mcps1.2.4.1.2 "><p id="p9959216015"><a name="p9959216015"></a><a name="p9959216015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.2.4.1.3 "><p id="p129597116019"><a name="p129597116019"></a><a name="p129597116019"></a>Specifies the type of the resource to be queried.</p>
    </td>
    </tr>
    <tr id="row295919112011"><td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.1 "><p id="p3959181809"><a name="p3959181809"></a><a name="p3959181809"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.57784221577842%" headers="mcps1.2.4.1.2 "><p id="p10959211404"><a name="p10959211404"></a><a name="p10959211404"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.2.4.1.3 "><p id="p189594110013"><a name="p189594110013"></a><a name="p189594110013"></a>Specifies the used quota.</p>
    </td>
    </tr>
    <tr id="row795911301"><td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.1 "><p id="p1795915119015"><a name="p1795915119015"></a><a name="p1795915119015"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.57784221577842%" headers="mcps1.2.4.1.2 "><p id="p129591818011"><a name="p129591818011"></a><a name="p129591818011"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.2.4.1.3 "><p id="p295918110014"><a name="p295918110014"></a><a name="p295918110014"></a>Specifies the total quota.</p>
    </td>
    </tr>
    <tr id="row5959311709"><td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.1 "><p id="p895931304"><a name="p895931304"></a><a name="p895931304"></a>min</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.57784221577842%" headers="mcps1.2.4.1.2 "><p id="p1095911116012"><a name="p1095911116012"></a><a name="p1095911116012"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.2.4.1.3 "><p id="p139592110017"><a name="p139592110017"></a><a name="p139592110017"></a>Specifies the minimum quota.</p>
    </td>
    </tr>
    <tr id="row18959111307"><td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.1 "><p id="p2959151404"><a name="p2959151404"></a><a name="p2959151404"></a>max</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.57784221577842%" headers="mcps1.2.4.1.2 "><p id="p12959411603"><a name="p12959411603"></a><a name="p12959411603"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.2.4.1.3 "><p id="p995941803"><a name="p995941803"></a><a name="p995941803"></a>Specifies the maximum quota.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    STATUS CODE 200
    ```

    ```
    {
      "quotas": {
        "resources": [
          {
            "type": "image",
            "used": 0,
            "quota": 20,
            "min": 1,
            "max": 1000
          }
        ]
      }
    }
    ```


## Returned Value<a name="section40084941"></a>

-   Normal

    200

-   Abnormal

    <a name="table56259839144728"></a>
    <table><thead align="left"><tr id="row64271486144728"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p38607917144728"><a name="p38607917144728"></a><a name="p38607917144728"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p40233605144728"><a name="p40233605144728"></a><a name="p40233605144728"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37696557144728"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p33522253144728"><a name="p33522253144728"></a><a name="p33522253144728"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p30947982144728"><a name="p30947982144728"></a><a name="p30947982144728"></a>Request error. For details, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row23758615144728"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p45399697144728"><a name="p45399697144728"></a><a name="p45399697144728"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p53496868144728"><a name="p53496868144728"></a><a name="p53496868144728"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row11709766144728"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p8966960144728"><a name="p8966960144728"></a><a name="p8966960144728"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p55235142144728"><a name="p55235142144728"></a><a name="p55235142144728"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row27354238144728"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p1100802144728"><a name="p1100802144728"></a><a name="p1100802144728"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p22056167144728"><a name="p22056167144728"></a><a name="p22056167144728"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row64287781144728"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p39927806144728"><a name="p39927806144728"></a><a name="p39927806144728"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p12926859144728"><a name="p12926859144728"></a><a name="p12926859144728"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row49232873144728"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p28439776144728"><a name="p28439776144728"></a><a name="p28439776144728"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p21920511144728"><a name="p21920511144728"></a><a name="p21920511144728"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


