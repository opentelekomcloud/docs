# Querying Quotas<a name="EN-US_TOPIC_0059304243"></a>

## Function<a name="section20206275"></a>

This API is used to query tenant quotas.

## URI<a name="section47638747"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/quotas

-   Parameter description

    **Table  1**  Parameter description

    <a name="table22748199"></a>
    <table><thead align="left"><tr id="row62712396"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59050273"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p18342809"><a name="p18342809"></a><a name="p18342809"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p9372574"><a name="p9372574"></a><a name="p9372574"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p20981015"><a name="p20981015"></a><a name="p20981015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section26095539"></a>

-   Parameter description

    None


-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/quotas
    ```


## Response<a name="section33533260"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table63494180"></a>
    <table><thead align="left"><tr id="row402618"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1621230201117"><a name="p1621230201117"></a><a name="p1621230201117"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p42163010113"><a name="p42163010113"></a><a name="p42163010113"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p72123051117"><a name="p72123051117"></a><a name="p72123051117"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3343372"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2377741"><a name="p2377741"></a><a name="p2377741"></a>quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p31108621"><a name="p31108621"></a><a name="p31108621"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36770396"><a name="p36770396"></a><a name="p36770396"></a>See the <strong id="b56981346142320"><a name="b56981346142320"></a><a name="b56981346142320"></a>quota</strong> field description.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **quota**

    **Table  3**  Parameter description of field  **quota**

    <a name="table25612095"></a>
    <table><thead align="left"><tr id="row63845268"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p998713511112"><a name="p998713511112"></a><a name="p998713511112"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1898719359117"><a name="p1898719359117"></a><a name="p1898719359117"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p32143631115"><a name="p32143631115"></a><a name="p32143631115"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39476433"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43474514"><a name="p43474514"></a><a name="p43474514"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p23617749"><a name="p23617749"></a><a name="p23617749"></a>List&lt;resource_resp&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p33989544"><a name="p33989544"></a><a name="p33989544"></a>Quota resources</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_resp**

    **Table  4**  Parameter description of field  **resource\_resp**

    <a name="table1689659"></a>
    <table><thead align="left"><tr id="row2352317"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p489318421119"><a name="p489318421119"></a><a name="p489318421119"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p10909342111111"><a name="p10909342111111"></a><a name="p10909342111111"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p990904210119"><a name="p990904210119"></a><a name="p990904210119"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20937927"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p18250530"><a name="p18250530"></a><a name="p18250530"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19515197"><a name="p19515197"></a><a name="p19515197"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37227085"><a name="p37227085"></a><a name="p37227085"></a>Unit</p>
    </td>
    </tr>
    <tr id="row66608310"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26564024"><a name="p26564024"></a><a name="p26564024"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p4843821"><a name="p4843821"></a><a name="p4843821"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p56805233"><a name="p56805233"></a><a name="p56805233"></a>Used quota</p>
    </td>
    </tr>
    <tr id="row41485049"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p4845804"><a name="p4845804"></a><a name="p4845804"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50831280"><a name="p50831280"></a><a name="p50831280"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23693009"><a name="p23693009"></a><a name="p23693009"></a>Quota size</p>
    </td>
    </tr>
    <tr id="row11910489"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25225559"><a name="p25225559"></a><a name="p25225559"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14440446"><a name="p14440446"></a><a name="p14440446"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28825462"><a name="p28825462"></a><a name="p28825462"></a>Type</p>
    <p id="p9493432134818"><a name="p9493432134818"></a><a name="p9493432134818"></a><strong id="b12189165934816"><a name="b12189165934816"></a><a name="b12189165934816"></a>backup_capacity</strong> specifies the backup storage capacity quota. Value <strong id="b842352706161346"><a name="b842352706161346"></a><a name="b842352706161346"></a>-1</strong> indicates no restriction on the quota size.</p>
    <p id="p58102567"><a name="p58102567"></a><a name="p58102567"></a><strong id="b1972617237494"><a name="b1972617237494"></a><a name="b1972617237494"></a>backups</strong> specifies the number of retained backups.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "quotas" : {
        "resources" : [{
          "type" : "backup_capacity",
          "unit" : "GB",
          "quota" : -1,
          "used" : 0
        },
        {
            "used": 0,
            "type": "backups",
            "quota": 600
        }]
      }
    }
    ```


## Status Codes<a name="section33363887"></a>

-   Normal

    <a name="table25516615"></a>
    <table><thead align="left"><tr id="row2411478"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p61112063"><a name="p61112063"></a><a name="p61112063"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p51130076"><a name="p51130076"></a><a name="p51130076"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47895510"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p54331092"><a name="p54331092"></a><a name="p54331092"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p38742335"><a name="p38742335"></a><a name="p38742335"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table51121406"></a>
    <table><thead align="left"><tr id="row44111723"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p16279805"><a name="p16279805"></a><a name="p16279805"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p43595815"><a name="p43595815"></a><a name="p43595815"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41600146"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p14168678"><a name="p14168678"></a><a name="p14168678"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p6812233"><a name="p6812233"></a><a name="p6812233"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row61310105"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p62617"><a name="p62617"></a><a name="p62617"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p5071997"><a name="p5071997"></a><a name="p5071997"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row45647976"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p6498590"><a name="p6498590"></a><a name="p6498590"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p56623788"><a name="p56623788"></a><a name="p56623788"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row39852052"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p6790811"><a name="p6790811"></a><a name="p6790811"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p13184781"><a name="p13184781"></a><a name="p13184781"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row51554171"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p15138299"><a name="p15138299"></a><a name="p15138299"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p18242716"><a name="p18242716"></a><a name="p18242716"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row29966720"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p11385269"><a name="p11385269"></a><a name="p11385269"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p49791582"><a name="p49791582"></a><a name="p49791582"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

