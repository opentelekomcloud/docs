# Querying IP Address Usage on a Specified Network<a name="vpc_natworkip_0001"></a>

## Function<a name="section1398541881511"></a>

This API is used to query the IP address usage on a specified network.

The obtained information includes the total number of IP addresses on the network, the number of in-use IP addresses on the network, the total number of IP addresses on each subnet, and the number of in-use IP addresses on the subnet.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>-   The first and last four IP addresses on each subnet are reserved by the system for the gateway and DHCP service.  
>-   The total number of IP addresses and the number of in-use IP addresses described in this section and the subsequent sections do not include the IP addresses reserved by the system.  
>-   When assigning an IP address, you can specify the reserved IP address for the system. The system reserved IP address will not be included in the number of in-use IP addresses and the total number of IP addresses no matter how the IP address is assigned.  

## URI<a name="section5633932181719"></a>

GET /v2.0/network-ip-availabilities/\{network\_id\}

[Table 1](#table38148684)  describes the parameters.

**Table  1**  Parameter description

<a name="table38148684"></a>
<table><thead align="left"><tr id="row7162954"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.5.1.1"><p id="p43328398"><a name="p43328398"></a><a name="p43328398"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.29%" id="mcps1.2.5.1.2"><p id="p19939379"><a name="p19939379"></a><a name="p19939379"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.36%" id="mcps1.2.5.1.3"><p id="p4477025"><a name="p4477025"></a><a name="p4477025"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="40.839999999999996%" id="mcps1.2.5.1.4"><p id="p27094719"><a name="p27094719"></a><a name="p27094719"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row47188597"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.1 "><p id="p64180012"><a name="p64180012"></a><a name="p64180012"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.2.5.1.2 "><p id="p31198475"><a name="p31198475"></a><a name="p31198475"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.3 "><p id="p44048571"><a name="p44048571"></a><a name="p44048571"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.839999999999996%" headers="mcps1.2.5.1.4 "><p id="p11164516"><a name="p11164516"></a><a name="p11164516"></a>Specifies the network ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section447915459203"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v2.0/network-ip-availabilities/6b50d967-779c-40c9-a157-de1df3c17043
    ```


## Response Message<a name="section752610492226"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table966523163317"></a>
    <table><thead align="left"><tr id="row966563103315"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p866615363313"><a name="p866615363313"></a><a name="p866615363313"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p8666143153316"><a name="p8666143153316"></a><a name="p8666143153316"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p66667320335"><a name="p66667320335"></a><a name="p66667320335"></a><strong id="b1278600137"><a name="b1278600137"></a><a name="b1278600137"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1166619314334"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p176661383319"><a name="p176661383319"></a><a name="p176661383319"></a>network_ip_availability</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p12666439333"><a name="p12666439333"></a><a name="p12666439333"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p666612311331"><a name="p666612311331"></a><a name="p666612311331"></a>Specifies the <strong id="b8305211437"><a name="b8305211437"></a><a name="b8305211437"></a>network_ip_avalability</strong> objects. For details, see <a href="#table4952133061113">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **network\_ip\_availability**  objects

    <a name="table4952133061113"></a>
    <table><thead align="left"><tr id="row59521030171119"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p109521330171118"><a name="p109521330171118"></a><a name="p109521330171118"></a><strong id="b1641635284315"><a name="b1641635284315"></a><a name="b1641635284315"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p20952113013119"><a name="p20952113013119"></a><a name="p20952113013119"></a><strong id="b198982119"><a name="b198982119"></a><a name="b198982119"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p79525309113"><a name="p79525309113"></a><a name="p79525309113"></a><strong id="b97551055184311"><a name="b97551055184311"></a><a name="b97551055184311"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17952113001111"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p18952103061110"><a name="p18952103061110"></a><a name="p18952103061110"></a>network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p9954103081111"><a name="p9954103081111"></a><a name="p9954103081111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p16954130171120"><a name="p16954130171120"></a><a name="p16954130171120"></a>Specifies the network ID.</p>
    </td>
    </tr>
    <tr id="row19954133091119"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p11954193013117"><a name="p11954193013117"></a><a name="p11954193013117"></a>network_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p195413091117"><a name="p195413091117"></a><a name="p195413091117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p19541130111110"><a name="p19541130111110"></a><a name="p19541130111110"></a>Specifies the network name.</p>
    </td>
    </tr>
    <tr id="row159543309110"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1295443001116"><a name="p1295443001116"></a><a name="p1295443001116"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p18954430201118"><a name="p18954430201118"></a><a name="p18954430201118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row13954730161115"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p39551930121112"><a name="p39551930121112"></a><a name="p39551930121112"></a>total_ips</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p179551630111114"><a name="p179551630111114"></a><a name="p179551630111114"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p119559304119"><a name="p119559304119"></a><a name="p119559304119"></a>Specifies the total number of IP addresses on a network. (System reserved IP addresses are not included.)</p>
    </td>
    </tr>
    <tr id="row295553016117"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p59551830161120"><a name="p59551830161120"></a><a name="p59551830161120"></a>used_ips</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p14955113081119"><a name="p14955113081119"></a><a name="p14955113081119"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p17955193011112"><a name="p17955193011112"></a><a name="p17955193011112"></a>Specifies the number of in-use IP addresses on a network. (System reserved IP addresses are not included.)</p>
    </td>
    </tr>
    <tr id="row6955830121114"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p19955103061116"><a name="p19955103061116"></a><a name="p19955103061116"></a>subnet_ip_availability</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p89556306114"><a name="p89556306114"></a><a name="p89556306114"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1395513031116"><a name="p1395513031116"></a><a name="p1395513031116"></a>Specifies the subnet IP address usage objects. For details, see <a href="#table110015141519">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **subnet\_ip\_availability**  field

    <a name="table110015141519"></a>
    <table><thead align="left"><tr id="row5101145151518"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.1"><p id="p610120518150"><a name="p610120518150"></a><a name="p610120518150"></a><strong id="b11173122913451"><a name="b11173122913451"></a><a name="b11173122913451"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.2"><p id="p10101105171513"><a name="p10101105171513"></a><a name="p10101105171513"></a><strong id="b1918023134512"><a name="b1918023134512"></a><a name="b1918023134512"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.339999999999996%" id="mcps1.2.4.1.3"><p id="p5101145151519"><a name="p5101145151519"></a><a name="p5101145151519"></a><strong id="b9193132174511"><a name="b9193132174511"></a><a name="b9193132174511"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12101751141514"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p110185111151"><a name="p110185111151"></a><a name="p110185111151"></a>used_ips</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.2 "><p id="p9102155131519"><a name="p9102155131519"></a><a name="p9102155131519"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p21021251151518"><a name="p21021251151518"></a><a name="p21021251151518"></a>Specifies the number of in-use IP addresses on a subnet. (System reserved IP addresses are not included.)</p>
    </td>
    </tr>
    <tr id="row10967175517178"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p12968105517179"><a name="p12968105517179"></a><a name="p12968105517179"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.2 "><p id="p4968175511716"><a name="p4968175511716"></a><a name="p4968175511716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p17968175591718"><a name="p17968175591718"></a><a name="p17968175591718"></a>Specifies the subnet ID.</p>
    </td>
    </tr>
    <tr id="row172761838198"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p42761137197"><a name="p42761137197"></a><a name="p42761137197"></a>subnet_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.2 "><p id="p7276735198"><a name="p7276735198"></a><a name="p7276735198"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p19276193141915"><a name="p19276193141915"></a><a name="p19276193141915"></a>Specifies the subnet name.</p>
    </td>
    </tr>
    <tr id="row28750203194"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p128759204193"><a name="p128759204193"></a><a name="p128759204193"></a>ip_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.2 "><p id="p987532012194"><a name="p987532012194"></a><a name="p987532012194"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p168761720161914"><a name="p168761720161914"></a><a name="p168761720161914"></a>Specifies the IP address version of the subnet. The value can be <strong id="b178848339461"><a name="b178848339461"></a><a name="b178848339461"></a>4</strong> or <strong id="b1335093716465"><a name="b1335093716465"></a><a name="b1335093716465"></a>6</strong>.</p>
    </td>
    </tr>
    <tr id="row1247822162114"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p047815214214"><a name="p047815214214"></a><a name="p047815214214"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.2 "><p id="p1647820252111"><a name="p1647820252111"></a><a name="p1647820252111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p1147842182113"><a name="p1147842182113"></a><a name="p1147842182113"></a>Specifies the subnet CIDR block.</p>
    </td>
    </tr>
    <tr id="row18913174252716"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p19141942112712"><a name="p19141942112712"></a><a name="p19141942112712"></a>total_ips</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.2 "><p id="p209141142102720"><a name="p209141142102720"></a><a name="p209141142102720"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p13914942152716"><a name="p13914942152716"></a><a name="p13914942152716"></a>Specifies the total number of IP addresses on a subnet. (System reserved IP addresses are not included.)</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "network_ip_availability": {
        "used_ips": 4,
        "subnet_ip_availability": [
          {
            "used_ips": 4,
            "subnet_id": "98e343d1-3cb8-4f69-9cd1-00569819480f",
            "subnet_name": "",
            "ip_version": 4,
            "cidr": "10.0.0.0/8",
            "total_ips": 300
          }
        ],
        "network_id": "6b50d967-779c-40c9-a157-de1df3c17043",
        "tenant_id": "7c4b23cb125d481c95cbe4f91b2c11cd",
        "total_ips": 300,
        "network_name": "pch_test_003"
      }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

