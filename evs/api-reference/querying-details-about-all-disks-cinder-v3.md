# Querying Details About All Disks<a name="evs_04_3033"></a>

## Function<a name="section60214390"></a>

This API is used to query details about all disks.

## URI<a name="section5058598"></a>

-   URI format

    GET /v3/\{project\_id\}/volumes/detail

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

    <a name="en-us_topic_0058762431_table4291376694520"></a>
    <table><thead align="left"><tr id="en-us_topic_0058762431_row75210794520"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.1.5.1.1"><p id="en-us_topic_0058762431_p6092069194520"><a name="en-us_topic_0058762431_p6092069194520"></a><a name="en-us_topic_0058762431_p6092069194520"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.1.5.1.2"><p id="en-us_topic_0058762431_p3562891594520"><a name="en-us_topic_0058762431_p3562891594520"></a><a name="en-us_topic_0058762431_p3562891594520"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.1.5.1.3"><p id="en-us_topic_0058762431_p26101294520"><a name="en-us_topic_0058762431_p26101294520"></a><a name="en-us_topic_0058762431_p26101294520"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.1.5.1.4"><p id="en-us_topic_0058762431_p2114201394520"><a name="en-us_topic_0058762431_p2114201394520"></a><a name="en-us_topic_0058762431_p2114201394520"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0058762431_row3478152794520"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p60095082153718"><a name="en-us_topic_0058762431_p60095082153718"></a><a name="en-us_topic_0058762431_p60095082153718"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p35863456153718"><a name="en-us_topic_0058762431_p35863456153718"></a><a name="en-us_topic_0058762431_p35863456153718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p19258860153718"><a name="en-us_topic_0058762431_p19258860153718"></a><a name="en-us_topic_0058762431_p19258860153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762431_p16463795153718"><a name="en-us_topic_0058762431_p16463795153718"></a><a name="en-us_topic_0058762431_p16463795153718"></a><span id="text97115183392"><a name="text97115183392"></a><a name="text97115183392"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row2183600894520"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p56729311153718"><a name="en-us_topic_0058762431_p56729311153718"></a><a name="en-us_topic_0058762431_p56729311153718"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p38113769154021"><a name="en-us_topic_0058762431_p38113769154021"></a><a name="en-us_topic_0058762431_p38113769154021"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p15250867153718"><a name="en-us_topic_0058762431_p15250867153718"></a><a name="en-us_topic_0058762431_p15250867153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762431_p27360714153718"><a name="en-us_topic_0058762431_p27360714153718"></a><a name="en-us_topic_0058762431_p27360714153718"></a>Specifies the disk name. <span id="text2141049795191221"><a name="text2141049795191221"></a><a name="text2141049795191221"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row4640654394520"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p14628184153718"><a name="en-us_topic_0058762431_p14628184153718"></a><a name="en-us_topic_0058762431_p14628184153718"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p44032231153718"><a name="en-us_topic_0058762431_p44032231153718"></a><a name="en-us_topic_0058762431_p44032231153718"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p9840947153718"><a name="en-us_topic_0058762431_p9840947153718"></a><a name="en-us_topic_0058762431_p9840947153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762431_p58919203153718"><a name="en-us_topic_0058762431_p58919203153718"></a><a name="en-us_topic_0058762431_p58919203153718"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p13400175415125"><a name="p13400175415125"></a><a name="p13400175415125"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    <p id="en-us_topic_0058762431_p14657115572511"><a name="en-us_topic_0058762431_p14657115572511"></a><a name="en-us_topic_0058762431_p14657115572511"></a>If the tenant has more than 50 disks in total, you are advised to use this parameter and set its value to <strong id="b8423527069161"><a name="b8423527069161"></a><a name="b8423527069161"></a>50</strong> to improve the query efficiency. Examples are provided as follows:</p>
    <p id="en-us_topic_0058762431_p1233994321914"><a name="en-us_topic_0058762431_p1233994321914"></a><a name="en-us_topic_0058762431_p1233994321914"></a><strong id="b320873402103755"><a name="b320873402103755"></a><a name="b320873402103755"></a>GET /v3/</strong><em id="i1514898224103755"><a name="i1514898224103755"></a><a name="i1514898224103755"></a>xxx</em><strong id="b738773580103755"><a name="b738773580103755"></a><a name="b738773580103755"></a>/volumes/detail?limit=50</strong>: Queries the 1–50 disks. <strong id="b842352706103810"><a name="b842352706103810"></a><a name="b842352706103810"></a>GET /v3/</strong><em id="i197699858310388"><a name="i197699858310388"></a><a name="i197699858310388"></a>xxx</em><strong id="b842352706103816"><a name="b842352706103816"></a><a name="b842352706103816"></a>/volumes/detail?offset=50&amp;limit=50</strong>: Queries the 51–100 disks.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row6054321594520"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p2426142153718"><a name="en-us_topic_0058762431_p2426142153718"></a><a name="en-us_topic_0058762431_p2426142153718"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p43526083154024"><a name="en-us_topic_0058762431_p43526083154024"></a><a name="en-us_topic_0058762431_p43526083154024"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p13119059153718"><a name="en-us_topic_0058762431_p13119059153718"></a><a name="en-us_topic_0058762431_p13119059153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p43249593152914"><a name="p43249593152914"></a><a name="p43249593152914"></a>Specifies the keyword based on which the returned results are sorted. The value can be <strong id="b4400163616110"><a name="b4400163616110"></a><a name="b4400163616110"></a>id</strong>, <strong id="b94018361111"><a name="b94018361111"></a><a name="b94018361111"></a>status</strong>, <strong id="b1940243615119"><a name="b1940243615119"></a><a name="b1940243615119"></a>size</strong>, or <strong id="b340215361117"><a name="b340215361117"></a><a name="b340215361117"></a>created_at</strong>, and the default value is <strong id="b1340310368117"><a name="b1340310368117"></a><a name="b1340310368117"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row5521380794520"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p29735682153718"><a name="en-us_topic_0058762431_p29735682153718"></a><a name="en-us_topic_0058762431_p29735682153718"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p16700889154026"><a name="en-us_topic_0058762431_p16700889154026"></a><a name="en-us_topic_0058762431_p16700889154026"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p10345862153718"><a name="en-us_topic_0058762431_p10345862153718"></a><a name="en-us_topic_0058762431_p10345862153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><div class="p" id="p2025341125211"><a name="p2025341125211"></a><a name="p2025341125211"></a>Specifies the result sorting order. The default value is <strong id="b160741201119"><a name="b160741201119"></a><a name="b160741201119"></a>desc</strong>.<a name="ul107075455529"></a><a name="ul107075455529"></a><ul id="ul107075455529"><li><strong id="b711942181114"><a name="b711942181114"></a><a name="b711942181114"></a>desc</strong>: indicates the descending order.</li><li><strong id="b15334124341110"><a name="b15334124341110"></a><a name="b15334124341110"></a>asc</strong>: indicates the ascending order.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row49871977153626"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p20840349153718"><a name="en-us_topic_0058762431_p20840349153718"></a><a name="en-us_topic_0058762431_p20840349153718"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p10346748153718"><a name="en-us_topic_0058762431_p10346748153718"></a><a name="en-us_topic_0058762431_p10346748153718"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p32780292153718"><a name="en-us_topic_0058762431_p32780292153718"></a><a name="en-us_topic_0058762431_p32780292153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p02247913491"><a name="p02247913491"></a><a name="p02247913491"></a>Specifies the offset.</p>
    <p id="en-us_topic_0058762430_p27592310152914"><a name="en-us_topic_0058762430_p27592310152914"></a><a name="en-us_topic_0058762430_p27592310152914"></a>All disks after this offset will be queried. The value must be an integer greater than 0 but less than the number of disks.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row2837320153624"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p22515601153718"><a name="en-us_topic_0058762431_p22515601153718"></a><a name="en-us_topic_0058762431_p22515601153718"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p53812252154029"><a name="en-us_topic_0058762431_p53812252154029"></a><a name="en-us_topic_0058762431_p53812252154029"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p18251790153718"><a name="en-us_topic_0058762431_p18251790153718"></a><a name="en-us_topic_0058762431_p18251790153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762431_p2000007153718"><a name="en-us_topic_0058762431_p2000007153718"></a><a name="en-us_topic_0058762431_p2000007153718"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row34125704153621"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p48719302153718"><a name="en-us_topic_0058762431_p48719302153718"></a><a name="en-us_topic_0058762431_p48719302153718"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p31082833154032"><a name="en-us_topic_0058762431_p31082833154032"></a><a name="en-us_topic_0058762431_p31082833154032"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p7822125153718"><a name="en-us_topic_0058762431_p7822125153718"></a><a name="en-us_topic_0058762431_p7822125153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762431_p29612385153718"><a name="en-us_topic_0058762431_p29612385153718"></a><a name="en-us_topic_0058762431_p29612385153718"></a>Specifies the disk metadata.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row61070326153619"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762431_p45483948153718"><a name="en-us_topic_0058762431_p45483948153718"></a><a name="en-us_topic_0058762431_p45483948153718"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762431_p23816783154035"><a name="en-us_topic_0058762431_p23816783154035"></a><a name="en-us_topic_0058762431_p23816783154035"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762431_p54179442153718"><a name="en-us_topic_0058762431_p54179442153718"></a><a name="en-us_topic_0058762431_p54179442153718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762431_p26458700153718"><a name="en-us_topic_0058762431_p26458700153718"></a><a name="en-us_topic_0058762431_p26458700153718"></a>Specifies the AZ.</p>
    </td>
    </tr>
    <tr id="row6676213154019"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p593962174016"><a name="p593962174016"></a><a name="p593962174016"></a>glance_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="p09391721164012"><a name="p09391721164012"></a><a name="p09391721164012"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="p109391521154019"><a name="p109391521154019"></a><a name="p109391521154019"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p119391721144016"><a name="p119391721144016"></a><a name="p119391721144016"></a>Specifies the filtered query of the image metadata in the {'key':'value'} format. This parameter is supported when the request version is 3.4 or later.</p>
    </td>
    </tr>
    <tr id="row9350191184012"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p555112711331"><a name="p555112711331"></a><a name="p555112711331"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="p9551927163312"><a name="p9551927163312"></a><a name="p9551927163312"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="p13551152715338"><a name="p13551152715338"></a><a name="p13551152715338"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p2066824720366"><a name="p2066824720366"></a><a name="p2066824720366"></a>Specifies whether the query result contains system disks. The values are as follows:</p>
    <a name="ul6874551442"></a><a name="ul6874551442"></a><ul id="ul6874551442"><li><strong id="b84235270611643"><a name="b84235270611643"></a><a name="b84235270611643"></a>True</strong>, <strong id="b84235270611646"><a name="b84235270611646"></a><a name="b84235270611646"></a>true</strong>, and <strong id="b84235270611648"><a name="b84235270611648"></a><a name="b84235270611648"></a>1</strong>: The query result contains system disks only.</li><li><strong id="b84235270611738"><a name="b84235270611738"></a><a name="b84235270611738"></a>False</strong>, <strong id="b84235270611740"><a name="b84235270611740"></a><a name="b84235270611740"></a>false</strong>, and <strong id="b84235270611746"><a name="b84235270611746"></a><a name="b84235270611746"></a>0</strong>: The query result does not contain system disks.</li></ul>
    <p id="p1555132715333"><a name="p1555132715333"></a><a name="p1555132715333"></a>This parameter is supported when the request version is 3.2 or later.</p>
    </td>
    </tr>
    <tr id="row33501019401"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p75521327113313"><a name="p75521327113313"></a><a name="p75521327113313"></a>migration_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="p655282715338"><a name="p655282715338"></a><a name="p655282715338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="p14552122793312"><a name="p14552122793312"></a><a name="p14552122793312"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p6552122783310"><a name="p6552122783310"></a><a name="p6552122783310"></a>Specifies the migration status. The value can be <strong id="b84235270618289"><a name="b84235270618289"></a><a name="b84235270618289"></a>starting</strong>, <strong id="b842352706182812"><a name="b842352706182812"></a><a name="b842352706182812"></a>migrating</strong>, <strong id="b842352706182815"><a name="b842352706182815"></a><a name="b842352706182815"></a>success</strong>, or <strong id="b842352706182821"><a name="b842352706182821"></a><a name="b842352706182821"></a>error</strong>.</p>
    </td>
    </tr>
    <tr id="row235071164017"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p1355262793315"><a name="p1355262793315"></a><a name="p1355262793315"></a>name~</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="p15552102720334"><a name="p15552102720334"></a><a name="p15552102720334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="p12552102719334"><a name="p12552102719334"></a><a name="p12552102719334"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p11552182715331"><a name="p11552182715331"></a><a name="p11552182715331"></a>Specifies the fuzzy search by disk name. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row73509116408"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p555232714335"><a name="p555232714335"></a><a name="p555232714335"></a>status~</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="p11553122753313"><a name="p11553122753313"></a><a name="p11553122753313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="p1955322717338"><a name="p1955322717338"></a><a name="p1955322717338"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p25531427163315"><a name="p25531427163315"></a><a name="p25531427163315"></a>Specifies the fuzzy search by disk status. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row1335212164020"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p13553122718335"><a name="p13553122718335"></a><a name="p13553122718335"></a>availability_zone~</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="p19553327153317"><a name="p19553327153317"></a><a name="p19553327153317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="p955392711337"><a name="p955392711337"></a><a name="p955392711337"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p155362723314"><a name="p155362723314"></a><a name="p155362723314"></a>Specifies the fuzzy search by AZ. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row133528115408"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p16553112711338"><a name="p16553112711338"></a><a name="p16553112711338"></a>migration_status~</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="p1255322763313"><a name="p1255322763313"></a><a name="p1255322763313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="p855362710335"><a name="p855362710335"></a><a name="p855362710335"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p45541272332"><a name="p45541272332"></a><a name="p45541272332"></a>Specifies the fuzzy search by migration status. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row153521411400"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p155547276337"><a name="p155547276337"></a><a name="p155547276337"></a>with_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.5.1.2 "><p id="p855442773311"><a name="p855442773311"></a><a name="p855442773311"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.3 "><p id="p1055420271339"><a name="p1055420271339"></a><a name="p1055420271339"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p355419276334"><a name="p355419276334"></a><a name="p355419276334"></a>Specifies to return parameter <strong id="b842352706111032"><a name="b842352706111032"></a><a name="b842352706111032"></a>counts</strong> in the response. This parameter indicates the number of disks queried. This parameter is in the <em id="i842352697111123"><a name="i842352697111123"></a><a name="i842352697111123"></a>with_count=true</em> format and is supported when the request version is 3.45 or later.</p>
    <p id="p136761332131419"><a name="p136761332131419"></a><a name="p136761332131419"></a>This parameter can be used together with parameters <strong id="evs_04_3032_b842352706155655"><a name="evs_04_3032_b842352706155655"></a><a name="evs_04_3032_b842352706155655"></a>marker</strong>, <strong id="evs_04_3032_b842352706155659"><a name="evs_04_3032_b842352706155659"></a><a name="evs_04_3032_b842352706155659"></a>limit</strong>, <strong id="evs_04_3032_b84235270615572"><a name="evs_04_3032_b84235270615572"></a><a name="evs_04_3032_b84235270615572"></a>sort_key</strong>, <strong id="evs_04_3032_b84235270615576"><a name="evs_04_3032_b84235270615576"></a><a name="evs_04_3032_b84235270615576"></a>sort_dir</strong>, or <strong id="evs_04_3032_b842352706155718"><a name="evs_04_3032_b842352706155718"></a><a name="evs_04_3032_b842352706155718"></a>offset</strong> in the table. It cannot be used with other filter parameters.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3266414134213"></a>

The following example shows how to query details of the disks in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/volumes/detail?status=available
    ```


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="table3231819124520"></a>
    <table><thead align="left"><tr id="row182320192456"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p62321919144515"><a name="p62321919144515"></a><a name="p62321919144515"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.14788521147885%" id="mcps1.1.4.1.2"><p id="p2232219174510"><a name="p2232219174510"></a><a name="p2232219174510"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.67423257674233%" id="mcps1.1.4.1.3"><p id="p132325192454"><a name="p132325192454"></a><a name="p132325192454"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42321819154515"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p823213196454"><a name="p823213196454"></a><a name="p823213196454"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="p13232181974513"><a name="p13232181974513"></a><a name="p13232181974513"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="p5232131916457"><a name="p5232131916457"></a><a name="p5232131916457"></a>Specifies the list of queried disks. For details, see <a href="#en-us_topic_0058762431_li3451542201439">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="row1024031914455"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p7240111944517"><a name="p7240111944517"></a><a name="p7240111944517"></a>volumes_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="p1924013198451"><a name="p1924013198451"></a><a name="p1924013198451"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="p9240101964519"><a name="p9240101964519"></a><a name="p9240101964519"></a>Specifies the query position marker in the disk list. If only some disks are returned in this query, the URL of the last disk queried will be returned. You can use this URL to continue to query the remaining disks in the next query. For details, see <a href="#en-us_topic_0058762431_li851885019247">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row12240101910453"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p524014194457"><a name="p524014194457"></a><a name="p524014194457"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="p42411119174517"><a name="p42411119174517"></a><a name="p42411119174517"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="p14241151924514"><a name="p14241151924514"></a><a name="p14241151924514"></a>Specifies the number of records returned in this query.</p>
    </td>
    </tr>
    <tr id="row1825458164715"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="en-us_topic_0058762431_li3451542201439"></a>Parameters in the  **volumes**  field

    <a name="en-us_topic_0058762431_table34701445142557"></a>
    <table><thead align="left"><tr id="en-us_topic_0058762431_row12524911142557"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="en-us_topic_0058762431_p7884856142557"><a name="en-us_topic_0058762431_p7884856142557"></a><a name="en-us_topic_0058762431_p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.14788521147885%" id="mcps1.1.4.1.2"><p id="en-us_topic_0058762431_p34693598142557"><a name="en-us_topic_0058762431_p34693598142557"></a><a name="en-us_topic_0058762431_p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.67423257674233%" id="mcps1.1.4.1.3"><p id="en-us_topic_0058762431_p58539486142557"><a name="en-us_topic_0058762431_p58539486142557"></a><a name="en-us_topic_0058762431_p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0058762431_row444782011610"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p54175786153922"><a name="en-us_topic_0058762431_p54175786153922"></a><a name="en-us_topic_0058762431_p54175786153922"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p26162565153922"><a name="en-us_topic_0058762431_p26162565153922"></a><a name="en-us_topic_0058762431_p26162565153922"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p55227932153922"><a name="en-us_topic_0058762431_p55227932153922"></a><a name="en-us_topic_0058762431_p55227932153922"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row44077962142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p62953588153922"><a name="en-us_topic_0058762431_p62953588153922"></a><a name="en-us_topic_0058762431_p62953588153922"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p494261191750"><a name="en-us_topic_0058762431_p494261191750"></a><a name="en-us_topic_0058762431_p494261191750"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p379966153922"><a name="en-us_topic_0058762431_p379966153922"></a><a name="en-us_topic_0058762431_p379966153922"></a>Specifies the disk URI. For details, see <a href="#en-us_topic_0058762431_li851885019247">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row16186817142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p8559918153922"><a name="en-us_topic_0058762431_p8559918153922"></a><a name="en-us_topic_0058762431_p8559918153922"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p38279089154138"><a name="en-us_topic_0058762431_p38279089154138"></a><a name="en-us_topic_0058762431_p38279089154138"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p50401086153922"><a name="en-us_topic_0058762431_p50401086153922"></a><a name="en-us_topic_0058762431_p50401086153922"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row45785905142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p33843531153922"><a name="en-us_topic_0058762431_p33843531153922"></a><a name="en-us_topic_0058762431_p33843531153922"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p15510513154140"><a name="en-us_topic_0058762431_p15510513154140"></a><a name="en-us_topic_0058762431_p15510513154140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p60776191153922"><a name="en-us_topic_0058762431_p60776191153922"></a><a name="en-us_topic_0058762431_p60776191153922"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row35247553142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p13993091153922"><a name="en-us_topic_0058762431_p13993091153922"></a><a name="en-us_topic_0058762431_p13993091153922"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p59698591153922"><a name="en-us_topic_0058762431_p59698591153922"></a><a name="en-us_topic_0058762431_p59698591153922"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p35128232153922"><a name="en-us_topic_0058762431_p35128232153922"></a><a name="en-us_topic_0058762431_p35128232153922"></a>Specifies the disk attachment information. For details, see <a href="#en-us_topic_0058762431_li5001921919316">Parameters in the attachments field</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row27126244142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p40004503153922"><a name="en-us_topic_0058762431_p40004503153922"></a><a name="en-us_topic_0058762431_p40004503153922"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p51760296154143"><a name="en-us_topic_0058762431_p51760296154143"></a><a name="en-us_topic_0058762431_p51760296154143"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p12372460153922"><a name="en-us_topic_0058762431_p12372460153922"></a><a name="en-us_topic_0058762431_p12372460153922"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row7009490142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p26935952153922"><a name="en-us_topic_0058762431_p26935952153922"></a><a name="en-us_topic_0058762431_p26935952153922"></a>os-vol-host-attr:host</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p61285780154145"><a name="en-us_topic_0058762431_p61285780154145"></a><a name="en-us_topic_0058762431_p61285780154145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p12079427153922"><a name="en-us_topic_0058762431_p12079427153922"></a><a name="en-us_topic_0058762431_p12079427153922"></a><span id="text1720893911585"><a name="text1720893911585"></a><a name="text1720893911585"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row49237196142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p14641407153922"><a name="en-us_topic_0058762431_p14641407153922"></a><a name="en-us_topic_0058762431_p14641407153922"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p15993974154147"><a name="en-us_topic_0058762431_p15993974154147"></a><a name="en-us_topic_0058762431_p15993974154147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p40148014153922"><a name="en-us_topic_0058762431_p40148014153922"></a><a name="en-us_topic_0058762431_p40148014153922"></a>Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.</p>
    <p id="p4357134552610"><a name="p4357134552610"></a><a name="p4357134552610"></a><span id="text18357144552617"><a name="text18357144552617"></a><a name="text18357144552617"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row39017307142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p8437822153922"><a name="en-us_topic_0058762431_p8437822153922"></a><a name="en-us_topic_0058762431_p8437822153922"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p43970411154151"><a name="en-us_topic_0058762431_p43970411154151"></a><a name="en-us_topic_0058762431_p43970411154151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p57569910153922"><a name="en-us_topic_0058762431_p57569910153922"></a><a name="en-us_topic_0058762431_p57569910153922"></a>Specifies the snapshot ID. This parameter has a value if the disk is created from a snapshot.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row20107664142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p25424812153922"><a name="en-us_topic_0058762431_p25424812153922"></a><a name="en-us_topic_0058762431_p25424812153922"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p16247974154153"><a name="en-us_topic_0058762431_p16247974154153"></a><a name="en-us_topic_0058762431_p16247974154153"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p22193516153922"><a name="en-us_topic_0058762431_p22193516153922"></a><a name="en-us_topic_0058762431_p22193516153922"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row12897861142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p5837556153922"><a name="en-us_topic_0058762431_p5837556153922"></a><a name="en-us_topic_0058762431_p5837556153922"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p30798966154156"><a name="en-us_topic_0058762431_p30798966154156"></a><a name="en-us_topic_0058762431_p30798966154156"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p8308266153922"><a name="en-us_topic_0058762431_p8308266153922"></a><a name="en-us_topic_0058762431_p8308266153922"></a>Specifies the time when the disk was created.</p>
    <p id="p23708433313"><a name="p23708433313"></a><a name="p23708433313"></a><span id="text127118487312"><a name="text127118487312"></a><a name="text127118487312"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row45680217142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p16928326153922"><a name="en-us_topic_0058762431_p16928326153922"></a><a name="en-us_topic_0058762431_p16928326153922"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p35495495154158"><a name="en-us_topic_0058762431_p35495495154158"></a><a name="en-us_topic_0058762431_p35495495154158"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p60775887153922"><a name="en-us_topic_0058762431_p60775887153922"></a><a name="en-us_topic_0058762431_p60775887153922"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row47480567142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p13771931153922"><a name="en-us_topic_0058762431_p13771931153922"></a><a name="en-us_topic_0058762431_p13771931153922"></a>os-vol-tenant-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p4873995415420"><a name="en-us_topic_0058762431_p4873995415420"></a><a name="en-us_topic_0058762431_p4873995415420"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p9058246153922"><a name="en-us_topic_0058762431_p9058246153922"></a><a name="en-us_topic_0058762431_p9058246153922"></a>Specifies the ID of the tenant to which the disk belongs. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row31517135142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p26792948153922"><a name="en-us_topic_0058762431_p26792948153922"></a><a name="en-us_topic_0058762431_p26792948153922"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p22745155153922"><a name="en-us_topic_0058762431_p22745155153922"></a><a name="en-us_topic_0058762431_p22745155153922"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p47959551153922"><a name="en-us_topic_0058762431_p47959551153922"></a><a name="en-us_topic_0058762431_p47959551153922"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row15610713142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p65903514153922"><a name="en-us_topic_0058762431_p65903514153922"></a><a name="en-us_topic_0058762431_p65903514153922"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p36584404153922"><a name="en-us_topic_0058762431_p36584404153922"></a><a name="en-us_topic_0058762431_p36584404153922"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p63055822144653"><a name="en-us_topic_0058762431_p63055822144653"></a><a name="en-us_topic_0058762431_p63055822144653"></a>Specifies the disk metadata. For details, see <a href="#li29114110314">Parameters in the metadata field</a>.</p>
    <p id="en-us_topic_0058762431_p1210013914474"><a name="en-us_topic_0058762431_p1210013914474"></a><a name="en-us_topic_0058762431_p1210013914474"></a>If <strong id="b842352706192015"><a name="b842352706192015"></a><a name="b842352706192015"></a>metadata</strong> does not contain the <strong id="b842352706143434"><a name="b842352706143434"></a><a name="b842352706143434"></a>hw:passthrough</strong> field, the disk device type is VBD.</p>
    <p id="en-us_topic_0058762431_p3812802015506"><a name="en-us_topic_0058762431_p3812802015506"></a><a name="en-us_topic_0058762431_p3812802015506"></a>If <strong id="b842352706192028"><a name="b842352706192028"></a><a name="b842352706192028"></a>metadata</strong> does not contain the <strong id="b842352706143455"><a name="b842352706143455"></a><a name="b842352706143455"></a>__system__encrypted</strong> field, the disk is not encrypted.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row5657368142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p5824606153922"><a name="en-us_topic_0058762431_p5824606153922"></a><a name="en-us_topic_0058762431_p5824606153922"></a>os-vol-mig-status-attr:migstat</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p28057958154213"><a name="en-us_topic_0058762431_p28057958154213"></a><a name="en-us_topic_0058762431_p28057958154213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p38401827153922"><a name="en-us_topic_0058762431_p38401827153922"></a><a name="en-us_topic_0058762431_p38401827153922"></a><span id="text203605127103"><a name="text203605127103"></a><a name="text203605127103"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row42462677142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p10535641153922"><a name="en-us_topic_0058762431_p10535641153922"></a><a name="en-us_topic_0058762431_p10535641153922"></a>os-vol-mig-status-attr:name_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p41814751154216"><a name="en-us_topic_0058762431_p41814751154216"></a><a name="en-us_topic_0058762431_p41814751154216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p45371608153922"><a name="en-us_topic_0058762431_p45371608153922"></a><a name="en-us_topic_0058762431_p45371608153922"></a><span id="text268125418222"><a name="text268125418222"></a><a name="text268125418222"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row35655683142957"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p42283458153922"><a name="en-us_topic_0058762431_p42283458153922"></a><a name="en-us_topic_0058762431_p42283458153922"></a>os-volume-replication:extended_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p9813320154224"><a name="en-us_topic_0058762431_p9813320154224"></a><a name="en-us_topic_0058762431_p9813320154224"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p28603805153922"><a name="en-us_topic_0058762431_p28603805153922"></a><a name="en-us_topic_0058762431_p28603805153922"></a><span id="text379518478151"><a name="text379518478151"></a><a name="text379518478151"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row57913155185111"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p47452553185118"><a name="en-us_topic_0058762431_p47452553185118"></a><a name="en-us_topic_0058762431_p47452553185118"></a>encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p18451581185118"><a name="en-us_topic_0058762431_p18451581185118"></a><a name="en-us_topic_0058762431_p18451581185118"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p27951625185124"><a name="en-us_topic_0058762431_p27951625185124"></a><a name="en-us_topic_0058762431_p27951625185124"></a><span id="text16290132561216"><a name="text16290132561216"></a><a name="text16290132561216"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row6226231314391"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p50459706153922"><a name="en-us_topic_0058762431_p50459706153922"></a><a name="en-us_topic_0058762431_p50459706153922"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p43392623154228"><a name="en-us_topic_0058762431_p43392623154228"></a><a name="en-us_topic_0058762431_p43392623154228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p57639660153922"><a name="en-us_topic_0058762431_p57639660153922"></a><a name="en-us_topic_0058762431_p57639660153922"></a><span id="text6498181171119"><a name="text6498181171119"></a><a name="text6498181171119"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row1430942214399"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p9163288153922"><a name="en-us_topic_0058762431_p9163288153922"></a><a name="en-us_topic_0058762431_p9163288153922"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p28184221154230"><a name="en-us_topic_0058762431_p28184221154230"></a><a name="en-us_topic_0058762431_p28184221154230"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p59763545153922"><a name="en-us_topic_0058762431_p59763545153922"></a><a name="en-us_topic_0058762431_p59763545153922"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row1801485814395"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p13972139153922"><a name="en-us_topic_0058762431_p13972139153922"></a><a name="en-us_topic_0058762431_p13972139153922"></a>consistencygroup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p60028304154232"><a name="en-us_topic_0058762431_p60028304154232"></a><a name="en-us_topic_0058762431_p60028304154232"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="p17844141412282"><a name="p17844141412282"></a><a name="p17844141412282"></a><span id="text13343838181111"><a name="text13343838181111"></a><a name="text13343838181111"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row53974058144326"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p48844805153922"><a name="en-us_topic_0058762431_p48844805153922"></a><a name="en-us_topic_0058762431_p48844805153922"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p26156143154240"><a name="en-us_topic_0058762431_p26156143154240"></a><a name="en-us_topic_0058762431_p26156143154240"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p8780414125315"><a name="en-us_topic_0098680634_p8780414125315"></a><a name="en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="ul185931714111"></a><a name="ul185931714111"></a><ul id="ul185931714111"><li><strong id="b488011641716"><a name="b488011641716"></a><a name="b488011641716"></a>true</strong>: specifies a bootable disk.</li><li><strong id="b4793177121718"><a name="b4793177121718"></a><a name="b4793177121718"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row46340323144336"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p57039357153922"><a name="en-us_topic_0058762431_p57039357153922"></a><a name="en-us_topic_0058762431_p57039357153922"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p51292786154244"><a name="en-us_topic_0058762431_p51292786154244"></a><a name="en-us_topic_0058762431_p51292786154244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p46488385153922"><a name="en-us_topic_0058762431_p46488385153922"></a><a name="en-us_topic_0058762431_p46488385153922"></a>Specifies the time when the disk was updated.</p>
    <p id="p121428117412"><a name="p121428117412"></a><a name="p121428117412"></a><span id="text91428118418"><a name="text91428118418"></a><a name="text91428118418"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row36758187144417"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p56950153922"><a name="en-us_topic_0058762431_p56950153922"></a><a name="en-us_topic_0058762431_p56950153922"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p4612960153922"><a name="en-us_topic_0058762431_p4612960153922"></a><a name="en-us_topic_0058762431_p4612960153922"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p66643618153922"><a name="en-us_topic_0058762431_p66643618153922"></a><a name="en-us_topic_0058762431_p66643618153922"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="en-us_topic_0058762431_note3800959821323"><a name="en-us_topic_0058762431_note3800959821323"></a><a name="en-us_topic_0058762431_note3800959821323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0058762431_p45212589213213"><a name="en-us_topic_0058762431_p45212589213213"></a><a name="en-us_topic_0058762431_p45212589213213"></a>This field is no longer used. Use <strong id="b84235270610834"><a name="b84235270610834"></a><a name="b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row4658776614505"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p63488919153922"><a name="en-us_topic_0058762431_p63488919153922"></a><a name="en-us_topic_0058762431_p63488919153922"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p42328837153922"><a name="en-us_topic_0058762431_p42328837153922"></a><a name="en-us_topic_0058762431_p42328837153922"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p4781191416535"><a name="en-us_topic_0098680634_p4781191416535"></a><a name="en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="ul161621719119"></a><a name="ul161621719119"></a><ul id="ul161621719119"><li><strong id="b4786119101714"><a name="b4786119101714"></a><a name="b4786119101714"></a>true</strong>: specifies a shared disk.</li><li><strong id="b2664161041719"><a name="b2664161041719"></a><a name="b2664161041719"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0058762431_row29234512142557"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762431_p5432339153922"><a name="en-us_topic_0058762431_p5432339153922"></a><a name="en-us_topic_0058762431_p5432339153922"></a>volume_image_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.14788521147885%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762431_p37366318153922"><a name="en-us_topic_0058762431_p37366318153922"></a><a name="en-us_topic_0058762431_p37366318153922"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.67423257674233%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762431_p11733449153922"><a name="en-us_topic_0058762431_p11733449153922"></a><a name="en-us_topic_0058762431_p11733449153922"></a>Specifies whether the disk is created from an image. This field has a value if the disk is created from an image. Otherwise, it is left empty.</p>
    <div class="note" id="note14735916164810"><a name="note14735916164810"></a><a name="note14735916164810"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2009_p1888154732118"><a name="evs_04_2009_p1888154732118"></a><a name="evs_04_2009_p1888154732118"></a>For details about <strong id="evs_04_2009_b664802919300"><a name="evs_04_2009_b664802919300"></a><a name="evs_04_2009_b664802919300"></a>volume_image_metadata</strong>, see <strong id="evs_04_2009_b0649629203016"><a name="evs_04_2009_b0649629203016"></a><a name="evs_04_2009_b0649629203016"></a>Querying Image Details</strong> in the <em id="evs_04_2009_i186501329183018"><a name="evs_04_2009_i186501329183018"></a><a name="evs_04_2009_i186501329183018"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="en-us_topic_0058762431_li851885019247"></a>Parameters in the  **links**  field

    <a name="evs_04_2069_evs_04_2067_table24355024185927"></a>
    <table><thead align="left"><tr id="evs_04_2069_evs_04_2067_row16225418185927"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_2069_evs_04_2067_p39190461185927"><a name="evs_04_2069_evs_04_2067_p39190461185927"></a><a name="evs_04_2069_evs_04_2067_p39190461185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2069_evs_04_2067_p20310744185927"><a name="evs_04_2069_evs_04_2067_p20310744185927"></a><a name="evs_04_2069_evs_04_2067_p20310744185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="evs_04_2069_evs_04_2067_p47699944185927"><a name="evs_04_2069_evs_04_2067_p47699944185927"></a><a name="evs_04_2069_evs_04_2067_p47699944185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2069_evs_04_2067_row38490285185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p30705403185927"><a name="evs_04_2069_evs_04_2067_p30705403185927"></a><a name="evs_04_2069_evs_04_2067_p30705403185927"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p4109689185927"><a name="evs_04_2069_evs_04_2067_p4109689185927"></a><a name="evs_04_2069_evs_04_2067_p4109689185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p53015590185927"><a name="evs_04_2069_evs_04_2067_p53015590185927"></a><a name="evs_04_2069_evs_04_2067_p53015590185927"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="evs_04_2069_evs_04_2067_row7378265185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p60768596185927"><a name="evs_04_2069_evs_04_2067_p60768596185927"></a><a name="evs_04_2069_evs_04_2067_p60768596185927"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p23309219185927"><a name="evs_04_2069_evs_04_2067_p23309219185927"></a><a name="evs_04_2069_evs_04_2067_p23309219185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p57795935185927"><a name="evs_04_2069_evs_04_2067_p57795935185927"></a><a name="evs_04_2069_evs_04_2067_p57795935185927"></a>Specifies the shortcut link marker name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="en-us_topic_0058762431_li5001921919316"></a>Parameters in the  **attachments**  field

    <a name="evs_04_2069_evs_04_2067_table6503386185927"></a>
    <table><thead align="left"><tr id="evs_04_2069_evs_04_2067_row1296819185927"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="evs_04_2069_evs_04_2067_p37933504185927"><a name="evs_04_2069_evs_04_2067_p37933504185927"></a><a name="evs_04_2069_evs_04_2067_p37933504185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="evs_04_2069_evs_04_2067_p52714965185927"><a name="evs_04_2069_evs_04_2067_p52714965185927"></a><a name="evs_04_2069_evs_04_2067_p52714965185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="evs_04_2069_evs_04_2067_p50913593185927"><a name="evs_04_2069_evs_04_2067_p50913593185927"></a><a name="evs_04_2069_evs_04_2067_p50913593185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2069_evs_04_2067_row30360408185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p43274016185927"><a name="evs_04_2069_evs_04_2067_p43274016185927"></a><a name="evs_04_2069_evs_04_2067_p43274016185927"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p15534392185927"><a name="evs_04_2069_evs_04_2067_p15534392185927"></a><a name="evs_04_2069_evs_04_2067_p15534392185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p49891705185927"><a name="evs_04_2069_evs_04_2067_p49891705185927"></a><a name="evs_04_2069_evs_04_2067_p49891705185927"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2069_evs_04_2067_row49550172185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p54141023185927"><a name="evs_04_2069_evs_04_2067_p54141023185927"></a><a name="evs_04_2069_evs_04_2067_p54141023185927"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p23346722185927"><a name="evs_04_2069_evs_04_2067_p23346722185927"></a><a name="evs_04_2069_evs_04_2067_p23346722185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p35416329185927"><a name="evs_04_2069_evs_04_2067_p35416329185927"></a><a name="evs_04_2069_evs_04_2067_p35416329185927"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="evs_04_2069_evs_04_2067_row35650386185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p2000176185927"><a name="evs_04_2069_evs_04_2067_p2000176185927"></a><a name="evs_04_2069_evs_04_2067_p2000176185927"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p27796542185927"><a name="evs_04_2069_evs_04_2067_p27796542185927"></a><a name="evs_04_2069_evs_04_2067_p27796542185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p38329099185927"><a name="evs_04_2069_evs_04_2067_p38329099185927"></a><a name="evs_04_2069_evs_04_2067_p38329099185927"></a>Specifies the time when the disk was attached.</p>
    <p id="evs_04_2069_evs_04_2067_p3414132514312"><a name="evs_04_2069_evs_04_2067_p3414132514312"></a><a name="evs_04_2069_evs_04_2067_p3414132514312"></a><span id="evs_04_2069_evs_04_2067_text7299269449"><a name="evs_04_2069_evs_04_2067_text7299269449"></a><a name="evs_04_2069_evs_04_2067_text7299269449"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2069_evs_04_2067_row9417574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p24626033185927"><a name="evs_04_2069_evs_04_2067_p24626033185927"></a><a name="evs_04_2069_evs_04_2067_p24626033185927"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p48551632185927"><a name="evs_04_2069_evs_04_2067_p48551632185927"></a><a name="evs_04_2069_evs_04_2067_p48551632185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p48591276185927"><a name="evs_04_2069_evs_04_2067_p48591276185927"></a><a name="evs_04_2069_evs_04_2067_p48591276185927"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2069_evs_04_2067_row34668301185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p56668991185927"><a name="evs_04_2069_evs_04_2067_p56668991185927"></a><a name="evs_04_2069_evs_04_2067_p56668991185927"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p26785545185927"><a name="evs_04_2069_evs_04_2067_p26785545185927"></a><a name="evs_04_2069_evs_04_2067_p26785545185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p48959624185927"><a name="evs_04_2069_evs_04_2067_p48959624185927"></a><a name="evs_04_2069_evs_04_2067_p48959624185927"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2069_evs_04_2067_row41070280185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p38358373185927"><a name="evs_04_2069_evs_04_2067_p38358373185927"></a><a name="evs_04_2069_evs_04_2067_p38358373185927"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p20020490185927"><a name="evs_04_2069_evs_04_2067_p20020490185927"></a><a name="evs_04_2069_evs_04_2067_p20020490185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p22392462185927"><a name="evs_04_2069_evs_04_2067_p22392462185927"></a><a name="evs_04_2069_evs_04_2067_p22392462185927"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="evs_04_2069_evs_04_2067_row205574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2069_evs_04_2067_p16651565185927"><a name="evs_04_2069_evs_04_2067_p16651565185927"></a><a name="evs_04_2069_evs_04_2067_p16651565185927"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2069_evs_04_2067_p6599487185927"><a name="evs_04_2069_evs_04_2067_p6599487185927"></a><a name="evs_04_2069_evs_04_2067_p6599487185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2069_evs_04_2067_p14021450185927"><a name="evs_04_2069_evs_04_2067_p14021450185927"></a><a name="evs_04_2069_evs_04_2067_p14021450185927"></a>Specifies the ID of the attached resource.</p>
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
        "count": 1, 
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
                "os-volume-replication:driver_data": null, 
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

