# Querying the Stacks<a name="EN-US_TOPIC_0084581285"></a>

## Function<a name="en-us_topic_0057973120_section13428899"></a>

This API is used to query stacks of a specified tenant.

## URI<a name="en-us_topic_0057973120_section53751233"></a>

GET /v1/\{project\_id\}/stacks

For details about the parameters, see  [Table 1](#table7797142512383).

**Table  1**  Parameter description

<a name="table7797142512383"></a>
<table><thead align="left"><tr id="row208001025193812"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p43085863"><a name="p43085863"></a><a name="p43085863"></a><strong id="b7158827171219"><a name="b7158827171219"></a><a name="b7158827171219"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p12821133562718"><a name="p12821133562718"></a><a name="p12821133562718"></a><strong id="b14789173031217"><a name="b14789173031217"></a><a name="b14789173031217"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p294000"><a name="p294000"></a><a name="p294000"></a><strong id="b493320314127"><a name="b493320314127"></a><a name="b493320314127"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p23814038"><a name="p23814038"></a><a name="p23814038"></a><strong id="b045173771212"><a name="b045173771212"></a><a name="b045173771212"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row148005254389"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14468758"><a name="p14468758"></a><a name="p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1581811351277"><a name="p1581811351277"></a><a name="p1581811351277"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p31118786"><a name="p31118786"></a><a name="p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973120_section13999052"></a>

<a name="en-us_topic_0057973120_table137237981111"></a>
<table><thead align="left"><tr id="en-us_topic_0057973120_row105115351111"><th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.1"><p id="p17493122142817"><a name="p17493122142817"></a><a name="p17493122142817"></a><strong id="b128620912138"><a name="b128620912138"></a><a name="b128620912138"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.2"><p id="p1887419221879"><a name="p1887419221879"></a><a name="p1887419221879"></a><strong id="b17852182671318"><a name="b17852182671318"></a><a name="b17852182671318"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.3"><p id="p16493922112813"><a name="p16493922112813"></a><a name="p16493922112813"></a><strong id="b108912815139"><a name="b108912815139"></a><a name="b108912815139"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.4"><p id="p94935225284"><a name="p94935225284"></a><a name="p94935225284"></a><strong id="b7284157121415"><a name="b7284157121415"></a><a name="b7284157121415"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.6.1.5"><p id="p1549342213284"><a name="p1549342213284"></a><a name="p1549342213284"></a><strong id="b136331116191419"><a name="b136331116191419"></a><a name="b136331116191419"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973120_row196510691111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973120_p158588311110"><a name="en-us_topic_0057973120_p158588311110"></a><a name="en-us_topic_0057973120_p158588311110"></a>status/stack_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p122521523151110"><a name="p122521523151110"></a><a name="p122521523151110"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973120_p6134773511110"><a name="en-us_topic_0057973120_p6134773511110"></a><a name="en-us_topic_0057973120_p6134773511110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973120_p311060611110"><a name="en-us_topic_0057973120_p311060611110"></a><a name="en-us_topic_0057973120_p311060611110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973120_p5063255411110"><a name="en-us_topic_0057973120_p5063255411110"></a><a name="en-us_topic_0057973120_p5063255411110"></a>Specifies the stack status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row125834051111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973120_p125732811110"><a name="en-us_topic_0057973120_p125732811110"></a><a name="en-us_topic_0057973120_p125732811110"></a>name/stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p7252112321117"><a name="p7252112321117"></a><a name="p7252112321117"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973120_p3473471011110"><a name="en-us_topic_0057973120_p3473471011110"></a><a name="en-us_topic_0057973120_p3473471011110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973120_p6204812511110"><a name="en-us_topic_0057973120_p6204812511110"></a><a name="en-us_topic_0057973120_p6204812511110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="p1331445961114"><a name="p1331445961114"></a><a name="p1331445961114"></a>Specifies the stack name.</p>
<a name="ul45291469124"></a><a name="ul45291469124"></a><ul id="ul45291469124"><li>The value can contain only uppercase letters, lowercase letters, digits, hyphens (-), periods (.), and underscores (_).</li><li>The value must start with an uppercase letter or a lowercase letter.</li><li>The value can contain 1 to 255 characters.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0057973120_row331239521111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973120_p421736211110"><a name="en-us_topic_0057973120_p421736211110"></a><a name="en-us_topic_0057973120_p421736211110"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p12252423151111"><a name="p12252423151111"></a><a name="p12252423151111"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973120_p606203011110"><a name="en-us_topic_0057973120_p606203011110"></a><a name="en-us_topic_0057973120_p606203011110"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973120_p2126238211110"><a name="en-us_topic_0057973120_p2126238211110"></a><a name="en-us_topic_0057973120_p2126238211110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="p36478401709"><a name="p36478401709"></a><a name="p36478401709"></a>Specifies the number of returned stacks. This parameter is used to control the stack display mode and quantity. It can be used independently or together with the <strong id="b32794414297"><a name="b32794414297"></a><a name="b32794414297"></a>marker</strong> parameter.</p>
<p id="p112805411408"><a name="p112805411408"></a><a name="p112805411408"></a>For example, if the <strong id="b1473516129298"><a name="b1473516129298"></a><a name="b1473516129298"></a>limit</strong> and <strong id="b178861532919"><a name="b178861532919"></a><a name="b178861532919"></a>marker</strong> parameters are not used, the queried stack list is as follows:</p>
<pre class="screen" id="screen1861429839"><a name="screen1861429839"></a><a name="screen1861429839"></a>[stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8]</pre>
<p id="p3265269310"><a name="p3265269310"></a><a name="p3265269310"></a>If <strong id="b4417173911298"><a name="b4417173911298"></a><a name="b4417173911298"></a>limit</strong> is set to <strong id="b5297142162918"><a name="b5297142162918"></a><a name="b5297142162918"></a>3</strong>, only the first three data records in the stack list are returned.</p>
<pre class="screen" id="screen784917559412"><a name="screen784917559412"></a><a name="screen784917559412"></a>[stack1,stack2,stack3]</pre>
<p id="p191422261844"><a name="p191422261844"></a><a name="p191422261844"></a>If <strong id="b12947821718"><a name="b12947821718"></a><a name="b12947821718"></a>limit</strong> is set to <strong id="b294842110118"><a name="b294842110118"></a><a name="b294842110118"></a>3</strong> and <strong id="b1394915211412"><a name="b1394915211412"></a><a name="b1394915211412"></a>marker</strong> is set to <strong id="b15949721312"><a name="b15949721312"></a><a name="b15949721312"></a>stack3</strong>, three stacks are displayed in sequence from the next data record of <strong id="b199501621517"><a name="b199501621517"></a><a name="b199501621517"></a>stack3</strong>.</p>
<pre class="screen" id="screen18967192216620"><a name="screen18967192216620"></a><a name="screen18967192216620"></a>[stack4,stack5,stack6]</pre>
<p id="p10106115619"><a name="p10106115619"></a><a name="p10106115619"></a>If <strong id="b121121236111"><a name="b121121236111"></a><a name="b121121236111"></a>limit</strong> is set to <strong id="b171126231714"><a name="b171126231714"></a><a name="b171126231714"></a>3</strong> and <strong id="b911318231616"><a name="b911318231616"></a><a name="b911318231616"></a>marker</strong> is set to <strong id="b131133231116"><a name="b131133231116"></a><a name="b131133231116"></a>stack6</strong>, but fewer than three data records are available after <strong id="b15114123515"><a name="b15114123515"></a><a name="b15114123515"></a>stack6</strong>, all the remaining data records are displayed.</p>
<pre class="screen" id="screen15316133011149"><a name="screen15316133011149"></a><a name="screen15316133011149"></a>[stack7,stack8]</pre>
</td>
</tr>
<tr id="en-us_topic_0057973120_row195985261111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973120_p4977634711110"><a name="en-us_topic_0057973120_p4977634711110"></a><a name="en-us_topic_0057973120_p4977634711110"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p62522236118"><a name="p62522236118"></a><a name="p62522236118"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973120_p535232611110"><a name="en-us_topic_0057973120_p535232611110"></a><a name="en-us_topic_0057973120_p535232611110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973120_p3088527411110"><a name="en-us_topic_0057973120_p3088527411110"></a><a name="en-us_topic_0057973120_p3088527411110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973120_p1867922911110"><a name="en-us_topic_0057973120_p1867922911110"></a><a name="en-us_topic_0057973120_p1867922911110"></a>Specifies the stack from which the next data record starts to be queried. This parameter is used to control the stack display mode and quantity. This parameter must be used together with the <strong id="b645112813714"><a name="b645112813714"></a><a name="b645112813714"></a>limit</strong> parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row245624561111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973120_p6116810911110"><a name="en-us_topic_0057973120_p6116810911110"></a><a name="en-us_topic_0057973120_p6116810911110"></a>sort_keys</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p132525235111"><a name="p132525235111"></a><a name="p132525235111"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973120_p5566977711110"><a name="en-us_topic_0057973120_p5566977711110"></a><a name="en-us_topic_0057973120_p5566977711110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973120_p1295808211110"><a name="en-us_topic_0057973120_p1295808211110"></a><a name="en-us_topic_0057973120_p1295808211110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973120_p4297168711110"><a name="en-us_topic_0057973120_p4297168711110"></a><a name="en-us_topic_0057973120_p4297168711110"></a>Specifies the sorting keyword.</p>
<p id="en-us_topic_0057973120_p5120086411110"><a name="en-us_topic_0057973120_p5120086411110"></a><a name="en-us_topic_0057973120_p5120086411110"></a>stack_name, stack_status, creation_time, and updated_time</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row390213191111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973120_p1290219111110"><a name="en-us_topic_0057973120_p1290219111110"></a><a name="en-us_topic_0057973120_p1290219111110"></a>sort_dir</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p1252123111119"><a name="p1252123111119"></a><a name="p1252123111119"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973120_p3844451311110"><a name="en-us_topic_0057973120_p3844451311110"></a><a name="en-us_topic_0057973120_p3844451311110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973120_p2699786411110"><a name="en-us_topic_0057973120_p2699786411110"></a><a name="en-us_topic_0057973120_p2699786411110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="p178611743131319"><a name="p178611743131319"></a><a name="p178611743131319"></a>Specifies the sorting method.</p>
<p id="en-us_topic_0057973120_p3934340411110"><a name="en-us_topic_0057973120_p3934340411110"></a><a name="en-us_topic_0057973120_p3934340411110"></a>The value can be <strong id="b1571183510283"><a name="b1571183510283"></a><a name="b1571183510283"></a>asc</strong> (in the ascending order) or <strong id="b1942363772813"><a name="b1942363772813"></a><a name="b1942363772813"></a>desc</strong> (in the descending order).</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0057973120_section58882605"></a>

<a name="en-us_topic_0057973120_table12551541"></a>
<table><thead align="left"><tr id="en-us_topic_0057973120_row55718695"><th class="cellrowborder" valign="top" width="15.290000000000001%" id="mcps1.1.5.1.1"><p id="p171065246399"><a name="p171065246399"></a><a name="p171065246399"></a><strong id="b677145518280"><a name="b677145518280"></a><a name="b677145518280"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.2"><p id="p2011052493920"><a name="p2011052493920"></a><a name="p2011052493920"></a><strong id="b17768859202814"><a name="b17768859202814"></a><a name="b17768859202814"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.3"><p id="p511442413391"><a name="p511442413391"></a><a name="p511442413391"></a><strong id="b29835217295"><a name="b29835217295"></a><a name="b29835217295"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.59%" id="mcps1.1.5.1.4"><p id="p1211902483916"><a name="p1211902483916"></a><a name="p1211902483916"></a><strong id="b19199660296"><a name="b19199660296"></a><a name="b19199660296"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973120_row42407121"><td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p12424780"><a name="en-us_topic_0057973120_p12424780"></a><a name="en-us_topic_0057973120_p12424780"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.2 "><p id="p181782893219"><a name="p181782893219"></a><a name="p181782893219"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p66883099"><a name="en-us_topic_0057973120_p66883099"></a><a name="en-us_topic_0057973120_p66883099"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p62261975"><a name="en-us_topic_0057973120_p62261975"></a><a name="en-us_topic_0057973120_p62261975"></a>Specifies the stack list.</p>
</td>
</tr>
</tbody>
</table>

**stacks**  structure information

<a name="en-us_topic_0057973120_table10055187"></a>
<table><thead align="left"><tr id="en-us_topic_0057973120_row17111243"><th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.1"><p id="p122191431163912"><a name="p122191431163912"></a><a name="p122191431163912"></a><strong id="b18216182611295"><a name="b18216182611295"></a><a name="b18216182611295"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.2"><p id="p13221731143918"><a name="p13221731143918"></a><a name="p13221731143918"></a><strong id="b142511052162912"><a name="b142511052162912"></a><a name="b142511052162912"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.1.5.1.3"><p id="p112241831133912"><a name="p112241831133912"></a><a name="p112241831133912"></a><strong id="b1332611533292"><a name="b1332611533292"></a><a name="b1332611533292"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.18488151184882%" id="mcps1.1.5.1.4"><p id="p1230163153911"><a name="p1230163153911"></a><a name="p1230163153911"></a><strong id="b122194576292"><a name="b122194576292"></a><a name="b122194576292"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973120_row12734291"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p24844657"><a name="en-us_topic_0057973120_p24844657"></a><a name="en-us_topic_0057973120_p24844657"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p1321172513328"><a name="p1321172513328"></a><a name="p1321172513328"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p66260240"><a name="en-us_topic_0057973120_p66260240"></a><a name="en-us_topic_0057973120_p66260240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p2219504"><a name="en-us_topic_0057973120_p2219504"></a><a name="en-us_topic_0057973120_p2219504"></a>Specifies the stack UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row19975537"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p7405829"><a name="en-us_topic_0057973120_p7405829"></a><a name="en-us_topic_0057973120_p7405829"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p17219258327"><a name="p17219258327"></a><a name="p17219258327"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p63001277"><a name="en-us_topic_0057973120_p63001277"></a><a name="en-us_topic_0057973120_p63001277"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p27889339"><a name="en-us_topic_0057973120_p27889339"></a><a name="en-us_topic_0057973120_p27889339"></a>Specifies the stack name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row49677463"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p64451546"><a name="en-us_topic_0057973120_p64451546"></a><a name="en-us_topic_0057973120_p64451546"></a>stack_status</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p3211925173218"><a name="p3211925173218"></a><a name="p3211925173218"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p53192709"><a name="en-us_topic_0057973120_p53192709"></a><a name="en-us_topic_0057973120_p53192709"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p31274549"><a name="en-us_topic_0057973120_p31274549"></a><a name="en-us_topic_0057973120_p31274549"></a>Specifies the stack status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row13035492"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p49241952"><a name="en-us_topic_0057973120_p49241952"></a><a name="en-us_topic_0057973120_p49241952"></a>stack_status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p821142516326"><a name="p821142516326"></a><a name="p821142516326"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p29175209"><a name="en-us_topic_0057973120_p29175209"></a><a name="en-us_topic_0057973120_p29175209"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p24069824"><a name="en-us_topic_0057973120_p24069824"></a><a name="en-us_topic_0057973120_p24069824"></a>Describes the stack operation.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row15301827"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p31488466"><a name="en-us_topic_0057973120_p31488466"></a><a name="en-us_topic_0057973120_p31488466"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p521225183218"><a name="p521225183218"></a><a name="p521225183218"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p428978"><a name="en-us_topic_0057973120_p428978"></a><a name="en-us_topic_0057973120_p428978"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p63065860"><a name="en-us_topic_0057973120_p63065860"></a><a name="en-us_topic_0057973120_p63065860"></a>Describes the stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row30721828"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p5440112"><a name="en-us_topic_0057973120_p5440112"></a><a name="en-us_topic_0057973120_p5440112"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p92152513219"><a name="p92152513219"></a><a name="p92152513219"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p37995953"><a name="en-us_topic_0057973120_p37995953"></a><a name="en-us_topic_0057973120_p37995953"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p49133105"><a name="en-us_topic_0057973120_p49133105"></a><a name="en-us_topic_0057973120_p49133105"></a>Specifies the stack URL list.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row39544768"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p49009603"><a name="en-us_topic_0057973120_p49009603"></a><a name="en-us_topic_0057973120_p49009603"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p7211125163213"><a name="p7211125163213"></a><a name="p7211125163213"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p10354944"><a name="en-us_topic_0057973120_p10354944"></a><a name="en-us_topic_0057973120_p10354944"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p24619586"><a name="en-us_topic_0057973120_p24619586"></a><a name="en-us_topic_0057973120_p24619586"></a>Specifies the time when the stack was created.</p>
</td>
</tr>
<tr id="en-us_topic_0057973120_row20249688"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973120_p29611997"><a name="en-us_topic_0057973120_p29611997"></a><a name="en-us_topic_0057973120_p29611997"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p19211225143210"><a name="p19211225143210"></a><a name="p19211225143210"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973120_p49761534"><a name="en-us_topic_0057973120_p49761534"></a><a name="en-us_topic_0057973120_p49761534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973120_p806967"><a name="en-us_topic_0057973120_p806967"></a><a name="en-us_topic_0057973120_p806967"></a>Specifies the time when the stack was updated.</p>
</td>
</tr>
<tr id="row129035129374"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p13904912183716"><a name="p13904912183716"></a><a name="p13904912183716"></a>parent</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p2090491273715"><a name="p2090491273715"></a><a name="p2090491273715"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="p129046120378"><a name="p129046120378"></a><a name="p129046120378"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p6904912203719"><a name="p6904912203719"></a><a name="p6904912203719"></a>Specifies the UUID of the parent stack (for a nested stack).</p>
</td>
</tr>
<tr id="row149043128375"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p139051112163716"><a name="p139051112163716"></a><a name="p139051112163716"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p590591223717"><a name="p590591223717"></a><a name="p590591223717"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="p17905412143711"><a name="p17905412143711"></a><a name="p17905412143711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p9905812173715"><a name="p9905812173715"></a><a name="p9905812173715"></a>Specifies the stack tag.</p>
</td>
</tr>
<tr id="row8905101293710"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p7905412143714"><a name="p7905412143714"></a><a name="p7905412143714"></a>stack_user_project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p159051012203715"><a name="p159051012203715"></a><a name="p159051012203715"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="p12905131273715"><a name="p12905131273715"></a><a name="p12905131273715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.18488151184882%" headers="mcps1.1.5.1.4 "><p id="p109052012153720"><a name="p109052012153720"></a><a name="p109052012153720"></a>Specifies the project UUID of the stack user. This parameter may be left blank.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973120_section60181397"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/stacks
```

## Response Example<a name="en-us_topic_0057973120_section4761661"></a>

```
{
    "stacks": [
        {
            "description": "Hello world HOT template that just defines a single compute instance. Contains just base features to verify base HOT support.\n",
            "links": [
                {
                     "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306",
                     "rel": "self"
                 }
             ],
            "stack_status_reason": "Stack create completed successfully",
            "stack_name": "HeatStack",
            "creation_time": "2018-01-26T17:21:35Z",
            "updated_time": "2018-01-26T17:21:41Z",
            "stack_status": "CREATE_COMPLETE",
            "id": "c89c4bb3-96cb-4a55-aafa-076a7939a306"
        }
    ]
}
```

## Return Code<a name="en-us_topic_0057973120_section42854950"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0057973117_p13413377194057"></a><strong id="b14910172512114"><a name="b14910172512114"></a><a name="b14910172512114"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0057973117_p8637307194057"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0057973117_p28533244194057"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0057973117_p29491459194057"></a>Request was successful.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a><strong id="b1593185095118"><a name="b1593185095118"></a><a name="b1593185095118"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="b1246719253"><a name="b1246719253"></a><a name="b1246719253"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="b208697501"><a name="b208697501"></a><a name="b208697501"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p896118101840"><a name="p896118101840"></a><a name="p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1296211015416"><a name="p1296211015416"></a><a name="p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p9963110146"><a name="p9963110146"></a><a name="p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p18134027201912"><a name="p18134027201912"></a><a name="p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1713419274191"><a name="p1713419274191"></a><a name="p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p11134162718196"><a name="p11134162718196"></a><a name="p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p156541031121913"><a name="p156541031121913"></a><a name="p156541031121913"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p12654183112194"><a name="p12654183112194"></a><a name="p12654183112194"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p196546319198"><a name="p196546319198"></a><a name="p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

