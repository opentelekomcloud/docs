# Querying Tags of an EVS Disk<a name="evs_04_2031"></a>

## Function<a name="section5299350116935"></a>

This API is used to query the tags of the specified EVS disk. 

## Constraints<a name="section4466609116935"></a>

None

## URI<a name="section1378135716935"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-volumes/\{volume\_id\}/tags

-   Parameter description

    <a name="table28484833104128"></a>
    <table><thead align="left"><tr id="row60547305104128"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p5384679104128"><a name="p5384679104128"></a><a name="p5384679104128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p33505894104128"><a name="p33505894104128"></a><a name="p33505894104128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p29622926104128"><a name="p29622926104128"></a><a name="p29622926104128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50646790104128"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p39499107192824"><a name="p39499107192824"></a><a name="p39499107192824"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p45311124192824"><a name="p45311124192824"></a><a name="p45311124192824"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p46322466192824"><a name="p46322466192824"></a><a name="p46322466192824"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row40869685152038"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p13319579192824"><a name="p13319579192824"></a><a name="p13319579192824"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p5144078192824"><a name="p5144078192824"></a><a name="p5144078192824"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p14017211192824"><a name="p14017211192824"></a><a name="p14017211192824"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section565234819217"></a>

None

## Response<a name="section3215934016935"></a>

-   Parameter description

    <a name="table716338716935"></a>
    <table><thead align="left"><tr id="row2937460716935"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p3053299616935"><a name="p3053299616935"></a><a name="p3053299616935"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.53%" id="mcps1.1.4.1.2"><p id="p5725363416935"><a name="p5725363416935"></a><a name="p5725363416935"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="p3278200616935"><a name="p3278200616935"></a><a name="p3278200616935"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63271571172633"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p4610476519311"><a name="p4610476519311"></a><a name="p4610476519311"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.53%" headers="mcps1.1.4.1.2 "><p id="p4349852319311"><a name="p4349852319311"></a><a name="p4349852319311"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p5468710519318"><a name="p5468710519318"></a><a name="p5468710519318"></a>Specifies the tag list. For details, see <a href="#li8528152083214">Parameters in the tags field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li8528152083214"></a>Parameters in the  **tags**  field

    <a name="table205290203323"></a>
    <table><thead align="left"><tr id="row13530142033210"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p19530182011329"><a name="p19530182011329"></a><a name="p19530182011329"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p20530120163211"><a name="p20530120163211"></a><a name="p20530120163211"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.95%" id="mcps1.1.4.1.3"><p id="p18533172017325"><a name="p18533172017325"></a><a name="p18533172017325"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row253510208321"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p17535320203220"><a name="p17535320203220"></a><a name="p17535320203220"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p175351020123212"><a name="p175351020123212"></a><a name="p175351020123212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.95%" headers="mcps1.1.4.1.3 "><p id="p118083133491"><a name="p118083133491"></a><a name="p118083133491"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row853810204325"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p1053816201325"><a name="p1053816201325"></a><a name="p1053816201325"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p13538520153211"><a name="p13538520153211"></a><a name="p13538520153211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.95%" headers="mcps1.1.4.1.3 "><p id="p656419560501"><a name="p656419560501"></a><a name="p656419560501"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "tags": [
            {
                "value": "value1", 
                "key": "key1"
            }, 
            {
                "value": "value2", 
                "key": "key2"
            }
        ]
    }
    ```


## Status Codes<a name="section6050296116935"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

