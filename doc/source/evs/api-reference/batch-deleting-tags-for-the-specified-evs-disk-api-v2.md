# Batch Deleting Tags for the Specified EVS Disk<a name="evs_04_2029"></a>

## Function<a name="section5299350116935"></a>

This API is used to batch delete tags for the specified EVS disk. 

## Constraints<a name="section4466609116935"></a>

None

## URI<a name="section1378135716935"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-volumes/\{volume\_id\}/tags/action

-   Parameter description

    <a name="table28484833104128"></a>
    <table><thead align="left"><tr id="row60547305104128"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p5384679104128"><a name="p5384679104128"></a><a name="p5384679104128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.340000000000003%" id="mcps1.1.4.1.2"><p id="p33505894104128"><a name="p33505894104128"></a><a name="p33505894104128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.09%" id="mcps1.1.4.1.3"><p id="p29622926104128"><a name="p29622926104128"></a><a name="p29622926104128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50646790104128"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p16385142185226"><a name="p16385142185226"></a><a name="p16385142185226"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.340000000000003%" headers="mcps1.1.4.1.2 "><p id="p52128135185226"><a name="p52128135185226"></a><a name="p52128135185226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.09%" headers="mcps1.1.4.1.3 "><p id="p50566709185232"><a name="p50566709185232"></a><a name="p50566709185232"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row40869685152038"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p66238361185240"><a name="p66238361185240"></a><a name="p66238361185240"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.340000000000003%" headers="mcps1.1.4.1.2 "><p id="p63707038185240"><a name="p63707038185240"></a><a name="p63707038185240"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.09%" headers="mcps1.1.4.1.3 "><p id="p42707547152038"><a name="p42707547152038"></a><a name="p42707547152038"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section5573802716935"></a>

-   Parameter description

    <a name="en-us_topic_0094910373_table54577306"></a>
    <table><thead align="left"><tr id="en-us_topic_0094910373_row28922261"><th class="cellrowborder" valign="top" width="15.151515151515149%" id="mcps1.1.5.1.1"><p id="en-us_topic_0094910373_p61001774"><a name="en-us_topic_0094910373_p61001774"></a><a name="en-us_topic_0094910373_p61001774"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.5.1.2"><p id="en-us_topic_0094910373_p42196623"><a name="en-us_topic_0094910373_p42196623"></a><a name="en-us_topic_0094910373_p42196623"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.3"><p id="en-us_topic_0094910373_p62483297"><a name="en-us_topic_0094910373_p62483297"></a><a name="en-us_topic_0094910373_p62483297"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.54545454545454%" id="mcps1.1.5.1.4"><p id="en-us_topic_0094910373_p27982283"><a name="en-us_topic_0094910373_p27982283"></a><a name="en-us_topic_0094910373_p27982283"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0094910373_row50513961"><td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0094910373_p52260429185445"><a name="en-us_topic_0094910373_p52260429185445"></a><a name="en-us_topic_0094910373_p52260429185445"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0094910373_p5236376185445"><a name="en-us_topic_0094910373_p5236376185445"></a><a name="en-us_topic_0094910373_p5236376185445"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0094910373_p21493324185445"><a name="en-us_topic_0094910373_p21493324185445"></a><a name="en-us_topic_0094910373_p21493324185445"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.54545454545454%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0094910373_p63237647185445"><a name="en-us_topic_0094910373_p63237647185445"></a><a name="en-us_topic_0094910373_p63237647185445"></a>Specifies the tag list. For details, see <a href="#li2051510427374">Parameters in the tags field</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0094910373_row5477191"><td class="cellrowborder" valign="top" width="15.151515151515149%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0094910373_p63564655185445"><a name="en-us_topic_0094910373_p63564655185445"></a><a name="en-us_topic_0094910373_p63564655185445"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0094910373_p48463411185445"><a name="en-us_topic_0094910373_p48463411185445"></a><a name="en-us_topic_0094910373_p48463411185445"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0094910373_p33222212185445"><a name="en-us_topic_0094910373_p33222212185445"></a><a name="en-us_topic_0094910373_p33222212185445"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.54545454545454%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0094910373_p8076185185456"><a name="en-us_topic_0094910373_p8076185185456"></a><a name="en-us_topic_0094910373_p8076185185456"></a>Specifies the operation to perform. The value can be <strong id="b842352706194823"><a name="b842352706194823"></a><a name="b842352706194823"></a>create</strong> or <strong id="b842352706194828"><a name="b842352706194828"></a><a name="b842352706194828"></a>delete</strong>.</p>
    <p id="p199258121833"><a name="p199258121833"></a><a name="p199258121833"></a><strong id="b842352706194852"><a name="b842352706194852"></a><a name="b842352706194852"></a>delete</strong>: specifies to delete tags.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li2051510427374"></a>Parameters in the  **tags**  field

    <a name="table251711423376"></a>
    <table><thead align="left"><tr id="row16518134283716"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.1.5.1.1"><p id="p75181742143717"><a name="p75181742143717"></a><a name="p75181742143717"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.099999999999998%" id="mcps1.1.5.1.2"><p id="p2051804253715"><a name="p2051804253715"></a><a name="p2051804253715"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.16%" id="mcps1.1.5.1.3"><p id="p1951816424370"><a name="p1951816424370"></a><a name="p1951816424370"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.33%" id="mcps1.1.5.1.4"><p id="p15181442193715"><a name="p15181442193715"></a><a name="p15181442193715"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10520194220379"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p652074219372"><a name="p652074219372"></a><a name="p652074219372"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.2 "><p id="p452094213376"><a name="p452094213376"></a><a name="p452094213376"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.1.5.1.3 "><p id="p13520174213710"><a name="p13520174213710"></a><a name="p13520174213710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.33%" headers="mcps1.1.5.1.4 "><p id="p0755543174416"><a name="p0755543174416"></a><a name="p0755543174416"></a>Specifies the tag key.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "action": "delete", 
        "tags": [
            {
                "key": "key1"
            }, 
            {
                "key": "key2"
            }
        ]
    }
    ```


## Response<a name="section3215934016935"></a>

None

## Status Codes<a name="section6050296116935"></a>

-   Normal

    204


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

