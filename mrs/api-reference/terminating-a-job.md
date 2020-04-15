# Terminating a Job<a name="EN-US_TOPIC_0177065250"></a>

## Function<a name="section4408504619327"></a>

This API is used to terminate a specified job in an MRS cluster.

## URI<a name="section10186656193217"></a>

-   Format

    POST /v2/\{project\_id\}/clusters/\{cluster\_id\}/job-executions/\{job\_execution\_id\}/kill

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="en-us_topic_0176790808_row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0176790808_p16571835194812"><a name="en-us_topic_0176790808_p16571835194812"></a><a name="en-us_topic_0176790808_p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0176790808_p141410194812"><a name="en-us_topic_0176790808_p141410194812"></a><a name="en-us_topic_0176790808_p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0176790808_p11454278194812"><a name="en-us_topic_0176790808_p11454278194812"></a><a name="en-us_topic_0176790808_p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0176790808_row39786771142917"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p1503055142917"><a name="en-us_topic_0176790808_p1503055142917"></a><a name="en-us_topic_0176790808_p1503055142917"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p54638598142917"><a name="en-us_topic_0176790808_p54638598142917"></a><a name="en-us_topic_0176790808_p54638598142917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p63650338142917"><a name="en-us_topic_0176790808_p63650338142917"></a><a name="en-us_topic_0176790808_p63650338142917"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0176790808_row3457216201210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p194589160122"><a name="en-us_topic_0176790808_p194589160122"></a><a name="en-us_topic_0176790808_p194589160122"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p045813165125"><a name="en-us_topic_0176790808_p045813165125"></a><a name="en-us_topic_0176790808_p045813165125"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p1845891641218"><a name="en-us_topic_0176790808_p1845891641218"></a><a name="en-us_topic_0176790808_p1845891641218"></a>Cluster ID. For details on how to obtain the cluster ID, see <a href="obtain-mrs-cluster-information.md#section177891315153619">Obtaining a Cluster ID</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0176790808_row121835121146"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176790808_p218419125412"><a name="en-us_topic_0176790808_p218419125412"></a><a name="en-us_topic_0176790808_p218419125412"></a>job_execution_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176790808_p16184161212420"><a name="en-us_topic_0176790808_p16184161212420"></a><a name="en-us_topic_0176790808_p16184161212420"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176790808_p121844121440"><a name="en-us_topic_0176790808_p121844121440"></a><a name="en-us_topic_0176790808_p121844121440"></a>Job ID. For details on how to obtain the job ID, see <a href="obtain-mrs-cluster-information.md#section247234143612">Obtaining a Job ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section673761354213"></a>

**Request parameters**

None

## Response<a name="section775516131425"></a>

**Response parameters**

None

## Example<a name="section1210015461189"></a>

-   Example request

    None

-   Example response
    -   Example of a successful response

        None

    -   Example of a failed response

        ```
        {
        "error_msg": "Failed to terminate the job."
        "error_code":"0175"
        }
        ```



## Status Code<a name="section4391766619434"></a>

[Table 2](#table1584477916050)  describes status codes.

**Table  2**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job termination request has been accepted. Please wait.</p>
</td>
</tr>
</tbody>
</table>

For details about status codes, see  [Status Codes](status-codes.md).

