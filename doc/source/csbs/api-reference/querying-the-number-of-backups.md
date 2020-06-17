# Querying the Number of Backups<a name="EN-US_TOPIC_0059304233"></a>

## Function<a name="section18839399"></a>

This interface is used to query the number of backups. Filtering parameters are supported.

## URI<a name="section35336865"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/checkpoint\_items/count

-   Parameter description

    **Table  1**  Parameter description

    <a name="table30414041"></a>
    <table><thead align="left"><tr id="row16726860"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45356064"><a name="p45356064"></a><a name="p45356064"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p49962569"><a name="p49962569"></a><a name="p49962569"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p20436323"><a name="p20436323"></a><a name="p20436323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p44729494"><a name="p44729494"></a><a name="p44729494"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9761029"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p52445905"><a name="p52445905"></a><a name="p52445905"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p20259946"><a name="p20259946"></a><a name="p20259946"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p30442935"><a name="p30442935"></a><a name="p30442935"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section49596331"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table19269226"></a>
    <table><thead align="left"><tr id="row18926014"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p8549123210525"><a name="p8549123210525"></a><a name="p8549123210525"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p1054913213528"><a name="p1054913213528"></a><a name="p1054913213528"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p9549163212527"><a name="p9549163212527"></a><a name="p9549163212527"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p25491432105218"><a name="p25491432105218"></a><a name="p25491432105218"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4633676"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p39783513"><a name="p39783513"></a><a name="p39783513"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1239110"><a name="p1239110"></a><a name="p1239110"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p33259067"><a name="p33259067"></a><a name="p33259067"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p9629921"><a name="p9629921"></a><a name="p9629921"></a>Query based on field <strong id="b66521989"><a name="b66521989"></a><a name="b66521989"></a>status</strong> is supported.</p>
    <p id="p199923219255"><a name="p199923219255"></a><a name="p199923219255"></a>Value range: waiting_protect, protecting, available, waiting_restore, restoring, error, waiting_delete, deleting, and deleted</p>
    </td>
    </tr>
    <tr id="row8716248"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p34927510"><a name="p34927510"></a><a name="p34927510"></a>all_tenants</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p10556036"><a name="p10556036"></a><a name="p10556036"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p49732554"><a name="p49732554"></a><a name="p49732554"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1805073"><a name="p1805073"></a><a name="p1805073"></a>Whether to query the backup of all tenants. Only administrators can query the backup of all tenants.</p>
    </td>
    </tr>
    <tr id="row16245660"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p40830087"><a name="p40830087"></a><a name="p40830087"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p18902726"><a name="p18902726"></a><a name="p18902726"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p54725826"><a name="p54725826"></a><a name="p54725826"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p3606882"><a name="p3606882"></a><a name="p3606882"></a>Supports query by backup name.</p>
    </td>
    </tr>
    <tr id="row32461939"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12171397"><a name="p12171397"></a><a name="p12171397"></a>az</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p46359087"><a name="p46359087"></a><a name="p46359087"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p64098586"><a name="p64098586"></a><a name="p64098586"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p24602990"><a name="p24602990"></a><a name="p24602990"></a>AZ-based filtering is supported.</p>
    </td>
    </tr>
    <tr id="row20100318"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p17513057"><a name="p17513057"></a><a name="p17513057"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p9271521"><a name="p9271521"></a><a name="p9271521"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12795717"><a name="p12795717"></a><a name="p12795717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p29820150"><a name="p29820150"></a><a name="p29820150"></a>Filtering based on the backup object ID is supported.</p>
    </td>
    </tr>
    <tr id="row67054758"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62726324"><a name="p62726324"></a><a name="p62726324"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p47667523"><a name="p47667523"></a><a name="p47667523"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p35864187"><a name="p35864187"></a><a name="p35864187"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p19318019"><a name="p19318019"></a><a name="p19318019"></a>Filtering based on the backup object name is supported.</p>
    </td>
    </tr>
    <tr id="row39644444"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p57083424"><a name="p57083424"></a><a name="p57083424"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p60354632"><a name="p60354632"></a><a name="p60354632"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p56887037"><a name="p56887037"></a><a name="p56887037"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p44447270"><a name="p44447270"></a><a name="p44447270"></a>Filtering based on the backup time is supported. This is the backup start time. For example, 2017-04-15T04:25:38</p>
    </td>
    </tr>
    <tr id="row64481114"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p55587725"><a name="p55587725"></a><a name="p55587725"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p6311848"><a name="p6311848"></a><a name="p6311848"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p41497684"><a name="p41497684"></a><a name="p41497684"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p5869240"><a name="p5869240"></a><a name="p5869240"></a>Filtering based on the backup time is supported. This is the backup end time. For example, 2017-04-15T04:25:38</p>
    </td>
    </tr>
    <tr id="row52823167"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p50818155"><a name="p50818155"></a><a name="p50818155"></a>image_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p22629924"><a name="p22629924"></a><a name="p22629924"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p21084561"><a name="p21084561"></a><a name="p21084561"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p30127899"><a name="p30127899"></a><a name="p30127899"></a>Supports filtering by backup image type. This parameter can be used only when images are created using backups. The image type can be obtained from Image Management Service.</p>
    </td>
    </tr>
    <tr id="row2715638"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p18640117"><a name="p18640117"></a><a name="p18640117"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p33454533"><a name="p33454533"></a><a name="p33454533"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p25462670"><a name="p25462670"></a><a name="p25462670"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p49210359"><a name="p49210359"></a><a name="p49210359"></a>Filtering based on <strong id="b32903664"><a name="b32903664"></a><a name="b32903664"></a>policy_id</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row40240047"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p38218347"><a name="p38218347"></a><a name="p38218347"></a>ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p8678428"><a name="p8678428"></a><a name="p8678428"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p31864106"><a name="p31864106"></a><a name="p31864106"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p30855804"><a name="p30855804"></a><a name="p30855804"></a>Searching based on the VM's IP address is supported.</p>
    </td>
    </tr>
    <tr id="row65048224462"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p0237194023212"><a name="p0237194023212"></a><a name="p0237194023212"></a>checkpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p102371140173220"><a name="p102371140173220"></a><a name="p102371140173220"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p723774013213"><a name="p723774013213"></a><a name="p723774013213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p102222037356"><a name="p102222037356"></a><a name="p102222037356"></a>Filtering based on <strong id="b10115730"><a name="b10115730"></a><a name="b10115730"></a>checkpoint_id</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row2683195684117"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1673325924119"><a name="p1673325924119"></a><a name="p1673325924119"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1568425604112"><a name="p1568425604112"></a><a name="p1568425604112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1768412567412"><a name="p1768412567412"></a><a name="p1768412567412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p186845561418"><a name="p186845561418"></a><a name="p186845561418"></a>Type of the backup object. For example, <strong id="b156017511420"><a name="b156017511420"></a><a name="b156017511420"></a>OS::Nova::Server</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description

    None


-   Example request

    ```
    Querying the total number of backups:
    GET https://{endpoint}/v1/{project_id}/checkpoint_items/count
    Querying the number of backups with certain conditions:
    GET https://{endpoint}/v1/{project_id}/checkpoint_items/count?status=error
    ```


## Response<a name="section43713798"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table62483314"></a>
    <table><thead align="left"><tr id="row54452290"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p112211038175218"><a name="p112211038175218"></a><a name="p112211038175218"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p2221538105212"><a name="p2221538105212"></a><a name="p2221538105212"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p172216385524"><a name="p172216385524"></a><a name="p172216385524"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15429337"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41816781"><a name="p41816781"></a><a name="p41816781"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18869760"><a name="p18869760"></a><a name="p18869760"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p52055566"><a name="p52055566"></a><a name="p52055566"></a>Number of backups</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "count" : 10
    }
    ```


## Status Codes<a name="section57879868"></a>

-   Normal

    <a name="table22031562"></a>
    <table><thead align="left"><tr id="row36417532"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p64138952"><a name="p64138952"></a><a name="p64138952"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p27872649"><a name="p27872649"></a><a name="p27872649"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43092135"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p802057"><a name="p802057"></a><a name="p802057"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p64966680"><a name="p64966680"></a><a name="p64966680"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table27809723"></a>
    <table><thead align="left"><tr id="row49575386"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p56183344"><a name="p56183344"></a><a name="p56183344"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p54557022"><a name="p54557022"></a><a name="p54557022"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57042701"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p57056101"><a name="p57056101"></a><a name="p57056101"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58141453"><a name="p58141453"></a><a name="p58141453"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row53511030"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p39426202"><a name="p39426202"></a><a name="p39426202"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p39405794"><a name="p39405794"></a><a name="p39405794"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row19107831"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p4230513"><a name="p4230513"></a><a name="p4230513"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p7127300"><a name="p7127300"></a><a name="p7127300"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row64145702"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p28419344"><a name="p28419344"></a><a name="p28419344"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p20265510"><a name="p20265510"></a><a name="p20265510"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row48171870"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p9607394"><a name="p9607394"></a><a name="p9607394"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p40001479"><a name="p40001479"></a><a name="p40001479"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row24468997"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p35831774"><a name="p35831774"></a><a name="p35831774"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p16692587"><a name="p16692587"></a><a name="p16692587"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

