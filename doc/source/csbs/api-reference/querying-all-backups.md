# Querying All Backups<a name="EN-US_TOPIC_0059304235"></a>

## Function<a name="section43284795"></a>

This API is used to query all backups. Filtering parameters are supported.

## URI<a name="section54018842"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/checkpoint\_items

-   Parameter description

    **Table  1**  Parameter description

    <a name="table9732370"></a>
    <table><thead align="left"><tr id="row34001014"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45356064"><a name="p45356064"></a><a name="p45356064"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p49962569"><a name="p49962569"></a><a name="p49962569"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p20436323"><a name="p20436323"></a><a name="p20436323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p44729494"><a name="p44729494"></a><a name="p44729494"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19711542"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p53131054"><a name="p53131054"></a><a name="p53131054"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p8648094"><a name="p8648094"></a><a name="p8648094"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p29407023"><a name="p29407023"></a><a name="p29407023"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section16407531"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table54172341"></a>
    <table><thead align="left"><tr id="row56350203"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55933134"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p34289996"><a name="p34289996"></a><a name="p34289996"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p26026295"><a name="p26026295"></a><a name="p26026295"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p27755126"><a name="p27755126"></a><a name="p27755126"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p33572722"><a name="p33572722"></a><a name="p33572722"></a>Query based on field <strong id="b51160835"><a name="b51160835"></a><a name="b51160835"></a>status</strong> is supported.</p>
    <p id="p199923219255"><a name="p199923219255"></a><a name="p199923219255"></a>Value range: waiting_protect, protecting, available, waiting_restore, restoring, error, waiting_delete, deleting, and deleted</p>
    </td>
    </tr>
    <tr id="row33719042"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p46887843"><a name="p46887843"></a><a name="p46887843"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p39818933"><a name="p39818933"></a><a name="p39818933"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p4108127"><a name="p4108127"></a><a name="p4108127"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p64322890"><a name="p64322890"></a><a name="p64322890"></a>Number of resources displayed per page. The value must be a positive integer. The value defaults to <strong id="b58471720141720"><a name="b58471720141720"></a><a name="b58471720141720"></a>1000</strong>.</p>
    </td>
    </tr>
    <tr id="row42035103"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49400206"><a name="p49400206"></a><a name="p49400206"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p41993745"><a name="p41993745"></a><a name="p41993745"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p46050193"><a name="p46050193"></a><a name="p46050193"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p39078133"><a name="p39078133"></a><a name="p39078133"></a>ID of the last record displayed on the previous page</p>
    </td>
    </tr>
    <tr id="row16158880"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p33800918"><a name="p33800918"></a><a name="p33800918"></a>sort</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p53519844"><a name="p53519844"></a><a name="p53519844"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p40140147"><a name="p40140147"></a><a name="p40140147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p5660133974020"><a name="p5660133974020"></a><a name="p5660133974020"></a>A group of properties separated by commas (,) and sorting directions. The value format is &lt;key1&gt;[:&lt;direction&gt;],&lt;key2&gt;[:&lt;direction&gt;], where the value of direction is <strong id="b1273581669173844"><a name="b1273581669173844"></a><a name="b1273581669173844"></a>asc</strong> (in ascending order) or <strong id="b421059629173844"><a name="b421059629173844"></a><a name="b421059629173844"></a>desc</strong> (in descending order). If the parameter direction is not specified, the default sorting direction is <strong id="b27144506173844"><a name="b27144506173844"></a><a name="b27144506173844"></a>desc</strong>. The value of <strong id="b788002962173844"><a name="b788002962173844"></a><a name="b788002962173844"></a>sort</strong> contains a maximum of 255 characters. Enumeration values of the key are as follows: <strong id="b1117032810303"><a name="b1117032810303"></a><a name="b1117032810303"></a>created_at</strong>, <strong id="b794232193019"><a name="b794232193019"></a><a name="b794232193019"></a>updated_at</strong>, <strong id="b15830183423015"><a name="b15830183423015"></a><a name="b15830183423015"></a>name</strong>, <strong id="b972153883013"><a name="b972153883013"></a><a name="b972153883013"></a>status</strong>, <strong id="b678910419306"><a name="b678910419306"></a><a name="b678910419306"></a>protected_at</strong>, and <strong id="b10398246133017"><a name="b10398246133017"></a><a name="b10398246133017"></a> id</strong>.</p>
    </td>
    </tr>
    <tr id="row2703109"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p17625292"><a name="p17625292"></a><a name="p17625292"></a>all_tenants</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p18362576"><a name="p18362576"></a><a name="p18362576"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p10973688"><a name="p10973688"></a><a name="p10973688"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p16453549"><a name="p16453549"></a><a name="p16453549"></a>Whether to query the backup of all tenants. Only administrators can query the backup of all tenants.</p>
    </td>
    </tr>
    <tr id="row13864215"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49259658"><a name="p49259658"></a><a name="p49259658"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p30609341"><a name="p30609341"></a><a name="p30609341"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p63437528"><a name="p63437528"></a><a name="p63437528"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p38166148"><a name="p38166148"></a><a name="p38166148"></a>Query based on field <strong id="b18388109"><a name="b18388109"></a><a name="b18388109"></a>name</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row7951016"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p40052527"><a name="p40052527"></a><a name="p40052527"></a>az</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p23029275"><a name="p23029275"></a><a name="p23029275"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p53432020"><a name="p53432020"></a><a name="p53432020"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p33026369"><a name="p33026369"></a><a name="p33026369"></a>Filtering based on the backup AZ is supported.</p>
    </td>
    </tr>
    <tr id="row28801871"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p51250214"><a name="p51250214"></a><a name="p51250214"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p57626661"><a name="p57626661"></a><a name="p57626661"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p37247989"><a name="p37247989"></a><a name="p37247989"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p64297150"><a name="p64297150"></a><a name="p64297150"></a>Filtering based on the backup object ID is supported.</p>
    </td>
    </tr>
    <tr id="row41803439"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p30635359"><a name="p30635359"></a><a name="p30635359"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p65544987"><a name="p65544987"></a><a name="p65544987"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p7543756"><a name="p7543756"></a><a name="p7543756"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p7064538"><a name="p7064538"></a><a name="p7064538"></a>Filtering based on the backup object name is supported.</p>
    </td>
    </tr>
    <tr id="row63580847"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49774995"><a name="p49774995"></a><a name="p49774995"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p5242758"><a name="p5242758"></a><a name="p5242758"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p22010291"><a name="p22010291"></a><a name="p22010291"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p38003136"><a name="p38003136"></a><a name="p38003136"></a>Filtering based on the backup start time is supported.</p>
    <p id="p2062445410316"><a name="p2062445410316"></a><a name="p2062445410316"></a>For example: <strong id="b1084273518171"><a name="b1084273518171"></a><a name="b1084273518171"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row6483906"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p55434371"><a name="p55434371"></a><a name="p55434371"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p60999032"><a name="p60999032"></a><a name="p60999032"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p41974537"><a name="p41974537"></a><a name="p41974537"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p44494368"><a name="p44494368"></a><a name="p44494368"></a>Filtering based on the backup end time is supported.</p>
    <p id="p12111456134"><a name="p12111456134"></a><a name="p12111456134"></a>For example: <strong id="b377520495176"><a name="b377520495176"></a><a name="b377520495176"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row64904992"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p22812984"><a name="p22812984"></a><a name="p22812984"></a>image_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p35912392"><a name="p35912392"></a><a name="p35912392"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p23222649"><a name="p23222649"></a><a name="p23222649"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1986418"><a name="p1986418"></a><a name="p1986418"></a>Supports filtering by image type, for example, <strong id="b3664184617190"><a name="b3664184617190"></a><a name="b3664184617190"></a>backup</strong>.</p>
    </td>
    </tr>
    <tr id="row17877770"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p38813251"><a name="p38813251"></a><a name="p38813251"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p56865625"><a name="p56865625"></a><a name="p56865625"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p42712883"><a name="p42712883"></a><a name="p42712883"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p37191481"><a name="p37191481"></a><a name="p37191481"></a>Filtering based on <strong id="b10115730"><a name="b10115730"></a><a name="b10115730"></a>policy_id</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row21812782"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p22004936"><a name="p22004936"></a><a name="p22004936"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p37569382"><a name="p37569382"></a><a name="p37569382"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p23221105"><a name="p23221105"></a><a name="p23221105"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1861328"><a name="p1861328"></a><a name="p1861328"></a>Offset value, which is a positive integer.</p>
    </td>
    </tr>
    <tr id="row8338346032"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p0237194023212"><a name="p0237194023212"></a><a name="p0237194023212"></a>checkpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p102371140173220"><a name="p102371140173220"></a><a name="p102371140173220"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p723774013213"><a name="p723774013213"></a><a name="p723774013213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p102222037356"><a name="p102222037356"></a><a name="p102222037356"></a>Filtering based on <strong id="b1539558292"><a name="b1539558292"></a><a name="b1539558292"></a>checkpoint_id</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row207191443979"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1673325924119"><a name="p1673325924119"></a><a name="p1673325924119"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1568425604112"><a name="p1568425604112"></a><a name="p1568425604112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1768412567412"><a name="p1768412567412"></a><a name="p1768412567412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p186845561418"><a name="p186845561418"></a><a name="p186845561418"></a>Type of the backup object. For example, <strong id="b613422516815"><a name="b613422516815"></a><a name="b613422516815"></a>OS::Nova::Server</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description

    None


-   Example request

    ```
    Querying all backups:
    GET https://{endpoint}/v1/{project_id}/checkpoint_items
    Querying backups with specified parameters:
    GET https://{endpoint}/v1/{project_id}/checkpoint_items?name=backup&status=error&limit=2
    ```


## Response<a name="section13450057"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table50382601"></a>
    <table><thead align="left"><tr id="row21078891"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p539510301635"><a name="p539510301635"></a><a name="p539510301635"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p24112301632"><a name="p24112301632"></a><a name="p24112301632"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p1641119303319"><a name="p1641119303319"></a><a name="p1641119303319"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64205574"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33269037"><a name="p33269037"></a><a name="p33269037"></a>checkpoint_items</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40126246"><a name="p40126246"></a><a name="p40126246"></a>List&lt;checkpoint_item&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p29000522"><a name="p29000522"></a><a name="p29000522"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **checkpoint\_item**

    **Table  4**  Parameter description of field  **checkpoint\_item**

    <a name="table232082"></a>
    <table><thead align="left"><tr id="row63549063"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p14665391317"><a name="p14665391317"></a><a name="p14665391317"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p108315399312"><a name="p108315399312"></a><a name="p108315399312"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p149815397313"><a name="p149815397313"></a><a name="p149815397313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17945957"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p44336387"><a name="p44336387"></a><a name="p44336387"></a>checkpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p41219056"><a name="p41219056"></a><a name="p41219056"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50409231"><a name="p50409231"></a><a name="p50409231"></a>Backup record ID</p>
    </td>
    </tr>
    <tr id="row51029902"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39781373"><a name="p39781373"></a><a name="p39781373"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19218425"><a name="p19218425"></a><a name="p19218425"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13188565"><a name="p13188565"></a><a name="p13188565"></a>Creation time, for example, <strong id="b573253111915"><a name="b573253111915"></a><a name="b573253111915"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row51588228"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17896926"><a name="p17896926"></a><a name="p17896926"></a>extend_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48333181"><a name="p48333181"></a><a name="p48333181"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22673552"><a name="p22673552"></a><a name="p22673552"></a>Extension information</p>
    </td>
    </tr>
    <tr id="row2735384"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20239560"><a name="p20239560"></a><a name="p20239560"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50421821"><a name="p50421821"></a><a name="p50421821"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57635666"><a name="p57635666"></a><a name="p57635666"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row48958947"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6251810"><a name="p6251810"></a><a name="p6251810"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14615362"><a name="p14615362"></a><a name="p14615362"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42993650"><a name="p42993650"></a><a name="p42993650"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row51398535"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2531807"><a name="p2531807"></a><a name="p2531807"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p35300637"><a name="p35300637"></a><a name="p35300637"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p40779347"><a name="p40779347"></a><a name="p40779347"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row31469804"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66026167"><a name="p66026167"></a><a name="p66026167"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9968167"><a name="p9968167"></a><a name="p9968167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p382654517414"><a name="p382654517414"></a><a name="p382654517414"></a>Backup status</p>
    <p id="p59971111165855"><a name="p59971111165855"></a><a name="p59971111165855"></a>The value can be <strong id="b65069390"><a name="b65069390"></a><a name="b65069390"></a>waiting_protect</strong>, <strong id="b48753600"><a name="b48753600"></a><a name="b48753600"></a>protecting</strong>, <strong id="b36129223"><a name="b36129223"></a><a name="b36129223"></a>available</strong>, <strong id="b56727555"><a name="b56727555"></a><a name="b56727555"></a>waiting_restore</strong>, <strong id="b40785949"><a name="b40785949"></a><a name="b40785949"></a>restoring</strong>, <strong id="b31529222"><a name="b31529222"></a><a name="b31529222"></a>error</strong>, <strong id="b15327543"><a name="b15327543"></a><a name="b15327543"></a>waiting_delete</strong>, <strong id="b3730161"><a name="b3730161"></a><a name="b3730161"></a>deleting</strong>, or <strong id="b1867431570153148"><a name="b1867431570153148"></a><a name="b1867431570153148"></a>deleted</strong>.</p>
    </td>
    </tr>
    <tr id="row37115802"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p53589960"><a name="p53589960"></a><a name="p53589960"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p20389589"><a name="p20389589"></a><a name="p20389589"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p40944004"><a name="p40944004"></a><a name="p40944004"></a>Modification time, for example, <strong id="b12601656181910"><a name="b12601656181910"></a><a name="b12601656181910"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row32951723"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p51843882"><a name="p51843882"></a><a name="p51843882"></a>backup_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p39989318"><a name="p39989318"></a><a name="p39989318"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p17909298"><a name="p17909298"></a><a name="p17909298"></a>VM metadata</p>
    </td>
    </tr>
    <tr id="row7783192115616"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2052319231152"><a name="p2052319231152"></a><a name="p2052319231152"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25231123550"><a name="p25231123550"></a><a name="p25231123550"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1452312318520"><a name="p1452312318520"></a><a name="p1452312318520"></a>Backup description</p>
    </td>
    </tr>
    <tr id="row20983254114410"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6983254204415"><a name="p6983254204415"></a><a name="p6983254204415"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1898312541445"><a name="p1898312541445"></a><a name="p1898312541445"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p7831173883410"><a name="p7831173883410"></a><a name="p7831173883410"></a>List of backup tags</p>
    <p id="p19965152115313"><a name="p19965152115313"></a><a name="p19965152115313"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    <tr id="row20439143618916"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p878984110915"><a name="p878984110915"></a><a name="p878984110915"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p17801341990"><a name="p17801341990"></a><a name="p17801341990"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p168078411097"><a name="p168078411097"></a><a name="p168078411097"></a>Type of backup objects</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **extend\_info**

    **Table  5**  Parameter description of field  **extend\_info**

    <a name="table41367059"></a>
    <table><thead align="left"><tr id="row33294357"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1370815313310"><a name="p1370815313310"></a><a name="p1370815313310"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p97232053738"><a name="p97232053738"></a><a name="p97232053738"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p1273917533317"><a name="p1273917533317"></a><a name="p1273917533317"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58515256"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p42115335"><a name="p42115335"></a><a name="p42115335"></a>auto_trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p31525703"><a name="p31525703"></a><a name="p31525703"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p49029033"><a name="p49029033"></a><a name="p49029033"></a>Whether automatic trigger is enabled</p>
    </td>
    </tr>
    <tr id="row31006148"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p28470060"><a name="p28470060"></a><a name="p28470060"></a>average_speed</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28099466"><a name="p28099466"></a><a name="p28099466"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57386915"><a name="p57386915"></a><a name="p57386915"></a>Average rate. The unit is kb/s</p>
    </td>
    </tr>
    <tr id="row16307537"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45842092"><a name="p45842092"></a><a name="p45842092"></a>copy_from</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55149628"><a name="p55149628"></a><a name="p55149628"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45970441"><a name="p45970441"></a><a name="p45970441"></a>The destination region of a backup replication. The default value is empty.</p>
    </td>
    </tr>
    <tr id="row5869903"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p5700168"><a name="p5700168"></a><a name="p5700168"></a>copy_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19168703"><a name="p19168703"></a><a name="p19168703"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p112911849103111"><a name="p112911849103111"></a><a name="p112911849103111"></a>Backup replication status. The default value is <strong id="b1343182015820"><a name="b1343182015820"></a><a name="b1343182015820"></a>na</strong>.</p>
    <p id="p173113381512"><a name="p173113381512"></a><a name="p173113381512"></a>Possible values are <strong id="b56691235173920"><a name="b56691235173920"></a><a name="b56691235173920"></a>na</strong>, <strong id="b29522398393"><a name="b29522398393"></a><a name="b29522398393"></a>replica_copy</strong>, <strong id="b1698920434398"><a name="b1698920434398"></a><a name="b1698920434398"></a>copying</strong>, <strong id="b1773412471397"><a name="b1773412471397"></a><a name="b1773412471397"></a>success</strong>, or <strong id="b16211051173910"><a name="b16211051173910"></a><a name="b16211051173910"></a>fail</strong>.</p>
    </td>
    </tr>
    <tr id="row3851720"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43553879"><a name="p43553879"></a><a name="p43553879"></a>fail_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7459475"><a name="p7459475"></a><a name="p7459475"></a>fail_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45042167"><a name="p45042167"></a><a name="p45042167"></a>Error code</p>
    </td>
    </tr>
    <tr id="row2139406"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39074184"><a name="p39074184"></a><a name="p39074184"></a>fail_op</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9865575"><a name="p9865575"></a><a name="p9865575"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p30981435"><a name="p30981435"></a><a name="p30981435"></a>Type of the failed operation</p>
    <p id="p10397463"><a name="p10397463"></a><a name="p10397463"></a>Enum: [backup, restore, delete]</p>
    </td>
    </tr>
    <tr id="row35092999"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23960660"><a name="p23960660"></a><a name="p23960660"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p36932527"><a name="p36932527"></a><a name="p36932527"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p31874881"><a name="p31874881"></a><a name="p31874881"></a>Failure cause</p>
    </td>
    </tr>
    <tr id="row13158141"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p59176532"><a name="p59176532"></a><a name="p59176532"></a>image_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p32448429"><a name="p32448429"></a><a name="p32448429"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50734894"><a name="p50734894"></a><a name="p50734894"></a>Backup type. For example, <strong id="b1635611217819"><a name="b1635611217819"></a><a name="b1635611217819"></a>backup</strong></p>
    </td>
    </tr>
    <tr id="row32585229"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p22157894"><a name="p22157894"></a><a name="p22157894"></a>incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p20149171"><a name="p20149171"></a><a name="p20149171"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1561311"><a name="p1561311"></a><a name="p1561311"></a>Whether the backup is an enhanced backup</p>
    </td>
    </tr>
    <tr id="row59013479"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p15362477"><a name="p15362477"></a><a name="p15362477"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p62812896"><a name="p62812896"></a><a name="p62812896"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p10774429"><a name="p10774429"></a><a name="p10774429"></a>Replication progress. The value is an integer ranging from 0 to 100.</p>
    </td>
    </tr>
    <tr id="row22356484"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66044754"><a name="p66044754"></a><a name="p66044754"></a>resource_az</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64805535"><a name="p64805535"></a><a name="p64805535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p55296057"><a name="p55296057"></a><a name="p55296057"></a>AZ to which the backup resource belongs</p>
    </td>
    </tr>
    <tr id="row65703909"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20416388"><a name="p20416388"></a><a name="p20416388"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2631392"><a name="p2631392"></a><a name="p2631392"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39494476"><a name="p39494476"></a><a name="p39494476"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row19291121584417"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p149812204222"><a name="p149812204222"></a><a name="p149812204222"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p998142020221"><a name="p998142020221"></a><a name="p998142020221"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p09822022216"><a name="p09822022216"></a><a name="p09822022216"></a>Type of the backup object. For example, <strong id="b1948758436"><a name="b1948758436"></a><a name="b1948758436"></a>OS::Nova::Server</strong></p>
    </td>
    </tr>
    <tr id="row39236691"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24055389"><a name="p24055389"></a><a name="p24055389"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54472796"><a name="p54472796"></a><a name="p54472796"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15817592"><a name="p15817592"></a><a name="p15817592"></a>Backup capacity. The unit is MB.</p>
    </td>
    </tr>
    <tr id="row49329695"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p36282367"><a name="p36282367"></a><a name="p36282367"></a>space_saving_ratio</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p13470932"><a name="p13470932"></a><a name="p13470932"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p16867749"><a name="p16867749"></a><a name="p16867749"></a>Space saving rate</p>
    </td>
    </tr>
    <tr id="row22415330"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p3702481"><a name="p3702481"></a><a name="p3702481"></a>volume_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p65683793"><a name="p65683793"></a><a name="p65683793"></a>List&lt;volume_backup&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p30484803"><a name="p30484803"></a><a name="p30484803"></a>Volume backup list</p>
    </td>
    </tr>
    <tr id="row34865214"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p5510086"><a name="p5510086"></a><a name="p5510086"></a>finished_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p47109732"><a name="p47109732"></a><a name="p47109732"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p106125"><a name="p106125"></a><a name="p106125"></a>Backup completion time, for example, <strong id="b11101130132017"><a name="b11101130132017"></a><a name="b11101130132017"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row101519181848"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14691120181216"><a name="p14691120181216"></a><a name="p14691120181216"></a>supported_restore_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p204691920121214"><a name="p204691920121214"></a><a name="p204691920121214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18728201715"><a name="p18728201715"></a><a name="p18728201715"></a>Restoration mode. Possible values are <strong id="b46774915241"><a name="b46774915241"></a><a name="b46774915241"></a>na</strong>, <strong id="b8823182419241"><a name="b8823182419241"></a><a name="b8823182419241"></a>snapshot</strong>, and <strong id="b667817919244"><a name="b667817919244"></a><a name="b667817919244"></a>backup</strong>.</p>
    <p id="p8166816173"><a name="p8166816173"></a><a name="p8166816173"></a><strong id="b84235270610831"><a name="b84235270610831"></a><a name="b84235270610831"></a>backup</strong>: Data is restored from backups of the EVS disks of the server.</p>
    <p id="p11211554424"><a name="p11211554424"></a><a name="p11211554424"></a><strong id="b84235270610912"><a name="b84235270610912"></a><a name="b84235270610912"></a>na</strong>: Restoration is not supported.</p>
    </td>
    </tr>
    <tr id="row173232391943"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p76063254014"><a name="p76063254014"></a><a name="p76063254014"></a>os_images_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p860103213408"><a name="p860103213408"></a><a name="p860103213408"></a>List&lt;image_data&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18603325403"><a name="p18603325403"></a><a name="p18603325403"></a>Image data. This parameter has a value if an image has been created for the VM.</p>
    </td>
    </tr>
    <tr id="row18629158185118"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p19986193041010"><a name="p19986193041010"></a><a name="p19986193041010"></a>support_lld</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p898783012102"><a name="p898783012102"></a><a name="p898783012102"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14987330181013"><a name="p14987330181013"></a><a name="p14987330181013"></a>Whether to allow lazyloading for fast restoration</p>
    </td>
    </tr>
    <tr id="row11469931161119"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p189025313106"><a name="p189025313106"></a><a name="p189025313106"></a>taskid</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p11902123114103"><a name="p11902123114103"></a><a name="p11902123114103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p690212311100"><a name="p690212311100"></a><a name="p690212311100"></a>Job ID</p>
    </td>
    </tr>
    <tr id="row1546853141111"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p990283111013"><a name="p990283111013"></a><a name="p990283111013"></a>hypervisor_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p11902163113108"><a name="p11902163113108"></a><a name="p11902163113108"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p17903133181016"><a name="p17903133181016"></a><a name="p17903133181016"></a>Virtualization type</p>
    <p id="p4573183054816"><a name="p4573183054816"></a><a name="p4573183054816"></a>The value is fixed at <strong id="b1018082394510"><a name="b1018082394510"></a><a name="b1018082394510"></a>QEMU</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **image\_data**

    **Table  6**  Parameter description of field  **image\_data**

    <a name="table17665422205719"></a>
    <table><thead align="left"><tr id="row156851122175719"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p117297291851"><a name="p117297291851"></a><a name="p117297291851"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p974518291653"><a name="p974518291653"></a><a name="p974518291653"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p147456292511"><a name="p147456292511"></a><a name="p147456292511"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6718112212576"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p11724172211573"><a name="p11724172211573"></a><a name="p11724172211573"></a>image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p173310227573"><a name="p173310227573"></a><a name="p173310227573"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p3739112205719"><a name="p3739112205719"></a><a name="p3739112205719"></a>Image ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **backup\_data**

    **Table  7**  Parameter description of field  **backup\_data**

    <a name="table50636020"></a>
    <table><thead align="left"><tr id="row60939915"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p930615331254"><a name="p930615331254"></a><a name="p930615331254"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p2032320338513"><a name="p2032320338513"></a><a name="p2032320338513"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p143394331455"><a name="p143394331455"></a><a name="p143394331455"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13239523"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65768467"><a name="p65768467"></a><a name="p65768467"></a>__openstack_region_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64029957"><a name="p64029957"></a><a name="p64029957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p19043990"><a name="p19043990"></a><a name="p19043990"></a>Name of the AZ where the server is located. If this parameter is left blank, such information about the server has not been obtained.</p>
    </td>
    </tr>
    <tr id="row37178185"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p58643034"><a name="p58643034"></a><a name="p58643034"></a>cloudservicetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p21835130"><a name="p21835130"></a><a name="p21835130"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23815129"><a name="p23815129"></a><a name="p23815129"></a>Server type</p>
    </td>
    </tr>
    <tr id="row13009572"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p47142449"><a name="p47142449"></a><a name="p47142449"></a>disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p63964947"><a name="p63964947"></a><a name="p63964947"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13778233"><a name="p13778233"></a><a name="p13778233"></a>System disk size corresponding to the server specifications</p>
    </td>
    </tr>
    <tr id="row56895238"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45111543"><a name="p45111543"></a><a name="p45111543"></a>imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26749136"><a name="p26749136"></a><a name="p26749136"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p41960885174133"><a name="p41960885174133"></a><a name="p41960885174133"></a>Image type</p>
    <p id="p47973354174135"><a name="p47973354174135"></a><a name="p47973354174135"></a>The value can be:</p>
    <p id="p51968304174137"><a name="p51968304174137"></a><a name="p51968304174137"></a><strong id="b35494469174137"><a name="b35494469174137"></a><a name="b35494469174137"></a>gold</strong>: public image</p>
    <p id="p3838096174139"><a name="p3838096174139"></a><a name="p3838096174139"></a><strong id="b46508891174139"><a name="b46508891174139"></a><a name="b46508891174139"></a>private</strong>: private image</p>
    <p id="p46394954165855"><a name="p46394954165855"></a><a name="p46394954165855"></a><strong id="b51449256417358"><a name="b51449256417358"></a><a name="b51449256417358"></a>market</strong>: market image</p>
    </td>
    </tr>
    <tr id="row11406459"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p51507987"><a name="p51507987"></a><a name="p51507987"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27451615134318"><a name="p27451615134318"></a><a name="p27451615134318"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p19278919"><a name="p19278919"></a><a name="p19278919"></a>Memory size of the server, in MB</p>
    </td>
    </tr>
    <tr id="row39292544"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p28579467"><a name="p28579467"></a><a name="p28579467"></a>vcpus</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p121076101718"><a name="p121076101718"></a><a name="p121076101718"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p21386544"><a name="p21386544"></a><a name="p21386544"></a>CPU cores corresponding to the server</p>
    </td>
    </tr>
    <tr id="row58261174"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21534687"><a name="p21534687"></a><a name="p21534687"></a>eip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24926390"><a name="p24926390"></a><a name="p24926390"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5771700"><a name="p5771700"></a><a name="p5771700"></a>Elastic IP address of the server. If this parameter is left blank, such information about the server has not been obtained.</p>
    </td>
    </tr>
    <tr id="row51945304"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p46820120"><a name="p46820120"></a><a name="p46820120"></a>private_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p29541418"><a name="p29541418"></a><a name="p29541418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p44044619"><a name="p44044619"></a><a name="p44044619"></a>Internal IP address of the server. If this parameter is left blank, such information about the server has not been obtained.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **fail\_code**

    **Table  8**  Parameter description of field  **fail\_code**

    <a name="table118451181322"></a>
    <table><thead align="left"><tr id="row1484515185212"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1587015571256"><a name="p1587015571256"></a><a name="p1587015571256"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1287025718518"><a name="p1287025718518"></a><a name="p1287025718518"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p13884757859"><a name="p13884757859"></a><a name="p13884757859"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row158454187210"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p384561819218"><a name="p384561819218"></a><a name="p384561819218"></a>Code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p178461018229"><a name="p178461018229"></a><a name="p178461018229"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1884661812215"><a name="p1884661812215"></a><a name="p1884661812215"></a>Error code</p>
    </td>
    </tr>
    <tr id="row28461718021"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p118469186215"><a name="p118469186215"></a><a name="p118469186215"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p0846418722"><a name="p0846418722"></a><a name="p0846418722"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p118461187213"><a name="p118461187213"></a><a name="p118461187213"></a>Error description</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field** volume\_backup**

    **Table  9**  Parameter description of field** volume\_backup**

    <a name="table10844381"></a>
    <table><thead align="left"><tr id="row32958070"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p108851081268"><a name="p108851081268"></a><a name="p108851081268"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.28%" id="mcps1.2.4.1.2"><p id="p119017811615"><a name="p119017811615"></a><a name="p119017811615"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p179011488613"><a name="p179011488613"></a><a name="p179011488613"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36942067"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p56836906"><a name="p56836906"></a><a name="p56836906"></a>average_speed</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p50095482"><a name="p50095482"></a><a name="p50095482"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p31202271"><a name="p31202271"></a><a name="p31202271"></a>Average rate, in MB/s</p>
    </td>
    </tr>
    <tr id="row65326043"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p63660086"><a name="p63660086"></a><a name="p63660086"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p55367277"><a name="p55367277"></a><a name="p55367277"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p55564443"><a name="p55564443"></a><a name="p55564443"></a>Whether the disk is bootable</p>
    <p id="p16852144118620"><a name="p16852144118620"></a><a name="p16852144118620"></a>The value can be <strong id="b94611340174514"><a name="b94611340174514"></a><a name="b94611340174514"></a>true</strong> or <strong id="b946264017457"><a name="b946264017457"></a><a name="b946264017457"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row58725572"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p59150862"><a name="p59150862"></a><a name="p59150862"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p65355792"><a name="p65355792"></a><a name="p65355792"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p59327767"><a name="p59327767"></a><a name="p59327767"></a>Cinder backup ID</p>
    </td>
    </tr>
    <tr id="row64187861"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p31834275"><a name="p31834275"></a><a name="p31834275"></a>image_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p21894647"><a name="p21894647"></a><a name="p21894647"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p28635982"><a name="p28635982"></a><a name="p28635982"></a>Backup set type: backup</p>
    <p id="p56397249"><a name="p56397249"></a><a name="p56397249"></a>Enum:[ backup]</p>
    </td>
    </tr>
    <tr id="row37813197"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p42970141"><a name="p42970141"></a><a name="p42970141"></a>incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p2762063"><a name="p2762063"></a><a name="p2762063"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p22400512"><a name="p22400512"></a><a name="p22400512"></a>Whether incremental backup is used</p>
    </td>
    </tr>
    <tr id="row278019"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p22519604"><a name="p22519604"></a><a name="p22519604"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p44518548"><a name="p44518548"></a><a name="p44518548"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p49232659"><a name="p49232659"></a><a name="p49232659"></a>EVS disk backup name</p>
    </td>
    </tr>
    <tr id="row40440750"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p54475355"><a name="p54475355"></a><a name="p54475355"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p58105725"><a name="p58105725"></a><a name="p58105725"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p8943299"><a name="p8943299"></a><a name="p8943299"></a>Accumulated size (MB) of backups</p>
    </td>
    </tr>
    <tr id="row13380832"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p10105585"><a name="p10105585"></a><a name="p10105585"></a>source_volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p66300170"><a name="p66300170"></a><a name="p66300170"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1604705"><a name="p1604705"></a><a name="p1604705"></a>Source disk ID</p>
    </td>
    </tr>
    <tr id="row14442352"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p28979873"><a name="p28979873"></a><a name="p28979873"></a>source_volume_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p17538436"><a name="p17538436"></a><a name="p17538436"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p11327239"><a name="p11327239"></a><a name="p11327239"></a>Source volume size in GB</p>
    </td>
    </tr>
    <tr id="row34836289"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p3167131"><a name="p3167131"></a><a name="p3167131"></a>space_saving_ratio</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p42909373"><a name="p42909373"></a><a name="p42909373"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p53107156"><a name="p53107156"></a><a name="p53107156"></a>Space saving rate</p>
    </td>
    </tr>
    <tr id="row8202362"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p60411608"><a name="p60411608"></a><a name="p60411608"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p15610444"><a name="p15610444"></a><a name="p15610444"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p56486451"><a name="p56486451"></a><a name="p56486451"></a>Status</p>
    </td>
    </tr>
    <tr id="row38616014"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p40889433"><a name="p40889433"></a><a name="p40889433"></a>source_volume_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p41441748"><a name="p41441748"></a><a name="p41441748"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1338388"><a name="p1338388"></a><a name="p1338388"></a>Source volume name</p>
    </td>
    </tr>
    <tr id="row418413316516"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p18739530979"><a name="p18739530979"></a><a name="p18739530979"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p773917301975"><a name="p773917301975"></a><a name="p773917301975"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p3739143011716"><a name="p3739143011716"></a><a name="p3739143011716"></a>ID of the snapshot from which the backup is generated</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  10**  Parameter description of field  **resource\_tag**

    <a name="table1431115645119"></a>
    <table><thead align="left"><tr id="row4339106155119"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p178211322063"><a name="p178211322063"></a><a name="p178211322063"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p998173214613"><a name="p998173214613"></a><a name="p998173214613"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p15986328613"><a name="p15986328613"></a><a name="p15986328613"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63768665110"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p10380567512"><a name="p10380567512"></a><a name="p10380567512"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1739414617517"><a name="p1739414617517"></a><a name="p1739414617517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13925135105714"><a name="p13925135105714"></a><a name="p13925135105714"></a>Tag key</p>
    <p id="p7327206587"><a name="p7327206587"></a><a name="p7327206587"></a>It consists of up to 36 characters.</p>
    <p id="p145821075819"><a name="p145821075819"></a><a name="p145821075819"></a>It cannot be an empty string.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1116111556513"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1816118554511"><a name="p1816118554511"></a><a name="p1816118554511"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1116145519518"><a name="p1116145519518"></a><a name="p1116145519518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1966153512589"><a name="p1966153512589"></a><a name="p1966153512589"></a>Tag value</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p03151815143814"><a name="p03151815143814"></a><a name="p03151815143814"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "checkpoint_items" : [ {
        "status" : "available",
        "backup_data" : {
          "eip" : "",
          "cloudservicetype" : "",
          "ram" : 4096,
          "vcpus" : 4,
          "__openstack_region_name" : "",
          "private_ip" : "",
          "disk" : 0,
          "imagetype" : ""
        },
        "name" : "backup_d32c",
        "resource_id" : "f45c477a-57e5-465f-999f-d845083962db",
        "created_at" : "2017-04-15T04:20:37.277880",
        "checkpoint_id" : "f672a1bb-6912-446a-816c-72792c5263e0",
        "updated_at" : "2017-04-15T04:25:38.680638",
        "resource_type": "OS::Nova::Server",
        "extend_info" : {
          "auto_trigger" : false,
          "space_saving_ratio" : 0,
          "copy_status" : "na",
          "fail_reason" : "",
          "resource_az" : "az1.dc1",
          "image_type" : "backup",
          "finished_at" : "2017-04-15T04:25:38.675478",
          "average_speed" : 0,
          "copy_from" : "",
          "supported_restore_mode": "backup",
          "support_lld": false,
          "os_images_data": [
                {
                    "image_id": "fe84dd80-0229-4918-8d3d-cbb33154b565"
                }
           ],
          "volume_backups" : [ {
            "status" : "available",
            "space_saving_ratio" : 0,
            "name" : "manualbk_47222",
            "bootable" : true,
            "average_speed" : 0,
            "source_volume_size" : 20,
            "source_volume_id" : "ee27f809-6fb5-40ae-ac46-c932bb4ee8fe",
            "incremental" : false,
            "image_type" : "backup",
            "source_volume_name" : "karbor_xj_02",
            "id" : "70675cbc-d3a8-43a7-9f81-c8b6bc3f5d6d",
            "size" : 0,
            "snapshot_id": "36f520e1-d2ea-4907-956a-3d9cd53e2d38"
          }, {
            "status" : "available",
            "space_saving_ratio" : 0,
            "name" : "manualbk_47222",
            "bootable" : true,
            "average_speed" : 0,
            "source_volume_size" : 20,
            "source_volume_id" : "e7f48980-927c-48de-afd4-f0245d2e5100",
            "incremental" : false,
            "image_type" : "backup",
            "source_volume_name" : "karbor_01",
            "id" : "8eb98e91-8924-4d4b-b6d6-28fb7b751e9c",
            "size" : 0,
            "snapshot_id": "36f520e1-d2ea-4907-956a-3d9cd53e2d38"
          } ],
          "fail_code" : { },
          "incremental" : false,
          "taskid" : "e0a21692-2192-11e7-bf23-0242ac110007",
          "hypervisor_type" : "QEMU",
          "progress" : 100,
          "fail_op" : "",
          "resource_name" : "karbor_02",
          "size" : 0
        },
        "id" : "90c1d5fa-1b9f-4aeb-b2f4-81c806e98190"
      } ]
    }
    ```


## Status Codes<a name="section53941652"></a>

-   Normal

    <a name="table8795054"></a>
    <table><thead align="left"><tr id="row50800261"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p21180466"><a name="p21180466"></a><a name="p21180466"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p37896167"><a name="p37896167"></a><a name="p37896167"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49690701"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p65523851"><a name="p65523851"></a><a name="p65523851"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p5831754"><a name="p5831754"></a><a name="p5831754"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table2610098"></a>
    <table><thead align="left"><tr id="row41742703"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p25715783"><a name="p25715783"></a><a name="p25715783"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p2603692"><a name="p2603692"></a><a name="p2603692"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9572485"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p37173819"><a name="p37173819"></a><a name="p37173819"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58289333"><a name="p58289333"></a><a name="p58289333"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row54841951"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13013051"><a name="p13013051"></a><a name="p13013051"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p47424207"><a name="p47424207"></a><a name="p47424207"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row24164686"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p11182570"><a name="p11182570"></a><a name="p11182570"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p33373011"><a name="p33373011"></a><a name="p33373011"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row31921648"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p35516662"><a name="p35516662"></a><a name="p35516662"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58277373"><a name="p58277373"></a><a name="p58277373"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row54734312"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p4294291"><a name="p4294291"></a><a name="p4294291"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p12293266"><a name="p12293266"></a><a name="p12293266"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row43530533"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p36312254"><a name="p36312254"></a><a name="p36312254"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p55611423"><a name="p55611423"></a><a name="p55611423"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

