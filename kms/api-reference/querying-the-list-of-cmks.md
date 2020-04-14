# Querying the List of CMKs<a name="kms_02_0017"></a>

## Function<a name="en-us_topic_0112992332_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API allows you to query the list of all CMKs.

## URI<a name="en-us_topic_0112992332_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/list-keys

-   Parameter description

    **Table  1**  Parameters

    <a name="en-us_topic_0112992332_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992332_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992332_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992332_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992332_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.18%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992332_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992332_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992332_ad98d2f62bd064b4e96ea922645197c24"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.49%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992332_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992332_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992332_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.589999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992332_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992332_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992332_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992332_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992332_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992332_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992332_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992332_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_a1a4a71c11a4a45a58d0de2fbe009e9d9"><a name="en-us_topic_0112992332_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a><a name="en-us_topic_0112992332_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992332_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992332_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992332_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992332_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992332_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992332_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992332_p16364058101230"><a name="en-us_topic_0112992332_p16364058101230"></a><a name="en-us_topic_0112992332_p16364058101230"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992332_p57514295101230"><a name="en-us_topic_0112992332_p57514295101230"></a><a name="en-us_topic_0112992332_p57514295101230"></a><strong id="en-us_topic_0112992332_b84235270617239"><a name="en-us_topic_0112992332_b84235270617239"></a><a name="en-us_topic_0112992332_b84235270617239"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992332_p50420322101230"><a name="en-us_topic_0112992332_p50420322101230"></a><a name="en-us_topic_0112992332_p50420322101230"></a><strong id="en-us_topic_0112992332_b84235270617236"><a name="en-us_topic_0112992332_b84235270617236"></a><a name="en-us_topic_0112992332_b84235270617236"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992332_p28146304101230"><a name="en-us_topic_0112992332_p28146304101230"></a><a name="en-us_topic_0112992332_p28146304101230"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992332_row57603225101653"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p2406663910414"><a name="en-us_topic_0112992332_p2406663910414"></a><a name="en-us_topic_0112992332_p2406663910414"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p6117641210414"><a name="en-us_topic_0112992332_p6117641210414"></a><a name="en-us_topic_0112992332_p6117641210414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p324077710414"><a name="en-us_topic_0112992332_p324077710414"></a><a name="en-us_topic_0112992332_p324077710414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992332_p626119710323"><a name="en-us_topic_0112992332_p626119710323"></a><a name="en-us_topic_0112992332_p626119710323"></a>This parameter specifies the number of entries returned. If the specified number is smaller than the actual number of existing entries, <span class="parmvalue" id="en-us_topic_0112992332_parmvalue555125744154359"><a name="en-us_topic_0112992332_parmvalue555125744154359"></a><a name="en-us_topic_0112992332_parmvalue555125744154359"></a><b>true</b></span> will be returned for the response parameter <span class="parmname" id="en-us_topic_0112992332_parmname769647905154346"><a name="en-us_topic_0112992332_parmname769647905154346"></a><a name="en-us_topic_0112992332_parmname769647905154346"></a><b>truncated</b></span>, indicating that the query results will be displayed in separate pages. The value is within the range of the maximum number of CMKs, for example, <span class="parmvalue" id="en-us_topic_0112992332_parmvalue581493328154547"><a name="en-us_topic_0112992332_parmvalue581493328154547"></a><a name="en-us_topic_0112992332_parmvalue581493328154547"></a><b>100</b></span>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992332_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p42887432104114"><a name="en-us_topic_0112992332_p42887432104114"></a><a name="en-us_topic_0112992332_p42887432104114"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p64085219104114"><a name="en-us_topic_0112992332_p64085219104114"></a><a name="en-us_topic_0112992332_p64085219104114"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p51329949104114"><a name="en-us_topic_0112992332_p51329949104114"></a><a name="en-us_topic_0112992332_p51329949104114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992332_p4503778810356"><a name="en-us_topic_0112992332_p4503778810356"></a><a name="en-us_topic_0112992332_p4503778810356"></a>This parameter marks the starting location in a pagination query. If the <span class="parmname" id="en-us_topic_0112992332_parmname769647905155414"><a name="en-us_topic_0112992332_parmname769647905155414"></a><a name="en-us_topic_0112992332_parmname769647905155414"></a><b>truncated</b></span> value is <span class="parmvalue" id="en-us_topic_0112992332_parmvalue555125744155422"><a name="en-us_topic_0112992332_parmvalue555125744155422"></a><a name="en-us_topic_0112992332_parmvalue555125744155422"></a><b>true</b></span>, you can send consecutive requests to obtain more record entries. The <span class="parmname" id="en-us_topic_0112992332_parmname769647905155539"><a name="en-us_topic_0112992332_parmname769647905155539"></a><a name="en-us_topic_0112992332_parmname769647905155539"></a><b>marker</b></span> value must be set to the <span class="parmname" id="en-us_topic_0112992332_parmname769647905155552"><a name="en-us_topic_0112992332_parmname769647905155552"></a><a name="en-us_topic_0112992332_parmname769647905155552"></a><b>next_marker</b></span> value in the response, for example, <strong id="en-us_topic_0112992332_b7956061174331"><a name="en-us_topic_0112992332_b7956061174331"></a><a name="en-us_topic_0112992332_b7956061174331"></a>10</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992332_row42549357201259"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p23945891201259"><a name="en-us_topic_0112992332_p23945891201259"></a><a name="en-us_topic_0112992332_p23945891201259"></a>key_state</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p7141059201259"><a name="en-us_topic_0112992332_p7141059201259"></a><a name="en-us_topic_0112992332_p7141059201259"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p60568989201259"><a name="en-us_topic_0112992332_p60568989201259"></a><a name="en-us_topic_0112992332_p60568989201259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992332_p41554943201259"><a name="en-us_topic_0112992332_p41554943201259"></a><a name="en-us_topic_0112992332_p41554943201259"></a>State of a CMK that matches the regular expression <strong id="en-us_topic_0112992332_b84235270614341"><a name="en-us_topic_0112992332_b84235270614341"></a><a name="en-us_topic_0112992332_b84235270614341"></a>^[1-5]{1}$</strong>. The following values are enumerated:<a name="en-us_topic_0112992332_ul2802984616441"></a><a name="en-us_topic_0112992332_ul2802984616441"></a><ul id="en-us_topic_0112992332_ul2802984616441"><li><span class="parmvalue" id="en-us_topic_0112992332_parmvalue790137356143445"><a name="en-us_topic_0112992332_parmvalue790137356143445"></a><a name="en-us_topic_0112992332_parmvalue790137356143445"></a><b>1</b></span> indicates that the CMK is waiting to be activated.</li><li><span class="parmvalue" id="en-us_topic_0112992332_parmvalue74644497143524"><a name="en-us_topic_0112992332_parmvalue74644497143524"></a><a name="en-us_topic_0112992332_parmvalue74644497143524"></a><b>2</b></span> indicates that the CMK is enabled.</li><li><span class="parmvalue" id="en-us_topic_0112992332_parmvalue1055024806143535"><a name="en-us_topic_0112992332_parmvalue1055024806143535"></a><a name="en-us_topic_0112992332_parmvalue1055024806143535"></a><b>3</b></span> indicates that the CMK is disabled.</li><li><span class="parmvalue" id="en-us_topic_0112992332_parmvalue7929059216370"><a name="en-us_topic_0112992332_parmvalue7929059216370"></a><a name="en-us_topic_0112992332_parmvalue7929059216370"></a><b>4</b></span> indicates that the CMK is scheduled for deletion.</li><li><span class="parmvalue" id="en-us_topic_0112992332_parmvalue173030430014366"><a name="en-us_topic_0112992332_parmvalue173030430014366"></a><a name="en-us_topic_0112992332_parmvalue173030430014366"></a><b>5</b></span> indicates that the CMK is waiting to be imported.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992332_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p269135101746"><a name="en-us_topic_0112992332_p269135101746"></a><a name="en-us_topic_0112992332_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p20967256101746"><a name="en-us_topic_0112992332_p20967256101746"></a><a name="en-us_topic_0112992332_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p21799971101746"><a name="en-us_topic_0112992332_p21799971101746"></a><a name="en-us_topic_0112992332_p21799971101746"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992332_p3278919416563"><a name="en-us_topic_0112992332_p3278919416563"></a><a name="en-us_topic_0112992332_p3278919416563"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992332_p20626198101746"><a name="en-us_topic_0112992332_p20626198101746"></a><a name="en-us_topic_0112992332_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992332_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992332_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992332_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992332_a9156e0b03f054d4e8547e0787f88a51b"><a name="en-us_topic_0112992332_a9156e0b03f054d4e8547e0787f88a51b"></a><a name="en-us_topic_0112992332_a9156e0b03f054d4e8547e0787f88a51b"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.07%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992332_a1851157c81e14d7f82db752a5737195a"><a name="en-us_topic_0112992332_a1851157c81e14d7f82db752a5737195a"></a><a name="en-us_topic_0112992332_a1851157c81e14d7f82db752a5737195a"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.93%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992332_a39360acf5daf4c01a1ebddeff5d68a1c"><a name="en-us_topic_0112992332_a39360acf5daf4c01a1ebddeff5d68a1c"></a><a name="en-us_topic_0112992332_a39360acf5daf4c01a1ebddeff5d68a1c"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992332_a0097000016b14857972b7929bcaaa038"><a name="en-us_topic_0112992332_a0097000016b14857972b7929bcaaa038"></a><a name="en-us_topic_0112992332_a0097000016b14857972b7929bcaaa038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992332_r3c4af7b36e9240d197ab56255e37b83c"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p2945204104212"><a name="en-us_topic_0112992332_p2945204104212"></a><a name="en-us_topic_0112992332_p2945204104212"></a>keys</p>
</td>
<td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p63244409104212"><a name="en-us_topic_0112992332_p63244409104212"></a><a name="en-us_topic_0112992332_p63244409104212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.93%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p37234992104212"><a name="en-us_topic_0112992332_p37234992104212"></a><a name="en-us_topic_0112992332_p37234992104212"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992332_p22523510104212"><a name="en-us_topic_0112992332_p22523510104212"></a><a name="en-us_topic_0112992332_p22523510104212"></a>List of CMK IDs</p>
</td>
</tr>
<tr id="en-us_topic_0112992332_row41153948202117"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p45135511202117"><a name="en-us_topic_0112992332_p45135511202117"></a><a name="en-us_topic_0112992332_p45135511202117"></a>key_details</p>
</td>
<td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p49783918202117"><a name="en-us_topic_0112992332_p49783918202117"></a><a name="en-us_topic_0112992332_p49783918202117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.93%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p32097787202117"><a name="en-us_topic_0112992332_p32097787202117"></a><a name="en-us_topic_0112992332_p32097787202117"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992332_p5965595202117"><a name="en-us_topic_0112992332_p5965595202117"></a><a name="en-us_topic_0112992332_p5965595202117"></a>Key details list. For details, see <a href="querying-the-information-about-a-cmk.md#en-us_topic_0112992343_t98d238e10953421e84a073707024c329">Table 3</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992332_rf212a916c502452a8e151eba2f118272"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p47854970104223"><a name="en-us_topic_0112992332_p47854970104223"></a><a name="en-us_topic_0112992332_p47854970104223"></a>next_marker</p>
</td>
<td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p41198131104223"><a name="en-us_topic_0112992332_p41198131104223"></a><a name="en-us_topic_0112992332_p41198131104223"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.93%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p51047393104223"><a name="en-us_topic_0112992332_p51047393104223"></a><a name="en-us_topic_0112992332_p51047393104223"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992332_p48714330104223"><a name="en-us_topic_0112992332_p48714330104223"></a><a name="en-us_topic_0112992332_p48714330104223"></a>This parameter indicates the <span class="parmname" id="en-us_topic_0112992332_parmname76964790515596"><a name="en-us_topic_0112992332_parmname76964790515596"></a><a name="en-us_topic_0112992332_parmname76964790515596"></a><b>marker</b></span> value required for obtaining the next page of query results. If the <span class="parmname" id="en-us_topic_0112992332_parmname769647905155931"><a name="en-us_topic_0112992332_parmname769647905155931"></a><a name="en-us_topic_0112992332_parmname769647905155931"></a><b>truncated</b></span> value is <span class="parmvalue" id="en-us_topic_0112992332_parmvalue555125744155940"><a name="en-us_topic_0112992332_parmvalue555125744155940"></a><a name="en-us_topic_0112992332_parmvalue555125744155940"></a><b>false</b></span>, the <span class="parmname" id="en-us_topic_0112992332_parmname76964790516018"><a name="en-us_topic_0112992332_parmname76964790516018"></a><a name="en-us_topic_0112992332_parmname76964790516018"></a><b>next_marker</b></span> parameter is left blank.</p>
</td>
</tr>
<tr id="en-us_topic_0112992332_row187911115485"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p50003685105542"><a name="en-us_topic_0112992332_p50003685105542"></a><a name="en-us_topic_0112992332_p50003685105542"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p46051398105542"><a name="en-us_topic_0112992332_p46051398105542"></a><a name="en-us_topic_0112992332_p46051398105542"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.93%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p23766661105542"><a name="en-us_topic_0112992332_p23766661105542"></a><a name="en-us_topic_0112992332_p23766661105542"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992332_p39175759105542"><a name="en-us_topic_0112992332_p39175759105542"></a><a name="en-us_topic_0112992332_p39175759105542"></a>Total number of keys.</p>
</td>
</tr>
<tr id="en-us_topic_0112992332_row29383366104234"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992332_p13323310104240"><a name="en-us_topic_0112992332_p13323310104240"></a><a name="en-us_topic_0112992332_p13323310104240"></a>truncated</p>
</td>
<td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992332_p38497122104240"><a name="en-us_topic_0112992332_p38497122104240"></a><a name="en-us_topic_0112992332_p38497122104240"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.93%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992332_p5446300104240"><a name="en-us_topic_0112992332_p5446300104240"></a><a name="en-us_topic_0112992332_p5446300104240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992332_p39550465161737"><a name="en-us_topic_0112992332_p39550465161737"></a><a name="en-us_topic_0112992332_p39550465161737"></a>This parameter indicates whether there are more results displayed in another page.<a name="en-us_topic_0112992332_ul43826915161742"></a><a name="en-us_topic_0112992332_ul43826915161742"></a><ul id="en-us_topic_0112992332_ul43826915161742"><li>If the value is <span class="parmvalue" id="en-us_topic_0112992332_parmvalue5551257441629"><a name="en-us_topic_0112992332_parmvalue5551257441629"></a><a name="en-us_topic_0112992332_parmvalue5551257441629"></a><b>true</b></span>, there are more results.</li><li>If the value is <span class="parmvalue" id="en-us_topic_0112992332_parmvalue30958336113051"><a name="en-us_topic_0112992332_parmvalue30958336113051"></a><a name="en-us_topic_0112992332_parmvalue30958336113051"></a><b>false</b></span>, the current page is the last page.</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992332_section1052520421315"></a>

The following shows an example when  **limit**  is set to  **2**  and  **marker**  is set to  **1**.

-   Example request

    ```
    {
        "limit": "2",
        "marker": "1"
    }
    ```

-   Example response

    ```
    {
        "keys": [
            "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "2e258389-bb1e-4568-a1d5-e1f50adf70ea"
        ],
        "key_details": [
            {
            "key_id":"0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "domain_id":"00074811d5c27c4f8d48bb91e4a1dcfd",
            "key_alias":"caseuirpr",
            "realm":"aaaa",
            "key_description":"123",
            "creation_date":"1502799822000",
            "scheduled_deletion_date":"",
            "key_state":"2",
            "default_key_flag":"0",
            "key_type":"1",
            "expiration_time":"1501578672000",
            "origin":"kms"
    },
            {
            "key_id":"2e258389-bb1e-4568-a1d5-e1f50adf70ea",
            "domain_id":"00074811d5c27c4f8d48bb91e4a1dcfd",
            "key_alias":"casehvniz",
            "realm":"aaaa",
            "key_description":"234",
            "creation_date":"1502799820000",             
            "scheduled_deletion_date":"",
            "key_state":"2",
            "default_key_flag":"0",
            "key_type":"1",
            "expiration_time":"1501578673000",
            "origin":"kms"
    }
         ],
        "next_marker": "",
        "truncated": "false",
        "total":2
    }
    ```

    or

    ```
    {
        "error": {
            "error_code": "KMS.XXXX",
            "error_msg": "XXX"
        }
    }
    ```


## Status Codes<a name="en-us_topic_0112992332_section3454223421"></a>

[Table 4](#en-us_topic_0112992332_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992332_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992332_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992332_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992332_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992332_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992332_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992332_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992332_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992332_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992332_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992332_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992332_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992332_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992332_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992332_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992332_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992332_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992332_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992332_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992332_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992332_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

