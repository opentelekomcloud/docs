# Querying Grants on a CMK<a name="kms_02_0031"></a>

## Function<a name="en-us_topic_0112992310_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API enables you to query grants on a CMK.

## URI<a name="en-us_topic_0112992310_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/list-grants

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992310_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992310_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992310_p13230838154934"><a name="en-us_topic_0112992310_p13230838154934"></a><a name="en-us_topic_0112992310_p13230838154934"></a><strong id="en-us_topic_0112992310_b842352706193429"><a name="en-us_topic_0112992310_b842352706193429"></a><a name="en-us_topic_0112992310_b842352706193429"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.18%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992310_p65064970154934"><a name="en-us_topic_0112992310_p65064970154934"></a><a name="en-us_topic_0112992310_p65064970154934"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.49%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992310_p35771181154934"><a name="en-us_topic_0112992310_p35771181154934"></a><a name="en-us_topic_0112992310_p35771181154934"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.589999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992310_p11784586154934"><a name="en-us_topic_0112992310_p11784586154934"></a><a name="en-us_topic_0112992310_p11784586154934"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992310_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992310_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992310_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992310_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992310_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p4386100291125"><a name="en-us_topic_0112992310_p4386100291125"></a><a name="en-us_topic_0112992310_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992310_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992310_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992310_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992310_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992310_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992310_p20133141954612"><a name="en-us_topic_0112992310_p20133141954612"></a><a name="en-us_topic_0112992310_p20133141954612"></a><strong id="en-us_topic_0112992310_b468655270"><a name="en-us_topic_0112992310_b468655270"></a><a name="en-us_topic_0112992310_b468655270"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992310_p9133171918460"><a name="en-us_topic_0112992310_p9133171918460"></a><a name="en-us_topic_0112992310_p9133171918460"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992310_p13133151913465"><a name="en-us_topic_0112992310_p13133151913465"></a><a name="en-us_topic_0112992310_p13133151913465"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992310_p5133161934610"><a name="en-us_topic_0112992310_p5133161934610"></a><a name="en-us_topic_0112992310_p5133161934610"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992310_row57603225101653"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p7106589164345"><a name="en-us_topic_0112992310_p7106589164345"></a><a name="en-us_topic_0112992310_p7106589164345"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p52781696164345"><a name="en-us_topic_0112992310_p52781696164345"></a><a name="en-us_topic_0112992310_p52781696164345"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p27799391411"><a name="en-us_topic_0112992310_p27799391411"></a><a name="en-us_topic_0112992310_p27799391411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p47458964164345"><a name="en-us_topic_0112992310_p47458964164345"></a><a name="en-us_topic_0112992310_p47458964164345"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992310_parmvalue80435593163333_1"><a name="en-us_topic_0112992310_parmvalue80435593163333_1"></a><a name="en-us_topic_0112992310_parmvalue80435593163333_1"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992310_p60245386164345"><a name="en-us_topic_0112992310_p60245386164345"></a><a name="en-us_topic_0112992310_p60245386164345"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p5119285016439"><a name="en-us_topic_0112992310_p5119285016439"></a><a name="en-us_topic_0112992310_p5119285016439"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p6353760916439"><a name="en-us_topic_0112992310_p6353760916439"></a><a name="en-us_topic_0112992310_p6353760916439"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p297894117415"><a name="en-us_topic_0112992310_p297894117415"></a><a name="en-us_topic_0112992310_p297894117415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p5221068611357"><a name="en-us_topic_0112992310_p5221068611357"></a><a name="en-us_topic_0112992310_p5221068611357"></a>This parameter specifies the number of entries returned. If the specified number is smaller than the actual number of existing entries, <span class="parmvalue" id="en-us_topic_0112992310_parmvalue555125744154359"><a name="en-us_topic_0112992310_parmvalue555125744154359"></a><a name="en-us_topic_0112992310_parmvalue555125744154359"></a><b>true</b></span> will be returned for the response parameter <span class="parmname" id="en-us_topic_0112992310_parmname769647905154346"><a name="en-us_topic_0112992310_parmname769647905154346"></a><a name="en-us_topic_0112992310_parmname769647905154346"></a><b>truncated</b></span>, indicating that the query results will be displayed in separate pages.</p>
<p id="en-us_topic_0112992310_p4627274216439"><a name="en-us_topic_0112992310_p4627274216439"></a><a name="en-us_topic_0112992310_p4627274216439"></a>The value is within the range of the maximum number of grants, for example, <span class="parmvalue" id="en-us_topic_0112992310_parmvalue581493328154547"><a name="en-us_topic_0112992310_parmvalue581493328154547"></a><a name="en-us_topic_0112992310_parmvalue581493328154547"></a><b>100</b></span>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p2967402816439"><a name="en-us_topic_0112992310_p2967402816439"></a><a name="en-us_topic_0112992310_p2967402816439"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p848971516439"><a name="en-us_topic_0112992310_p848971516439"></a><a name="en-us_topic_0112992310_p848971516439"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p5811174412414"><a name="en-us_topic_0112992310_p5811174412414"></a><a name="en-us_topic_0112992310_p5811174412414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p3222420811429"><a name="en-us_topic_0112992310_p3222420811429"></a><a name="en-us_topic_0112992310_p3222420811429"></a>This parameter marks the starting location in a pagination query.</p>
<p id="en-us_topic_0112992310_p1657829916439"><a name="en-us_topic_0112992310_p1657829916439"></a><a name="en-us_topic_0112992310_p1657829916439"></a>If the <span class="parmname" id="en-us_topic_0112992310_parmname769647905155414"><a name="en-us_topic_0112992310_parmname769647905155414"></a><a name="en-us_topic_0112992310_parmname769647905155414"></a><b>truncated</b></span> value is <span class="parmvalue" id="en-us_topic_0112992310_parmvalue555125744155422"><a name="en-us_topic_0112992310_parmvalue555125744155422"></a><a name="en-us_topic_0112992310_parmvalue555125744155422"></a><b>true</b></span>, you can send consecutive requests to obtain more record entries. The <span class="parmname" id="en-us_topic_0112992310_parmname769647905155539"><a name="en-us_topic_0112992310_parmname769647905155539"></a><a name="en-us_topic_0112992310_parmname769647905155539"></a><b>marker</b></span> value must be set to the <span class="parmname" id="en-us_topic_0112992310_parmname769647905155552"><a name="en-us_topic_0112992310_parmname769647905155552"></a><a name="en-us_topic_0112992310_parmname769647905155552"></a><b>next_marker</b></span> value in the response, for example, <strong id="en-us_topic_0112992310_b7956061174331"><a name="en-us_topic_0112992310_b7956061174331"></a><a name="en-us_topic_0112992310_b7956061174331"></a>10</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row59920057164255"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p5386140416439"><a name="en-us_topic_0112992310_p5386140416439"></a><a name="en-us_topic_0112992310_p5386140416439"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p5650607916439"><a name="en-us_topic_0112992310_p5650607916439"></a><a name="en-us_topic_0112992310_p5650607916439"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p125415468416"><a name="en-us_topic_0112992310_p125415468416"></a><a name="en-us_topic_0112992310_p125415468416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p1358971416439"><a name="en-us_topic_0112992310_p1358971416439"></a><a name="en-us_topic_0112992310_p1358971416439"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992310_p5519856416439"><a name="en-us_topic_0112992310_p5519856416439"></a><a name="en-us_topic_0112992310_p5519856416439"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992310_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992310_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992310_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992310_p37751323114611"><a name="en-us_topic_0112992310_p37751323114611"></a><a name="en-us_topic_0112992310_p37751323114611"></a><strong id="en-us_topic_0112992310_b1356013904"><a name="en-us_topic_0112992310_b1356013904"></a><a name="en-us_topic_0112992310_b1356013904"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992310_p177751023164619"><a name="en-us_topic_0112992310_p177751023164619"></a><a name="en-us_topic_0112992310_p177751023164619"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992310_p167751823124611"><a name="en-us_topic_0112992310_p167751823124611"></a><a name="en-us_topic_0112992310_p167751823124611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992310_p4775323194612"><a name="en-us_topic_0112992310_p4775323194612"></a><a name="en-us_topic_0112992310_p4775323194612"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992310_r3c4af7b36e9240d197ab56255e37b83c"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p54751797164430"><a name="en-us_topic_0112992310_p54751797164430"></a><a name="en-us_topic_0112992310_p54751797164430"></a>grants</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p63244409104212"><a name="en-us_topic_0112992310_p63244409104212"></a><a name="en-us_topic_0112992310_p63244409104212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p37234992104212"><a name="en-us_topic_0112992310_p37234992104212"></a><a name="en-us_topic_0112992310_p37234992104212"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p22523510104212"><a name="en-us_topic_0112992310_p22523510104212"></a><a name="en-us_topic_0112992310_p22523510104212"></a>Grant list. For details, see <a href="#en-us_topic_0112992310_table17099798154440">Table 4</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row1195616116587"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p5734209165853"><a name="en-us_topic_0112992310_p5734209165853"></a><a name="en-us_topic_0112992310_p5734209165853"></a>next_marker</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p41184394165853"><a name="en-us_topic_0112992310_p41184394165853"></a><a name="en-us_topic_0112992310_p41184394165853"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p10107153514"><a name="en-us_topic_0112992310_p10107153514"></a><a name="en-us_topic_0112992310_p10107153514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p5174976311616"><a name="en-us_topic_0112992310_p5174976311616"></a><a name="en-us_topic_0112992310_p5174976311616"></a>This parameter indicates the <span class="parmname" id="en-us_topic_0112992310_parmname76964790515596"><a name="en-us_topic_0112992310_parmname76964790515596"></a><a name="en-us_topic_0112992310_parmname76964790515596"></a><b>marker</b></span> value required for obtaining the next page of query results.</p>
<p id="en-us_topic_0112992310_p47601640165853"><a name="en-us_topic_0112992310_p47601640165853"></a><a name="en-us_topic_0112992310_p47601640165853"></a>If the <span class="parmname" id="en-us_topic_0112992310_parmname769647905155931"><a name="en-us_topic_0112992310_parmname769647905155931"></a><a name="en-us_topic_0112992310_parmname769647905155931"></a><b>truncated</b></span> value is <span class="parmvalue" id="en-us_topic_0112992310_parmvalue555125744155940"><a name="en-us_topic_0112992310_parmvalue555125744155940"></a><a name="en-us_topic_0112992310_parmvalue555125744155940"></a><b>false</b></span>, the <span class="parmname" id="en-us_topic_0112992310_parmname76964790516018"><a name="en-us_topic_0112992310_parmname76964790516018"></a><a name="en-us_topic_0112992310_parmname76964790516018"></a><b>next_marker</b></span> parameter is left blank.</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row63650114165815"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p6312998165853"><a name="en-us_topic_0112992310_p6312998165853"></a><a name="en-us_topic_0112992310_p6312998165853"></a>truncated</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p13415518165853"><a name="en-us_topic_0112992310_p13415518165853"></a><a name="en-us_topic_0112992310_p13415518165853"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p3631073515"><a name="en-us_topic_0112992310_p3631073515"></a><a name="en-us_topic_0112992310_p3631073515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992310_p12915177165853"><a name="en-us_topic_0112992310_p12915177165853"></a><a name="en-us_topic_0112992310_p12915177165853"></a>This parameter indicates whether there are more results displayed in another page.<a name="en-us_topic_0112992310_ul49127730165853"></a><a name="en-us_topic_0112992310_ul49127730165853"></a><ul id="en-us_topic_0112992310_ul49127730165853"><li>If the value is <span class="parmvalue" id="en-us_topic_0112992310_parmvalue5551257441629"><a name="en-us_topic_0112992310_parmvalue5551257441629"></a><a name="en-us_topic_0112992310_parmvalue5551257441629"></a><b>true</b></span>, there are more results.</li><li>If the value is <span class="parmvalue" id="en-us_topic_0112992310_parmvalue199802661016215"><a name="en-us_topic_0112992310_parmvalue199802661016215"></a><a name="en-us_topic_0112992310_parmvalue199802661016215"></a><b>false</b></span>, the current page is the last page.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992310_row20501437105542"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p50003685105542"><a name="en-us_topic_0112992310_p50003685105542"></a><a name="en-us_topic_0112992310_p50003685105542"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p46051398105542"><a name="en-us_topic_0112992310_p46051398105542"></a><a name="en-us_topic_0112992310_p46051398105542"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p23766661105542"><a name="en-us_topic_0112992310_p23766661105542"></a><a name="en-us_topic_0112992310_p23766661105542"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p39175759105542"><a name="en-us_topic_0112992310_p39175759105542"></a><a name="en-us_topic_0112992310_p39175759105542"></a>This parameter indicates the total number of grants.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **grants**  field description

<a name="en-us_topic_0112992310_table17099798154440"></a>
<table><thead align="left"><tr id="en-us_topic_0112992310_row19888582154440"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992310_p102828329468"><a name="en-us_topic_0112992310_p102828329468"></a><a name="en-us_topic_0112992310_p102828329468"></a><strong id="en-us_topic_0112992310_b1229630228"><a name="en-us_topic_0112992310_b1229630228"></a><a name="en-us_topic_0112992310_b1229630228"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992310_p32825325461"><a name="en-us_topic_0112992310_p32825325461"></a><a name="en-us_topic_0112992310_p32825325461"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992310_p19282932124618"><a name="en-us_topic_0112992310_p19282932124618"></a><a name="en-us_topic_0112992310_p19282932124618"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992310_p92821132104612"><a name="en-us_topic_0112992310_p92821132104612"></a><a name="en-us_topic_0112992310_p92821132104612"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992310_row54890850154440"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p16973884154440"><a name="en-us_topic_0112992310_p16973884154440"></a><a name="en-us_topic_0112992310_p16973884154440"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p32050021154440"><a name="en-us_topic_0112992310_p32050021154440"></a><a name="en-us_topic_0112992310_p32050021154440"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p2457151017517"><a name="en-us_topic_0112992310_p2457151017517"></a><a name="en-us_topic_0112992310_p2457151017517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p45914884154440"><a name="en-us_topic_0112992310_p45914884154440"></a><a name="en-us_topic_0112992310_p45914884154440"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992310_parmvalue80435593163333_3"><a name="en-us_topic_0112992310_parmvalue80435593163333_3"></a><a name="en-us_topic_0112992310_parmvalue80435593163333_3"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992310_p62974560154440"><a name="en-us_topic_0112992310_p62974560154440"></a><a name="en-us_topic_0112992310_p62974560154440"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row665708154440"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p53922413154440"><a name="en-us_topic_0112992310_p53922413154440"></a><a name="en-us_topic_0112992310_p53922413154440"></a>grant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p54135917154440"><a name="en-us_topic_0112992310_p54135917154440"></a><a name="en-us_topic_0112992310_p54135917154440"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p1665915121259"><a name="en-us_topic_0112992310_p1665915121259"></a><a name="en-us_topic_0112992310_p1665915121259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p22933180154440"><a name="en-us_topic_0112992310_p22933180154440"></a><a name="en-us_topic_0112992310_p22933180154440"></a>64-byte ID of a grant that meets the regular expression <strong id="en-us_topic_0112992310_b842352706105044"><a name="en-us_topic_0112992310_b842352706105044"></a><a name="en-us_topic_0112992310_b842352706105044"></a>^[A-Fa-f0-9]{64}$</strong></p>
<p id="en-us_topic_0112992310_p45648287154440"><a name="en-us_topic_0112992310_p45648287154440"></a><a name="en-us_topic_0112992310_p45648287154440"></a>Example: 7c9a3286af4fcca5f0a385ad13e1d21a50e27b6dbcab50f37f30f93b8939827d</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row8181404154440"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p58713977154440"><a name="en-us_topic_0112992310_p58713977154440"></a><a name="en-us_topic_0112992310_p58713977154440"></a>grantee_principal</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p17525492154440"><a name="en-us_topic_0112992310_p17525492154440"></a><a name="en-us_topic_0112992310_p17525492154440"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p127211151354"><a name="en-us_topic_0112992310_p127211151354"></a><a name="en-us_topic_0112992310_p127211151354"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p10278754154440"><a name="en-us_topic_0112992310_p10278754154440"></a><a name="en-us_topic_0112992310_p10278754154440"></a>Indicates the ID of the authorized user. The value is between 1 to 64 bytes and meets the regular expression <strong id="en-us_topic_0112992310_b2067817137576"><a name="en-us_topic_0112992310_b2067817137576"></a><a name="en-us_topic_0112992310_b2067817137576"></a>"^[a-zA-Z0-9]{1,64}$"</strong>.</p>
<p id="en-us_topic_0112992310_p44128481154440"><a name="en-us_topic_0112992310_p44128481154440"></a><a name="en-us_topic_0112992310_p44128481154440"></a>Example: 0d0466b00d0466b00d0466b00d0466b0</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row61612009154440"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p24516817154440"><a name="en-us_topic_0112992310_p24516817154440"></a><a name="en-us_topic_0112992310_p24516817154440"></a>operations</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p61999538154440"><a name="en-us_topic_0112992310_p61999538154440"></a><a name="en-us_topic_0112992310_p61999538154440"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p39705137154440"><a name="en-us_topic_0112992310_p39705137154440"></a><a name="en-us_topic_0112992310_p39705137154440"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p55906683154440"><a name="en-us_topic_0112992310_p55906683154440"></a><a name="en-us_topic_0112992310_p55906683154440"></a>Permissions that can be granted. Values: <span class="parmname" id="en-us_topic_0112992310_parmname3365890071844"><a name="en-us_topic_0112992310_parmname3365890071844"></a><a name="en-us_topic_0112992310_parmname3365890071844"></a><b>create-datakey</b></span>, <span class="parmname" id="en-us_topic_0112992310_parmname11797450841844"><a name="en-us_topic_0112992310_parmname11797450841844"></a><a name="en-us_topic_0112992310_parmname11797450841844"></a><b>create-datakey-without-plaintext</b></span>, <span class="parmname" id="en-us_topic_0112992310_parmname3378262721844"><a name="en-us_topic_0112992310_parmname3378262721844"></a><a name="en-us_topic_0112992310_parmname3378262721844"></a><b>encrypt-datakey</b></span>, <span class="parmname" id="en-us_topic_0112992310_parmname2516172031844"><a name="en-us_topic_0112992310_parmname2516172031844"></a><a name="en-us_topic_0112992310_parmname2516172031844"></a><b>decrypt-datakey</b></span>, <span class="parmname" id="en-us_topic_0112992310_parmname18730752881844"><a name="en-us_topic_0112992310_parmname18730752881844"></a><a name="en-us_topic_0112992310_parmname18730752881844"></a><b>describe-key</b></span>, <span class="parmname" id="en-us_topic_0112992310_parmname13794118891844"><a name="en-us_topic_0112992310_parmname13794118891844"></a><a name="en-us_topic_0112992310_parmname13794118891844"></a><b>create-grant</b></span>, <span class="parmname" id="en-us_topic_0112992310_parmname14425042041844"><a name="en-us_topic_0112992310_parmname14425042041844"></a><a name="en-us_topic_0112992310_parmname14425042041844"></a><b>retire-grant</b></span></p>
<p id="en-us_topic_0112992310_p64392214154440"><a name="en-us_topic_0112992310_p64392214154440"></a><a name="en-us_topic_0112992310_p64392214154440"></a><span class="parmname" id="en-us_topic_0112992310_parmname42659018154440"><a name="en-us_topic_0112992310_parmname42659018154440"></a><a name="en-us_topic_0112992310_parmname42659018154440"></a><b>create-grant</b></span> cannot be the only value.</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row48386850154440"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p27020774154440"><a name="en-us_topic_0112992310_p27020774154440"></a><a name="en-us_topic_0112992310_p27020774154440"></a>issuing_principal</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p48794041154440"><a name="en-us_topic_0112992310_p48794041154440"></a><a name="en-us_topic_0112992310_p48794041154440"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p1540402714518"><a name="en-us_topic_0112992310_p1540402714518"></a><a name="en-us_topic_0112992310_p1540402714518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p60003223154440"><a name="en-us_topic_0112992310_p60003223154440"></a><a name="en-us_topic_0112992310_p60003223154440"></a>Indicates the ID of the user who created the grant. The value is between 1 to 64 bytes and meets the regular expression <strong id="en-us_topic_0112992310_b14326165710"><a name="en-us_topic_0112992310_b14326165710"></a><a name="en-us_topic_0112992310_b14326165710"></a>"^[a-zA-Z0-9]{1,64}$"</strong>.</p>
<p id="en-us_topic_0112992310_p54479161154440"><a name="en-us_topic_0112992310_p54479161154440"></a><a name="en-us_topic_0112992310_p54479161154440"></a>Example: 0d0466b00d0466b00d0466b00d0466b0</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row20550404154440"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p53970019154440"><a name="en-us_topic_0112992310_p53970019154440"></a><a name="en-us_topic_0112992310_p53970019154440"></a>creation_date</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p30933436154440"><a name="en-us_topic_0112992310_p30933436154440"></a><a name="en-us_topic_0112992310_p30933436154440"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p1871912812515"><a name="en-us_topic_0112992310_p1871912812515"></a><a name="en-us_topic_0112992310_p1871912812515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p22580357154440"><a name="en-us_topic_0112992310_p22580357154440"></a><a name="en-us_topic_0112992310_p22580357154440"></a>Creation time. The value is a timestamp expressed in the number of seconds since 00:00:00 UTC on January 1, 1970.</p>
<p id="en-us_topic_0112992310_p17069590154440"><a name="en-us_topic_0112992310_p17069590154440"></a><a name="en-us_topic_0112992310_p17069590154440"></a>Example: 1497341531000</p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row19408585154440"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p28591578154440"><a name="en-us_topic_0112992310_p28591578154440"></a><a name="en-us_topic_0112992310_p28591578154440"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p20074746154440"><a name="en-us_topic_0112992310_p20074746154440"></a><a name="en-us_topic_0112992310_p20074746154440"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p14336173019518"><a name="en-us_topic_0112992310_p14336173019518"></a><a name="en-us_topic_0112992310_p14336173019518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p15441753154440"><a name="en-us_topic_0112992310_p15441753154440"></a><a name="en-us_topic_0112992310_p15441753154440"></a>Name of a grant which can be 1 to 255 characters in length and matches the regular expression <strong id="en-us_topic_0112992310_b842352706104539"><a name="en-us_topic_0112992310_b842352706104539"></a><a name="en-us_topic_0112992310_b842352706104539"></a>^[a-zA-Z0-9:/_-]{1,255}$</strong></p>
</td>
</tr>
<tr id="en-us_topic_0112992310_row4758052154440"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992310_p49857969154440"><a name="en-us_topic_0112992310_p49857969154440"></a><a name="en-us_topic_0112992310_p49857969154440"></a>retiring_principal</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992310_p29533843154440"><a name="en-us_topic_0112992310_p29533843154440"></a><a name="en-us_topic_0112992310_p29533843154440"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992310_p1140143218518"><a name="en-us_topic_0112992310_p1140143218518"></a><a name="en-us_topic_0112992310_p1140143218518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992310_p43431097154440"><a name="en-us_topic_0112992310_p43431097154440"></a><a name="en-us_topic_0112992310_p43431097154440"></a>Indicates the ID of the retiring user. The value is between 1 to 64 bytes and meets the regular expression <strong id="en-us_topic_0112992310_b19526162355818"><a name="en-us_topic_0112992310_b19526162355818"></a><a name="en-us_topic_0112992310_b19526162355818"></a>"^[a-zA-Z0-9]{1,64}$"</strong>.</p>
<p id="en-us_topic_0112992310_p52995191154440"><a name="en-us_topic_0112992310_p52995191154440"></a><a name="en-us_topic_0112992310_p52995191154440"></a>Example: 0d0466b00d0466b00d0466b00d0466b0</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992310_section853474470"></a>

The following example describes how to query the grant list of a CMK whose ID is  **0d0466b0-e727-4d9c-b35d-f84bb474a37f**.

-   Example request

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
        "limit": "",
        "marker": ""
    }
    ```

-   Example response

    ```
    {
        "grants": [
         {"key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
          "grant_id": "7c9a3286af4fcca5f0a385ad13e1d21a50e27b6dbcab50f37f30f93b8939827d",
          "operations": 
          ["describe-key","create-datakey", "encrypt-datakey"],
          "grantee_principal":"13gg44z4g2sglzk0egw0u726zoyzvrs8",
          "retiring_principal":"13gg44z4g2sglzk0egw0u726zoyzvrs8",
          "issuing_principal":"e4hkeeea506ex3wgnzyhi656n8hx8xa3",
          "name":"my_grant",
          "creation_date":"1497341531000",
          }],
        "next_marker": "",
        "truncated": "false",
        "total":1
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


## Status Codes<a name="en-us_topic_0112992310_section3454223421"></a>

[Table 5](#en-us_topic_0112992310_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  5**  Status codes

<a name="en-us_topic_0112992310_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992310_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992310_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992310_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992310_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992310_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992310_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992310_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992310_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992310_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992310_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992310_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992310_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992310_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992310_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992310_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992310_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992310_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992310_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992310_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992310_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

