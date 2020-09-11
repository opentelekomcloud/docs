# Querying Tags of an Image<a name="EN-US_TOPIC_0102682865"></a>

## Function<a name="section9600505183747"></a>

This API is used to query all the tags of a specified image.

## URI<a name="section26015555183747"></a>

GET /v2/\{project\_id\}/images/\{image\_id\}/tags

[Table 1](#table16231211183747)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table16231211183747"></a>
<table><thead align="left"><tr id="row34211813183747"><th class="cellrowborder" valign="top" width="18.55814418558144%" id="mcps1.2.5.1.1"><p id="p19693454183747"><a name="p19693454183747"></a><a name="p19693454183747"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.2"><p id="p51665940183747"><a name="p51665940183747"></a><a name="p51665940183747"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.3"><p id="p24191582183747"><a name="p24191582183747"></a><a name="p24191582183747"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.4"><p id="p13361108183747"><a name="p13361108183747"></a><a name="p13361108183747"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8508000183747"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p18059367183747"><a name="p18059367183747"></a><a name="p18059367183747"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p53522643183747"><a name="p53522643183747"></a><a name="p53522643183747"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p40366860183747"><a name="p40366860183747"></a><a name="p40366860183747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p48490233183747"><a name="p48490233183747"></a><a name="p48490233183747"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row33758919183747"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p50117918183747"><a name="p50117918183747"></a><a name="p50117918183747"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p33019549183747"><a name="p33019549183747"></a><a name="p33019549183747"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p57337837183747"><a name="p57337837183747"></a><a name="p57337837183747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p13853238183747"><a name="p13853238183747"></a><a name="p13853238183747"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section57570279183747"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v2/fd73a4a14a4a4dfb9771a8475e5198ea/images/67e17426-359e-49fb-aa12-0bd1756ec240/tags
    ```


## Response<a name="section29913939183747"></a>

-   Response parameters

    <a name="table39040786183747"></a>
    <table><thead align="left"><tr id="row55439147183747"><th class="cellrowborder" valign="top" width="33.78337833783378%" id="mcps1.1.4.1.1"><p id="p61385912183747"><a name="p61385912183747"></a><a name="p61385912183747"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.78337833783378%" id="mcps1.1.4.1.2"><p id="p32677523183747"><a name="p32677523183747"></a><a name="p32677523183747"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="32.43324332433243%" id="mcps1.1.4.1.3"><p id="p29633713183747"><a name="p29633713183747"></a><a name="p29633713183747"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51520592183747"><td class="cellrowborder" valign="top" width="33.78337833783378%" headers="mcps1.1.4.1.1 "><p id="p12418456183747"><a name="p12418456183747"></a><a name="p12418456183747"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.78337833783378%" headers="mcps1.1.4.1.2 "><p id="p7330880183747"><a name="p7330880183747"></a><a name="p7330880183747"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.43324332433243%" headers="mcps1.1.4.1.3 "><p id="p56930417183747"><a name="p56930417183747"></a><a name="p56930417183747"></a>Lists the tags.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Data structure description of the  **resource\_tag**  field

    <a name="table47961066183747"></a>
    <table><thead align="left"><tr id="row12649451183747"><th class="cellrowborder" valign="top" width="34.22%" id="mcps1.2.4.1.1"><p id="p17972593183747"><a name="p17972593183747"></a><a name="p17972593183747"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.77%" id="mcps1.2.4.1.2"><p id="p7914788183747"><a name="p7914788183747"></a><a name="p7914788183747"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="32.01%" id="mcps1.2.4.1.3"><p id="p37118112183747"><a name="p37118112183747"></a><a name="p37118112183747"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53777129183747"><td class="cellrowborder" valign="top" width="34.22%" headers="mcps1.2.4.1.1 "><p id="p60980198183747"><a name="p60980198183747"></a><a name="p60980198183747"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.2.4.1.2 "><p id="p55145502183747"><a name="p55145502183747"></a><a name="p55145502183747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.01%" headers="mcps1.2.4.1.3 "><p id="p37600681183747"><a name="p37600681183747"></a><a name="p37600681183747"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row2861810183747"><td class="cellrowborder" valign="top" width="34.22%" headers="mcps1.2.4.1.1 "><p id="p30480075183747"><a name="p30480075183747"></a><a name="p30480075183747"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.77%" headers="mcps1.2.4.1.2 "><p id="p62466949183747"><a name="p62466949183747"></a><a name="p62466949183747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.01%" headers="mcps1.2.4.1.3 "><p id="p26658103183747"><a name="p26658103183747"></a><a name="p26658103183747"></a>Specifies the tag value.</p>
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
       "tags": [{
          "value": "value0",
          "key": "key0"
       },
       {
          "value": "value0",
          "key": "key1"
       }]
    }
    ```


## Returned Value<a name="section39295631183747"></a>

-   Normal

    200

-   Abnormal

    <a name="table37923619183747"></a>
    <table><thead align="left"><tr id="row63239554183747"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p22130264183747"><a name="p22130264183747"></a><a name="p22130264183747"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p47720966183747"><a name="p47720966183747"></a><a name="p47720966183747"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40193077183747"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p34413837183747"><a name="p34413837183747"></a><a name="p34413837183747"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p36057397183747"><a name="p36057397183747"></a><a name="p36057397183747"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row56081118183747"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p46276738183747"><a name="p46276738183747"></a><a name="p46276738183747"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p57428298183747"><a name="p57428298183747"></a><a name="p57428298183747"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row47092639183747"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p56407449183747"><a name="p56407449183747"></a><a name="p56407449183747"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p5600684183747"><a name="p5600684183747"></a><a name="p5600684183747"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row50406158183747"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p56366968183747"><a name="p56366968183747"></a><a name="p56366968183747"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p2321678183747"><a name="p2321678183747"></a><a name="p2321678183747"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row20895110183747"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p14782346183747"><a name="p14782346183747"></a><a name="p14782346183747"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p56519407183747"><a name="p56519407183747"></a><a name="p56519407183747"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row38912621183747"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p64914630183747"><a name="p64914630183747"></a><a name="p64914630183747"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p23593683183747"><a name="p23593683183747"></a><a name="p23593683183747"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


