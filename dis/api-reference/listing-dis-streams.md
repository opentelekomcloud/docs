# Listing DIS Streams<a name="dis_02_0024"></a>

## Function<a name="section725717310134"></a>

This API is used to query all streams created by the current tenant.

During query, you need to specify the stream from which the stream list is returned and the maximum number of streams returned in a single request.

## URI<a name="section5598831810134"></a>

-   URI format

    GET /v2/\{project\_id\}/streams

-   Parameter description

    None


## Request<a name="section5438760810134"></a>

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/streams?limit=10&start_stream_name=test_stream 
    ```

-   Parameter description

    **Table  1**  Parameter description

    <a name="table1737490910134"></a>
    <table><thead align="left"><tr id="row1021513210134"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p2211937910134"><a name="p2211937910134"></a><a name="p2211937910134"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p4683930310134"><a name="p4683930310134"></a><a name="p4683930310134"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p3588719910134"><a name="p3588719910134"></a><a name="p3588719910134"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p2118202010134"><a name="p2118202010134"></a><a name="p2118202010134"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3802204510134"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p5988680310134"><a name="p5988680310134"></a><a name="p5988680310134"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p1899284510134"><a name="p1899284510134"></a><a name="p1899284510134"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p6202545910134"><a name="p6202545910134"></a><a name="p6202545910134"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p5508123911310"><a name="p5508123911310"></a><a name="p5508123911310"></a>The maximum number of DIS streams to list in a single API call.</p>
    <p id="p3493446010514"><a name="p3493446010514"></a><a name="p3493446010514"></a>Value range: 1 to 100</p>
    <p id="p5800631910134"><a name="p5800631910134"></a><a name="p5800631910134"></a>Default value: 10</p>
    </td>
    </tr>
    <tr id="row5229482310134"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p802230010134"><a name="p802230010134"></a><a name="p802230010134"></a>start_stream_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p4582658610134"><a name="p4582658610134"></a><a name="p4582658610134"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p2096596010134"><a name="p2096596010134"></a><a name="p2096596010134"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p2052116610134"><a name="p2052116610134"></a><a name="p2052116610134"></a>Name of the DIS stream to start the list with. The returned stream list does not contain this DIS stream name.</p>
    <p id="p162141712132713"><a name="p162141712132713"></a><a name="p162141712132713"></a>If pagination query is required, this parameter is not transferred when you query data on the first page. If the value of <strong id="b16317187449"><a name="b16317187449"></a><a name="b16317187449"></a>has_more_streams</strong> is <strong id="b206511011940"><a name="b206511011940"></a><a name="b206511011940"></a>true</strong>, go to the next page,</p>
    <p id="p9210111212277"><a name="p9210111212277"></a><a name="p9210111212277"></a><strong id="b63441236121618"><a name="b63441236121618"></a><a name="b63441236121618"></a>start_stream_name</strong> is set to the name of the last stream in the query result on the first page.</p>
    <div class="note" id="note350514352913"><a name="note350514352913"></a><a name="note350514352913"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p205051743102914"><a name="p205051743102914"></a><a name="p205051743102914"></a>Streams in the stream list are arranged in alphabetical order.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="section5047277010134"></a>

-   Example response

    ```
    {
      "total_number": 1,
      "has_more_streams": false,
      "stream_names": [
        "stream_test"
      ]
    }
    ```

-   Parameter description

    **Table  2**  Response parameter description

    <a name="table1022333410134"></a>
    <table><thead align="left"><tr id="row2248734710134"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.1"><p id="p953583810134"><a name="p953583810134"></a><a name="p953583810134"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p3420542610134"><a name="p3420542610134"></a><a name="p3420542610134"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.2.4.1.3"><p id="p1917608510134"><a name="p1917608510134"></a><a name="p1917608510134"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row975909010134"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p5228881510134"><a name="p5228881510134"></a><a name="p5228881510134"></a>total_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p753560410134"><a name="p753560410134"></a><a name="p753560410134"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p640420210134"><a name="p640420210134"></a><a name="p640420210134"></a>Total number of DIS streams created by the current tenant.</p>
    </td>
    </tr>
    <tr id="row5763782310134"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p3815206410134"><a name="p3815206410134"></a><a name="p3815206410134"></a>stream_names</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p330951110134"><a name="p330951110134"></a><a name="p330951110134"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p6674380110134"><a name="p6674380110134"></a><a name="p6674380110134"></a>Name of the list of the streams meeting the current requests.</p>
    </td>
    </tr>
    <tr id="row6382330310134"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p230503110134"><a name="p230503110134"></a><a name="p230503110134"></a>has_more_streams</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p5248983210134"><a name="p5248983210134"></a><a name="p5248983210134"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p2381800110134"><a name="p2381800110134"></a><a name="p2381800110134"></a>Specify whether there are more matching DIS streams to list. Possible values:</p>
    <a name="ul64226242104757"></a><a name="ul64226242104757"></a><ul id="ul64226242104757"><li><strong id="b988918134286"><a name="b988918134286"></a><a name="b988918134286"></a>true</strong>: There are more streams.</li><li><strong id="b66544233288"><a name="b66544233288"></a><a name="b66544233288"></a>false</strong>: There are no more streams.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Status Code<a name="section1303542510134"></a>

-   Normal

    200 OK

-   Failed

    For more information, see  [Error Codes](error-codes.md).


