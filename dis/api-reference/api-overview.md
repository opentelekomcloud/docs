# API Overview<a name="dis_02_0200"></a>

The DIS API is a self-developed API that complies with REST API design specifications. DIS provides the functions listed in  [Table 1](#table6550431105030)  through the DIS API.

**Table  1**  API functions

<a name="table6550431105030"></a>
<table><thead align="left"><tr id="row1547110105030"><th class="cellrowborder" valign="top" width="22.439999999999998%" id="mcps1.2.4.1.1"><p id="p54101492105030"><a name="p54101492105030"></a><a name="p54101492105030"></a>API Name</p>
</th>
<th class="cellrowborder" valign="top" width="28.439999999999998%" id="mcps1.2.4.1.2"><p id="p20144750105030"><a name="p20144750105030"></a><a name="p20144750105030"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="49.120000000000005%" id="mcps1.2.4.1.3"><p id="p21112044105030"><a name="p21112044105030"></a><a name="p21112044105030"></a>API URI</p>
</th>
</tr>
</thead>
<tbody><tr id="row55790672105030"><td class="cellrowborder" rowspan="4" valign="top" width="22.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p19630156303"><a name="p19630156303"></a><a name="p19630156303"></a>Stream management</p>
<p id="p726519334222"><a name="p726519334222"></a><a name="p726519334222"></a></p>
<p id="p92651433102210"><a name="p92651433102210"></a><a name="p92651433102210"></a></p>
<p id="p8265733172210"><a name="p8265733172210"></a><a name="p8265733172210"></a></p>
<p id="p705174586"><a name="p705174586"></a><a name="p705174586"></a></p>
<p id="p65859208585"><a name="p65859208585"></a><a name="p65859208585"></a></p>
<p id="p11462112118165"><a name="p11462112118165"></a><a name="p11462112118165"></a></p>
<p id="p1346302171614"><a name="p1346302171614"></a><a name="p1346302171614"></a></p>
<p id="p4463132131613"><a name="p4463132131613"></a><a name="p4463132131613"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.439999999999998%" headers="mcps1.2.4.1.2 "><p id="p30859977105030"><a name="p30859977105030"></a><a name="p30859977105030"></a><a href="creating-a-dis-stream.md">Creating a DIS Stream</a></p>
</td>
<td class="cellrowborder" valign="top" width="49.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p1597883515203"><a name="p1597883515203"></a><a name="p1597883515203"></a>POST /v2/{project_id}/streams</p>
</td>
</tr>
<tr id="row15453874105030"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p58483711105030"><a name="p58483711105030"></a><a name="p58483711105030"></a><a href="deleting-a-dis-stream.md">Deleting a DIS Stream</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p128074072110"><a name="p128074072110"></a><a name="p128074072110"></a>DELETE /v2/{project_id}/streams</p>
</td>
</tr>
<tr id="row10170161211814"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p101711112111819"><a name="p101711112111819"></a><a name="p101711112111819"></a><a href="listing-dis-streams.md">Listing DIS Streams</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p51711512151819"><a name="p51711512151819"></a><a name="p51711512151819"></a>GET /v2/{project_id}/streams</p>
</td>
</tr>
<tr id="row125219148184"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p852121401818"><a name="p852121401818"></a><a name="p852121401818"></a><a href="viewing-details-of-a-dis-stream.md">Viewing Details of a DIS Stream</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1752141418185"><a name="p1752141418185"></a><a name="p1752141418185"></a>GET /v2/{project_id}/streams/{stream_name}</p>
</td>
</tr>
<tr id="row3325121711183"><td class="cellrowborder" rowspan="3" valign="top" width="22.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p1632551711184"><a name="p1632551711184"></a><a name="p1632551711184"></a>Data management</p>
</td>
<td class="cellrowborder" valign="top" width="28.439999999999998%" headers="mcps1.2.4.1.2 "><p id="p13325417181816"><a name="p13325417181816"></a><a name="p13325417181816"></a><a href="uploading-data-to-a-dis-stream.md">Uploading Data to a DIS Stream</a></p>
</td>
<td class="cellrowborder" valign="top" width="49.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p1325151720181"><a name="p1325151720181"></a><a name="p1325151720181"></a>POST /v2/{project_id}/records</p>
</td>
</tr>
<tr id="row4113320191811"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p511382051817"><a name="p511382051817"></a><a name="p511382051817"></a><a href="downloading-data-from-a-dis-stream.md">Downloading Data from a DIS Stream</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1311312207183"><a name="p1311312207183"></a><a name="p1311312207183"></a>GET /v2/{project_id}/records{?partition-cursor}</p>
</td>
</tr>
<tr id="row39325181815"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p209162514186"><a name="p209162514186"></a><a name="p209162514186"></a><a href="obtaining-a-cursor.md">Obtaining a Cursor</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6922581818"><a name="p6922581818"></a><a name="p6922581818"></a>GET /v2/{project_id}/cursors{?stream-name,partition-id,cursor-type,starting-sequence-number}</p>
</td>
</tr>
<tr id="row1878113271184"><td class="cellrowborder" rowspan="2" valign="top" width="22.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p67811027161812"><a name="p67811027161812"></a><a name="p67811027161812"></a>Program management</p>
<p id="p139581917104719"><a name="p139581917104719"></a><a name="p139581917104719"></a></p>
<p id="p206952020104720"><a name="p206952020104720"></a><a name="p206952020104720"></a></p>
<p id="p6169816145711"><a name="p6169816145711"></a><a name="p6169816145711"></a></p>
<p id="p177843183572"><a name="p177843183572"></a><a name="p177843183572"></a></p>
<p id="p983921031710"><a name="p983921031710"></a><a name="p983921031710"></a></p>
<p id="p16839410201713"><a name="p16839410201713"></a><a name="p16839410201713"></a></p>
<p id="p8531171410251"><a name="p8531171410251"></a><a name="p8531171410251"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.439999999999998%" headers="mcps1.2.4.1.2 "><p id="p1878102721819"><a name="p1878102721819"></a><a name="p1878102721819"></a><a href="creating-an-application.md">Creating an Application</a></p>
</td>
<td class="cellrowborder" valign="top" width="49.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p19781112721813"><a name="p19781112721813"></a><a name="p19781112721813"></a>POST /v2/{project_id}/apps</p>
</td>
</tr>
<tr id="row394773371812"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p79471433141818"><a name="p79471433141818"></a><a name="p79471433141818"></a><a href="deleting-an-application.md">Deleting an Application</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p4947143319180"><a name="p4947143319180"></a><a name="p4947143319180"></a>DELETE /v2/{project_id}/apps/{app_name}</p>
</td>
</tr>
<tr id="row2988114415189"><td class="cellrowborder" rowspan="2" valign="top" width="22.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p598834401813"><a name="p598834401813"></a><a name="p598834401813"></a>Checkpoint management</p>
<p id="p83251331175714"><a name="p83251331175714"></a><a name="p83251331175714"></a></p>
<p id="p924413404256"><a name="p924413404256"></a><a name="p924413404256"></a></p>
</td>
<td class="cellrowborder" valign="top" width="28.439999999999998%" headers="mcps1.2.4.1.2 "><p id="p1798817449182"><a name="p1798817449182"></a><a name="p1798817449182"></a><a href="adding-a-checkpoint.md">Adding a Checkpoint</a></p>
</td>
<td class="cellrowborder" valign="top" width="49.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p39881344151812"><a name="p39881344151812"></a><a name="p39881344151812"></a>POST /v2/{project_id}/checkpoints</p>
</td>
</tr>
<tr id="row91605423181"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p16160184291811"><a name="p16160184291811"></a><a name="p16160184291811"></a><a href="querying-a-checkpoint.md">Querying a Checkpoint</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p16161144217183"><a name="p16161144217183"></a><a name="p16161144217183"></a>GET /v2/{project_id}/checkpoints{?stream_name,partition_id,app_name,checkpoint_type}</p>
</td>
</tr>
<tr id="row17480154213415"><td class="cellrowborder" rowspan="6" valign="top" width="22.439999999999998%" headers="mcps1.2.4.1.1 "><p id="p2417112158"><a name="p2417112158"></a><a name="p2417112158"></a>Tag management</p>
</td>
<td class="cellrowborder" valign="top" width="28.439999999999998%" headers="mcps1.2.4.1.2 "><p id="p2048010421444"><a name="p2048010421444"></a><a name="p2048010421444"></a><a href="adding-a-tag-to-a-specified-stream.md">Adding a Tag to a Specified Stream</a></p>
</td>
<td class="cellrowborder" valign="top" width="49.120000000000005%" headers="mcps1.2.4.1.3 "><p id="p204802424413"><a name="p204802424413"></a><a name="p204802424413"></a>POST /v1.1/{project_id}/stream/{stream_id}/tags</p>
</td>
</tr>
<tr id="row49181344947"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p12918124414410"><a name="p12918124414410"></a><a name="p12918124414410"></a><a href="deleting-a-tag-of-a-specified-stream.md">Deleting a Tag of a Specified Stream</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1691824419417"><a name="p1691824419417"></a><a name="p1691824419417"></a>DELETE /v1.1/{project_id}/stream/{stream_id}/tags/{key}</p>
</td>
</tr>
<tr id="row6261124717410"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1026118471443"><a name="p1026118471443"></a><a name="p1026118471443"></a><a href="querying-a-tag-of-a-specified-stream.md">Querying a Tag of a Specified Stream</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1626124716413"><a name="p1626124716413"></a><a name="p1626124716413"></a>GET /v1.1/{project_id}/stream/{stream_id}/tags</p>
</td>
</tr>
<tr id="row1413675012419"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1113645014411"><a name="p1113645014411"></a><a name="p1113645014411"></a><a href="adding-or-deleting-stream-tags-in-batches.md">Adding or Deleting Stream Tags in Batches</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p8136150443"><a name="p8136150443"></a><a name="p8136150443"></a>POST /v1.1/{project_id}/stream/{stream_id}/tags/action</p>
</td>
</tr>
<tr id="row19495853645"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1149517535413"><a name="p1149517535413"></a><a name="p1149517535413"></a><a href="querying-all-tags.md">Querying All Tags</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p14495853343"><a name="p14495853343"></a><a name="p14495853343"></a>GET /v1.1/{project_id}/stream/tags</p>
</td>
</tr>
<tr id="row144321561345"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p34321456741"><a name="p34321456741"></a><a name="p34321456741"></a><a href="querying-a-list-of-streams-with-specified-tags.md">Querying a List of Streams with Specified Tags</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p104328560412"><a name="p104328560412"></a><a name="p104328560412"></a>POST /v1.1/{project_id}/stream/resource_instances/action</p>
</td>
</tr>
</tbody>
</table>

