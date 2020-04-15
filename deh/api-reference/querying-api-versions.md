# Querying API Versions<a name="EN-US_TOPIC_0133576326"></a>

## Function<a name="section54478915181842"></a>

This API is used to query all API versions available to the DeH service.

## URI<a name="section53791107181842"></a>

GET /

## Request<a name="section10595142262918"></a>

-   Request parameters

    None

-   Example request

    ```
    GET /
    ```


## Response<a name="section15015447489"></a>

-   Response parameters

    <a name="table2931457104815"></a>
    <table><thead align="left"><tr id="row1695125724813"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p1297357184816"><a name="p1297357184816"></a><a name="p1297357184816"></a><strong id="b1629615953015"><a name="b1629615953015"></a><a name="b1629615953015"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p298135714811"><a name="p298135714811"></a><a name="p298135714811"></a><strong id="b635631017303"><a name="b635631017303"></a><a name="b635631017303"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1299557164816"><a name="p1299557164816"></a><a name="p1299557164816"></a><strong id="b3311101123019"><a name="b3311101123019"></a><a name="b3311101123019"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1010185711485"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1010316575488"><a name="p1010316575488"></a><a name="p1010316575488"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p1210417575480"><a name="p1210417575480"></a><a name="p1210417575480"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p9104557124813"><a name="p9104557124813"></a><a name="p9104557124813"></a>Specifies the API versions.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **versions**  field description

    <a name="table1430613366502"></a>
    <table><thead align="left"><tr id="row14310136175015"><th class="cellrowborder" valign="top" width="21.33%" id="mcps1.1.4.1.1"><p id="p1593982875118"><a name="p1593982875118"></a><a name="p1593982875118"></a><strong id="b473912151512"><a name="b473912151512"></a><a name="b473912151512"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.669999999999998%" id="mcps1.1.4.1.2"><p id="p6941172885114"><a name="p6941172885114"></a><a name="p6941172885114"></a><strong id="b9832124712114"><a name="b9832124712114"></a><a name="b9832124712114"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.4.1.3"><p id="p10941172814517"><a name="p10941172814517"></a><a name="p10941172814517"></a><strong id="b97931348016"><a name="b97931348016"></a><a name="b97931348016"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1315163675017"><td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.1.4.1.1 "><p id="p231663616504"><a name="p231663616504"></a><a name="p231663616504"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p14318936195017"><a name="p14318936195017"></a><a name="p14318936195017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.3 "><p id="p3318103610504"><a name="p3318103610504"></a><a name="p3318103610504"></a>Specifies the ID of the API version.</p>
    </td>
    </tr>
    <tr id="row23205365509"><td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.1.4.1.1 "><p id="p8321193615508"><a name="p8321193615508"></a><a name="p8321193615508"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p132223615502"><a name="p132223615502"></a><a name="p132223615502"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.3 "><p id="p1932333615506"><a name="p1932333615506"></a><a name="p1932333615506"></a>Specifies the URL of the API version.</p>
    </td>
    </tr>
    <tr id="row53251536115018"><td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.1.4.1.1 "><p id="p032773635015"><a name="p032773635015"></a><a name="p032773635015"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p6328133617506"><a name="p6328133617506"></a><a name="p6328133617506"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.3 "><p id="p11330136195014"><a name="p11330136195014"></a><a name="p11330136195014"></a>Specifies the microversion. If the APIs of this version support microversions, set this parameter to the supported minimum microversion. If the microversion is not supported, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row16334436165018"><td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.1.4.1.1 "><p id="p033517368501"><a name="p033517368501"></a><a name="p033517368501"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p123361336205019"><a name="p123361336205019"></a><a name="p123361336205019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.3 "><p id="p11337193613501"><a name="p11337193613501"></a><a name="p11337193613501"></a>Specifies the API version status.</p>
    <a name="ul183371236125014"></a><a name="ul183371236125014"></a><ul id="ul183371236125014"><li><strong id="b8750591114"><a name="b8750591114"></a><a name="b8750591114"></a>CURRENT</strong>: indicates a primary version.</li><li><strong id="b1362524131119"><a name="b1362524131119"></a><a name="b1362524131119"></a>SUPPORTED</strong>: indicates an earlier version which is still supported.</li><li><strong id="b183298371111"><a name="b183298371111"></a><a name="b183298371111"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row113408369509"><td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.1.4.1.1 "><p id="p19341193620501"><a name="p19341193620501"></a><a name="p19341193620501"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p234110368500"><a name="p234110368500"></a><a name="p234110368500"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.3 "><p id="p5343173620508"><a name="p5343173620508"></a><a name="p5343173620508"></a>Specifies the API version update time, which must be UTC time.</p>
    </td>
    </tr>
    <tr id="row3345183625015"><td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.1.4.1.1 "><p id="p10346183615509"><a name="p10346183615509"></a><a name="p10346183615509"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p123461936195020"><a name="p123461936195020"></a><a name="p123461936195020"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.3 "><p id="p73481636205010"><a name="p73481636205010"></a><a name="p73481636205010"></a>Specifies the API version. If the APIs of this version support microversions, set this parameter to the supported minimum microversion. If the microversion is not supported, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **links**  field description

    <a name="table8533213516"></a>
    <table><thead align="left"><tr id="row7536161155116"><th class="cellrowborder" valign="top" width="21.44%" id="mcps1.1.4.1.1"><p id="p08961831105119"><a name="p08961831105119"></a><a name="p08961831105119"></a><strong id="b4673742101513"><a name="b4673742101513"></a><a name="b4673742101513"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.1.4.1.2"><p id="p1189723195114"><a name="p1189723195114"></a><a name="p1189723195114"></a><strong id="b148671343191517"><a name="b148671343191517"></a><a name="b148671343191517"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.13%" id="mcps1.1.4.1.3"><p id="p3897183165115"><a name="p3897183165115"></a><a name="p3897183165115"></a><strong id="b484994441513"><a name="b484994441513"></a><a name="b484994441513"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row454313111517"><td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.1.4.1.1 "><p id="p15544913512"><a name="p15544913512"></a><a name="p15544913512"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="p654531195120"><a name="p654531195120"></a><a name="p654531195120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.1.4.1.3 "><p id="p454810165112"><a name="p454810165112"></a><a name="p454810165112"></a>Specifies the URL of the API version.</p>
    </td>
    </tr>
    <tr id="row3548111155120"><td class="cellrowborder" valign="top" width="21.44%" headers="mcps1.1.4.1.1 "><p id="p205503185118"><a name="p205503185118"></a><a name="p205503185118"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="p955281145112"><a name="p955281145112"></a><a name="p955281145112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.1.4.1.3 "><p id="p3554161155116"><a name="p3554161155116"></a><a name="p3554161155116"></a>Specifies the API URL dependency.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "versions": [
            {
                "id": "v1.0",
                "links": [
                    {
                        "href": "https//deh.xxx.com/v1.0/",
                        "rel": "self"
                    }
                ],
                "min_version": "",
                "status": "SUPPORTED",
                "updated": "2016-12-01T11:33:21Z",
                "version": ""
            }
        ]
    }
    ```


## Status Code<a name="section9992350"></a>

See  [Status Codes](status-codes.md).

