# Querying Events of a Specified EIP<a name="antiddos_02_0026"></a>

## Function<a name="section8942221"></a>

This API allows you to query events of a specified EIP in the last 24 hours. Events include cleaning and blackhole events, and the query delay is within five minutes.

## URI<a name="section13371131"></a>

-   URI format

    GET /v1/\{project\_id\}/antiddos/\{floating\_ip\_id\}/logs

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >You can use  **?** and **&**  behind the URI to add query conditions, as shown in the request example.


-   Parameter description

    <a name="table12728880"></a>
    <table><thead align="left"><tr id="row10054985"><th class="cellrowborder" valign="top" width="16.16%" id="mcps1.1.5.1.1"><p id="p9147475"><a name="p9147475"></a><a name="p9147475"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.1.5.1.2"><p id="p2748001"><a name="p2748001"></a><a name="p2748001"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="11.93%" id="mcps1.1.5.1.3"><p id="p21261532"><a name="p21261532"></a><a name="p21261532"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.68000000000001%" id="mcps1.1.5.1.4"><p id="p44462507"><a name="p44462507"></a><a name="p44462507"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4777932153447"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.1.5.1.1 "><p id="p5325329815351"><a name="p5325329815351"></a><a name="p5325329815351"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p1854992115351"><a name="p1854992115351"></a><a name="p1854992115351"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.93%" headers="mcps1.1.5.1.3 "><p id="p2614866515351"><a name="p2614866515351"></a><a name="p2614866515351"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.1.5.1.4 "><p id="p3766710515351"><a name="p3766710515351"></a><a name="p3766710515351"></a>A user's ID</p>
    </td>
    </tr>
    <tr id="row58945129153451"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.1.5.1.1 "><p id="p1179431815351"><a name="p1179431815351"></a><a name="p1179431815351"></a>floating_ip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p1581570215351"><a name="p1581570215351"></a><a name="p1581570215351"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.93%" headers="mcps1.1.5.1.3 "><p id="p600349915351"><a name="p600349915351"></a><a name="p600349915351"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.1.5.1.4 "><p id="p1652139615351"><a name="p1652139615351"></a><a name="p1652139615351"></a>ID corresponding to the EIP of a user</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section9319803"></a>

-   Parameter description

    <a name="table29941125133911"></a>
    <table><thead align="left"><tr id="row1599716259399"><th class="cellrowborder" valign="top" width="24.80751924807519%" id="mcps1.1.5.1.1"><p id="p899972514398"><a name="p899972514398"></a><a name="p899972514398"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.348365163483653%" id="mcps1.1.5.1.2"><p id="p81162683919"><a name="p81162683919"></a><a name="p81162683919"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.508449155084492%" id="mcps1.1.5.1.3"><p id="p142192673917"><a name="p142192673917"></a><a name="p142192673917"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.335666433356664%" id="mcps1.1.5.1.4"><p id="p15411266392"><a name="p15411266392"></a><a name="p15411266392"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row315126183915"><td class="cellrowborder" valign="top" width="24.80751924807519%" headers="mcps1.1.5.1.1 "><p id="p191614268395"><a name="p191614268395"></a><a name="p191614268395"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.348365163483653%" headers="mcps1.1.5.1.2 "><p id="p141722613918"><a name="p141722613918"></a><a name="p141722613918"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.508449155084492%" headers="mcps1.1.5.1.3 "><p id="p181813267392"><a name="p181813267392"></a><a name="p181813267392"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.335666433356664%" headers="mcps1.1.5.1.4 "><p id="p112052610392"><a name="p112052610392"></a><a name="p112052610392"></a>Limit of number of returned results or the maximum number of returned results of a query. The value ranges from 1 to 100, and this parameter is used together with the <span class="parmname" id="parmname769647905144327"><a name="parmname769647905144327"></a><a name="parmname769647905144327"></a><b>offset</b></span> parameter.</p>
    <p id="p15201026193916"><a name="p15201026193916"></a><a name="p15201026193916"></a>If neither <span class="parmname" id="parmname1938148844144344"><a name="parmname1938148844144344"></a><a name="parmname1938148844144344"></a><b>limit</b></span>&nbsp;nor&nbsp;<span class="parmname" id="parmname1749591609144344"><a name="parmname1749591609144344"></a><a name="parmname1749591609144344"></a><b>offset</b></span> is used, query results of all ECSs are returned.</p>
    </td>
    </tr>
    <tr id="row1722192643912"><td class="cellrowborder" valign="top" width="24.80751924807519%" headers="mcps1.1.5.1.1 "><p id="p1223126183917"><a name="p1223126183917"></a><a name="p1223126183917"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.348365163483653%" headers="mcps1.1.5.1.2 "><p id="p1024426113918"><a name="p1024426113918"></a><a name="p1024426113918"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.508449155084492%" headers="mcps1.1.5.1.3 "><p id="p152542616395"><a name="p152542616395"></a><a name="p152542616395"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.335666433356664%" headers="mcps1.1.5.1.4 "><p id="p122672614393"><a name="p122672614393"></a><a name="p122672614393"></a>Offset. This parameter is valid only when used together with the <span class="parmname" id="parmname528723325144828"><a name="parmname528723325144828"></a><a name="parmname528723325144828"></a><b>limit</b></span> parameter.</p>
    </td>
    </tr>
    <tr id="row19271126113914"><td class="cellrowborder" valign="top" width="24.80751924807519%" headers="mcps1.1.5.1.1 "><p id="p152811266391"><a name="p152811266391"></a><a name="p152811266391"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.348365163483653%" headers="mcps1.1.5.1.2 "><p id="p10305264390"><a name="p10305264390"></a><a name="p10305264390"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.508449155084492%" headers="mcps1.1.5.1.3 "><p id="p43118268396"><a name="p43118268396"></a><a name="p43118268396"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.335666433356664%" headers="mcps1.1.5.1.4 "><div class="p" id="p163112616393"><a name="p163112616393"></a><a name="p163112616393"></a>Possible values:<a name="ul15321626123912"></a><a name="ul15321626123912"></a><ul id="ul15321626123912"><li><span class="parmvalue" id="parmvalue55512574414498"><a name="parmvalue55512574414498"></a><a name="parmvalue55512574414498"></a><b>desc</b></span>: indicates that query results are given and sorted by time in descending order.</li><li><span class="parmvalue" id="parmvalue981466981144937"><a name="parmvalue981466981144937"></a><a name="parmvalue981466981144937"></a><b>asc</b></span>: indicates that query results are given and sorted by time in ascending order.</li></ul>
    </div>
    <p id="p23522617395"><a name="p23522617395"></a><a name="p23522617395"></a>The default value is <span class="parmvalue" id="parmvalue103515263397"><a name="parmvalue103515263397"></a><a name="parmvalue103515263397"></a><b>desc</b></span>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/1df977c2-fdc6-4483-bc1c-ba46829f57b8/logs
    ```


## Response<a name="section16769368"></a>

-   Element description

    <a name="table45106256"></a>
    <table><thead align="left"><tr id="row27807639"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.1.4.1.1"><p id="p37826280"><a name="p37826280"></a><a name="p37826280"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="31.313131313131308%" id="mcps1.1.4.1.2"><p id="p44029805"><a name="p44029805"></a><a name="p44029805"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.1.4.1.3"><p id="p9644430"><a name="p9644430"></a><a name="p9644430"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43001397"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.4.1.1 "><p id="p60561095"><a name="p60561095"></a><a name="p60561095"></a>total</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131308%" headers="mcps1.1.4.1.2 "><p id="p43167711152327"><a name="p43167711152327"></a><a name="p43167711152327"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.4.1.3 "><p id="p56873938"><a name="p56873938"></a><a name="p56873938"></a>Total number of EIPs</p>
    </td>
    </tr>
    <tr id="row42103398"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.4.1.1 "><p id="p54932079"><a name="p54932079"></a><a name="p54932079"></a>logs</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131308%" headers="mcps1.1.4.1.2 "><p id="p20313449"><a name="p20313449"></a><a name="p20313449"></a>Data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.4.1.3 "><p id="p34776700"><a name="p34776700"></a><a name="p34776700"></a>List of events</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **logs**

    <a name="table66901514"></a>
    <table><thead align="left"><tr id="row55903933"><th class="cellrowborder" valign="top" width="25.16%" id="mcps1.1.5.1.1"><p id="p31924758"><a name="p31924758"></a><a name="p31924758"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.09%" id="mcps1.1.5.1.2"><p id="p35768611"><a name="p35768611"></a><a name="p35768611"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.37%" id="mcps1.1.5.1.3"><p id="p11576397"><a name="p11576397"></a><a name="p11576397"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="37.38%" id="mcps1.1.5.1.4"><p id="p65272955"><a name="p65272955"></a><a name="p65272955"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52618006"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.1.5.1.1 "><p id="p34200069"><a name="p34200069"></a><a name="p34200069"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p18742193"><a name="p18742193"></a><a name="p18742193"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.1.5.1.3 "><p id="p41722625"><a name="p41722625"></a><a name="p41722625"></a>Long integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.38%" headers="mcps1.1.5.1.4 "><p id="p24089437"><a name="p24089437"></a><a name="p24089437"></a>Start time</p>
    </td>
    </tr>
    <tr id="row15478348"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.1.5.1.1 "><p id="p45786662"><a name="p45786662"></a><a name="p45786662"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p17732161"><a name="p17732161"></a><a name="p17732161"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.1.5.1.3 "><p id="p27018949"><a name="p27018949"></a><a name="p27018949"></a>Long integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.38%" headers="mcps1.1.5.1.4 "><p id="p41051224"><a name="p41051224"></a><a name="p41051224"></a>End time</p>
    </td>
    </tr>
    <tr id="row33916704"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.1.5.1.1 "><p id="p62898512"><a name="p62898512"></a><a name="p62898512"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p61614692"><a name="p61614692"></a><a name="p61614692"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.1.5.1.3 "><p id="p44557253152337"><a name="p44557253152337"></a><a name="p44557253152337"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.38%" headers="mcps1.1.5.1.4 "><div class="p" id="p57309018"><a name="p57309018"></a><a name="p57309018"></a>Defense status, the possible value of which is one of the following:<a name="ul46019115"></a><a name="ul46019115"></a><ul id="ul46019115"><li><span class="parmvalue" id="parmvalue1506354986114925"><a name="parmvalue1506354986114925"></a><a name="parmvalue1506354986114925"></a><b>1</b></span>: indicates that traffic cleaning is underway.</li><li><span class="parmvalue" id="parmvalue1400332350143613"><a name="parmvalue1400332350143613"></a><a name="parmvalue1400332350143613"></a><b>2</b></span>: indicates that traffic is discarded.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row60612418"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.1.5.1.1 "><p id="p10658788"><a name="p10658788"></a><a name="p10658788"></a>trigger_bps</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p58055515"><a name="p58055515"></a><a name="p58055515"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.1.5.1.3 "><p id="p15266258152342"><a name="p15266258152342"></a><a name="p15266258152342"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.38%" headers="mcps1.1.5.1.4 "><p id="p59436263"><a name="p59436263"></a><a name="p59436263"></a>Traffic at the triggering point</p>
    </td>
    </tr>
    <tr id="row65164324"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.1.5.1.1 "><p id="p43818926"><a name="p43818926"></a><a name="p43818926"></a>trigger_pps</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p59672145"><a name="p59672145"></a><a name="p59672145"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.1.5.1.3 "><p id="p57307436152346"><a name="p57307436152346"></a><a name="p57307436152346"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.38%" headers="mcps1.1.5.1.4 "><p id="p62941183"><a name="p62941183"></a><a name="p62941183"></a>Packet rate at the triggering point</p>
    </td>
    </tr>
    <tr id="row29599739"><td class="cellrowborder" valign="top" width="25.16%" headers="mcps1.1.5.1.1 "><p id="p48768695"><a name="p48768695"></a><a name="p48768695"></a>trigger_http_pps</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.09%" headers="mcps1.1.5.1.2 "><p id="p57950190"><a name="p57950190"></a><a name="p57950190"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.1.5.1.3 "><p id="p51299491152351"><a name="p51299491152351"></a><a name="p51299491152351"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.38%" headers="mcps1.1.5.1.4 "><p id="p39486963"><a name="p39486963"></a><a name="p39486963"></a>HTTP request rate at the triggering point</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
       "total": 1,
       "logs": [
          {
             "start_time": 1473217200000,
             "end_time": 1473242400000,
             "status": 1,
             "trigger_bps": 51106,
             "trigger_pps": 2600,
             "trigger_http_pps": 3589
          }
       ]
    }
    ```


## Returned Value<a name="section16706588"></a>

See  [Status Code](status-code.md).

