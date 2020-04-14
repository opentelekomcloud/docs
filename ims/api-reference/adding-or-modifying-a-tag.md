# Adding or Modifying a Tag<a name="EN-US_TOPIC_0067360381"></a>

## Function<a name="section30340876173741"></a>

This API is used to add a tag to an image or modify a tag of an image. With tags, you can manage easily the images.

## URI<a name="section1046471173754"></a>

PUT /v1/cloudimages/tags

## Request<a name="section8520341173813"></a>

-   Request parameters

    <a name="table6337411917425"></a>
    <table><thead align="left"><tr id="row2485160717425"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p6453764617425"><a name="p6453764617425"></a><a name="p6453764617425"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p6016684317425"><a name="p6016684317425"></a><a name="p6016684317425"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.3"><p id="p4167613317425"><a name="p4167613317425"></a><a name="p4167613317425"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.4"><p id="p2032360317425"><a name="p2032360317425"></a><a name="p2032360317425"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4869470317425"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p11027285174310"><a name="p11027285174310"></a><a name="p11027285174310"></a>image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p20794863174310"><a name="p20794863174310"></a><a name="p20794863174310"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p6662325174310"><a name="p6662325174310"></a><a name="p6662325174310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p6489949174317"><a name="p6489949174317"></a><a name="p6489949174317"></a>Specifies the image ID.</p>
    <p id="p127065072116"><a name="p127065072116"></a><a name="p127065072116"></a>For details about how to obtain the image ID, see <a href="querying-images.md">Querying Images</a>.</p>
    </td>
    </tr>
    <tr id="row446091717425"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p21105754174331"><a name="p21105754174331"></a><a name="p21105754174331"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p31844545174331"><a name="p31844545174331"></a><a name="p31844545174331"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p29271315174331"><a name="p29271315174331"></a><a name="p29271315174331"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p4639858113657"><a name="p4639858113657"></a><a name="p4639858113657"></a>Specifies the tag.</p>
    <p id="p20992085173243"><a name="p20992085173243"></a><a name="p20992085173243"></a>Use either <strong id="b84235270693042"><a name="b84235270693042"></a><a name="b84235270693042"></a>tag</strong> or <strong id="b84235270693044"><a name="b84235270693044"></a><a name="b84235270693044"></a>image_tag</strong>.</p>
    </td>
    </tr>
    <tr id="row323937184633"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p51830302113147"><a name="p51830302113147"></a><a name="p51830302113147"></a>image_tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p6802785113147"><a name="p6802785113147"></a><a name="p6802785113147"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.3 "><p id="p19173032113147"><a name="p19173032113147"></a><a name="p19173032113147"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.4 "><p id="p5661683113147"><a name="p5661683113147"></a><a name="p5661683113147"></a>Lists the image tags. For detailed description, see <a href="image-tag-data-formats.md">Image Tag Data Formats</a>. This parameter is left blank by default.</p>
    <p id="p15340342977"><a name="p15340342977"></a><a name="p15340342977"></a>Use either <strong id="b1948808226"><a name="b1948808226"></a><a name="b1948808226"></a>tag</strong> or <strong id="b976702736"><a name="b976702736"></a><a name="b976702736"></a>image_tag</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request
    -   Example request containing parameter  **tag**

        ```
        PUT https://{Endpoint}/v1/cloudimages/tags
        ```

        ```
        {
          "image_id": "62a15f6c-9197-44d2-89c7-708981c1bec1",
          "tag": "aaaa.1111"
        }
        ```

    -   Example request containing parameter  **image\_tag**

        ```
        PUT https://{Endpoint}/v1/cloudimages/tags
        ```

        ```
        {
          "image_id": "67437ebd-2563-46e0-887e-ad1923977fa1",
          "image_tag": {"key":"key1","value":"value1"}
        }
        ```



## Response<a name="section39788910173834"></a>

-   Response parameters

    None

-   Example response

    ```
    STATUS CODE 204
    ```


## Returned Value<a name="section44583302173851"></a>

-   Normal

    204

-   Abnormal

    <a name="table14374540175339"></a>
    <table><thead align="left"><tr id="row16614073175339"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p32064062175339"><a name="p32064062175339"></a><a name="p32064062175339"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p47052264175339"><a name="p47052264175339"></a><a name="p47052264175339"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20817199175339"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p32333240175448"><a name="p32333240175448"></a><a name="p32333240175448"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1746788175448"><a name="p1746788175448"></a><a name="p1746788175448"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row1749657175339"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p65449231175448"><a name="p65449231175448"></a><a name="p65449231175448"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p66896379175448"><a name="p66896379175448"></a><a name="p66896379175448"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row34986904175339"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p46425689175448"><a name="p46425689175448"></a><a name="p46425689175448"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2384431175448"><a name="p2384431175448"></a><a name="p2384431175448"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row62469322175339"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p60528953175448"><a name="p60528953175448"></a><a name="p60528953175448"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3898164175448"><a name="p3898164175448"></a><a name="p3898164175448"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row45180882175339"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p23189406175448"><a name="p23189406175448"></a><a name="p23189406175448"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p66402567175448"><a name="p66402567175448"></a><a name="p66402567175448"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row40153247175339"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p21980411175448"><a name="p21980411175448"></a><a name="p21980411175448"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p35582892175448"><a name="p35582892175448"></a><a name="p35582892175448"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


