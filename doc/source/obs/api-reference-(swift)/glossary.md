# Glossary<a name="obs_03_0078"></a>

<a name="table66613088"></a>
<table><tbody><tr id="row40200758223939"><td class="cell-norowborder" style="border:none" colspan="2" valign="top"><p id="p35035946223939"><a name="p35035946223939"></a><a name="p35035946223939"></a><strong id="b55253677223953"><a name="b55253677223953"></a><a name="b55253677223953"></a>A</strong></p>
</td>
</tr>
<tr id="row53563666223940"><td class="nocellnorowborder" style="border:none" valign="top" width="16%"><p id="p43689696223940"><a name="p43689696223940"></a><a name="p43689696223940"></a><strong id="b27521046223953"><a name="b27521046223953"></a><a name="b27521046223953"></a>ACL</strong></p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="84%"><p id="p49204527223940"><a name="p49204527223940"></a><a name="p49204527223940"></a>Access control list. An ACL describes a user's permission to access a container or object.</p>
</td>
</tr>
<tr id="row12835456223939"><td class="nocellnorowborder" style="border:none" valign="top" width="16%"><p id="p3647381215622"><a name="p3647381215622"></a><a name="p3647381215622"></a><strong id="b1822290410852"><a name="b1822290410852"></a><a name="b1822290410852"></a>Account</strong></p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="84%"><p id="p185972215622"><a name="p185972215622"></a><a name="p185972215622"></a>A logical concept at the top layer of OBS APIs, corresponding to the tenant in IAM. Multiple containers can be stored in an account.</p>
</td>
</tr>
<tr id="row4703049"><td class="cell-norowborder" style="border:none" colspan="2" valign="top"><p id="p24686674"><a name="p24686674"></a><a name="p24686674"></a><strong id="b1024960710855"><a name="b1024960710855"></a><a name="b1024960710855"></a>C</strong></p>
</td>
</tr>
<tr id="row15198020"><td class="nocellnorowborder" style="border:none" valign="top" width="16%"><p id="p19868667"><a name="p19868667"></a><a name="p19868667"></a><strong id="b155453715639"><a name="b155453715639"></a><a name="b155453715639"></a>Containe</strong></p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="84%"><p id="p38732155"><a name="p38732155"></a><a name="p38732155"></a>Objects uploaded by users are stored in containers. Only a user with the write permission of a container can upload an object to that container. A user can have a maximum of 10,000 containers, and each object stored in a container must be unique.</p>
</td>
</tr>
<tr id="row66407319"><td class="cell-norowborder" style="border:none" colspan="2" valign="top"><p id="p6691051"><a name="p6691051"></a><a name="p6691051"></a><strong id="b33907665"><a name="b33907665"></a><a name="b33907665"></a>K</strong></p>
</td>
</tr>
<tr id="row25147901"><td class="nocellnorowborder" style="border:none" valign="top" width="16%"><p id="p24077986"><a name="p24077986"></a><a name="p24077986"></a><strong id="b10877813"><a name="b10877813"></a><a name="b10877813"></a>Key</strong></p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="84%"><p id="p10710767"><a name="p10710767"></a><a name="p10710767"></a>A key is the unique identifier of an object in a container. An object is uniquely identified by its key and the name of the container to which the object belongs. When users send requests to OBS (compatible with OpenStack Swift), <strong id="b842352706171030"><a name="b842352706171030"></a><a name="b842352706171030"></a>/BucketName/ObjectKey</strong> is used to determine the target object.</p>
</td>
</tr>
<tr id="row1791515223536"><td class="cell-norowborder" style="border:none" colspan="2" valign="top"><p id="p18915022195312"><a name="p18915022195312"></a><a name="p18915022195312"></a><strong id="b5102234010918"><a name="b5102234010918"></a><a name="b5102234010918"></a>L</strong></p>
</td>
</tr>
<tr id="row2424998715543"><td class="nocellnorowborder" style="border:none" valign="top" width="16%"><p id="p4571790315917"><a name="p4571790315917"></a><a name="p4571790315917"></a><strong id="b520445910921"><a name="b520445910921"></a><a name="b520445910921"></a>Large Object</strong></p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="84%"><p id="p1425350215931"><a name="p1425350215931"></a><a name="p1425350215931"></a>A large object contains multiple segment objects, which are normal objects in OBS. Large objects can be classified into dynamic large objects and static large objects. A dynamic large object specifies the same prefix for all the segment objects to form a large object. A static large object specifies the names for all the segment objects to form a large object.</p>
</td>
</tr>
<tr id="row7175805"><td class="cell-norowborder" style="border:none" colspan="2" valign="top"><p id="p56330311"><a name="p56330311"></a><a name="p56330311"></a><strong id="b30727819"><a name="b30727819"></a><a name="b30727819"></a>O</strong></p>
</td>
</tr>
<tr id="row32923164"><td class="row-nocellborder" style="border:none" valign="top" width="16%"><p id="p38960454"><a name="p38960454"></a><a name="p38960454"></a><strong id="b48072900"><a name="b48072900"></a><a name="b48072900"></a>Object</strong></p>
</td>
<td class="cellrowborder" style="border:none" valign="top" width="84%"><p id="p33211345"><a name="p33211345"></a><a name="p33211345"></a>Fundamental entities stored in OBS (compatible with OpenStack Swift). The data uploaded by users is stored in the OBS as objects. An object consists of object data and metadata. In a single upload operation, the object can be of any data type and with a size ranging from 0 bytes to 5 GB (configurable, 5 GB by default). An object uploaded in segments can be of any data type and with a size ranging from 0 bytes to 5 TB. Object metadata contains multiple key pairs that describe properties including the data type and MD5 value. OBS (compatible with OpenStack Swift) automatically generates metadata on the server for the uploaded data.</p>
</td>
</tr>
</tbody>
</table>

