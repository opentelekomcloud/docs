# Creating a Manual Backup<a name="rds_09_0004"></a>

## Function<a name="section117711820496"></a>

This API is used to create a manual backup.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section5287193373915"></a>

-   Read replicas do not support manual backup creation.
-   The backup name must be unique.

## URI<a name="section12081471012"></a>

-   URI format

    POST https://\{_Endpoint_\}/v3/\{project\_id\}/backups

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/backups

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p53901255"><a name="p53901255"></a><a name="p53901255"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3925534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p17161892810"><a name="p17161892810"></a><a name="p17161892810"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section420839121019"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table202301459171110"></a>
    <table><thead align="left"><tr id="row823025911111"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.199999999999996%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.8%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2230759191118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4230195918114"><a name="p4230195918114"></a><a name="p4230195918114"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.199999999999996%" headers="mcps1.2.5.1.2 "><p id="p6230185941112"><a name="p6230185941112"></a><a name="p6230185941112"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.5.1.3 "><p id="p10230155931112"><a name="p10230155931112"></a><a name="p10230155931112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p02307591119"><a name="p02307591119"></a><a name="p02307591119"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row112306593118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8230105941111"><a name="p8230105941111"></a><a name="p8230105941111"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.199999999999996%" headers="mcps1.2.5.1.2 "><p id="p92301659121111"><a name="p92301659121111"></a><a name="p92301659121111"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.5.1.3 "><p id="p7230175920117"><a name="p7230175920117"></a><a name="p7230175920117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p123113599116"><a name="p123113599116"></a><a name="p123113599116"></a>Specifies the backup name. It must be 4 to 64 characters in length and start with a letter. It is case-sensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    <p id="p17357102816399"><a name="p17357102816399"></a><a name="p17357102816399"></a>The backup name must be unique.</p>
    </td>
    </tr>
    <tr id="row15231185918118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1223185918111"><a name="p1223185918111"></a><a name="p1223185918111"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.199999999999996%" headers="mcps1.2.5.1.2 "><p id="p182311759171117"><a name="p182311759171117"></a><a name="p182311759171117"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.5.1.3 "><p id="p1823155941110"><a name="p1823155941110"></a><a name="p1823155941110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1767465913384"><a name="p1767465913384"></a><a name="p1767465913384"></a>Specifies the backup description. It contains a maximum of 256 characters and cannot contain the following special characters: &gt;!&lt;"&amp;'=</p>
    </td>
    </tr>
    <tr id="row12312590112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p223118596112"><a name="p223118596112"></a><a name="p223118596112"></a>databases</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.199999999999996%" headers="mcps1.2.5.1.2 "><p id="p5231115951110"><a name="p5231115951110"></a><a name="p5231115951110"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.5.1.3 "><p id="p1423120591112"><a name="p1423120591112"></a><a name="p1423120591112"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p14506444145712"><a name="p14506444145712"></a><a name="p14506444145712"></a>Specifies a list of self-built Microsoft SQL Server databases that are partially backed up. (Only Microsoft SQL Server support partial backups.)</p>
    <p id="p3671141614219"><a name="p3671141614219"></a><a name="p3671141614219"></a>For details, see <a href="#table917312715167">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  databases field data structure description

    <a name="table917312715167"></a>
    <table><thead align="left"><tr id="row517382720169"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p8770145810165"><a name="p8770145810165"></a><a name="p8770145810165"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.82%" id="mcps1.2.5.1.2"><p id="p977017582168"><a name="p977017582168"></a><a name="p977017582168"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.18%" id="mcps1.2.5.1.3"><p id="p877117581162"><a name="p877117581162"></a><a name="p877117581162"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p877215584161"><a name="p877215584161"></a><a name="p877215584161"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row91737272168"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p117795416175"><a name="p117795416175"></a><a name="p117795416175"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p67815471718"><a name="p67815471718"></a><a name="p67815471718"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.3 "><p id="p378117451712"><a name="p378117451712"></a><a name="p378117451712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p12173142714169"><a name="p12173142714169"></a><a name="p12173142714169"></a>Specifies the names of self-built databases.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    {
    	"instance_id": "d8e6ca5a624745bcb546a227aa3ae1cfin01",
    	"name": "backup",
    "description": "manual backup"
    }
    ```


## Response<a name="section1229512143106"></a>

-   Normal response

    **Table  4**  Parameter description

    <a name="table68261136172016"></a>
    <table><thead align="left"><tr id="row17826143612201"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p163303524208"><a name="p163303524208"></a><a name="p163303524208"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1133119521209"><a name="p1133119521209"></a><a name="p1133119521209"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p23321252122014"><a name="p23321252122014"></a><a name="p23321252122014"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row168268363208"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4826133632011"><a name="p4826133632011"></a><a name="p4826133632011"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p834134411411"><a name="p834134411411"></a><a name="p834134411411"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p20826183652017"><a name="p20826183652017"></a><a name="p20826183652017"></a>Indicates the backup information.</p>
    <p id="p414016219433"><a name="p414016219433"></a><a name="p414016219433"></a>For details, see <a href="#table153397472217">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  backup field data structure description

    <a name="table153397472217"></a>
    <table><thead align="left"><tr id="row1634420492210"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p11345749225"><a name="p11345749225"></a><a name="p11345749225"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p234611418224"><a name="p234611418224"></a><a name="p234611418224"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18348847226"><a name="p18348847226"></a><a name="p18348847226"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8899185920226"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3899105932211"><a name="p3899105932211"></a><a name="p3899105932211"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p78995598228"><a name="p78995598228"></a><a name="p78995598228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p289935912214"><a name="p289935912214"></a><a name="p289935912214"></a>Indicates the backup ID.</p>
    </td>
    </tr>
    <tr id="row13350204182216"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p183506462212"><a name="p183506462212"></a><a name="p183506462212"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12353144162213"><a name="p12353144162213"></a><a name="p12353144162213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1354204102218"><a name="p1354204102218"></a><a name="p1354204102218"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row9354247227"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5355543228"><a name="p5355543228"></a><a name="p5355543228"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14357104142214"><a name="p14357104142214"></a><a name="p14357104142214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p153585432217"><a name="p153585432217"></a><a name="p153585432217"></a>Indicates the backup name.</p>
    </td>
    </tr>
    <tr id="row9358174182213"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p835917492218"><a name="p835917492218"></a><a name="p835917492218"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p183602402212"><a name="p183602402212"></a><a name="p183602402212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1136119402219"><a name="p1136119402219"></a><a name="p1136119402219"></a>Indicates the backup description.</p>
    </td>
    </tr>
    <tr id="row163614412228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1236284122218"><a name="p1236284122218"></a><a name="p1236284122218"></a>databases</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p24228398437"><a name="p24228398437"></a><a name="p24228398437"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p93661240224"><a name="p93661240224"></a><a name="p93661240224"></a>Indicates a list of self-built Microsoft SQL Server databases that are partially backed up. (Only Microsoft SQL Server support partial backups.)</p>
    <p id="p5643320435"><a name="p5643320435"></a><a name="p5643320435"></a>For details, see <a href="#table917312715167">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row1692174318237"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6921543102310"><a name="p6921543102310"></a><a name="p6921543102310"></a>begin_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9921943202312"><a name="p9921943202312"></a><a name="p9921943202312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p292144316236"><a name="p292144316236"></a><a name="p292144316236"></a>Indicates the backup start time in the "yyyy-mm-ddThh:mm:ssZ" format, where "T" indicates the start time of the time field, and "Z" indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row17211154692312"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14211546182316"><a name="p14211546182316"></a><a name="p14211546182316"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10211146122315"><a name="p10211146122315"></a><a name="p10211146122315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10279105193013"><a name="p10279105193013"></a><a name="p10279105193013"></a>Indicates the backup status. Value:</p>
    <a name="ul15878173144414"></a><a name="ul15878173144414"></a><ul id="ul15878173144414"><li>BUILDING: Backup in progress</li><li>COMPLETED: Backup completed</li><li>FAILED: Backup failed</li><li>DELETING: Backup being deleted</li></ul>
    </td>
    </tr>
    <tr id="row13315349112319"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p131574962320"><a name="p131574962320"></a><a name="p131574962320"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p143153499234"><a name="p143153499234"></a><a name="p143153499234"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p72791553309"><a name="p72791553309"></a><a name="p72791553309"></a>Indicates the backup type. Value:</p>
    <a name="ul8290171310448"></a><a name="ul8290171310448"></a><ul id="ul8290171310448"><li>auto: automated full backup</li><li>manual: manual full backup</li><li>fragment: differential full backup</li><li>incremental: automated incremental backup</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example normal response

    ```
    {
    	"backup": {
    		"id": "2f4ddb93-b901-4b08-93d8-1d2e472f30fe",
    		"name": "backupDemo",
    		"description": "This is a description",
    		"begin_time": "2016-09-12T01:17:05",
    		"status": "BUILDING",
    		"type": "manual",
    		"instance_id": "d8e6ca5a624745bcb546a227aa3ae1cfin01"
    	}
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

