# Adding a Tag \(Native OpenStack API\)<a name="EN-US_TOPIC_0020092111"></a>

## Function<a name="section43944024"></a>

This API is used to add a custom tag to an image. With tags, you can manage easily the images.

## URI<a name="section59951903"></a>

PUT /v2/images/\{image\_id\}/tags/\{tag\}

[Table 1](#table58396974)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table58396974"></a>
<table><thead align="left"><tr id="row52161898"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.2.5.1.1"><p id="p64364196"><a name="p64364196"></a><a name="p64364196"></a><strong id="b29862858161838"><a name="b29862858161838"></a><a name="b29862858161838"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.68%" id="mcps1.2.5.1.2"><p id="p40455902205623"><a name="p40455902205623"></a><a name="p40455902205623"></a><strong id="b31324481161845"><a name="b31324481161845"></a><a name="b31324481161845"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.119999999999997%" id="mcps1.2.5.1.3"><p id="p46117407"><a name="p46117407"></a><a name="p46117407"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="35.709999999999994%" id="mcps1.2.5.1.4"><p id="p44522499"><a name="p44522499"></a><a name="p44522499"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49552630"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.2.5.1.1 "><p id="p54340131"><a name="p54340131"></a><a name="p54340131"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.5.1.2 "><p id="p15622373205623"><a name="p15622373205623"></a><a name="p15622373205623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.5.1.3 "><p id="p39474480"><a name="p39474480"></a><a name="p39474480"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.5.1.4 "><p id="p43316293"><a name="p43316293"></a><a name="p43316293"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row54302323"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.2.5.1.1 "><p id="p36412008"><a name="p36412008"></a><a name="p36412008"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.5.1.2 "><p id="p47312118205623"><a name="p47312118205623"></a><a name="p47312118205623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.5.1.3 "><p id="p63691513"><a name="p63691513"></a><a name="p63691513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.2.5.1.4 "><p id="p75636161112"><a name="p75636161112"></a><a name="p75636161112"></a>Specifies the tag to be added.</p>
<p id="p15777461117"><a name="p15777461117"></a><a name="p15777461117"></a>The tag can contain only digits, letters, underscores (_), and hyphens (-).</p>
<div class="note" id="note1350761815387"><a name="note1350761815387"></a><a name="note1350761815387"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p550721883817"><a name="p550721883817"></a><a name="p550721883817"></a>This API can only be used to add a tag key. To add a tag value, use the PUT /v1/cloudimages/tags API. For details, see <a href="adding-or-modifying-a-tag.md">Adding or Modifying a Tag</a>.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Request<a name="section2696221"></a>

-   Request parameters

    None

-   Example request

    ```
    PUT https://{Endpoint}/v2/images/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90/tags/aaaa
    ```


## Response<a name="section24265995"></a>

-   Response parameters

    None

-   Example response

    ```
    STATUS CODE 204
    ```


## Returned Values<a name="section17067371"></a>

-   Normal

    204

-   Abnormal

    <a name="table642803117411"></a>
    <table><thead align="left"><tr id="row109645217411"><th class="cellrowborder" valign="top" width="38.080000000000005%" id="mcps1.1.3.1.1"><p id="p2170376317411"><a name="p2170376317411"></a><a name="p2170376317411"></a><strong id="b39973114161856"><a name="b39973114161856"></a><a name="b39973114161856"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.919999999999995%" id="mcps1.1.3.1.2"><p id="p1317436717411"><a name="p1317436717411"></a><a name="p1317436717411"></a><strong id="b5047798416190"><a name="b5047798416190"></a><a name="b5047798416190"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6049076717411"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p80506717411"><a name="p80506717411"></a><a name="p80506717411"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p6521049217411"><a name="p6521049217411"></a><a name="p6521049217411"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row5002352417411"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p2537366317411"><a name="p2537366317411"></a><a name="p2537366317411"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p4200083517411"><a name="p4200083517411"></a><a name="p4200083517411"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row4246319517411"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p1696676617411"><a name="p1696676617411"></a><a name="p1696676617411"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p3213081417411"><a name="p3213081417411"></a><a name="p3213081417411"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row22446538192234"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p2466565192236"><a name="p2466565192236"></a><a name="p2466565192236"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p65574046192236"><a name="p65574046192236"></a><a name="p65574046192236"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row2074187217411"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p237005317411"><a name="p237005317411"></a><a name="p237005317411"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p5775661917411"><a name="p5775661917411"></a><a name="p5775661917411"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row5004752817411"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p2731794517411"><a name="p2731794517411"></a><a name="p2731794517411"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p6526996817411"><a name="p6526996817411"></a><a name="p6526996817411"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


