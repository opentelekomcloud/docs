# Replicating an Image Within a Region<a name="EN-US_TOPIC_0049147856"></a>

## Function<a name="section57853128105524"></a>

This API is an extension one and is used to copy an existing image to another image. When replicating an image, you can change the image attributes to meet the requirements of different scenarios.

This API is an asynchronous one. If  **job\_id**  is returned, the task is successfully delivered. You need to query the status of the asynchronous task. If the status is  **success**, the task is successfully executed. If the status is  **failed**, the task fails. For details about how to query the status of an asynchronous task, see  [Asynchronous Job Query](asynchronous-job-query.md).

## Constraints<a name="section183915210102"></a>

You can replicate private images in  **Normal**  or  **Normal \(Uninitialized\)**  state.

Full-ECS images cannot be replicated.

## URI<a name="section30564347105524"></a>

POST /v1/cloudimages/\{image\_id\}/copy

[Table 1](#table51065259105524)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table51065259105524"></a>
<table><thead align="left"><tr id="row36742558105524"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p23357191105524"><a name="p23357191105524"></a><a name="p23357191105524"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.007999200079993%" id="mcps1.2.5.1.2"><p id="p12884280105524"><a name="p12884280105524"></a><a name="p12884280105524"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="20.087991200879912%" id="mcps1.2.5.1.3"><p id="p36993754105524"><a name="p36993754105524"></a><a name="p36993754105524"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.515948405159484%" id="mcps1.2.5.1.4"><p id="p43704084105524"><a name="p43704084105524"></a><a name="p43704084105524"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row50369935105524"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p53432947105524"><a name="p53432947105524"></a><a name="p53432947105524"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.007999200079993%" headers="mcps1.2.5.1.2 "><p id="p33101414105524"><a name="p33101414105524"></a><a name="p33101414105524"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.087991200879912%" headers="mcps1.2.5.1.3 "><p id="p63968915105524"><a name="p63968915105524"></a><a name="p63968915105524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.515948405159484%" headers="mcps1.2.5.1.4 "><p id="p14099616105524"><a name="p14099616105524"></a><a name="p14099616105524"></a>Specifies the image ID.</p>
<p id="p127065072116"><a name="p127065072116"></a><a name="p127065072116"></a>For details about how to obtain the image ID, see <a href="querying-images.md">Querying Images</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1218229105524"></a>

-   Request parameters

    <a name="table6850073105524"></a>
    <table><thead align="left"><tr id="row3268825105524"><th class="cellrowborder" valign="top" width="26.26%" id="mcps1.1.5.1.1"><p id="p63448301105524"><a name="p63448301105524"></a><a name="p63448301105524"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.43%" id="mcps1.1.5.1.2"><p id="p39038757105524"><a name="p39038757105524"></a><a name="p39038757105524"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.97%" id="mcps1.1.5.1.3"><p id="p8022762105524"><a name="p8022762105524"></a><a name="p8022762105524"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.339999999999996%" id="mcps1.1.5.1.4"><p id="p45863971105524"><a name="p45863971105524"></a><a name="p45863971105524"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23994169105524"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.1.5.1.1 "><p id="p64479507105524"><a name="p64479507105524"></a><a name="p64479507105524"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.2 "><p id="p55457561105524"><a name="p55457561105524"></a><a name="p55457561105524"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.1.5.1.3 "><p id="p62877493105524"><a name="p62877493105524"></a><a name="p62877493105524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p34441981163338"><a name="p34441981163338"></a><a name="p34441981163338"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row2338354105524"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.1.5.1.1 "><p id="p55189008105524"><a name="p55189008105524"></a><a name="p55189008105524"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.2 "><p id="p41124638105524"><a name="p41124638105524"></a><a name="p41124638105524"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.1.5.1.3 "><p id="p42761348105524"><a name="p42761348105524"></a><a name="p42761348105524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p30451415163338"><a name="p30451415163338"></a><a name="p30451415163338"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>. The value contains a maximum of 1024 characters and consists of only letters and digits. Carriage returns and angle brackets (&lt; &gt;) are not allowed. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row34510150105524"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.1.5.1.1 "><p id="p43858769105524"><a name="p43858769105524"></a><a name="p43858769105524"></a>cmk_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.2 "><p id="p62899376105524"><a name="p62899376105524"></a><a name="p62899376105524"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.1.5.1.3 "><p id="p61684684105524"><a name="p61684684105524"></a><a name="p61684684105524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p30403468105524"><a name="p30403468105524"></a><a name="p30403468105524"></a>Specifies the encryption key. This parameter is left blank by default.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v1/cloudimages/465076de-dc36-4aec-80f5-ef9d8009428f/copy
    ```

    ```
    {
        "name": "ims_encrypted_copy3",
        "description": "test copy",
        "cmk_id": "bd66288c-9081-460a-8227-4cbd0c814cb4"
    }
    ```


## Response<a name="section32485736105524"></a>

-   Response parameters

    <a name="table1162152105524"></a>
    <table><thead align="left"><tr id="row45730117105524"><th class="cellrowborder" valign="top" width="30.486951304869514%" id="mcps1.1.4.1.1"><p id="p13151974105524"><a name="p13151974105524"></a><a name="p13151974105524"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.078292170782923%" id="mcps1.1.4.1.2"><p id="p55216927105524"><a name="p55216927105524"></a><a name="p55216927105524"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.1.4.1.3"><p id="p43386118105524"><a name="p43386118105524"></a><a name="p43386118105524"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24614698105524"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p47633522105524"><a name="p47633522105524"></a><a name="p47633522105524"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p64671376105524"><a name="p64671376105524"></a><a name="p64671376105524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p3890102105524"><a name="p3890102105524"></a><a name="p3890102105524"></a>Specifies the asynchronous job ID.</p>
    <p id="p19968122117312"><a name="p19968122117312"></a><a name="p19968122117312"></a>For details, see <a href="asynchronous-job-query.md">Asynchronous Job Query</a>.</p>
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
        "job_id": "edc89b490d7d4392898e19b2deb34797"
    }
    ```


## Returned Value<a name="section40084941"></a>

-   Normal

    200

-   Abnormal

    <a name="table1069408417333"></a>
    <table><thead align="left"><tr id="row4772021317333"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p4013206717333"><a name="p4013206717333"></a><a name="p4013206717333"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p2947196917333"><a name="p2947196917333"></a><a name="p2947196917333"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3841925517333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p2495195017333"><a name="p2495195017333"></a><a name="p2495195017333"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p784206117333"><a name="p784206117333"></a><a name="p784206117333"></a>Request error. For details, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row3122722917333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4637763817333"><a name="p4637763817333"></a><a name="p4637763817333"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p6560116717333"><a name="p6560116717333"></a><a name="p6560116717333"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row5353959117333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4173958717333"><a name="p4173958717333"></a><a name="p4173958717333"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2546341217333"><a name="p2546341217333"></a><a name="p2546341217333"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row5197513192250"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p21898657192252"><a name="p21898657192252"></a><a name="p21898657192252"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p28960832192252"><a name="p28960832192252"></a><a name="p28960832192252"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row2784412417333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4078159117333"><a name="p4078159117333"></a><a name="p4078159117333"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1497458717333"><a name="p1497458717333"></a><a name="p1497458717333"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row55355517333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4483799017333"><a name="p4483799017333"></a><a name="p4483799017333"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p799858217333"><a name="p799858217333"></a><a name="p799858217333"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


