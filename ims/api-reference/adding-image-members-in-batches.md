# Adding Image Members in Batches<a name="EN-US_TOPIC_0036994322"></a>

## Function<a name="section66302617144828"></a>

This API is an extension one and used to share more than one image with multiple tenants.

This API is an asynchronous one. If  **job\_id**  is returned, the task is successfully delivered. You need to query the status of the asynchronous task. If the status is  **success**, the task is successfully executed. If the status is  **failed**, the task fails. For details about how to query the status of an asynchronous task, see  [Asynchronous Job Query](asynchronous-job-query.md).

## URI<a name="section16226363144828"></a>

POST /v1/cloudimages/members

## Request<a name="section22707920144828"></a>

-   Request parameters

    <a name="table53011268153646"></a>
    <table><thead align="left"><tr id="row8255548153646"><th class="cellrowborder" valign="top" width="28.9%" id="mcps1.1.4.1.1"><p id="p64719651153646"><a name="p64719651153646"></a><a name="p64719651153646"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.89%" id="mcps1.1.4.1.2"><p id="p27850258153646"><a name="p27850258153646"></a><a name="p27850258153646"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.21%" id="mcps1.1.4.1.3"><p id="p41278443153646"><a name="p41278443153646"></a><a name="p41278443153646"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55219556153646"><td class="cellrowborder" valign="top" width="28.9%" headers="mcps1.1.4.1.1 "><p id="p45852693181844"><a name="p45852693181844"></a><a name="p45852693181844"></a>images</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.89%" headers="mcps1.1.4.1.2 "><p id="p57596693181844"><a name="p57596693181844"></a><a name="p57596693181844"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.1.4.1.3 "><p id="p34820580181844"><a name="p34820580181844"></a><a name="p34820580181844"></a>Specifies the image IDs.</p>
    </td>
    </tr>
    <tr id="row6698413181831"><td class="cellrowborder" valign="top" width="28.9%" headers="mcps1.1.4.1.1 "><p id="p17052548181844"><a name="p17052548181844"></a><a name="p17052548181844"></a>projects</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.89%" headers="mcps1.1.4.1.2 "><p id="p11293510181844"><a name="p11293510181844"></a><a name="p11293510181844"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.21%" headers="mcps1.1.4.1.3 "><p id="p42359132181844"><a name="p42359132181844"></a><a name="p42359132181844"></a>Specifies the project IDs.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v1/cloudimages/members
    ```

    ```
    {
        "images": [
            "d164b5df-1bc3-4c3f-893e-3e471fd16e64",
            "0b680482-acaa-4045-b14c-9a8c7dfe9c70"
        ],
        "projects": [
            "9c61004714024f9586705d090530f9fa",
            "edc89b490d7d4392898e19b2deb34797"
        ]
    }
    ```


## Response<a name="section37386190144828"></a>

-   Response parameters

    <a name="table65680948153746"></a>
    <table><thead align="left"><tr id="row59664825153746"><th class="cellrowborder" valign="top" width="36.36636336366364%" id="mcps1.1.4.1.1"><p id="p1012670153746"><a name="p1012670153746"></a><a name="p1012670153746"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.58834116588341%" id="mcps1.1.4.1.2"><p id="p352397153746"><a name="p352397153746"></a><a name="p352397153746"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.045295470452956%" id="mcps1.1.4.1.3"><p id="p28544167153746"><a name="p28544167153746"></a><a name="p28544167153746"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30376173153746"><td class="cellrowborder" valign="top" width="36.36636336366364%" headers="mcps1.1.4.1.1 "><p id="p3318816181939"><a name="p3318816181939"></a><a name="p3318816181939"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.58834116588341%" headers="mcps1.1.4.1.2 "><p id="p31480262181939"><a name="p31480262181939"></a><a name="p31480262181939"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.045295470452956%" headers="mcps1.1.4.1.3 "><p id="p66873325181939"><a name="p66873325181939"></a><a name="p66873325181939"></a>Specifies the asynchronous task ID.</p>
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


