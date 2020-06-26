# Querying Grants That Can Be Retired<a name="kms_02_0032"></a>

## Function<a name="en-us_topic_0112992293_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API enables you to query grants that can be retired.

## URI<a name="en-us_topic_0112992293_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/list-retirable-grants

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992293_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992293_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992293_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992293_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992293_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><strong id="en-us_topic_0112992293_b842352706193829"><a name="en-us_topic_0112992293_b842352706193829"></a><a name="en-us_topic_0112992293_b842352706193829"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.18%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992293_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992293_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992293_ad98d2f62bd064b4e96ea922645197c24"></a><strong id="en-us_topic_0112992293_b842352706193832"><a name="en-us_topic_0112992293_b842352706193832"></a><a name="en-us_topic_0112992293_b842352706193832"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.49%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992293_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992293_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992293_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.589999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992293_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992293_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992293_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992293_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992293_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992293_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992293_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992293_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992293_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992293_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992293_p4386100291125"><a name="en-us_topic_0112992293_p4386100291125"></a><a name="en-us_topic_0112992293_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992293_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992293_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992293_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992293_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992293_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992293_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992293_p16364058101230"><a name="en-us_topic_0112992293_p16364058101230"></a><a name="en-us_topic_0112992293_p16364058101230"></a><strong id="en-us_topic_0112992293_b673430343"><a name="en-us_topic_0112992293_b673430343"></a><a name="en-us_topic_0112992293_b673430343"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992293_p57514295101230"><a name="en-us_topic_0112992293_p57514295101230"></a><a name="en-us_topic_0112992293_p57514295101230"></a><strong id="en-us_topic_0112992293_b842352706193857"><a name="en-us_topic_0112992293_b842352706193857"></a><a name="en-us_topic_0112992293_b842352706193857"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992293_p50420322101230"><a name="en-us_topic_0112992293_p50420322101230"></a><a name="en-us_topic_0112992293_p50420322101230"></a><strong id="en-us_topic_0112992293_b842352706193855"><a name="en-us_topic_0112992293_b842352706193855"></a><a name="en-us_topic_0112992293_b842352706193855"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992293_p28146304101230"><a name="en-us_topic_0112992293_p28146304101230"></a><a name="en-us_topic_0112992293_p28146304101230"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992293_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992293_p5119285016439"><a name="en-us_topic_0112992293_p5119285016439"></a><a name="en-us_topic_0112992293_p5119285016439"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992293_p6353760916439"><a name="en-us_topic_0112992293_p6353760916439"></a><a name="en-us_topic_0112992293_p6353760916439"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992293_p0691401259"><a name="en-us_topic_0112992293_p0691401259"></a><a name="en-us_topic_0112992293_p0691401259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992293_p187030631183"><a name="en-us_topic_0112992293_p187030631183"></a><a name="en-us_topic_0112992293_p187030631183"></a>This parameter specifies the number of entries returned. If the specified number is smaller than the actual number of existing entries, <span class="parmvalue" id="en-us_topic_0112992293_parmvalue555125744154359"><a name="en-us_topic_0112992293_parmvalue555125744154359"></a><a name="en-us_topic_0112992293_parmvalue555125744154359"></a><b>true</b></span> will be returned for the response parameter <span class="parmname" id="en-us_topic_0112992293_parmname769647905154346"><a name="en-us_topic_0112992293_parmname769647905154346"></a><a name="en-us_topic_0112992293_parmname769647905154346"></a><b>truncated</b></span>, indicating that the query results will be displayed in separate pages.</p>
<p id="en-us_topic_0112992293_p4627274216439"><a name="en-us_topic_0112992293_p4627274216439"></a><a name="en-us_topic_0112992293_p4627274216439"></a>The value is within the range of the maximum number of grants, for example, <span class="parmvalue" id="en-us_topic_0112992293_parmvalue581493328154547"><a name="en-us_topic_0112992293_parmvalue581493328154547"></a><a name="en-us_topic_0112992293_parmvalue581493328154547"></a><b>100</b></span>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992293_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992293_p2967402816439"><a name="en-us_topic_0112992293_p2967402816439"></a><a name="en-us_topic_0112992293_p2967402816439"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992293_p848971516439"><a name="en-us_topic_0112992293_p848971516439"></a><a name="en-us_topic_0112992293_p848971516439"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992293_p1110110421756"><a name="en-us_topic_0112992293_p1110110421756"></a><a name="en-us_topic_0112992293_p1110110421756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992293_p1313368711816"><a name="en-us_topic_0112992293_p1313368711816"></a><a name="en-us_topic_0112992293_p1313368711816"></a>This parameter marks the starting location in a pagination query.</p>
<p id="en-us_topic_0112992293_p1657829916439"><a name="en-us_topic_0112992293_p1657829916439"></a><a name="en-us_topic_0112992293_p1657829916439"></a>If the <span class="parmname" id="en-us_topic_0112992293_parmname769647905155414"><a name="en-us_topic_0112992293_parmname769647905155414"></a><a name="en-us_topic_0112992293_parmname769647905155414"></a><b>truncated</b></span> value is <span class="parmvalue" id="en-us_topic_0112992293_parmvalue555125744155422"><a name="en-us_topic_0112992293_parmvalue555125744155422"></a><a name="en-us_topic_0112992293_parmvalue555125744155422"></a><b>true</b></span>, you can send consecutive requests to obtain more record entries. The <span class="parmname" id="en-us_topic_0112992293_parmname769647905155539"><a name="en-us_topic_0112992293_parmname769647905155539"></a><a name="en-us_topic_0112992293_parmname769647905155539"></a><b>marker</b></span> value must be set to the <span class="parmname" id="en-us_topic_0112992293_parmname769647905155552"><a name="en-us_topic_0112992293_parmname769647905155552"></a><a name="en-us_topic_0112992293_parmname769647905155552"></a><b>next_marker</b></span> value in the response, for example, <strong id="en-us_topic_0112992293_b7956061174331"><a name="en-us_topic_0112992293_b7956061174331"></a><a name="en-us_topic_0112992293_b7956061174331"></a>10</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992293_row59920057164255"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992293_p5386140416439"><a name="en-us_topic_0112992293_p5386140416439"></a><a name="en-us_topic_0112992293_p5386140416439"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992293_p5650607916439"><a name="en-us_topic_0112992293_p5650607916439"></a><a name="en-us_topic_0112992293_p5650607916439"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992293_p213117445516"><a name="en-us_topic_0112992293_p213117445516"></a><a name="en-us_topic_0112992293_p213117445516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992293_p1358971416439"><a name="en-us_topic_0112992293_p1358971416439"></a><a name="en-us_topic_0112992293_p1358971416439"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992293_p5519856416439"><a name="en-us_topic_0112992293_p5519856416439"></a><a name="en-us_topic_0112992293_p5519856416439"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992293_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992293_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992293_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992293_p13230838154934"><a name="en-us_topic_0112992293_p13230838154934"></a><a name="en-us_topic_0112992293_p13230838154934"></a><strong id="en-us_topic_0112992293_b1065095169"><a name="en-us_topic_0112992293_b1065095169"></a><a name="en-us_topic_0112992293_b1065095169"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992293_p65064970154934"><a name="en-us_topic_0112992293_p65064970154934"></a><a name="en-us_topic_0112992293_p65064970154934"></a><strong id="en-us_topic_0112992293_b1114472755"><a name="en-us_topic_0112992293_b1114472755"></a><a name="en-us_topic_0112992293_b1114472755"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992293_p35771181154934"><a name="en-us_topic_0112992293_p35771181154934"></a><a name="en-us_topic_0112992293_p35771181154934"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992293_p11784586154934"><a name="en-us_topic_0112992293_p11784586154934"></a><a name="en-us_topic_0112992293_p11784586154934"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992293_r3c4af7b36e9240d197ab56255e37b83c"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992293_p54751797164430"><a name="en-us_topic_0112992293_p54751797164430"></a><a name="en-us_topic_0112992293_p54751797164430"></a>grants</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992293_p63244409104212"><a name="en-us_topic_0112992293_p63244409104212"></a><a name="en-us_topic_0112992293_p63244409104212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992293_p18681346567"><a name="en-us_topic_0112992293_p18681346567"></a><a name="en-us_topic_0112992293_p18681346567"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992293_p22523510104212"><a name="en-us_topic_0112992293_p22523510104212"></a><a name="en-us_topic_0112992293_p22523510104212"></a>Grant list. For details, see <a href="querying-grants-on-a-cmk.md#en-us_topic_0112992310_table17099798154440">Table 4</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992293_row1195616116587"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992293_p5734209165853"><a name="en-us_topic_0112992293_p5734209165853"></a><a name="en-us_topic_0112992293_p5734209165853"></a>next_marker</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992293_p41184394165853"><a name="en-us_topic_0112992293_p41184394165853"></a><a name="en-us_topic_0112992293_p41184394165853"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992293_p750913471517"><a name="en-us_topic_0112992293_p750913471517"></a><a name="en-us_topic_0112992293_p750913471517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992293_p40375092113058"><a name="en-us_topic_0112992293_p40375092113058"></a><a name="en-us_topic_0112992293_p40375092113058"></a>This parameter indicates the <span class="parmname" id="en-us_topic_0112992293_parmname76964790515596"><a name="en-us_topic_0112992293_parmname76964790515596"></a><a name="en-us_topic_0112992293_parmname76964790515596"></a><b>marker</b></span> value required for obtaining the next page of query results.</p>
<p id="en-us_topic_0112992293_p47601640165853"><a name="en-us_topic_0112992293_p47601640165853"></a><a name="en-us_topic_0112992293_p47601640165853"></a>If the <span class="parmname" id="en-us_topic_0112992293_parmname769647905155931"><a name="en-us_topic_0112992293_parmname769647905155931"></a><a name="en-us_topic_0112992293_parmname769647905155931"></a><b>truncated</b></span> value is <span class="parmvalue" id="en-us_topic_0112992293_parmvalue555125744155940"><a name="en-us_topic_0112992293_parmvalue555125744155940"></a><a name="en-us_topic_0112992293_parmvalue555125744155940"></a><b>false</b></span>, the <span class="parmname" id="en-us_topic_0112992293_parmname76964790516018"><a name="en-us_topic_0112992293_parmname76964790516018"></a><a name="en-us_topic_0112992293_parmname76964790516018"></a><b>next_marker</b></span> parameter is left blank.</p>
</td>
</tr>
<tr id="en-us_topic_0112992293_row63650114165815"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992293_p6312998165853"><a name="en-us_topic_0112992293_p6312998165853"></a><a name="en-us_topic_0112992293_p6312998165853"></a>truncated</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992293_p13415518165853"><a name="en-us_topic_0112992293_p13415518165853"></a><a name="en-us_topic_0112992293_p13415518165853"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992293_p26461450057"><a name="en-us_topic_0112992293_p26461450057"></a><a name="en-us_topic_0112992293_p26461450057"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992293_p12915177165853"><a name="en-us_topic_0112992293_p12915177165853"></a><a name="en-us_topic_0112992293_p12915177165853"></a>This parameter indicates whether there are more results displayed in another page.<a name="en-us_topic_0112992293_ul49127730165853"></a><a name="en-us_topic_0112992293_ul49127730165853"></a><ul id="en-us_topic_0112992293_ul49127730165853"><li>If the value is <span class="parmvalue" id="en-us_topic_0112992293_parmvalue5551257441629"><a name="en-us_topic_0112992293_parmvalue5551257441629"></a><a name="en-us_topic_0112992293_parmvalue5551257441629"></a><b>true</b></span>, there are more results.</li><li>If the value is <span class="parmvalue" id="en-us_topic_0112992293_parmvalue30958336113051"><a name="en-us_topic_0112992293_parmvalue30958336113051"></a><a name="en-us_topic_0112992293_parmvalue30958336113051"></a><b>false</b></span>, the current page is the last page.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992293_row41123860163925"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992293_p37562908163928"><a name="en-us_topic_0112992293_p37562908163928"></a><a name="en-us_topic_0112992293_p37562908163928"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992293_p26496943163928"><a name="en-us_topic_0112992293_p26496943163928"></a><a name="en-us_topic_0112992293_p26496943163928"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992293_p22696744163928"><a name="en-us_topic_0112992293_p22696744163928"></a><a name="en-us_topic_0112992293_p22696744163928"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992293_p65877659163928"><a name="en-us_topic_0112992293_p65877659163928"></a><a name="en-us_topic_0112992293_p65877659163928"></a>This parameter indicates the total number of grants.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992293_section122445141020"></a>

The following example describes how to query the list of grants that can be retired.

-   Example request

    ```
    {
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
          "creation_date":"1497341531000"
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


## Status Codes<a name="en-us_topic_0112992293_section3454223421"></a>

[Table 4](#en-us_topic_0112992293_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992293_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992293_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992293_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992293_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992293_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992293_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992293_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992293_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992293_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992293_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992293_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992293_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992293_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992293_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992293_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992293_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992293_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992293_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992293_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992293_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992293_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

