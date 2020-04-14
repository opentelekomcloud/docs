# Creating a User Group<a name="en-us_topic_0057845650"></a>

## Function Description<a name="section16448035101644"></a>

This interface is used to create a user group.

## URI<a name="section60989708101648"></a>

URI format

POST /v3/groups

## **Request**<a name="section763260110344"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_1"><a name="a173ae121cc9e48328ca613e72f2a1504_1"></a><a name="a173ae121cc9e48328ca613e72f2a1504_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.57%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.080000000000005%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b20601766145329"><a name="b20601766145329"></a><a name="b20601766145329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row9196329"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p6705199"><a name="en-us_topic_0032920307_p6705199"></a><a name="en-us_topic_0032920307_p6705199"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p6250253"><a name="en-us_topic_0032920307_p6250253"></a><a name="en-us_topic_0032920307_p6250253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36508524"><a name="en-us_topic_0032920307_p36508524"></a><a name="en-us_topic_0032920307_p36508524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p4400500"><a name="en-us_topic_0032920307_p4400500"></a><a name="en-us_topic_0032920307_p4400500"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p4433597211513"><a name="p4433597211513"></a><a name="p4433597211513"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request body parameter description

    <a name="table20476227103839"></a>
    <table><thead align="left"><tr id="row27191649103839"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="p55039964103839"><a name="p55039964103839"></a><a name="p55039964103839"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_3"><a name="a173ae121cc9e48328ca613e72f2a1504_3"></a><a name="a173ae121cc9e48328ca613e72f2a1504_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="p29052075103839"><a name="p29052075103839"></a><a name="p29052075103839"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.099999999999998%" id="mcps1.1.5.1.3"><p id="p4407863103839"><a name="p4407863103839"></a><a name="p4407863103839"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.55%" id="mcps1.1.5.1.4"><p id="p21492583103839"><a name="p21492583103839"></a><a name="p21492583103839"></a><strong id="b26002689171855_1"><a name="b26002689171855_1"></a><a name="b26002689171855_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6819406103839"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p15501051103839"><a name="p15501051103839"></a><a name="p15501051103839"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p47625608103839"><a name="p47625608103839"></a><a name="p47625608103839"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.1.5.1.3 "><p id="p32469021103839"><a name="p32469021103839"></a><a name="p32469021103839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.55%" headers="mcps1.1.5.1.4 "><p id="p12745059103839"><a name="p12745059103839"></a><a name="p12745059103839"></a>Description for a user group. The length is less than or equal to 255 characters.</p>
    </td>
    </tr>
    <tr id="row29609315103946"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p65157251103946"><a name="p65157251103946"></a><a name="p65157251103946"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p43245998103946"><a name="p43245998103946"></a><a name="p43245998103946"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.1.5.1.3 "><p id="p13264962103946"><a name="p13264962103946"></a><a name="p13264962103946"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.55%" headers="mcps1.1.5.1.4 "><p id="p720101103946"><a name="p720101103946"></a><a name="p720101103946"></a>ID of the domain to which a user group belongs.</p>
    </td>
    </tr>
    <tr id="row47644029103953"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p26143083103953"><a name="p26143083103953"></a><a name="p26143083103953"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p37214989103953"><a name="p37214989103953"></a><a name="p37214989103953"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.1.5.1.3 "><p id="p61624156103953"><a name="p61624156103953"></a><a name="p61624156103953"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.55%" headers="mcps1.1.5.1.4 "><p id="p25500735103953"><a name="p25500735103953"></a><a name="p25500735103953"></a>Name of a user group. The length is less than or equal to 64 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X POST -d'{"group": {"description": "Contract developers","domain_id": "d54061ebcb5145dd814f8eb3fe9b7ac0","name": "jixiang2"}}' https://172.30.48.86:31943/v3/groups
    ```


## **Response**<a name="section7621113105350"></a>

-   Response body parameter description

    <a name="table1056195410010"></a>
    <table><thead align="left"><tr id="row2747156110010"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.5.1.1"><p id="p447620910517"><a name="p447620910517"></a><a name="p447620910517"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_5"><a name="a173ae121cc9e48328ca613e72f2a1504_5"></a><a name="a173ae121cc9e48328ca613e72f2a1504_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.32%" id="mcps1.1.5.1.2"><p id="p15423142105019"><a name="p15423142105019"></a><a name="p15423142105019"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.56%" id="mcps1.1.5.1.3"><p id="p755696810517"><a name="p755696810517"></a><a name="p755696810517"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.120000000000005%" id="mcps1.1.5.1.4"><p id="p6407638510517"><a name="p6407638510517"></a><a name="p6407638510517"></a><strong id="b26002689171855_3"><a name="b26002689171855_3"></a><a name="b26002689171855_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row809135110010"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p53468292105715"><a name="p53468292105715"></a><a name="p53468292105715"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p34246211507"><a name="p34246211507"></a><a name="p34246211507"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.3 "><p id="p852996010010"><a name="p852996010010"></a><a name="p852996010010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.120000000000005%" headers="mcps1.1.5.1.4 "><p id="p1983818310010"><a name="p1983818310010"></a><a name="p1983818310010"></a>Description for a user group.</p>
    </td>
    </tr>
    <tr id="row23913924105725"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p13898724105725"><a name="p13898724105725"></a><a name="p13898724105725"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p1842462175011"><a name="p1842462175011"></a><a name="p1842462175011"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.3 "><p id="p52054821105725"><a name="p52054821105725"></a><a name="p52054821105725"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.120000000000005%" headers="mcps1.1.5.1.4 "><p id="p55690967105725"><a name="p55690967105725"></a><a name="p55690967105725"></a>ID of the domain to which a user group belongs.</p>
    </td>
    </tr>
    <tr id="row43504723105810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p55998188105810"><a name="p55998188105810"></a><a name="p55998188105810"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p14424152175015"><a name="p14424152175015"></a><a name="p14424152175015"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.3 "><p id="p39559385105810"><a name="p39559385105810"></a><a name="p39559385105810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.120000000000005%" headers="mcps1.1.5.1.4 "><p id="p50193635105810"><a name="p50193635105810"></a><a name="p50193635105810"></a>ID of a user group.</p>
    </td>
    </tr>
    <tr id="row42687591105820"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p48644001105820"><a name="p48644001105820"></a><a name="p48644001105820"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p11424629506"><a name="p11424629506"></a><a name="p11424629506"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.3 "><p id="p1071821654919"><a name="p1071821654919"></a><a name="p1071821654919"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.120000000000005%" headers="mcps1.1.5.1.4 "><p id="p50648609105820"><a name="p50648609105820"></a><a name="p50648609105820"></a>Links to a user group.</p>
    </td>
    </tr>
    <tr id="row1704891105830"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p15344026105830"><a name="p15344026105830"></a><a name="p15344026105830"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p1842462135019"><a name="p1842462135019"></a><a name="p1842462135019"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.3 "><p id="p34906626105830"><a name="p34906626105830"></a><a name="p34906626105830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.120000000000005%" headers="mcps1.1.5.1.4 "><p id="p8864442105830"><a name="p8864442105830"></a><a name="p8864442105830"></a>Name of a user group.</p>
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
            "name":"abcdef"
        }
    }
    ```


## **Status Codes**<a name="section49475145112813"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b2474889171855"><a name="b2474889171855"></a><a name="b2474889171855"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0032920307_p16041657"><a name="en-us_topic_0032920307_p16041657"></a><a name="en-us_topic_0032920307_p16041657"></a><strong id="b59363903171855"><a name="b59363903171855"></a><a name="b59363903171855"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032920307_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p22613965"><a name="en-us_topic_0032920307_p22613965"></a><a name="en-us_topic_0032920307_p22613965"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p19791876"><a name="en-us_topic_0032920307_p19791876"></a><a name="en-us_topic_0032920307_p19791876"></a>The user group is successfully created.</p>
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
<tr id="row2520892414217"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2555372914217"><a name="p2555372914217"></a><a name="p2555372914217"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5658613514217"><a name="p5658613514217"></a><a name="p5658613514217"></a>A resource conflict occurs.</p>
</td>
</tr>
</tbody>
</table>

