# Accepting or Rejecting a VPC Endpoint for a VPC Endpoint Service<a name="vpcep_06_0207"></a>

## Function<a name="section63412692"></a>

This API is used to accept or reject a VPC endpoint for a VPC endpoint service.

## URI<a name="section33843318"></a>

Format

POST /v1/\{project\_id\}/vpc-endpoint-services/\{vpc\_endpoint\_service\_id\}/connections/action

[Table 1](#table25752879)  describes the required parameters.

**Table  1**  Parameters

<a name="table25752879"></a>
<table><thead align="left"><tr id="row57361053"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p15733705"><a name="p15733705"></a><a name="p15733705"></a><strong id="b16701248121820"><a name="b16701248121820"></a><a name="b16701248121820"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p66470553"><a name="p66470553"></a><a name="p66470553"></a><strong id="b10841164917184"><a name="b10841164917184"></a><a name="b10841164917184"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p15405685"><a name="p15405685"></a><a name="p15405685"></a><strong id="b47195191817"><a name="b47195191817"></a><a name="b47195191817"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row39900998"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p10755444"><a name="p10755444"></a><a name="p10755444"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p65884646"><a name="p65884646"></a><a name="p65884646"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p35056133"><a name="p35056133"></a><a name="p35056133"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row47069744"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p2525846205519"><a name="p2525846205519"></a><a name="p2525846205519"></a>vpc_endpoint_service_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p952520469552"><a name="p952520469552"></a><a name="p952520469552"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p85254465554"><a name="p85254465554"></a><a name="p85254465554"></a>Specifies the ID of the VPC endpoint service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section36154407"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table5608491"></a>
    <table><thead align="left"><tr id="row12498161"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p5718131"><a name="p5718131"></a><a name="p5718131"></a><strong id="b15495210161914"><a name="b15495210161914"></a><a name="b15495210161914"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.2"><p id="p60515490"><a name="p60515490"></a><a name="p60515490"></a><strong id="b1106278819"><a name="b1106278819"></a><a name="b1106278819"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p2807653"><a name="p2807653"></a><a name="p2807653"></a><strong id="b15863193613199"><a name="b15863193613199"></a><a name="b15863193613199"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p26093349"><a name="p26093349"></a><a name="p26093349"></a><strong id="b171755761"><a name="b171755761"></a><a name="b171755761"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33186505"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p3752378"><a name="p3752378"></a><a name="p3752378"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p35507167"><a name="p35507167"></a><a name="p35507167"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p57508256"><a name="p57508256"></a><a name="p57508256"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p395953515810"><a name="p395953515810"></a><a name="p395953515810"></a>Specifies whether to accept or reject a VPC endpoint for a VPC endpoint service.</p>
    <a name="ul435862711616"></a><a name="ul435862711616"></a><ul id="ul435862711616"><li><strong id="b5810642182211"><a name="b5810642182211"></a><a name="b5810642182211"></a>receive</strong>: means to accept the VPC endpoint.</li><li><strong id="b11381722182316"><a name="b11381722182316"></a><a name="b11381722182316"></a>reject</strong>: means to reject the VPC endpoint.</li></ul>
    </td>
    </tr>
    <tr id="row25639961"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p63570976"><a name="p63570976"></a><a name="p63570976"></a>endpoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p48975460"><a name="p48975460"></a><a name="p48975460"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p7589324"><a name="p7589324"></a><a name="p7589324"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p10755521"><a name="p10755521"></a><a name="p10755521"></a>Lists the VPC endpoints.</p>
    <p id="p1131733311216"><a name="p1131733311216"></a><a name="p1131733311216"></a>Each request accepts or rejects only one VPC endpoint.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    This request is to accept VPC endpoint  **705290f3-0d00-41f2-aedc-71f09844e879**  to connect to VPC endpoint service  **4189d3c2-8882-4871-a3c2-d380272eed88**.

    ```
    POST https://{endpoint}/v1/{project_id}/vpc-endpoint-services/4189d3c2-8882-4871-a3c2-d380272eed88/connections/action
    ```

    ```
    { 
       "endpoints":["705290f3-0d00-41f2-aedc-71f09844e879"],
       "action": "receive"
    }
    ```


## Response<a name="section42825826"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table50476419"></a>
    <table><thead align="left"><tr id="row8264929"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p65479535"><a name="p65479535"></a><a name="p65479535"></a><strong id="b1190034083"><a name="b1190034083"></a><a name="b1190034083"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p2242093"><a name="p2242093"></a><a name="p2242093"></a><strong id="b1758224382"><a name="b1758224382"></a><a name="b1758224382"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p47391811"><a name="p47391811"></a><a name="p47391811"></a><strong id="b378315221"><a name="b378315221"></a><a name="b378315221"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13531482"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p22308249"><a name="p22308249"></a><a name="p22308249"></a>connections</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p62137769"><a name="p62137769"></a><a name="p62137769"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p67103410"><a name="p67103410"></a><a name="p67103410"></a>Lists the connections. For details, see <a href="#table31325900">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Connection parameters

    <a name="table31325900"></a>
    <table><thead align="left"><tr id="row37736931"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.4.1.1"><p id="p36792583"><a name="p36792583"></a><a name="p36792583"></a><strong id="b657875212245"><a name="b657875212245"></a><a name="b657875212245"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.58%" id="mcps1.2.4.1.2"><p id="p27409210"><a name="p27409210"></a><a name="p27409210"></a><strong id="b309700308"><a name="b309700308"></a><a name="b309700308"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.68000000000001%" id="mcps1.2.4.1.3"><p id="p5553575"><a name="p5553575"></a><a name="p5553575"></a><strong id="b548551611"><a name="b548551611"></a><a name="b548551611"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47186420"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.1 "><p id="p64003657"><a name="p64003657"></a><a name="p64003657"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.58%" headers="mcps1.2.4.1.2 "><p id="p16913743"><a name="p16913743"></a><a name="p16913743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p27835949"><a name="p27835949"></a><a name="p27835949"></a>Specifies the unique ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row49196957"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.1 "><p id="p25530612"><a name="p25530612"></a><a name="p25530612"></a>marker_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.58%" headers="mcps1.2.4.1.2 "><p id="p54713654"><a name="p54713654"></a><a name="p54713654"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p2621005"><a name="p2621005"></a><a name="p2621005"></a>Specifies the packet ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row23589052"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.1 "><p id="p31665069"><a name="p31665069"></a><a name="p31665069"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.58%" headers="mcps1.2.4.1.2 "><p id="p14733798"><a name="p14733798"></a><a name="p14733798"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row3521175"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.1 "><p id="p16779757"><a name="p16779757"></a><a name="p16779757"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.58%" headers="mcps1.2.4.1.2 "><p id="p16983047"><a name="p16983047"></a><a name="p16983047"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p27321481"><a name="p27321481"></a><a name="p27321481"></a>Specifies the update time of the VPC endpoint.</p>
    <p id="p181016810016"><a name="p181016810016"></a><a name="p181016810016"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row32610493"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.1 "><p id="p24204273"><a name="p24204273"></a><a name="p24204273"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.58%" headers="mcps1.2.4.1.2 "><p id="p14389126"><a name="p14389126"></a><a name="p14389126"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p24668580"><a name="p24668580"></a><a name="p24668580"></a>Specifies the user's domain ID.</p>
    </td>
    </tr>
    <tr id="row20690629"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.1 "><p id="p65328258"><a name="p65328258"></a><a name="p65328258"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.58%" headers="mcps1.2.4.1.2 "><p id="p57097564"><a name="p57097564"></a><a name="p57097564"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p583352918492"><a name="p583352918492"></a><a name="p583352918492"></a>Specifies the connection status of the VPC endpoint.</p>
    <a name="ul1730143812614"></a><a name="ul1730143812614"></a><ul id="ul1730143812614"><li><strong id="b676735219545"><a name="b676735219545"></a><a name="b676735219545"></a>accepted</strong>: indicates the VPC endpoint has been accepted.</li><li><strong id="b1418684416262"><a name="b1418684416262"></a><a name="b1418684416262"></a>rejected</strong>: indicates the VPC endpoint has been rejected.</li></ul>
    </td>
    </tr>
    <tr id="row4751534"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.4.1.1 "><p id="p94959157573"><a name="p94959157573"></a><a name="p94959157573"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.58%" headers="mcps1.2.4.1.2 "><p id="p04951415205715"><a name="p04951415205715"></a><a name="p04951415205715"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p84071479448"><a name="p84071479448"></a><a name="p84071479448"></a>Specifies the error message.</p>
    <p id="p45203393322"><a name="p45203393322"></a><a name="p45203393322"></a>This field is returned when the status of the VPC endpoint service changes to <strong id="b19966145141415"><a name="b19966145141415"></a><a name="b19966145141415"></a>failed</strong>. For details, see <a href="#table1979118317570">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Error parameters

    <a name="table1979118317570"></a>
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
      "connections":
     [
       {
          "id":"4189d3c2-8882-4871-a3c2-d380272eed83",
          "status":"accepted",
          "marker_id":422321321312321321,
          "domain_id":"6e9dfd51d1124e8d8498dce894923a0d",
          "created_at":"2018-01-30T07:42:01.174",
          "updated_at":"2018-01-30T07:42:01.174"
           }
       ]
    }
    ```

    or

    ```
    {
      "error_code": "Endpoint.2013"
      "error_msg": "The endpoint does not belong to the endpoint service."
    }
    ```


## Status Code<a name="section46339886"></a>

For details about status codes, see  [Status Code](status-code.md).

