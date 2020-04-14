# Querying an API Version \(Native OpenStack API\)<a name="EN-US_TOPIC_0170918588"></a>

## Function<a name="section18441284152049"></a>

This API is used to query a specified API version, such as version compatibility and domain name information of an API.

## URI<a name="section21923693152049"></a>

GET /\{api\_version\}

[Table 1](#table6209770492526)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table6209770492526"></a>
<table><thead align="left"><tr id="row4392035892526"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.1"><p id="p77928492526"><a name="p77928492526"></a><a name="p77928492526"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.73%" id="mcps1.2.5.1.2"><p id="p6312205492526"><a name="p6312205492526"></a><a name="p6312205492526"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="20.919999999999998%" id="mcps1.2.5.1.3"><p id="p1261277392526"><a name="p1261277392526"></a><a name="p1261277392526"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.61%" id="mcps1.2.5.1.4"><p id="p1500168892526"><a name="p1500168892526"></a><a name="p1500168892526"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row717722492526"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p4448425292526"><a name="p4448425292526"></a><a name="p4448425292526"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.2.5.1.2 "><p id="p4645465392526"><a name="p4645465392526"></a><a name="p4645465392526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p473051492526"><a name="p473051492526"></a><a name="p473051492526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.61%" headers="mcps1.2.5.1.4 "><p id="p4762733192526"><a name="p4762733192526"></a><a name="p4762733192526"></a>Specifies the API version, for example v2.0.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section62484847152049"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v2.0
    ```


## Response<a name="section47461859152049"></a>

-   Response parameters

    <a name="table38630935152049"></a>
    <table><thead align="left"><tr id="row1849976152049"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p15630386152049"><a name="p15630386152049"></a><a name="p15630386152049"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p58101744152049"><a name="p58101744152049"></a><a name="p58101744152049"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p27198362152049"><a name="p27198362152049"></a><a name="p27198362152049"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55583702152049"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p5985974152049"><a name="p5985974152049"></a><a name="p5985974152049"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p15101858152049"><a name="p15101858152049"></a><a name="p15101858152049"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p30612417152049"><a name="p30612417152049"></a><a name="p30612417152049"></a>Specifies the version.</p>
    <p id="p1025574924719"><a name="p1025574924719"></a><a name="p1025574924719"></a>For details, see <a href="#table854484962011">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  VersionInfo parameter description

    <a name="table854484962011"></a>
    <table><thead align="left"><tr id="row454414499200"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p15544144932017"><a name="p15544144932017"></a><a name="p15544144932017"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1354414918206"><a name="p1354414918206"></a><a name="p1354414918206"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p175441049112011"><a name="p175441049112011"></a><a name="p175441049112011"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3544134915207"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p554412490205"><a name="p554412490205"></a><a name="p554412490205"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p13544154992013"><a name="p13544154992013"></a><a name="p13544154992013"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13544549172014"><a name="p13544549172014"></a><a name="p13544549172014"></a>Specifies the API status.</p>
    </td>
    </tr>
    <tr id="row1654434982010"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7544144912017"><a name="p7544144912017"></a><a name="p7544144912017"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7544849202011"><a name="p7544849202011"></a><a name="p7544849202011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p854474942018"><a name="p854474942018"></a><a name="p854474942018"></a>Specifies the API ID.</p>
    </td>
    </tr>
    <tr id="row13545134914208"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p85451494204"><a name="p85451494204"></a><a name="p85451494204"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11545184910208"><a name="p11545184910208"></a><a name="p11545184910208"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p454514493203"><a name="p454514493203"></a><a name="p454514493203"></a>Specifies the description.</p>
    <p id="p1381418418482"><a name="p1381418418482"></a><a name="p1381418418482"></a>For details, see <a href="#table9477147162314">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Dict parameter description

    <a name="table9477147162314"></a>
    <table><thead align="left"><tr id="row147754713235"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p147713470235"><a name="p147713470235"></a><a name="p147713470235"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1847764752313"><a name="p1847764752313"></a><a name="p1847764752313"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p647724711236"><a name="p647724711236"></a><a name="p647724711236"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15478104772314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10478114720236"><a name="p10478114720236"></a><a name="p10478114720236"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2478104702312"><a name="p2478104702312"></a><a name="p2478104702312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1547818479233"><a name="p1547818479233"></a><a name="p1547818479233"></a>Specifies the domain name.</p>
    </td>
    </tr>
    <tr id="row181111958142415"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1911295882410"><a name="p1911295882410"></a><a name="p1911295882410"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p211211580241"><a name="p211211580241"></a><a name="p211211580241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4112758122414"><a name="p4112758122414"></a><a name="p4112758122414"></a>Specifies the domain name description.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    STATUS CODE 300
    ```

    ```
    {
        "versions": [
            {
                "status": "SUPPORTED",
                "id": "v2.0",
                "links": [
                    {
                        "href": "https://image.az1.dc1.domainname.com/v2/",
                        "rel": "self"
                    }
                ]
            }
        ]
    }
    ```


## Returned Values<a name="section37588986152049"></a>

-   Normal

    200

-   Abnormal

    <a name="table271454817439"></a>
    <table><thead align="left"><tr id="row3541095017439"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p4971469317439"><a name="p4971469317439"></a><a name="p4971469317439"></a>Returned Values</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p35835717439"><a name="p35835717439"></a><a name="p35835717439"></a>Description</p>
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


