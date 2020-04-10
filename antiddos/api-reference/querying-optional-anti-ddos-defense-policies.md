# Querying Optional Anti-DDoS Defense Policies<a name="antiddos_02_0017"></a>

## Function<a name="toc460486713"></a>

This API allows you to query optional Anti-DDoS defense policies. Based on your service, you can select a policy for Anti-DDoS traffic scrubbing.

## URI<a name="section26052191"></a>

-   URI format

    GET /v1/\{project\_id\}/antiddos/query\_config\_list

-   Parameter description

    <a name="table48445579"></a>
    <table><thead align="left"><tr id="row16653875"><th class="cellrowborder" valign="top" width="22.847715228477146%" id="mcps1.1.5.1.1"><p id="p6786611"><a name="p6786611"></a><a name="p6786611"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.60743925607439%" id="mcps1.1.5.1.2"><p id="p12844628"><a name="p12844628"></a><a name="p12844628"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.617938206179375%" id="mcps1.1.5.1.3"><p id="p33781949"><a name="p33781949"></a><a name="p33781949"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.92690730926907%" id="mcps1.1.5.1.4"><p id="p51983383"><a name="p51983383"></a><a name="p51983383"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49904522"><td class="cellrowborder" valign="top" width="22.847715228477146%" headers="mcps1.1.5.1.1 "><p id="p15734461"><a name="p15734461"></a><a name="p15734461"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.60743925607439%" headers="mcps1.1.5.1.2 "><p id="p66531800"><a name="p66531800"></a><a name="p66531800"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.617938206179375%" headers="mcps1.1.5.1.3 "><p id="p20366724"><a name="p20366724"></a><a name="p20366724"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.4 "><p id="p39091944"><a name="p39091944"></a><a name="p39091944"></a>A user's ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section33143133"></a>

-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/query_config_list
    ```


## Response<a name="section29852746"></a>

-   Element description

    <a name="table11887819"></a>
    <table><thead align="left"><tr id="row12791742"><th class="cellrowborder" valign="top" width="30.61%" id="mcps1.1.5.1.1"><p id="p29498151"><a name="p29498151"></a><a name="p29498151"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.46%" id="mcps1.1.5.1.2"><p id="p40539992"><a name="p40539992"></a><a name="p40539992"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.4%" id="mcps1.1.5.1.3"><p id="p62513914"><a name="p62513914"></a><a name="p62513914"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.5.1.4"><p id="p30462260"><a name="p30462260"></a><a name="p30462260"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51524015"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.1.5.1.1 "><p id="p12695699"><a name="p12695699"></a><a name="p12695699"></a>traffic_limited_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.46%" headers="mcps1.1.5.1.2 "><p id="p21718662"><a name="p21718662"></a><a name="p21718662"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.4%" headers="mcps1.1.5.1.3 "><p id="p14381235"><a name="p14381235"></a><a name="p14381235"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.5.1.4 "><p id="p14937794"><a name="p14937794"></a><a name="p14937794"></a>List of traffic limits</p>
    </td>
    </tr>
    <tr id="row222421"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.1.5.1.1 "><p id="p18016155"><a name="p18016155"></a><a name="p18016155"></a>http_limited_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.46%" headers="mcps1.1.5.1.2 "><p id="p50022457"><a name="p50022457"></a><a name="p50022457"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.4%" headers="mcps1.1.5.1.3 "><p id="p25287256"><a name="p25287256"></a><a name="p25287256"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.5.1.4 "><p id="p46581538"><a name="p46581538"></a><a name="p46581538"></a>List of HTTP limits</p>
    </td>
    </tr>
    <tr id="row16580664"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.1.5.1.1 "><p id="p856520"><a name="p856520"></a><a name="p856520"></a>connection_limited_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.46%" headers="mcps1.1.5.1.2 "><p id="p2269305"><a name="p2269305"></a><a name="p2269305"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.4%" headers="mcps1.1.5.1.3 "><p id="p49596018"><a name="p49596018"></a><a name="p49596018"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.5.1.4 "><p id="p50928963"><a name="p50928963"></a><a name="p50928963"></a>List of limits of numbers of connections</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **traffic\_limited\_list**

    <a name="table9895475"></a>
    <table><thead align="left"><tr id="row17224274"><th class="cellrowborder" valign="top" width="27.98%" id="mcps1.1.5.1.1"><p id="p52988976"><a name="p52988976"></a><a name="p52988976"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.96%" id="mcps1.1.5.1.2"><p id="p64248638"><a name="p64248638"></a><a name="p64248638"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.979999999999999%" id="mcps1.1.5.1.3"><p id="p36757156"><a name="p36757156"></a><a name="p36757156"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.08%" id="mcps1.1.5.1.4"><p id="p24539659"><a name="p24539659"></a><a name="p24539659"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41555354"><td class="cellrowborder" valign="top" width="27.98%" headers="mcps1.1.5.1.1 "><p id="p10540538"><a name="p10540538"></a><a name="p10540538"></a>traffic_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.2 "><p id="p48477267"><a name="p48477267"></a><a name="p48477267"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p626126015239"><a name="p626126015239"></a><a name="p626126015239"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.08%" headers="mcps1.1.5.1.4 "><p id="p30443021"><a name="p30443021"></a><a name="p30443021"></a>Position ID of traffic</p>
    </td>
    </tr>
    <tr id="row5551736"><td class="cellrowborder" valign="top" width="27.98%" headers="mcps1.1.5.1.1 "><p id="p47037497"><a name="p47037497"></a><a name="p47037497"></a>traffic_per_second</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.2 "><p id="p51940951"><a name="p51940951"></a><a name="p51940951"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p3938182315247"><a name="p3938182315247"></a><a name="p3938182315247"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.08%" headers="mcps1.1.5.1.4 "><p id="p5772232"><a name="p5772232"></a><a name="p5772232"></a>Threshold of traffic per second (Mbit/s)</p>
    </td>
    </tr>
    <tr id="row51950091"><td class="cellrowborder" valign="top" width="27.98%" headers="mcps1.1.5.1.1 "><p id="p47207880"><a name="p47207880"></a><a name="p47207880"></a>packet_per_second</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.1.5.1.2 "><p id="p65741925"><a name="p65741925"></a><a name="p65741925"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.979999999999999%" headers="mcps1.1.5.1.3 "><p id="p3599349815255"><a name="p3599349815255"></a><a name="p3599349815255"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.08%" headers="mcps1.1.5.1.4 "><p id="p24102752"><a name="p24102752"></a><a name="p24102752"></a>Threshold of number of packets per second</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **http\_limited\_list**

    <a name="table29676093"></a>
    <table><thead align="left"><tr id="row26366538"><th class="cellrowborder" valign="top" width="30.3%" id="mcps1.1.5.1.1"><p id="p55314834"><a name="p55314834"></a><a name="p55314834"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.61%" id="mcps1.1.5.1.2"><p id="p51316583"><a name="p51316583"></a><a name="p51316583"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="11.459999999999999%" id="mcps1.1.5.1.3"><p id="p63002544"><a name="p63002544"></a><a name="p63002544"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.629999999999995%" id="mcps1.1.5.1.4"><p id="p2932438"><a name="p2932438"></a><a name="p2932438"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36200896"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p46591446"><a name="p46591446"></a><a name="p46591446"></a>http_request_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.2 "><p id="p15810818"><a name="p15810818"></a><a name="p15810818"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.459999999999999%" headers="mcps1.1.5.1.3 "><p id="p470492221531"><a name="p470492221531"></a><a name="p470492221531"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.629999999999995%" headers="mcps1.1.5.1.4 "><p id="p51582645"><a name="p51582645"></a><a name="p51582645"></a>Position ID of number of HTTP requests</p>
    </td>
    </tr>
    <tr id="row61590629"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p22785027"><a name="p22785027"></a><a name="p22785027"></a>http_packet_per_second</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.1.5.1.2 "><p id="p33647865"><a name="p33647865"></a><a name="p33647865"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.459999999999999%" headers="mcps1.1.5.1.3 "><p id="p493536161538"><a name="p493536161538"></a><a name="p493536161538"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.629999999999995%" headers="mcps1.1.5.1.4 "><p id="p42591759"><a name="p42591759"></a><a name="p42591759"></a>Threshold of number of HTTP requests per second</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **connection\_limited\_list**

    <a name="table29037097"></a>
    <table><thead align="left"><tr id="row63040734"><th class="cellrowborder" valign="top" width="31.803180318031803%" id="mcps1.1.5.1.1"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.98189818981898%" id="mcps1.1.5.1.2"><p id="p18331773"><a name="p18331773"></a><a name="p18331773"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.1.5.1.3"><p id="p8478608"><a name="p8478608"></a><a name="p8478608"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="36.343634363436344%" id="mcps1.1.5.1.4"><p id="p15678685"><a name="p15678685"></a><a name="p15678685"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62013962"><td class="cellrowborder" valign="top" width="31.803180318031803%" headers="mcps1.1.5.1.1 "><p id="p57075007"><a name="p57075007"></a><a name="p57075007"></a>cleaning_access_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.1.5.1.2 "><p id="p59672869"><a name="p59672869"></a><a name="p59672869"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.5.1.3 "><p id="p1794580015316"><a name="p1794580015316"></a><a name="p1794580015316"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.1.5.1.4 "><p id="p584738"><a name="p584738"></a><a name="p584738"></a>Position ID of access limit during cleaning</p>
    </td>
    </tr>
    <tr id="row5262650"><td class="cellrowborder" valign="top" width="31.803180318031803%" headers="mcps1.1.5.1.1 "><p id="p23621468"><a name="p23621468"></a><a name="p23621468"></a>new_connection_limited</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.1.5.1.2 "><p id="p34290771"><a name="p34290771"></a><a name="p34290771"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.5.1.3 "><p id="p4121372515321"><a name="p4121372515321"></a><a name="p4121372515321"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.1.5.1.4 "><p id="p32841951"><a name="p32841951"></a><a name="p32841951"></a>Number of new connections of a source IP address</p>
    </td>
    </tr>
    <tr id="row27142108"><td class="cellrowborder" valign="top" width="31.803180318031803%" headers="mcps1.1.5.1.1 "><p id="p51027174"><a name="p51027174"></a><a name="p51027174"></a>total_connection_limited</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98189818981898%" headers="mcps1.1.5.1.2 "><p id="p39560457"><a name="p39560457"></a><a name="p39560457"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.5.1.3 "><p id="p6366945115325"><a name="p6366945115325"></a><a name="p6366945115325"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.1.5.1.4 "><p id="p46182839"><a name="p46182839"></a><a name="p46182839"></a>Total number of connections of a source IP address</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

```
{
  "traffic_limited_list": [
    {
      "traffic_pos_id": 1,
      "traffic_per_second": 10,
      "packet_per_second": 2000
    },
    {
      "traffic_pos_id": 2,
      "traffic_per_second": 30,
      "packet_per_second": 6000
    },
    {
      "traffic_pos_id": 3,
      "traffic_per_second": 50,
      "packet_per_second": 10000
    },
    {
      "traffic_pos_id": 4,
      "traffic_per_second": 70,
      "packet_per_second": 15000
    },
    {
      "traffic_pos_id": 5,
      "traffic_per_second": 100,
      "packet_per_second": 20000
    },
    {
      "traffic_pos_id": 6,
      "traffic_per_second": 150,
      "packet_per_second": 25000
    },
    {
      "traffic_pos_id": 7,
      "traffic_per_second": 200,
      "packet_per_second": 35000
    },
    {
      "traffic_pos_id": 8,
      "traffic_per_second": 250,
      "packet_per_second": 50000
    },
    {
      "traffic_pos_id": 9,
      "traffic_per_second": 300,
      "packet_per_second": 70000
    }
  ],
  "http_limited_list": [
    {
      "http_request_pos_id": 1,
      "http_packet_per_second": 100
    },
    {
      "http_request_pos_id": 2,
      "http_packet_per_second": 150
    },
    {
      "http_request_pos_id": 3,
      "http_packet_per_second": 240
    },
    {
      "http_request_pos_id": 4,
      "http_packet_per_second": 350
    },
    {
      "http_request_pos_id": 5,
      "http_packet_per_second": 480
    },
    {
      "http_request_pos_id": 6,
      "http_packet_per_second": 550
    },
    {
      "http_request_pos_id": 7,
      "http_packet_per_second": 700
    },
    {
      "http_request_pos_id": 8,
      "http_packet_per_second": 850
    },
    {
      "http_request_pos_id": 9,
      "http_packet_per_second": 1000
    },
    {
      "http_request_pos_id": 10,
      "http_packet_per_second": 1500
    },
    {
      "http_request_pos_id": 11,
      "http_packet_per_second": 2000
    },
    {
      "http_request_pos_id": 12,
      "http_packet_per_second": 3000
    },
    {
      "http_request_pos_id": 13,
      "http_packet_per_second": 5000
    },
    {
      "http_request_pos_id": 14,
      "http_packet_per_second": 10000
    },
    {
      "http_request_pos_id": 15,
      "http_packet_per_second": 20000
    }
  ],
  "connection_limited_list": [
    {
      "cleaning_access_pos_id": 1,
      "new_connection_limited": 10,
      "total_connection_limited": 30
    },
    {
      "cleaning_access_pos_id": 2,
      "new_connection_limited": 20,
      "total_connection_limited": 100
    },
    {
      "cleaning_access_pos_id": 3,
      "new_connection_limited": 30,
      "total_connection_limited": 200
    },
    {
      "cleaning_access_pos_id": 4,
      "new_connection_limited": 40,
      "total_connection_limited": 250
    },
    {
      "cleaning_access_pos_id": 5,
      "new_connection_limited": 50,
      "total_connection_limited": 300
    },
    {
      "cleaning_access_pos_id": 6,
      "new_connection_limited": 60,
      "total_connection_limited": 500
    },
    {
      "cleaning_access_pos_id": 7,
      "new_connection_limited": 70,
      "total_connection_limited": 600
    },
    {
      "cleaning_access_pos_id": 8,
      "new_connection_limited": 80,
      "total_connection_limited": 700
    }
  ],
  "extend_ddos_config": [
    {
      "new_connection_limited": 80,
      "total_connection_limited": 700,
      "http_packet_per_second": 500000,
      "traffic_per_second": 1000,
      "packet_per_second": 200000,
      "setID": 33
    },
    {
      "new_connection_limited": 80,
      "total_connection_limited": 700,
      "http_packet_per_second": 500000,
      "traffic_per_second": 2000,
      "packet_per_second": 200000,
      "setID": 34
    },
    {
      "new_connection_limited": 80,
      "total_connection_limited": 700,
      "http_packet_per_second": 500000,
      "traffic_per_second": 5000,
      "packet_per_second": 400000,
      "setID": 35
    },
    {
      "new_connection_limited": 80,
      "total_connection_limited": 700,
      "http_packet_per_second": 0,
      "traffic_per_second": 0,
      "packet_per_second": 0,
      "setID": 36
    }
  ]
}
```

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The  **extend\_ddos\_config**  field displays information about Anti-DDoS defense policies set by users based on their needs.   

## Returned Value<a name="section239263"></a>

See  [Status Code](status-code.md).

