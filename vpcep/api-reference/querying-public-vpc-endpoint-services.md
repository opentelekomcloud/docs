# Querying Public VPC Endpoint Services<a name="vpcep_06_0301"></a>

## Function<a name="section1226995"></a>

This API is used to query public VPC endpoint services. These services are created by operations people and can be visible to and assessed by all users.

## URI<a name="section11042957"></a>

GET /v1/\{project\_id\}/vpc-endpoint-services/public?limit=\{limit\}&offset=\{offset\}&endpoint\_service\_name=\{endpoint\_service\_name\}&id=\{endpoint\_service\_id\}&sort\_key=\{sort\_key\}&sort\_dir=\{sort\_dir\}

[Table 1](#table52235709)  describes the required parameters.

**Table  1**  Parameters

<a name="table52235709"></a>
<table><thead align="left"><tr id="row50088028"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p30598464"><a name="p30598464"></a><a name="p30598464"></a><strong id="b13906917134110"><a name="b13906917134110"></a><a name="b13906917134110"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p62556549"><a name="p62556549"></a><a name="p62556549"></a><strong id="b88701118124110"><a name="b88701118124110"></a><a name="b88701118124110"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p33915731"><a name="p33915731"></a><a name="p33915731"></a><strong id="b1577412196418"><a name="b1577412196418"></a><a name="b1577412196418"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row62819665"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p55228071"><a name="p55228071"></a><a name="p55228071"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p44288766"><a name="p44288766"></a><a name="p44288766"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p30620285"><a name="p30620285"></a><a name="p30620285"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section32277752"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table15507252"></a>
    <table><thead align="left"><tr id="row19550945"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p40122709"><a name="p40122709"></a><a name="p40122709"></a><strong id="b4886252426"><a name="b4886252426"></a><a name="b4886252426"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.2"><p id="p28714026"><a name="p28714026"></a><a name="p28714026"></a><strong id="b107425283"><a name="b107425283"></a><a name="b107425283"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p44134792"><a name="p44134792"></a><a name="p44134792"></a><strong id="b138371333184217"><a name="b138371333184217"></a><a name="b138371333184217"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p18148374"><a name="p18148374"></a><a name="p18148374"></a><strong id="b683995851"><a name="b683995851"></a><a name="b683995851"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60732156"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p20357603"><a name="p20357603"></a><a name="p20357603"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p38353138"><a name="p38353138"></a><a name="p38353138"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p19596498"><a name="p19596498"></a><a name="p19596498"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p43812523"><a name="p43812523"></a><a name="p43812523"></a>Specifies the maximum number of public VPC endpoint services displayed on each page.</p>
    <p id="p58768388"><a name="p58768388"></a><a name="p58768388"></a>The value ranges from <strong id="b059014481693"><a name="b059014481693"></a><a name="b059014481693"></a>0</strong> to <strong id="b18994550791"><a name="b18994550791"></a><a name="b18994550791"></a>1000</strong> and is generally <strong id="b14762151110419"><a name="b14762151110419"></a><a name="b14762151110419"></a>10</strong>, <strong id="b157634113418"><a name="b157634113418"></a><a name="b157634113418"></a>20</strong>, or <strong id="b6764141117412"><a name="b6764141117412"></a><a name="b6764141117412"></a>50</strong>. The default value is <strong id="b1876421111411"><a name="b1876421111411"></a><a name="b1876421111411"></a>10</strong>.</p>
    </td>
    </tr>
    <tr id="row59153444"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p26699621"><a name="p26699621"></a><a name="p26699621"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p15185687"><a name="p15185687"></a><a name="p15185687"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p22081121"><a name="p22081121"></a><a name="p22081121"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p5736126132214"><a name="p5736126132214"></a><a name="p5736126132214"></a>Specifies the offset.</p>
    <p id="p11912494222"><a name="p11912494222"></a><a name="p11912494222"></a>All VPC endpoint services after this offset will be queried. The value must be an integer greater than 0 but less than the number of VPC endpoint services.</p>
    </td>
    </tr>
    <tr id="row58119249"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p10038752"><a name="p10038752"></a><a name="p10038752"></a>endpoint_service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p7832579"><a name="p7832579"></a><a name="p7832579"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p30459171"><a name="p30459171"></a><a name="p30459171"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p51273767"><a name="p51273767"></a><a name="p51273767"></a>Specifies the name of the public VPC endpoint service. The value is not case-sensitive and supports fuzzy match.</p>
    </td>
    </tr>
    <tr id="row58810722"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p66048056"><a name="p66048056"></a><a name="p66048056"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p48292326"><a name="p48292326"></a><a name="p48292326"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p19364373"><a name="p19364373"></a><a name="p19364373"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p25010413"><a name="p25010413"></a><a name="p25010413"></a>Specifies the unique ID of the public VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row23767127"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p46089150"><a name="p46089150"></a><a name="p46089150"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p42233698"><a name="p42233698"></a><a name="p42233698"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p65486378"><a name="p65486378"></a><a name="p65486378"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p562418271823"><a name="p562418271823"></a><a name="p562418271823"></a>Specifies the sorting field of the VPC endpoint service list. The value can be:</p>
    <a name="ul512472071414"></a><a name="ul512472071414"></a><ul id="ul512472071414"><li><strong id="vpcep_06_0205_b91061528181018"><a name="vpcep_06_0205_b91061528181018"></a><a name="vpcep_06_0205_b91061528181018"></a>create_at</strong>: indicates that VPC endpoint services are sorted by creation time.</li><li><strong id="vpcep_06_0205_b10717101561115"><a name="vpcep_06_0205_b10717101561115"></a><a name="vpcep_06_0205_b10717101561115"></a>update_at</strong>: indicates that VPC endpoint services are sorted by update time.</li></ul>
    <p id="p36041148141413"><a name="p36041148141413"></a><a name="p36041148141413"></a>The default value is <strong id="vpcep_06_0205_b84581912152219"><a name="vpcep_06_0205_b84581912152219"></a><a name="vpcep_06_0205_b84581912152219"></a>create_at</strong>.</p>
    </td>
    </tr>
    <tr id="row25167737"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p25320844"><a name="p25320844"></a><a name="p25320844"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p37722463"><a name="p37722463"></a><a name="p37722463"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p35620634"><a name="p35620634"></a><a name="p35620634"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p2195022"><a name="p2195022"></a><a name="p2195022"></a>Specifies the sorting method of the VPC endpoint service list. The value can be:</p>
    <a name="ul9628101291617"></a><a name="ul9628101291617"></a><ul id="ul9628101291617"><li><strong id="vpcep_06_0205_b842352706193046"><a name="vpcep_06_0205_b842352706193046"></a><a name="vpcep_06_0205_b842352706193046"></a>desc</strong>: indicates that VPC endpoint services are sorted in the descending order.</li><li><strong id="vpcep_06_0205_b84235270619316"><a name="vpcep_06_0205_b84235270619316"></a><a name="vpcep_06_0205_b84235270619316"></a>asc</strong>: indicates that VPC endpoint services are sorted in the ascending order.</li></ul>
    <p id="p1719319255168"><a name="p1719319255168"></a><a name="p1719319255168"></a>The default value is <strong id="vpcep_06_0205_b84235270614202"><a name="vpcep_06_0205_b84235270614202"></a><a name="vpcep_06_0205_b84235270614202"></a>desc</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/vpc-endpoint-services/public
    ```


## Response<a name="section64361134"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table359340"></a>
    <table><thead align="left"><tr id="row55100582"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p33962133"><a name="p33962133"></a><a name="p33962133"></a><strong id="b1293000420"><a name="b1293000420"></a><a name="b1293000420"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p66578241"><a name="p66578241"></a><a name="p66578241"></a><strong id="b1352283230"><a name="b1352283230"></a><a name="b1352283230"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p24128401"><a name="p24128401"></a><a name="p24128401"></a><strong id="b1823487449"><a name="b1823487449"></a><a name="b1823487449"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8243437"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p63738686"><a name="p63738686"></a><a name="p63738686"></a>endpoint_services</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p62559980"><a name="p62559980"></a><a name="p62559980"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p34193630"><a name="p34193630"></a><a name="p34193630"></a>Lists the VPC endpoint services. For details, see <a href="#table55935485">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row39307221"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p29768296"><a name="p29768296"></a><a name="p29768296"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p62421813"><a name="p62421813"></a><a name="p62421813"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p23002082"><a name="p23002082"></a><a name="p23002082"></a>Specifies the total number of public VPC endpoint services that meet the search criteria. The number is not affected by the limit or offset.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **endpoint\_service**  parameters

    <a name="table55935485"></a>
    <table><thead align="left"><tr id="row2212450"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.1"><p id="p44990746"><a name="p44990746"></a><a name="p44990746"></a><strong id="b01908481117"><a name="b01908481117"></a><a name="b01908481117"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.659999999999997%" id="mcps1.2.4.1.2"><p id="p20371786"><a name="p20371786"></a><a name="p20371786"></a><strong id="b693409362"><a name="b693409362"></a><a name="b693409362"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.1%" id="mcps1.2.4.1.3"><p id="p39501979"><a name="p39501979"></a><a name="p39501979"></a><strong id="b914946694"><a name="b914946694"></a><a name="b914946694"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45543732"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p65163710"><a name="p65163710"></a><a name="p65163710"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.659999999999997%" headers="mcps1.2.4.1.2 "><p id="p43769185"><a name="p43769185"></a><a name="p43769185"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.1%" headers="mcps1.2.4.1.3 "><p id="p55643076"><a name="p55643076"></a><a name="p55643076"></a>Specifies the unique ID of the public VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row50153511499"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p22343611293"><a name="p22343611293"></a><a name="p22343611293"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.659999999999997%" headers="mcps1.2.4.1.2 "><p id="p1234176152920"><a name="p1234176152920"></a><a name="p1234176152920"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.1%" headers="mcps1.2.4.1.3 "><p id="p1234266298"><a name="p1234266298"></a><a name="p1234266298"></a>Specifies the owner of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row31025637"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p30048651"><a name="p30048651"></a><a name="p30048651"></a>service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.659999999999997%" headers="mcps1.2.4.1.2 "><p id="p18021703"><a name="p18021703"></a><a name="p18021703"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.1%" headers="mcps1.2.4.1.3 "><p id="p50471806"><a name="p50471806"></a><a name="p50471806"></a>Specifies the name of the public VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row51593076"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p18289650"><a name="p18289650"></a><a name="p18289650"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.659999999999997%" headers="mcps1.2.4.1.2 "><p id="p5066656"><a name="p5066656"></a><a name="p5066656"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.1%" headers="mcps1.2.4.1.3 "><div class="p" id="p135911520141219"><a name="p135911520141219"></a><a name="p135911520141219"></a>Specifies the type of the VPC endpoint service. The value can be:<a name="en-us_topic_0178993304_ul87241928184613"></a><a name="en-us_topic_0178993304_ul87241928184613"></a><ul id="en-us_topic_0178993304_ul87241928184613"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    </div>
    <p id="p941115410718"><a name="p941115410718"></a><a name="p941115410718"></a>You can perform the operations in <a href="creating-a-vpc-endpoint.md">Creating a VPC Endpoint</a> to create VPC endpoints for accessing VPC endpoints of the gateway and interface types.</p>
    </td>
    </tr>
    <tr id="row2604762"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p9659160"><a name="p9659160"></a><a name="p9659160"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.659999999999997%" headers="mcps1.2.4.1.2 "><p id="p44194499"><a name="p44194499"></a><a name="p44194499"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.1%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint service.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row1162673919385"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p2089991612413"><a name="p2089991612413"></a><a name="p2089991612413"></a>is_charge</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.659999999999997%" headers="mcps1.2.4.1.2 "><p id="p68996168416"><a name="p68996168416"></a><a name="p68996168416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.1%" headers="mcps1.2.4.1.3 "><p id="p1389951614111"><a name="p1389951614111"></a><a name="p1389951614111"></a>Specifies whether the associated VPC endpoint carries a charge.</p>
    <a name="ul4942193713444"></a><a name="ul4942193713444"></a><ul id="ul4942193713444"><li><strong id="b19200830195415"><a name="b19200830195415"></a><a name="b19200830195415"></a>true</strong>: indicates that the associated VPC endpoint carries a charge.</li><li><strong id="b950713385556"><a name="b950713385556"></a><a name="b950713385556"></a>false</strong>: indicates that the associated VPC endpoint does not a charge.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "endpoint_services": [
        {
          "id": "b0e22f6f-26f4-461c-b140-d873464d4fa0",
          "owner": "example"
          "service_name": "test123",
          "service_type": "interface",
          "created_at": "2018-09-10T13:13:23Z",
          "is_charge": "true"
        },
    	{
          "id": "26391a76-546b-42a9-b2fc-496ec68c0e4d",
          "owner": "example"
          "service_name":  "OBS",
          "service_type": "gateway",
          "created_at": "2019-03-28T09:30:27Z",
          "is_charge": "true"
        }
      ],
      "total_count": 2
    }
    ```


## Status Code<a name="section45869372"></a>

For details about status codes, see  [Status Code](status-code.md).

