# Deleting a Job Object<a name="EN-US_TOPIC_0172486164"></a>

## Function<a name="section4408504619327"></a>

This API is used to delete a job object. This API is compatible with Sahara.

## URI<a name="section10186656193217"></a>

-   Format

    DELETE /v1.1/\{project\_id\}/jobs/\{job\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16571835194812"><a name="p16571835194812"></a><a name="p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p141410194812"><a name="p141410194812"></a><a name="p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11454278194812"><a name="p11454278194812"></a><a name="p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12931900144556"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p40851019144556"><a name="p40851019144556"></a><a name="p40851019144556"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p20598275144556"><a name="p20598275144556"></a><a name="p20598275144556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p57847563144556"><a name="p57847563144556"></a><a name="p57847563144556"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row693784194754"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p56196540194754"><a name="p56196540194754"></a><a name="p56196540194754"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p56703698153439"><a name="p56703698153439"></a><a name="p56703698153439"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p29596849153439"><a name="p29596849153439"></a><a name="p29596849153439"></a>Job object ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11749164442314"></a>

**Request parameters**

None.

## Response<a name="section1575113448238"></a>

**Response parameters**

None.

## Example<a name="section1210015461189"></a>

-   Example request

    None.

-   Example response

    None.


## Status Code<a name="section4391766619434"></a>

[Table 2](#table1584477916050)  describes the status code of this API.

**Table  2**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job object has been successfully deleted.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

