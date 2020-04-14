# Querying Image Members \(Native OpenStack API\)<a name="EN-US_TOPIC_0036994320"></a>

## Function<a name="section24723024"></a>

This API is used to query the tenants with whom an image is shared using search criteria and to display the tenants in a list.

## URI<a name="section21180630"></a>

GET /v2/images/\{image\_id\}/members

[Table 1](#table27262282)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table27262282"></a>
<table><thead align="left"><tr id="row27551015"><th class="cellrowborder" valign="top" width="25.75%" id="mcps1.2.5.1.1"><p id="p17039762"><a name="p17039762"></a><a name="p17039762"></a><strong id="b65605719162353"><a name="b65605719162353"></a><a name="b65605719162353"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.81%" id="mcps1.2.5.1.2"><p id="p38043494"><a name="p38043494"></a><a name="p38043494"></a><strong id="b45657467162356"><a name="b45657467162356"></a><a name="b45657467162356"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.3"><p id="p1119157921331"><a name="p1119157921331"></a><a name="p1119157921331"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.4"><p id="p61624137"><a name="p61624137"></a><a name="p61624137"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25499238"><td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.1 "><p id="p52172387"><a name="p52172387"></a><a name="p52172387"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.81%" headers="mcps1.2.5.1.2 "><p id="p65213800"><a name="p65213800"></a><a name="p65213800"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.3 "><p id="p3410274521331"><a name="p3410274521331"></a><a name="p3410274521331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><p id="p47826462"><a name="p47826462"></a><a name="p47826462"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section56407950"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v2/images/d164b5df-1bc3-4c3f-893e-3e471fd16e64/members
    ```


## Response<a name="section37909503"></a>

-   Response parameters

    <a name="table3448659117582"></a>
    <table><thead align="left"><tr id="row1240616417582"><th class="cellrowborder" valign="top" width="30.486951304869514%" id="mcps1.1.4.1.1"><p id="p6537523417582"><a name="p6537523417582"></a><a name="p6537523417582"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.078292170782923%" id="mcps1.1.4.1.2"><p id="p3416692117582"><a name="p3416692117582"></a><a name="p3416692117582"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.1.4.1.3"><p id="p1605720117582"><a name="p1605720117582"></a><a name="p1605720117582"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2556488117582"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p202041354101614"><a name="p202041354101614"></a><a name="p202041354101614"></a>members</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p102036546164"><a name="p102036546164"></a><a name="p102036546164"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p1420210549169"><a name="p1420210549169"></a><a name="p1420210549169"></a>Specifies the members.</p>
    <p id="p05981305593"><a name="p05981305593"></a><a name="p05981305593"></a>For details, see <a href="#table47745347163">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row5330047317582"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p2237105217582"><a name="p2237105217582"></a><a name="p2237105217582"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p939051217582"><a name="p939051217582"></a><a name="p939051217582"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p2243400117582"><a name="p2243400117582"></a><a name="p2243400117582"></a>Specifies the sharing schema.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  MemberInfo parameter description

    <a name="table47745347163"></a>
    <table><thead align="left"><tr id="row177518341163"><th class="cellrowborder" valign="top" width="30.486951304869514%" id="mcps1.2.4.1.1"><p id="p157751734151616"><a name="p157751734151616"></a><a name="p157751734151616"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.987401259874016%" id="mcps1.2.4.1.2"><p id="p377543421614"><a name="p377543421614"></a><a name="p377543421614"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.525647435256474%" id="mcps1.2.4.1.3"><p id="p14775103451614"><a name="p14775103451614"></a><a name="p14775103451614"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row877510347162"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.2.4.1.1 "><p id="p27752348167"><a name="p27752348167"></a><a name="p27752348167"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.2 "><p id="p57752347164"><a name="p57752347164"></a><a name="p57752347164"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.525647435256474%" headers="mcps1.2.4.1.3 "><p id="p17755341167"><a name="p17755341167"></a><a name="p17755341167"></a>Specifies the image sharing status.</p>
    </td>
    </tr>
    <tr id="row2775113417167"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.2.4.1.1 "><p id="p577543414167"><a name="p577543414167"></a><a name="p577543414167"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.2 "><p id="p17775534161611"><a name="p17775534161611"></a><a name="p17775534161611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.525647435256474%" headers="mcps1.2.4.1.3 "><p id="p47756349164"><a name="p47756349164"></a><a name="p47756349164"></a>Specifies the time when a shared image was created. The value is in UTC format.</p>
    </td>
    </tr>
    <tr id="row1477583419160"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.2.4.1.1 "><p id="p577523419160"><a name="p577523419160"></a><a name="p577523419160"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.2 "><p id="p187759346162"><a name="p187759346162"></a><a name="p187759346162"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.525647435256474%" headers="mcps1.2.4.1.3 "><p id="p1277553417163"><a name="p1277553417163"></a><a name="p1277553417163"></a>Specifies the time when a shared image was updated. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row8776634121612"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.2.4.1.1 "><p id="p2776113410160"><a name="p2776113410160"></a><a name="p2776113410160"></a>image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.2 "><p id="p197761034141614"><a name="p197761034141614"></a><a name="p197761034141614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.525647435256474%" headers="mcps1.2.4.1.3 "><p id="p7776143461612"><a name="p7776143461612"></a><a name="p7776143461612"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="row4776183417161"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.2.4.1.1 "><p id="p6776203420161"><a name="p6776203420161"></a><a name="p6776203420161"></a>member_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.2 "><p id="p1377620348165"><a name="p1377620348165"></a><a name="p1377620348165"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.525647435256474%" headers="mcps1.2.4.1.3 "><p id="p147761734171613"><a name="p147761734171613"></a><a name="p147761734171613"></a>Specifies the member ID.</p>
    </td>
    </tr>
    <tr id="row8776163481619"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.2.4.1.1 "><p id="p37761534151618"><a name="p37761534151618"></a><a name="p37761534151618"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.987401259874016%" headers="mcps1.2.4.1.2 "><p id="p11776163431611"><a name="p11776163431611"></a><a name="p11776163431611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.525647435256474%" headers="mcps1.2.4.1.3 "><p id="p7776123401620"><a name="p7776123401620"></a><a name="p7776123401620"></a>Specifies the sharing schema.</p>
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
        "members": [
            {
                "status": "accepted",
                "created_at": "2016-09-01T02:05:14Z",
                "updated_at": "2016-09-01T02:37:11Z",
                "image_id": "d164b5df-1bc3-4c3f-893e-3e471fd16e64",
                "member_id": "edc89b490d7d4392898e19b2deb34797",
                "schema": "/v2/schemas/member"
            }
        ],
        "schema": "/v2/schemas/members"
    }
    ```


## Returned Values<a name="section61374531"></a>

-   Normal

    200

-   Abnormal

    <a name="table271454817439"></a>
    <table><thead align="left"><tr id="row3541095017439"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p4971469317439"><a name="p4971469317439"></a><a name="p4971469317439"></a><strong id="b63549115204622"><a name="b63549115204622"></a><a name="b63549115204622"></a>Returned Value</strong></p>
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


