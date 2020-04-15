# Allocating DeHs<a name="EN-US_TOPIC_0087389315"></a>

## Function<a name="section48259009"></a>

This API is used to allocate one or more DeHs and set required parameters, such as the flavor, AZ, and quantity.

## Constraints<a name="section16665627"></a>

The number of allocatable DeHs depends on the DeH quota owned by the tenant.

## URI<a name="section31677898"></a>

POST /v1.0/\{project\_id\}/dedicated-hosts

[Table 1](#table572214121015)  describes the parameters.

**Table  1**  Parameters description

<a name="table572214121015"></a>
<table><thead align="left"><tr id="row572516410109"><th class="cellrowborder" valign="top" width="21.23787621237876%" id="mcps1.2.5.1.1"><p id="p107252049107"><a name="p107252049107"></a><a name="p107252049107"></a><strong id="b1679518201213"><a name="b1679518201213"></a><a name="b1679518201213"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.5.1.2"><p id="p726975522919"><a name="p726975522919"></a><a name="p726975522919"></a><strong id="b161650227212"><a name="b161650227212"></a><a name="b161650227212"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.48755124487551%" id="mcps1.2.5.1.3"><p id="p072564201017"><a name="p072564201017"></a><a name="p072564201017"></a><strong id="b252042320216"><a name="b252042320216"></a><a name="b252042320216"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p47253421017"><a name="p47253421017"></a><a name="p47253421017"></a><strong id="b208241224223"><a name="b208241224223"></a><a name="b208241224223"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row107256481017"><td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.1 "><p id="p1872514451016"><a name="p1872514451016"></a><a name="p1872514451016"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.5.1.2 "><p id="p12269175511291"><a name="p12269175511291"></a><a name="p12269175511291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.3 "><p id="p147251646108"><a name="p147251646108"></a><a name="p147251646108"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p6725747104"><a name="p6725747104"></a><a name="p6725747104"></a>Specifies the project ID.</p>
<p id="p13397185821014"><a name="p13397185821014"></a><a name="p13397185821014"></a>For details about how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section15772917"></a>

-   Request parameters

    <a name="table64696659"></a>
    <table><thead align="left"><tr id="row27762102"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.6.1.1"><p id="p1559348151811"><a name="p1559348151811"></a><a name="p1559348151811"></a><strong id="b162766431724"><a name="b162766431724"></a><a name="b162766431724"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.31%" id="mcps1.1.6.1.2"><p id="p8560184813187"><a name="p8560184813187"></a><a name="p8560184813187"></a><strong id="b56202615314"><a name="b56202615314"></a><a name="b56202615314"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.25%" id="mcps1.1.6.1.3"><p id="p20561184820185"><a name="p20561184820185"></a><a name="p20561184820185"></a><strong id="b1782741637"><a name="b1782741637"></a><a name="b1782741637"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.93%" id="mcps1.1.6.1.4"><p id="p3563104819181"><a name="p3563104819181"></a><a name="p3563104819181"></a><strong id="b97370101836"><a name="b97370101836"></a><a name="b97370101836"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.51%" id="mcps1.1.6.1.5"><p id="p556424815182"><a name="p556424815182"></a><a name="p556424815182"></a><strong id="b16898711036"><a name="b16898711036"></a><a name="b16898711036"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13977142"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.1 "><p id="p58406714"><a name="p58406714"></a><a name="p58406714"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.31%" headers="mcps1.1.6.1.2 "><p id="p33323423"><a name="p33323423"></a><a name="p33323423"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.25%" headers="mcps1.1.6.1.3 "><p id="p14842765"><a name="p14842765"></a><a name="p14842765"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.1.6.1.4 "><p id="p61413291"><a name="p61413291"></a><a name="p61413291"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.51%" headers="mcps1.1.6.1.5 "><p id="p8420641"><a name="p8420641"></a><a name="p8420641"></a>Specifies the DeH name.</p>
    </td>
    </tr>
    <tr id="row8676909"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.1 "><p id="p31741019"><a name="p31741019"></a><a name="p31741019"></a>auto_placement</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.31%" headers="mcps1.1.6.1.2 "><p id="p20885750"><a name="p20885750"></a><a name="p20885750"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.25%" headers="mcps1.1.6.1.3 "><p id="p14024165"><a name="p14024165"></a><a name="p14024165"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.1.6.1.4 "><p id="p62215569"><a name="p62215569"></a><a name="p62215569"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.51%" headers="mcps1.1.6.1.5 "><p id="OLE_LINK105"><a name="OLE_LINK105"></a><a name="OLE_LINK105"></a>Specifies whether to allow an ECS to be placed on any available DeH if its DeH ID is not specified during its creation.</p>
    <p id="p56666602"><a name="p56666602"></a><a name="p56666602"></a>The value can be <strong id="b1472295311720"><a name="b1472295311720"></a><a name="b1472295311720"></a>on</strong> or <strong id="b11733175681720"><a name="b11733175681720"></a><a name="b11733175681720"></a>off</strong>.</p>
    <p id="p1193901932917"><a name="p1193901932917"></a><a name="p1193901932917"></a>The default value is <strong id="b188181091818"><a name="b188181091818"></a><a name="b188181091818"></a>on</strong>.</p>
    </td>
    </tr>
    <tr id="row58247484"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.1 "><p id="p20425774"><a name="p20425774"></a><a name="p20425774"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.31%" headers="mcps1.1.6.1.2 "><p id="p43875021"><a name="p43875021"></a><a name="p43875021"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.25%" headers="mcps1.1.6.1.3 "><p id="p64215808"><a name="p64215808"></a><a name="p64215808"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.1.6.1.4 "><p id="p34097968"><a name="p34097968"></a><a name="p34097968"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.51%" headers="mcps1.1.6.1.5 "><p id="p10472004"><a name="p10472004"></a><a name="p10472004"></a>Specifies the AZ to which the DeH belongs.</p>
    </td>
    </tr>
    <tr id="row27139175"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.1 "><p id="p50789581"><a name="p50789581"></a><a name="p50789581"></a>host_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.31%" headers="mcps1.1.6.1.2 "><p id="p20315403"><a name="p20315403"></a><a name="p20315403"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.25%" headers="mcps1.1.6.1.3 "><p id="p34934986"><a name="p34934986"></a><a name="p34934986"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.1.6.1.4 "><p id="p11161650"><a name="p11161650"></a><a name="p11161650"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.51%" headers="mcps1.1.6.1.5 "><p id="p31678442"><a name="p31678442"></a><a name="p31678442"></a>Specifies the DeH type.</p>
    </td>
    </tr>
    <tr id="row16670523"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.1 "><p id="p8135151"><a name="p8135151"></a><a name="p8135151"></a>quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.31%" headers="mcps1.1.6.1.2 "><p id="p54967495"><a name="p54967495"></a><a name="p54967495"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.25%" headers="mcps1.1.6.1.3 "><p id="p23182124"><a name="p23182124"></a><a name="p23182124"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.1.6.1.4 "><p id="p65812741"><a name="p65812741"></a><a name="p65812741"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.51%" headers="mcps1.1.6.1.5 "><p id="p29231803"><a name="p29231803"></a><a name="p29231803"></a>Specifies the number of allocatable DeHs.</p>
    </td>
    </tr>
    <tr id="row05351151181518"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.6.1.1 "><p id="p2537115171515"><a name="p2537115171515"></a><a name="p2537115171515"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.31%" headers="mcps1.1.6.1.2 "><p id="p1553717518159"><a name="p1553717518159"></a><a name="p1553717518159"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.25%" headers="mcps1.1.6.1.3 "><p id="p95371151151520"><a name="p95371151151520"></a><a name="p95371151151520"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.1.6.1.4 "><p id="p1353716514155"><a name="p1353716514155"></a><a name="p1353716514155"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.51%" headers="mcps1.1.6.1.5 "><p id="p853725121512"><a name="p853725121512"></a><a name="p853725121512"></a>Specifies the DeH tags.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **resource\_tag**  field description

    <a name="table1291492117268"></a>
    <table><thead align="left"><tr id="row17915421152613"><th class="cellrowborder" valign="top" width="16.731673167316732%" id="mcps1.1.5.1.1"><p id="p88171201349"><a name="p88171201349"></a><a name="p88171201349"></a><strong id="b36711287344"><a name="b36711287344"></a><a name="b36711287344"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.31163116311631%" id="mcps1.1.5.1.2"><p id="p198191902346"><a name="p198191902346"></a><a name="p198191902346"></a><strong id="b87133010341"><a name="b87133010341"></a><a name="b87133010341"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.72177217721772%" id="mcps1.1.5.1.3"><p id="p118191013413"><a name="p118191013413"></a><a name="p118191013413"></a><strong id="b1030273133412"><a name="b1030273133412"></a><a name="b1030273133412"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.23492349234924%" id="mcps1.1.5.1.4"><p id="p1582070173413"><a name="p1582070173413"></a><a name="p1582070173413"></a><strong id="b643313283410"><a name="b643313283410"></a><a name="b643313283410"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20915132182619"><td class="cellrowborder" valign="top" width="16.731673167316732%" headers="mcps1.1.5.1.1 "><p id="p1079518715372"><a name="p1079518715372"></a><a name="p1079518715372"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.31163116311631%" headers="mcps1.1.5.1.2 "><p id="p1798167163710"><a name="p1798167163710"></a><a name="p1798167163710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.72177217721772%" headers="mcps1.1.5.1.3 "><p id="p1143462293118"><a name="p1143462293118"></a><a name="p1143462293118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.23492349234924%" headers="mcps1.1.5.1.4 "><p id="p187993733712"><a name="p187993733712"></a><a name="p187993733712"></a>Specifies the tag key.</p>
    <a name="ul85106389279"></a><a name="ul85106389279"></a><ul id="ul85106389279"><li>It contains a maximum of 36 Unicode characters.</li><li>The value cannot be empty.</li><li>It cannot contain the following ASCII characters: =*&lt;&gt;\|/,</li><li>It can contain letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    </tr>
    <tr id="row13915421202616"><td class="cellrowborder" valign="top" width="16.731673167316732%" headers="mcps1.1.5.1.1 "><p id="p180118718372"><a name="p180118718372"></a><a name="p180118718372"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.31163116311631%" headers="mcps1.1.5.1.2 "><p id="p280411723712"><a name="p280411723712"></a><a name="p280411723712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.72177217721772%" headers="mcps1.1.5.1.3 "><p id="p7435142215318"><a name="p7435142215318"></a><a name="p7435142215318"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.23492349234924%" headers="mcps1.1.5.1.4 "><p id="p1480513718375"><a name="p1480513718375"></a><a name="p1480513718375"></a>Specifies the tag value.</p>
    <a name="ul198416113281"></a><a name="ul198416113281"></a><ul id="ul198416113281"><li>It contains a maximum of 43 Unicode characters.</li><li>It cannot contain the following ASCII characters: =*&lt;&gt;\|/,</li><li>It can contain letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-hosts
    {
         "availability_zone": "dc1.az1",
         "name": "high performance servers1",
         "auto_placement": "off",
         "host_type": "h1",
         "quantity": 2,
         "tags": [
             {
                 "key": "key1",
                 "value": "value1"
             }
         ] 
    }
    ```


## Response<a name="section7738529"></a>

-   Response parameters

    <a name="table36474591"></a>
    <table><thead align="left"><tr id="row36048322"><th class="cellrowborder" valign="top" width="20.69%" id="mcps1.1.5.1.1"><p id="p32701116171216"><a name="p32701116171216"></a><a name="p32701116171216"></a><strong id="b1320112413441"><a name="b1320112413441"></a><a name="b1320112413441"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.24%" id="mcps1.1.5.1.2"><p id="p427521616123"><a name="p427521616123"></a><a name="p427521616123"></a><strong id="b191591965441"><a name="b191591965441"></a><a name="b191591965441"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.24%" id="mcps1.1.5.1.3"><p id="p62781016171210"><a name="p62781016171210"></a><a name="p62781016171210"></a><strong id="b96422724414"><a name="b96422724414"></a><a name="b96422724414"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.83%" id="mcps1.1.5.1.4"><p id="p1228181618125"><a name="p1228181618125"></a><a name="p1228181618125"></a><strong id="b811310913440"><a name="b811310913440"></a><a name="b811310913440"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1482002"><td class="cellrowborder" valign="top" width="20.69%" headers="mcps1.1.5.1.1 "><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a>dedicated_host_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.1.5.1.2 "><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.1.5.1.3 "><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.83%" headers="mcps1.1.5.1.4 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>Specifies a group of IDs of allocated DeHs. The tenant can create ECSs on these DeHs.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "dedicated_host_ids": ["xxxxxxx1","xxxxxxx2"]
    }
    ```


## Status Code<a name="section4243749"></a>

<a name="table32922799"></a>
<table><thead align="left"><tr id="row48838504"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p63604780"><a name="p63604780"></a><a name="p63604780"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p51713556"><a name="p51713556"></a><a name="p51713556"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62768825"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p51110099"><a name="p51110099"></a><a name="p51110099"></a>403 Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><a name="ol46277382"></a><a name="ol46277382"></a><ol id="ol46277382"><li>Insufficient quota.</li><li>The flavor is not supported.</li></ol>
</td>
</tr>
<tr id="row47561922"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p27310456"><a name="p27310456"></a><a name="p27310456"></a>404 FlavorNotFound</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p64663364"><a name="p64663364"></a><a name="p64663364"></a>Invalid flavor.</p>
</td>
</tr>
</tbody>
</table>

For more status codes, see  [Status Codes](status-codes.md).

