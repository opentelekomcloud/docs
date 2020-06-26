# Querying Backup Shares<a name="EN-US_TOPIC_0078214153"></a>

## Function<a name="section353862016108"></a>

This interface is used to query backup shares.

## URI<a name="section16539122018107"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-backup-sharing/detail

-   Parameter description

    <a name="table145421020191019"></a>
    <table><thead align="left"><tr id="row1478021111013"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p1625418168917"><a name="p1625418168917"></a><a name="p1625418168917"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p9254916897"><a name="p9254916897"></a><a name="p9254916897"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1254191615916"><a name="p1254191615916"></a><a name="p1254191615916"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1378122131018"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1025419164915"><a name="p1025419164915"></a><a name="p1025419164915"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3254171615911"><a name="p3254171615911"></a><a name="p3254171615911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


-   **Request filter **parameter description

    <a name="table454752051016"></a>
    <table><thead align="left"><tr id="row079122141016"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row167912113108"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p0791621141014"><a name="p0791621141014"></a><a name="p0791621141014"></a>share_to_me</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p8796219109"><a name="p8796219109"></a><a name="p8796219109"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p1280142120108"><a name="p1280142120108"></a><a name="p1280142120108"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p48092119105"><a name="p48092119105"></a><a name="p48092119105"></a>If this parameter is set to <strong id="b84235270673034"><a name="b84235270673034"></a><a name="b84235270673034"></a>true</strong>, this interface will list the backups shared with the current project. Otherwise, this interface will list the backups shared by the current project.</p>
    </td>
    </tr>
    <tr id="row12801221191016"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p1780152112108"><a name="p1780152112108"></a><a name="p1780152112108"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p1099415331413"><a name="p1099415331413"></a><a name="p1099415331413"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p158092101011"><a name="p158092101011"></a><a name="p158092101011"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p1580221161020"><a name="p1580221161020"></a><a name="p1580221161020"></a>Volume ID</p>
    </td>
    </tr>
    <tr id="row88052151012"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p18806213109"><a name="p18806213109"></a><a name="p18806213109"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p739341018"><a name="p739341018"></a><a name="p739341018"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p1381182161017"><a name="p1381182161017"></a><a name="p1381182161017"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p1381122131012"><a name="p1381122131012"></a><a name="p1381122131012"></a>Backup name. Fuzzy match is supported.</p>
    </td>
    </tr>
    <tr id="row08122113103"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p1181621161019"><a name="p1181621161019"></a><a name="p1181621161019"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p41114341110"><a name="p41114341110"></a><a name="p41114341110"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p681172141015"><a name="p681172141015"></a><a name="p681172141015"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p1581102131018"><a name="p1581102131018"></a><a name="p1581102131018"></a>Backup status</p>
    </td>
    </tr>
    <tr id="row2081121101010"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p1181102101010"><a name="p1181102101010"></a><a name="p1181102101010"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p14185341911"><a name="p14185341911"></a><a name="p14185341911"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p4811521171017"><a name="p4811521171017"></a><a name="p4811521171017"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p281182111013"><a name="p281182111013"></a><a name="p281182111013"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row9816218106"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p98152116102"><a name="p98152116102"></a><a name="p98152116102"></a>from_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p1522193412116"><a name="p1522193412116"></a><a name="p1522193412116"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p2082221181010"><a name="p2082221181010"></a><a name="p2082221181010"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p58342117100"><a name="p58342117100"></a><a name="p58342117100"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row1383192151017"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p168332171018"><a name="p168332171018"></a><a name="p168332171018"></a>to_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p92717341119"><a name="p92717341119"></a><a name="p92717341119"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p1083162111105"><a name="p1083162111105"></a><a name="p1083162111105"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p383102141010"><a name="p383102141010"></a><a name="p383102141010"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row168312111020"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p5832217106"><a name="p5832217106"></a><a name="p5832217106"></a>avalilability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p63219345113"><a name="p63219345113"></a><a name="p63219345113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p108322171019"><a name="p108322171019"></a><a name="p108322171019"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p138362110103"><a name="p138362110103"></a><a name="p138362110103"></a>AZ name</p>
    </td>
    </tr>
    <tr id="row1983192181010"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p11834210108"><a name="p11834210108"></a><a name="p11834210108"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p103617341411"><a name="p103617341411"></a><a name="p103617341411"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p148442111100"><a name="p148442111100"></a><a name="p148442111100"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p784621131017"><a name="p784621131017"></a><a name="p784621131017"></a>Sorting direction</p>
    </td>
    </tr>
    <tr id="row128417214104"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p48482161014"><a name="p48482161014"></a><a name="p48482161014"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p04114341413"><a name="p04114341413"></a><a name="p04114341413"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p1984721141016"><a name="p1984721141016"></a><a name="p1984721141016"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p1484142112106"><a name="p1484142112106"></a><a name="p1484142112106"></a>Sorts by attribute. Possible values are <strong id="b84235270673358"><a name="b84235270673358"></a><a name="b84235270673358"></a>name</strong>, <strong id="b8423527067341"><a name="b8423527067341"></a><a name="b8423527067341"></a>status</strong>, <strong id="b84235270673411"><a name="b84235270673411"></a><a name="b84235270673411"></a>container_format</strong>, <strong id="b84235270673417"><a name="b84235270673417"></a><a name="b84235270673417"></a>disk_format</strong>, <strong id="b84235270673420"><a name="b84235270673420"></a><a name="b84235270673420"></a>size</strong>, <strong id="b84235270673423"><a name="b84235270673423"></a><a name="b84235270673423"></a>id</strong>, <strong id="b84235270673428"><a name="b84235270673428"></a><a name="b84235270673428"></a>created_at</strong>, or <strong id="b84235270673431"><a name="b84235270673431"></a><a name="b84235270673431"></a>updated_at</strong>. The default value is <strong id="b84235270673435"><a name="b84235270673435"></a><a name="b84235270673435"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row4841621201016"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p16841021201015"><a name="p16841021201015"></a><a name="p16841021201015"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p647203415119"><a name="p647203415119"></a><a name="p647203415119"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p1184202114108"><a name="p1184202114108"></a><a name="p1184202114108"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p1984421131015"><a name="p1984421131015"></a><a name="p1984421131015"></a>Number of shares to be queried</p>
    </td>
    </tr>
    <tr id="row684132114101"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p084142114104"><a name="p084142114104"></a><a name="p084142114104"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="p195443410110"><a name="p195443410110"></a><a name="p195443410110"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="p785021161011"><a name="p785021161011"></a><a name="p785021161011"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.1.5.1.4 "><p id="p18854218109"><a name="p18854218109"></a><a name="p18854218109"></a>Offset of the query</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section5592152001016"></a>

None

## Response<a name="section15592620111016"></a>

-   Parameter description

    <a name="table1760412202109"></a>
    <table><thead align="left"><tr id="row178522115109"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p1241273320221"><a name="p1241273320221"></a><a name="p1241273320221"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.2"><p id="p042833332211"><a name="p042833332211"></a><a name="p042833332211"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.3"><p id="p142803372219"><a name="p142803372219"></a><a name="p142803372219"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1586521131012"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p188614218102"><a name="p188614218102"></a><a name="p188614218102"></a>shared</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p15865210104"><a name="p15865210104"></a><a name="p15865210104"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p186521181010"><a name="p186521181010"></a><a name="p186521181010"></a>Backup share list</p>
    </td>
    </tr>
    <tr id="row12861021111010"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p98662191010"><a name="p98662191010"></a><a name="p98662191010"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p986192113102"><a name="p986192113102"></a><a name="p986192113102"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p4861214107"><a name="p4861214107"></a><a name="p4861214107"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row178612181019"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p108614212109"><a name="p108614212109"></a><a name="p108614212109"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p198612191018"><a name="p198612191018"></a><a name="p198612191018"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p28652112106"><a name="p28652112106"></a><a name="p28652112106"></a>Creation time of the backup share</p>
    </td>
    </tr>
    <tr id="row4860216104"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p78682114102"><a name="p78682114102"></a><a name="p78682114102"></a>from_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p188618213101"><a name="p188618213101"></a><a name="p188618213101"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p186142117106"><a name="p186142117106"></a><a name="p186142117106"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row16861213109"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p58662111106"><a name="p58662111106"></a><a name="p58662111106"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p1286102111015"><a name="p1286102111015"></a><a name="p1286102111015"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p386821111013"><a name="p386821111013"></a><a name="p386821111013"></a>Backup share ID</p>
    </td>
    </tr>
    <tr id="row186202112108"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p886621201019"><a name="p886621201019"></a><a name="p886621201019"></a>to_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p14872217105"><a name="p14872217105"></a><a name="p14872217105"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p1487421171010"><a name="p1487421171010"></a><a name="p1487421171010"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row1787192141016"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p487172181012"><a name="p487172181012"></a><a name="p487172181012"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p78715218103"><a name="p78715218103"></a><a name="p78715218103"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p12871121121014"><a name="p12871121121014"></a><a name="p12871121121014"></a>Update time of the backup share</p>
    </td>
    </tr>
    <tr id="row3874210102"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p148719216102"><a name="p148719216102"></a><a name="p148719216102"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p5871321101019"><a name="p5871321101019"></a><a name="p5871321101019"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p18717218107"><a name="p18717218107"></a><a name="p18717218107"></a>Details about the source backup</p>
    </td>
    </tr>
    <tr id="row1987162161014"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p88792115106"><a name="p88792115106"></a><a name="p88792115106"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p687112111015"><a name="p687112111015"></a><a name="p687112111015"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p42822461202619"><a name="p42822461202619"></a><a name="p42822461202619"></a>AZ where the backup resides</p>
    </td>
    </tr>
    <tr id="row158762115101"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p13870215102"><a name="p13870215102"></a><a name="p13870215102"></a>container</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p1987221191017"><a name="p1987221191017"></a><a name="p1987221191017"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p45004514202619"><a name="p45004514202619"></a><a name="p45004514202619"></a>Container of the backup</p>
    </td>
    </tr>
    <tr id="row2871521191012"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p3871921171019"><a name="p3871921171019"></a><a name="p3871921171019"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p5876210102"><a name="p5876210102"></a><a name="p5876210102"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p1604592202619"><a name="p1604592202619"></a><a name="p1604592202619"></a>Backup creation time</p>
    </td>
    </tr>
    <tr id="row088142114104"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p2881217109"><a name="p2881217109"></a><a name="p2881217109"></a>data_timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p168810219108"><a name="p168810219108"></a><a name="p168810219108"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p14905520174631"><a name="p14905520174631"></a><a name="p14905520174631"></a>Current time</p>
    </td>
    </tr>
    <tr id="row88802161011"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1789112141012"><a name="p1789112141012"></a><a name="p1789112141012"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p1589621171013"><a name="p1589621171013"></a><a name="p1589621171013"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p51398114202619"><a name="p51398114202619"></a><a name="p51398114202619"></a>Backup description</p>
    </td>
    </tr>
    <tr id="row1589132151010"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p489202181015"><a name="p489202181015"></a><a name="p489202181015"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p4897216107"><a name="p4897216107"></a><a name="p4897216107"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p44790369202619"><a name="p44790369202619"></a><a name="p44790369202619"></a>Cause of the backup failure</p>
    </td>
    </tr>
    <tr id="row198942191012"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1290182120106"><a name="p1290182120106"></a><a name="p1290182120106"></a>has_dependent_backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p199012110106"><a name="p199012110106"></a><a name="p199012110106"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p2446587175250"><a name="p2446587175250"></a><a name="p2446587175250"></a>Whether a dependent backup exists. VBS generates a full backup for the initial backup operation and incremental backups for subsequent backup operations. Therefore, this parameter will be skipped.</p>
    </td>
    </tr>
    <tr id="row1090421191013"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p990152151012"><a name="p990152151012"></a><a name="p990152151012"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p1290132161014"><a name="p1290132161014"></a><a name="p1290132161014"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p60551425202619"><a name="p60551425202619"></a><a name="p60551425202619"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row15909211101"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p119018212108"><a name="p119018212108"></a><a name="p119018212108"></a>is_incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p1591921121017"><a name="p1591921121017"></a><a name="p1591921121017"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p16898564175250"><a name="p16898564175250"></a><a name="p16898564175250"></a>Whether the backup is an incremental backup. VBS generates a full backup for the initial backup operation and incremental backups for subsequent backup operations. Therefore, this parameter will be skipped.</p>
    </td>
    </tr>
    <tr id="row591182181015"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p13911221101018"><a name="p13911221101018"></a><a name="p13911221101018"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p169122115109"><a name="p169122115109"></a><a name="p169122115109"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p27753504202619"><a name="p27753504202619"></a><a name="p27753504202619"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row17916210107"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p149152181010"><a name="p149152181010"></a><a name="p149152181010"></a>object_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p1692132151010"><a name="p1692132151010"></a><a name="p1692132151010"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p51837782202619"><a name="p51837782202619"></a><a name="p51837782202619"></a>Number of objects on OBS for the disk data</p>
    </td>
    </tr>
    <tr id="row8921021161020"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p19921721181010"><a name="p19921721181010"></a><a name="p19921721181010"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p1592421151012"><a name="p1592421151012"></a><a name="p1592421151012"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p38938725202619"><a name="p38938725202619"></a><a name="p38938725202619"></a>Backup size</p>
    </td>
    </tr>
    <tr id="row1692182111019"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p092152121011"><a name="p092152121011"></a><a name="p092152121011"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p119212141018"><a name="p119212141018"></a><a name="p119212141018"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p1617637175250"><a name="p1617637175250"></a><a name="p1617637175250"></a>ID of the snapshot associated with the backup</p>
    </td>
    </tr>
    <tr id="row793162119102"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1293132141019"><a name="p1293132141019"></a><a name="p1293132141019"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p1093122119106"><a name="p1093122119106"></a><a name="p1093122119106"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p55194315202619"><a name="p55194315202619"></a><a name="p55194315202619"></a>Backup status</p>
    </td>
    </tr>
    <tr id="row893142141017"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1493182119108"><a name="p1493182119108"></a><a name="p1493182119108"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p193821181011"><a name="p193821181011"></a><a name="p193821181011"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p5110169017462"><a name="p5110169017462"></a><a name="p5110169017462"></a>Update time of the backup</p>
    </td>
    </tr>
    <tr id="row89317219104"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p994182141010"><a name="p994182141010"></a><a name="p994182141010"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p19414212101"><a name="p19414212101"></a><a name="p19414212101"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p39169096202619"><a name="p39169096202619"></a><a name="p39169096202619"></a>Source disk ID of the backup</p>
    </td>
    </tr>
    <tr id="row11945211101"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p6941921101011"><a name="p6941921101011"></a><a name="p6941921101011"></a>service_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.2 "><p id="p89612115106"><a name="p89612115106"></a><a name="p89612115106"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.3 "><p id="p10122423202619"><a name="p10122423202619"></a><a name="p10122423202619"></a>Backup metadata</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "shared": [
            {
                "backup": {
                    "availability_zone": "AZ1",
                    "container": null,
                    "created_at": "2017-08-08T04:03:27.456859",
                    "data_timestamp": "2017-08-08T04:03:27.456859",
                    "description": null,
                    "fail_reason": "Invalid InitiatorConnector protocol specified DSWARE",
                    "has_dependent_backups": null,
                    "id": "066b1e37-9305-4057-97e5-2e99b21fc71d",
                    "is_incremental": null,
                    "name": "lbf",
                    "object_count": null,
                    "size": 1,
                    "snapshot_id": null,
                    "status": "available",
                    "updated_at": "2017-08-08T04:03:35.109308",
                    "volume_id": "a7d7783f-02b7-4645-b0e3-61df63f0ba10",
                    "service_metadata": null
                },
                "backup_id": "066b1e37-9305-4057-97e5-2e99b21fc71d",
                "created_at": "2017-08-10T12:25:40.480424",
                "from_project_id": "c13f5220dc1949b0b741ea81a7cd5554",
                "id": "e842bf23-1e05-4c2c-b0f9-25222f4686da",
                "to_project_id": "722513ed0a324dadaabe5b2d0fe848b9",
                "updated_at": "2017-08-14T06:41:49.381069"
            },
            {
                "backup": {
                    "availability_zone": "AZ1",
                    "container": null,
                    "created_at": "2017-08-08T04:03:27.456859",
                    "data_timestamp": "2017-08-08T04:03:27.456859",
                    "description": null,
                    "fail_reason": "Invalid InitiatorConnector protocol specified DSWARE",
                    "has_dependent_backups": null,
                    "id": "066b1e37-9305-4057-97e5-2e99b21fc71d",
                    "is_incremental": null,
                    "name": "lbf",
                    "object_count": null,
                    "size": 1,
                    "snapshot_id": null,
                    "status": "available",
                    "updated_at": "2017-08-08T04:03:35.109308",
                    "volume_id": "a7d7783f-02b7-4645-b0e3-61df63f0ba10",
                    "service_metadata": null
                },
                "backup_id": "066b1e37-9305-4057-97e5-2e99b21fc71d",
                "created_at": "2017-08-10T12:19:37.318031",
                "from_project_id": "c13f5220dc1949b0b741ea81a7cd5554",
                "id": "f842bf23-1e05-4c2c-b0f9-25222f4686da",
                "to_project_id": "722513ed0a324dadaabe5b2d0fe848a9",
                "updated_at": null
            }
        ]
    }
    ```


## Status Codes<a name="section368014204108"></a>

-   Normal

    200

-   Abnormal

    <a name="table59178184203255"></a>
    <table><thead align="left"><tr id="row54047877203255"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p15801936203255"><a name="p15801936203255"></a><a name="p15801936203255"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p4888452203255"><a name="p4888452203255"></a><a name="p4888452203255"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60420295203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p62205764203255"><a name="p62205764203255"></a><a name="p62205764203255"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5502113203255"><a name="p5502113203255"></a><a name="p5502113203255"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row49519019203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p51617596203255"><a name="p51617596203255"></a><a name="p51617596203255"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p20275713203255"><a name="p20275713203255"></a><a name="p20275713203255"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row48263690203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17044857203255"><a name="p17044857203255"></a><a name="p17044857203255"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38456209203255"><a name="p38456209203255"></a><a name="p38456209203255"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row10561563203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p50180290203255"><a name="p50180290203255"></a><a name="p50180290203255"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38071718203255"><a name="p38071718203255"></a><a name="p38071718203255"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row7101146203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p38321955203255"><a name="p38321955203255"></a><a name="p38321955203255"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p17070685203255"><a name="p17070685203255"></a><a name="p17070685203255"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row19418444203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p29390130203255"><a name="p29390130203255"></a><a name="p29390130203255"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31790300203255"><a name="p31790300203255"></a><a name="p31790300203255"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row17677246203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p22570826203255"><a name="p22570826203255"></a><a name="p22570826203255"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16297614203255"><a name="p16297614203255"></a><a name="p16297614203255"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row12460805203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2692305203255"><a name="p2692305203255"></a><a name="p2692305203255"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16750186203255"><a name="p16750186203255"></a><a name="p16750186203255"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row16533951203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p64181621203255"><a name="p64181621203255"></a><a name="p64181621203255"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31328812203255"><a name="p31328812203255"></a><a name="p31328812203255"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row13523855203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p21690474203255"><a name="p21690474203255"></a><a name="p21690474203255"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12097945203255"><a name="p12097945203255"></a><a name="p12097945203255"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row41772644203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28140973203255"><a name="p28140973203255"></a><a name="p28140973203255"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p64826302203255"><a name="p64826302203255"></a><a name="p64826302203255"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row46565809203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p13734210203255"><a name="p13734210203255"></a><a name="p13734210203255"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38729264203255"><a name="p38729264203255"></a><a name="p38729264203255"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row13019061203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p47911033203255"><a name="p47911033203255"></a><a name="p47911033203255"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p55588428203255"><a name="p55588428203255"></a><a name="p55588428203255"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row30533812203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p57319716203255"><a name="p57319716203255"></a><a name="p57319716203255"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12385400203255"><a name="p12385400203255"></a><a name="p12385400203255"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

