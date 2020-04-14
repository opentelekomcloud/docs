# Adding a Checkpoint<a name="dis_02_0403"></a>

## Function<a name="section56390275192627"></a>

This API is used to add a checkpoint.

-   When an application consumes data, the latest SN of the consumed data is recorded as a checkpoint. When the data is reconsumed, the consumption can be continued based on this checkpoint.
-   An application and checkpoint are used together. When adding a checkpoint, you need to specify the stream name, partition ID, and application name.

## URI<a name="section37885970192627"></a>

-   URI format

    POST /v2/\{project\_id\}/checkpoints

-   Parameter description

    None


## Request<a name="section315688192627"></a>

-   Example request

    ```
    POST https://{endpoint}/v2/{project_id}/checkpoints
    
    {
     "stream_name": "stream_name_test1",
      "app_name": "app_name1",
      "partition_id": "shardId-0000000000",
      "sequence_number": "10",
      "metadata": "metadata",
      "checkpoint_type": "LAST_READ"
    }
    ```

-   Parameter description

    **Table  1**  Parameter description

    <a name="table11826479192627"></a>
    <table><thead align="left"><tr id="row21460173192627"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p60552482192627"><a name="p60552482192627"></a><a name="p60552482192627"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p5804032192627"><a name="p5804032192627"></a><a name="p5804032192627"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p364558192627"><a name="p364558192627"></a><a name="p364558192627"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p29529204192627"><a name="p29529204192627"></a><a name="p29529204192627"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43055323192627"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p64929130192627"><a name="p64929130192627"></a><a name="p64929130192627"></a>stream_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p24768202192627"><a name="p24768202192627"></a><a name="p24768202192627"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p60067363192627"><a name="p60067363192627"></a><a name="p60067363192627"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p33618204192627"><a name="p33618204192627"></a><a name="p33618204192627"></a>Name of the DIS stream whose data record will have a checkpoint.</p>
    <p id="p34128380192627"><a name="p34128380192627"></a><a name="p34128380192627"></a>A stream name is 1 to 64 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="row38719965192627"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p49309455192627"><a name="p49309455192627"></a><a name="p49309455192627"></a>app_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p34642905192627"><a name="p34642905192627"></a><a name="p34642905192627"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p54611940192627"><a name="p54611940192627"></a><a name="p54611940192627"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p61491032192627"><a name="p61491032192627"></a><a name="p61491032192627"></a>Unique name of the consumer application that will read data from the chosen DIS stream.</p>
    <p id="p960834795334"><a name="p960834795334"></a><a name="p960834795334"></a>An application name must contain 1 to 50 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="row16548376192627"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p65350075192627"><a name="p65350075192627"></a><a name="p65350075192627"></a>partition_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p58864731192627"><a name="p58864731192627"></a><a name="p58864731192627"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p3313887192627"><a name="p3313887192627"></a><a name="p3313887192627"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p67098288192627"><a name="p67098288192627"></a><a name="p67098288192627"></a>Unique identifier of the partition.</p>
    </td>
    </tr>
    <tr id="row67013680192627"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p59399006192627"><a name="p59399006192627"></a><a name="p59399006192627"></a>sequence_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p46590221192627"><a name="p46590221192627"></a><a name="p46590221192627"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p15711589192627"><a name="p15711589192627"></a><a name="p15711589192627"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p64679181192627"><a name="p64679181192627"></a><a name="p64679181192627"></a>Sequence number used to record the consumption checkpoint of the stream.</p>
    </td>
    </tr>
    <tr id="row45241718192627"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p40700570192627"><a name="p40700570192627"></a><a name="p40700570192627"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p8411874192627"><a name="p8411874192627"></a><a name="p8411874192627"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p10273207192627"><a name="p10273207192627"></a><a name="p10273207192627"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p26823424192627"><a name="p26823424192627"></a><a name="p26823424192627"></a>Metadata of the consumer application.</p>
    <p id="p2017818095754"><a name="p2017818095754"></a><a name="p2017818095754"></a>The maximum metadata length is 1000 characters.</p>
    </td>
    </tr>
    <tr id="row40084228192627"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p25597015192627"><a name="p25597015192627"></a><a name="p25597015192627"></a>checkpoint_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p60092306192627"><a name="p60092306192627"></a><a name="p60092306192627"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p35638622192627"><a name="p35638622192627"></a><a name="p35638622192627"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p1047266192627"><a name="p1047266192627"></a><a name="p1047266192627"></a>Type of the checkpoint.</p>
    <p id="p9425401192627"><a name="p9425401192627"></a><a name="p9425401192627"></a>The checkpoint type <strong id="b30197392141926"><a name="b30197392141926"></a><a name="b30197392141926"></a>LAST_READ</strong> indicates that only sequence numbers are recorded into the database.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="section66209678192039"></a>

-   If the DIS stream was successfully created, a 201 response with an empty response body is returned.
-   If the DIS stream failed to be created, identify the failure cause according to the response body and the instructions in  [Error Codes](error-codes.md).

## Status Code<a name="section54218581192039"></a>

-   Normal

    201 Created

-   Failed

    For more information, see  [Error Codes](error-codes.md).


