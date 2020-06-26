# Restoring Data to an Existing or Original DB Instance<a name="rds_09_0009"></a>

## Function<a name="section117711820496"></a>

This API is used to restore a database to an existing or the original DB instance.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section12081471012"></a>

-   URI format

    POST https://\{_Endpoint_\}/v3/\{project\_id\}/instances/recovery

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/instances/recovery

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
    <p id="p1574719483818"><a name="p1574719483818"></a><a name="p1574719483818"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
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
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2230759191118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4230195918114"><a name="p4230195918114"></a><a name="p4230195918114"></a>source</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6230185941112"><a name="p6230185941112"></a><a name="p6230185941112"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p10230155931112"><a name="p10230155931112"></a><a name="p10230155931112"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p02307591119"><a name="p02307591119"></a><a name="p02307591119"></a>Specifies the restoration information.</p>
    <p id="p17312173532"><a name="p17312173532"></a><a name="p17312173532"></a>For details, see <a href="#table15343138128">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row112306593118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8230105941111"><a name="p8230105941111"></a><a name="p8230105941111"></a>target</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p92301659121111"><a name="p92301659121111"></a><a name="p92301659121111"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p14598434729"><a name="p14598434729"></a><a name="p14598434729"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p123113599116"><a name="p123113599116"></a><a name="p123113599116"></a>Specifies the restoration target.</p>
    <p id="p17705736165313"><a name="p17705736165313"></a><a name="p17705736165313"></a>For details, see <a href="#table13185192412159">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  source field data structure description

    <a name="table15343138128"></a>
    <table><thead align="left"><tr id="row53891320125"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p103841361219"><a name="p103841361219"></a><a name="p103841361219"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p14391313121214"><a name="p14391313121214"></a><a name="p14391313121214"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p44051314123"><a name="p44051314123"></a><a name="p44051314123"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p2414137127"><a name="p2414137127"></a><a name="p2414137127"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2421813191218"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p13264155191218"><a name="p13264155191218"></a><a name="p13264155191218"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2265855161214"><a name="p2265855161214"></a><a name="p2265855161214"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1626555516125"><a name="p1626555516125"></a><a name="p1626555516125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p02661255101216"><a name="p02661255101216"></a><a name="p02661255101216"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row85749514384"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1953065318318"><a name="p1953065318318"></a><a name="p1953065318318"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p65301153103119"><a name="p65301153103119"></a><a name="p65301153103119"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p753012532312"><a name="p753012532312"></a><a name="p753012532312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p338385533211"><a name="p338385533211"></a><a name="p338385533211"></a>Specifies the restoration mode. Enumerated values include:</p>
    <a name="ul1286842916197"></a><a name="ul1286842916197"></a><ul id="ul1286842916197"><li><span class="parmvalue" id="parmvalue14106203115377"><a name="parmvalue14106203115377"></a><a name="parmvalue14106203115377"></a><b>backup</b></span>: indicates using backup files for restoration. In this mode, <span class="parmname" id="parmname151076313376"><a name="parmname151076313376"></a><a name="parmname151076313376"></a><b>type</b></span> is not mandatory and <span class="parmname" id="parmname410715311373"><a name="parmname410715311373"></a><a name="parmname410715311373"></a><b>backup_id</b></span> is mandatory.</li><li><span class="parmvalue" id="parmvalue18771173218374"><a name="parmvalue18771173218374"></a><a name="parmvalue18771173218374"></a><b>timestamp</b></span>: indicates the point-in-time restoration mode. In this mode, <span class="parmname" id="parmname37721032123717"><a name="parmname37721032123717"></a><a name="parmname37721032123717"></a><b>type</b></span> is mandatory and <span class="parmname" id="parmname107730322372"><a name="parmname107730322372"></a><a name="parmname107730322372"></a><b>restore_time</b></span> is no mandatory.</li></ul>
    </td>
    </tr>
    <tr id="row1246181331215"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5479131120"><a name="p5479131120"></a><a name="p5479131120"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p164741341214"><a name="p164741341214"></a><a name="p164741341214"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p148131319124"><a name="p148131319124"></a><a name="p148131319124"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p104915134120"><a name="p104915134120"></a><a name="p104915134120"></a>Specifies the ID of the backup used to restore data. This parameter must be specified when the backup file is used for restoration.</p>
    </td>
    </tr>
    <tr id="row149971720381"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1876020715326"><a name="p1876020715326"></a><a name="p1876020715326"></a>restore_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p167604743213"><a name="p167604743213"></a><a name="p167604743213"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1976018715320"><a name="p1976018715320"></a><a name="p1976018715320"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p147606715321"><a name="p147606715321"></a><a name="p147606715321"></a>Specifies the time point of data restoration in the UNIX timestamp. The unit is millisecond and the time zone is UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  target field data structure description

    <a name="table13185192412159"></a>
    <table><thead align="left"><tr id="row13189624131514"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1191122441517"><a name="p1191122441517"></a><a name="p1191122441517"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p1192132416156"><a name="p1192132416156"></a><a name="p1192132416156"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p8193152420154"><a name="p8193152420154"></a><a name="p8193152420154"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p16195112415153"><a name="p16195112415153"></a><a name="p16195112415153"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17195102481518"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4195224181513"><a name="p4195224181513"></a><a name="p4195224181513"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p5196162491515"><a name="p5196162491515"></a><a name="p5196162491515"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p719812247154"><a name="p719812247154"></a><a name="p719812247154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p71982245158"><a name="p71982245158"></a><a name="p71982245158"></a>Specifies the ID of the DB instance to be restored to.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    Use backup files for restoration:

    ```
    {
    	"source": {
    		"instance_id": "d8e6ca5a624745bcb546a227aa3ae1cfin01",
    		"type": "backup",
    		"backup_id": "2f4ddb93-b901-4b08-93d8-1d2e472f30fe"
    	},
    	"target": {
    		"instance_id": "d8e6ca5a624745bcb546a227aa3ae1cfin01"
    	}
    }
    ```

    Use PITR for restoration:

    ```
    {
    	"source": {
    		"instance_id": "d8e6ca5a624745bcb546a227aa3ae1cfin01",
    		"type": "timestamp",
    		"restore_time": 1532001446987
    	},
    	"target": {
    		"instance_id": "d8e6ca5a624745bcb546a227aa3ae1cfin01"
    	}
    }
    ```


## Response<a name="section1229512143106"></a>

-   Normal response

    **Table  5**  Parameter description

    <a name="table68261136172016"></a>
    <table><thead align="left"><tr id="row17826143612201"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p163303524208"><a name="p163303524208"></a><a name="p163303524208"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1133119521209"><a name="p1133119521209"></a><a name="p1133119521209"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p23321252122014"><a name="p23321252122014"></a><a name="p23321252122014"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17826183612020"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5826143617203"><a name="p5826143617203"></a><a name="p5826143617203"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3826236182018"><a name="p3826236182018"></a><a name="p3826236182018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48266368201"><a name="p48266368201"></a><a name="p48266368201"></a>Indicates the task ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example normal response

    ```
    {
    	"job_id": "ff80808157127d9301571bf8160c001d"
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

