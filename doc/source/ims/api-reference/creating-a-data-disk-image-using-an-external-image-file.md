# Creating a Data Disk Image Using an External Image File<a name="EN-US_TOPIC_0083905788"></a>

## Function<a name="section29995926"></a>

This API is used to create a data disk image from a data disk image file uploaded to the OBS bucket. The API is an asynchronous one. If it is successfully called, the cloud service system receives the request. However, you need to use the asynchronous job query API to query the image creation status. For details, see  [Asynchronous Job Query](asynchronous-job-query.md).

## Constraints<a name="section13509102512278"></a>

-   The OS type of the data disk image must be defined, and it can either Windows or Linux.
-   The data disk has about 40 GB to 2048 GB of storage space.
-   When uploading the external image file, you must select an OBS bucket with standard storage.

## URI<a name="section1527883"></a>

POST /v1/cloudimages/dataimages/action

## Request<a name="section13750947"></a>

-   Request parameters

    <a name="table62551043151553"></a>
    <table><thead align="left"><tr id="row63356413151553"><th class="cellrowborder" valign="top" width="18.42%" id="mcps1.1.5.1.1"><p id="p41292683151745"><a name="p41292683151745"></a><a name="p41292683151745"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.1.5.1.2"><p id="p51323166151745"><a name="p51323166151745"></a><a name="p51323166151745"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85%" id="mcps1.1.5.1.3"><p id="p36943663151745"><a name="p36943663151745"></a><a name="p36943663151745"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.5%" id="mcps1.1.5.1.4"><p id="p16401653151745"><a name="p16401653151745"></a><a name="p16401653151745"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58293752151553"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.1 "><p id="p24173439151553"><a name="p24173439151553"></a><a name="p24173439151553"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p11891563151553"><a name="p11891563151553"></a><a name="p11891563151553"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.3 "><p id="p23692580151553"><a name="p23692580151553"></a><a name="p23692580151553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.5%" headers="mcps1.1.5.1.4 "><p id="p40050833151553"><a name="p40050833151553"></a><a name="p40050833151553"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row57744127151553"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.1 "><p id="p46762671151553"><a name="p46762671151553"></a><a name="p46762671151553"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p29679979151553"><a name="p29679979151553"></a><a name="p29679979151553"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.3 "><p id="p55268124151553"><a name="p55268124151553"></a><a name="p55268124151553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.5%" headers="mcps1.1.5.1.4 "><p id="p47533098151553"><a name="p47533098151553"></a><a name="p47533098151553"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>. The value contains a maximum of 1024 characters and consists of only letters and digits. Carriage returns and angle brackets (&lt; &gt;) are not allowed. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row25144703151553"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.1 "><p id="p26913998111642"><a name="p26913998111642"></a><a name="p26913998111642"></a>os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p32550218111642"><a name="p32550218111642"></a><a name="p32550218111642"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.3 "><p id="p19321962111642"><a name="p19321962111642"></a><a name="p19321962111642"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.5%" headers="mcps1.1.5.1.4 "><p id="p21575062111642"><a name="p21575062111642"></a><a name="p21575062111642"></a>Specifies the OS type.</p>
    <p id="p59957837111642"><a name="p59957837111642"></a><a name="p59957837111642"></a>It can only be Windows or Linux.</p>
    </td>
    </tr>
    <tr id="row30504483181035"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.1 "><p id="p3325055511177"><a name="p3325055511177"></a><a name="p3325055511177"></a>image_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p894042511177"><a name="p894042511177"></a><a name="p894042511177"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.3 "><p id="p5308582811177"><a name="p5308582811177"></a><a name="p5308582811177"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.5%" headers="mcps1.1.5.1.4 "><p id="p498478711177"><a name="p498478711177"></a><a name="p498478711177"></a>Specifies the URL of the external image file in the OBS bucket.</p>
    <p id="p1003131911177"><a name="p1003131911177"></a><a name="p1003131911177"></a>The format is <em id="i84235269710218"><a name="i84235269710218"></a><a name="i84235269710218"></a>OBS bucket name</em>:<em id="i84235269710226"><a name="i84235269710226"></a><a name="i84235269710226"></a>Image file name</em>.</p>
    <div class="notice" id="note24311794102659"><a name="note24311794102659"></a><a name="note24311794102659"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p17479562102659"><a name="p17479562102659"></a><a name="p17479562102659"></a>The storage class of the OBS bucket must be <strong id="b84235270695937"><a name="b84235270695937"></a><a name="b84235270695937"></a>Standard</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row52404160111723"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.1 "><p id="p55358975111759"><a name="p55358975111759"></a><a name="p55358975111759"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p54892022111759"><a name="p54892022111759"></a><a name="p54892022111759"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.3 "><p id="p17068760111759"><a name="p17068760111759"></a><a name="p17068760111759"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.5%" headers="mcps1.1.5.1.4 "><p id="p40392335111759"><a name="p40392335111759"></a><a name="p40392335111759"></a>Specifies the minimum size of the data disk.</p>
    <p id="p27986702111759"><a name="p27986702111759"></a><a name="p27986702111759"></a>Value range: 40 GB to 2048 GB</p>
    </td>
    </tr>
    <tr id="row39879232111737"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.1 "><p id="p10803010111759"><a name="p10803010111759"></a><a name="p10803010111759"></a>cmk_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p2628645111759"><a name="p2628645111759"></a><a name="p2628645111759"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.3 "><p id="p11593672111759"><a name="p11593672111759"></a><a name="p11593672111759"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.5%" headers="mcps1.1.5.1.4 "><p id="p66672211111759"><a name="p66672211111759"></a><a name="p66672211111759"></a>Specifies the master key used for encrypting an image. For its value, see the <em id="i842352697163941"><a name="i842352697163941"></a><a name="i842352697163941"></a>Key Management Service User Guide</em>.</p>
    </td>
    </tr>
    <tr id="row44108176111744"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.1 "><p id="p17224683111759"><a name="p17224683111759"></a><a name="p17224683111759"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p53022050111759"><a name="p53022050111759"></a><a name="p53022050111759"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.3 "><p id="p66927678111759"><a name="p66927678111759"></a><a name="p66927678111759"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.5%" headers="mcps1.1.5.1.4 "><p id="p55071526615"><a name="p55071526615"></a><a name="p55071526615"></a>Specifies image tags. This parameter is left blank by default.</p>
    <p id="p52432871111759"><a name="p52432871111759"></a><a name="p52432871111759"></a>For detailed parameter description, see <a href="image-tag-data-formats.md">Image Tag Data Formats</a>.</p>
    <p id="p20992085173243"><a name="p20992085173243"></a><a name="p20992085173243"></a>Use either <strong id="b84235270693042"><a name="b84235270693042"></a><a name="b84235270693042"></a>tags</strong> or <strong id="b84235270693044"><a name="b84235270693044"></a><a name="b84235270693044"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row2323281018425"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.1 "><p id="p4480124311356"><a name="p4480124311356"></a><a name="p4480124311356"></a>image_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.1.5.1.2 "><p id="p3825882611356"><a name="p3825882611356"></a><a name="p3825882611356"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.1.5.1.3 "><p id="p4539910111356"><a name="p4539910111356"></a><a name="p4539910111356"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.5%" headers="mcps1.1.5.1.4 "><p id="p62821058568"><a name="p62821058568"></a><a name="p62821058568"></a>Lists the image tags. This parameter is left blank by default.</p>
    <p id="p6735471074"><a name="p6735471074"></a><a name="p6735471074"></a>For detailed parameter descriptions, see <a href="image-tag-data-formats.md">Image Tag Data Formats</a>.</p>
    <p id="p1407230811356"><a name="p1407230811356"></a><a name="p1407230811356"></a>Use either <strong id="b483541052"><a name="b483541052"></a><a name="b483541052"></a>tags</strong> or <strong id="b1919627999"><a name="b1919627999"></a><a name="b1919627999"></a>image_tags</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example requests
    -   Request for creating an image \(**tags**\)

        ```
        POST https://{Endpoint}/v1/cloudimages/dataimages/action
        ```

        ```
        {
          "name": "fedora-data1",
          "image_url": "image-test:fedora_data1.qcow2",
          "description":"Data disk 1 of Fedora",
          "min_disk": 40,
          "tags": [
            "aaa.111",
            "bbb.222"
          ],
          "os_type": "Linux"
        }
        ```

    -   Request for creating an image \(**image\_tags**\)

        ```
        POST https://{Endpoint}/v1/cloudimages/dataimages/action
        ```

        ```
        {
          "name": "fedora-data2",
          "image_url": "image-test:fedora_data1.qcow2",
          "description":"Data disk 2 of Fedora",
          "min_disk": 40,
          "image_tags": [{"key":"aaa","value":"111"},{"key":"bbb","value":"222"}],
          "os_type": "Linux"
        }
        ```



## Response<a name="section56649665"></a>

-   Response parameters

    <a name="table1337332211159"></a>
    <table><thead align="left"><tr id="row1133156911159"><th class="cellrowborder" valign="top" width="23.84%" id="mcps1.1.4.1.1"><p id="p4544189211159"><a name="p4544189211159"></a><a name="p4544189211159"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.97%" id="mcps1.1.4.1.2"><p id="p556206921988"><a name="p556206921988"></a><a name="p556206921988"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.19%" id="mcps1.1.4.1.3"><p id="p5691464411159"><a name="p5691464411159"></a><a name="p5691464411159"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4668343211159"><td class="cellrowborder" valign="top" width="23.84%" headers="mcps1.1.4.1.1 "><p id="p2326164111159"><a name="p2326164111159"></a><a name="p2326164111159"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.1.4.1.2 "><p id="p89821791988"><a name="p89821791988"></a><a name="p89821791988"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.19%" headers="mcps1.1.4.1.3 "><p id="p514473411159"><a name="p514473411159"></a><a name="p514473411159"></a>Specifies the asynchronous task ID.</p>
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
        "job_id": "4010a32b5f909853015f90aaa24b0015"
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
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p784206117333"><a name="p784206117333"></a><a name="p784206117333"></a>Request error. For details about the returned error code, see <a href="error-codes.md">Error Codes</a>.</p>
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


