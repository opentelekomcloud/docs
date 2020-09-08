# Querying VPC Endpoints<a name="vpcep_06_0306"></a>

## Function<a name="section51695639"></a>

This API is used to query VPC endpoints.

## URI<a name="section62607570"></a>

GET /v1/\{project\_id\}/vpc-endpoints?endpoint\_service\_name=\{endpoint\_service\_name\}&vpc\_id=\{vpc\_id\}&limit=\{limit\}&offset=\{offset\}&id=\{id\}&sort\_key=\{sort\_key\}&sort\_dir=\{sort\_dir\}

[Table 1](#table35342882)  describes the required parameters.

**Table  1**  Parameters

<a name="table35342882"></a>
<table><thead align="left"><tr id="row34818463"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p1723244"><a name="p1723244"></a><a name="p1723244"></a><strong id="b0386425811"><a name="b0386425811"></a><a name="b0386425811"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p5365057"><a name="p5365057"></a><a name="p5365057"></a><strong id="b167394261113"><a name="b167394261113"></a><a name="b167394261113"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p31916487"><a name="p31916487"></a><a name="p31916487"></a><strong id="b56611427211"><a name="b56611427211"></a><a name="b56611427211"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row35098661"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p24419332"><a name="p24419332"></a><a name="p24419332"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p31808908"><a name="p31808908"></a><a name="p31808908"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p26384740"><a name="p26384740"></a><a name="p26384740"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section26597221"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table44201211"></a>
    <table><thead align="left"><tr id="row21673883"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p10754092"><a name="p10754092"></a><a name="p10754092"></a><strong id="b16326154916319"><a name="b16326154916319"></a><a name="b16326154916319"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p65775089"><a name="p65775089"></a><a name="p65775089"></a><strong id="b589689032"><a name="b589689032"></a><a name="b589689032"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p26181970"><a name="p26181970"></a><a name="p26181970"></a><strong id="b552515521333"><a name="b552515521333"></a><a name="b552515521333"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p40364857"><a name="p40364857"></a><a name="p40364857"></a><strong id="b928219803"><a name="b928219803"></a><a name="b928219803"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48327947"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p22249650"><a name="p22249650"></a><a name="p22249650"></a>endpoint_service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p57391254"><a name="p57391254"></a><a name="p57391254"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p18179998"><a name="p18179998"></a><a name="p18179998"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p63293747"><a name="p63293747"></a><a name="p63293747"></a>Specifies the name of the VPC endpoint service. The value is not case-sensitive and supports fuzzy match.</p>
    </td>
    </tr>
    <tr id="row32772813"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p37352224"><a name="p37352224"></a><a name="p37352224"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p5631283"><a name="p5631283"></a><a name="p5631283"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p53480750"><a name="p53480750"></a><a name="p53480750"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p53427648"><a name="p53427648"></a><a name="p53427648"></a>Specifies the ID of the VPC where the VPC endpoint is to be created.</p>
    </td>
    </tr>
    <tr id="row1959717469498"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p540954724913"><a name="p540954724913"></a><a name="p540954724913"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p12410114719497"><a name="p12410114719497"></a><a name="p12410114719497"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p2041024784917"><a name="p2041024784917"></a><a name="p2041024784917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p241024744918"><a name="p241024744918"></a><a name="p241024744918"></a>Specifies the unique ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row46491877"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p7745692"><a name="p7745692"></a><a name="p7745692"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p23421307"><a name="p23421307"></a><a name="p23421307"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p18077739"><a name="p18077739"></a><a name="p18077739"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p55010772"><a name="p55010772"></a><a name="p55010772"></a>Specifies the maximum number of VPC endpoints displayed on each page.</p>
    <p id="p25334901"><a name="p25334901"></a><a name="p25334901"></a>The value ranges from <strong id="b5516178181014"><a name="b5516178181014"></a><a name="b5516178181014"></a>0</strong> to <strong id="b2325511151014"><a name="b2325511151014"></a><a name="b2325511151014"></a>1000</strong> and is generally <strong id="b147120145814"><a name="b147120145814"></a><a name="b147120145814"></a>10</strong>, <strong id="b1971310146815"><a name="b1971310146815"></a><a name="b1971310146815"></a>20</strong>, or <strong id="b771461413810"><a name="b771461413810"></a><a name="b771461413810"></a>50</strong>. The default value is <strong id="b197156146810"><a name="b197156146810"></a><a name="b197156146810"></a>10</strong>.</p>
    </td>
    </tr>
    <tr id="row26687517"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p14205230"><a name="p14205230"></a><a name="p14205230"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p9772976"><a name="p9772976"></a><a name="p9772976"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p53413578"><a name="p53413578"></a><a name="p53413578"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5736126132214"><a name="p5736126132214"></a><a name="p5736126132214"></a>Specifies the offset.</p>
    <p id="p11912494222"><a name="p11912494222"></a><a name="p11912494222"></a>All VPC endpoint services after this offset will be queried. The value must be an integer greater than 0 but less than the number of VPC endpoint services.</p>
    </td>
    </tr>
    <tr id="row45895083"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p26514257"><a name="p26514257"></a><a name="p26514257"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p171215"><a name="p171215"></a><a name="p171215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p13868494"><a name="p13868494"></a><a name="p13868494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p562418271823"><a name="p562418271823"></a><a name="p562418271823"></a>Specifies the sorting field of the VPC endpoint list. The value can be:</p>
    <a name="ul512472071414"></a><a name="ul512472071414"></a><ul id="ul512472071414"><li><strong id="b2551555143814"><a name="b2551555143814"></a><a name="b2551555143814"></a>create_at</strong>: indicates the creation time of the VPC endpoint.</li><li><strong id="b15797171353914"><a name="b15797171353914"></a><a name="b15797171353914"></a>update_at</strong>: indicates the update time of the VPC endpoint.</li></ul>
    <p id="p36041148141413"><a name="p36041148141413"></a><a name="p36041148141413"></a>The default value is <strong id="vpcep_06_0205_b84581912152219"><a name="vpcep_06_0205_b84581912152219"></a><a name="vpcep_06_0205_b84581912152219"></a>create_at</strong>.</p>
    </td>
    </tr>
    <tr id="row43803176"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p58396383"><a name="p58396383"></a><a name="p58396383"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p32486611"><a name="p32486611"></a><a name="p32486611"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p14169835"><a name="p14169835"></a><a name="p14169835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p2195022"><a name="p2195022"></a><a name="p2195022"></a>Specifies the sorting method of the VPC endpoint list. The value can be:</p>
    <a name="ul9628101291617"></a><a name="ul9628101291617"></a><ul id="ul9628101291617"><li><strong id="b383853604518"><a name="b383853604518"></a><a name="b383853604518"></a>desc</strong>: indicates that VPC endpoints are sorted in the descending order.</li><li><strong id="b1313815489454"><a name="b1313815489454"></a><a name="b1313815489454"></a>asc</strong>: indicates that VPC endpoints are sorted in the ascending order.</li></ul>
    <p id="p1719319255168"><a name="p1719319255168"></a><a name="p1719319255168"></a>The default value is <strong id="vpcep_06_0205_b84235270614202"><a name="vpcep_06_0205_b84235270614202"></a><a name="vpcep_06_0205_b84235270614202"></a>desc</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/vpc-endpoints
    ```


## Response<a name="section6891296"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table62266580"></a>
    <table><thead align="left"><tr id="row18576134"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p28271860"><a name="p28271860"></a><a name="p28271860"></a><strong id="b214385500"><a name="b214385500"></a><a name="b214385500"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p8319290"><a name="p8319290"></a><a name="p8319290"></a><strong id="b1420988526"><a name="b1420988526"></a><a name="b1420988526"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p2773889"><a name="p2773889"></a><a name="p2773889"></a><strong id="b641034115"><a name="b641034115"></a><a name="b641034115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23358448"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p12986160"><a name="p12986160"></a><a name="p12986160"></a>endpoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p45246057"><a name="p45246057"></a><a name="p45246057"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p41051970"><a name="p41051970"></a><a name="p41051970"></a>Lists the VPC endpoints. For details, see <a href="#table66917326">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row33923410"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p63441662"><a name="p63441662"></a><a name="p63441662"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p38501023"><a name="p38501023"></a><a name="p38501023"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p31575197"><a name="p31575197"></a><a name="p31575197"></a>Specifies the total number of VPC endpoints that meet the search criteria. The number is not affected by the limit or offset.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  VPC endpoint parameters

    <a name="table66917326"></a>
    <table><thead align="left"><tr id="row13233973"><th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.1"><p id="p65318886"><a name="p65318886"></a><a name="p65318886"></a><strong id="b199751343956"><a name="b199751343956"></a><a name="b199751343956"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.06%" id="mcps1.2.4.1.2"><p id="p56338379"><a name="p56338379"></a><a name="p56338379"></a><strong id="b1533007319"><a name="b1533007319"></a><a name="b1533007319"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="59.27%" id="mcps1.2.4.1.3"><p id="p5964"><a name="p5964"></a><a name="p5964"></a><strong id="b129518153"><a name="b129518153"></a><a name="b129518153"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row483155"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p39135557"><a name="p39135557"></a><a name="p39135557"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p15863564"><a name="p15863564"></a><a name="p15863564"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p9880336"><a name="p9880336"></a><a name="p9880336"></a>Specifies the unique ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row21814164"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p22116861"><a name="p22116861"></a><a name="p22116861"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p46635351"><a name="p46635351"></a><a name="p46635351"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p20173443232"><a name="p20173443232"></a><a name="p20173443232"></a>Specifies the type of the VPC endpoint service that is associated with the VPC endpoint.</p>
    <a name="ul649612552553"></a><a name="ul649612552553"></a><ul id="ul649612552553"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    <p id="p183231822163010"><a name="p183231822163010"></a><a name="p183231822163010"></a>You can perform the operations in <a href="creating-a-vpc-endpoint.md">Creating a VPC Endpoint</a> to create VPC endpoints for accessing VPC endpoints of the gateway and interface types.</p>
    </td>
    </tr>
    <tr id="row40086300"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p25764838"><a name="p25764838"></a><a name="p25764838"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p6577116"><a name="p6577116"></a><a name="p6577116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p9341183673"><a name="p9341183673"></a><a name="p9341183673"></a>Specifies the connection status of the VPC endpoint.</p>
    <a name="ul5651138111613"></a><a name="ul5651138111613"></a><ul id="ul5651138111613"><li><strong id="b7185310918"><a name="b7185310918"></a><a name="b7185310918"></a>pendingAcceptance</strong>: indicates that the VPC endpoint is pending acceptance.</li><li><strong id="b8388551564"><a name="b8388551564"></a><a name="b8388551564"></a>creating</strong>: indicates the VPC endpoint is being created.</li><li><strong id="b58094713615"><a name="b58094713615"></a><a name="b58094713615"></a>accepted</strong>: indicates the VPC endpoint has been accepted.</li><li><strong id="b12181151017617"><a name="b12181151017617"></a><a name="b12181151017617"></a>rejected</strong>: indicates the VPC endpoint has been rejected.</li><li><strong id="b1828515121565"><a name="b1828515121565"></a><a name="b1828515121565"></a>failed</strong>: indicates the creation of the VPC endpoint failed.</li><li><strong id="b851981414616"><a name="b851981414616"></a><a name="b851981414616"></a>deleting</strong>: indicates the VPC endpoint is being deleted.</li></ul>
    </td>
    </tr>
    <tr id="row649392710720"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p5596102919715"><a name="p5596102919715"></a><a name="p5596102919715"></a>active_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p65968291278"><a name="p65968291278"></a><a name="p65968291278"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p14324144165119"><a name="p14324144165119"></a><a name="p14324144165119"></a>Specifies the domain status.</p>
    <a name="ul13303174918418"></a><a name="ul13303174918418"></a><ul id="ul13303174918418"><li><strong id="vpcep_06_0303_b34043383318171"><a name="vpcep_06_0303_b34043383318171"></a><a name="vpcep_06_0303_b34043383318171"></a>frozen</strong>: indicates that the domain is frozen.</li><li><strong id="vpcep_06_0303_b8423527061970"><a name="vpcep_06_0303_b8423527061970"></a><a name="vpcep_06_0303_b8423527061970"></a>active</strong>: indicates that the domain is normal.</li></ul>
    </td>
    </tr>
    <tr id="row13248788"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p66518913"><a name="p66518913"></a><a name="p66518913"></a>endpoint_service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p19322891"><a name="p19322891"></a><a name="p19322891"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p40790059"><a name="p40790059"></a><a name="p40790059"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row60635237"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p12507189"><a name="p12507189"></a><a name="p12507189"></a>marker_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p6449406"><a name="p6449406"></a><a name="p6449406"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p41592001"><a name="p41592001"></a><a name="p41592001"></a>Specifies the packet ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row3996575"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p55287131"><a name="p55287131"></a><a name="p55287131"></a>endpoint_service_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p49072652"><a name="p49072652"></a><a name="p49072652"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p30414410"><a name="p30414410"></a><a name="p30414410"></a>Specifies the ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row4939503"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p64555475"><a name="p64555475"></a><a name="p64555475"></a>enable_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p61610950"><a name="p61610950"></a><a name="p61610950"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p72792580273"><a name="p72792580273"></a><a name="p72792580273"></a>Specifies whether to create a private domain name.</p>
    <a name="ul145169269292"></a><a name="ul145169269292"></a><ul id="ul145169269292"><li><strong id="b145871113172413"><a name="b145871113172413"></a><a name="b145871113172413"></a>true</strong>: indicates that a private domain name is created.</li><li><strong id="b1962121413245"><a name="b1962121413245"></a><a name="b1962121413245"></a>false</strong>: indicates that a private domain name is not created.</li></ul>
    <div class="note" id="note1021533535814"><a name="note1021533535814"></a><a name="note1021533535814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="vpcep_06_0303_p119994525918"><a name="vpcep_06_0303_p119994525918"></a><a name="vpcep_06_0303_p119994525918"></a>When a VPC endpoint for connecting to a gateway VPC endpoint service is created, no private domain name is created no matter <strong id="vpcep_06_0303_b960193116271"><a name="vpcep_06_0303_b960193116271"></a><a name="vpcep_06_0303_b960193116271"></a>enable_dns</strong> is set to <strong id="vpcep_06_0303_b1156335172819"><a name="vpcep_06_0303_b1156335172819"></a><a name="vpcep_06_0303_b1156335172819"></a>true</strong> or <strong id="vpcep_06_0303_b844393752815"><a name="vpcep_06_0303_b844393752815"></a><a name="vpcep_06_0303_b844393752815"></a>false</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row18553230"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p19065375"><a name="p19065375"></a><a name="p19065375"></a>dns_names</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p791512"><a name="p791512"></a><a name="p791512"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p64112473"><a name="p64112473"></a><a name="p64112473"></a>Specifies the domain name for accessing the associated VPC endpoint service.</p>
    <p id="p1755062051318"><a name="p1755062051318"></a><a name="p1755062051318"></a>This parameter is only available when <strong id="vpcep_06_0303_b513454594811"><a name="vpcep_06_0303_b513454594811"></a><a name="vpcep_06_0303_b513454594811"></a>enable_dns</strong> is set to <strong id="vpcep_06_0303_b10660919124617"><a name="vpcep_06_0303_b10660919124617"></a><a name="vpcep_06_0303_b10660919124617"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row64991609"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p29829016"><a name="p29829016"></a><a name="p29829016"></a>ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p231264"><a name="p231264"></a><a name="p231264"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p58649253"><a name="p58649253"></a><a name="p58649253"></a>Specifies the IP address for accessing the associated VPC endpoint service.</p>
    <p id="p6384123752411"><a name="p6384123752411"></a><a name="p6384123752411"></a>This parameter is returned only under the following conditions:</p>
    <a name="ul173695525264"></a><a name="ul173695525264"></a><ul id="ul173695525264"><li>You query a VPC endpoint for accessing an interface VPC endpoint service.</li><li>The connection approval function is enabled for the VPC endpoint service, and the connection has been approved.<p id="vpcep_06_0304_p753135720212"><a name="vpcep_06_0304_p753135720212"></a><a name="vpcep_06_0304_p753135720212"></a>The status of the VPC endpoint can be <strong id="vpcep_06_0304_b918718321178"><a name="vpcep_06_0304_b918718321178"></a><a name="vpcep_06_0304_b918718321178"></a>Accepted</strong> or <strong id="vpcep_06_0304_b14930933772"><a name="vpcep_06_0304_b14930933772"></a><a name="vpcep_06_0304_b14930933772"></a>Rejected</strong>. The <strong id="vpcep_06_0304_b11266144183514"><a name="vpcep_06_0304_b11266144183514"></a><a name="vpcep_06_0304_b11266144183514"></a>Rejected</strong> status only appears when the VPC endpoint is accepted and then rejected.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row27309271653"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p3122202914513"><a name="p3122202914513"></a><a name="p3122202914513"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p131221129354"><a name="p131221129354"></a><a name="p131221129354"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p74750053813"><a name="p74750053813"></a><a name="p74750053813"></a>Specifies the ID of the VPC where the VPC endpoint is to be created.</p>
    </td>
    </tr>
    <tr id="row48344988"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p23629983"><a name="p23629983"></a><a name="p23629983"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p34980450"><a name="p34980450"></a><a name="p34980450"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p1593291111113"><a name="p1593291111113"></a><a name="p1593291111113"></a>Specifies the ID of the subnet created in the VPC specified by <strong id="vpcep_06_0303_b1757761010202"><a name="vpcep_06_0303_b1757761010202"></a><a name="vpcep_06_0303_b1757761010202"></a>vpc_id</strong>. The value is in the UUID format.</p>
    </td>
    </tr>
    <tr id="row66488697"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p16875413"><a name="p16875413"></a><a name="p16875413"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p24731180"><a name="p24731180"></a><a name="p24731180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row43855216"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p62611582"><a name="p62611582"></a><a name="p62611582"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p38373348"><a name="p38373348"></a><a name="p38373348"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p27321481"><a name="p27321481"></a><a name="p27321481"></a>Specifies the update time of the VPC endpoint.</p>
    <p id="p181016810016"><a name="p181016810016"></a><a name="p181016810016"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row56883622"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p44170673"><a name="p44170673"></a><a name="p44170673"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p21054736"><a name="p21054736"></a><a name="p21054736"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p27712044"><a name="p27712044"></a><a name="p27712044"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row726332011274"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p13103244015"><a name="p13103244015"></a><a name="p13103244015"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p21037441512"><a name="p21037441512"></a><a name="p21037441512"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p1510414411116"><a name="p1510414411116"></a><a name="p1510414411116"></a>Lists the resource tags. For details, see <a href="#table489217571060">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row1880234911514"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p121325518514"><a name="p121325518514"></a><a name="p121325518514"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p1113213511156"><a name="p1113213511156"></a><a name="p1113213511156"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p84071479448"><a name="p84071479448"></a><a name="p84071479448"></a>Specifies the error message.</p>
    <p id="p45203393322"><a name="p45203393322"></a><a name="p45203393322"></a>This field is returned when the status of the VPC endpoint changes to <strong id="b118547229151"><a name="b118547229151"></a><a name="b118547229151"></a>failed</strong>. For details, see <a href="#table1736562411812">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row10379344155716"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p165011381477"><a name="p165011381477"></a><a name="p165011381477"></a>whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p450173820473"><a name="p450173820473"></a><a name="p450173820473"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p2538528143320"><a name="p2538528143320"></a><a name="p2538528143320"></a>Specifies the whitelist for controlling access to the VPC endpoint.</p>
    <p id="p386713773414"><a name="p386713773414"></a><a name="p386713773414"></a>If you do not specify this parameter, an empty whitelist is returned.</p>
    <p id="p14661112073410"><a name="p14661112073410"></a><a name="p14661112073410"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row5137168152410"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p050938124710"><a name="p050938124710"></a><a name="p050938124710"></a>enable_whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p85019382479"><a name="p85019382479"></a><a name="p85019382479"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p1458051113412"><a name="p1458051113412"></a><a name="p1458051113412"></a>Specifies whether to enable access control.</p>
    <a name="ul1343419257325"></a><a name="ul1343419257325"></a><ul id="ul1343419257325"><li><strong id="vpcep_06_0303_b11313153317138"><a name="vpcep_06_0303_b11313153317138"></a><a name="vpcep_06_0303_b11313153317138"></a>true</strong>: indicates that access control is enabled.</li><li><strong id="vpcep_06_0303_b12134145911314"><a name="vpcep_06_0303_b12134145911314"></a><a name="vpcep_06_0303_b12134145911314"></a>false</strong>: indicates that access control is disabled.</li></ul>
    <p id="p16973392358"><a name="p16973392358"></a><a name="p16973392358"></a>If you do not specify this parameter, the whitelist is not enabled.</p>
    <p id="p69731393355"><a name="p69731393355"></a><a name="p69731393355"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row17501117248"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p9502038174719"><a name="p9502038174719"></a><a name="p9502038174719"></a>routetables</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.4.1.2 "><p id="p650203810476"><a name="p650203810476"></a><a name="p650203810476"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.27%" headers="mcps1.2.4.1.3 "><p id="p422280153614"><a name="p422280153614"></a><a name="p422280153614"></a>Lists the IDs of route tables.</p>
    <p id="p17737722113611"><a name="p17737722113611"></a><a name="p17737722113611"></a>If you do not specify this parameter, the route table ID of the VPC is returned.</p>
    <p id="p18501138164714"><a name="p18501138164714"></a><a name="p18501138164714"></a>This parameter is available only if you create a VPC endpoint for connecting to a gateway VPC endpoint service.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **ResourceTags**  parameters

    <a name="table489217571060"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.4.1.1"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><strong id="vpcep_06_0201_b1866348132314"><a name="vpcep_06_0201_b1866348132314"></a><a name="vpcep_06_0201_b1866348132314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><strong id="vpcep_06_0201_b616714104231"><a name="vpcep_06_0201_b616714104231"></a><a name="vpcep_06_0201_b616714104231"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.91%" id="mcps1.2.4.1.3"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><strong id="vpcep_06_0201_b163691023811"><a name="vpcep_06_0201_b163691023811"></a><a name="vpcep_06_0201_b163691023811"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters. This parameter cannot be left empty. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a>Specifies the tag value. A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Error parameters

    <a name="table1736562411812"></a>
    <table><thead align="left"><tr id="vpcep_06_0202_row4652255153018"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="vpcep_06_0202_p665015573309"><a name="vpcep_06_0202_p665015573309"></a><a name="vpcep_06_0202_p665015573309"></a><strong id="vpcep_06_0202_b085424117110"><a name="vpcep_06_0202_b085424117110"></a><a name="vpcep_06_0202_b085424117110"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.630000000000003%" id="mcps1.2.4.1.2"><p id="vpcep_06_0202_p865015710307"><a name="vpcep_06_0202_p865015710307"></a><a name="vpcep_06_0202_p865015710307"></a><strong id="vpcep_06_0202_b1597841565"><a name="vpcep_06_0202_b1597841565"></a><a name="vpcep_06_0202_b1597841565"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.029999999999994%" id="mcps1.2.4.1.3"><p id="vpcep_06_0202_p1565011575303"><a name="vpcep_06_0202_p1565011575303"></a><a name="vpcep_06_0202_p1565011575303"></a><strong id="vpcep_06_0202_b1010514442017"><a name="vpcep_06_0202_b1010514442017"></a><a name="vpcep_06_0202_b1010514442017"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0202_row865255513010"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0202_p96501057153013"><a name="vpcep_06_0202_p96501057153013"></a><a name="vpcep_06_0202_p96501057153013"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.630000000000003%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0202_p6650155710309"><a name="vpcep_06_0202_p6650155710309"></a><a name="vpcep_06_0202_p6650155710309"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.029999999999994%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0202_p12650557133019"><a name="vpcep_06_0202_p12650557133019"></a><a name="vpcep_06_0202_p12650557133019"></a>Specifies the error code.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0202_row186521755153018"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0202_p10650057123018"><a name="vpcep_06_0202_p10650057123018"></a><a name="vpcep_06_0202_p10650057123018"></a>error_message</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.630000000000003%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0202_p14650157113016"><a name="vpcep_06_0202_p14650157113016"></a><a name="vpcep_06_0202_p14650157113016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.029999999999994%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0202_p156501957183013"><a name="vpcep_06_0202_p156501957183013"></a><a name="vpcep_06_0202_p156501957183013"></a>Specifies the error message.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {  
    "endpoints":
     [
        {
          "id":"03184a04-95d5-4555-86c4-e767a371ff99",
          "status":"accepted",
          "ip":"192.168.0.232",
          "marker_id":16777337,
          "active_status":"active",
          "vpc_id":"84758cf5-9c62-43ae-a778-3dbd8370c0a4",
          "service_type":"interface",
          "project_id":"295dacf46a4842fcbf7844dc2dc2489d",
          "subnet_id":"68bfbcc1-dff2-47e4-a9d4-332b9bc1b8de",
          "enable_dns":"true",
          "dns_name":"test123",
          "created_at":"2018-10-18T06:49:46Z",
          "updated_at":"2018-10-18T06:49:50Z",
          "endpoint_service_id":"5133655d-0e28-4090-b669-13f87b355c78",
          "endpoint_service_name":"test123",
          "whitelist":["127.0.0.1"],
          "enable_whitelist":true,
          "tags":
            [
              {
                "key":"test1",
                "value":"test1"
              }
            ]
        },
        {
          "id":"43b0e3b0-eec9-49da-866b-6687b75f9fe5",
          "status":"accepted",
          "ip":"192.168.0.115",
          "marker_id":16777322,
          "active_status":"active",
          "vpc_id":"e251b400-2963-4131-b38a-da81e32026ee",
          "service_type":"interface",
          "project_id":"295dacf46a4842fcbf7844dc2dc2489d",
          "subnet_id":"65528a22-59a1-4972-ba64-88984b3207cd",
          "enable_dns":"true",
          "dns_name":"test123",
          "created_at":"2018-10-18T06:36:20Z",
          "updated_at":"2018-10-18T06:36:24Z",
          "endpoint_service_id":"5133655d-0e28-4090-b669-13f87b355c78",
          "endpoint_service_name":"test123",
          "whitelist":["127.0.0.1"],
          "enable_whitelist":true,
          "tags":
            [
              {
                "key":"test1",
                "value":"test1"
              }
            ]
        }
     ],
     "total_count":17
    }
    ```


## Status Code<a name="section21324079"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

