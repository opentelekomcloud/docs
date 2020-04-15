# Querying Quotas<a name="EN-US_TOPIC_0171212590"></a>

## Function<a name="section66578044"></a>

This API is used to query a resource quota and the used amount. The current resource refers to alarm rules only.

## URI<a name="section62331491"></a>

GET /V1.0/\{project\_id\}/quotas

-   Parameter description

    **Table  1**  Parameter description

    <a name="table35846240171810"></a>
    <table><thead align="left"><tr id="row35634314171810"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="p698337171810"><a name="p698337171810"></a><a name="p698337171810"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.520000000000003%" id="mcps1.2.4.1.2"><p id="p56565365171810"><a name="p56565365171810"></a><a name="p56565365171810"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.49%" id="mcps1.2.4.1.3"><p id="p18391853171810"><a name="p18391853171810"></a><a name="p18391853171810"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13345138171810"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p7214379171810"><a name="p7214379171810"></a><a name="p7214379171810"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.520000000000003%" headers="mcps1.2.4.1.2 "><p id="p47493825171810"><a name="p47493825171810"></a><a name="p47493825171810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.49%" headers="mcps1.2.4.1.3 "><p id="p21794587171810"><a name="p21794587171810"></a><a name="p21794587171810"></a>Specifies the project ID.</p>
    <p id="p18591141575"><a name="p18591141575"></a><a name="p18591141575"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example: Query the alarm rule quota.

    ```
    GET https://{Cloud Eye endpoint}/V1.0/{project_id}/quotas
    ```


## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table42705518481"></a>
    <table><thead align="left"><tr id="row132701852487"><th class="cellrowborder" valign="top" width="13.919999999999998%" id="mcps1.2.4.1.1"><p id="p5270957481"><a name="p5270957481"></a><a name="p5270957481"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.33%" id="mcps1.2.4.1.2"><p id="p172701651483"><a name="p172701651483"></a><a name="p172701651483"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="73.75%" id="mcps1.2.4.1.3"><p id="p82701152484"><a name="p82701152484"></a><a name="p82701152484"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1127018534818"><td class="cellrowborder" valign="top" width="13.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p1027016514810"><a name="p1027016514810"></a><a name="p1027016514810"></a>quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.33%" headers="mcps1.2.4.1.2 "><p id="p18450111523616"><a name="p18450111523616"></a><a name="p18450111523616"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75%" headers="mcps1.2.4.1.3 "><p id="p192711858485"><a name="p192711858485"></a><a name="p192711858485"></a>Specifies the quota list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Response parameters

    <a name="table5856932152840"></a>
    <table><thead align="left"><tr id="row5206426152840"><th class="cellrowborder" valign="top" width="13.919999999999998%" id="mcps1.2.4.1.1"><p id="p19067323152840"><a name="p19067323152840"></a><a name="p19067323152840"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.33%" id="mcps1.2.4.1.2"><p id="p9786487152840"><a name="p9786487152840"></a><a name="p9786487152840"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="73.75%" id="mcps1.2.4.1.3"><p id="p54508002152840"><a name="p54508002152840"></a><a name="p54508002152840"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41015029105352"><td class="cellrowborder" valign="top" width="13.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p33883078105352"><a name="p33883078105352"></a><a name="p33883078105352"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.33%" headers="mcps1.2.4.1.2 "><p id="p42323558105352"><a name="p42323558105352"></a><a name="p42323558105352"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75%" headers="mcps1.2.4.1.3 "><p id="p5656197105352"><a name="p5656197105352"></a><a name="p5656197105352"></a>Specifies the resource quota list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Response parameters

    <a name="table3902130144815"></a>
    <table><thead align="left"><tr id="row109007015486"><th class="cellrowborder" valign="top" width="13.919999999999998%" id="mcps1.2.4.1.1"><p id="p15900109481"><a name="p15900109481"></a><a name="p15900109481"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.33%" id="mcps1.2.4.1.2"><p id="p5900200114811"><a name="p5900200114811"></a><a name="p5900200114811"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="73.75%" id="mcps1.2.4.1.3"><p id="p119009018486"><a name="p119009018486"></a><a name="p119009018486"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row119019044811"><td class="cellrowborder" valign="top" width="13.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p169014024810"><a name="p169014024810"></a><a name="p169014024810"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.33%" headers="mcps1.2.4.1.2 "><p id="p091411437363"><a name="p091411437363"></a><a name="p091411437363"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75%" headers="mcps1.2.4.1.3 "><p id="p79010019488"><a name="p79010019488"></a><a name="p79010019488"></a>Specifies the quota type.</p>
    <p id="p109017084815"><a name="p109017084815"></a><a name="p109017084815"></a><strong id="b310912710247"><a name="b310912710247"></a><a name="b310912710247"></a>alarm</strong> indicates the alarm rule.</p>
    </td>
    </tr>
    <tr id="row9901110114818"><td class="cellrowborder" valign="top" width="13.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p159013019489"><a name="p159013019489"></a><a name="p159013019489"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.33%" headers="mcps1.2.4.1.2 "><p id="p138071851103619"><a name="p138071851103619"></a><a name="p138071851103619"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75%" headers="mcps1.2.4.1.3 "><p id="p109014019483"><a name="p109014019483"></a><a name="p109014019483"></a>Specifies the used amount of the quota.</p>
    </td>
    </tr>
    <tr id="row209021101484"><td class="cellrowborder" valign="top" width="13.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p390212054810"><a name="p390212054810"></a><a name="p390212054810"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.33%" headers="mcps1.2.4.1.2 "><p id="p49029044813"><a name="p49029044813"></a><a name="p49029044813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75%" headers="mcps1.2.4.1.3 "><p id="p179021806488"><a name="p179021806488"></a><a name="p179021806488"></a>Specifies the quota unit.</p>
    </td>
    </tr>
    <tr id="row1490215013484"><td class="cellrowborder" valign="top" width="13.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p16902170104814"><a name="p16902170104814"></a><a name="p16902170104814"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.33%" headers="mcps1.2.4.1.2 "><p id="p119026084815"><a name="p119026084815"></a><a name="p119026084815"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.75%" headers="mcps1.2.4.1.3 "><p id="p390213012486"><a name="p390213012486"></a><a name="p390213012486"></a>Specifies the total amount of the quota.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
    "quotas": 
        { 
        "resources": [
                {
                    "type":"alarm",
                    "used":0, 
                    "unit":"",
                    "quota":20
                }
            ]
        } 
    }
    ```


## Returned Values<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="table46793998"></a>
    <table><thead align="left"><tr id="row65573909"><th class="cellrowborder" valign="top" width="31.580000000000002%" id="mcps1.1.3.1.1"><p id="p9886408"><a name="p9886408"></a><a name="p9886408"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="68.42%" id="mcps1.1.3.1.2"><p id="p62601592"><a name="p62601592"></a><a name="p62601592"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37564172"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p5859848991623"><a name="p5859848991623"></a><a name="p5859848991623"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.42%" headers="mcps1.1.3.1.2 "><p id="p4885720391623"><a name="p4885720391623"></a><a name="p4885720391623"></a>Request error</p>
    </td>
    </tr>
    <tr id="row66248115"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p4920367291623"><a name="p4920367291623"></a><a name="p4920367291623"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.42%" headers="mcps1.1.3.1.2 "><p id="p2607446691623"><a name="p2607446691623"></a><a name="p2607446691623"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1647740891623"><a name="p1647740891623"></a><a name="p1647740891623"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.42%" headers="mcps1.1.3.1.2 "><p id="p5960166891623"><a name="p5960166891623"></a><a name="p5960166891623"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row1815156"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3018159191623"><a name="p3018159191623"></a><a name="p3018159191623"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.42%" headers="mcps1.1.3.1.2 "><p id="p2878984091623"><a name="p2878984091623"></a><a name="p2878984091623"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p4982820391623"><a name="p4982820391623"></a><a name="p4982820391623"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.42%" headers="mcps1.1.3.1.2 "><p id="p955264291623"><a name="p955264291623"></a><a name="p955264291623"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row47530006"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p5166331291623"><a name="p5166331291623"></a><a name="p5166331291623"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.42%" headers="mcps1.1.3.1.2 "><p id="p2397871991623"><a name="p2397871991623"></a><a name="p2397871991623"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row20561848"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3218176391623"><a name="p3218176391623"></a><a name="p3218176391623"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.42%" headers="mcps1.1.3.1.2 "><p id="p5658597291623"><a name="p5658597291623"></a><a name="p5658597291623"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section915823415474"></a>

For details, see  [Error Codes](error-codes.md).

