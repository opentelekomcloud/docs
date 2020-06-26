# Querying Extension APIs<a name="evs_04_2080"></a>

## Function<a name="section19390540"></a>

This API is used to query extension APIs.

## URI<a name="section40297137"></a>

-   URI format

    GET /v2/\{project\_id\}/extensions

-   Parameter description

    <a name="table8745607"></a>
    <table><thead align="left"><tr id="row15985080"><th class="cellrowborder" valign="top" width="24.87%" id="mcps1.1.4.1.1"><p id="p19723089"><a name="p19723089"></a><a name="p19723089"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.12%" id="mcps1.1.4.1.2"><p id="p54066375"><a name="p54066375"></a><a name="p54066375"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.1.4.1.3"><p id="p17300225"><a name="p17300225"></a><a name="p17300225"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59140967"><td class="cellrowborder" valign="top" width="24.87%" headers="mcps1.1.4.1.1 "><p id="p25689059"><a name="p25689059"></a><a name="p25689059"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.12%" headers="mcps1.1.4.1.2 "><p id="p439002"><a name="p439002"></a><a name="p439002"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.4.1.3 "><p id="p35559222"><a name="p35559222"></a><a name="p35559222"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section27129916"></a>

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/extensions
    ```


## Response<a name="section42842654"></a>

-   Parameter description

    <a name="table11977025201856"></a>
    <table><thead align="left"><tr id="row8102228201856"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p52300707201856"><a name="p52300707201856"></a><a name="p52300707201856"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="p3642697315541"><a name="p3642697315541"></a><a name="p3642697315541"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p17319263201856"><a name="p17319263201856"></a><a name="p17319263201856"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60683035201856"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p16378828201856"><a name="p16378828201856"></a><a name="p16378828201856"></a>extensions</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p6490369115541"><a name="p6490369115541"></a><a name="p6490369115541"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p20205612201856"><a name="p20205612201856"></a><a name="p20205612201856"></a>Specifies the extension APIs. For details, see <a href="#li35330737222812">Parameters in the extensions field</a>.</p>
    </td>
    </tr>
    <tr id="row18487163602815"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li35330737222812"></a>Parameters in the  **extensions**  field

    <a name="table49541177222812"></a>
    <table><thead align="left"><tr id="row31307356222812"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p52867918222812"><a name="p52867918222812"></a><a name="p52867918222812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="p54442989222812"><a name="p54442989222812"></a><a name="p54442989222812"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p47079504222812"><a name="p47079504222812"></a><a name="p47079504222812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55343460222812"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p66542884171033"><a name="p66542884171033"></a><a name="p66542884171033"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p21264523171033"><a name="p21264523171033"></a><a name="p21264523171033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p172841210852"><a name="p172841210852"></a><a name="p172841210852"></a>Specifies the last update time.</p>
    <p id="p64318586171033"><a name="p64318586171033"></a><a name="p64318586171033"></a><span id="text15197123457"><a name="text15197123457"></a><a name="text15197123457"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.+XX.XX</span></p>
    </td>
    </tr>
    <tr id="row49897554222812"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p46262636171033"><a name="p46262636171033"></a><a name="p46262636171033"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p56285996171033"><a name="p56285996171033"></a><a name="p56285996171033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p59451065171033"><a name="p59451065171033"></a><a name="p59451065171033"></a>Specifies the description.</p>
    </td>
    </tr>
    <tr id="row15692876222812"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p54609812171033"><a name="p54609812171033"></a><a name="p54609812171033"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p44048737191438"><a name="p44048737191438"></a><a name="p44048737191438"></a>list&lt;map&lt;String,String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p61224008171033"><a name="p61224008171033"></a><a name="p61224008171033"></a><span id="text658942018365"><a name="text658942018365"></a><a name="text658942018365"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row23073040222812"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p19600405171033"><a name="p19600405171033"></a><a name="p19600405171033"></a>alias</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p44128957171033"><a name="p44128957171033"></a><a name="p44128957171033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p22448926171033"><a name="p22448926171033"></a><a name="p22448926171033"></a>Specifies the extension parameter alias.</p>
    </td>
    </tr>
    <tr id="row52652485222812"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p57813479171033"><a name="p57813479171033"></a><a name="p57813479171033"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p52380208171033"><a name="p52380208171033"></a><a name="p52380208171033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p2055232171033"><a name="p2055232171033"></a><a name="p2055232171033"></a>Specifies the extension parameter name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p19541716103019"><a name="evs_04_2013_p19541716103019"></a><a name="evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p39375186103019"><a name="evs_04_2013_p39375186103019"></a><a name="evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p38578950103019"><a name="evs_04_2013_p38578950103019"></a><a name="evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p46815658103019"><a name="evs_04_2013_p46815658103019"></a><a name="evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p33971979103019"><a name="evs_04_2013_p33971979103019"></a><a name="evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p21623243103019"><a name="evs_04_2013_p21623243103019"></a><a name="evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p59870541103019"><a name="evs_04_2013_p59870541103019"></a><a name="evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p17675690103019"><a name="evs_04_2013_p17675690103019"></a><a name="evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p6087468103019"><a name="evs_04_2013_p6087468103019"></a><a name="evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2013_p54787218103019"><a name="evs_04_2013_p54787218103019"></a><a name="evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "extensions": [
            {
                "updated": "2013-04-18T00:00:00+00:00", 
                "name": "SchedulerHints", 
                "links": [ ], 
                "alias": "OS-SCH-HNT", 
                "description": "Pass arbitrary key/value pairs to the scheduler."
            }, 
            {
                "updated": "2011-06-29T00:00:00+00:00", 
                "name": "Hosts", 
                "links": [ ], 
                "alias": "os-hosts", 
                "description": "Admin-only host administration."
            }, 
            {
                "updated": "2011-11-03T00:00:00+00:00", 
                "name": "VolumeTenantAttribute", 
                "links": [ ], 
                "alias": "os-vol-tenant-attr", 
                "description": "Expose the internal project_id as an attribute of a volume."
            }, 
            {
                "updated": "2011-08-08T00:00:00+00:00", 
                "name": "Quotas", 
                "links": [ ], 
                "alias": "os-quota-sets", 
                "description": "Quota management support."
            }, 
            {
                "updated": "2011-08-24T00:00:00+00:00", 
                "name": "TypesManage", 
                "links": [ ], 
                "alias": "os-types-manage", 
                "description": "Types manage support."
            }, 
            {
                "updated": "2013-07-10T00:00:00+00:00", 
                "name": "VolumeEncryptionMetadata", 
                "links": [ ], 
                "alias": "os-volume-encryption-metadata", 
                "description": "Volume encryption metadata retrieval support."
            }, 
            {
                "updated": "2012-12-12T00:00:00+00:00", 
                "name": "Backups", 
                "links": [ ], 
                "alias": "backups", 
                "description": "Backups support."
            }, 
            {
                "updated": "2013-07-16T00:00:00+00:00", 
                "name": "SnapshotActions", 
                "links": [ ], 
                "alias": "os-snapshot-actions", 
                "description": "Enable snapshot manager actions."
            }, 
            {
                "updated": "2012-05-31T00:00:00+00:00", 
                "name": "VolumeActions", 
                "links": [ ], 
                "alias": "os-volume-actions", 
                "description": "Enable volume actions
        "
            }, 
            {
                "updated": "2013-10-03T00:00:00+00:00", 
                "name": "UsedLimits", 
                "links": [ ], 
                "alias": "os-used-limits", 
                "description": "Provide data on limited resources that are being used."
            }, 
            {
                "updated": "2012-05-31T00:00:00+00:00", 
                "name": "VolumeUnmanage", 
                "links": [ ], 
                "alias": "os-volume-unmanage", 
                "description": "Enable volume unmanage operation."
            }, 
            {
                "updated": "2011-11-03T00:00:00+00:00", 
                "name": "VolumeHostAttribute", 
                "links": [ ], 
                "alias": "os-vol-host-attr", 
                "description": "Expose host as an attribute of a volume."
            }, 
            {
                "updated": "2013-07-01T00:00:00+00:00", 
                "name": "VolumeTypeEncryption", 
                "links": [ ], 
                "alias": "encryption", 
                "description": "Encryption support for volume types."
            }, 
            {
                "updated": "2013-06-27T00:00:00+00:00", 
                "name": "AvailabilityZones", 
                "links": [ ], 
                "alias": "os-availability-zone", 
                "description": "Describe Availability Zones."
            }, 
            {
                "updated": "2013-08-02T00:00:00+00:00", 
                "name": "Qos_specs_manage", 
                "links": [ ], 
                "alias": "qos-specs", 
                "description": "QoS specs support."
            }, 
            {
                "updated": "2011-08-24T00:00:00+00:00", 
                "name": "TypesExtraSpecs", 
                "links": [ ], 
                "alias": "os-types-extra-specs", 
                "description": "Type extra specs support."
            }, 
            {
                "updated": "2013-08-08T00:00:00+00:00", 
                "name": "VolumeMigStatusAttribute", 
                "links": [ ],  
                "alias": "os-vol-mig-status-attr", 
                "description": "Expose migration_status as an attribute of a volume."
            }, 
            {
                "updated": "2012-08-13T00:00:00+00:00", 
                "name": "CreateVolumeExtension", 
                "links": [ ], 
                "alias": "os-image-create", 
                "description": "Allow creating a volume from an image in the Create Volume v1 API."
            }, 
            {
                "updated": "2014-01-10T00:00:00-00:00", 
                "name": "ExtendedServices", 
                "links": [ ],  
                "alias": "os-extended-services", 
                "description": "Extended services support."
            }, 
            {
                "updated": "2012-06-19T00:00:00+00:00", 
                "name": "ExtendedSnapshotAttributes", 
                "links": [ ], 
                "alias": "os-extended-snapshot-attributes", 
                "description": "Extended SnapshotAttributes support."
            }, 
            {
                "updated": "2012-12-07T00:00:00+00:00", 
                "name": "VolumeImageMetadata", 
                "links": [ ], 
                "alias": "os-vol-image-meta", 
                "description": "Show image metadata associated with the volume."
            }, 
            {
                "updated": "2012-03-12T00:00:00+00:00", 
                "name": "QuotaClasses", 
                "links": [ ], 
                "alias": "os-quota-class-sets", 
                "description": "Quota classes management support."
            }, 
            {
                "updated": "2013-05-29T00:00:00+00:00", 
                "name": "VolumeTransfer", 
                "links": [ ], 
                "alias": "os-volume-transfer", 
                "description": "Volume transfer management support."
            }, 
            {
                "updated": "2014-02-10T00:00:00+00:00", 
                "name": "VolumeManage", 
                "links": [ ],  
                "alias": "os-volume-manage", 
                "description": "Allows existing backend storage to be 'managed' by Cinder."
            }, 
            {
                "updated": "2012-08-25T00:00:00+00:00", 
                "name": "AdminActions", 
                "links": [ ],  
                "alias": "os-admin-actions", 
                "description": "Enable admin actions."
            }, 
            {
                "updated": "2012-10-28T00:00:00-00:00", 
                "name": "Services", 
                "links": [ ],  
                "alias": "os-services", 
                "description": "Services support."
            }
        ]
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badRequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "badRequest": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section50039568"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

