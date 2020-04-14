# Creating an Application<a name="dis_02_0401"></a>

## Function<a name="section27008210192039"></a>

This API is used to create an application.

-   Application: Multiple applications can access data in the same stream. Checkpoints generated for each application are used to record the consumed data in the stream by each application.
-   An application and checkpoint are used together. When adding a checkpoint, you need to specify an application name. For details about how to add a checkpoint, see  [Adding a Checkpoint](adding-a-checkpoint.md).

    Checkpoint: When an application consumes data, the latest SN of the consumed data is recorded as a checkpoint. When the data is reconsumed, the consumption can be continued based on this checkpoint.


## URL<a name="section26088326192039"></a>

-   URI format

    POST /v2/\{project\_id\}/apps

-   Parameter description

    None


## Request<a name="section53416356192039"></a>

-   Example request

    ```
    POST https://{endpoint}/v2/{project_id}/apps
    
    {
      "app_name": "app_test"
    }
    ```

-   Parameter description

    **Table  1**  Parameter description

    <a name="table26527159192039"></a>
    <table><thead align="left"><tr id="row40395442192039"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p50805401192039"><a name="p50805401192039"></a><a name="p50805401192039"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p21596779192039"><a name="p21596779192039"></a><a name="p21596779192039"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p4508690192039"><a name="p4508690192039"></a><a name="p4508690192039"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p29659638192039"><a name="p29659638192039"></a><a name="p29659638192039"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53620478192039"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p48291475192039"><a name="p48291475192039"></a><a name="p48291475192039"></a>app_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p19295388192039"><a name="p19295388192039"></a><a name="p19295388192039"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p19422594192039"><a name="p19422594192039"></a><a name="p19422594192039"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p29726252192039"><a name="p29726252192039"></a><a name="p29726252192039"></a>Unique name of the consumer application to be created.</p>
    <p id="p98686589521"><a name="p98686589521"></a><a name="p98686589521"></a>An application name is 1 to 200 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
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


