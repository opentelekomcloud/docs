# Deleting the Image with a Specified Tag<a name="EN-US_TOPIC_0198655149"></a>

## Function<a name="section14905762191056"></a>

Delete the image with a specified tag in an image repository.

## URI<a name="section10482810165331"></a>

DELETE /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}/tags/\{_tag_\}

For details about parameters, see  [Table 1](#table05962819187).

**Table  1**  Parameter description

<a name="table05962819187"></a>
<table><thead align="left"><tr id="row18599289181"><th class="cellrowborder" valign="top" width="19.02%" id="mcps1.2.5.1.1"><p id="p145942820183"><a name="p145942820183"></a><a name="p145942820183"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.400000000000002%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25.27%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="36.309999999999995%" id="mcps1.2.5.1.4"><p id="p205910283185"><a name="p205910283185"></a><a name="p205910283185"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row146018284188"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.2.5.1.1 "><p id="p0601928131816"><a name="p0601928131816"></a><a name="p0601928131816"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.5.1.2 "><p id="p660333115711"><a name="p660333115711"></a><a name="p660333115711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25.27%" headers="mcps1.2.5.1.3 "><p id="p10507114164313"><a name="p10507114164313"></a><a name="p10507114164313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.309999999999995%" headers="mcps1.2.5.1.4 "><p id="p11460935127"><a name="p11460935127"></a><a name="p11460935127"></a>Organization name.</p>
</td>
</tr>
<tr id="row1160152816186"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.2.5.1.1 "><p id="p206018288188"><a name="p206018288188"></a><a name="p206018288188"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.5.1.2 "><p id="p3603203112717"><a name="p3603203112717"></a><a name="p3603203112717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25.27%" headers="mcps1.2.5.1.3 "><p id="p18920840134520"><a name="p18920840134520"></a><a name="p18920840134520"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.309999999999995%" headers="mcps1.2.5.1.4 "><p id="p11611528111811"><a name="p11611528111811"></a><a name="p11611528111811"></a>Image repository name.</p>
</td>
</tr>
<tr id="row7611288187"><td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.2.5.1.1 "><p id="p761728131819"><a name="p761728131819"></a><a name="p761728131819"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.5.1.2 "><p id="p142711318125017"><a name="p142711318125017"></a><a name="p142711318125017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25.27%" headers="mcps1.2.5.1.3 "><p id="p923624264510"><a name="p923624264510"></a><a name="p923624264510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.309999999999995%" headers="mcps1.2.5.1.4 "><p id="p261202814184"><a name="p261202814184"></a><a name="p261202814184"></a>Tag name.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3270966102931"></a>

N/A

## Response<a name="section46271297104114"></a>

N/A

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 2](#table334923162011).

**Table  2**  Status code

<a name="table334923162011"></a>
<table><thead align="left"><tr id="row834914392012"><th class="cellrowborder" valign="top" width="20.87%" id="mcps1.2.3.1.1"><p id="p1434911342014"><a name="p1434911342014"></a><a name="p1434911342014"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="79.13%" id="mcps1.2.3.1.2"><p id="p4349430208"><a name="p4349430208"></a><a name="p4349430208"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5349837207"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.3.1.1 "><p id="p834920312011"><a name="p834920312011"></a><a name="p834920312011"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="79.13%" headers="mcps1.2.3.1.2 "><p id="p4349113182014"><a name="p4349113182014"></a><a name="p4349113182014"></a>The image with a specified tag is deleted successfully.</p>
</td>
</tr>
<tr id="row53501322011"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.3.1.1 "><p id="p23509352013"><a name="p23509352013"></a><a name="p23509352013"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="79.13%" headers="mcps1.2.3.1.2 "><p id="p83505352020"><a name="p83505352020"></a><a name="p83505352020"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row187384312201"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.3.1.1 "><p id="p11739731182020"><a name="p11739731182020"></a><a name="p11739731182020"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="79.13%" headers="mcps1.2.3.1.2 "><p id="p137391931122010"><a name="p137391931122010"></a><a name="p137391931122010"></a>The repository or the image with a specified tag does not exist.</p>
</td>
</tr>
<tr id="row0350123192020"><td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.3.1.1 "><p id="p335019311201"><a name="p335019311201"></a><a name="p335019311201"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="79.13%" headers="mcps1.2.3.1.2 "><p id="p43509342017"><a name="p43509342017"></a><a name="p43509342017"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

