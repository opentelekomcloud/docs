# Deleting Jobs in Batches<a name="EN-US_TOPIC_0183401341"></a>

## Function<a name="section4408504619327"></a>

This API is used to delete APIs in batches.

## URI<a name="section10186656193217"></a>

-   Format

    POST /v2/\{project\_id\}/clusters/\{cluster\_id\}/job-executions/batch-delete

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="en-us_topic_0176713997_row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0176713997_p16571835194812"><a name="en-us_topic_0176713997_p16571835194812"></a><a name="en-us_topic_0176713997_p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0176713997_p141410194812"><a name="en-us_topic_0176713997_p141410194812"></a><a name="en-us_topic_0176713997_p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0176713997_p11454278194812"><a name="en-us_topic_0176713997_p11454278194812"></a><a name="en-us_topic_0176713997_p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0176713997_row39786771142917"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176713997_p1503055142917"><a name="en-us_topic_0176713997_p1503055142917"></a><a name="en-us_topic_0176713997_p1503055142917"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176713997_p54638598142917"><a name="en-us_topic_0176713997_p54638598142917"></a><a name="en-us_topic_0176713997_p54638598142917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176713997_p63650338142917"><a name="en-us_topic_0176713997_p63650338142917"></a><a name="en-us_topic_0176713997_p63650338142917"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0176713997_row3457216201210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0176713997_p194589160122"><a name="en-us_topic_0176713997_p194589160122"></a><a name="en-us_topic_0176713997_p194589160122"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0176713997_p045813165125"><a name="en-us_topic_0176713997_p045813165125"></a><a name="en-us_topic_0176713997_p045813165125"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0176713997_p1845891641218"><a name="en-us_topic_0176713997_p1845891641218"></a><a name="en-us_topic_0176713997_p1845891641218"></a>Cluster ID. For details on how to obtain the cluster ID, see <a href="obtain-mrs-cluster-information.md#section177891315153619">Obtaining a Cluster ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section673761354213"></a>

**Table  2**  Request parameter description

<a name="table46210785193317"></a>
<table><thead align="left"><tr id="row34262165193317"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p12621391193317"><a name="p12621391193317"></a><a name="p12621391193317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p15699711193317"><a name="p15699711193317"></a><a name="p15699711193317"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p562413019313"><a name="p562413019313"></a><a name="p562413019313"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p63717051193317"><a name="p63717051193317"></a><a name="p63717051193317"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36582554193317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2182648173014"><a name="p2182648173014"></a><a name="p2182648173014"></a>job_id_list</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2181448193015"><a name="p2181448193015"></a><a name="p2181448193015"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3180194813304"><a name="p3180194813304"></a><a name="p3180194813304"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p151790482306"><a name="p151790482306"></a><a name="p151790482306"></a>List of job IDs. For details on how to obtain the list of job IDs, see <a href="obtain-mrs-cluster-information.md#section247234143612">Obtaining a Job ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section775516131425"></a>

**Response parameters**

None

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    {
    	"job_id_list": ["c23c1f53-5c8e-4eb8-ab2f-a6acff8ac369", "8f7969b6-d2fb-4442-9533-3fe7d7bdf31b"]
    }
    ```

-   Example response
    -   Example of a successful response

        None

    -   Example of a failed response

        ```
        {
        "error_msg": "Failed to delete jobs in batches.",
        "error_code":"0161"
        }
        ```



## Status Code<a name="section4391766619434"></a>

For details about status codes, see  [Status Codes](status-codes.md).

