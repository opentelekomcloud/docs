# Querying User Group Details<a name="en-us_topic_0057845618"></a>

## Function Description<a name="section374725841447"></a>

This interface is used to query detailed information about a user group.

## **URI**<a name="section37905744151541"></a>

-   URI format

    GET /v3/groups/\{group\_id\}

-   Query parameter description

    <a name="table1045846915195"></a>
    <table><thead align="left"><tr id="row5974534815195"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="p753502915195"><a name="p753502915195"></a><a name="p753502915195"></a><strong id="b84235270611173"><a name="b84235270611173"></a><a name="b84235270611173"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.24%" id="mcps1.1.5.1.2"><p id="p635761415195"><a name="p635761415195"></a><a name="p635761415195"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.05%" id="mcps1.1.5.1.3"><p id="p4520476015195"><a name="p4520476015195"></a><a name="p4520476015195"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.35%" id="mcps1.1.5.1.4"><p id="p3770697115195"><a name="p3770697115195"></a><a name="p3770697115195"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3436579015195"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="p3216557715195"><a name="p3216557715195"></a><a name="p3216557715195"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.1.5.1.2 "><p id="p5527494915195"><a name="p5527494915195"></a><a name="p5527494915195"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p4808588115195"><a name="p4808588115195"></a><a name="p4808588115195"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.35%" headers="mcps1.1.5.1.4 "><p id="p264231815195"><a name="p264231815195"></a><a name="p264231815195"></a>ID of a user group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section24249773152039"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.34%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.309999999999995%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b1522845415265"><a name="b1522845415265"></a><a name="b1522845415265"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row9196329"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p6705199"><a name="en-us_topic_0032920307_p6705199"></a><a name="en-us_topic_0032920307_p6705199"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p6250253"><a name="en-us_topic_0032920307_p6250253"></a><a name="en-us_topic_0032920307_p6250253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.34%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36508524"><a name="en-us_topic_0032920307_p36508524"></a><a name="en-us_topic_0032920307_p36508524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.309999999999995%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p4400500"><a name="en-us_topic_0032920307_p4400500"></a><a name="en-us_topic_0032920307_p4400500"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.34%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.309999999999995%" headers="mcps1.1.5.1.4 "><p id="p2531632811434"><a name="p2531632811434"></a><a name="p2531632811434"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X GET https://10.145.93.56:31943/v3/groups/ab9f261180d746ef8624beb5ae39b5aa
    ```


## **Response**<a name="section58835528153619"></a>

-   Response body parameter description

    <a name="table1056195410010"></a>
    <table><thead align="left"><tr id="row2747156110010"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.1.5.1.1"><p id="p447620910517"><a name="p447620910517"></a><a name="p447620910517"></a><strong id="b1709237332"><a name="b1709237332"></a><a name="b1709237332"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.761976197619763%" id="mcps1.1.5.1.2"><p id="p17754564499"><a name="p17754564499"></a><a name="p17754564499"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.01190119011901%" id="mcps1.1.5.1.3"><p id="p755696810517"><a name="p755696810517"></a><a name="p755696810517"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.41424142414241%" id="mcps1.1.5.1.4"><p id="p6407638510517"><a name="p6407638510517"></a><a name="p6407638510517"></a><strong id="b230267746154854"><a name="b230267746154854"></a><a name="b230267746154854"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row570214510010"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p5922062510010"><a name="p5922062510010"></a><a name="p5922062510010"></a>group</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.761976197619763%" headers="mcps1.1.5.1.2 "><p id="p87595644915"><a name="p87595644915"></a><a name="p87595644915"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.1.5.1.3 "><p id="p5331155510010"><a name="p5331155510010"></a><a name="p5331155510010"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.41424142414241%" headers="mcps1.1.5.1.4 "><p id="p2326866010010"><a name="p2326866010010"></a><a name="p2326866010010"></a>Response body of a user group.</p>
    </td>
    </tr>
    <tr id="row809135110010"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p53468292105715"><a name="p53468292105715"></a><a name="p53468292105715"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.761976197619763%" headers="mcps1.1.5.1.2 "><p id="p1875135616490"><a name="p1875135616490"></a><a name="p1875135616490"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.1.5.1.3 "><p id="p852996010010"><a name="p852996010010"></a><a name="p852996010010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.41424142414241%" headers="mcps1.1.5.1.4 "><p id="p1983818310010"><a name="p1983818310010"></a><a name="p1983818310010"></a>Description for a user group.</p>
    </td>
    </tr>
    <tr id="row23913924105725"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p13898724105725"><a name="p13898724105725"></a><a name="p13898724105725"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.761976197619763%" headers="mcps1.1.5.1.2 "><p id="p157565634918"><a name="p157565634918"></a><a name="p157565634918"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.1.5.1.3 "><p id="p52054821105725"><a name="p52054821105725"></a><a name="p52054821105725"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.41424142414241%" headers="mcps1.1.5.1.4 "><p id="p55690967105725"><a name="p55690967105725"></a><a name="p55690967105725"></a>ID of the domain to which a user group belongs.</p>
    </td>
    </tr>
    <tr id="row43504723105810"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p55998188105810"><a name="p55998188105810"></a><a name="p55998188105810"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.761976197619763%" headers="mcps1.1.5.1.2 "><p id="p375175610498"><a name="p375175610498"></a><a name="p375175610498"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.1.5.1.3 "><p id="p39559385105810"><a name="p39559385105810"></a><a name="p39559385105810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.41424142414241%" headers="mcps1.1.5.1.4 "><p id="p50193635105810"><a name="p50193635105810"></a><a name="p50193635105810"></a>ID of a user group.</p>
    </td>
    </tr>
    <tr id="row42687591105820"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p48644001105820"><a name="p48644001105820"></a><a name="p48644001105820"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.761976197619763%" headers="mcps1.1.5.1.2 "><p id="p1876556104917"><a name="p1876556104917"></a><a name="p1876556104917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.1.5.1.3 "><p id="p47850047105820"><a name="p47850047105820"></a><a name="p47850047105820"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.41424142414241%" headers="mcps1.1.5.1.4 "><p id="p50648609105820"><a name="p50648609105820"></a><a name="p50648609105820"></a>Links to a user group.</p>
    </td>
    </tr>
    <tr id="row1704891105830"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p15344026105830"><a name="p15344026105830"></a><a name="p15344026105830"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.761976197619763%" headers="mcps1.1.5.1.2 "><p id="p57695694919"><a name="p57695694919"></a><a name="p57695694919"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.1.5.1.3 "><p id="p34906626105830"><a name="p34906626105830"></a><a name="p34906626105830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.41424142414241%" headers="mcps1.1.5.1.4 "><p id="p8864442105830"><a name="p8864442105830"></a><a name="p8864442105830"></a>Name of a user group.</p>
    </td>
    </tr>
    <tr id="row1815813393114"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.1 "><p id="p41591433113114"><a name="p41591433113114"></a><a name="p41591433113114"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.761976197619763%" headers="mcps1.1.5.1.2 "><p id="p19761056154914"><a name="p19761056154914"></a><a name="p19761056154914"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.1.5.1.3 "><p id="p515903373115"><a name="p515903373115"></a><a name="p515903373115"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.41424142414241%" headers="mcps1.1.5.1.4 "><p id="p315918330319"><a name="p315918330319"></a><a name="p315918330319"></a>Time when a user group is created.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "group":{
            "domain_id":"d54061ebcb5145dd814f8eb3fe9b7ac0",
            "description":"Contract developers",
            "id":"ab9f261180d746ef8624beb5ae39b5aa",
            "links":{
                "self":"https://sample.domain.com/v3/groups/ab9f261180d746ef8624beb5ae39b5aa"
            },
            "name":"abcdef",
            "create_time": 1494943784468
        }
    }
    ```


## **Status Codes**<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b2587340315265"><a name="b2587340315265"></a><a name="b2587340315265"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0032920307_p16041657"><a name="en-us_topic_0032920307_p16041657"></a><a name="en-us_topic_0032920307_p16041657"></a><strong id="b412025515265"><a name="b412025515265"></a><a name="b412025515265"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032920307_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p22613965"><a name="en-us_topic_0032920307_p22613965"></a><a name="en-us_topic_0032920307_p22613965"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p19791876"><a name="en-us_topic_0032920307_p19791876"></a><a name="en-us_topic_0032920307_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p66980994"><a name="en-us_topic_0032920307_p66980994"></a><a name="en-us_topic_0032920307_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p56751409"><a name="en-us_topic_0032920307_p56751409"></a><a name="en-us_topic_0032920307_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row460808479497"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p120744399497"><a name="p120744399497"></a><a name="p120744399497"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p385055099497"><a name="p385055099497"></a><a name="p385055099497"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p32717189"><a name="en-us_topic_0032920307_p32717189"></a><a name="en-us_topic_0032920307_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p32846614"><a name="en-us_topic_0032920307_p32846614"></a><a name="en-us_topic_0032920307_p32846614"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row1306642216138"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5048894216138"><a name="p5048894216138"></a><a name="p5048894216138"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6307248716138"><a name="p6307248716138"></a><a name="p6307248716138"></a>The server could not find the requested page.</p>
</td>
</tr>
</tbody>
</table>

