# Querying a Specified API Version<a name="EN-US_TOPIC_0171212610"></a>

## Function<a name="section66578044"></a>

This API is used to query a specified API version supported by Cloud Eye.

## URI<a name="section62331491"></a>

GET /\{api\_version\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table23820074175412"></a>
    <table><thead align="left"><tr id="row17704405175412"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="p24770673175412"><a name="p24770673175412"></a><a name="p24770673175412"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.2"><p id="p60267522175412"><a name="p60267522175412"></a><a name="p60267522175412"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.08%" id="mcps1.2.4.1.3"><p id="p49831152175412"><a name="p49831152175412"></a><a name="p49831152175412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9791522175412"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p54915841175412"><a name="p54915841175412"></a><a name="p54915841175412"></a>api_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p18998132175412"><a name="p18998132175412"></a><a name="p18998132175412"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.08%" headers="mcps1.2.4.1.3 "><p id="p62453732175412"><a name="p62453732175412"></a><a name="p62453732175412"></a>Specifies the API version.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example

    ```
    GET https://{Cloud Eye endpoint}/V1.0
    ```


## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table26246518152631"></a>
    <table><thead align="left"><tr id="row29602547152631"><th class="cellrowborder" valign="top" width="18.72%" id="mcps1.2.4.1.1"><p id="p1143665616354"><a name="p1143665616354"></a><a name="p1143665616354"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="p11440156143517"><a name="p11440156143517"></a><a name="p11440156143517"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.55%" id="mcps1.2.4.1.3"><p id="p244212561357"><a name="p244212561357"></a><a name="p244212561357"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56174697152631"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p4445556153516"><a name="p4445556153516"></a><a name="p4445556153516"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p444855610353"><a name="p444855610353"></a><a name="p444855610353"></a>Objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p344911569354"><a name="p344911569354"></a><a name="p344911569354"></a>Specifies the list of all versions.</p>
    <p id="p76411522123610"><a name="p76411522123610"></a><a name="p76411522123610"></a>For details, see <a href="#table697164712507">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **versions**  field data structure description

    <a name="table697164712507"></a>
    <table><thead align="left"><tr id="row1898124785019"><th class="cellrowborder" valign="top" width="18.72%" id="mcps1.2.4.1.1"><p id="p4981247195018"><a name="p4981247195018"></a><a name="p4981247195018"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="p79844713504"><a name="p79844713504"></a><a name="p79844713504"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.55%" id="mcps1.2.4.1.3"><p id="p698194713501"><a name="p698194713501"></a><a name="p698194713501"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row89854714509"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p139834735010"><a name="p139834735010"></a><a name="p139834735010"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p298114755020"><a name="p298114755020"></a><a name="p298114755020"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p179964715014"><a name="p179964715014"></a><a name="p179964715014"></a>Specifies the version ID, for example, v1.</p>
    </td>
    </tr>
    <tr id="row299164795019"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p199919474509"><a name="p199919474509"></a><a name="p199919474509"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p8991047175014"><a name="p8991047175014"></a><a name="p8991047175014"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p59964795019"><a name="p59964795019"></a><a name="p59964795019"></a>Specifies the API URL.</p>
    <p id="p181431404541"><a name="p181431404541"></a><a name="p181431404541"></a>For details, see <a href="#table826514508503">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row79914725015"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p199974711501"><a name="p199974711501"></a><a name="p199974711501"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p12992477506"><a name="p12992477506"></a><a name="p12992477506"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p1613574610538"><a name="p1613574610538"></a><a name="p1613574610538"></a>Specifies the API version. If the APIs of this version support microversions, set this parameter to the supported maximum microversion. If the microversion is not supported, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row1910011478501"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p4100134718509"><a name="p4100134718509"></a><a name="p4100134718509"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p110019470505"><a name="p110019470505"></a><a name="p110019470505"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p1210024725017"><a name="p1210024725017"></a><a name="p1210024725017"></a>Specifies the version status. Possible values are as follows:</p>
    <p id="p1010024712509"><a name="p1010024712509"></a><a name="p1010024712509"></a><strong id="b842352706192132"><a name="b842352706192132"></a><a name="b842352706192132"></a>CURRENT</strong>: indicates a primary version.</p>
    <p id="p210054735017"><a name="p210054735017"></a><a name="p210054735017"></a><strong id="b842352706192150"><a name="b842352706192150"></a><a name="b842352706192150"></a>SUPPORTED</strong>: indicates an old version but is still supported.</p>
    <p id="p1100047125014"><a name="p1100047125014"></a><a name="p1100047125014"></a><strong id="b84235270619220"><a name="b84235270619220"></a><a name="b84235270619220"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</p>
    </td>
    </tr>
    <tr id="row1310017478505"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p3100154715016"><a name="p3100154715016"></a><a name="p3100154715016"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p141001847135012"><a name="p141001847135012"></a><a name="p141001847135012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p9100164765020"><a name="p9100164765020"></a><a name="p9100164765020"></a>Specifies the version release time, which must be the UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
    </td>
    </tr>
    <tr id="row5100144717502"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p1310010474502"><a name="p1310010474502"></a><a name="p1310010474502"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p7100134735019"><a name="p7100134735019"></a><a name="p7100134735019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p7556103913538"><a name="p7556103913538"></a><a name="p7556103913538"></a>If the APIs of this version support microversions, set this parameter to the supported minimum microversion. If not, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **links**  field data structure description

    <a name="table826514508503"></a>
    <table><thead align="left"><tr id="row15266125018507"><th class="cellrowborder" valign="top" width="18.72%" id="mcps1.2.4.1.1"><p id="p726618502508"><a name="p726618502508"></a><a name="p726618502508"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="p11266135011504"><a name="p11266135011504"></a><a name="p11266135011504"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.55%" id="mcps1.2.4.1.3"><p id="p726625019507"><a name="p726625019507"></a><a name="p726625019507"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16267105014508"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p726735018501"><a name="p726735018501"></a><a name="p726735018501"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p1526745015503"><a name="p1526745015503"></a><a name="p1526745015503"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p1726735085010"><a name="p1726735085010"></a><a name="p1726735085010"></a>Specifies the reference address of the current API version.</p>
    </td>
    </tr>
    <tr id="row1326725018501"><td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.2.4.1.1 "><p id="p72674509503"><a name="p72674509503"></a><a name="p72674509503"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="p132670509503"><a name="p132670509503"></a><a name="p132670509503"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.55%" headers="mcps1.2.4.1.3 "><p id="p15267750125020"><a name="p15267750125020"></a><a name="p15267750125020"></a>Specifies the relationship between the current API version and the referenced address.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
      "version": { 
          "id": "V1.0", 
          "links": [ 
            { 
              "href": "https://x.x.x.x/V1.0/", 
              "rel": "self" 
            } 
          ], 
          "min_version": "", 
          "status": "CURRENT", 
          "updated": "2018-09-30T00:00:00Z", 
          "version": "" 
        } 
    }
    ```


## Returned Value<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="table46793998"></a>
    <table><thead align="left"><tr id="row65573909"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p9886408"><a name="p9886408"></a><a name="p9886408"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p62601592"><a name="p62601592"></a><a name="p62601592"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37564172"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p22799085"><a name="p22799085"></a><a name="p22799085"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p44643603"><a name="p44643603"></a><a name="p44643603"></a>Request error</p>
    </td>
    </tr>
    <tr id="row66248115"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p64497130"><a name="p64497130"></a><a name="p64497130"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p42202994"><a name="p42202994"></a><a name="p42202994"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p30123063"><a name="p30123063"></a><a name="p30123063"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p15114764"><a name="p15114764"></a><a name="p15114764"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row1815156"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p12809933"><a name="p12809933"></a><a name="p12809933"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p10309404"><a name="p10309404"></a><a name="p10309404"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p66471715"><a name="p66471715"></a><a name="p66471715"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p5281111"><a name="p5281111"></a><a name="p5281111"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row47530006"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p24725298"><a name="p24725298"></a><a name="p24725298"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p39567352"><a name="p39567352"></a><a name="p39567352"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row20561848"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p54897010"><a name="p54897010"></a><a name="p54897010"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1451523117958"><a name="p1451523117958"></a><a name="p1451523117958"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section137621219143417"></a>

For details, see  [Error Codes](error-codes.md).

