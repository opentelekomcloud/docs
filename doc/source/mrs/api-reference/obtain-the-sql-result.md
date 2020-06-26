# Obtain the SQL Result<a name="EN-US_TOPIC_0183401342"></a>

## Function<a name="section4408504619327"></a>

This API is used to obtain results returned after the SQL statements for querying SparkSQL and SparkScript jobs in an MRS cluster are executed.

## URI<a name="section10186656193217"></a>

-   Format

    GET /v2/\{project\_id\}/clusters/\{cluster\_id\}/job-executions/\{job\_execution\_id\}/sql-result

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

**Table  2**  Response parameter description

<a name="table12040613193927"></a>
<table><thead align="left"><tr id="en-us_topic_0177065250_row8843854193927"><th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.1"><p id="en-us_topic_0177065250_p45263556193927"><a name="en-us_topic_0177065250_p45263556193927"></a><a name="en-us_topic_0177065250_p45263556193927"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.94%" id="mcps1.2.4.1.2"><p id="en-us_topic_0177065250_p1907984993927"><a name="en-us_topic_0177065250_p1907984993927"></a><a name="en-us_topic_0177065250_p1907984993927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0177065250_p17473879193927"><a name="en-us_topic_0177065250_p17473879193927"></a><a name="en-us_topic_0177065250_p17473879193927"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0177065250_row8387056194027"><td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.1 "><p id="p199501699424"><a name="p199501699424"></a><a name="p199501699424"></a>sql-results</p>
</td>
<td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.2.4.1.2 "><p id="p1949129154215"><a name="p1949129154215"></a><a name="p1949129154215"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p99471893420"><a name="p99471893420"></a><a name="p99471893420"></a>SQL statement query result.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    {
    	"job_name": "111",
    	"job_type": "SparkSql",
    	"arguments": [
                 "create table src_wordcount (id int,name string);
                  show tables;
                  insert INTO src_wordcount VALUES (1, 'a');
                  insert INTO src_wordcount VALUES (2, 'b');SELECT * FROM src_wordcount;"
                      ],
    	"properties": {}
    }
    ```

-   Example response
    -   Example of a successful response

        ```
        {
        	"sql_results": {
        		"0": [{
        			"result": "succeed"
        		}],
        		"1": [{
        			"database": "default",
        			"isTemporary": "false",
        			"tableName": "src_wordcount"
        		}],
        		"2": [{
        			"result": "succeed"
        		}],
        		"3": [{
        			"result": "succeed"
        		}],
        		"4": [{
        			"name": "a",
        			"id": "1"
        		}, {
        			"name": "b",
        			"id": "2"
        		}]
        	}
        }
        ```

    -   Example of a failed response

        ```
        {
        "error_msg": "Failed to collect SQL job results."
        "error_code":"0172"
        }
        ```



## Status Code<a name="section4391766619434"></a>

For details about status codes, see  [Status Codes](status-codes.md).

