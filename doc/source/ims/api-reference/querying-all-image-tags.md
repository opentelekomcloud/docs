# Querying All Image Tags<a name="EN-US_TOPIC_0102682866"></a>

## Function<a name="section9844937183829"></a>

This API is used to query all the image tags.

## URI<a name="section35296793183829"></a>

GET /v2/\{project\_id\}/images/tags

[Table 1](#table49437288183829)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table49437288183829"></a>
<table><thead align="left"><tr id="row8590979183829"><th class="cellrowborder" valign="top" width="18.55814418558144%" id="mcps1.2.5.1.1"><p id="p24780738183829"><a name="p24780738183829"></a><a name="p24780738183829"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.2"><p id="p61082794183829"><a name="p61082794183829"></a><a name="p61082794183829"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.3"><p id="p48759266183829"><a name="p48759266183829"></a><a name="p48759266183829"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.4"><p id="p57186450183829"><a name="p57186450183829"></a><a name="p57186450183829"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1590883183829"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p61752700183829"><a name="p61752700183829"></a><a name="p61752700183829"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p35912838183829"><a name="p35912838183829"></a><a name="p35912838183829"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p23258793183829"><a name="p23258793183829"></a><a name="p23258793183829"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p4914060183829"><a name="p4914060183829"></a><a name="p4914060183829"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section44226541183829"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v2/fd73a4a14a4a4dfb9771a8475e5198ea/images/tags
    ```


## Response<a name="section58718287183829"></a>

-   Response parameters

    <a name="table45802274183829"></a>
    <table><thead align="left"><tr id="row14285173183829"><th class="cellrowborder" valign="top" width="33.78337833783378%" id="mcps1.1.4.1.1"><p id="p16248356183829"><a name="p16248356183829"></a><a name="p16248356183829"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.872787278727873%" id="mcps1.1.4.1.2"><p id="p36592925183829"><a name="p36592925183829"></a><a name="p36592925183829"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.34383438343835%" id="mcps1.1.4.1.3"><p id="p11236918183829"><a name="p11236918183829"></a><a name="p11236918183829"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37775127183829"><td class="cellrowborder" valign="top" width="33.78337833783378%" headers="mcps1.1.4.1.1 "><p id="p39886441183829"><a name="p39886441183829"></a><a name="p39886441183829"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.872787278727873%" headers="mcps1.1.4.1.2 "><p id="p37480830183829"><a name="p37480830183829"></a><a name="p37480830183829"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.34383438343835%" headers="mcps1.1.4.1.3 "><p id="p16048402183829"><a name="p16048402183829"></a><a name="p16048402183829"></a>Lists tags.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Data structure description of the  **tags**  field

    <a name="table24852149183829"></a>
    <table><thead align="left"><tr id="row17696442183829"><th class="cellrowborder" valign="top" width="34.31%" id="mcps1.2.4.1.1"><p id="p24125663183829"><a name="p24125663183829"></a><a name="p24125663183829"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="27.68%" id="mcps1.2.4.1.2"><p id="p45775079183829"><a name="p45775079183829"></a><a name="p45775079183829"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.01%" id="mcps1.2.4.1.3"><p id="p16793881183829"><a name="p16793881183829"></a><a name="p16793881183829"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18127136183829"><td class="cellrowborder" valign="top" width="34.31%" headers="mcps1.2.4.1.1 "><p id="p59011940183829"><a name="p59011940183829"></a><a name="p59011940183829"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.68%" headers="mcps1.2.4.1.2 "><p id="p26305217183829"><a name="p26305217183829"></a><a name="p26305217183829"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.01%" headers="mcps1.2.4.1.3 "><p id="p50347818183829"><a name="p50347818183829"></a><a name="p50347818183829"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row50477182183829"><td class="cellrowborder" valign="top" width="34.31%" headers="mcps1.2.4.1.1 "><p id="p62119921183829"><a name="p62119921183829"></a><a name="p62119921183829"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.68%" headers="mcps1.2.4.1.2 "><p id="p547751991834"><a name="p547751991834"></a><a name="p547751991834"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.01%" headers="mcps1.2.4.1.3 "><p id="p8217820183829"><a name="p8217820183829"></a><a name="p8217820183829"></a>Lists the tag values. If a tag contains the key only, tag values will be empty character strings.</p>
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
          "values": ["value9"],
          "key": "key9"
       },
       {
          "values": [""],
          "key": "key8"
       },
       {
          "values": 
            ["valueXX",
            "value3"],
          "key": "key3"
       }]
    }
    ```


## Returned Value<a name="section18102511183829"></a>

-   Normal

    200

-   Abnormal

    <a name="table25832287183829"></a>
    <table><thead align="left"><tr id="row53367465183829"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p27797426183829"><a name="p27797426183829"></a><a name="p27797426183829"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p36999003183829"><a name="p36999003183829"></a><a name="p36999003183829"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44129228183829"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p17697710183829"><a name="p17697710183829"></a><a name="p17697710183829"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p24228392183829"><a name="p24228392183829"></a><a name="p24228392183829"></a>Request error</p>
    </td>
    </tr>
    <tr id="row16728942183829"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p12867072183829"><a name="p12867072183829"></a><a name="p12867072183829"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p35599935183829"><a name="p35599935183829"></a><a name="p35599935183829"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row51963962183829"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p48331431183829"><a name="p48331431183829"></a><a name="p48331431183829"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p22531828183829"><a name="p22531828183829"></a><a name="p22531828183829"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row1459862183829"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p51139991183829"><a name="p51139991183829"></a><a name="p51139991183829"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p48698572183829"><a name="p48698572183829"></a><a name="p48698572183829"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row35633965183829"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p670092183829"><a name="p670092183829"></a><a name="p670092183829"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p54277524183829"><a name="p54277524183829"></a><a name="p54277524183829"></a>Internal service error</p>
    </td>
    </tr>
    <tr id="row18735670183829"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p41194317183829"><a name="p41194317183829"></a><a name="p41194317183829"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p48405409183829"><a name="p48405409183829"></a><a name="p48405409183829"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


