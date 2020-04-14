# Object Metadata Overview<a name="en-us_topic_0049066876"></a>

Object metadata is a set of name-value pairs that are part of object management.

Currently, only the metadata defined by the system is supported.

The metadata defined by the system is classified into the following types: system-controlled and user-controlled. For example, metadata such as  **Last-Modified**  is controlled by the system and cannot be modified. Users can modify the metadata such as  **ContentLanguage**  through the API. The metadata that can be modified by users is described as follows:

**Table  1**  OBS metadata

<a name="table63362710151941"></a>
<table><thead align="left"><tr id="r40d16ee062c8406e9b4bfa133383394b"><th class="cellrowborder" valign="top" width="34.589999999999996%" id="mcps1.2.3.1.1"><p id="a5bcb1f27f2e6434482cec614651aa348"><a name="a5bcb1f27f2e6434482cec614651aa348"></a><a name="a5bcb1f27f2e6434482cec614651aa348"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="65.41%" id="mcps1.2.3.1.2"><p id="a1298648fc238467db505e62d55dce601"><a name="a1298648fc238467db505e62d55dce601"></a><a name="a1298648fc238467db505e62d55dce601"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="raeaa496cd5104fc7993613258270efa7"><td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.3.1.1 "><p id="a0372510a577b45d3bd87af2da191354b"><a name="a0372510a577b45d3bd87af2da191354b"></a><a name="a0372510a577b45d3bd87af2da191354b"></a>ContentDisposition</p>
</td>
<td class="cellrowborder" valign="top" width="65.41%" headers="mcps1.2.3.1.2 "><p id="ad2074dcb13754e11b486bc520171189d"><a name="ad2074dcb13754e11b486bc520171189d"></a><a name="ad2074dcb13754e11b486bc520171189d"></a>Provides a default file name for the object that is being requested. When an object is being downloaded or accessed, the file with the default file name is directly displayed in the browser or a download dialog box is displayed if the file is being accessed.</p>
<p id="ac05b69907c674bcab5c4494f2ebb3afe"><a name="ac05b69907c674bcab5c4494f2ebb3afe"></a><a name="ac05b69907c674bcab5c4494f2ebb3afe"></a>For example, select <strong id="b9579115015416"><a name="b9579115015416"></a><a name="b9579115015416"></a>ContentDisposition</strong> as the metadata name and enter <strong id="b1758125011547"><a name="b1758125011547"></a><a name="b1758125011547"></a>attachment;filename="testfile.xls"</strong> as the metadata value for an object. If you access the object through a link, a dialog box is directly displayed for downloading objects, and the object name is changed to <strong id="b165831750105419"><a name="b165831750105419"></a><a name="b165831750105419"></a>testfile.xls</strong>. For details, see the definition about ContentDisposition in HTTP.</p>
</td>
</tr>
<tr id="r01c36a4b317a461293129ce020122bbe"><td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0047496338_p746994151941"><a name="en-us_topic_0047496338_p746994151941"></a><a name="en-us_topic_0047496338_p746994151941"></a>ContentLanguage</p>
</td>
<td class="cellrowborder" valign="top" width="65.41%" headers="mcps1.2.3.1.2 "><p id="p1366173895810"><a name="p1366173895810"></a><a name="p1366173895810"></a>Indicates the language or languages intended for the audience. Therefore, a user can differentiate according to the user's preferred language. For details, see the definition about ContentLanguage in HTTP.</p>
</td>
</tr>
<tr id="r168517bc0acb475fb3e6f23add45cf70"><td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.2.3.1.1 "><p id="a4aa323a101b640fe87e364b6212b51ce"><a name="a4aa323a101b640fe87e364b6212b51ce"></a><a name="a4aa323a101b640fe87e364b6212b51ce"></a>WebsiteRedirectLocation</p>
</td>
<td class="cellrowborder" valign="top" width="65.41%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0047496338_p297677011524"><a name="en-us_topic_0047496338_p297677011524"></a><a name="en-us_topic_0047496338_p297677011524"></a>Redirects an object to another object or an external URL. The redirection function is implemented using static website hosting.</p>
<p id="p293004410328"><a name="p293004410328"></a><a name="p293004410328"></a>For example, you can perform the following operations to implement object redirection:</p>
<a name="ol64035022103214"></a><a name="ol64035022103214"></a><ol id="ol64035022103214"><li>Set metadata of object <strong id="b3403178165515"><a name="b3403178165515"></a><a name="b3403178165515"></a>testobject.html</strong> in the root directory of bucket <strong id="b144046825515"><a name="b144046825515"></a><a name="b144046825515"></a>testbucket</strong>. Select <strong id="b18405585550"><a name="b18405585550"></a><a name="b18405585550"></a>WebsiteRedirectLocation</strong> for <strong id="b54061586550"><a name="b54061586550"></a><a name="b54061586550"></a>Name</strong> and enter <strong id="b18407128155519"><a name="b18407128155519"></a><a name="b18407128155519"></a>http://www.example.com</strong> for <strong id="b34091884557"><a name="b34091884557"></a><a name="b34091884557"></a>Value</strong>.<div class="note" id="note66951730103627"><a name="note66951730103627"></a><a name="note66951730103627"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p65694662103627"><a name="p65694662103627"></a><a name="p65694662103627"></a>OBS only supports redirection for objects in the root directory of a bucket. It does not support redirection for objects in folders in a bucket.</p>
</div></div>
</li><li>Configure static website hosting for bucket <strong id="b20224317114715"><a name="b20224317114715"></a><a name="b20224317114715"></a>testbucket</strong>, and set the object <strong id="b4226191704715"><a name="b4226191704715"></a><a name="b4226191704715"></a>testobject.html</strong> in the bucket as the default home page of the hosted static website.</li><li>If you access object <strong id="b537162135512"><a name="b537162135512"></a><a name="b537162135512"></a>testobject.html</strong> through the URL link provided on the <strong id="b1337312105510"><a name="b1337312105510"></a><a name="b1337312105510"></a>Configure Static Website Hosting</strong> page, the access request is redirected to <strong id="b1437682125516"><a name="b1437682125516"></a><a name="b1437682125516"></a>http://www.example.com</strong>.</li></ol>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   When versioning is enabled for a bucket, you can set metadata for objects which are  **Latest Version**, but cannot set metadata for objects which are  **Historical Version**.  
>-   You cannot set object metadata for a  **Cold**  object.  

