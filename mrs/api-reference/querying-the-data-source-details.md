# Querying the Data Source Details<a name="EN-US_TOPIC_0172486221"></a>

## Function<a name="section11410068144834"></a>

This API is used to query detailed information about a data source. This API is compatible with Sahara.

## URI<a name="section4721807314497"></a>

-   Format

    GET /v1.1/\{project\_id\}/data-sources/\{data\_source\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16571835194812"><a name="p16571835194812"></a><a name="p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p141410194812"><a name="p141410194812"></a><a name="p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11454278194812"><a name="p11454278194812"></a><a name="p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6505449415356"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3492262515356"><a name="p3492262515356"></a><a name="p3492262515356"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1016041415356"><a name="p1016041415356"></a><a name="p1016041415356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row20659256153330"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p62787041153330"><a name="p62787041153330"></a><a name="p62787041153330"></a>data_source_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p52585595153330"><a name="p52585595153330"></a><a name="p52585595153330"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p31574830153330"><a name="p31574830153330"></a><a name="p31574830153330"></a>Data source ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section31697334144924"></a>

**Request parameters**

None.

## Response<a name="section10069032144933"></a>

**Table  2**  Response parameter description

<a name="table51257841151049"></a>
<table><thead align="left"><tr id="row8480851151049"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p15860319151049"><a name="p15860319151049"></a><a name="p15860319151049"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p40813771151049"><a name="p40813771151049"></a><a name="p40813771151049"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p17581180151049"><a name="p17581180151049"></a><a name="p17581180151049"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20438892151640"><a name="p20438892151640"></a><a name="p20438892151640"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16062920151640"><a name="p16062920151640"></a><a name="p16062920151640"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p26028163151640"><a name="p26028163151640"></a><a name="p26028163151640"></a>Whether the data source is public</p>
<a name="ul35290564102533"></a><a name="ul35290564102533"></a><ul id="ul35290564102533"><li>true</li><li>false</li></ul>
<p id="p24126416102533"><a name="p24126416102533"></a><a name="p24126416102533"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row1794513155918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p25070059155926"><a name="p25070059155926"></a><a name="p25070059155926"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p835343155926"><a name="p835343155926"></a><a name="p835343155926"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p81141338103617"><a name="p81141338103617"></a><a name="p81141338103617"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row66462107155939"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p42920418155947"><a name="p42920418155947"></a><a name="p42920418155947"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p12070089155947"><a name="p12070089155947"></a><a name="p12070089155947"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p38153149155947"><a name="p38153149155947"></a><a name="p38153149155947"></a>Whether the data source is protected</p>
<a name="ul52779881153338"></a><a name="ul52779881153338"></a><ul id="ul52779881153338"><li>true</li><li>false</li></ul>
<p id="p23154383153338"><a name="p23154383153338"></a><a name="p23154383153338"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row23363161601"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6056003416010"><a name="p6056003416010"></a><a name="p6056003416010"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4991056416010"><a name="p4991056416010"></a><a name="p4991056416010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1622389816010"><a name="p1622389816010"></a><a name="p1622389816010"></a>Data source creation time</p>
</td>
</tr>
<tr id="row8652083151249"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p29730140151249"><a name="p29730140151249"></a><a name="p29730140151249"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p17113312151828"><a name="p17113312151828"></a><a name="p17113312151828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p39995064151249"><a name="p39995064151249"></a><a name="p39995064151249"></a>Data source ID</p>
</td>
</tr>
<tr id="row12228393151256"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p50975775151256"><a name="p50975775151256"></a><a name="p50975775151256"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p21869845151828"><a name="p21869845151828"></a><a name="p21869845151828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43580859151256"><a name="p43580859151256"></a><a name="p43580859151256"></a>Data source name</p>
</td>
</tr>
<tr id="row4419889616034"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2334078616034"><a name="p2334078616034"></a><a name="p2334078616034"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6358268516034"><a name="p6358268516034"></a><a name="p6358268516034"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p4992386116034"><a name="p4992386116034"></a><a name="p4992386116034"></a>Data source update time</p>
</td>
</tr>
<tr id="row1546567016045"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2185314916152"><a name="p2185314916152"></a><a name="p2185314916152"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p3397791716152"><a name="p3397791716152"></a><a name="p3397791716152"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p74792916152"><a name="p74792916152"></a><a name="p74792916152"></a>Data source description</p>
</td>
</tr>
<tr id="row2803391316050"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p836939816152"><a name="p836939816152"></a><a name="p836939816152"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1657456216152"><a name="p1657456216152"></a><a name="p1657456216152"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p36224816152"><a name="p36224816152"></a><a name="p36224816152"></a>Data source URL</p>
</td>
</tr>
<tr id="row101826416056"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p40975601628"><a name="p40975601628"></a><a name="p40975601628"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p405511081628"><a name="p405511081628"></a><a name="p405511081628"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p634143291628"><a name="p634143291628"></a><a name="p634143291628"></a>Data source type</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section14801515937"></a>

-   Example request

    None.


-   Example response

    ```
    {
        "data_source": {
            "name": "my-data-source-update",
            "type": "hdfs",
            "url": "/simple/mapreduce/input",
            "description": "this is the data source template",
            "created_at": "2017-06-22T08:28:57",
            "updated_at": "2017-06-22T08:30:08",
            "id": "e275a927-fe72-4b8b-a634-e47a11dca181",
            "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
            "is_public": false,
            "is_protected": false
        }
    }
    ```


## Status Code<a name="section13299747144948"></a>

[Table 3](#table1584477916050)  describes the status code of this API.

**Table  3**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>Data source details have been queried successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

