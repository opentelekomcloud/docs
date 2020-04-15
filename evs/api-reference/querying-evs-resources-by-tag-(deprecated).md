# Querying EVS Resources by Tag \(Deprecated\)<a name="evs_04_2042"></a>

## Function<a name="section5299350116935"></a>

This API is used to query the EVS resources by tag.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>This API has been deprecated. Use another API. For details, see  [Querying Details of EVS Disks by Tag](querying-details-of-evs-disks-by-tag.md).  

## Constraints<a name="section4466609116935"></a>

None

## URI<a name="section1378135716935"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-tags/\{resource\_type\}/resource\_instances

    Examples:

    -   https://\{\{evs\_url\}\}/v2/\{\{project\_id\}\}/os-vendor-tags/volumes/resource\_instances?tags=\{'test':\['test'\]\}
    -   https://\{\{evs\_url\}\}/v2/\{\{project\_id\}\}/os-vendor-tags/volumes/resource\_instances

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
    <tbody><tr id="row50646790104128"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p8749302104128"><a name="p8749302104128"></a><a name="p8749302104128"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p37604871104128"><a name="p37604871104128"></a><a name="p37604871104128"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p26095712104128"><a name="p26095712104128"></a><a name="p26095712104128"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row40869685152038"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p33171521152058"><a name="p33171521152058"></a><a name="p33171521152058"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p2538652152058"><a name="p2538652152058"></a><a name="p2538652152058"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p42707547152038"><a name="p42707547152038"></a><a name="p42707547152038"></a>Specifies the resource type. The value can be <strong id="b842352706193556"><a name="b842352706193556"></a><a name="b842352706193556"></a>volumes</strong>, <strong id="b84235270619367"><a name="b84235270619367"></a><a name="b84235270619367"></a>snapshots</strong>, or <strong id="b842352706193615"><a name="b842352706193615"></a><a name="b842352706193615"></a>backups</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request filter parameters

    <a name="table54577306"></a>
    <table><thead align="left"><tr id="row28922261"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.1.5.1.1"><p id="p61001774"><a name="p61001774"></a><a name="p61001774"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.91%" id="mcps1.1.5.1.2"><p id="p42196623"><a name="p42196623"></a><a name="p42196623"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.35%" id="mcps1.1.5.1.3"><p id="p62483297"><a name="p62483297"></a><a name="p62483297"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.33%" id="mcps1.1.5.1.4"><p id="p27982283"><a name="p27982283"></a><a name="p27982283"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50513961"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p30237605165039"><a name="p30237605165039"></a><a name="p30237605165039"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.1.5.1.2 "><p id="p38531802"><a name="p38531802"></a><a name="p38531802"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.3 "><p id="p34068253"><a name="p34068253"></a><a name="p34068253"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.33%" headers="mcps1.1.5.1.4 "><p id="p65671492181059"><a name="p65671492181059"></a><a name="p65671492181059"></a>Specifies to query the EVS resources owning the tags in the filtering tag.</p>
    <p id="p1883368165151"><a name="p1883368165151"></a><a name="p1883368165151"></a>For example, if the filtering tag is <strong id="b842352706203359"><a name="b842352706203359"></a><a name="b842352706203359"></a>tags={'a':['b', 'c'], 'd':['e']}</strong>, EVS resources owning tags (key is <strong id="b842352706203853"><a name="b842352706203853"></a><a name="b842352706203853"></a>a</strong> and value is <strong id="b842352706203857"><a name="b842352706203857"></a><a name="b842352706203857"></a>b</strong> or <strong id="b84235270620390"><a name="b84235270620390"></a><a name="b84235270620390"></a>c</strong>) and tags (key is <strong id="b84235270620395"><a name="b84235270620395"></a><a name="b84235270620395"></a>d</strong> and value is <strong id="b84235270620398"><a name="b84235270620398"></a><a name="b84235270620398"></a>e</strong>) are queried.</p>
    </td>
    </tr>
    <tr id="row5477191"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p31507053165039"><a name="p31507053165039"></a><a name="p31507053165039"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.1.5.1.2 "><p id="p32609666"><a name="p32609666"></a><a name="p32609666"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.3 "><p id="p24137296"><a name="p24137296"></a><a name="p24137296"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.33%" headers="mcps1.1.5.1.4 "><p id="p2148140218111"><a name="p2148140218111"></a><a name="p2148140218111"></a>Specifies to query EVS resources owing one of the tags in the filtering tag.</p>
    <p id="p50690543165151"><a name="p50690543165151"></a><a name="p50690543165151"></a>For example, if the filtering tag is <strong id="b842352706203359_1"><a name="b842352706203359_1"></a><a name="b842352706203359_1"></a>tags_any={'a':['b', 'c'], 'd':['e']}</strong>, EVS resources owning tags (key is <strong id="b842352706203853_1"><a name="b842352706203853_1"></a><a name="b842352706203853_1"></a>a</strong> and value is <strong id="b842352706203857_1"><a name="b842352706203857_1"></a><a name="b842352706203857_1"></a>b</strong> or <strong id="b84235270620390_1"><a name="b84235270620390_1"></a><a name="b84235270620390_1"></a>c</strong>) or tags (key is <strong id="b84235270620395_1"><a name="b84235270620395_1"></a><a name="b84235270620395_1"></a>d</strong> and value is <strong id="b84235270620398_1"><a name="b84235270620398_1"></a><a name="b84235270620398_1"></a>e</strong>) are queried.</p>
    </td>
    </tr>
    <tr id="row38858233"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p17410218165039"><a name="p17410218165039"></a><a name="p17410218165039"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.1.5.1.2 "><p id="p2294440"><a name="p2294440"></a><a name="p2294440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.3 "><p id="p51631922"><a name="p51631922"></a><a name="p51631922"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.33%" headers="mcps1.1.5.1.4 "><p id="p29712730181116"><a name="p29712730181116"></a><a name="p29712730181116"></a>Specifies to query EVS resources not owning the tags in the filtering tag.</p>
    <p id="p57150714165151"><a name="p57150714165151"></a><a name="p57150714165151"></a>For example, if the filtering tag is <strong id="b842352706203359_2"><a name="b842352706203359_2"></a><a name="b842352706203359_2"></a>not_tags={'a':['b', 'c'], 'd':['e']}</strong>, EVS resources not owning tags (key is <strong id="b842352706203853_2"><a name="b842352706203853_2"></a><a name="b842352706203853_2"></a>a</strong> and value is <strong id="b842352706203857_2"><a name="b842352706203857_2"></a><a name="b842352706203857_2"></a>b</strong> or <strong id="b84235270620390_2"><a name="b84235270620390_2"></a><a name="b84235270620390_2"></a>c</strong>) and tags (key is <strong id="b84235270620395_2"><a name="b84235270620395_2"></a><a name="b84235270620395_2"></a>d</strong> and value is <strong id="b84235270620398_2"><a name="b84235270620398_2"></a><a name="b84235270620398_2"></a>e</strong>) are queried.</p>
    </td>
    </tr>
    <tr id="row865613"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p8474185165039"><a name="p8474185165039"></a><a name="p8474185165039"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.1.5.1.2 "><p id="p42147045"><a name="p42147045"></a><a name="p42147045"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.3 "><p id="p58467488"><a name="p58467488"></a><a name="p58467488"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.33%" headers="mcps1.1.5.1.4 "><p id="p28872281181125"><a name="p28872281181125"></a><a name="p28872281181125"></a>Specifies to query EVS resources not owning one of the tags in the filtering tag.</p>
    <p id="p63524872165151"><a name="p63524872165151"></a><a name="p63524872165151"></a>For example, if the filtering tag is <strong id="b842352706203359_3"><a name="b842352706203359_3"></a><a name="b842352706203359_3"></a>not_tags={'a':['b', 'c'], 'd':['e']}</strong>, EVS resources not owning tags (key is <strong id="b842352706203853_3"><a name="b842352706203853_3"></a><a name="b842352706203853_3"></a>a</strong> and value is <strong id="b842352706203857_3"><a name="b842352706203857_3"></a><a name="b842352706203857_3"></a>b</strong> or <strong id="b84235270620390_3"><a name="b84235270620390_3"></a><a name="b84235270620390_3"></a>c</strong>) or tags (key is <strong id="b84235270620395_3"><a name="b84235270620395_3"></a><a name="b84235270620395_3"></a>d</strong> and value is <strong id="b84235270620398_3"><a name="b84235270620398_3"></a><a name="b84235270620398_3"></a>e</strong>) are queried.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section5573802716935"></a>

None

## Response<a name="section3215934016935"></a>

-   Parameter description

    <a name="table716338716935"></a>
    <table><thead align="left"><tr id="row2937460716935"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.1"><p id="p3053299616935"><a name="p3053299616935"></a><a name="p3053299616935"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p5725363416935"><a name="p5725363416935"></a><a name="p5725363416935"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p3278200616935"><a name="p3278200616935"></a><a name="p3278200616935"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63271571172633"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p24723652172633"><a name="p24723652172633"></a><a name="p24723652172633"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p56458834172633"><a name="p56458834172633"></a><a name="p56458834172633"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p52593571172633"><a name="p52593571172633"></a><a name="p52593571172633"></a>Specifies the number of EVS resources.</p>
    </td>
    </tr>
    <tr id="row3809682916935"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p6594430016935"><a name="p6594430016935"></a><a name="p6594430016935"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p3988810816935"><a name="p3988810816935"></a><a name="p3988810816935"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p4842047816935"><a name="p4842047816935"></a><a name="p4842047816935"></a>Specifies the EVS resource lists.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "total_count": 2, 
        "resources": [
            {
                "resource_name": null, 
                "resource_detail": {
                    "status": "available", 
                    "description": null, 
                    "availability_zone": "az-dc-1", 
                    "updated_at": "2017-07-26T08:14:07.857625", 
                    "source_volid": null, 
                    "snapshot_id": null, 
                    "id": "47cc4949-447a-43dc-b482-a1d7917fef69", 
                    "size": 45, 
                    "name": null, 
                    "bootable": "true", 
                    "created_at": "2017-07-26T08:09:39.787432", 
                    "multiattach": false
                }, 
                "tags": {
                    "a": "c", 
                    "d": "e"
                }, 
                "resource_id": "47cc4949-447a-43dc-b482-a1d7917fef69"
            }, 
            {
                "resource_name": null, 
                "resource_detail": {
                    "status": "available", 
                    "description": null, 
                    "availability_zone": "az-dc-1", 
                    "updated_at": "2017-07-26T08:02:11.250455", 
                    "source_volid": null, 
                    "snapshot_id": null, 
                    "id": "588e94ef-eb2d-4895-a692-18163a7eeddc", 
                    "size": 100, 
                    "name": null, 
                    "bootable": "false", 
                    "created_at": "2017-07-26T08:00:51.563309", 
                    "multiattach": false
                }, 
                "tags": {
                    "a": "c", 
                    "d": "e"
                }, 
                "resource_id": "588e94ef-eb2d-4895-a692-18163a7eeddc"
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
        "computeFault": {
            "message": "The server has either erred or is incapable of performing the requested operation.", 
            "code": 500
        }
    }
    ```


## Status Codes<a name="section6050296116935"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

