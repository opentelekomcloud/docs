# Querying API Versions \(Native OpenStack API\)<a name="EN-US_TOPIC_0134720582"></a>

## Function<a name="section54478915181842"></a>

This interface is used to query all available Nova versions.

## URI<a name="section53791107181842"></a>

GET /

## Request Message<a name="section39878380181842"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/
    ```


## Response Message<a name="section13201080181842"></a>

-   Response parameters

    <a name="table26246518152631"></a>
    <table><thead align="left"><tr id="row29602547152631"><th class="cellrowborder" valign="top" width="27.889999999999997%" id="mcps1.1.4.1.1"><p id="p1143665616354"><a name="p1143665616354"></a><a name="p1143665616354"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.740000000000002%" id="mcps1.1.4.1.2"><p id="p11440156143517"><a name="p11440156143517"></a><a name="p11440156143517"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.370000000000005%" id="mcps1.1.4.1.3"><p id="p244212561357"><a name="p244212561357"></a><a name="p244212561357"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56174697152631"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p4445556153516"><a name="p4445556153516"></a><a name="p4445556153516"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p444855610353"><a name="p444855610353"></a><a name="p444855610353"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p344911569354"><a name="p344911569354"></a><a name="p344911569354"></a>Specifies the list of all API versions.</p>
    </td>
    </tr>
    <tr id="row4615503152631"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p8452756123518"><a name="p8452756123518"></a><a name="p8452756123518"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p1445545663515"><a name="p1445545663515"></a><a name="p1445545663515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p045585620357"><a name="p045585620357"></a><a name="p045585620357"></a>Specifies the version ID, for example, v1.</p>
    </td>
    </tr>
    <tr id="row9239644152631"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p9460175653518"><a name="p9460175653518"></a><a name="p9460175653518"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p14983184716501"><a name="p14983184716501"></a><a name="p14983184716501"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p746525619351"><a name="p746525619351"></a><a name="p746525619351"></a>Specifies the API URL.</p>
    </td>
    </tr>
    <tr id="row19267144531214"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p16283354130"><a name="p16283354130"></a><a name="p16283354130"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p13242332181317"><a name="p13242332181317"></a><a name="p13242332181317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p2269104581219"><a name="p2269104581219"></a><a name="p2269104581219"></a>Specifies the reference address of the current API version.</p>
    </td>
    </tr>
    <tr id="row113965641213"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p2139956101218"><a name="p2139956101218"></a><a name="p2139956101218"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p824653211138"><a name="p824653211138"></a><a name="p824653211138"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p513917563125"><a name="p513917563125"></a><a name="p513917563125"></a>Specifies the relationship between the current API version and the referenced address.</p>
    </td>
    </tr>
    <tr id="row12929787152631"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p13468556113518"><a name="p13468556113518"></a><a name="p13468556113518"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p18472756113513"><a name="p18472756113513"></a><a name="p18472756113513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p11474856173511"><a name="p11474856173511"></a><a name="p11474856173511"></a>If the APIs of this version support minor versions, set this parameter to the maximum minor version supported. If not, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row39341340152631"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p647516561358"><a name="p647516561358"></a><a name="p647516561358"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p164801756103517"><a name="p164801756103517"></a><a name="p164801756103517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p104811756113517"><a name="p104811756113517"></a><a name="p104811756113517"></a>Specifies the version status. Possible values are as follows:</p>
    <a name="ul4932195311538"></a><a name="ul4932195311538"></a><ul id="ul4932195311538"><li><strong id="b11954152420422"><a name="b11954152420422"></a><a name="b11954152420422"></a>CURRENT</strong>: indicates a primary version.</li><li><strong id="b3117229104215"><a name="b3117229104215"></a><a name="b3117229104215"></a>SUPPORTED</strong>: indicates an old version that is still supported.</li><li><strong id="b449312382428"><a name="b449312382428"></a><a name="b449312382428"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row398200152631"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p7486145617358"><a name="p7486145617358"></a><a name="p7486145617358"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p34901556173518"><a name="p34901556173518"></a><a name="p34901556173518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p14678111311550"><a name="p14678111311550"></a><a name="p14678111311550"></a>Specifies the version release time, which must be the UTC time.</p>
    <p id="p24932056163517"><a name="p24932056163517"></a><a name="p24932056163517"></a>For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
    </td>
    </tr>
    <tr id="row61549520152631"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.1.4.1.1 "><p id="p2495115693510"><a name="p2495115693510"></a><a name="p2495115693510"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.2 "><p id="p134991256203512"><a name="p134991256203512"></a><a name="p134991256203512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p205014565351"><a name="p205014565351"></a><a name="p205014565351"></a>If the APIs of this version support minor versions, set this parameter to the supported minimum minor version. If not, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "versions": [
            {
                "links": [
                    {
                        "rel": "self",
                        "href": "https://192.168.82.231:443/v2/"
                    }
                ],
                "id": "v2.0",
                "updated": "2018-09-21T12:33:21Z",
                "status": "SUPPORTED"
            }
        ]
    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

