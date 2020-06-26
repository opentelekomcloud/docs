# Deleting an Image Tag<a name="EN-US_TOPIC_0102682864"></a>

## Function<a name="section59308875183714"></a>

This API is used to delete a specified tag from an image.

## Constraints<a name="section18061938183714"></a>

-   To be compatible with remaining tags, the system will not verify the character set and length of the keys and values in the query condition.
-   This API is a non-idempotent one. If the key to be deleted does not exist, status code 404 is returned.

## URI<a name="section5580419183714"></a>

DELETE /v2/\{project\_id\}/images/\{image\_id\}/tags/\{key\}

[Table 1](#table33665774183714)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table33665774183714"></a>
<table><thead align="left"><tr id="row7288033183714"><th class="cellrowborder" valign="top" width="18.55814418558144%" id="mcps1.2.5.1.1"><p id="p53459792183714"><a name="p53459792183714"></a><a name="p53459792183714"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.2"><p id="p35275920183714"><a name="p35275920183714"></a><a name="p35275920183714"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.3"><p id="p38777289183714"><a name="p38777289183714"></a><a name="p38777289183714"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.4"><p id="p53952674183714"><a name="p53952674183714"></a><a name="p53952674183714"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8090435183714"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p51345493183714"><a name="p51345493183714"></a><a name="p51345493183714"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p65344255183714"><a name="p65344255183714"></a><a name="p65344255183714"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p58393322183714"><a name="p58393322183714"></a><a name="p58393322183714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p32238654183714"><a name="p32238654183714"></a><a name="p32238654183714"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row21712430183714"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p13876401183714"><a name="p13876401183714"></a><a name="p13876401183714"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p50246705183714"><a name="p50246705183714"></a><a name="p50246705183714"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p43451285183714"><a name="p43451285183714"></a><a name="p43451285183714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p29893190183714"><a name="p29893190183714"></a><a name="p29893190183714"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row603254183714"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p48863620183714"><a name="p48863620183714"></a><a name="p48863620183714"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p65639187183714"><a name="p65639187183714"></a><a name="p65639187183714"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p15173963183714"><a name="p15173963183714"></a><a name="p15173963183714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p21131475183714"><a name="p21131475183714"></a><a name="p21131475183714"></a>Specifies the key of the tag to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section55965548183714"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v2/fd73a4a14a4a4dfb9771a8475e5198ea/images/67e17426-359e-49fb-aa12-0bd1756ec240/tags/key1
    ```


## Response<a name="section37371032183714"></a>

-   Response parameters

    None

-   Example response

    ```
    STATUS CODE 204
    ```


## Returned Value<a name="section64392887183714"></a>

-   Normal

    204

-   Abnormal

    <a name="table63464056183714"></a>
    <table><thead align="left"><tr id="row63000527183714"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p2769083183714"><a name="p2769083183714"></a><a name="p2769083183714"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p22969204183714"><a name="p22969204183714"></a><a name="p22969204183714"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48566241183714"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p41551467183714"><a name="p41551467183714"></a><a name="p41551467183714"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p10225657183714"><a name="p10225657183714"></a><a name="p10225657183714"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row24922053183714"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p5420437183714"><a name="p5420437183714"></a><a name="p5420437183714"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p36402270183714"><a name="p36402270183714"></a><a name="p36402270183714"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row59184975183714"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p29253631183714"><a name="p29253631183714"></a><a name="p29253631183714"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p20733883183714"><a name="p20733883183714"></a><a name="p20733883183714"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row52387226183714"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p15506900183714"><a name="p15506900183714"></a><a name="p15506900183714"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p48099407183714"><a name="p48099407183714"></a><a name="p48099407183714"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row30241484183714"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p33641163183714"><a name="p33641163183714"></a><a name="p33641163183714"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p40579678183714"><a name="p40579678183714"></a><a name="p40579678183714"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row29672787183714"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p54685536183714"><a name="p54685536183714"></a><a name="p54685536183714"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p343413183714"><a name="p343413183714"></a><a name="p343413183714"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


