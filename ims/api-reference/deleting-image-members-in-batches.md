# Deleting Image Members in Batches<a name="EN-US_TOPIC_0036994324"></a>

## Function<a name="section11046056154747"></a>

This API is an extension one and used to stop sharing images by deleting tenants with whom the image is shared in batches.

This API is an asynchronous one. If  **job\_id**  is returned, the task is successfully delivered. You need to query the status of the asynchronous task. If the status is  **success**, the task is successfully executed. If the status is  **failed**, the task fails. For details about how to query the status of an asynchronous task, see  [Asynchronous Job Query](asynchronous-job-query.md).

## URI<a name="section66620681154747"></a>

DELETE /v1/cloudimages/members

## Request<a name="section29704853154747"></a>

-   Request parameters

    <a name="table57282886154747"></a>
    <table><thead align="left"><tr id="row33194661154747"><th class="cellrowborder" valign="top" width="20.01200120012001%" id="mcps1.1.5.1.1"><p id="p4413036154747"><a name="p4413036154747"></a><a name="p4413036154747"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.69216921692169%" id="mcps1.1.5.1.2"><p id="p15244109154747"><a name="p15244109154747"></a><a name="p15244109154747"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.761776177617765%" id="mcps1.1.5.1.3"><p id="p4364817210345"><a name="p4364817210345"></a><a name="p4364817210345"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.53405340534053%" id="mcps1.1.5.1.4"><p id="p26813302154747"><a name="p26813302154747"></a><a name="p26813302154747"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24393852154747"><td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.1 "><p id="p29744966154747"><a name="p29744966154747"></a><a name="p29744966154747"></a>images</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69216921692169%" headers="mcps1.1.5.1.2 "><p id="p384719154747"><a name="p384719154747"></a><a name="p384719154747"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.761776177617765%" headers="mcps1.1.5.1.3 "><p id="p2213925010345"><a name="p2213925010345"></a><a name="p2213925010345"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.1.5.1.4 "><p id="p129047121673"><a name="p129047121673"></a><a name="p129047121673"></a>Specifies the image IDs.</p>
    </td>
    </tr>
    <tr id="row2933734592853"><td class="cellrowborder" valign="top" width="20.01200120012001%" headers="mcps1.1.5.1.1 "><p id="p6350774992915"><a name="p6350774992915"></a><a name="p6350774992915"></a>projects</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69216921692169%" headers="mcps1.1.5.1.2 "><p id="p4385401492915"><a name="p4385401492915"></a><a name="p4385401492915"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.761776177617765%" headers="mcps1.1.5.1.3 "><p id="p6251420792915"><a name="p6251420792915"></a><a name="p6251420792915"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.53405340534053%" headers="mcps1.1.5.1.4 "><p id="p3048600192915"><a name="p3048600192915"></a><a name="p3048600192915"></a>Specifies the project IDs.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    DELETE https://{Endpoint}/v1/cloudimages/members
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


## Response<a name="section42338041154747"></a>

-   Response parameters

    <a name="table1858875391115"></a>
    <table><thead align="left"><tr id="row5097995091115"><th class="cellrowborder" valign="top" width="30.486951304869514%" id="mcps1.1.4.1.1"><p id="p3573529991115"><a name="p3573529991115"></a><a name="p3573529991115"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.078292170782923%" id="mcps1.1.4.1.2"><p id="p4803685091115"><a name="p4803685091115"></a><a name="p4803685091115"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.1.4.1.3"><p id="p6577961291115"><a name="p6577961291115"></a><a name="p6577961291115"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2654833891115"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p293180691115"><a name="p293180691115"></a><a name="p293180691115"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p4244468991115"><a name="p4244468991115"></a><a name="p4244468991115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p1546781891115"><a name="p1546781891115"></a><a name="p1546781891115"></a>Specifies the asynchronous task ID.</p>
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
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1497458717333"><a name="p1497458717333"></a><a name="p1497458717333"></a>Internal service error</p>
    </td>
    </tr>
    <tr id="row55355517333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4483799017333"><a name="p4483799017333"></a><a name="p4483799017333"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p799858217333"><a name="p799858217333"></a><a name="p799858217333"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


