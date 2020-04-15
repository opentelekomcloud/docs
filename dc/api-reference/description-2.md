# Description<a name="en-dc_topic_0055025335"></a>

## Object<a name="en-us_topic_0070658768_section23215317204921"></a>

Used to manage Direct Connect endpoint groups, including the APIs used to create, delete, query, and update a Direct Connect endpoint group, and the API to query the Direct Connect endpoint group list.

## Object Models<a name="en-us_topic_0070658768_section51721924204921"></a>

**Table  1**  Direct Connect endpoint group objects

<a name="en-us_topic_0070658768_table49902238182444"></a>
<table><thead align="left"><tr id="en-us_topic_0070658768_row27727643182444"><th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.7.1.1"><p id="en-us_topic_0070658768_p31346634182444"><a name="en-us_topic_0070658768_p31346634182444"></a><a name="en-us_topic_0070658768_p31346634182444"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.7.1.2"><p id="en-us_topic_0070658768_p56049421182444"><a name="en-us_topic_0070658768_p56049421182444"></a><a name="en-us_topic_0070658768_p56049421182444"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="10.1989801019898%" id="mcps1.2.7.1.3"><p id="en-us_topic_0070658768_p43709261182444"><a name="en-us_topic_0070658768_p43709261182444"></a><a name="en-us_topic_0070658768_p43709261182444"></a>CRUD</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.7.1.4"><p id="en-us_topic_0070658768_p50789233182444"><a name="en-us_topic_0070658768_p50789233182444"></a><a name="en-us_topic_0070658768_p50789233182444"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="19.928007199280074%" id="mcps1.2.7.1.5"><p id="en-us_topic_0070658768_p20287202182444"><a name="en-us_topic_0070658768_p20287202182444"></a><a name="en-us_topic_0070658768_p20287202182444"></a>Constraints</p>
</th>
<th class="cellrowborder" valign="top" width="24.967503249675033%" id="mcps1.2.7.1.6"><p id="en-us_topic_0070658768_p32650631182444"><a name="en-us_topic_0070658768_p32650631182444"></a><a name="en-us_topic_0070658768_p32650631182444"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658768_row27455432182444"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0070658768_p4494938144931"><a name="en-us_topic_0070658768_p4494938144931"></a><a name="en-us_topic_0070658768_p4494938144931"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0070658768_p42554614144931"><a name="en-us_topic_0070658768_p42554614144931"></a><a name="en-us_topic_0070658768_p42554614144931"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.1989801019898%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0070658768_p5312449144931"><a name="en-us_topic_0070658768_p5312449144931"></a><a name="en-us_topic_0070658768_p5312449144931"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0070658768_p1836529015518"><a name="en-us_topic_0070658768_p1836529015518"></a><a name="en-us_topic_0070658768_p1836529015518"></a>Automatically generated</p>
</td>
<td class="cellrowborder" valign="top" width="19.928007199280074%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0070658768_p19966830144931"><a name="en-us_topic_0070658768_p19966830144931"></a><a name="en-us_topic_0070658768_p19966830144931"></a>uuid</p>
</td>
<td class="cellrowborder" valign="top" width="24.967503249675033%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0070658768_p5002125015621"><a name="en-us_topic_0070658768_p5002125015621"></a><a name="en-us_topic_0070658768_p5002125015621"></a>Specifies the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658768_row39593523182444"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0070658768_p54924320144931"><a name="en-us_topic_0070658768_p54924320144931"></a><a name="en-us_topic_0070658768_p54924320144931"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0070658768_p22360669144931"><a name="en-us_topic_0070658768_p22360669144931"></a><a name="en-us_topic_0070658768_p22360669144931"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.1989801019898%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0070658768_p48980642144931"><a name="en-us_topic_0070658768_p48980642144931"></a><a name="en-us_topic_0070658768_p48980642144931"></a>CR</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0070658768_p66009631144931"><a name="en-us_topic_0070658768_p66009631144931"></a><a name="en-us_topic_0070658768_p66009631144931"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="19.928007199280074%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0070658768_p55755184144931"><a name="en-us_topic_0070658768_p55755184144931"></a><a name="en-us_topic_0070658768_p55755184144931"></a>The value can contain 0 to 255 characters.</p>
</td>
<td class="cellrowborder" valign="top" width="24.967503249675033%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0070658768_p13314730144931"><a name="en-us_topic_0070658768_p13314730144931"></a><a name="en-us_topic_0070658768_p13314730144931"></a>Specifies the tenant ID.</p>
</td>
</tr>
<tr id="en-us_topic_0070658768_row64801111182444"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0070658768_p18813514144931"><a name="en-us_topic_0070658768_p18813514144931"></a><a name="en-us_topic_0070658768_p18813514144931"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0070658768_p46641892144931"><a name="en-us_topic_0070658768_p46641892144931"></a><a name="en-us_topic_0070658768_p46641892144931"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.1989801019898%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0070658768_p27661266144931"><a name="en-us_topic_0070658768_p27661266144931"></a><a name="en-us_topic_0070658768_p27661266144931"></a>CRU</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0070658768_p45271865144931"><a name="en-us_topic_0070658768_p45271865144931"></a><a name="en-us_topic_0070658768_p45271865144931"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.928007199280074%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0070658768_p29489597144931"><a name="en-us_topic_0070658768_p29489597144931"></a><a name="en-us_topic_0070658768_p29489597144931"></a>length  &lt;0,64&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="24.967503249675033%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0070658768_p56655190144931"><a name="en-us_topic_0070658768_p56655190144931"></a><a name="en-us_topic_0070658768_p56655190144931"></a>Specifies the name of the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658768_row20716483182444"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0070658768_p19305467144931"><a name="en-us_topic_0070658768_p19305467144931"></a><a name="en-us_topic_0070658768_p19305467144931"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0070658768_p36212713144931"><a name="en-us_topic_0070658768_p36212713144931"></a><a name="en-us_topic_0070658768_p36212713144931"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.1989801019898%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0070658768_p47865666144931"><a name="en-us_topic_0070658768_p47865666144931"></a><a name="en-us_topic_0070658768_p47865666144931"></a>CRU</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0070658768_p22775300144931"><a name="en-us_topic_0070658768_p22775300144931"></a><a name="en-us_topic_0070658768_p22775300144931"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.928007199280074%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0070658768_p42972714144931"><a name="en-us_topic_0070658768_p42972714144931"></a><a name="en-us_topic_0070658768_p42972714144931"></a>length  &lt;0,128&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="24.967503249675033%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0070658768_p46658170144931"><a name="en-us_topic_0070658768_p46658170144931"></a><a name="en-us_topic_0070658768_p46658170144931"></a>Provides supplementary information about the Direct Connect endpoint group.</p>
</td>
</tr>
<tr id="en-us_topic_0070658768_row48951951182444"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0070658768_p43662562144931"><a name="en-us_topic_0070658768_p43662562144931"></a><a name="en-us_topic_0070658768_p43662562144931"></a>endpoints</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0070658768_p34314890144931"><a name="en-us_topic_0070658768_p34314890144931"></a><a name="en-us_topic_0070658768_p34314890144931"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="10.1989801019898%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0070658768_p29978928144931"><a name="en-us_topic_0070658768_p29978928144931"></a><a name="en-us_topic_0070658768_p29978928144931"></a>CR</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0070658768_p40916745144931"><a name="en-us_topic_0070658768_p40916745144931"></a><a name="en-us_topic_0070658768_p40916745144931"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="19.928007199280074%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0070658768_p44072253144931"><a name="en-us_topic_0070658768_p44072253144931"></a><a name="en-us_topic_0070658768_p44072253144931"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="24.967503249675033%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0070658768_p58632544144931"><a name="en-us_topic_0070658768_p58632544144931"></a><a name="en-us_topic_0070658768_p58632544144931"></a>Specifies the list of the Direct Connect endpoints.</p>
</td>
</tr>
<tr id="en-us_topic_0070658768_row4783956182444"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0070658768_p18394572144931"><a name="en-us_topic_0070658768_p18394572144931"></a><a name="en-us_topic_0070658768_p18394572144931"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0070658768_p3590299144931"><a name="en-us_topic_0070658768_p3590299144931"></a><a name="en-us_topic_0070658768_p3590299144931"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10.1989801019898%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0070658768_p22599112144931"><a name="en-us_topic_0070658768_p22599112144931"></a><a name="en-us_topic_0070658768_p22599112144931"></a>CR</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0070658768_p62067315144931"><a name="en-us_topic_0070658768_p62067315144931"></a><a name="en-us_topic_0070658768_p62067315144931"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="19.928007199280074%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0070658768_p58519784144931"><a name="en-us_topic_0070658768_p58519784144931"></a><a name="en-us_topic_0070658768_p58519784144931"></a>Only <strong id="b842352706212540"><a name="b842352706212540"></a><a name="b842352706212540"></a>cidr</strong> is supported.</p>
</td>
<td class="cellrowborder" valign="top" width="24.967503249675033%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0070658768_p55417893144931"><a name="en-us_topic_0070658768_p55417893144931"></a><a name="en-us_topic_0070658768_p55417893144931"></a>Specifies the type of the Direct Connect endpoint.</p>
</td>
</tr>
</tbody>
</table>

