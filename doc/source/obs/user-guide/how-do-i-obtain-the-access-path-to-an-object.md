# How Do I Obtain the Access Path to an Object?<a name="obs_faq_0031"></a>

Format of an object access path is as follows:  **https://_Bucket name_._Domain name_/_Object name_** 

You can combine path manually or use the following tools to obtain the path:

**Table  1**  How to obtain an object URL

<a name="table183872112467"></a>
<table><thead align="left"><tr id="row138391521154614"><th class="cellrowborder" valign="top" width="23.1%" id="mcps1.2.3.1.1"><p id="p783982111460"><a name="p783982111460"></a><a name="p783982111460"></a>Tool</p>
</th>
<th class="cellrowborder" valign="top" width="76.9%" id="mcps1.2.3.1.2"><p id="p7101132916461"><a name="p7101132916461"></a><a name="p7101132916461"></a>Object URL</p>
</th>
</tr>
</thead>
<tbody><tr id="row12839921174611"><td class="cellrowborder" valign="top" width="23.1%" headers="mcps1.2.3.1.1 "><p id="p88397218466"><a name="p88397218466"></a><a name="p88397218466"></a>OBS Console</p>
</td>
<td class="cellrowborder" valign="top" width="76.9%" headers="mcps1.2.3.1.2 "><p id="p16862193904619"><a name="p16862193904619"></a><a name="p16862193904619"></a>Click the object and copy the URL for the detailed information of the object.</p>
</td>
</tr>
<tr id="row5839182144619"><td class="cellrowborder" valign="top" width="23.1%" headers="mcps1.2.3.1.1 "><p id="p17839162112463"><a name="p17839162112463"></a><a name="p17839162112463"></a>OBS Browser</p>
</td>
<td class="cellrowborder" valign="top" width="76.9%" headers="mcps1.2.3.1.2 "><p id="p1486233920469"><a name="p1486233920469"></a><a name="p1486233920469"></a>Click the <strong id="b185215547347"><a name="b185215547347"></a><a name="b185215547347"></a>Attribute</strong> button of the object and then you can copy the URL displayed in the detailed information about the object.</p>
</td>
</tr>
<tr id="row1577903941316"><td class="cellrowborder" valign="top" width="23.1%" headers="mcps1.2.3.1.1 "><p id="p1588131810149"><a name="p1588131810149"></a><a name="p1588131810149"></a>SDK</p>
</td>
<td class="cellrowborder" valign="top" width="76.9%" headers="mcps1.2.3.1.2 "><p id="p777943971320"><a name="p777943971320"></a><a name="p777943971320"></a>You can get the URL of an object by calling the <strong id="b538723103814"><a name="b538723103814"></a><a name="b538723103814"></a>getObjectUrl</strong> interface.</p>
</td>
</tr>
<tr id="row377914398139"><td class="cellrowborder" valign="top" width="23.1%" headers="mcps1.2.3.1.1 "><p id="p16881161812146"><a name="p16881161812146"></a><a name="p16881161812146"></a>API</p>
</td>
<td class="cellrowborder" valign="top" width="76.9%" headers="mcps1.2.3.1.2 "><p id="p1385333913311"><a name="p1385333913311"></a><a name="p1385333913311"></a>Not supported</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>If the object access path is user-assembled, you need to escape the object name by referring to the URL encoding rules.  

