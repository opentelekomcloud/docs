# Obtaining Detailed Information of a Specified DB Instance<a name="en-us_topic_0056890054"></a>

## Function<a name="section2219913118372"></a>

This API is used to obtain detailed information of a specified DB instance.

## URI<a name="section993084518372"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/instances/\{instanceId\}

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table1260521818372"></a>
    <table><thead align="left"><tr id="row3225837518372"><th class="cellrowborder" valign="top" width="21.25%" id="mcps1.2.4.1.1"><p id="p6279156718372"><a name="p6279156718372"></a><a name="p6279156718372"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.749999999999996%" id="mcps1.2.4.1.2"><p id="p5295214318372"><a name="p5295214318372"></a><a name="p5295214318372"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p6126520018372"><a name="p6126520018372"></a><a name="p6126520018372"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6353416918372"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p4599409918372"><a name="p4599409918372"></a><a name="p4599409918372"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p3453456618372"><a name="p3453456618372"></a><a name="p3453456618372"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4583644118372"><a name="p4583644118372"></a><a name="p4583644118372"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row987478618372"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p6166018418372"><a name="p6166018418372"></a><a name="p6166018418372"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p2841904418372"><a name="p2841904418372"></a><a name="p2841904418372"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2024119518372"><a name="p2024119518372"></a><a name="p2024119518372"></a>Specifies the ID of the queried DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section254315618372"></a>

None

## Normal Response<a name="section4202204618372"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table29970750185052"></a>
    <table><thead align="left"><tr id="row535897185052"><th class="cellrowborder" valign="top" width="28.78%" id="mcps1.2.4.1.1"><p id="p43407726185052"><a name="p43407726185052"></a><a name="p43407726185052"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.4%" id="mcps1.2.4.1.2"><p id="p26364940185052"><a name="p26364940185052"></a><a name="p26364940185052"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.82%" id="mcps1.2.4.1.3"><p id="p55185370185052"><a name="p55185370185052"></a><a name="p55185370185052"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40829952185052"><td class="cellrowborder" valign="top" width="28.78%" headers="mcps1.2.4.1.1 "><p id="p32816846185116"><a name="p32816846185116"></a><a name="p32816846185116"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.4%" headers="mcps1.2.4.1.2 "><p id="p40918884185116"><a name="p40918884185116"></a><a name="p40918884185116"></a>Dictionary data structure. For details, see <a href="#table36134360185226">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.4.1.3 "><p id="p6277740185150"><a name="p6277740185150"></a><a name="p6277740185150"></a>Indicates the DB instance information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instance field data structure description

    <a name="table36134360185226"></a>
    <table><thead align="left"><tr id="row12336344185226"><th class="cellrowborder" valign="top" width="29.630000000000003%" id="mcps1.2.4.1.1"><p id="p59719836185226"><a name="p59719836185226"></a><a name="p59719836185226"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.980000000000004%" id="mcps1.2.4.1.2"><p id="p10445045185251"><a name="p10445045185251"></a><a name="p10445045185251"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.39%" id="mcps1.2.4.1.3"><p id="p40742336185251"><a name="p40742336185251"></a><a name="p40742336185251"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9560700192945"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p44665392192949"><a name="p44665392192949"></a><a name="p44665392192949"></a>configurationStatus</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p61126993192949"><a name="p61126993192949"></a><a name="p61126993192949"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p52339366192949"><a name="p52339366192949"></a><a name="p52339366192949"></a>Indicates the parameter template status.</p>
    </td>
    </tr>
    <tr id="row66276799193024"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p15135364193027"><a name="p15135364193027"></a><a name="p15135364193027"></a>paramsGroupId</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p18004953193027"><a name="p18004953193027"></a><a name="p18004953193027"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p49115103193027"><a name="p49115103193027"></a><a name="p49115103193027"></a>Indicates the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row40912132193130"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p18122206193133"><a name="p18122206193133"></a><a name="p18122206193133"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p58612605193133"><a name="p58612605193133"></a><a name="p58612605193133"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p50000560193133"><a name="p50000560193133"></a><a name="p50000560193133"></a>Indicates the DB instance type.</p>
    </td>
    </tr>
    <tr id="row710329119321"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p4283541819325"><a name="p4283541819325"></a><a name="p4283541819325"></a>subnetid</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p4711684019325"><a name="p4711684019325"></a><a name="p4711684019325"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p5836773519325"><a name="p5836773519325"></a><a name="p5836773519325"></a>Indicates the subnet ID.</p>
    </td>
    </tr>
    <tr id="row31360246193230"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p37392557193234"><a name="p37392557193234"></a><a name="p37392557193234"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p8898308193234"><a name="p8898308193234"></a><a name="p8898308193234"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p49674310193234"><a name="p49674310193234"></a><a name="p49674310193234"></a>Indicates the DB instance role.</p>
    </td>
    </tr>
    <tr id="row5973685519339"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p61423156193315"><a name="p61423156193315"></a><a name="p61423156193315"></a>internalSubnetId</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p9219711193315"><a name="p9219711193315"></a><a name="p9219711193315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p8599131193315"><a name="p8599131193315"></a><a name="p8599131193315"></a>Indicates the internal subnet ID.</p>
    </td>
    </tr>
    <tr id="row14987063193346"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p35860274193350"><a name="p35860274193350"></a><a name="p35860274193350"></a>group</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p19001085193350"><a name="p19001085193350"></a><a name="p19001085193350"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p63972773181030"><a name="p63972773181030"></a><a name="p63972773181030"></a>Indicates the user group which the DB instance belongs to.</p>
    </td>
    </tr>
    <tr id="row45408653193410"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p30955040193413"><a name="p30955040193413"></a><a name="p30955040193413"></a>securegroup</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p24330275193413"><a name="p24330275193413"></a><a name="p24330275193413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p24595296193413"><a name="p24595296193413"></a><a name="p24595296193413"></a>Indicates the security group ID.</p>
    </td>
    </tr>
    <tr id="row8599082193438"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p22654055193441"><a name="p22654055193441"></a><a name="p22654055193441"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p23039138193441"><a name="p23039138193441"></a><a name="p23039138193441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p54230894193441"><a name="p54230894193441"></a><a name="p54230894193441"></a>Indicates the VPC ID.</p>
    </td>
    </tr>
    <tr id="row1335553319355"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p5157818919359"><a name="p5157818919359"></a><a name="p5157818919359"></a>azcode</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p1708374219359"><a name="p1708374219359"></a><a name="p1708374219359"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p4160585619359"><a name="p4160585619359"></a><a name="p4160585619359"></a>Indicates the AZ.</p>
    </td>
    </tr>
    <tr id="row58512727193531"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p9551023193535"><a name="p9551023193535"></a><a name="p9551023193535"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p35435432193535"><a name="p35435432193535"></a><a name="p35435432193535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p51697749193535"><a name="p51697749193535"></a><a name="p51697749193535"></a>Indicates the region where the DB instance is deployed.</p>
    </td>
    </tr>
    <tr id="row25449698193548"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p35644336193552"><a name="p35644336193552"></a><a name="p35644336193552"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p1510079193552"><a name="p1510079193552"></a><a name="p1510079193552"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p55207563193552"><a name="p55207563193552"></a><a name="p55207563193552"></a>Indicates the DB instance creation time.</p>
    </td>
    </tr>
    <tr id="row5195814914599"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p25050509145926"><a name="p25050509145926"></a><a name="p25050509145926"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p15825367145926"><a name="p15825367145926"></a><a name="p15825367145926"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p6786341145926"><a name="p6786341145926"></a><a name="p6786341145926"></a>Indicates the updated time, which is the same as <strong id="b1895841192164211"><a name="b1895841192164211"></a><a name="b1895841192164211"></a>created</strong>.</p>
    </td>
    </tr>
    <tr id="row60256134193617"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p48301797193621"><a name="p48301797193621"></a><a name="p48301797193621"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p20131514193621"><a name="p20131514193621"></a><a name="p20131514193621"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p20039960193621"><a name="p20039960193621"></a><a name="p20039960193621"></a>Indicates the DB instance status.</p>
    <div class="p" id="p122952317516"><a name="p122952317516"></a><a name="p122952317516"></a>Value:<a name="ul3066104695748"></a><a name="ul3066104695748"></a><ul id="ul3066104695748"><li>If the value is <strong id="b84235270616547_1"><a name="b84235270616547_1"></a><a name="b84235270616547_1"></a>BUILD</strong>, the instance is being created.</li><li>If the value is <strong id="b842352706165415"><a name="b842352706165415"></a><a name="b842352706165415"></a>ACTIVE</strong>, the instance is normal.</li><li>If the value is <strong id="b842352706165427"><a name="b842352706165427"></a><a name="b842352706165427"></a>FAILED</strong>, the instance is abnormal.</li><li>If the value is <strong id="b84235270616547_3"><a name="b84235270616547_3"></a><a name="b84235270616547_3"></a>MODIFYING</strong>, the instance is being scaled up.</li><li>If the value is <strong id="b84235270616547_5"><a name="b84235270616547_5"></a><a name="b84235270616547_5"></a>REBOOTING</strong>, the instance is being rebooted.</li><li>If the value is <strong id="b84235270616547_7"><a name="b84235270616547_7"></a><a name="b84235270616547_7"></a>RESTORING</strong>, the instance is being restored.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row27364532185226"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p21996717185244"><a name="p21996717185244"></a><a name="p21996717185244"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p36903653185244"><a name="p36903653185244"></a><a name="p36903653185244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p36405930185244"><a name="p36405930185244"></a><a name="p36405930185244"></a>Indicates the DB instance name.</p>
    </td>
    </tr>
    <tr id="row3151013017829"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p3157102517833"><a name="p3157102517833"></a><a name="p3157102517833"></a>publicEndpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p711621417833"><a name="p711621417833"></a><a name="p711621417833"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p3954247617833"><a name="p3954247617833"></a><a name="p3954247617833"></a>Indicates the EIP for public access, including the IP address and port number.</p>
    </td>
    </tr>
    <tr id="row44328680173349"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p38759832173353"><a name="p38759832173353"></a><a name="p38759832173353"></a>dbPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p52538688173353"><a name="p52538688173353"></a><a name="p52538688173353"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p27775349173353"><a name="p27775349173353"></a><a name="p27775349173353"></a>Indicates the database port number.</p>
    </td>
    </tr>
    <tr id="row16185637185226"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p63199203185244"><a name="p63199203185244"></a><a name="p63199203185244"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p18861817185244"><a name="p18861817185244"></a><a name="p18861817185244"></a>List data structure. For details, see <a href="#table55695058185421">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p51412179185244"><a name="p51412179185244"></a><a name="p51412179185244"></a>Indicates the link address.</p>
    </td>
    </tr>
    <tr id="row24175008185226"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p3636953185244"><a name="p3636953185244"></a><a name="p3636953185244"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p26157813185244"><a name="p26157813185244"></a><a name="p26157813185244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p38408076185244"><a name="p38408076185244"></a><a name="p38408076185244"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row31897396193652"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p37677186193658"><a name="p37677186193658"></a><a name="p37677186193658"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p31953188193658"><a name="p31953188193658"></a><a name="p31953188193658"></a>Dictionary data structure. For details, see <a href="#table37355134185555">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p7098746193658"><a name="p7098746193658"></a><a name="p7098746193658"></a>Indicates the DB instance specifications.</p>
    </td>
    </tr>
    <tr id="row10508356185226"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p24046472185244"><a name="p24046472185244"></a><a name="p24046472185244"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p1607249185244"><a name="p1607249185244"></a><a name="p1607249185244"></a>Dictionary data structure. For details, see <a href="#table12148497185732">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p63078350185244"><a name="p63078350185244"></a><a name="p63078350185244"></a>Indicates the volume information.</p>
    </td>
    </tr>
    <tr id="row11905516185226"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p57792624185244"><a name="p57792624185244"></a><a name="p57792624185244"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p50690956185244"><a name="p50690956185244"></a><a name="p50690956185244"></a>Dictionary data structure. For details, see <a href="#table49473740185347">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p12326732185244"><a name="p12326732185244"></a><a name="p12326732185244"></a>Indicates the database information.</p>
    </td>
    </tr>
    <tr id="row48131082141435"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p30868211141511"><a name="p30868211141511"></a><a name="p30868211141511"></a>fault</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p17297192141511"><a name="p17297192141511"></a><a name="p17297192141511"></a>Dictionary data structure. For details, see <a href="#table49716197145035">Table 8</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p58895334141511"><a name="p58895334141511"></a><a name="p58895334141511"></a>This parameter is valid when the DB instance is faulty.</p>
    </td>
    </tr>
    <tr id="row55809903141448"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p5792724141511"><a name="p5792724141511"></a><a name="p5792724141511"></a>configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p66557466141511"><a name="p66557466141511"></a><a name="p66557466141511"></a>Dictionary data structure. For details, see <a href="#table46303018145144">Table 9</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p22445665141511"><a name="p22445665141511"></a><a name="p22445665141511"></a>This parameter is valid when a parameter template exists.</p>
    </td>
    </tr>
    <tr id="row48038564141445"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p6159568141511"><a name="p6159568141511"></a><a name="p6159568141511"></a>locality</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p29163024141511"><a name="p29163024141511"></a><a name="p29163024141511"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p13394761141511"><a name="p13394761141511"></a><a name="p13394761141511"></a>Currently, this parameter is not supported.</p>
    </td>
    </tr>
    <tr id="row13505736141428"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p21289621141520"><a name="p21289621141520"></a><a name="p21289621141520"></a>replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p1993962215941"><a name="p1993962215941"></a><a name="p1993962215941"></a>Dictionary data structure. For details, see <a href="#table841114018543">Table 10</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p4741363314153"><a name="p4741363314153"></a><a name="p4741363314153"></a>This parameter is valid when obtaining the primary DB instance information.</p>
    </td>
    </tr>
    <tr id="row31420619141640"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p618958141716"><a name="p618958141716"></a><a name="p618958141716"></a>dbuser</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p50135614141716"><a name="p50135614141716"></a><a name="p50135614141716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p34452943141716"><a name="p34452943141716"></a><a name="p34452943141716"></a>Indicates the new administrator account.</p>
    </td>
    </tr>
    <tr id="row40773882141640"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p39225000141716"><a name="p39225000141716"></a><a name="p39225000141716"></a>storageEngine</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p23108466141716"><a name="p23108466141716"></a><a name="p23108466141716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p59846485141716"><a name="p59846485141716"></a><a name="p59846485141716"></a>Indicates the storage engine.</p>
    </td>
    </tr>
    <tr id="row49269674141640"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p15727096141716"><a name="p15727096141716"></a><a name="p15727096141716"></a>payModel</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p65935235141716"><a name="p65935235141716"></a><a name="p65935235141716"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p39153823141716"><a name="p39153823141716"></a><a name="p39153823141716"></a>Indicates the payment mode. The value <strong id="b883717511878"><a name="b883717511878"></a><a name="b883717511878"></a>1</strong> indicates the pay-per-use mode and only this mode is supported currently.</p>
    </td>
    </tr>
    <tr id="row43639818193825"><td class="cellrowborder" valign="top" width="29.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p6177172193829"><a name="p6177172193829"></a><a name="p6177172193829"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p30588910193829"><a name="p30588910193829"></a><a name="p30588910193829"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.39%" headers="mcps1.2.4.1.3 "><p id="p61782665193829"><a name="p61782665193829"></a><a name="p61782665193829"></a>Indicates the cluster ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  links field data structure description

    <a name="table55695058185421"></a>
    <table><thead align="left"><tr id="row4765718185421"><th class="cellrowborder" valign="top" width="30.259999999999998%" id="mcps1.2.4.1.1"><p id="p50478848185421"><a name="p50478848185421"></a><a name="p50478848185421"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.92%" id="mcps1.2.4.1.2"><p id="p66918829185440"><a name="p66918829185440"></a><a name="p66918829185440"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.82%" id="mcps1.2.4.1.3"><p id="p51716079185440"><a name="p51716079185440"></a><a name="p51716079185440"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row192005185421"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p7742898185436"><a name="p7742898185436"></a><a name="p7742898185436"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.92%" headers="mcps1.2.4.1.2 "><p id="p23194967185436"><a name="p23194967185436"></a><a name="p23194967185436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.4.1.3 "><p id="p66853016185436"><a name="p66853016185436"></a><a name="p66853016185436"></a>Its value is <strong id="b842352706142823"><a name="b842352706142823"></a><a name="b842352706142823"></a>self</strong> or <strong id="b842352706142833"><a name="b842352706142833"></a><a name="b842352706142833"></a>bookmark</strong>.</p>
    </td>
    </tr>
    <tr id="row20802817194340"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.4.1.1 "><p id="p10839188194347"><a name="p10839188194347"></a><a name="p10839188194347"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.92%" headers="mcps1.2.4.1.2 "><p id="p5559001194347"><a name="p5559001194347"></a><a name="p5559001194347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.4.1.3 "><p id="p47625914194347"><a name="p47625914194347"></a><a name="p47625914194347"></a>Its value is <strong id="b842352706121418"><a name="b842352706121418"></a><a name="b842352706121418"></a>""</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  flavor field data structure description

    <a name="table37355134185555"></a>
    <table><thead align="left"><tr id="row39954632185555"><th class="cellrowborder" valign="top" width="30.31%" id="mcps1.2.4.1.1"><p id="p10063079185615"><a name="p10063079185615"></a><a name="p10063079185615"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.55%" id="mcps1.2.4.1.2"><p id="p9803102185615"><a name="p9803102185615"></a><a name="p9803102185615"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.14%" id="mcps1.2.4.1.3"><p id="p2363714614266"><a name="p2363714614266"></a><a name="p2363714614266"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33751272194030"><td class="cellrowborder" valign="top" width="30.31%" headers="mcps1.2.4.1.1 "><p id="p16169010194039"><a name="p16169010194039"></a><a name="p16169010194039"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.2 "><p id="p34621427194039"><a name="p34621427194039"></a><a name="p34621427194039"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.14%" headers="mcps1.2.4.1.3 "><p id="p52872168194039"><a name="p52872168194039"></a><a name="p52872168194039"></a>Indicates the specification ID.</p>
    </td>
    </tr>
    <tr id="row30414096194034"><td class="cellrowborder" valign="top" width="30.31%" headers="mcps1.2.4.1.1 "><p id="p23322696194039"><a name="p23322696194039"></a><a name="p23322696194039"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.2 "><p id="p10090256194039"><a name="p10090256194039"></a><a name="p10090256194039"></a>List data structure. For details, see <a href="#table55695058185421">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.14%" headers="mcps1.2.4.1.3 "><p id="p40930665194039"><a name="p40930665194039"></a><a name="p40930665194039"></a>Indicates the link address.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  volume field data structure description

    <a name="table12148497185732"></a>
    <table><thead align="left"><tr id="row1275258185732"><th class="cellrowborder" valign="top" width="30.070000000000004%" id="mcps1.2.4.1.1"><p id="p36187113185732"><a name="p36187113185732"></a><a name="p36187113185732"></a><strong id="b84235270691445_13"><a name="b84235270691445_13"></a><a name="b84235270691445_13"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.54%" id="mcps1.2.4.1.2"><p id="p9917550185749"><a name="p9917550185749"></a><a name="p9917550185749"></a><strong id="b842352706164541_9"><a name="b842352706164541_9"></a><a name="b842352706164541_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.39%" id="mcps1.2.4.1.3"><p id="p65124095185749"><a name="p65124095185749"></a><a name="p65124095185749"></a><strong id="b842352706163417_13"><a name="b842352706163417_13"></a><a name="b842352706163417_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60088509194046"><td class="cellrowborder" valign="top" width="30.070000000000004%" headers="mcps1.2.4.1.1 "><p id="p17406830194132"><a name="p17406830194132"></a><a name="p17406830194132"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.2.4.1.2 "><p id="p667151194132"><a name="p667151194132"></a><a name="p667151194132"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.39%" headers="mcps1.2.4.1.3 "><p id="p54039309194132"><a name="p54039309194132"></a><a name="p54039309194132"></a>Indicates the volume type.</p>
    </td>
    </tr>
    <tr id="row2863733194242"><td class="cellrowborder" valign="top" width="30.070000000000004%" headers="mcps1.2.4.1.1 "><p id="p21906213194251"><a name="p21906213194251"></a><a name="p21906213194251"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.2.4.1.2 "><p id="p29572844194251"><a name="p29572844194251"></a><a name="p29572844194251"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.39%" headers="mcps1.2.4.1.3 "><p id="p46590192194251"><a name="p46590192194251"></a><a name="p46590192194251"></a>Indicates the volume size.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  datastore field data structure description

    <a name="table49473740185347"></a>
    <table><thead align="left"><tr id="row60560615185347"><th class="cellrowborder" valign="top" width="29.94%" id="mcps1.2.4.1.1"><p id="p6462774185347"><a name="p6462774185347"></a><a name="p6462774185347"></a><strong id="b84235270691445_15"><a name="b84235270691445_15"></a><a name="b84235270691445_15"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.54%" id="mcps1.2.4.1.2"><p id="p33091282185514"><a name="p33091282185514"></a><a name="p33091282185514"></a><strong id="b842352706164541_11"><a name="b842352706164541_11"></a><a name="b842352706164541_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.52%" id="mcps1.2.4.1.3"><p id="p63148213185514"><a name="p63148213185514"></a><a name="p63148213185514"></a><strong id="b842352706163417_15"><a name="b842352706163417_15"></a><a name="b842352706163417_15"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4845382611494"><td class="cellrowborder" valign="top" width="29.94%" headers="mcps1.2.4.1.1 "><p id="p50166913114913"><a name="p50166913114913"></a><a name="p50166913114913"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.2.4.1.2 "><p id="p36988191114913"><a name="p36988191114913"></a><a name="p36988191114913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.3 "><p id="p43253505114913"><a name="p43253505114913"></a><a name="p43253505114913"></a>Indicates the DB engine type.</p>
    </td>
    </tr>
    <tr id="row12567563121457"><td class="cellrowborder" valign="top" width="29.94%" headers="mcps1.2.4.1.1 "><p id="p1652613812155"><a name="p1652613812155"></a><a name="p1652613812155"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.2.4.1.2 "><p id="p6354880112155"><a name="p6354880112155"></a><a name="p6354880112155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.3 "><p id="p4717924812155"><a name="p4717924812155"></a><a name="p4717924812155"></a>Indicates the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  fault field data structure description

    <a name="table49716197145035"></a>
    <table><thead align="left"><tr id="row63339866145035"><th class="cellrowborder" valign="top" width="29.98%" id="mcps1.2.4.1.1"><p id="p30255525145035"><a name="p30255525145035"></a><a name="p30255525145035"></a><strong id="b84235270691445_17"><a name="b84235270691445_17"></a><a name="b84235270691445_17"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.5%" id="mcps1.2.4.1.2"><p id="p36187606145049"><a name="p36187606145049"></a><a name="p36187606145049"></a><strong id="b842352706164541_13"><a name="b842352706164541_13"></a><a name="b842352706164541_13"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.52%" id="mcps1.2.4.1.3"><p id="p45514958145049"><a name="p45514958145049"></a><a name="p45514958145049"></a><strong id="b842352706163417_17"><a name="b842352706163417_17"></a><a name="b842352706163417_17"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33540513145035"><td class="cellrowborder" valign="top" width="29.98%" headers="mcps1.2.4.1.1 "><p id="p20251722145043"><a name="p20251722145043"></a><a name="p20251722145043"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.5%" headers="mcps1.2.4.1.2 "><p id="p29776786145043"><a name="p29776786145043"></a><a name="p29776786145043"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.3 "><p id="p63109479145043"><a name="p63109479145043"></a><a name="p63109479145043"></a>Indicates the message returned when creating the DB instance failed.</p>
    </td>
    </tr>
    <tr id="row33429165145035"><td class="cellrowborder" valign="top" width="29.98%" headers="mcps1.2.4.1.1 "><p id="p11594160145043"><a name="p11594160145043"></a><a name="p11594160145043"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.5%" headers="mcps1.2.4.1.2 "><p id="p66711766145043"><a name="p66711766145043"></a><a name="p66711766145043"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.3 "><p id="p34943936145043"><a name="p34943936145043"></a><a name="p34943936145043"></a>Indicates the DB instance creation time.</p>
    </td>
    </tr>
    <tr id="row37060537145035"><td class="cellrowborder" valign="top" width="29.98%" headers="mcps1.2.4.1.1 "><p id="p11886550145043"><a name="p11886550145043"></a><a name="p11886550145043"></a>details</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.5%" headers="mcps1.2.4.1.2 "><p id="p23286530145043"><a name="p23286530145043"></a><a name="p23286530145043"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.52%" headers="mcps1.2.4.1.3 "><p id="p7160745145043"><a name="p7160745145043"></a><a name="p7160745145043"></a>Indicates the fault details.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  configuration field data structure description

    <a name="table46303018145144"></a>
    <table><thead align="left"><tr id="row45622109145144"><th class="cellrowborder" valign="top" width="29.67%" id="mcps1.2.4.1.1"><p id="p4403381145144"><a name="p4403381145144"></a><a name="p4403381145144"></a><strong id="b84235270691445_19"><a name="b84235270691445_19"></a><a name="b84235270691445_19"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.75%" id="mcps1.2.4.1.2"><p id="p5164732914520"><a name="p5164732914520"></a><a name="p5164732914520"></a><strong id="b842352706164541_15"><a name="b842352706164541_15"></a><a name="b842352706164541_15"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.58%" id="mcps1.2.4.1.3"><p id="p2268408314520"><a name="p2268408314520"></a><a name="p2268408314520"></a><strong id="b842352706163417_19"><a name="b842352706163417_19"></a><a name="b842352706163417_19"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58805170145144"><td class="cellrowborder" valign="top" width="29.67%" headers="mcps1.2.4.1.1 "><p id="p65335242145153"><a name="p65335242145153"></a><a name="p65335242145153"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.4.1.2 "><p id="p57663254145153"><a name="p57663254145153"></a><a name="p57663254145153"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.58%" headers="mcps1.2.4.1.3 "><p id="p40211994145153"><a name="p40211994145153"></a><a name="p40211994145153"></a>Indicates the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row60053159145144"><td class="cellrowborder" valign="top" width="29.67%" headers="mcps1.2.4.1.1 "><p id="p35946111145153"><a name="p35946111145153"></a><a name="p35946111145153"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.4.1.2 "><p id="p25953901145153"><a name="p25953901145153"></a><a name="p25953901145153"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.58%" headers="mcps1.2.4.1.3 "><p id="p21891211145153"><a name="p21891211145153"></a><a name="p21891211145153"></a>Indicates the parameter template name.</p>
    </td>
    </tr>
    <tr id="row18160073145144"><td class="cellrowborder" valign="top" width="29.67%" headers="mcps1.2.4.1.1 "><p id="p28357633145153"><a name="p28357633145153"></a><a name="p28357633145153"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.4.1.2 "><p id="p15266936145153"><a name="p15266936145153"></a><a name="p15266936145153"></a>List data structure. For details, see <a href="#table55695058185421">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.58%" headers="mcps1.2.4.1.3 "><p id="p28662295145153"><a name="p28662295145153"></a><a name="p28662295145153"></a>Indicates the link address.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10**  replicas field data structure description

    <a name="table841114018543"></a>
    <table><thead align="left"><tr id="row3773109718543"><th class="cellrowborder" valign="top" width="29.720000000000002%" id="mcps1.2.4.1.1"><p id="p3632003918543"><a name="p3632003918543"></a><a name="p3632003918543"></a><strong id="b84235270691445_21"><a name="b84235270691445_21"></a><a name="b84235270691445_21"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.709999999999994%" id="mcps1.2.4.1.2"><p id="p46653346185835"><a name="p46653346185835"></a><a name="p46653346185835"></a><strong id="b842352706164541_17"><a name="b842352706164541_17"></a><a name="b842352706164541_17"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.57%" id="mcps1.2.4.1.3"><p id="p20824648185835"><a name="p20824648185835"></a><a name="p20824648185835"></a><strong id="b842352706163417_21"><a name="b842352706163417_21"></a><a name="b842352706163417_21"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1874998918543"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.4.1.1 "><p id="p42130172185828"><a name="p42130172185828"></a><a name="p42130172185828"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.4.1.2 "><p id="p57100770185828"><a name="p57100770185828"></a><a name="p57100770185828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.57%" headers="mcps1.2.4.1.3 "><p id="p61759628185828"><a name="p61759628185828"></a><a name="p61759628185828"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row6264758145313"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.4.1.1 "><p id="p10595924145352"><a name="p10595924145352"></a><a name="p10595924145352"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.4.1.2 "><p id="p52963533145352"><a name="p52963533145352"></a><a name="p52963533145352"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.57%" headers="mcps1.2.4.1.3 "><p id="p62187750145352"><a name="p62187750145352"></a><a name="p62187750145352"></a>Indicates the DB instance name.</p>
    </td>
    </tr>
    <tr id="row2382555518543"><td class="cellrowborder" valign="top" width="29.720000000000002%" headers="mcps1.2.4.1.1 "><p id="p36473954185828"><a name="p36473954185828"></a><a name="p36473954185828"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.4.1.2 "><p id="p1600334185828"><a name="p1600334185828"></a><a name="p1600334185828"></a>List data structure. For details, see <a href="#table55695058185421">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.57%" headers="mcps1.2.4.1.3 "><p id="p62518197185828"><a name="p62518197185828"></a><a name="p62518197185828"></a>Indicates the link address.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "instance": {
        "configurationStatus": "In-Sync",
        "paramsGroupId": "b89db814-6ba1-454f-a9ad-380064ef0c6f",
        "type": "MySQL",
        "subnetid": "0fb5d084-4e5d-463b-8920-fca10e6b4028",
        "role": "master",
        "internalSubnetId": "330a10fd-3962-44c5-b3a1-1d282617a183",
        "group": "root",
        "securegroup": "ca99fcef-502f-495f-b28d-85c9c6f4666e",
        "vpc": "292997f2-3bf7-4d60-86a5-4e9d593bc850",
        "azcode": "eu-de-01",
        "region": null,
        "created": "2017-05-12T02:18:46",
        "updated": "2017-05-12T02:18:46",
        "status": "ACTIVE",
        "name": "rds-MySQL-1-1",
        "publicEndpoint": "10.11.77.101:8635",
        "dbPort": 8635,
        "links": [
          {
            "rel": "self",
            "href": ""
          },
          {
            "rel": "bookmark",
            "href": ""
          }
        ],
        "id": "e8faac23-8129-4c68-a231-480e46fc5f4f",
        "flavor": {
          "id": "31b2863c-0e15-44fd-a80d-1e83a7aca338",
          "links": [
            {
              "rel": "self",
              "href": ""
            },
            {
              "rel": "bookmark",
              "href": ""
            }
          ]
        },
        "volume": {
          "type": "COMMON",
          "size": 210
        },
        "datastore": {
          "type": "MySQL",
          "version": "MySQL-5.7.17"
        },
        "fault": null,
        "configuration": null,
        "locality": null,
        "replicas": null,
        "dbuser": "root",
        "storageEngine": "",
        "payModel": 0,
        "cluster_id": "fb22f24c-0466-48f2-8275-70af04ef4935"
      }
    }
    ```


## Abnormal Response<a name="section4665940119121"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

