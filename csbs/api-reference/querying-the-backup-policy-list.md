# Querying the Backup Policy List<a name="EN-US_TOPIC_0059304227"></a>

## Function<a name="section37588797"></a>

This interface is used to query the backup policy list. Filtering parameters are supported.

## URI<a name="section2754853"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/policies

-   Parameter description

    **Table  1**  Parameter description

    <a name="table29578263"></a>
    <table><thead align="left"><tr id="row55030713"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45356064"><a name="p45356064"></a><a name="p45356064"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p49962569"><a name="p49962569"></a><a name="p49962569"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p20436323"><a name="p20436323"></a><a name="p20436323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p44729494"><a name="p44729494"></a><a name="p44729494"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row806275"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p65308318"><a name="p65308318"></a><a name="p65308318"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p55482381"><a name="p55482381"></a><a name="p55482381"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p64887865"><a name="p64887865"></a><a name="p64887865"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section24793679"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table47880374"></a>
    <table><thead align="left"><tr id="row8615968"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p81019812473"><a name="p81019812473"></a><a name="p81019812473"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p15102081479"><a name="p15102081479"></a><a name="p15102081479"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p18101081479"><a name="p18101081479"></a><a name="p18101081479"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p325148194714"><a name="p325148194714"></a><a name="p325148194714"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18906739"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p55050930"><a name="p55050930"></a><a name="p55050930"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p29940378"><a name="p29940378"></a><a name="p29940378"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p9251538"><a name="p9251538"></a><a name="p9251538"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p11177090"><a name="p11177090"></a><a name="p11177090"></a>Number of resources displayed per page. The value must be a positive integer. The value defaults to <strong id="b18247153115518"><a name="b18247153115518"></a><a name="b18247153115518"></a>1000</strong>.</p>
    </td>
    </tr>
    <tr id="row33484951"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p27926511"><a name="p27926511"></a><a name="p27926511"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p47454932"><a name="p47454932"></a><a name="p47454932"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p18644269"><a name="p18644269"></a><a name="p18644269"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p33790819"><a name="p33790819"></a><a name="p33790819"></a>ID of the last record displayed on the previous page when pagination query is applied</p>
    </td>
    </tr>
    <tr id="row35681916"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p4554055"><a name="p4554055"></a><a name="p4554055"></a>sort</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p33334179"><a name="p33334179"></a><a name="p33334179"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p15713975"><a name="p15713975"></a><a name="p15713975"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p64872492"><a name="p64872492"></a><a name="p64872492"></a>The value of <strong id="b34759433"><a name="b34759433"></a><a name="b34759433"></a>sort</strong> is a group of properties separated by commas (,) and sorting directions. The format is &lt;key1&gt;[:&lt;direction&gt;],&lt;key2&gt;[:&lt;direction&gt;], where the value of direction is <strong id="b1273581669173844"><a name="b1273581669173844"></a><a name="b1273581669173844"></a>asc</strong> (in ascending order) or <strong id="b421059629173844"><a name="b421059629173844"></a><a name="b421059629173844"></a>desc</strong> (in descending order). If the parameter direction is not specified, backup policies are sorted in descending order by time. The value of <strong id="b788002962173844"><a name="b788002962173844"></a><a name="b788002962173844"></a>sort</strong> contains a maximum of 255 characters.</p>
    </td>
    </tr>
    <tr id="row46981522"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p47406971"><a name="p47406971"></a><a name="p47406971"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p14759448"><a name="p14759448"></a><a name="p14759448"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p54664658"><a name="p54664658"></a><a name="p54664658"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65761168"><a name="p65761168"></a><a name="p65761168"></a>Exact matching based on field <strong id="b41027498"><a name="b41027498"></a><a name="b41027498"></a>name</strong></p>
    </td>
    </tr>
    <tr id="row54979604"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p24162964"><a name="p24162964"></a><a name="p24162964"></a>all_tenants</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p11043085"><a name="p11043085"></a><a name="p11043085"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p22074662"><a name="p22074662"></a><a name="p22074662"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p921691216449"><a name="p921691216449"></a><a name="p921691216449"></a>Whether backup policies of all tenants can be queried</p>
    <p id="p43217159"><a name="p43217159"></a><a name="p43217159"></a>This parameter is only available for administrators.</p>
    </td>
    </tr>
    <tr id="row53410114"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p31252003"><a name="p31252003"></a><a name="p31252003"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p48384353"><a name="p48384353"></a><a name="p48384353"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p26818531"><a name="p26818531"></a><a name="p26818531"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p24817426"><a name="p24817426"></a><a name="p24817426"></a>Offset value, which is a positive integer.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description

None

-   Example request

    ```
    Querying all backup policies:
    GET https://{endpoint}/v1/{project_id}/policies
    Querying backup policies with certain conditions:
    GET https://{endpoint}/v1/{project_id}/policies?sort=created_at%3Aasc&limit=3&offset=3
    ```


## Response<a name="section21816525"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table65599866"></a>
    <table><thead align="left"><tr id="row3333769"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p78731344718"><a name="p78731344718"></a><a name="p78731344718"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p6102161317473"><a name="p6102161317473"></a><a name="p6102161317473"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p9102513174714"><a name="p9102513174714"></a><a name="p9102513174714"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33962906"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66640864"><a name="p66640864"></a><a name="p66640864"></a>policies</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16460576"><a name="p16460576"></a><a name="p16460576"></a>List&lt;policy_resp&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p760491412288"><a name="p760491412288"></a><a name="p760491412288"></a>For details, see the <strong id="b89724121070"><a name="b89724121070"></a><a name="b89724121070"></a>policy_resp</strong> field description.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_resp**

    **Table  4**  Parameter description of field  **policy\_resp**

    <a name="table19683123"></a>
    <table><thead align="left"><tr id="row33757491"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p272811199473"><a name="p272811199473"></a><a name="p272811199473"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p16728619134712"><a name="p16728619134712"></a><a name="p16728619134712"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p874381934711"><a name="p874381934711"></a><a name="p874381934711"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62410315"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p22070716"><a name="p22070716"></a><a name="p22070716"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p52150808"><a name="p52150808"></a><a name="p52150808"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p63465939"><a name="p63465939"></a><a name="p63465939"></a>Creation time, for example, <strong id="b1854418211776"><a name="b1854418211776"></a><a name="b1854418211776"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row34322544"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p28662703"><a name="p28662703"></a><a name="p28662703"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16960338"><a name="p16960338"></a><a name="p16960338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p25044971164419"><a name="p25044971164419"></a><a name="p25044971164419"></a>Backup policy description</p>
    <p id="p31610118"><a name="p31610118"></a><a name="p31610118"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row16055609"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25435967"><a name="p25435967"></a><a name="p25435967"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p52747388"><a name="p52747388"></a><a name="p52747388"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p44680068"><a name="p44680068"></a><a name="p44680068"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row66576294"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23970749"><a name="p23970749"></a><a name="p23970749"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p36021385"><a name="p36021385"></a><a name="p36021385"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p43152724164422"><a name="p43152724164422"></a><a name="p43152724164422"></a>Backup policy name</p>
    <p id="p32051086"><a name="p32051086"></a><a name="p32051086"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row20024320"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p11357251"><a name="p11357251"></a><a name="p11357251"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24086321"><a name="p24086321"></a><a name="p24086321"></a>policy_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4834989"><a name="p4834989"></a><a name="p4834989"></a>Parameters of a backup policy</p>
    </td>
    </tr>
    <tr id="row43514905"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p35046384"><a name="p35046384"></a><a name="p35046384"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24362293"><a name="p24362293"></a><a name="p24362293"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p27188722"><a name="p27188722"></a><a name="p27188722"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row43371912"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23463983"><a name="p23463983"></a><a name="p23463983"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p66569886"><a name="p66569886"></a><a name="p66569886"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23451703"><a name="p23451703"></a><a name="p23451703"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b1532195820912"><a name="b1532195820912"></a><a name="b1532195820912"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row9738736"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50640112"><a name="p50640112"></a><a name="p50640112"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p60899069"><a name="p60899069"></a><a name="p60899069"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p33877595"><a name="p33877595"></a><a name="p33877595"></a>Backup object list</p>
    </td>
    </tr>
    <tr id="row36462904"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p705260"><a name="p705260"></a><a name="p705260"></a>scheduled_operations</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p63808428"><a name="p63808428"></a><a name="p63808428"></a>List&lt;scheduled_operation_resp&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1100169"><a name="p1100169"></a><a name="p1100169"></a>Scheduling period list</p>
    </td>
    </tr>
    <tr id="row9901523"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p63825892"><a name="p63825892"></a><a name="p63825892"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2366474"><a name="p2366474"></a><a name="p2366474"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57466737"><a name="p57466737"></a><a name="p57466737"></a>Backup policy status</p>
    </td>
    </tr>
    <tr id="row164178313331"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p441718303317"><a name="p441718303317"></a><a name="p441718303317"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16417932330"><a name="p16417932330"></a><a name="p16417932330"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p44179311333"><a name="p44179311333"></a><a name="p44179311333"></a>Tag list</p>
    <p id="p20418998516"><a name="p20418998516"></a><a name="p20418998516"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_param**

    **Table  5**  Parameter description of field  **policy\_param**

    <a name="table24294083"></a>
    <table><thead align="left"><tr id="row59113611"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p3946192354719"><a name="p3946192354719"></a><a name="p3946192354719"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1946202394716"><a name="p1946202394716"></a><a name="p1946202394716"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p12962923104716"><a name="p12962923104716"></a><a name="p12962923104716"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17853234"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p36825846"><a name="p36825846"></a><a name="p36825846"></a>common</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p22470857"><a name="p22470857"></a><a name="p22470857"></a>common_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8200103"><a name="p8200103"></a><a name="p8200103"></a>General backup policy parameters, which are blank by default</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource**

    **Table  6**  Parameter description of field  **resource**

    <a name="table60228573"></a>
    <table><thead align="left"><tr id="row24510657"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p141036335476"><a name="p141036335476"></a><a name="p141036335476"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1611811332473"><a name="p1611811332473"></a><a name="p1611811332473"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p15118833124716"><a name="p15118833124716"></a><a name="p15118833124716"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9935832"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66604938"><a name="p66604938"></a><a name="p66604938"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p49189852"><a name="p49189852"></a><a name="p49189852"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p24955084"><a name="p24955084"></a><a name="p24955084"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row23269166"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p5754275"><a name="p5754275"></a><a name="p5754275"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p38621127"><a name="p38621127"></a><a name="p38621127"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p12469818162119"><a name="p12469818162119"></a><a name="p12469818162119"></a>Entity object type of backup objects</p>
    <p id="p41303622"><a name="p41303622"></a><a name="p41303622"></a>The value is fixed at <strong id="b65541511163014"><a name="b65541511163014"></a><a name="b65541511163014"></a>OS::Nova::Server</strong>, indicating that the object type is ECSs.</p>
    </td>
    </tr>
    <tr id="row36188286"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45570016"><a name="p45570016"></a><a name="p45570016"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14890379"><a name="p14890379"></a><a name="p14890379"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p65270051"><a name="p65270051"></a><a name="p65270051"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row42041022105013"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p777318533616"><a name="p777318533616"></a><a name="p777318533616"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10773185103617"><a name="p10773185103617"></a><a name="p10773185103617"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1677325193612"><a name="p1677325193612"></a><a name="p1677325193612"></a>Additional information about the backup object</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **scheduled\_operation\_resp**

    **Table  7**  Parameter description of field  **scheduled\_operation\_resp**

    <a name="table52382792"></a>
    <table><thead align="left"><tr id="row32282907"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1893113910472"><a name="p1893113910472"></a><a name="p1893113910472"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p39473396479"><a name="p39473396479"></a><a name="p39473396479"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p19947739114713"><a name="p19947739114713"></a><a name="p19947739114713"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9730668"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p49986610"><a name="p49986610"></a><a name="p49986610"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1133032"><a name="p1133032"></a><a name="p1133032"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28250778164442"><a name="p28250778164442"></a><a name="p28250778164442"></a>Scheduling period description</p>
    <p id="p24666792"><a name="p24666792"></a><a name="p24666792"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row20674542"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p64025194"><a name="p64025194"></a><a name="p64025194"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34918070"><a name="p34918070"></a><a name="p34918070"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34970950164444"><a name="p34970950164444"></a><a name="p34970950164444"></a>Whether the scheduling period is enabled</p>
    <p id="p9791447"><a name="p9791447"></a><a name="p9791447"></a>The default value is <strong id="b1653051661164049"><a name="b1653051661164049"></a><a name="b1653051661164049"></a>true</strong>. If it is set to <strong id="b1776574786164051"><a name="b1776574786164051"></a><a name="b1776574786164051"></a>false</strong>, automatic scheduling is disabled but manual scheduling is supported.</p>
    </td>
    </tr>
    <tr id="row21014167"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24425986"><a name="p24425986"></a><a name="p24425986"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2931129"><a name="p2931129"></a><a name="p2931129"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42130752164450"><a name="p42130752164450"></a><a name="p42130752164450"></a>Scheduling period name</p>
    <p id="p36094934"><a name="p36094934"></a><a name="p36094934"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row56418953"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6532461"><a name="p6532461"></a><a name="p6532461"></a>operation_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p44024067"><a name="p44024067"></a><a name="p44024067"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9179652"><a name="p9179652"></a><a name="p9179652"></a>Operation type, which can be backup </p>
    <p id="p15508011"><a name="p15508011"></a><a name="p15508011"></a>Enumeration values: <strong id="b176371156132920"><a name="b176371156132920"></a><a name="b176371156132920"></a>backup</strong></p>
    </td>
    </tr>
    <tr id="row5354379"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p31051517"><a name="p31051517"></a><a name="p31051517"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p53605320"><a name="p53605320"></a><a name="p53605320"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p47063664"><a name="p47063664"></a><a name="p47063664"></a>Scheduling period parameters</p>
    </td>
    </tr>
    <tr id="row20919797"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16782031"><a name="p16782031"></a><a name="p16782031"></a>trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48373877"><a name="p48373877"></a><a name="p48373877"></a>trigger_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p25969936"><a name="p25969936"></a><a name="p25969936"></a>Scheduling policy</p>
    </td>
    </tr>
    <tr id="row32402836"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p7384096"><a name="p7384096"></a><a name="p7384096"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p61563539"><a name="p61563539"></a><a name="p61563539"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p20590796"><a name="p20590796"></a><a name="p20590796"></a>Scheduling period ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **operation\_definition**

    **Table  8**  Parameter description of field  **operation\_definition**

    <a name="table28128170"></a>
    <table><thead align="left"><tr id="row9995691"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p17744544114718"><a name="p17744544114718"></a><a name="p17744544114718"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1374416445472"><a name="p1374416445472"></a><a name="p1374416445472"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p17760204415477"><a name="p17760204415477"></a><a name="p17760204415477"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32788649"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p38634918"><a name="p38634918"></a><a name="p38634918"></a>max_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p13522398"><a name="p13522398"></a><a name="p13522398"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1662615433283"><a name="p1662615433283"></a><a name="p1662615433283"></a>Maximum number of backups that can be automatically created for a backup object. The value can be <strong id="b19987125062417"><a name="b19987125062417"></a><a name="b19987125062417"></a>-1</strong> or ranges from <strong id="b1698745015246"><a name="b1698745015246"></a><a name="b1698745015246"></a>0</strong> to <strong id="b1098865012241"><a name="b1098865012241"></a><a name="b1098865012241"></a>99999</strong>. If the value is set to <strong id="b16972105532418"><a name="b16972105532418"></a><a name="b16972105532418"></a>-1</strong>, the backups will not be cleared even though the configured retained backup quantity limit is exceeded.</p>
    </td>
    </tr>
    <tr id="row59934386"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p22847115"><a name="p22847115"></a><a name="p22847115"></a>retention_duration_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p45828933"><a name="p45828933"></a><a name="p45828933"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p762624392810"><a name="p762624392810"></a><a name="p762624392810"></a>Duration of retaining a backup, in days. The value can be <strong id="b2594958192418"><a name="b2594958192418"></a><a name="b2594958192418"></a>-1</strong> or ranges from <strong id="b185951758152414"><a name="b185951758152414"></a><a name="b185951758152414"></a>0</strong> to <strong id="b459519580247"><a name="b459519580247"></a><a name="b459519580247"></a>99999</strong>. If the value is set to <strong id="b035610152515"><a name="b035610152515"></a><a name="b035610152515"></a>-1</strong>, backups will not be cleared even though the configured retention duration is exceeded.</p>
    </td>
    </tr>
    <tr id="row56187057"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p54857807"><a name="p54857807"></a><a name="p54857807"></a>permanent</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p17238208"><a name="p17238208"></a><a name="p17238208"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p54117603"><a name="p54117603"></a><a name="p54117603"></a>Whether backups are permanently retained</p>
    </td>
    </tr>
    <tr id="row3396336335"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p11411933133315"><a name="p11411933133315"></a><a name="p11411933133315"></a>plan_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p74143383318"><a name="p74143383318"></a><a name="p74143383318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p241193320331"><a name="p241193320331"></a><a name="p241193320331"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row8465551103314"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1646519515336"><a name="p1646519515336"></a><a name="p1646519515336"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3465195117335"><a name="p3465195117335"></a><a name="p3465195117335"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p11465115133318"><a name="p11465115133318"></a><a name="p11465115133318"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b1335125812116"><a name="b1335125812116"></a><a name="b1335125812116"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **trigger\_resp**

    **Table  9**  Parameter description of field  **trigger\_resp**

    <a name="table21449731"></a>
    <table><thead align="left"><tr id="row52707782"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p125258482474"><a name="p125258482474"></a><a name="p125258482474"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p16541124814713"><a name="p16541124814713"></a><a name="p16541124814713"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p175411048174714"><a name="p175411048174714"></a><a name="p175411048174714"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23976022"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p63009631"><a name="p63009631"></a><a name="p63009631"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p15592812"><a name="p15592812"></a><a name="p15592812"></a>trigger_properties_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p55058239"><a name="p55058239"></a><a name="p55058239"></a>Scheduler properties</p>
    </td>
    </tr>
    <tr id="row25762104"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6355662"><a name="p6355662"></a><a name="p6355662"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24900001"><a name="p24900001"></a><a name="p24900001"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p3634221"><a name="p3634221"></a><a name="p3634221"></a>Scheduler ID</p>
    </td>
    </tr>
    <tr id="row32707997"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p32102075"><a name="p32102075"></a><a name="p32102075"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34099368"><a name="p34099368"></a><a name="p34099368"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p10585415"><a name="p10585415"></a><a name="p10585415"></a>Scheduler name</p>
    </td>
    </tr>
    <tr id="row28159878"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66357621"><a name="p66357621"></a><a name="p66357621"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p37152881"><a name="p37152881"></a><a name="p37152881"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p56593357"><a name="p56593357"></a><a name="p56593357"></a>Scheduling type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **trigger\_properties\_resp**

    **Table  10**  Parameter description of field  **trigger\_properties\_resp**

    <a name="table20659230"></a>
    <table><thead align="left"><tr id="row27765832"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1830094912471"><a name="p1830094912471"></a><a name="p1830094912471"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p730017494479"><a name="p730017494479"></a><a name="p730017494479"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p1131594910479"><a name="p1131594910479"></a><a name="p1131594910479"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21119259"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p32938458"><a name="p32938458"></a><a name="p32938458"></a>pattern</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18686714"><a name="p18686714"></a><a name="p18686714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p10408666164546"><a name="p10408666164546"></a><a name="p10408666164546"></a>Scheduling policy of the scheduler</p>
    <p id="p37228842"><a name="p37228842"></a><a name="p37228842"></a>The value consists of a maximum of 10,240 characters. The scheduling policy complies with iCalendar RFC 2445, but it supports only four parameters, which are <strong id="b385511552917"><a name="b385511552917"></a><a name="b385511552917"></a>FREQ</strong>, <strong id="b1685513518298"><a name="b1685513518298"></a><a name="b1685513518298"></a>BYDAY</strong>, <strong id="b1085516511293"><a name="b1085516511293"></a><a name="b1085516511293"></a>BYHOUR</strong>, and <strong id="b1785515518294"><a name="b1785515518294"></a><a name="b1785515518294"></a>BYMINUTE</strong>. <strong id="b1285595102915"><a name="b1285595102915"></a><a name="b1285595102915"></a>FREQ</strong> can be set to <strong id="b118559510297"><a name="b118559510297"></a><a name="b118559510297"></a>WEEKLY</strong> and <strong id="b1856451297"><a name="b1856451297"></a><a name="b1856451297"></a>DAILY</strong>, <strong id="b9856105132914"><a name="b9856105132914"></a><a name="b9856105132914"></a>BYDAY</strong> can be set to <strong id="b58561658292"><a name="b58561658292"></a><a name="b58561658292"></a>MO</strong>, <strong id="b128564520295"><a name="b128564520295"></a><a name="b128564520295"></a>TU</strong>, <strong id="b1085612512293"><a name="b1085612512293"></a><a name="b1085612512293"></a>WE</strong>, <strong id="b685617502913"><a name="b685617502913"></a><a name="b685617502913"></a>TH</strong>, <strong id="b108568572917"><a name="b108568572917"></a><a name="b108568572917"></a>FR</strong>, <strong id="b1185613532911"><a name="b1185613532911"></a><a name="b1185613532911"></a>SA</strong>, and <strong id="b585655142913"><a name="b585655142913"></a><a name="b585655142913"></a>SU</strong> (seven days of a week), <strong id="b48579532912"><a name="b48579532912"></a><a name="b48579532912"></a>BYHOUR</strong> ranges from 0 hours to 23 hours, and <strong id="b1385711572917"><a name="b1385711572917"></a><a name="b1385711572917"></a>BYMINUTE</strong> ranges from 0 minutes to 59 minutes. The scheduling interval must not be less than 1 hour. A maximum of 24 time points are allowed in a day.</p>
    </td>
    </tr>
    <tr id="row66624127"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p27845207"><a name="p27845207"></a><a name="p27845207"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p22079637"><a name="p22079637"></a><a name="p22079637"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p43620171"><a name="p43620171"></a><a name="p43620171"></a>Start time of the scheduler, for example, 2017-03-07 09:31:08</p>
    </td>
    </tr>
    <tr id="row1159494211512"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p959412428152"><a name="p959412428152"></a><a name="p959412428152"></a>format</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1859464217158"><a name="p1859464217158"></a><a name="p1859464217158"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p115944424156"><a name="p115944424156"></a><a name="p115944424156"></a>Scheduler type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  11**  Parameter description of field  **resource\_tag**

    <a name="table1431115645119"></a>
    <table><thead align="left"><tr id="row4339106155119"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p81901352194712"><a name="p81901352194712"></a><a name="p81901352194712"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p3206952154720"><a name="p3206952154720"></a><a name="p3206952154720"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p15221135214471"><a name="p15221135214471"></a><a name="p15221135214471"></a>Description</p>
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
    <p id="p83271213184417"><a name="p83271213184417"></a><a name="p83271213184417"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "policies" : [ {
        "created_at" : "2017-03-07T09:31:08.265000",
        "description" : "My plan",
        "id" : "27b11f3f-578d-4464-89d1-7c6d5894f753",
        "name" : "my-plan",
        "parameters" : {
          "common" : {
          }
        },
        "project_id" : "tenant",
        "provider_id" : "c714180d-ea34-4b13-9a5e-577c7c416eec",
        "resources" : [ {
          "id" : "45baf976-c20a-4894-a7c3-c94b7376bf55",
          "name" : "resource1",
          "type" : "OS::Nova::Server",
          "extra_info" : {
        }
        }, {
          "id" : "5aa119a8-d25b-45a7-8d1b-88e127885635",
          "name" : "resource2",
          "type" : "OS::Nova::Server",
          "extra_info" : {
        }
        } ],
        "scheduled_operations" : [ {
          "description" : "My backup policy",
          "enabled" : true,
          "id" : "3b2fdf8c-2cc2-4887-9605-a8443922f6f2",
          "name" : "my-backup-policy",
          "operation_definition" : {
            "max_backups" : "20",
            "plan_id" : "27b11f3f-578d-4464-89d1-7c6d5894f753",
            "provider_id" : "c714180d-ea34-4b13-9a5e-577c7c416eec"
          },
          "operation_type" : "backup",
          "trigger" : {
            "id" : "f1246246-ec6a-4e9a-917e-d050dc2808c9",
            "name" : "default",
            "properties" : {
              "pattern" : "BEGIN:VCALENDAR\r\nBEGIN:VEVENT\r\nRRULE:FREQ=WEEKLY;BYDAY=TH;BYHOUR=12;BYMINUTE=27\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n",
              "start_time" : "2017-03-07 09:31:08",
              "format": "ical"
            },
            "type" : "time"
          },
          "trigger_id" : "f1246246-ec6a-4e9a-917e-d050dc2808c9"
        } ],
        "status" : "disabled"
      } ]
    }
    ```


## Status Codes<a name="section62130998"></a>

-   Normal

    <a name="table43900785"></a>
    <table><thead align="left"><tr id="row16295584"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p44873929"><a name="p44873929"></a><a name="p44873929"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p10909667"><a name="p10909667"></a><a name="p10909667"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11267862"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p40281609"><a name="p40281609"></a><a name="p40281609"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p41584868"><a name="p41584868"></a><a name="p41584868"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table12931152"></a>
    <table><thead align="left"><tr id="row6966727"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p27434048"><a name="p27434048"></a><a name="p27434048"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p7565421"><a name="p7565421"></a><a name="p7565421"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8819383"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p43281413"><a name="p43281413"></a><a name="p43281413"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p16133568"><a name="p16133568"></a><a name="p16133568"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row10984385"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p17320010"><a name="p17320010"></a><a name="p17320010"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p60743539"><a name="p60743539"></a><a name="p60743539"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row9820939"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p57298567"><a name="p57298567"></a><a name="p57298567"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p10672376"><a name="p10672376"></a><a name="p10672376"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row28942528"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p62643451"><a name="p62643451"></a><a name="p62643451"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p40954783"><a name="p40954783"></a><a name="p40954783"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row33048727"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p59701226"><a name="p59701226"></a><a name="p59701226"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p3961146"><a name="p3961146"></a><a name="p3961146"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row35650316"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p1994465"><a name="p1994465"></a><a name="p1994465"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p27333991"><a name="p27333991"></a><a name="p27333991"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

