# Querying All Replication Consistency Groups \(Deprecated\)<a name="evs_04_2051"></a>

## Function<a name="en-us_topic_0079692911_section49131481"></a>

This API is used to query all replication consistency groups of the current tenant.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079692911_section47825138"></a>

None

## URI<a name="en-us_topic_0079692911_section27773061"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-replication-consistency-groups

-   Parameter description

    <a name="en-us_topic_0079692911_table43603258"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692911_row24049039"><th class="cellrowborder" valign="top" width="26.83%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079692911_p1815156"><a name="en-us_topic_0079692911_p1815156"></a><a name="en-us_topic_0079692911_p1815156"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.270000000000003%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079692911_p57431367111711"><a name="en-us_topic_0079692911_p57431367111711"></a><a name="en-us_topic_0079692911_p57431367111711"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.9%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079692911_p61214164111723"><a name="en-us_topic_0079692911_p61214164111723"></a><a name="en-us_topic_0079692911_p61214164111723"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692911_row66471715"><td class="cellrowborder" valign="top" width="26.83%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692911_p15499871"><a name="en-us_topic_0079692911_p15499871"></a><a name="en-us_topic_0079692911_p15499871"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.270000000000003%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692911_p15272580112548"><a name="en-us_topic_0079692911_p15272580112548"></a><a name="en-us_topic_0079692911_p15272580112548"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.9%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692911_p56592155"><a name="en-us_topic_0079692911_p56592155"></a><a name="en-us_topic_0079692911_p56592155"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079692911_section48630964"></a>

-   Parameter description

    <a name="en-us_topic_0079692911_table24311045"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692911_row51797270"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079692911_p12490165112556"><a name="en-us_topic_0079692911_p12490165112556"></a><a name="en-us_topic_0079692911_p12490165112556"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079692911_p5070476112556"><a name="en-us_topic_0079692911_p5070476112556"></a><a name="en-us_topic_0079692911_p5070476112556"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079692911_p8055374112556"><a name="en-us_topic_0079692911_p8055374112556"></a><a name="en-us_topic_0079692911_p8055374112556"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="36%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079692911_p48505573112556"><a name="en-us_topic_0079692911_p48505573112556"></a><a name="en-us_topic_0079692911_p48505573112556"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079692911_row1832323"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692911_p14200498"><a name="en-us_topic_0079692911_p14200498"></a><a name="en-us_topic_0079692911_p14200498"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692911_p45031451112559"><a name="en-us_topic_0079692911_p45031451112559"></a><a name="en-us_topic_0079692911_p45031451112559"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692911_p22367029"><a name="en-us_topic_0079692911_p22367029"></a><a name="en-us_topic_0079692911_p22367029"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692911_p66898905"><a name="en-us_topic_0079692911_p66898905"></a><a name="en-us_topic_0079692911_p66898905"></a>Specifies the ID of the last replication consistency group on the previous page. The next replication consistency group ID is returned.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row65219236"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692911_p48266778"><a name="en-us_topic_0079692911_p48266778"></a><a name="en-us_topic_0079692911_p48266778"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692911_p3440575511267"><a name="en-us_topic_0079692911_p3440575511267"></a><a name="en-us_topic_0079692911_p3440575511267"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692911_p58713911"><a name="en-us_topic_0079692911_p58713911"></a><a name="en-us_topic_0079692911_p58713911"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692911_p58206383"><a name="en-us_topic_0079692911_p58206383"></a><a name="en-us_topic_0079692911_p58206383"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p6697193316112"><a name="p6697193316112"></a><a name="p6697193316112"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row54095401"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692911_p19651376"><a name="en-us_topic_0079692911_p19651376"></a><a name="en-us_topic_0079692911_p19651376"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692911_p3589366411267"><a name="en-us_topic_0079692911_p3589366411267"></a><a name="en-us_topic_0079692911_p3589366411267"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692911_p16555740"><a name="en-us_topic_0079692911_p16555740"></a><a name="en-us_topic_0079692911_p16555740"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692911_p31429445202427"><a name="en-us_topic_0079692911_p31429445202427"></a><a name="en-us_topic_0079692911_p31429445202427"></a>Specifies that the returned results are sorted by keyword. The default keyword is <strong id="b842352706153317"><a name="b842352706153317"></a><a name="b842352706153317"></a>created_at</strong>, indicating that the replication consistency groups are sorted by creation time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row56648283"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692911_p25108238"><a name="en-us_topic_0079692911_p25108238"></a><a name="en-us_topic_0079692911_p25108238"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692911_p2969827711267"><a name="en-us_topic_0079692911_p2969827711267"></a><a name="en-us_topic_0079692911_p2969827711267"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692911_p49998812"><a name="en-us_topic_0079692911_p49998812"></a><a name="en-us_topic_0079692911_p49998812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692911_p35200389202451"><a name="en-us_topic_0079692911_p35200389202451"></a><a name="en-us_topic_0079692911_p35200389202451"></a>Specifies that the returned results are sorted by ascending or descending order. The default value is <strong id="b84235270615371"><a name="b84235270615371"></a><a name="b84235270615371"></a>desc</strong>, indicating that the replication consistency groups are sorted by descending order.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row9021196"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079692911_p59628243"><a name="en-us_topic_0079692911_p59628243"></a><a name="en-us_topic_0079692911_p59628243"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079692911_p5895390811267"><a name="en-us_topic_0079692911_p5895390811267"></a><a name="en-us_topic_0079692911_p5895390811267"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079692911_p43339000"><a name="en-us_topic_0079692911_p43339000"></a><a name="en-us_topic_0079692911_p43339000"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079692911_p20798117"><a name="en-us_topic_0079692911_p20798117"></a><a name="en-us_topic_0079692911_p20798117"></a>Specifies the offset.</p>
    </td>
    </tr>
    <tr id="row2264966812320"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p55512933123242"><a name="p55512933123242"></a><a name="p55512933123242"></a>changes-since</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p253728123242"><a name="p253728123242"></a><a name="p253728123242"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p20551983123242"><a name="p20551983123242"></a><a name="p20551983123242"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="p54097915123242"><a name="p54097915123242"></a><a name="p54097915123242"></a>Specifies to query all the replication consistency groups that have been updated from the specified time point to the current time.</p>
    </td>
    </tr>
    <tr id="row1779215012323"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p44476868123242"><a name="p44476868123242"></a><a name="p44476868123242"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p45856550123242"><a name="p45856550123242"></a><a name="p45856550123242"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p23393056123242"><a name="p23393056123242"></a><a name="p23393056123242"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="p15789403123242"><a name="p15789403123242"></a><a name="p15789403123242"></a>Specifies the name of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="row5851136312327"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p34859511123242"><a name="p34859511123242"></a><a name="p34859511123242"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p5048138123242"><a name="p5048138123242"></a><a name="p5048138123242"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p6246042123242"><a name="p6246042123242"></a><a name="p6246042123242"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="p36167374123242"><a name="p36167374123242"></a><a name="p36167374123242"></a>Specifies the status of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="row11730812123239"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p48533413123242"><a name="p48533413123242"></a><a name="p48533413123242"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p38892351123242"><a name="p38892351123242"></a><a name="p38892351123242"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p63272709123242"><a name="p63272709123242"></a><a name="p63272709123242"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="p24815841123242"><a name="p24815841123242"></a><a name="p24815841123242"></a>Specifies the primary site of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="row38742139112849"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p46145988112852"><a name="p46145988112852"></a><a name="p46145988112852"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p46837508112852"><a name="p46837508112852"></a><a name="p46837508112852"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p35741776112852"><a name="p35741776112852"></a><a name="p35741776112852"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.5.1.4 "><p id="p9402769112852"><a name="p9402769112852"></a><a name="p9402769112852"></a>Specifies the ID of an EVS disk.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    None


## Response<a name="en-us_topic_0079692911_section35025494"></a>

-   Parameter description

    <a name="en-us_topic_0079692911_table10429724"></a>
    <table><thead align="left"><tr id="en-us_topic_0079692911_row12329649"><th class="cellrowborder" valign="top" width="31.080000000000002%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079692911_p23717325112645"><a name="en-us_topic_0079692911_p23717325112645"></a><a name="en-us_topic_0079692911_p23717325112645"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.97%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079692911_p51025866112645"><a name="en-us_topic_0079692911_p51025866112645"></a><a name="en-us_topic_0079692911_p51025866112645"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.95%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079692911_p39454467112645"><a name="en-us_topic_0079692911_p39454467112645"></a><a name="en-us_topic_0079692911_p39454467112645"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11855113192114"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="p785511310214"><a name="p785511310214"></a><a name="p785511310214"></a>replication_consistency_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p98552013102110"><a name="p98552013102110"></a><a name="p98552013102110"></a>List&lt;replication_consistency_group&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p1855613192117"><a name="p1855613192117"></a><a name="p1855613192117"></a>Specifies the replication consistency groups.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row1984791"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692911_p26550365"><a name="en-us_topic_0079692911_p26550365"></a><a name="en-us_topic_0079692911_p26550365"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692911_p49448848"><a name="en-us_topic_0079692911_p49448848"></a><a name="en-us_topic_0079692911_p49448848"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692911_p45933772"><a name="en-us_topic_0079692911_p45933772"></a><a name="en-us_topic_0079692911_p45933772"></a>Specifies the ID of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row10750772"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692911_p65506178"><a name="en-us_topic_0079692911_p65506178"></a><a name="en-us_topic_0079692911_p65506178"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692911_p20869327"><a name="en-us_topic_0079692911_p20869327"></a><a name="en-us_topic_0079692911_p20869327"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692911_p12693918"><a name="en-us_topic_0079692911_p12693918"></a><a name="en-us_topic_0079692911_p12693918"></a>Specifies the name of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row47136405"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692911_p59952436"><a name="en-us_topic_0079692911_p59952436"></a><a name="en-us_topic_0079692911_p59952436"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692911_p22882960"><a name="en-us_topic_0079692911_p22882960"></a><a name="en-us_topic_0079692911_p22882960"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692911_p41580444"><a name="en-us_topic_0079692911_p41580444"></a><a name="en-us_topic_0079692911_p41580444"></a>Specifies the description of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row38679683"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692911_p46046605"><a name="en-us_topic_0079692911_p46046605"></a><a name="en-us_topic_0079692911_p46046605"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692911_p54783372"><a name="en-us_topic_0079692911_p54783372"></a><a name="en-us_topic_0079692911_p54783372"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692911_p8268111"><a name="en-us_topic_0079692911_p8268111"></a><a name="en-us_topic_0079692911_p8268111"></a>Specifies the status of the replication consistency group. For details, see <a href="replication-consistency-group-status-(deprecated).md">Replication Consistency Group Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row7304143"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692911_p54764719"><a name="en-us_topic_0079692911_p54764719"></a><a name="en-us_topic_0079692911_p54764719"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692911_p10465156"><a name="en-us_topic_0079692911_p10465156"></a><a name="en-us_topic_0079692911_p10465156"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692911_p42371273"><a name="en-us_topic_0079692911_p42371273"></a><a name="en-us_topic_0079692911_p42371273"></a>Specifies the primary site.</p>
    </td>
    </tr>
    <tr id="row27595198121350"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="p1793278121416"><a name="p1793278121416"></a><a name="p1793278121416"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p21648333121416"><a name="p21648333121416"></a><a name="p21648333121416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p8684566121416"><a name="p8684566121416"></a><a name="p8684566121416"></a>Specifies the replication type of the replication consistency group.</p>
    </td>
    </tr>
    <tr id="row55336518121353"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="p1776836121425"><a name="p1776836121425"></a><a name="p1776836121425"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p47991944121425"><a name="p47991944121425"></a><a name="p47991944121425"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p62142295121425"><a name="p62142295121425"></a><a name="p62142295121425"></a>Specifies the replication status of the replication consistency group. For details, see <a href="replication-consistency-group-status-(deprecated).md">Replication Consistency Group Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row36951558121356"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="p62149492121432"><a name="p62149492121432"></a><a name="p62149492121432"></a>replication_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p36839689121432"><a name="p36839689121432"></a><a name="p36839689121432"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p15606360121432"><a name="p15606360121432"></a><a name="p15606360121432"></a>Specifies the IDs of all EVS replication pairs in the replication consistency group.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row45797138"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692911_p18580737"><a name="en-us_topic_0079692911_p18580737"></a><a name="en-us_topic_0079692911_p18580737"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692911_p38524289"><a name="en-us_topic_0079692911_p38524289"></a><a name="en-us_topic_0079692911_p38524289"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692911_p33459681"><a name="en-us_topic_0079692911_p33459681"></a><a name="en-us_topic_0079692911_p33459681"></a>Specifies the creation time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079692911_row32701678"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079692911_p31590262"><a name="en-us_topic_0079692911_p31590262"></a><a name="en-us_topic_0079692911_p31590262"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079692911_p31541268"><a name="en-us_topic_0079692911_p31541268"></a><a name="en-us_topic_0079692911_p31541268"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079692911_p4705914"><a name="en-us_topic_0079692911_p4705914"></a><a name="en-us_topic_0079692911_p4705914"></a>Specifies the latest update time.</p>
    </td>
    </tr>
    <tr id="row6422788112955"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="p3427373111302"><a name="p3427373111302"></a><a name="p3427373111302"></a>failure_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p5525583111302"><a name="p5525583111302"></a><a name="p5525583111302"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p4653732611302"><a name="p4653732611302"></a><a name="p4653732611302"></a>Specifies the returned error code if the status of the replication consistency group is <strong id="b842352706173222"><a name="b842352706173222"></a><a name="b842352706173222"></a>error</strong>. For details, see <a href="details-of-evs-replication-failure_detail-values-(deprecated).md">Details of EVS Replication failure_detail Values (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="row1481212554561"><td class="cellrowborder" valign="top" width="31.080000000000002%" headers="mcps1.1.4.1.1 "><p id="p3193205912567"><a name="p3193205912567"></a><a name="p3193205912567"></a>fault_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p6193165985616"><a name="p6193165985616"></a><a name="p6193165985616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><div class="p" id="p1919345911565"><a name="p1919345911565"></a><a name="p1919345911565"></a>Specifies the fault level of the replication consistency group. The value can be as follows:<a name="ul1837105465719"></a><a name="ul1837105465719"></a><ul id="ul1837105465719"><li><strong id="b84235270620364"><a name="b84235270620364"></a><a name="b84235270620364"></a>0</strong>: indicates that no fault occurs.</li><li><strong id="b842352706203620"><a name="b842352706203620"></a><a name="b842352706203620"></a>2</strong>: indicates that a production disk in the replication consistency group does not have read/write permissions. In this case, you are advised to perform a failover.</li><li><strong id="b84235270620377"><a name="b84235270620377"></a><a name="b84235270620377"></a>5</strong>: indicates that the replication link is disconnected. In this case, a failover cannot be performed. Contact technical support engineers.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {  
        "replication_consistency_groups": [  
       { 
                "status": "available", 
                "priority_station": "az3.dc3", 
                "replication_ids": [ 
                    "86080dc0-2fcf-4b85-8102-bc123eb8dcaa", 
                    "580b730e-3160-4382-8a4e-174515d1fa77" 
                ], 
                "name": "replication consistency group", 
                "replication_model": "hypermetro",
                "fault_level": "0", 
                "updated_at": "2017-11-28T07:17:21.904376", 
                "created_at": "2017-11-28T03:05:10.677939", 
                "replication_status": "active-stopped", 
                "id": "57b84092-7a75-4e22-bc2a-fab0bec547c5", 
                "description": "replication consistency group" 
            }, 
            { 
                "status": "available", 
                "priority_station": "az3.dc3", 
                "replication_ids": [ 
                    "3e9ba31c-6406-4060-870e-b7736ac76836", 
                    "6690b30a-b40c-4a50-bd4a-7e5c1e28b821" 
                ], 
                "name": "replication consistency group", 
                "replication_model": "hypermetro",
                "fault_level": "0", 
                "updated_at": "2017-11-28T06:29:27.155762", 
                "created_at": "2017-11-27T11:38:50.421364", 
                "replication_status": "active", 
                "id": "13b582e6-092e-4f7a-9260-8eb7a4ad860e", 
                "description": "replication consistency group" 
            } 
        ]  
    }
    ```


## Status Codes<a name="en-us_topic_0079692911_section46793998"></a>

-   Normal

    <a name="evs_04_2046_table4315991194956"></a>
    <table><thead align="left"><tr id="evs_04_2046_row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="evs_04_2046_p1363125894956"><a name="evs_04_2046_p1363125894956"></a><a name="evs_04_2046_p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="evs_04_2046_p3039012494956"><a name="evs_04_2046_p3039012494956"></a><a name="evs_04_2046_p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2046_row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="evs_04_2046_p847584694956"><a name="evs_04_2046_p847584694956"></a><a name="evs_04_2046_p847584694956"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="evs_04_2046_p1545496394956"><a name="evs_04_2046_p1545496394956"></a><a name="evs_04_2046_p1545496394956"></a>The server has processed the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="evs_04_2044_table22458872203835"></a>
    <table><thead align="left"><tr id="evs_04_2044_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="evs_04_2044_p6387753203835"><a name="evs_04_2044_p6387753203835"></a><a name="evs_04_2044_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="evs_04_2044_p47646009203835"><a name="evs_04_2044_p47646009203835"></a><a name="evs_04_2044_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2044_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p12381163203835"><a name="evs_04_2044_p12381163203835"></a><a name="evs_04_2044_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p63350108203835"><a name="evs_04_2044_p63350108203835"></a><a name="evs_04_2044_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p11330608203835"><a name="evs_04_2044_p11330608203835"></a><a name="evs_04_2044_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p45364094203835"><a name="evs_04_2044_p45364094203835"></a><a name="evs_04_2044_p45364094203835"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p52863895203835"><a name="evs_04_2044_p52863895203835"></a><a name="evs_04_2044_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p54117066203835"><a name="evs_04_2044_p54117066203835"></a><a name="evs_04_2044_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p58438642203835"><a name="evs_04_2044_p58438642203835"></a><a name="evs_04_2044_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p35909542203835"><a name="evs_04_2044_p35909542203835"></a><a name="evs_04_2044_p35909542203835"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p5599455203835"><a name="evs_04_2044_p5599455203835"></a><a name="evs_04_2044_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p50902717203835"><a name="evs_04_2044_p50902717203835"></a><a name="evs_04_2044_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p63988484203835"><a name="evs_04_2044_p63988484203835"></a><a name="evs_04_2044_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p15684678203835"><a name="evs_04_2044_p15684678203835"></a><a name="evs_04_2044_p15684678203835"></a>The response generated by the server cannot be accepted by the client.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p25623884203835"><a name="evs_04_2044_p25623884203835"></a><a name="evs_04_2044_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p62268733203835"><a name="evs_04_2044_p62268733203835"></a><a name="evs_04_2044_p62268733203835"></a>You must use the proxy server for authentication. Then, the request can be processed.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p28314670203835"><a name="evs_04_2044_p28314670203835"></a><a name="evs_04_2044_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p11786919203835"><a name="evs_04_2044_p11786919203835"></a><a name="evs_04_2044_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p2729702203835"><a name="evs_04_2044_p2729702203835"></a><a name="evs_04_2044_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p19779281203835"><a name="evs_04_2044_p19779281203835"></a><a name="evs_04_2044_p19779281203835"></a>The request cannot be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p57799353203835"><a name="evs_04_2044_p57799353203835"></a><a name="evs_04_2044_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p51235984203835"><a name="evs_04_2044_p51235984203835"></a><a name="evs_04_2044_p51235984203835"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p38504500203835"><a name="evs_04_2044_p38504500203835"></a><a name="evs_04_2044_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p31856770203835"><a name="evs_04_2044_p31856770203835"></a><a name="evs_04_2044_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p3918444203835"><a name="evs_04_2044_p3918444203835"></a><a name="evs_04_2044_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p48958538203835"><a name="evs_04_2044_p48958538203835"></a><a name="evs_04_2044_p48958538203835"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p55967806203835"><a name="evs_04_2044_p55967806203835"></a><a name="evs_04_2044_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p37098455203835"><a name="evs_04_2044_p37098455203835"></a><a name="evs_04_2044_p37098455203835"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="evs_04_2044_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="evs_04_2044_p67010448203835"><a name="evs_04_2044_p67010448203835"></a><a name="evs_04_2044_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="evs_04_2044_p59137180203835"><a name="evs_04_2044_p59137180203835"></a><a name="evs_04_2044_p59137180203835"></a>A gateway timeout error occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


