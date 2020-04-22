# Querying the List of Defense Statuses of EIPs<a name="antiddos_02_0023"></a>

## Function<a name="section52441537"></a>

This API enables you to query the defense statuses of all EIPs, regardless whether an EIP has been bound to an Elastic Cloud Server \(ECS\) or not.

## URI<a name="section2211792"></a>

-   URI format

    GET /v1/\{project\_id\}/antiddos

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can use  **?**  and  **&**  behind the URI to add query conditions, as shown in the request example.  


-   Parameter description

    <a name="table41565035"></a>
    <table><thead align="left"><tr id="row37005770"><th class="cellrowborder" valign="top" width="17.5%" id="mcps1.1.5.1.1"><p id="p44677416"><a name="p44677416"></a><a name="p44677416"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.98%" id="mcps1.1.5.1.2"><p id="p62100918"><a name="p62100918"></a><a name="p62100918"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.56%" id="mcps1.1.5.1.3"><p id="p64118428"><a name="p64118428"></a><a name="p64118428"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.96%" id="mcps1.1.5.1.4"><p id="p26210179"><a name="p26210179"></a><a name="p26210179"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41323472153226"><td class="cellrowborder" valign="top" width="17.5%" headers="mcps1.1.5.1.1 "><p id="p6683636153231"><a name="p6683636153231"></a><a name="p6683636153231"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.98%" headers="mcps1.1.5.1.2 "><p id="p4503635153231"><a name="p4503635153231"></a><a name="p4503635153231"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.1.5.1.3 "><p id="p29250179153231"><a name="p29250179153231"></a><a name="p29250179153231"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.1.5.1.4 "><p id="p20454316153231"><a name="p20454316153231"></a><a name="p20454316153231"></a>A user's ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section19906136"></a>

-   Parameter description

    <a name="table12269316123713"></a>
    <table><thead align="left"><tr id="row5274111623710"><th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.1.5.1.1"><p id="p122751516203719"><a name="p122751516203719"></a><a name="p122751516203719"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.040000000000003%" id="mcps1.1.5.1.2"><p id="p8277141623715"><a name="p8277141623715"></a><a name="p8277141623715"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.540000000000001%" id="mcps1.1.5.1.3"><p id="p0279151643712"><a name="p0279151643712"></a><a name="p0279151643712"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.23%" id="mcps1.1.5.1.4"><p id="p928114167375"><a name="p928114167375"></a><a name="p928114167375"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42908167372"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.1.5.1.1 "><p id="p82911316143720"><a name="p82911316143720"></a><a name="p82911316143720"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.1.5.1.2 "><p id="p1029217166379"><a name="p1029217166379"></a><a name="p1029217166379"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.540000000000001%" headers="mcps1.1.5.1.3 "><p id="p172931316173720"><a name="p172931316173720"></a><a name="p172931316173720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.5.1.4 "><div class="p" id="p7294161683716"><a name="p7294161683716"></a><a name="p7294161683716"></a>Possible values:<a name="ul20295116183711"></a><a name="ul20295116183711"></a><ul id="ul20295116183711"><li><span class="parmvalue" id="parmvalue555125744114325"><a name="parmvalue555125744114325"></a><a name="parmvalue555125744114325"></a><b>normal</b></span>: indicates that the defense status is normal.</li><li><span class="parmvalue" id="parmvalue404664094114337"><a name="parmvalue404664094114337"></a><a name="parmvalue404664094114337"></a><b>configging</b></span>: indicates that defense is being configured.</li><li><span class="parmvalue" id="parmvalue600552156114412"><a name="parmvalue600552156114412"></a><a name="parmvalue600552156114412"></a><b>notConfig</b></span>: indicates that defense is not configured.</li><li><span class="parmvalue" id="parmvalue1506354986114925"><a name="parmvalue1506354986114925"></a><a name="parmvalue1506354986114925"></a><b>packetcleaning</b></span>: indicates that traffic cleaning is underway.</li><li><span class="parmvalue" id="parmvalue1400332350143613"><a name="parmvalue1400332350143613"></a><a name="parmvalue1400332350143613"></a><b>packetdropping</b></span>: indicates that traffic is discarded.</li></ul>
    </div>
    <p id="p103021416173718"><a name="p103021416173718"></a><a name="p103021416173718"></a>If this parameter is not used, the defense statuses of all ECSs are displayed in the Neutron-queried order by default.</p>
    </td>
    </tr>
    <tr id="row03031816133717"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.1.5.1.1 "><p id="p1039510257597"><a name="p1039510257597"></a><a name="p1039510257597"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.1.5.1.2 "><p id="p133951725195913"><a name="p133951725195913"></a><a name="p133951725195913"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.540000000000001%" headers="mcps1.1.5.1.3 "><p id="p12395112565914"><a name="p12395112565914"></a><a name="p12395112565914"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.5.1.4 "><p id="p2039512251595"><a name="p2039512251595"></a><a name="p2039512251595"></a>Maximum number of returned results. The value ranges from 1 to 100.</p>
    </td>
    </tr>
    <tr id="row16307516123720"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.1.5.1.1 "><p id="p33951825165920"><a name="p33951825165920"></a><a name="p33951825165920"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.1.5.1.2 "><p id="p6395225165913"><a name="p6395225165913"></a><a name="p6395225165913"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.540000000000001%" headers="mcps1.1.5.1.3 "><p id="p7395192565911"><a name="p7395192565911"></a><a name="p7395192565911"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.5.1.4 "><p id="p639510257594"><a name="p639510257594"></a><a name="p639510257594"></a>Offset. The value ranges from 0 to 2147483647.</p>
    </td>
    </tr>
    <tr id="row17313416103715"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.1.5.1.1 "><p id="p17314516193713"><a name="p17314516193713"></a><a name="p17314516193713"></a>ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.1.5.1.2 "><p id="p1315161615372"><a name="p1315161615372"></a><a name="p1315161615372"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.540000000000001%" headers="mcps1.1.5.1.3 "><p id="p20316316193714"><a name="p20316316193714"></a><a name="p20316316193714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.1.5.1.4 "><p id="p93181616173716"><a name="p93181616173716"></a><a name="p93181616173716"></a>IP address. Both IPv4 and IPv6 addresses are supported. For example, if you enter <span class="uicontrol" id="uicontrol203181416163714"><a name="uicontrol203181416163714"></a><a name="uicontrol203181416163714"></a><b>?ip=192.168</b></span>, the defense status of EIPs corresponding to 192.168.111.1 and 10.192.168.8 is returned.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos?status=packetdropping 
    ```


## Response<a name="section44937496"></a>

-   Element description

    <a name="table10712809"></a>
    <table><thead align="left"><tr id="row45459670"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.1.4.1.1"><p id="p58354673"><a name="p58354673"></a><a name="p58354673"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="31.313131313131308%" id="mcps1.1.4.1.2"><p id="p29108085"><a name="p29108085"></a><a name="p29108085"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.1.4.1.3"><p id="p8944648"><a name="p8944648"></a><a name="p8944648"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53427925"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.4.1.1 "><p id="p32694658"><a name="p32694658"></a><a name="p32694658"></a>total</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131308%" headers="mcps1.1.4.1.2 "><p id="p23850200151829"><a name="p23850200151829"></a><a name="p23850200151829"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.4.1.3 "><p id="p29723549"><a name="p29723549"></a><a name="p29723549"></a>Total number of EIPs</p>
    </td>
    </tr>
    <tr id="row66185354"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.4.1.1 "><p id="p59413435"><a name="p59413435"></a><a name="p59413435"></a>ddosStatus</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131308%" headers="mcps1.1.4.1.2 "><p id="p47758962"><a name="p47758962"></a><a name="p47758962"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.4.1.3 "><p id="p43270676"><a name="p43270676"></a><a name="p43270676"></a>List of defense statuses</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **ddosStatus**

    <a name="table28415039"></a>
    <table><thead align="left"><tr id="row52787457"><th class="cellrowborder" valign="top" width="25.52%" id="mcps1.1.5.1.1"><p id="p47925604"><a name="p47925604"></a><a name="p47925604"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.55%" id="mcps1.1.5.1.2"><p id="p56768687"><a name="p56768687"></a><a name="p56768687"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.93%" id="mcps1.1.5.1.3"><p id="p34860939"><a name="p34860939"></a><a name="p34860939"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.1.5.1.4"><p id="p5163807"><a name="p5163807"></a><a name="p5163807"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15615252"><td class="cellrowborder" valign="top" width="25.52%" headers="mcps1.1.5.1.1 "><p id="p56875922"><a name="p56875922"></a><a name="p56875922"></a>floating_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55%" headers="mcps1.1.5.1.2 "><p id="p43546944"><a name="p43546944"></a><a name="p43546944"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.93%" headers="mcps1.1.5.1.3 "><p id="p37641542"><a name="p37641542"></a><a name="p37641542"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.5.1.4 "><p id="p29066061"><a name="p29066061"></a><a name="p29066061"></a>Floating IP address</p>
    </td>
    </tr>
    <tr id="row60267960"><td class="cellrowborder" valign="top" width="25.52%" headers="mcps1.1.5.1.1 "><p id="p49866595"><a name="p49866595"></a><a name="p49866595"></a>floating_ip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55%" headers="mcps1.1.5.1.2 "><p id="p12662370"><a name="p12662370"></a><a name="p12662370"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.93%" headers="mcps1.1.5.1.3 "><p id="p19019038"><a name="p19019038"></a><a name="p19019038"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.5.1.4 "><p id="p64147070"><a name="p64147070"></a><a name="p64147070"></a>ID of an EIP</p>
    </td>
    </tr>
    <tr id="row2739500019464"><td class="cellrowborder" valign="top" width="25.52%" headers="mcps1.1.5.1.1 "><p id="p1650312719469"><a name="p1650312719469"></a><a name="p1650312719469"></a>network_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55%" headers="mcps1.1.5.1.2 "><p id="p6168491719469"><a name="p6168491719469"></a><a name="p6168491719469"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.93%" headers="mcps1.1.5.1.3 "><p id="p3042242019469"><a name="p3042242019469"></a><a name="p3042242019469"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.5.1.4 "><p id="p4829698819469"><a name="p4829698819469"></a><a name="p4829698819469"></a>EIP type. The value can be:</p>
    <a name="ul3201971019469"></a><a name="ul3201971019469"></a><ul id="ul3201971019469"><li><strong id="b842352706163129"><a name="b842352706163129"></a><a name="b842352706163129"></a>EIP</strong>: EIP that is bound or not bound with ECS.</li><li><strong id="b842352706163134"><a name="b842352706163134"></a><a name="b842352706163134"></a>ELB</strong>: EIP that is bound with ELB.</li></ul>
    </td>
    </tr>
    <tr id="row40452719"><td class="cellrowborder" valign="top" width="25.52%" headers="mcps1.1.5.1.1 "><p id="p55444801"><a name="p55444801"></a><a name="p55444801"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55%" headers="mcps1.1.5.1.2 "><p id="p61843883"><a name="p61843883"></a><a name="p61843883"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.93%" headers="mcps1.1.5.1.3 "><p id="p43298646"><a name="p43298646"></a><a name="p43298646"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.5.1.4 "><div class="p" id="p17529450"><a name="p17529450"></a><a name="p17529450"></a>Defense status, the possible value of which is one of the following:<a name="ul23547322"></a><a name="ul23547322"></a><ul id="ul23547322"><li><span class="parmvalue" id="parmvalue1507623571"><a name="parmvalue1507623571"></a><a name="parmvalue1507623571"></a><b>normal</b></span>: indicates that the defense status is normal.</li><li><span class="parmvalue" id="parmvalue1096523868"><a name="parmvalue1096523868"></a><a name="parmvalue1096523868"></a><b>configging</b></span>: indicates that defense is being configured.</li><li><span class="parmvalue" id="parmvalue1637115095"><a name="parmvalue1637115095"></a><a name="parmvalue1637115095"></a><b>notConfig</b></span>: indicates that defense is not configured.</li><li><span class="parmvalue" id="parmvalue2046483687"><a name="parmvalue2046483687"></a><a name="parmvalue2046483687"></a><b>packetcleaning</b></span>: indicates that traffic cleaning is underway.</li><li><span class="parmvalue" id="parmvalue202788450"><a name="parmvalue202788450"></a><a name="parmvalue202788450"></a><b>packetdropping</b></span>: indicates that traffic is discarded.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
       "total": 5,
       "ddosStatus": [
          {
             "floating_ip_id": "1867f954-fc11-4202-8247-6af2144867ea",
             "floating_ip_address": "192.168.42.221",
             "network_type": "EIP",
             "status": "notConfig"
          },
          {
             "floating_ip_id": "49c6af49-9ace-42e6-ab89-1eee1f4ac821",
             "floating_ip_address": "192.168.35.152",
             "network_type": "EIP",
             "status": "normal"
          },
          {
             "floating_ip_id": "7a8dc957-083b-499d-b7cf-6fa48f4880c5",
             "floating_ip_address": "192.168.42.222",
             "network_type": "EIP",
             "status": "notConfig"
          },
          {
             "floating_ip_id": "7c6676a0-b281-4163-9d0d-cb6485ae9860",
             "floating_ip_address": "192.168.44.69",
             "network_type": "EIP",
             "status": "normal"
          },
          {
             "floating_ip_id": "969c1d48-6a92-4ef1-b66c-b17c7e7d7ce7",
             "floating_ip_address": "192.168.47.192",
             "network_type": "EIP",
             "status": "notConfig"
          }
       ]
    }
    ```


## Returned Value<a name="section1784282"></a>

See  [Status Code](status-code.md).

