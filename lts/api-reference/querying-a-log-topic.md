# Querying a Log Topic<a name="lts_02_0008"></a>

## Function<a name="section13262100202410"></a>

This function describes how to query a log group you have created to obtain the name, ID, expiration time, and creation time of the log group.

## URI<a name="section31681806"></a>

-   URI format

    GET /v2.0/\{project\_id\}/log-groups/\{group\_id\}/log-topics/\{topic\_id\}


-   Parameter description

    **Table  1**  Parameter description

    <a name="table805068"></a>
    <table><thead align="left"><tr id="row57933110"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p39489582428"><a name="p39489582428"></a><a name="p39489582428"></a><strong id="b12403115915814"><a name="b12403115915814"></a><a name="b12403115915814"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p394816582427"><a name="p394816582427"></a><a name="p394816582427"></a><strong id="b204011214911"><a name="b204011214911"></a><a name="b204011214911"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p1494835804214"><a name="p1494835804214"></a><a name="p1494835804214"></a><strong id="b1037483398"><a name="b1037483398"></a><a name="b1037483398"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p5948158184213"><a name="p5948158184213"></a><a name="p5948158184213"></a><strong id="b12371341915"><a name="b12371341915"></a><a name="b12371341915"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19139995"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12949115814421"><a name="p12949115814421"></a><a name="p12949115814421"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2949195894219"><a name="p2949195894219"></a><a name="p2949195894219"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p294911584424"><a name="p294911584424"></a><a name="p294911584424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p129498583422"><a name="p129498583422"></a><a name="p129498583422"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row8975271"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1294955816424"><a name="p1294955816424"></a><a name="p1294955816424"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1794916588423"><a name="p1794916588423"></a><a name="p1794916588423"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1394955813422"><a name="p1394955813422"></a><a name="p1394955813422"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p4949155824210"><a name="p4949155824210"></a><a name="p4949155824210"></a>Specifies the log group ID.</p>
    </td>
    </tr>
    <tr id="row19973124944214"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1949458144212"><a name="p1949458144212"></a><a name="p1949458144212"></a>topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p20949125820420"><a name="p20949125820420"></a><a name="p20949125820420"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p159491458124217"><a name="p159491458124217"></a><a name="p159491458124217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1394955864216"><a name="p1394955864216"></a><a name="p1394955864216"></a>Specifies the log topic ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section16700806"></a>

-   Request parameters

    None

-   Example request

    ```
    GET /v2.0/{project_id}/log-groups/{group_id}/log-topics/{topic_id}
    ```


## Response<a name="section16089528"></a>

-   Response parameters

    **Table  2**  Parameter description

    <a name="table894955330"></a>
    <table><thead align="left"><tr id="row396125513310"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p10735906504"><a name="p10735906504"></a><a name="p10735906504"></a><strong id="b1689691817108"><a name="b1689691817108"></a><a name="b1689691817108"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p107353013504"><a name="p107353013504"></a><a name="p107353013504"></a><strong id="b1724720217107"><a name="b1724720217107"></a><a name="b1724720217107"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p273530165013"><a name="p273530165013"></a><a name="p273530165013"></a><strong id="b12145023131013"><a name="b12145023131013"></a><a name="b12145023131013"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p137351504505"><a name="p137351504505"></a><a name="p137351504505"></a><strong id="b313592471017"><a name="b313592471017"></a><a name="b313592471017"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4961055739"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p165468114508"><a name="p165468114508"></a><a name="p165468114508"></a>log_topic_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p19546911175015"><a name="p19546911175015"></a><a name="p19546911175015"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p55461211165011"><a name="p55461211165011"></a><a name="p55461211165011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p15546171114507"><a name="p15546171114507"></a><a name="p15546171114507"></a>Specifies the log topic name.</p>
    </td>
    </tr>
    <tr id="row1296185518312"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p454691175011"><a name="p454691175011"></a><a name="p454691175011"></a>creation_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p454611125019"><a name="p454611125019"></a><a name="p454611125019"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p0546171111508"><a name="p0546171111508"></a><a name="p0546171111508"></a>Int64</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p155465118505"><a name="p155465118505"></a><a name="p155465118505"></a>Specifies the log group creation time.</p>
    </td>
    </tr>
    <tr id="row669372916492"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p054681125013"><a name="p054681125013"></a><a name="p054681125013"></a>index_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p125461811185017"><a name="p125461811185017"></a><a name="p125461811185017"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p454611117504"><a name="p454611117504"></a><a name="p454611117504"></a>Bool</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p5546181175014"><a name="p5546181175014"></a><a name="p5546181175014"></a>Specifies the search switch.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
           "log_topic_name": "lts-topic-jgpv", 
           "creation_time": 1550803822973, 
           "index_enabled": true
    }
    ```


## Returned Value<a name="section10588031"></a>

-   Normal

    200

-   Abnormal

    For details, see  [Status Code](status-code.md).


