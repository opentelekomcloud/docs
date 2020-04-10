# Updating the Image Sharing Status in Batches \(Native OpenStack API\)<a name="EN-US_TOPIC_0036994318"></a>

## Function<a name="section39958021"></a>

This API is used to update the image sharing status when a tenant accepts or rejects a shared image.

## URI<a name="section24077873"></a>

PUT /v2/images/\{image\_id\}/members/\{member\_id\}

[Table 1](#table37590215162351)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table37590215162351"></a>
<table><thead align="left"><tr id="row14906674162351"><th class="cellrowborder" valign="top" width="30.82691730826917%" id="mcps1.2.5.1.1"><p id="p66589937162351"><a name="p66589937162351"></a><a name="p66589937162351"></a><strong id="b3875848816228"><a name="b3875848816228"></a><a name="b3875848816228"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.2979702029797%" id="mcps1.2.5.1.2"><p id="p25075841162351"><a name="p25075841162351"></a><a name="p25075841162351"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.048195180481947%" id="mcps1.2.5.1.3"><p id="p3182134421246"><a name="p3182134421246"></a><a name="p3182134421246"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.82691730826917%" id="mcps1.2.5.1.4"><p id="p17877258162351"><a name="p17877258162351"></a><a name="p17877258162351"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row38771763162351"><td class="cellrowborder" valign="top" width="30.82691730826917%" headers="mcps1.2.5.1.1 "><p id="p944143142612"><a name="p944143142612"></a><a name="p944143142612"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.2979702029797%" headers="mcps1.2.5.1.2 "><p id="p9366762142612"><a name="p9366762142612"></a><a name="p9366762142612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.048195180481947%" headers="mcps1.2.5.1.3 "><p id="p20510233142612"><a name="p20510233142612"></a><a name="p20510233142612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.82691730826917%" headers="mcps1.2.5.1.4 "><p id="p50716165142612"><a name="p50716165142612"></a><a name="p50716165142612"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row5130782114260"><td class="cellrowborder" valign="top" width="30.82691730826917%" headers="mcps1.2.5.1.1 "><p id="p62209086142612"><a name="p62209086142612"></a><a name="p62209086142612"></a>member_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.2979702029797%" headers="mcps1.2.5.1.2 "><p id="p5771200142612"><a name="p5771200142612"></a><a name="p5771200142612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.048195180481947%" headers="mcps1.2.5.1.3 "><p id="p64814042142612"><a name="p64814042142612"></a><a name="p64814042142612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.82691730826917%" headers="mcps1.2.5.1.4 "><p id="p15446069142612"><a name="p15446069142612"></a><a name="p15446069142612"></a>Specifies the member ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section15374270"></a>

-   Request parameters

    <a name="table31018281142633"></a>
    <table><thead align="left"><tr id="row35509333142633"><th class="cellrowborder" valign="top" width="18.279999999999998%" id="mcps1.1.5.1.1"><p id="p57683706142633"><a name="p57683706142633"></a><a name="p57683706142633"></a><strong id="b12533317162228"><a name="b12533317162228"></a><a name="b12533317162228"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.83%" id="mcps1.1.5.1.2"><p id="p41868624142633"><a name="p41868624142633"></a><a name="p41868624142633"></a><strong id="b41457289162230"><a name="b41457289162230"></a><a name="b41457289162230"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.28%" id="mcps1.1.5.1.3"><p id="p35915390142633"><a name="p35915390142633"></a><a name="p35915390142633"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.61%" id="mcps1.1.5.1.4"><p id="p23465517142633"><a name="p23465517142633"></a><a name="p23465517142633"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21658757142633"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.1.5.1.1 "><p id="p9528877142633"><a name="p9528877142633"></a><a name="p9528877142633"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.83%" headers="mcps1.1.5.1.2 "><p id="p33641549142633"><a name="p33641549142633"></a><a name="p33641549142633"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.28%" headers="mcps1.1.5.1.3 "><p id="p40610958142633"><a name="p40610958142633"></a><a name="p40610958142633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.61%" headers="mcps1.1.5.1.4 "><p id="p461165194819"><a name="p461165194819"></a><a name="p461165194819"></a>Specifies whether a shared image will be accepted or declined.</p>
    <p id="p166859539539"><a name="p166859539539"></a><a name="p166859539539"></a>Available values include:</p>
    <a name="ul346242429557"></a><a name="ul346242429557"></a><ul id="ul346242429557"><li><strong id="b1137310403226"><a name="b1137310403226"></a><a name="b1137310403226"></a>accepted</strong>: indicates that a shared image is accepted. After an image is accepted, the image is displayed in the image list. You can use the image to create <span id="text1013631371215"><a name="text1013631371215"></a><a name="text1013631371215"></a>ECS</span><span id="text20797319151218"><a name="text20797319151218"></a><a name="text20797319151218"></a></span>s.</li><li><strong id="b312435229"><a name="b312435229"></a><a name="b312435229"></a>rejected</strong>: indicates that a shared image is declined. After an image is rejected, the image is not displayed in the image list. However, you can still use the image to create <span id="text1028103661311"><a name="text1028103661311"></a><a name="text1028103661311"></a>ECS</span><span id="text82811536111310"><a name="text82811536111310"></a><a name="text82811536111310"></a></span>s.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PUT https://{Endpoint}/v2/images/d164b5df-1bc3-4c3f-893e-3e471fd16e64/members/edc89b490d7d4392898e19b2deb34797
    ```

    ```
    {
        "status":"accepted"
    }
    ```


## Response<a name="section4150710"></a>

-   Response parameters

    <a name="table3940930519484"></a>
    <table><thead align="left"><tr id="row5108650619484"><th class="cellrowborder" valign="top" width="27.389999999999997%" id="mcps1.1.4.1.1"><p id="p4436630719484"><a name="p4436630719484"></a><a name="p4436630719484"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.469999999999999%" id="mcps1.1.4.1.2"><p id="p3690111319484"><a name="p3690111319484"></a><a name="p3690111319484"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.14%" id="mcps1.1.4.1.3"><p id="p3620014719484"><a name="p3620014719484"></a><a name="p3620014719484"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4653077719484"><td class="cellrowborder" valign="top" width="27.389999999999997%" headers="mcps1.1.4.1.1 "><p id="p1237238714338"><a name="p1237238714338"></a><a name="p1237238714338"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.2 "><p id="p4061628614338"><a name="p4061628614338"></a><a name="p4061628614338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.14%" headers="mcps1.1.4.1.3 "><p id="p158487614338"><a name="p158487614338"></a><a name="p158487614338"></a>Specifies the image sharing status.</p>
    </td>
    </tr>
    <tr id="row6237230419484"><td class="cellrowborder" valign="top" width="27.389999999999997%" headers="mcps1.1.4.1.1 "><p id="p1452463514338"><a name="p1452463514338"></a><a name="p1452463514338"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.2 "><p id="p154357214338"><a name="p154357214338"></a><a name="p154357214338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.14%" headers="mcps1.1.4.1.3 "><p id="p5792053614338"><a name="p5792053614338"></a><a name="p5792053614338"></a>Specifies the time when a shared image was created. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row5992935019484"><td class="cellrowborder" valign="top" width="27.389999999999997%" headers="mcps1.1.4.1.1 "><p id="p1259565314338"><a name="p1259565314338"></a><a name="p1259565314338"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.2 "><p id="p2907381014338"><a name="p2907381014338"></a><a name="p2907381014338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.14%" headers="mcps1.1.4.1.3 "><p id="p616838914338"><a name="p616838914338"></a><a name="p616838914338"></a>Specifies the time when a shared image was updated. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row1403543619484"><td class="cellrowborder" valign="top" width="27.389999999999997%" headers="mcps1.1.4.1.1 "><p id="p46179614338"><a name="p46179614338"></a><a name="p46179614338"></a>image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.2 "><p id="p995083914338"><a name="p995083914338"></a><a name="p995083914338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.14%" headers="mcps1.1.4.1.3 "><p id="p71165114338"><a name="p71165114338"></a><a name="p71165114338"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="row4544843919484"><td class="cellrowborder" valign="top" width="27.389999999999997%" headers="mcps1.1.4.1.1 "><p id="p4903219314338"><a name="p4903219314338"></a><a name="p4903219314338"></a>member_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.2 "><p id="p4743364614338"><a name="p4743364614338"></a><a name="p4743364614338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.14%" headers="mcps1.1.4.1.3 "><p id="p1692010914338"><a name="p1692010914338"></a><a name="p1692010914338"></a>Specifies the member ID.</p>
    </td>
    </tr>
    <tr id="row4954506419484"><td class="cellrowborder" valign="top" width="27.389999999999997%" headers="mcps1.1.4.1.1 "><p id="p5383793114338"><a name="p5383793114338"></a><a name="p5383793114338"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.2 "><p id="p3671632714338"><a name="p3671632714338"></a><a name="p3671632714338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.14%" headers="mcps1.1.4.1.3 "><p id="p2123248314338"><a name="p2123248314338"></a><a name="p2123248314338"></a>Specifies the sharing schema.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    STATUS CODE 200
    ```

    ```
    {
        "status": "accepted",
        "created_at": "2016-09-01T02:05:14Z",
        "updated_at": "2016-09-01T02:37:11Z",
        "image_id": "d164b5df-1bc3-4c3f-893e-3e471fd16e64",
        "member_id": "edc89b490d7d4392898e19b2deb34797",
        "schema": "/v2/schemas/member"
    }
    ```


## Returned Values<a name="section61374531"></a>

-   Normal

    200

-   Abnormal

    <a name="table271454817439"></a>
    <table><thead align="left"><tr id="row3541095017439"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p4971469317439"><a name="p4971469317439"></a><a name="p4971469317439"></a><strong>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p35835717439"><a name="p35835717439"></a><a name="p35835717439"></a><strong id="b84235270616929"><a name="b84235270616929"></a><a name="b84235270616929"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2902697417439"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p237466317439"><a name="p237466317439"></a><a name="p237466317439"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p5812997617439"><a name="p5812997617439"></a><a name="p5812997617439"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row5340773917439"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p3105962817439"><a name="p3105962817439"></a><a name="p3105962817439"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p3280197817439"><a name="p3280197817439"></a><a name="p3280197817439"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row2678235117439"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p2188683517439"><a name="p2188683517439"></a><a name="p2188683517439"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2800317417439"><a name="p2800317417439"></a><a name="p2800317417439"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row16775501191954"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p19013873191957"><a name="p19013873191957"></a><a name="p19013873191957"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p63728762191957"><a name="p63728762191957"></a><a name="p63728762191957"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row5070198217439"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p1321988617439"><a name="p1321988617439"></a><a name="p1321988617439"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p6417782617439"><a name="p6417782617439"></a><a name="p6417782617439"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row4072952517439"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p1075724317439"><a name="p1075724317439"></a><a name="p1075724317439"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p6603036117439"><a name="p6603036117439"></a><a name="p6603036117439"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


