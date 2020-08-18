# Querying the Whitelist Records of a VPC Endpoint Service<a name="vpcep_06_0208"></a>

## Function<a name="section1446932"></a>

This API is used to query the whitelist records of a VPC endpoint service.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>Your domain ID is in the whitelist of your own VPC endpoint service by default.

## URI<a name="section13022395"></a>

GET /v1/\{project\_id\}/vpc-endpoint-services/\{vpc\_endpoint\_service\_id\}/permissions?sort\_dir=\{sort\_dir\}&limit=\{limit\}&offset=\{offset\}

[Table 1](#table26447764)  describes the required parameters.

**Table  1**  Parameters

<a name="table26447764"></a>
<table><thead align="left"><tr id="row61738601"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p34770760"><a name="p34770760"></a><a name="p34770760"></a><strong id="b2989112416347"><a name="b2989112416347"></a><a name="b2989112416347"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p64968164"><a name="p64968164"></a><a name="p64968164"></a><strong id="b3249162617346"><a name="b3249162617346"></a><a name="b3249162617346"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p27929892"><a name="p27929892"></a><a name="p27929892"></a><strong id="b11183162783419"><a name="b11183162783419"></a><a name="b11183162783419"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row47728752"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p40823729"><a name="p40823729"></a><a name="p40823729"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p18387791"><a name="p18387791"></a><a name="p18387791"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p13016113"><a name="p13016113"></a><a name="p13016113"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row50036160"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p26397123"><a name="p26397123"></a><a name="p26397123"></a>vpc_endpoint_service_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p57792256"><a name="p57792256"></a><a name="p57792256"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p50661149"><a name="p50661149"></a><a name="p50661149"></a>Specifies the ID of the VPC endpoint service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section50092695"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table61894122"></a>
    <table><thead align="left"><tr id="row39767838"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p67078348"><a name="p67078348"></a><a name="p67078348"></a><strong id="b18624194183415"><a name="b18624194183415"></a><a name="b18624194183415"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.2"><p id="p64637118"><a name="p64637118"></a><a name="p64637118"></a><strong id="b1543255479"><a name="b1543255479"></a><a name="b1543255479"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p1115229"><a name="p1115229"></a><a name="p1115229"></a><strong id="b14373215355"><a name="b14373215355"></a><a name="b14373215355"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p23224720"><a name="p23224720"></a><a name="p23224720"></a><strong id="b1785568989"><a name="b1785568989"></a><a name="b1785568989"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2154176"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p40270548"><a name="p40270548"></a><a name="p40270548"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p40688949"><a name="p40688949"></a><a name="p40688949"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p7470538"><a name="p7470538"></a><a name="p7470538"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1133819"><a name="p1133819"></a><a name="p1133819"></a>Specifies the maximum number of whitelist records displayed on each page.</p>
    <p id="p10204378"><a name="p10204378"></a><a name="p10204378"></a>The value ranges from <strong id="b1254717241318"><a name="b1254717241318"></a><a name="b1254717241318"></a>0</strong> to <strong id="b1354113691319"><a name="b1354113691319"></a><a name="b1354113691319"></a>500</strong> and is generally <strong id="b946715895412"><a name="b946715895412"></a><a name="b946715895412"></a>10</strong>,<strong id="b1847005835417"><a name="b1847005835417"></a><a name="b1847005835417"></a> 20</strong>, or <strong id="b2471115814546"><a name="b2471115814546"></a><a name="b2471115814546"></a>50</strong>. The default value is <strong id="b34732586549"><a name="b34732586549"></a><a name="b34732586549"></a>10</strong>.</p>
    </td>
    </tr>
    <tr id="row24730546"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p57017172"><a name="p57017172"></a><a name="p57017172"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p54988235"><a name="p54988235"></a><a name="p54988235"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p24862079"><a name="p24862079"></a><a name="p24862079"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p5736126132214"><a name="p5736126132214"></a><a name="p5736126132214"></a>Specifies the offset.</p>
    <p id="p11912494222"><a name="p11912494222"></a><a name="p11912494222"></a>All VPC endpoint services after this offset will be queried. The value must be an integer greater than 0 but less than the number of VPC endpoint services.</p>
    </td>
    </tr>
    <tr id="row66994296244"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p594733716244"><a name="p594733716244"></a><a name="p594733716244"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p129471037182413"><a name="p129471037182413"></a><a name="p129471037182413"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p119471937202418"><a name="p119471937202418"></a><a name="p119471937202418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p562418271823"><a name="p562418271823"></a><a name="p562418271823"></a>Specifies the sorting field of the whitelist record list. The value can be:</p>
    <a name="ul512472071414"></a><a name="ul512472071414"></a><ul id="ul512472071414"><li><strong id="b2811116368"><a name="b2811116368"></a><a name="b2811116368"></a>create_at</strong>: indicates the time of adding the whitelist record.</li><li><strong id="b2087421616363"><a name="b2087421616363"></a><a name="b2087421616363"></a>update_at</strong>: indicates the time of updating the whitelist record.</li></ul>
    <p id="p36041148141413"><a name="p36041148141413"></a><a name="p36041148141413"></a>The default value is <strong id="vpcep_06_0205_b84581912152219"><a name="vpcep_06_0205_b84581912152219"></a><a name="vpcep_06_0205_b84581912152219"></a>create_at</strong>.</p>
    </td>
    </tr>
    <tr id="row1253984418240"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p146661827153215"><a name="p146661827153215"></a><a name="p146661827153215"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.2 "><p id="p1666182717328"><a name="p1666182717328"></a><a name="p1666182717328"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p14666182718326"><a name="p14666182718326"></a><a name="p14666182718326"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1648594010189"><a name="p1648594010189"></a><a name="p1648594010189"></a>Specifies the sorting method of the whitelist record list. The value can be:</p>
    <a name="ul9628101291617"></a><a name="ul9628101291617"></a><ul id="ul9628101291617"><li><strong id="b39503129475"><a name="b39503129475"></a><a name="b39503129475"></a>desc</strong>: indicates that whitelist records are sorted in the descending order.</li><li><strong id="b82461415204717"><a name="b82461415204717"></a><a name="b82461415204717"></a>asc</strong>: indicates that whitelist records are sorted in the ascending order.</li></ul>
    <p id="p1719319255168"><a name="p1719319255168"></a><a name="p1719319255168"></a>The default value is <strong id="vpcep_06_0205_b84235270614202"><a name="vpcep_06_0205_b84235270614202"></a><a name="vpcep_06_0205_b84235270614202"></a>desc</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    This request is to query whitelist records of the VPC endpoint service whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed88**.

    ```
    GET https://{endpoint}/v1/{project_id}/vpc-endpoint-services/4189d3c2-8882-4871-a3c2-d380272eed88/permissions
    ```


## Response<a name="section30976474"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table20176194"></a>
    <table><thead align="left"><tr id="row11639215"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p3252353"><a name="p3252353"></a><a name="p3252353"></a><strong id="b1329792667"><a name="b1329792667"></a><a name="b1329792667"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p62114027"><a name="p62114027"></a><a name="p62114027"></a><strong id="b1094611042"><a name="b1094611042"></a><a name="b1094611042"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p65180310"><a name="p65180310"></a><a name="p65180310"></a><strong id="b1818730356"><a name="b1818730356"></a><a name="b1818730356"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45113770"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p30336717"><a name="p30336717"></a><a name="p30336717"></a>permissions</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p41355050"><a name="p41355050"></a><a name="p41355050"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p61424743"><a name="p61424743"></a><a name="p61424743"></a>Lists the whitelist records. For details, see <a href="#table50257079">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row15951777"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p17025554"><a name="p17025554"></a><a name="p17025554"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p36892599"><a name="p36892599"></a><a name="p36892599"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p35510520"><a name="p35510520"></a><a name="p35510520"></a>Specifies the total number of whitelist records that meet the search criteria. The number is not affected by the limit or offset.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Whitelist record parameters 

    <a name="table50257079"></a>
    <table><thead align="left"><tr id="row15696288"><th class="cellrowborder" valign="top" width="17.72%" id="mcps1.2.4.1.1"><p id="p63439817"><a name="p63439817"></a><a name="p63439817"></a><strong id="b114315252378"><a name="b114315252378"></a><a name="b114315252378"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.94%" id="mcps1.2.4.1.2"><p id="p38351587"><a name="p38351587"></a><a name="p38351587"></a><strong id="b270042550"><a name="b270042550"></a><a name="b270042550"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.339999999999996%" id="mcps1.2.4.1.3"><p id="p19470870"><a name="p19470870"></a><a name="p19470870"></a><strong id="b163363606"><a name="b163363606"></a><a name="b163363606"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33636617"><td class="cellrowborder" valign="top" width="17.72%" headers="mcps1.2.4.1.1 "><p id="p40211428"><a name="p40211428"></a><a name="p40211428"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.94%" headers="mcps1.2.4.1.2 "><p id="p35900240"><a name="p35900240"></a><a name="p35900240"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p22238324"><a name="p22238324"></a><a name="p22238324"></a>Specifies the unique ID of the permission.</p>
    </td>
    </tr>
    <tr id="row65927195"><td class="cellrowborder" valign="top" width="17.72%" headers="mcps1.2.4.1.1 "><p id="p38502599"><a name="p38502599"></a><a name="p38502599"></a>permission</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.94%" headers="mcps1.2.4.1.2 "><p id="p31702848"><a name="p31702848"></a><a name="p31702848"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p8301318441"><a name="p8301318441"></a><a name="p8301318441"></a>Lists the whitelist records.</p>
    <p id="p17793901"><a name="p17793901"></a><a name="p17793901"></a>The permission format is <strong id="b10288112415171"><a name="b10288112415171"></a><a name="b10288112415171"></a>iam:domain:: 6e9dfd51d1124e8d8498dce894923a0d</strong> or <strong id="b1728912421716"><a name="b1728912421716"></a><a name="b1728912421716"></a>*</strong>. <strong id="b4289142441711"><a name="b4289142441711"></a><a name="b4289142441711"></a>*</strong> indicates all users can connect to the VPC endpoint service. <strong id="b61191344184217"><a name="b61191344184217"></a><a name="b61191344184217"></a>6e9dfd51d1124e8d8498dce894923a0d</strong> indicates the domain ID of the user.</p>
    </td>
    </tr>
    <tr id="row25927387"><td class="cellrowborder" valign="top" width="17.72%" headers="mcps1.2.4.1.1 "><p id="p19743602"><a name="p19743602"></a><a name="p19743602"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.94%" headers="mcps1.2.4.1.2 "><p id="p55727921"><a name="p55727921"></a><a name="p55727921"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.339999999999996%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a><strong id="b5520114064017"><a name="b5520114064017"></a><a name="b5520114064017"></a>create_at</strong>: indicates the time of adding the whitelist record.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "permissions":
       [
              {
                    "id":"f2659906-c622-480a-83e9-ef42bdb67b90",
                    "permission":"*",
                    "created_at":"2018-10-18T13:26:40Z"
                }
        ],
     "total_count":1
    }
    ```


## Status Code<a name="section26066437"></a>

For details about status codes, see  [Status Code](status-code.md).

