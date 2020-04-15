# Querying All API Versions<a name="sfs_02_0018"></a>

## Function<a name="section922844914513"></a>

This API is used to query all available versions of APIs provided by SFS.

To support function extension, SFS APIs can be distinguished by version. SFS has two types API version IDs:

Major version: Independent URL. For example:  **v1**  and  **v2**.

Microversion: with the HTTP request header  **X-Openstack-Manila-Api-Version: **_Microversion ID_. For example:  **X-Openstack-Manila-Api-Version: 2.4**.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API does not require authentication.  

## URI<a name="section1665327514513"></a>

-   GET /
-   Parameter description

None

## Request<a name="section5063604914513"></a>

-   Parameter description

    None

-   Example request

    GET https://\{endpoint\}/


## Response<a name="section6408307814513"></a>

-   Parameter description

    <a name="table1204662914513"></a>
    <table><thead align="left"><tr id="row5640646814513"><th class="cellrowborder" valign="top" width="19.72%" id="mcps1.1.4.1.1"><p id="p552118914513"><a name="p552118914513"></a><a name="p552118914513"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.54%" id="mcps1.1.4.1.2"><p id="p5284375514513"><a name="p5284375514513"></a><a name="p5284375514513"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.74%" id="mcps1.1.4.1.3"><p id="p5248579414513"><a name="p5248579414513"></a><a name="p5248579414513"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2349088414513"><td class="cellrowborder" valign="top" width="19.72%" headers="mcps1.1.4.1.1 "><p id="p2371346714513"><a name="p2371346714513"></a><a name="p2371346714513"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.54%" headers="mcps1.1.4.1.2 "><p id="p2571578314513"><a name="p2571578314513"></a><a name="p2571578314513"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.74%" headers="mcps1.1.4.1.3 "><p id="p1868846815102"><a name="p1868846815102"></a><a name="p1868846815102"></a>Lists objects of all available API versions, including <strong id="b579818912284"><a name="b579818912284"></a><a name="b579818912284"></a>v1</strong> and <strong id="b524481252813"><a name="b524481252813"></a><a name="b524481252813"></a>v2</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Description of the  **version**  field

    <a name="table6612891614513"></a>
    <table><thead align="left"><tr id="row2416468614513"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.36%" id="mcps1.1.4.1.2"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64%" id="mcps1.1.4.1.3"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5473431214513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p429429114513"><a name="p429429114513"></a><a name="p429429114513"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p5623047814513"><a name="p5623047814513"></a><a name="p5623047814513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p5837483014513"><a name="p5837483014513"></a><a name="p5837483014513"></a>Common name of the version</p>
    </td>
    </tr>
    <tr id="row124101142184120"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1841116421417"><a name="p1841116421417"></a><a name="p1841116421417"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p5411114210413"><a name="p5411114210413"></a><a name="p5411114210413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p7411114214418"><a name="p7411114214418"></a><a name="p7411114214418"></a>UTC time when the API is last modified. The format is YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row5561142314513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p823140914513"><a name="p823140914513"></a><a name="p823140914513"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p5074995814513"><a name="p5074995814513"></a><a name="p5074995814513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p5875536214030"><a name="p5875536214030"></a><a name="p5875536214030"></a>API version status, including:</p>
    <a name="ul7010819214058"></a><a name="ul7010819214058"></a><ul id="ul7010819214058"><li><strong id="b842352706235943"><a name="b842352706235943"></a><a name="b842352706235943"></a>CURRENT</strong>: indicates that the current API is the preferred version.</li><li><strong id="b7890108302"><a name="b7890108302"></a><a name="b7890108302"></a>SUPPORTED</strong>: indicates that the current version is an earlier version which is still supported.</li><li><strong id="b14630634173115"><a name="b14630634173115"></a><a name="b14630634173115"></a>DEPRECATED</strong>: indicates that the current version is a deprecated version that may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row1598568214513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1977187214513"><a name="p1977187214513"></a><a name="p1977187214513"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p182455114513"><a name="p182455114513"></a><a name="p182455114513"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p26535624151532"><a name="p26535624151532"></a><a name="p26535624151532"></a>Share links. For details, see the description of the <strong id="b186774613218"><a name="b186774613218"></a><a name="b186774613218"></a>links</strong> field.</p>
    </td>
    </tr>
    <tr id="row5502948014513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p2820292414513"><a name="p2820292414513"></a><a name="p2820292414513"></a>media-types</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p2024960914513"><a name="p2024960914513"></a><a name="p2024960914513"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p2960561814513"><a name="p2960561814513"></a><a name="p2960561814513"></a>Media types supported by the API. For details, see the description of the <strong id="b1627502312356"><a name="b1627502312356"></a><a name="b1627502312356"></a>media-types</strong> field.</p>
    </td>
    </tr>
    <tr id="row6512397414513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p4055052114513"><a name="p4055052114513"></a><a name="p4055052114513"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p3243232014513"><a name="p3243232014513"></a><a name="p3243232014513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p977226014513"><a name="p977226014513"></a><a name="p977226014513"></a>If the API in the current version supports microversions, this parameter is the latest microversion. If microversions are not supported, this parameter is an empty string.</p>
    </td>
    </tr>
    <tr id="row2084148314513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1043858314513"><a name="p1043858314513"></a><a name="p1043858314513"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p3650774114513"><a name="p3650774114513"></a><a name="p3650774114513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p433706314513"><a name="p433706314513"></a><a name="p433706314513"></a>If the API in the current version supports microversions, this parameter is the earliest microversion. If microversions are not supported, this parameter is an empty string.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **links**  field

    <a name="table1185748131212"></a>
    <table><thead align="left"><tr id="row085184881214"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p1385548131216"><a name="p1385548131216"></a><a name="p1385548131216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.36%" id="mcps1.1.4.1.2"><p id="p185548181220"><a name="p185548181220"></a><a name="p185548181220"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64%" id="mcps1.1.4.1.3"><p id="p785124815128"><a name="p785124815128"></a><a name="p785124815128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row128510489127"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p78554816123"><a name="p78554816123"></a><a name="p78554816123"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p186174811210"><a name="p186174811210"></a><a name="p186174811210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p88674821214"><a name="p88674821214"></a><a name="p88674821214"></a>API access path, which is used as a reference</p>
    </td>
    </tr>
    <tr id="row164131834144"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p204134351411"><a name="p204134351411"></a><a name="p204134351411"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p1262491711519"><a name="p1262491711519"></a><a name="p1262491711519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p1541415316146"><a name="p1541415316146"></a><a name="p1541415316146"></a>Type of the text returned by the reference API</p>
    </td>
    </tr>
    <tr id="row16345199111417"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p63455931416"><a name="p63455931416"></a><a name="p63455931416"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p1734579161412"><a name="p1734579161412"></a><a name="p1734579161412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p14346998145"><a name="p14346998145"></a><a name="p14346998145"></a>Additional description on links</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **media-types**

    <a name="table148711510121316"></a>
    <table><thead align="left"><tr id="row1487161011312"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p18872111011139"><a name="p18872111011139"></a><a name="p18872111011139"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.36%" id="mcps1.1.4.1.2"><p id="p987201014133"><a name="p987201014133"></a><a name="p987201014133"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64%" id="mcps1.1.4.1.3"><p id="p287281016132"><a name="p287281016132"></a><a name="p287281016132"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1587241013138"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p198721410151320"><a name="p198721410151320"></a><a name="p198721410151320"></a>base</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p118721210111310"><a name="p118721210111310"></a><a name="p118721210111310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p087261031310"><a name="p087261031310"></a><a name="p087261031310"></a>Basic text type</p>
    </td>
    </tr>
    <tr id="row1470713171416"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p3470141381410"><a name="p3470141381410"></a><a name="p3470141381410"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.1.4.1.2 "><p id="p114701613111411"><a name="p114701613111411"></a><a name="p114701613111411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64%" headers="mcps1.1.4.1.3 "><p id="p6470121319141"><a name="p6470121319141"></a><a name="p6470121319141"></a>Text type</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "versions": [
        {
          "status": "CURRENT",
          "updated": "2015-08-27T11:33:21Z",
          "links": [
            {
              "href": "http://docs.openstack.org/",
              "type": "text/html",
              "rel": "describedby"
            },
            {
              "href": "https://sfs.region.www.t-systems.com/v2/",
              "rel": "self"
            }
          ],
          "min_version": "2.0",
          "version": "2.28",
          "media-types": [
            {
              "base": "application/json",
              "type": "application/vnd.openstack.share+json;version=1"
            }
          ],
          "id": "v2.0"
        }
      ]
    }
    ```


## Status Codes<a name="section4959408514513"></a>

-   Normal

    300

-   Abnormal

    <a name="table6245403714513"></a>
    <table><thead align="left"><tr id="row1507735814513"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p1330652014513"><a name="p1330652014513"></a><a name="p1330652014513"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p408636314513"><a name="p408636314513"></a><a name="p408636314513"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6255996614513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3419245714513"><a name="p3419245714513"></a><a name="p3419245714513"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1812563714513"><a name="p1812563714513"></a><a name="p1812563714513"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row2891300914513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p6025236014513"><a name="p6025236014513"></a><a name="p6025236014513"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p4860301214513"><a name="p4860301214513"></a><a name="p4860301214513"></a>Invalid input: The post-deduction capacity must be larger than 0 and smaller than the current capacity. (Current capacity: <em id="i1442372620142837"><a name="i1442372620142837"></a><a name="i1442372620142837"></a>XX</em>; post-deduction capacity: <em id="i1852505181142837"><a name="i1852505181142837"></a><a name="i1852505181142837"></a>XX</em>)</p>
    </td>
    </tr>
    <tr id="row3477393214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p6522508214513"><a name="p6522508214513"></a><a name="p6522508214513"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p4874025614513"><a name="p4874025614513"></a><a name="p4874025614513"></a>Invalid input: The post-expansion capacity must be larger than the current capacity. (Current capacity: <em id="i167922714514297"><a name="i167922714514297"></a><a name="i167922714514297"></a>XX</em>; post-expansion capacity: <em id="i66903648114297"><a name="i66903648114297"></a><a name="i66903648114297"></a>XX</em>)</p>
    </td>
    </tr>
    <tr id="row3600912414513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3105792214513"><a name="p3105792214513"></a><a name="p3105792214513"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p3266375714513"><a name="p3266375714513"></a><a name="p3266375714513"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row2553835814513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p5534113514513"><a name="p5534113514513"></a><a name="p5534113514513"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p5344692014513"><a name="p5344692014513"></a><a name="p5344692014513"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="row1126023214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3966357214513"><a name="p3966357214513"></a><a name="p3966357214513"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p5863278914513"><a name="p5863278914513"></a><a name="p5863278914513"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="row5793306114513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p6206638414513"><a name="p6206638414513"></a><a name="p6206638414513"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p6132122014513"><a name="p6132122014513"></a><a name="p6132122014513"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row1502006814513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p866599114513"><a name="p866599114513"></a><a name="p866599114513"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p3085667914513"><a name="p3085667914513"></a><a name="p3085667914513"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row927465714513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1304973414513"><a name="p1304973414513"></a><a name="p1304973414513"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p5039554814513"><a name="p5039554814513"></a><a name="p5039554814513"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="row5090675314513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p2980630614513"><a name="p2980630614513"></a><a name="p2980630614513"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p6550061714513"><a name="p6550061714513"></a><a name="p6550061714513"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row5263464114513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3554751314513"><a name="p3554751314513"></a><a name="p3554751314513"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p6077628114513"><a name="p6077628114513"></a><a name="p6077628114513"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row1011562214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1405905414513"><a name="p1405905414513"></a><a name="p1405905414513"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p6504160314513"><a name="p6504160314513"></a><a name="p6504160314513"></a>The request is not completed because of a service error.</p>
    </td>
    </tr>
    <tr id="row4850351714513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3647083214513"><a name="p3647083214513"></a><a name="p3647083214513"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p134739514513"><a name="p134739514513"></a><a name="p134739514513"></a>The request is not completed because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row1212655614513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p4272696214513"><a name="p4272696214513"></a><a name="p4272696214513"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p3833193414513"><a name="p3833193414513"></a><a name="p3833193414513"></a>The request is not completed because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row944308614513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p2669253114513"><a name="p2669253114513"></a><a name="p2669253114513"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1461142514513"><a name="p1461142514513"></a><a name="p1461142514513"></a>The request is not completed because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row6439396214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p4852843914513"><a name="p4852843914513"></a><a name="p4852843914513"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p3848950514513"><a name="p3848950514513"></a><a name="p3848950514513"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


