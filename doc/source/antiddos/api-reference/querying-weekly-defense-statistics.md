# Querying Weekly Defense Statistics<a name="antiddos_02_0027"></a>

## Functions<a name="section63597034"></a>

This API allows you to query weekly defense statistics about all your EIPs, including the number of intercepted DDoS attacks, number of attacks, and ranking by the number of attacks. Currently, you can query weekly statistics up to four weeks before the current time. Data older than four weeks cannot be queried.

## URI<a name="section35502400"></a>

-   URI format

    GET /v1/\{project\_id\}/antiddos/weekly

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can use  **?**  and  **&**  behind the URI to add query conditions, as shown in the request example.  


-   Parameter description

    <a name="table21758931"></a>
    <table><thead align="left"><tr id="row3371364"><th class="cellrowborder" valign="top" width="22.68%" id="mcps1.1.5.1.1"><p id="p4645057"><a name="p4645057"></a><a name="p4645057"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.689999999999998%" id="mcps1.1.5.1.2"><p id="p40705318"><a name="p40705318"></a><a name="p40705318"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.309999999999999%" id="mcps1.1.5.1.3"><p id="p8796476"><a name="p8796476"></a><a name="p8796476"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.32%" id="mcps1.1.5.1.4"><p id="p41425962"><a name="p41425962"></a><a name="p41425962"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62092003153657"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.5.1.1 "><p id="p312432915377"><a name="p312432915377"></a><a name="p312432915377"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.2 "><p id="p5174406715377"><a name="p5174406715377"></a><a name="p5174406715377"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.309999999999999%" headers="mcps1.1.5.1.3 "><p id="p3051988115377"><a name="p3051988115377"></a><a name="p3051988115377"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.32%" headers="mcps1.1.5.1.4 "><p id="p5619133315377"><a name="p5619133315377"></a><a name="p5619133315377"></a>A user's ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section51086148"></a>

-   Parameter description

    <a name="table4679845412"></a>
    <table><thead align="left"><tr id="row468410444120"><th class="cellrowborder" valign="top" width="22.682268226822682%" id="mcps1.1.5.1.1"><p id="p2685164124115"><a name="p2685164124115"></a><a name="p2685164124115"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.18181818181818%" id="mcps1.1.5.1.2"><p id="p26879419416"><a name="p26879419416"></a><a name="p26879419416"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.13161316131613%" id="mcps1.1.5.1.3"><p id="p176891647414"><a name="p176891647414"></a><a name="p176891647414"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.004300430043%" id="mcps1.1.5.1.4"><p id="p126913434120"><a name="p126913434120"></a><a name="p126913434120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1169917434116"><td class="cellrowborder" valign="top" width="22.682268226822682%" headers="mcps1.1.5.1.1 "><p id="p1769954144120"><a name="p1769954144120"></a><a name="p1769954144120"></a>period_start_date</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.1.5.1.2 "><p id="p870114164120"><a name="p870114164120"></a><a name="p870114164120"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13161316131613%" headers="mcps1.1.5.1.3 "><p id="p970212464115"><a name="p970212464115"></a><a name="p970212464115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.004300430043%" headers="mcps1.1.5.1.4 "><p id="p8703164124118"><a name="p8703164124118"></a><a name="p8703164124118"></a>Start date of a seven-day period</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/weekly?period_start_date=1006510306
    ```


## Response<a name="section57122151"></a>

-   Element description

    <a name="table15327568"></a>
    <table><thead align="left"><tr id="row24486356"><th class="cellrowborder" valign="top" width="28.599999999999998%" id="mcps1.1.4.1.1"><p id="p37237828"><a name="p37237828"></a><a name="p37237828"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.42%" id="mcps1.1.4.1.2"><p id="p63474072"><a name="p63474072"></a><a name="p63474072"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.980000000000004%" id="mcps1.1.4.1.3"><p id="p41126201"><a name="p41126201"></a><a name="p41126201"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42887950"><td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.1.4.1.1 "><p id="p51371903"><a name="p51371903"></a><a name="p51371903"></a>ddos_intercept_times</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.1.4.1.2 "><p id="p2142367152712"><a name="p2142367152712"></a><a name="p2142367152712"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.1.4.1.3 "><p id="p30346328"><a name="p30346328"></a><a name="p30346328"></a>Number of DDoS attacks blocked in a week</p>
    </td>
    </tr>
    <tr id="row4681502"><td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.1.4.1.1 "><p id="p43657358"><a name="p43657358"></a><a name="p43657358"></a>weekdata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.1.4.1.2 "><p id="p46585119"><a name="p46585119"></a><a name="p46585119"></a>Data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.1.4.1.3 "><p id="p15298296"><a name="p15298296"></a><a name="p15298296"></a>Number of attacks in a week</p>
    </td>
    </tr>
    <tr id="row3466944"><td class="cellrowborder" valign="top" width="28.599999999999998%" headers="mcps1.1.4.1.1 "><p id="p12387033"><a name="p12387033"></a><a name="p12387033"></a>top10</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.1.4.1.2 "><p id="p63825615"><a name="p63825615"></a><a name="p63825615"></a>Data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.1.4.1.3 "><p id="p2492297"><a name="p2492297"></a><a name="p2492297"></a>Top 10 attacked IP addresses</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **weekdata**

    <a name="table44508523"></a>
    <table><thead align="left"><tr id="row13604004"><th class="cellrowborder" valign="top" width="29.48%" id="mcps1.1.5.1.1"><p id="p28182506"><a name="p28182506"></a><a name="p28182506"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.59%" id="mcps1.1.5.1.2"><p id="p1081649"><a name="p1081649"></a><a name="p1081649"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="11.17%" id="mcps1.1.5.1.3"><p id="p20504736"><a name="p20504736"></a><a name="p20504736"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.760000000000005%" id="mcps1.1.5.1.4"><p id="p50270944"><a name="p50270944"></a><a name="p50270944"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45414681"><td class="cellrowborder" valign="top" width="29.48%" headers="mcps1.1.5.1.1 "><p id="p54710514"><a name="p54710514"></a><a name="p54710514"></a>ddos_intercept_times</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.1.5.1.2 "><p id="p2366611"><a name="p2366611"></a><a name="p2366611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.17%" headers="mcps1.1.5.1.3 "><p id="p53636340152723"><a name="p53636340152723"></a><a name="p53636340152723"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.760000000000005%" headers="mcps1.1.5.1.4 "><p id="p25189967"><a name="p25189967"></a><a name="p25189967"></a>Number of DDoS attacks blocked</p>
    </td>
    </tr>
    <tr id="row25383117"><td class="cellrowborder" valign="top" width="29.48%" headers="mcps1.1.5.1.1 "><p id="p42766607"><a name="p42766607"></a><a name="p42766607"></a>ddos_blackhole_times</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.1.5.1.2 "><p id="p41543166"><a name="p41543166"></a><a name="p41543166"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.17%" headers="mcps1.1.5.1.3 "><p id="p65381003152726"><a name="p65381003152726"></a><a name="p65381003152726"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.760000000000005%" headers="mcps1.1.5.1.4 "><p id="p35618305"><a name="p35618305"></a><a name="p35618305"></a>Number of DDoS black holes</p>
    </td>
    </tr>
    <tr id="row52129291"><td class="cellrowborder" valign="top" width="29.48%" headers="mcps1.1.5.1.1 "><p id="p61723024"><a name="p61723024"></a><a name="p61723024"></a>max_attack_bps</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.1.5.1.2 "><p id="p33509062"><a name="p33509062"></a><a name="p33509062"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.17%" headers="mcps1.1.5.1.3 "><p id="p53706368152730"><a name="p53706368152730"></a><a name="p53706368152730"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.760000000000005%" headers="mcps1.1.5.1.4 "><p id="p4321123"><a name="p4321123"></a><a name="p4321123"></a>Maximum attack traffic</p>
    </td>
    </tr>
    <tr id="row38890115"><td class="cellrowborder" valign="top" width="29.48%" headers="mcps1.1.5.1.1 "><p id="p63091573"><a name="p63091573"></a><a name="p63091573"></a>max_attack_conns</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.1.5.1.2 "><p id="p10143804"><a name="p10143804"></a><a name="p10143804"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.17%" headers="mcps1.1.5.1.3 "><p id="p58619775152733"><a name="p58619775152733"></a><a name="p58619775152733"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.760000000000005%" headers="mcps1.1.5.1.4 "><p id="p48619368"><a name="p48619368"></a><a name="p48619368"></a>Maximum number of attack connections</p>
    </td>
    </tr>
    <tr id="row34921133"><td class="cellrowborder" valign="top" width="29.48%" headers="mcps1.1.5.1.1 "><p id="p10039559"><a name="p10039559"></a><a name="p10039559"></a>period_start_date</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.1.5.1.2 "><p id="p7897978"><a name="p7897978"></a><a name="p7897978"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.17%" headers="mcps1.1.5.1.3 "><p id="p35756461"><a name="p35756461"></a><a name="p35756461"></a>Long integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.760000000000005%" headers="mcps1.1.5.1.4 "><p id="p10592200"><a name="p10592200"></a><a name="p10592200"></a>Start date</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **top10**

    <a name="table37753560"></a>
    <table><thead align="left"><tr id="row63016113"><th class="cellrowborder" valign="top" width="26.532653265326534%" id="mcps1.1.5.1.1"><p id="p4031547"><a name="p4031547"></a><a name="p4031547"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.771877187718776%" id="mcps1.1.5.1.2"><p id="p58119881"><a name="p58119881"></a><a name="p58119881"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.051205120512053%" id="mcps1.1.5.1.3"><p id="p10089924"><a name="p10089924"></a><a name="p10089924"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.644264426442646%" id="mcps1.1.5.1.4"><p id="p11977491"><a name="p11977491"></a><a name="p11977491"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30652703"><td class="cellrowborder" valign="top" width="26.532653265326534%" headers="mcps1.1.5.1.1 "><p id="p66949839"><a name="p66949839"></a><a name="p66949839"></a>floating_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.771877187718776%" headers="mcps1.1.5.1.2 "><p id="p54227851"><a name="p54227851"></a><a name="p54227851"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.051205120512053%" headers="mcps1.1.5.1.3 "><p id="p30379836"><a name="p30379836"></a><a name="p30379836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.644264426442646%" headers="mcps1.1.5.1.4 "><p id="p44847690"><a name="p44847690"></a><a name="p44847690"></a>EIP</p>
    </td>
    </tr>
    <tr id="row976031"><td class="cellrowborder" valign="top" width="26.532653265326534%" headers="mcps1.1.5.1.1 "><p id="p11949699"><a name="p11949699"></a><a name="p11949699"></a>times</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.771877187718776%" headers="mcps1.1.5.1.2 "><p id="p28401526"><a name="p28401526"></a><a name="p28401526"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.051205120512053%" headers="mcps1.1.5.1.3 "><p id="p40695790152738"><a name="p40695790152738"></a><a name="p40695790152738"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.644264426442646%" headers="mcps1.1.5.1.4 "><p id="p48211888"><a name="p48211888"></a><a name="p48211888"></a>Number of DDoS attacks intercepted, including cleaning operations and black holes</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
       "ddos_intercept_times": 23,
       "weekdata": [
          {
             "ddos_intercept_times": 0,
             "ddos_blackhole_times": 0,
             "max_attack_bps": 0,
             "max_attack_conns": 0,
             "period_start_date": 1474214461651
          },
          {
             "ddos_intercept_times": 0,
             "ddos_blackhole_times": 0,
             "max_attack_bps": 0,
             "max_attack_conns": 0,
             "period_start_date": 1474300861651
          },
          {
             "ddos_intercept_times": 0,
             "ddos_blackhole_times": 0,
             "max_attack_bps": 0,
             "max_attack_conns": 0,
             "period_start_date": 1474387261651
          },
          {
             "ddos_intercept_times": 0,
             "ddos_blackhole_times": 0,
             "max_attack_bps": 0,
             "max_attack_conns": 0,
             "period_start_date": 1474473661651
          },
          {
             "ddos_intercept_times": 0,
             "ddos_blackhole_times": 0,
             "max_attack_bps": 0,
             "max_attack_conns": 0,
             "period_start_date": 1474560061651
          },
          {
             "ddos_intercept_times": 2,
             "ddos_blackhole_times": 0,
             "max_attack_bps": 16375,
             "max_attack_conns": 0,
             "period_start_date": 1474646461651
          },
          {
             "ddos_intercept_times": 1,
             "ddos_blackhole_times": 0,
             "max_attack_bps": 0,
             "max_attack_conns": 0,
             "period_start_date": 1474732861651
          }
       ],
       "top10": [
          {
             "floating_ip_address": "192.168.44.69",
             "times": 23
          }
       ]
    }
    ```


## Returned Value<a name="section44337314"></a>

See  [Status Code](status-code.md).

