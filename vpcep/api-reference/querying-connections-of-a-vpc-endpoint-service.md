# Querying Connections of a VPC Endpoint Service<a name="vpcep_06_0206"></a>

## Function<a name="section59609807"></a>

This API is used to query connections of a VPC endpoint service. The marker ID is the unique ID of each connection.

## URI<a name="section66726219"></a>

Format

GET /v1/\{project\_id\}/vpc-endpoint-services/\{vpc\_endpoint\_service\_id\}/connections?id=\{vpc\_endpoint\_id\}&marker\_id=\{marker\_id\}&sort\_key=\{sort\_key\}&sort\_dir=\{sort\_dir\}&limit=\{limit\}&offset=\{offset\}

[Table 1](#table36274863)  describes the required parameters.

**Table  1**  Parameters

<a name="table36274863"></a>
<table><thead align="left"><tr id="row8393309"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p8769420"><a name="p8769420"></a><a name="p8769420"></a><strong id="b20111832112818"><a name="b20111832112818"></a><a name="b20111832112818"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p39234444"><a name="p39234444"></a><a name="p39234444"></a><strong id="b189663352812"><a name="b189663352812"></a><a name="b189663352812"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p23873413"><a name="p23873413"></a><a name="p23873413"></a><strong id="b2012193413286"><a name="b2012193413286"></a><a name="b2012193413286"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row54698270"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p1374847"><a name="p1374847"></a><a name="p1374847"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p44253777"><a name="p44253777"></a><a name="p44253777"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p27786171"><a name="p27786171"></a><a name="p27786171"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row48748953"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p56351131"><a name="p56351131"></a><a name="p56351131"></a>vpc_endpoint_service_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p1038922"><a name="p1038922"></a><a name="p1038922"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p17043853"><a name="p17043853"></a><a name="p17043853"></a>Specifies the ID of the VPC endpoint service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section63665063"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table52582818"></a>
    <table><thead align="left"><tr id="row52789044"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p48054166"><a name="p48054166"></a><a name="p48054166"></a><strong id="b4618154752810"><a name="b4618154752810"></a><a name="b4618154752810"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.2"><p id="p73360"><a name="p73360"></a><a name="p73360"></a><strong id="b19897611"><a name="b19897611"></a><a name="b19897611"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p5942219"><a name="p5942219"></a><a name="p5942219"></a><strong id="b92291454292"><a name="b92291454292"></a><a name="b92291454292"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p11557743"><a name="p11557743"></a><a name="p11557743"></a><strong id="b1749833766"><a name="b1749833766"></a><a name="b1749833766"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63761954"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p64444687"><a name="p64444687"></a><a name="p64444687"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p52637148"><a name="p52637148"></a><a name="p52637148"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p35750577"><a name="p35750577"></a><a name="p35750577"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p10115639"><a name="p10115639"></a><a name="p10115639"></a>Specifies the unique ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row23931892"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p59435077"><a name="p59435077"></a><a name="p59435077"></a>marker_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p49511964"><a name="p49511964"></a><a name="p49511964"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p51046110"><a name="p51046110"></a><a name="p51046110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p41094261"><a name="p41094261"></a><a name="p41094261"></a>Specifies the packet ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row34304036"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p27163541"><a name="p27163541"></a><a name="p27163541"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p52763214"><a name="p52763214"></a><a name="p52763214"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p45961976"><a name="p45961976"></a><a name="p45961976"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p562418271823"><a name="p562418271823"></a><a name="p562418271823"></a>Specifies the sorting field of the VPC endpoint list. The value can be:</p>
    <a name="ul512472071414"></a><a name="ul512472071414"></a><ul id="ul512472071414"><li><strong id="b131528358343"><a name="b131528358343"></a><a name="b131528358343"></a>create_at</strong>: indicates the creation time of the VPC endpoint.</li><li><strong id="b168571558133414"><a name="b168571558133414"></a><a name="b168571558133414"></a>update_at</strong>: indicates the update time of the VPC endpoint.</li></ul>
    <p id="p36041148141413"><a name="p36041148141413"></a><a name="p36041148141413"></a>The default value is <strong id="vpcep_06_0205_b84581912152219"><a name="vpcep_06_0205_b84581912152219"></a><a name="vpcep_06_0205_b84581912152219"></a>create_at</strong>.</p>
    </td>
    </tr>
    <tr id="row18957973"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p59200815"><a name="p59200815"></a><a name="p59200815"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p30536693"><a name="p30536693"></a><a name="p30536693"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p57553105"><a name="p57553105"></a><a name="p57553105"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p2195022"><a name="p2195022"></a><a name="p2195022"></a>Specifies the sorting method of the VPC endpoint list. The value can be:</p>
    <a name="ul9628101291617"></a><a name="ul9628101291617"></a><ul id="ul9628101291617"><li><strong id="b4405105916458"><a name="b4405105916458"></a><a name="b4405105916458"></a>desc</strong>: indicates that VPC endpoints are sorted in the descending order.</li><li><strong id="b20953813164614"><a name="b20953813164614"></a><a name="b20953813164614"></a>asc</strong>: indicates that VPC endpoints are sorted in the ascending order.</li></ul>
    <p id="p1719319255168"><a name="p1719319255168"></a><a name="p1719319255168"></a>The default value is <strong id="vpcep_06_0205_b84235270614202"><a name="vpcep_06_0205_b84235270614202"></a><a name="vpcep_06_0205_b84235270614202"></a>desc</strong>.</p>
    </td>
    </tr>
    <tr id="row60429836"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p62978522"><a name="p62978522"></a><a name="p62978522"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p986624"><a name="p986624"></a><a name="p986624"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p12807719"><a name="p12807719"></a><a name="p12807719"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p30792310"><a name="p30792310"></a><a name="p30792310"></a>Specifies the maximum number of connections displayed on each page.</p>
    <p id="p8695341"><a name="p8695341"></a><a name="p8695341"></a>The value ranges from <strong id="b11334153516916"><a name="b11334153516916"></a><a name="b11334153516916"></a>0</strong> to <strong id="b18135173816911"><a name="b18135173816911"></a><a name="b18135173816911"></a>1000</strong> and is generally <strong id="b18432047311"><a name="b18432047311"></a><a name="b18432047311"></a>10</strong>,<strong id="b194327474118"><a name="b194327474118"></a><a name="b194327474118"></a> 20</strong>, or <strong id="b743316471615"><a name="b743316471615"></a><a name="b743316471615"></a>50</strong>. The default value is <strong id="b1434247811"><a name="b1434247811"></a><a name="b1434247811"></a>10</strong>.</p>
    </td>
    </tr>
    <tr id="row11149206"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p30670511"><a name="p30670511"></a><a name="p30670511"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p1283432"><a name="p1283432"></a><a name="p1283432"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p36849129"><a name="p36849129"></a><a name="p36849129"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p5736126132214"><a name="p5736126132214"></a><a name="p5736126132214"></a>Specifies the offset.</p>
    <p id="p11912494222"><a name="p11912494222"></a><a name="p11912494222"></a>All VPC endpoint services after this offset will be queried. The value must be an integer greater than 0 but less than the number of VPC endpoint services.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    This request is to query connections of the VPC endpoint service whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed88**.

    ```
    GET https://{endpoint}/v1/{project_id}/vpc-endpoint-services/4189d3c2-8882-4871-a3c2-d380272eed88/connections
    ```


## Response<a name="section56596492"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table3483316"></a>
    <table><thead align="left"><tr id="row57609611"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p35866908"><a name="p35866908"></a><a name="p35866908"></a><strong id="b1081759740"><a name="b1081759740"></a><a name="b1081759740"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p19538401"><a name="p19538401"></a><a name="p19538401"></a><strong id="b1963200347"><a name="b1963200347"></a><a name="b1963200347"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p39106626"><a name="p39106626"></a><a name="p39106626"></a><strong id="b1363230059"><a name="b1363230059"></a><a name="b1363230059"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13520169"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p21391867"><a name="p21391867"></a><a name="p21391867"></a>connections</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p55019682"><a name="p55019682"></a><a name="p55019682"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p27409286"><a name="p27409286"></a><a name="p27409286"></a>Lists the connections. For details, see <a href="#table35346078">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row45356986"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p50037251"><a name="p50037251"></a><a name="p50037251"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p26485565"><a name="p26485565"></a><a name="p26485565"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p19295714142518"><a name="p19295714142518"></a><a name="p19295714142518"></a>Specifies the total number of VPC endpoints that meet the search criteria. The number is not affected by the limit or offset.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Connection parameters

    <a name="table35346078"></a>
    <table><thead align="left"><tr id="row47425555"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p16264769"><a name="p16264769"></a><a name="p16264769"></a><strong id="b152329173414"><a name="b152329173414"></a><a name="b152329173414"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.73%" id="mcps1.2.4.1.2"><p id="p42377887"><a name="p42377887"></a><a name="p42377887"></a><strong id="b1771072993"><a name="b1771072993"></a><a name="b1771072993"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.779999999999994%" id="mcps1.2.4.1.3"><p id="p10056789"><a name="p10056789"></a><a name="p10056789"></a><strong id="b1486846998"><a name="b1486846998"></a><a name="b1486846998"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9293580"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p14582507"><a name="p14582507"></a><a name="p14582507"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.4.1.2 "><p id="p40332443"><a name="p40332443"></a><a name="p40332443"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.779999999999994%" headers="mcps1.2.4.1.3 "><p id="p45702468"><a name="p45702468"></a><a name="p45702468"></a>Specifies the unique ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row8669029"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p31102709"><a name="p31102709"></a><a name="p31102709"></a>marker_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.4.1.2 "><p id="p36291473"><a name="p36291473"></a><a name="p36291473"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.779999999999994%" headers="mcps1.2.4.1.3 "><p id="p53928226"><a name="p53928226"></a><a name="p53928226"></a>Specifies the packet ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row15591994"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p54992021"><a name="p54992021"></a><a name="p54992021"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.4.1.2 "><p id="p25168729"><a name="p25168729"></a><a name="p25168729"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.779999999999994%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row27283604"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p62488324"><a name="p62488324"></a><a name="p62488324"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.4.1.2 "><p id="p28389464"><a name="p28389464"></a><a name="p28389464"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.779999999999994%" headers="mcps1.2.4.1.3 "><p id="p27321481"><a name="p27321481"></a><a name="p27321481"></a>Specifies the update time of the VPC endpoint.</p>
    <p id="p181016810016"><a name="p181016810016"></a><a name="p181016810016"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row26389441"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p57169983"><a name="p57169983"></a><a name="p57169983"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.4.1.2 "><p id="p257086"><a name="p257086"></a><a name="p257086"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.779999999999994%" headers="mcps1.2.4.1.3 "><p id="p20824038"><a name="p20824038"></a><a name="p20824038"></a>Specifies the user's domain ID.</p>
    </td>
    </tr>
    <tr id="row53198616"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p14120655"><a name="p14120655"></a><a name="p14120655"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.73%" headers="mcps1.2.4.1.2 "><p id="p2922435"><a name="p2922435"></a><a name="p2922435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.779999999999994%" headers="mcps1.2.4.1.3 "><p id="p583352918492"><a name="p583352918492"></a><a name="p583352918492"></a>Specifies the connection status of the VPC endpoint.</p>
    <a name="ul1860111019616"></a><a name="ul1860111019616"></a><ul id="ul1860111019616"><li><strong id="b164761182419"><a name="b164761182419"></a><a name="b164761182419"></a>pendingAcceptance</strong>: indicates that the VPC endpoint is pending acceptance.</li><li><strong id="b7464355131310"><a name="b7464355131310"></a><a name="b7464355131310"></a>creating</strong>: indicates the VPC endpoint is being created.</li><li><strong id="b16976115612137"><a name="b16976115612137"></a><a name="b16976115612137"></a>accepted</strong>: indicates the VPC endpoint has been accepted.</li><li><strong id="b181305583138"><a name="b181305583138"></a><a name="b181305583138"></a>rejected</strong>: indicates the VPC endpoint has been rejected.</li><li><strong id="b9399155911311"><a name="b9399155911311"></a><a name="b9399155911311"></a>failed</strong>: indicates the creation of the VPC endpoint failed.</li><li><strong id="b11461337105417"><a name="b11461337105417"></a><a name="b11461337105417"></a>deleting</strong>: indicates the VPC endpoint is being deleted.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "connections": [
        {
          "id": "adb7b229-bb11-4072-bcc0-3327cd784263",
          "status": "accepted",
          "marker_id": 16777510,
          "domain_id": "5fc973eea581490997e82ea11a1df31f",
          "created_at": "2018-09-17T11:10:11Z",
          "updated_at": "2018-09-17T11:10:12Z"
        },
        {
          "id": "fd69d29f-dc29-4a9b-80d8-b51d1e7e58ea",
          "status": "accepted",
          "marker_id": 16777513,
          "domain_id": "5fc973eea581490997e82ea11a1df31f",
          "created_at": "2018-09-17T07:28:56Z",
          "updated_at": "2018-09-17T07:28:58Z"
        }
      ],
      "total_count":2
    }
    ```


## Status Code<a name="section20913125"></a>

For details about status codes, see  [Status Code](status-code.md).

