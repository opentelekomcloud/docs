# Batch Adding Tags for the Specified EVS Disk<a name="evs_04_2027"></a>

## Function<a name="section5299350116935"></a>

This API is used to batch add tags for the specified EVS disk. 

-   When adding tags, if a tag key is consistent with an existing one, the new tag will overwrite the existing tag.
-   A maximum of 10 tags can be created for a disk.

## Constraints<a name="section4466609116935"></a>

None

## URI<a name="section1378135716935"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-volumes/\{volume\_id\}/tags/action

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
    <tbody><tr id="row50646790104128"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p16385142185226"><a name="p16385142185226"></a><a name="p16385142185226"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p52128135185226"><a name="p52128135185226"></a><a name="p52128135185226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p50566709185232"><a name="p50566709185232"></a><a name="p50566709185232"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row40869685152038"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p66238361185240"><a name="p66238361185240"></a><a name="p66238361185240"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p63707038185240"><a name="p63707038185240"></a><a name="p63707038185240"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p42707547152038"><a name="p42707547152038"></a><a name="p42707547152038"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section5573802716935"></a>

-   Parameter description

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
    <tbody><tr id="row50513961"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p52260429185445"><a name="p52260429185445"></a><a name="p52260429185445"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.1.5.1.2 "><p id="p5236376185445"><a name="p5236376185445"></a><a name="p5236376185445"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.3 "><p id="p21493324185445"><a name="p21493324185445"></a><a name="p21493324185445"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.33%" headers="mcps1.1.5.1.4 "><p id="p63237647185445"><a name="p63237647185445"></a><a name="p63237647185445"></a>Specifies the tag list. For details, see <a href="#li4495404118563">Parameters in the tags field</a>.</p>
    </td>
    </tr>
    <tr id="row5477191"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p63564655185445"><a name="p63564655185445"></a><a name="p63564655185445"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.1.5.1.2 "><p id="p48463411185445"><a name="p48463411185445"></a><a name="p48463411185445"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.3 "><p id="p33222212185445"><a name="p33222212185445"></a><a name="p33222212185445"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.33%" headers="mcps1.1.5.1.4 "><p id="p8076185185456"><a name="p8076185185456"></a><a name="p8076185185456"></a>Specifies the operation to perform. The value can be <strong id="b842352706194823"><a name="b842352706194823"></a><a name="b842352706194823"></a>create</strong> or <strong id="b842352706194828"><a name="b842352706194828"></a><a name="b842352706194828"></a>delete</strong>.</p>
    <p id="p1055696513"><a name="p1055696513"></a><a name="p1055696513"></a><strong id="b842352706194834"><a name="b842352706194834"></a><a name="b842352706194834"></a>create</strong>: specifies to add tags.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li4495404118563"></a>Parameters in the  **tags**  field

    <a name="table24916402185553"></a>
    <table><thead align="left"><tr id="row45194334185553"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.1.5.1.1"><p id="p36862455185553"><a name="p36862455185553"></a><a name="p36862455185553"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.099999999999998%" id="mcps1.1.5.1.2"><p id="p33068848185553"><a name="p33068848185553"></a><a name="p33068848185553"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.35%" id="mcps1.1.5.1.3"><p id="p61330993185553"><a name="p61330993185553"></a><a name="p61330993185553"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.14%" id="mcps1.1.5.1.4"><p id="p1754531185553"><a name="p1754531185553"></a><a name="p1754531185553"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7899309185553"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p27402824185630"><a name="p27402824185630"></a><a name="p27402824185630"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.2 "><p id="p5036281185630"><a name="p5036281185630"></a><a name="p5036281185630"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.3 "><p id="p5285618185630"><a name="p5285618185630"></a><a name="p5285618185630"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.1.5.1.4 "><div class="p" id="p65027314233"><a name="p65027314233"></a><a name="p65027314233"></a>Specifies the tag key.<a name="ul20512635161710"></a><a name="ul20512635161710"></a><ul id="ul20512635161710"><li>Cannot be left blank.</li><li>Must be unique for each resource.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row55890127185553"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p54294233185630"><a name="p54294233185630"></a><a name="p54294233185630"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.2 "><p id="p35756723185630"><a name="p35756723185630"></a><a name="p35756723185630"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.1.5.1.3 "><p id="p10613433185630"><a name="p10613433185630"></a><a name="p10613433185630"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.1.5.1.4 "><div class="p" id="p2724127122616"><a name="p2724127122616"></a><a name="p2724127122616"></a>Specifies the tag value.<a name="ul4512173118234"></a><a name="ul4512173118234"></a><ul id="ul4512173118234"><li>Can contain a maximum of 43 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "action": "create", 
        "tags": [
            {
                "key": "key1", 
                "value": "value1"
            }, 
            {
                "key": "key2", 
                "value": "value3"
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

