# Querying Details About All Disks<a name="evs_04_2069"></a>

## Function<a name="section60214390"></a>

This API is used to query details about all disks.

## URI<a name="section5058598"></a>

-   URI format

    GET /v2/\{project\_id\}/volumes/detail

-   Parameter description

    <a name="table58294385"></a>
    <table><thead align="left"><tr id="row24683273"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p53188122"><a name="p53188122"></a><a name="p53188122"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p13270664"><a name="p13270664"></a><a name="p13270664"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1182010"><a name="p1182010"></a><a name="p1182010"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28634009"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p37653388"><a name="p37653388"></a><a name="p37653388"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p30025596"><a name="p30025596"></a><a name="p30025596"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p16154192"><a name="p16154192"></a><a name="p16154192"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request filter parameters

    <a name="table4291376694520"></a>
    <table><thead align="left"><tr id="row75210794520"><th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.1"><p id="p6092069194520"><a name="p6092069194520"></a><a name="p6092069194520"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85%" id="mcps1.1.5.1.2"><p id="p3562891594520"><a name="p3562891594520"></a><a name="p3562891594520"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.1.5.1.3"><p id="p26101294520"><a name="p26101294520"></a><a name="p26101294520"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.63%" id="mcps1.1.5.1.4"><p id="p2114201394520"><a name="p2114201394520"></a><a name="p2114201394520"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3478152794520"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p60095082153718"><a name="p60095082153718"></a><a name="p60095082153718"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p35863456153718"><a name="p35863456153718"></a><a name="p35863456153718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p19258860153718"><a name="p19258860153718"></a><a name="p19258860153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p16463795153718"><a name="p16463795153718"></a><a name="p16463795153718"></a><span id="text1666413213419"><a name="text1666413213419"></a><a name="text1666413213419"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="row2183600894520"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p56729311153718"><a name="p56729311153718"></a><a name="p56729311153718"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p38113769154021"><a name="p38113769154021"></a><a name="p38113769154021"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p15250867153718"><a name="p15250867153718"></a><a name="p15250867153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p27360714153718"><a name="p27360714153718"></a><a name="p27360714153718"></a>Specifies the disk name. <span id="text557493116201645"><a name="text557493116201645"></a><a name="text557493116201645"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row4640654394520"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p14628184153718"><a name="p14628184153718"></a><a name="p14628184153718"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p44032231153718"><a name="p44032231153718"></a><a name="p44032231153718"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p9840947153718"><a name="p9840947153718"></a><a name="p9840947153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p58919203153718"><a name="p58919203153718"></a><a name="p58919203153718"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p1412911417152"><a name="p1412911417152"></a><a name="p1412911417152"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    <p id="p14657115572511"><a name="p14657115572511"></a><a name="p14657115572511"></a>If the tenant has more than 50 disks in total, you are advised to use this parameter and set its value to <strong id="b8423527069161"><a name="b8423527069161"></a><a name="b8423527069161"></a>50</strong> to improve the query efficiency. Examples are provided as follows:</p>
    <p id="p1233994321914"><a name="p1233994321914"></a><a name="p1233994321914"></a><strong id="b320873402103755"><a name="b320873402103755"></a><a name="b320873402103755"></a>GET /v2/</strong><em id="i1514898224103755"><a name="i1514898224103755"></a><a name="i1514898224103755"></a>xxx</em><strong id="b738773580103755"><a name="b738773580103755"></a><a name="b738773580103755"></a>/volumes/detail?limit=50</strong>: Queries the 1–50 disks. <strong id="b842352706103810"><a name="b842352706103810"></a><a name="b842352706103810"></a>GET /v2/</strong><em id="i197699858310388"><a name="i197699858310388"></a><a name="i197699858310388"></a>xxx</em><strong id="b842352706103816"><a name="b842352706103816"></a><a name="b842352706103816"></a>/volumes/detail?offset=50&amp;limit=50</strong>: Queries the 51–100 disks.</p>
    </td>
    </tr>
    <tr id="row6054321594520"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p2426142153718"><a name="p2426142153718"></a><a name="p2426142153718"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p43526083154024"><a name="p43526083154024"></a><a name="p43526083154024"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p13119059153718"><a name="p13119059153718"></a><a name="p13119059153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p56010871153718"><a name="p56010871153718"></a><a name="p56010871153718"></a>Specifies the keyword based on which the returned results are sorted. The value can be <strong id="b1323065485511"><a name="b1323065485511"></a><a name="b1323065485511"></a>id</strong>, <strong id="b1723118546555"><a name="b1723118546555"></a><a name="b1723118546555"></a>status</strong>, <strong id="b1523165419550"><a name="b1523165419550"></a><a name="b1523165419550"></a>size</strong>, or <strong id="b5232155414552"><a name="b5232155414552"></a><a name="b5232155414552"></a>created_at</strong>, and the default value is <strong id="b1823295495513"><a name="b1823295495513"></a><a name="b1823295495513"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row5521380794520"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p29735682153718"><a name="p29735682153718"></a><a name="p29735682153718"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p16700889154026"><a name="p16700889154026"></a><a name="p16700889154026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p10345862153718"><a name="p10345862153718"></a><a name="p10345862153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><div class="p" id="p62620581361"><a name="p62620581361"></a><a name="p62620581361"></a>Specifies the result sorting order. The default value is <strong id="b596612596554"><a name="b596612596554"></a><a name="b596612596554"></a>desc</strong>.<a name="ul022952573"></a><a name="ul022952573"></a><ul id="ul022952573"><li><strong id="b149057020567"><a name="b149057020567"></a><a name="b149057020567"></a>desc</strong>: indicates the descending order.</li><li><strong id="b57865275610"><a name="b57865275610"></a><a name="b57865275610"></a>asc</strong>: indicates the ascending order.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row49871977153626"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p20840349153718"><a name="p20840349153718"></a><a name="p20840349153718"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p10346748153718"><a name="p10346748153718"></a><a name="p10346748153718"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p32780292153718"><a name="p32780292153718"></a><a name="p32780292153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p98722321465"><a name="p98722321465"></a><a name="p98722321465"></a>Specifies the offset.</p>
    <p id="p37957980153718"><a name="p37957980153718"></a><a name="p37957980153718"></a>All disks after this offset will be queried. The value must be an integer greater than 0 but less than the number of disks.</p>
    </td>
    </tr>
    <tr id="row2837320153624"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p22515601153718"><a name="p22515601153718"></a><a name="p22515601153718"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p53812252154029"><a name="p53812252154029"></a><a name="p53812252154029"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p18251790153718"><a name="p18251790153718"></a><a name="p18251790153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p2000007153718"><a name="p2000007153718"></a><a name="p2000007153718"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row34125704153621"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p48719302153718"><a name="p48719302153718"></a><a name="p48719302153718"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p31082833154032"><a name="p31082833154032"></a><a name="p31082833154032"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p7822125153718"><a name="p7822125153718"></a><a name="p7822125153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p29612385153718"><a name="p29612385153718"></a><a name="p29612385153718"></a>Specifies the disk metadata.</p>
    </td>
    </tr>
    <tr id="row61070326153619"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p45483948153718"><a name="p45483948153718"></a><a name="p45483948153718"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.2 "><p id="p23816783154035"><a name="p23816783154035"></a><a name="p23816783154035"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p54179442153718"><a name="p54179442153718"></a><a name="p54179442153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p26458700153718"><a name="p26458700153718"></a><a name="p26458700153718"></a>Specifies the AZ.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query details of the disks in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/volumes/detail?status=available
    ```


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="table682710305552"></a>
    <table><thead align="left"><tr id="row18828730125511"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p17828103014554"><a name="p17828103014554"></a><a name="p17828103014554"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p982813025513"><a name="p982813025513"></a><a name="p982813025513"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p10828123085512"><a name="p10828123085512"></a><a name="p10828123085512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6828153014554"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p1828130105513"><a name="p1828130105513"></a><a name="p1828130105513"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p582813013559"><a name="p582813013559"></a><a name="p582813013559"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p158281930195514"><a name="p158281930195514"></a><a name="p158281930195514"></a>Specifies the list of queried disks. For details, see <a href="#li3451542201439">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="row16651711135716"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p20139619153059"><a name="p20139619153059"></a><a name="p20139619153059"></a>volumes_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p20696419153059"><a name="p20696419153059"></a><a name="p20696419153059"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p27977197153059"><a name="p27977197153059"></a><a name="p27977197153059"></a>Specifies the query position marker in the disk list. If only some disks are returned in this query, the URL of the last disk queried will be returned. You can use this URL to continue to query the remaining disks in the next query. For details, see <a href="#li851885019247">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row1383518379555"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li3451542201439"></a>Parameters in the  **volumes**  field

    <a name="table34701445142557"></a>
    <table><thead align="left"><tr id="row12524911142557"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p7884856142557"><a name="p7884856142557"></a><a name="p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="p34693598142557"><a name="p34693598142557"></a><a name="p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p58539486142557"><a name="p58539486142557"></a><a name="p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row444782011610"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p54175786153922"><a name="p54175786153922"></a><a name="p54175786153922"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p26162565153922"><a name="p26162565153922"></a><a name="p26162565153922"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p55227932153922"><a name="p55227932153922"></a><a name="p55227932153922"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row44077962142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p62953588153922"><a name="p62953588153922"></a><a name="p62953588153922"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p494261191750"><a name="p494261191750"></a><a name="p494261191750"></a>list&lt;map&lt;String,String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p379966153922"><a name="p379966153922"></a><a name="p379966153922"></a>Specifies the disk URI. For details, see <a href="#li851885019247">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row16186817142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p8559918153922"><a name="p8559918153922"></a><a name="p8559918153922"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p38279089154138"><a name="p38279089154138"></a><a name="p38279089154138"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p50401086153922"><a name="p50401086153922"></a><a name="p50401086153922"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="row45785905142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p33843531153922"><a name="p33843531153922"></a><a name="p33843531153922"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p15510513154140"><a name="p15510513154140"></a><a name="p15510513154140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p60776191153922"><a name="p60776191153922"></a><a name="p60776191153922"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row35247553142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p13993091153922"><a name="p13993091153922"></a><a name="p13993091153922"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p59698591153922"><a name="p59698591153922"></a><a name="p59698591153922"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p35128232153922"><a name="p35128232153922"></a><a name="p35128232153922"></a>Specifies the disk attachment information. For details, see <a href="#li5001921919316">Parameters in the attachments field</a>.</p>
    </td>
    </tr>
    <tr id="row27126244142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p40004503153922"><a name="p40004503153922"></a><a name="p40004503153922"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p51760296154143"><a name="p51760296154143"></a><a name="p51760296154143"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p12372460153922"><a name="p12372460153922"></a><a name="p12372460153922"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="row7009490142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p26935952153922"><a name="p26935952153922"></a><a name="p26935952153922"></a>os-vol-host-attr:host</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p61285780154145"><a name="p61285780154145"></a><a name="p61285780154145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p12079427153922"><a name="p12079427153922"></a><a name="p12079427153922"></a><span id="text657995710581"><a name="text657995710581"></a><a name="text657995710581"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row49237196142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p14641407153922"><a name="p14641407153922"></a><a name="p14641407153922"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p15993974154147"><a name="p15993974154147"></a><a name="p15993974154147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p40148014153922"><a name="p40148014153922"></a><a name="p40148014153922"></a>Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.</p>
    <p id="p1587817436328"><a name="p1587817436328"></a><a name="p1587817436328"></a><span id="text18357144552617"><a name="text18357144552617"></a><a name="text18357144552617"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row39017307142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p8437822153922"><a name="p8437822153922"></a><a name="p8437822153922"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p43970411154151"><a name="p43970411154151"></a><a name="p43970411154151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p57569910153922"><a name="p57569910153922"></a><a name="p57569910153922"></a>Specifies the snapshot ID. This parameter has a value if the disk is created from a snapshot.</p>
    </td>
    </tr>
    <tr id="row20107664142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p25424812153922"><a name="p25424812153922"></a><a name="p25424812153922"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p16247974154153"><a name="p16247974154153"></a><a name="p16247974154153"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p22193516153922"><a name="p22193516153922"></a><a name="p22193516153922"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="row12897861142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p5837556153922"><a name="p5837556153922"></a><a name="p5837556153922"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p30798966154156"><a name="p30798966154156"></a><a name="p30798966154156"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p8308266153922"><a name="p8308266153922"></a><a name="p8308266153922"></a>Specifies the time when the disk was created.</p>
    <p id="p15772145473814"><a name="p15772145473814"></a><a name="p15772145473814"></a><span id="text151181202390"><a name="text151181202390"></a><a name="text151181202390"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row45680217142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p16928326153922"><a name="p16928326153922"></a><a name="p16928326153922"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p35495495154158"><a name="p35495495154158"></a><a name="p35495495154158"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p60775887153922"><a name="p60775887153922"></a><a name="p60775887153922"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="row47480567142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p13771931153922"><a name="p13771931153922"></a><a name="p13771931153922"></a>os-vol-tenant-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p4873995415420"><a name="p4873995415420"></a><a name="p4873995415420"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p9058246153922"><a name="p9058246153922"></a><a name="p9058246153922"></a>Specifies the ID of the tenant to which the disk belongs. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="row31517135142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p26792948153922"><a name="p26792948153922"></a><a name="p26792948153922"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p22745155153922"><a name="p22745155153922"></a><a name="p22745155153922"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p47959551153922"><a name="p47959551153922"></a><a name="p47959551153922"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="row15610713142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p65903514153922"><a name="p65903514153922"></a><a name="p65903514153922"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p36584404153922"><a name="p36584404153922"></a><a name="p36584404153922"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p63055822144653"><a name="p63055822144653"></a><a name="p63055822144653"></a>Specifies the disk metadata. For details, see <a href="#li29114110314">Parameters in the metadata field</a>.</p>
    <p id="p1210013914474"><a name="p1210013914474"></a><a name="p1210013914474"></a>If <strong id="evs_04_2005_b842352706182520"><a name="evs_04_2005_b842352706182520"></a><a name="evs_04_2005_b842352706182520"></a>metadata</strong> does not contain the <strong id="evs_04_2005_b842352706143434"><a name="evs_04_2005_b842352706143434"></a><a name="evs_04_2005_b842352706143434"></a>hw:passthrough</strong> field, the disk device type is VBD.</p>
    <p id="p3812802015506"><a name="p3812802015506"></a><a name="p3812802015506"></a>If <strong id="evs_04_2005_b842352706182629"><a name="evs_04_2005_b842352706182629"></a><a name="evs_04_2005_b842352706182629"></a>metadata</strong> does not contain the <strong id="evs_04_2005_b842352706143455"><a name="evs_04_2005_b842352706143455"></a><a name="evs_04_2005_b842352706143455"></a>__system__encrypted</strong> field, the disk is not encrypted.</p>
    </td>
    </tr>
    <tr id="row5657368142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p5824606153922"><a name="p5824606153922"></a><a name="p5824606153922"></a>os-vol-mig-status-attr:migstat</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p28057958154213"><a name="p28057958154213"></a><a name="p28057958154213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p38401827153922"><a name="p38401827153922"></a><a name="p38401827153922"></a><span id="text7576132237"><a name="text7576132237"></a><a name="text7576132237"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row42462677142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p10535641153922"><a name="p10535641153922"></a><a name="p10535641153922"></a>os-vol-mig-status-attr:name_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p41814751154216"><a name="p41814751154216"></a><a name="p41814751154216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p45371608153922"><a name="p45371608153922"></a><a name="p45371608153922"></a><span id="text203605127103"><a name="text203605127103"></a><a name="text203605127103"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row35655683142957"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p42283458153922"><a name="p42283458153922"></a><a name="p42283458153922"></a>os-volume-replication:extended_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p9813320154224"><a name="p9813320154224"></a><a name="p9813320154224"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p28603805153922"><a name="p28603805153922"></a><a name="p28603805153922"></a><span id="text379518478151"><a name="text379518478151"></a><a name="text379518478151"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row57913155185111"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p47452553185118"><a name="p47452553185118"></a><a name="p47452553185118"></a>encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p18451581185118"><a name="p18451581185118"></a><a name="p18451581185118"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p27951625185124"><a name="p27951625185124"></a><a name="p27951625185124"></a><span id="text1610112322316"><a name="text1610112322316"></a><a name="text1610112322316"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row6226231314391"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p50459706153922"><a name="p50459706153922"></a><a name="p50459706153922"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p43392623154228"><a name="p43392623154228"></a><a name="p43392623154228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p57639660153922"><a name="p57639660153922"></a><a name="p57639660153922"></a><span id="text13830109172317"><a name="text13830109172317"></a><a name="text13830109172317"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row1430942214399"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p9163288153922"><a name="p9163288153922"></a><a name="p9163288153922"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p28184221154230"><a name="p28184221154230"></a><a name="p28184221154230"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p16698134793611"><a name="p16698134793611"></a><a name="p16698134793611"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="row1801485814395"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p13972139153922"><a name="p13972139153922"></a><a name="p13972139153922"></a>consistencygroup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p60028304154232"><a name="p60028304154232"></a><a name="p60028304154232"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p40663722153922"><a name="p40663722153922"></a><a name="p40663722153922"></a>Specifies the ID of the consistency group where the disk belongs.</p>
    <p id="p1890419561322"><a name="p1890419561322"></a><a name="p1890419561322"></a><span id="text16334171582811"><a name="text16334171582811"></a><a name="text16334171582811"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row53974058144326"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p48844805153922"><a name="p48844805153922"></a><a name="p48844805153922"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p26156143154240"><a name="p26156143154240"></a><a name="p26156143154240"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p8780414125315"><a name="en-us_topic_0098680634_p8780414125315"></a><a name="en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="ul185931714111"></a><a name="ul185931714111"></a><ul id="ul185931714111"><li><strong id="b1758062272117"><a name="b1758062272117"></a><a name="b1758062272117"></a>true</strong>: specifies a bootable disk.</li><li><strong id="b037922312116"><a name="b037922312116"></a><a name="b037922312116"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row46340323144336"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p57039357153922"><a name="p57039357153922"></a><a name="p57039357153922"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p51292786154244"><a name="p51292786154244"></a><a name="p51292786154244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p46488385153922"><a name="p46488385153922"></a><a name="p46488385153922"></a>Specifies the time when the disk was updated.</p>
    <p id="p14195114017102"><a name="p14195114017102"></a><a name="p14195114017102"></a><span id="text8196154011011"><a name="text8196154011011"></a><a name="text8196154011011"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row36758187144417"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p56950153922"><a name="p56950153922"></a><a name="p56950153922"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p4612960153922"><a name="p4612960153922"></a><a name="p4612960153922"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p66643618153922"><a name="p66643618153922"></a><a name="p66643618153922"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="note3800959821323"><a name="note3800959821323"></a><a name="note3800959821323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p45212589213213"><a name="p45212589213213"></a><a name="p45212589213213"></a>This field is no longer used. Use <strong id="b84235270610834"><a name="b84235270610834"></a><a name="b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row4658776614505"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p63488919153922"><a name="p63488919153922"></a><a name="p63488919153922"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p42328837153922"><a name="p42328837153922"></a><a name="p42328837153922"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p4781191416535"><a name="en-us_topic_0098680634_p4781191416535"></a><a name="en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="ul161621719119"></a><a name="ul161621719119"></a><ul id="ul161621719119"><li><strong id="b1152162642119"><a name="b1152162642119"></a><a name="b1152162642119"></a>true</strong>: specifies a shared disk.</li><li><strong id="b1967128122110"><a name="b1967128122110"></a><a name="b1967128122110"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row29234512142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p5432339153922"><a name="p5432339153922"></a><a name="p5432339153922"></a>volume_image_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p37366318153922"><a name="p37366318153922"></a><a name="p37366318153922"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p11733449153922"><a name="p11733449153922"></a><a name="p11733449153922"></a>Specifies whether the disk is created from an image. This field has a value if the disk is created from an image. Otherwise, it is left empty.</p>
    <div class="note" id="note13108526174911"><a name="note13108526174911"></a><a name="note13108526174911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2009_p1888154732118"><a name="evs_04_2009_p1888154732118"></a><a name="evs_04_2009_p1888154732118"></a>For details about <strong id="evs_04_2009_b664802919300"><a name="evs_04_2009_b664802919300"></a><a name="evs_04_2009_b664802919300"></a>volume_image_metadata</strong>, see <strong id="evs_04_2009_b0649629203016"><a name="evs_04_2009_b0649629203016"></a><a name="evs_04_2009_b0649629203016"></a>Querying Image Details</strong> in the <em id="evs_04_2009_i186501329183018"><a name="evs_04_2009_i186501329183018"></a><a name="evs_04_2009_i186501329183018"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li851885019247"></a>Parameters in the  **links**  field

    <a name="evs_04_2067_table24355024185927"></a>
    <table><thead align="left"><tr id="evs_04_2067_row16225418185927"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_2067_p39190461185927"><a name="evs_04_2067_p39190461185927"></a><a name="evs_04_2067_p39190461185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2067_p20310744185927"><a name="evs_04_2067_p20310744185927"></a><a name="evs_04_2067_p20310744185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="evs_04_2067_p47699944185927"><a name="evs_04_2067_p47699944185927"></a><a name="evs_04_2067_p47699944185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2067_row38490285185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p30705403185927"><a name="evs_04_2067_p30705403185927"></a><a name="evs_04_2067_p30705403185927"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p4109689185927"><a name="evs_04_2067_p4109689185927"></a><a name="evs_04_2067_p4109689185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p53015590185927"><a name="evs_04_2067_p53015590185927"></a><a name="evs_04_2067_p53015590185927"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row7378265185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p60768596185927"><a name="evs_04_2067_p60768596185927"></a><a name="evs_04_2067_p60768596185927"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p23309219185927"><a name="evs_04_2067_p23309219185927"></a><a name="evs_04_2067_p23309219185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p57795935185927"><a name="evs_04_2067_p57795935185927"></a><a name="evs_04_2067_p57795935185927"></a>Specifies the shortcut link marker name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li5001921919316"></a>Parameters in the  **attachments**  field

    <a name="evs_04_2067_table6503386185927"></a>
    <table><thead align="left"><tr id="evs_04_2067_row1296819185927"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="evs_04_2067_p37933504185927"><a name="evs_04_2067_p37933504185927"></a><a name="evs_04_2067_p37933504185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="evs_04_2067_p52714965185927"><a name="evs_04_2067_p52714965185927"></a><a name="evs_04_2067_p52714965185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="evs_04_2067_p50913593185927"><a name="evs_04_2067_p50913593185927"></a><a name="evs_04_2067_p50913593185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2067_row30360408185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p43274016185927"><a name="evs_04_2067_p43274016185927"></a><a name="evs_04_2067_p43274016185927"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p15534392185927"><a name="evs_04_2067_p15534392185927"></a><a name="evs_04_2067_p15534392185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p49891705185927"><a name="evs_04_2067_p49891705185927"></a><a name="evs_04_2067_p49891705185927"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row49550172185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p54141023185927"><a name="evs_04_2067_p54141023185927"></a><a name="evs_04_2067_p54141023185927"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p23346722185927"><a name="evs_04_2067_p23346722185927"></a><a name="evs_04_2067_p23346722185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p35416329185927"><a name="evs_04_2067_p35416329185927"></a><a name="evs_04_2067_p35416329185927"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row35650386185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p2000176185927"><a name="evs_04_2067_p2000176185927"></a><a name="evs_04_2067_p2000176185927"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p27796542185927"><a name="evs_04_2067_p27796542185927"></a><a name="evs_04_2067_p27796542185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p38329099185927"><a name="evs_04_2067_p38329099185927"></a><a name="evs_04_2067_p38329099185927"></a>Specifies the time when the disk was attached.</p>
    <p id="evs_04_2067_p3414132514312"><a name="evs_04_2067_p3414132514312"></a><a name="evs_04_2067_p3414132514312"></a><span id="evs_04_2067_text7299269449"><a name="evs_04_2067_text7299269449"></a><a name="evs_04_2067_text7299269449"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2067_row9417574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p24626033185927"><a name="evs_04_2067_p24626033185927"></a><a name="evs_04_2067_p24626033185927"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p48551632185927"><a name="evs_04_2067_p48551632185927"></a><a name="evs_04_2067_p48551632185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p48591276185927"><a name="evs_04_2067_p48591276185927"></a><a name="evs_04_2067_p48591276185927"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row34668301185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p56668991185927"><a name="evs_04_2067_p56668991185927"></a><a name="evs_04_2067_p56668991185927"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p26785545185927"><a name="evs_04_2067_p26785545185927"></a><a name="evs_04_2067_p26785545185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p48959624185927"><a name="evs_04_2067_p48959624185927"></a><a name="evs_04_2067_p48959624185927"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row41070280185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p38358373185927"><a name="evs_04_2067_p38358373185927"></a><a name="evs_04_2067_p38358373185927"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p20020490185927"><a name="evs_04_2067_p20020490185927"></a><a name="evs_04_2067_p20020490185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p22392462185927"><a name="evs_04_2067_p22392462185927"></a><a name="evs_04_2067_p22392462185927"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row205574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p16651565185927"><a name="evs_04_2067_p16651565185927"></a><a name="evs_04_2067_p16651565185927"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p6599487185927"><a name="evs_04_2067_p6599487185927"></a><a name="evs_04_2067_p6599487185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p14021450185927"><a name="evs_04_2067_p14021450185927"></a><a name="evs_04_2067_p14021450185927"></a>Specifies the ID of the attached resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li29114110314"></a>Parameters in the  **metadata**  field

    <a name="evs_04_3004_table3430728295554"></a>
    <table><thead align="left"><tr id="evs_04_3004_row4496975195554"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_3004_p8809200174410"><a name="evs_04_3004_p8809200174410"></a><a name="evs_04_3004_p8809200174410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="evs_04_3004_p168135017449"><a name="evs_04_3004_p168135017449"></a><a name="evs_04_3004_p168135017449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_3004_p1282213034412"><a name="evs_04_3004_p1282213034412"></a><a name="evs_04_3004_p1282213034412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_3004_row456195295554"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p1562408795622"><a name="evs_04_3004_p1562408795622"></a><a name="evs_04_3004_p1562408795622"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p5759155095622"><a name="evs_04_3004_p5759155095622"></a><a name="evs_04_3004_p5759155095622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_3004_p177192813501"><a name="evs_04_3004_p177192813501"></a><a name="evs_04_3004_p177192813501"></a>Specifies the parameter that describes the encryption function in <strong id="evs_04_3004_b84235270614509"><a name="evs_04_3004_b84235270614509"></a><a name="evs_04_3004_b84235270614509"></a>metadata</strong>. The value can be <strong id="evs_04_3004_b842352706145015"><a name="evs_04_3004_b842352706145015"></a><a name="evs_04_3004_b842352706145015"></a>0</strong> or <strong id="evs_04_3004_b842352706145020"><a name="evs_04_3004_b842352706145020"></a><a name="evs_04_3004_b842352706145020"></a>1</strong>.<a name="evs_04_3004_ul141951225145011"></a><a name="evs_04_3004_ul141951225145011"></a><ul id="evs_04_3004_ul141951225145011"><li><strong id="evs_04_3004_b842352706145038"><a name="evs_04_3004_b842352706145038"></a><a name="evs_04_3004_b842352706145038"></a>0</strong>: indicates the disk is not encrypted.</li><li><strong id="evs_04_3004_b842352706145058"><a name="evs_04_3004_b842352706145058"></a><a name="evs_04_3004_b842352706145058"></a>1</strong>: indicates the disk is encrypted.</li><li>If this parameter does not appear, the disk is not encrypted by default.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_3004_row247050109562"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p241272995622"><a name="evs_04_3004_p241272995622"></a><a name="evs_04_3004_p241272995622"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p6121338895622"><a name="evs_04_3004_p6121338895622"></a><a name="evs_04_3004_p6121338895622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_3004_p4159804295622"><a name="evs_04_3004_p4159804295622"></a><a name="evs_04_3004_p4159804295622"></a>Specifies the parameter that describes the encryption CMK ID in <strong id="evs_04_3004_b84235270615116"><a name="evs_04_3004_b84235270615116"></a><a name="evs_04_3004_b84235270615116"></a>metadata</strong>. This parameter is used together with <strong id="evs_04_3004_b842352706143827"><a name="evs_04_3004_b842352706143827"></a><a name="evs_04_3004_b842352706143827"></a>__system__encrypted</strong> for encryption. The length of <strong id="evs_04_3004_b84235270614396"><a name="evs_04_3004_b84235270614396"></a><a name="evs_04_3004_b84235270614396"></a>cmkid</strong> is fixed at 36 bytes.</p>
    </td>
    </tr>
    <tr id="evs_04_3004_row60499086104915"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p1478896104915"><a name="evs_04_3004_p1478896104915"></a><a name="evs_04_3004_p1478896104915"></a>hw:passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p52681767104915"><a name="evs_04_3004_p52681767104915"></a><a name="evs_04_3004_p52681767104915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_3004_p17177177145116"><a name="evs_04_3004_p17177177145116"></a><a name="evs_04_3004_p17177177145116"></a>Specifies the parameter that describes the disk device type in <strong id="evs_04_3004_b84235270615173"><a name="evs_04_3004_b84235270615173"></a><a name="evs_04_3004_b84235270615173"></a>metadata</strong>. The value can be <strong id="evs_04_3004_b842352706151718"><a name="evs_04_3004_b842352706151718"></a><a name="evs_04_3004_b842352706151718"></a>true</strong> or <strong id="evs_04_3004_b842352706151722"><a name="evs_04_3004_b842352706151722"></a><a name="evs_04_3004_b842352706151722"></a>false</strong>.<a name="evs_04_3004_ul14462208141855"></a><a name="evs_04_3004_ul14462208141855"></a><ul id="evs_04_3004_ul14462208141855"><li>If this parameter is set to <strong id="evs_04_3004_b55868159103732"><a name="evs_04_3004_b55868159103732"></a><a name="evs_04_3004_b55868159103732"></a>true</strong>, the disk device type is SCSI, that is, Small Computer System Interface (SCSI), which allows ECS OSs to directly access the underlying storage media and supports SCSI reservation commands.</li><li>If this parameter is set to <strong>false</strong>, the disk device type is VBD (the default type), that is, Virtual Block Device (VBD), which supports only simple SCSI read/write commands.</li><li>If this parameter does not appear, the disk device type is VBD.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_3004_row991210132288"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p3500156018292"><a name="evs_04_3004_p3500156018292"></a><a name="evs_04_3004_p3500156018292"></a>full_clone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p1655411118292"><a name="evs_04_3004_p1655411118292"></a><a name="evs_04_3004_p1655411118292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_3004_p47931946183150"><a name="evs_04_3004_p47931946183150"></a><a name="evs_04_3004_p47931946183150"></a>Specifies the clone method. When the disk is created from a snapshot, the parameter value is <strong id="evs_04_3004_b84235270616922"><a name="evs_04_3004_b84235270616922"></a><a name="evs_04_3004_b84235270616922"></a>0</strong>, indicating the linked cloning method.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p19541716103019"><a name="evs_04_2013_p19541716103019"></a><a name="evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p39375186103019"><a name="evs_04_2013_p39375186103019"></a><a name="evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p38578950103019"><a name="evs_04_2013_p38578950103019"></a><a name="evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p46815658103019"><a name="evs_04_2013_p46815658103019"></a><a name="evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p33971979103019"><a name="evs_04_2013_p33971979103019"></a><a name="evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p21623243103019"><a name="evs_04_2013_p21623243103019"></a><a name="evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p59870541103019"><a name="evs_04_2013_p59870541103019"></a><a name="evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p17675690103019"><a name="evs_04_2013_p17675690103019"></a><a name="evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p6087468103019"><a name="evs_04_2013_p6087468103019"></a><a name="evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2013_p54787218103019"><a name="evs_04_2013_p54787218103019"></a><a name="evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "volumes": [
            {
                "attachments": [ ], 
                "availability_zone": "az-dc-1", 
                "bootable": "false", 
                "consistencygroup_id": null, 
                "created_at": "2016-05-25T02:42:10.856332", 
                "description": null, 
                "encrypted": false, 
                "id": "b104b8db-170d-441b-897a-3c8ba9c5a214", 
                "links": [
                    {
                        "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes/b104b8db-170d-441b-897a-3c8ba9c5a214", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.localdomain.com:8776/dd14c6ac581f40059e27f5320b60bf2f/volumes/b104b8db-170d-441b-897a-3c8ba9c5a214", 
                        "rel": "bookmark"
                    }
                ], 
                "metadata": {}, 
                "name": "zjb_u25_test", 
                "os-vol-host-attr:host": "pod01.xxx#SATA", 
                "volume_image_metadata": { }, 
                "os-vol-mig-status-attr:migstat": null, 
                "os-vol-mig-status-attr:name_id": null, 
                "os-vol-tenant-attr:tenant_id": "dd14c6ac581f40059e27f5320b60bf2f",  
                "os-volume-replication:extended_status": null, 
                "replication_status": "disabled", 
                "multiattach": false, 
                "size": 1, 
                "snapshot_id": null, 
                "source_volid": null, 
                "status": "available", 
                "updated_at": "2016-05-25T02:42:22.341984", 
                "user_id": "b0524e8342084ef5b74f158f78fc3049", 
                "volume_type": "SATA"
            }
        ], 
        "volumes_links": [
            {
                "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes/detail?limit=1&marker=b104b8db-170d-441b-897a-3c8ba9c5a214", 
                "rel": "next"
            }
        ]
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badrequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "itemNotFound": {
            "message": "XXXX", 
            "code": "XXX"
        }
    } 
    ```


## Status Codes<a name="section63839913"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

