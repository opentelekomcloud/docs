# Querying a List of Streams with Specified Tags<a name="dis_02_0420"></a>

## Function<a name="en-us_topic_0112442490_en-us_topic_0110707086_section1471126172111"></a>

This API is used to filter streams by tag.

By default, streams and tags are sorted in descending order of creation time.

## URI<a name="en-us_topic_0112442490_en-us_topic_0110707086_section315415176217"></a>

POST /v2/\{project\_id\}/stream/resource\_instances/action

The following table describes URI parameters.

**Table  1**  URI parameter description

<a name="en-us_topic_0112442490_en-us_topic_0110707086_table2882182815226"></a>
<table><thead align="left"><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row12884528142211"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p7884228122214"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p7884228122214"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p7884228122214"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p388412816227"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p388412816227"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p388412816227"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p19884182820220"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p19884182820220"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p19884182820220"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row78841828112220"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p18884132810221"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p18884132810221"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p18884132810221"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p29494508194812"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p29494508194812"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p29494508194812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p40820562194812"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p40820562194812"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p40820562194812"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0112442490_en-us_topic_0110707086_section158621312122315"></a>

**Request parameters**

**Table  2**  Parameter description

<a name="en-us_topic_0112442490_en-us_topic_0110707086_table1759719014243"></a>
<table><thead align="left"><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row2597110112415"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p20597120152420"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p20597120152420"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p20597120152420"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p359718019240"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p359718019240"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p359718019240"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p35978012418"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p35978012418"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p35978012418"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p3597160132417"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p3597160132417"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p3597160132417"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row75973022419"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_p1575715772816"><a name="en-us_topic_0112442490_p1575715772816"></a><a name="en-us_topic_0112442490_p1575715772816"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_p7758165732819"><a name="en-us_topic_0112442490_p7758165732819"></a><a name="en-us_topic_0112442490_p7758165732819"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_p275835732812"><a name="en-us_topic_0112442490_p275835732812"></a><a name="en-us_topic_0112442490_p275835732812"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_p4758257172813"><a name="en-us_topic_0112442490_p4758257172813"></a><a name="en-us_topic_0112442490_p4758257172813"></a>The return result contains resources corresponding to all tags in this parameter. This parameter contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string.</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_row17786165614171"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_p16656934491"><a name="en-us_topic_0112442490_p16656934491"></a><a name="en-us_topic_0112442490_p16656934491"></a>tags_any</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_p5656734297"><a name="en-us_topic_0112442490_p5656734297"></a><a name="en-us_topic_0112442490_p5656734297"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_p1552517316103"><a name="en-us_topic_0112442490_p1552517316103"></a><a name="en-us_topic_0112442490_p1552517316103"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_p8656153420912"><a name="en-us_topic_0112442490_p8656153420912"></a><a name="en-us_topic_0112442490_p8656153420912"></a>The return result contains resources corresponding to any tag in this parameter. This parameter contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string. Keys must be unique and values of a key must be unique.</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_row1829235651717"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_p89561301799"><a name="en-us_topic_0112442490_p89561301799"></a><a name="en-us_topic_0112442490_p89561301799"></a>not_tags</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_p49567301595"><a name="en-us_topic_0112442490_p49567301595"></a><a name="en-us_topic_0112442490_p49567301595"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_p555763231010"><a name="en-us_topic_0112442490_p555763231010"></a><a name="en-us_topic_0112442490_p555763231010"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_p16956230793"><a name="en-us_topic_0112442490_p16956230793"></a><a name="en-us_topic_0112442490_p16956230793"></a>The return result does not contain resources corresponding to all tags in this parameter. This parameter contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string. Keys must be unique and values of a key must be unique.</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_row15171115419176"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_p1384616271395"><a name="en-us_topic_0112442490_p1384616271395"></a><a name="en-us_topic_0112442490_p1384616271395"></a>not_tags_any</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_p6846102716912"><a name="en-us_topic_0112442490_p6846102716912"></a><a name="en-us_topic_0112442490_p6846102716912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_p143919332103"><a name="en-us_topic_0112442490_p143919332103"></a><a name="en-us_topic_0112442490_p143919332103"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_p784672718910"><a name="en-us_topic_0112442490_p784672718910"></a><a name="en-us_topic_0112442490_p784672718910"></a>The return result does not contain resources corresponding to any tag in this parameter. This parameter contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string. Keys must be unique and values of a key must be unique.</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_en-us_topic_0110707086_row145981052413"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1278101811292"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1278101811292"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1278101811292"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p7278118172916"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p7278118172916"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p7278118172916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p19278171810294"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p19278171810294"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p19278171810294"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1027811182298"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1027811182298"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1027811182298"></a>Number of records. This parameter is not available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> when <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The maximum value is <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_en-us_topic_0110707086_row175983016249"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p027813183295"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p027813183295"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p027813183295"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p9278218202913"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p9278218202913"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p9278218202913"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1527871812913"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1527871812913"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1527871812913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p32781718132918"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p32781718132918"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p32781718132918"></a>Index position. The query starts from the next piece of data specified by the <strong id="b8423527069263"><a name="b8423527069263"></a><a name="b8423527069263"></a>offset</strong> parameter. This parameter is not required when you query data on the first page. The value in the response body returned for querying data on the previous page will be included in this parameter for querying data on subsequent pages. This parameter is not available when <strong id="b84235270621521"><a name="b84235270621521"></a><a name="b84235270621521"></a>action</strong> is set to <strong id="b84235270621525"><a name="b84235270621525"></a><a name="b84235270621525"></a>count</strong>. If <strong id="b84235270621528"><a name="b84235270621528"></a><a name="b84235270621528"></a>action</strong> is set to <strong id="b84235270621532"><a name="b84235270621532"></a><a name="b84235270621532"></a>filter</strong>, the value must be a number, and the default value is <strong id="b84235270621539"><a name="b84235270621539"></a><a name="b84235270621539"></a>0</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_en-us_topic_0110707086_row4598130152410"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p928051819292"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p928051819292"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p928051819292"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p16280101811291"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p16280101811291"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p16280101811291"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p628011814294"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p628011814294"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p628011814294"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p228061852911"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p228061852911"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p228061852911"></a>Operation to be performed. The value can be <strong id="b84235270616546"><a name="b84235270616546"></a><a name="b84235270616546"></a>filter</strong> or <strong id="b84235270616552"><a name="b84235270616552"></a><a name="b84235270616552"></a>count</strong>.</p>
<p id="en-us_topic_0112442490_en-us_topic_0110707086_p1428010183299"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1428010183299"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1428010183299"></a>The value <strong id="b842352706112921"><a name="b842352706112921"></a><a name="b842352706112921"></a>filter</strong> indicates pagination query. The value <strong id="b84235270611312"><a name="b84235270611312"></a><a name="b84235270611312"></a>count</strong> indicates that the total number of query results meeting the search criteria will be returned.</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_en-us_topic_0110707086_row116791713182912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1028011862914"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1028011862914"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1028011862914"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1128051892917"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1128051892917"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1128051892917"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p428031819290"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p428031819290"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p428031819290"></a>List&lt;match&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p132801218172917"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p132801218172917"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p132801218172917"></a>Search field. <strong id="b139191241144216"><a name="b139191241144216"></a><a name="b139191241144216"></a>key</strong> indicates the field to be matched, for example, <strong id="b1815994217155439"><a name="b1815994217155439"></a><a name="b1815994217155439"></a>resource_name</strong>. <strong id="b383113710436"><a name="b383113710436"></a><a name="b383113710436"></a>value</strong> indicates the matched value. This field is a fixed dictionary value.</p>
<p id="en-us_topic_0112442490_en-us_topic_0110707086_p152805187296"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p152805187296"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p152805187296"></a>Determine whether fuzzy match is required based on different fields. For example, if <strong id="b8423527062245"><a name="b8423527062245"></a><a name="b8423527062245"></a>key</strong> is <strong id="b842352706123028"><a name="b842352706123028"></a><a name="b842352706123028"></a>resource_name</strong>, fuzzy search is used by default. If <strong id="b842352706123110"><a name="b842352706123110"></a><a name="b842352706123110"></a>value</strong> is an empty string, exact match is used. If <strong id="b84235270622448"><a name="b84235270622448"></a><a name="b84235270622448"></a>key</strong> is <strong id="b842352706123558"><a name="b842352706123558"></a><a name="b842352706123558"></a>resource_id</strong>, exact match is used. Only <strong id="b842352706123249"><a name="b842352706123249"></a><a name="b842352706123249"></a>resource_name</strong> is queried at the first phase, and other keys will be queried later.</p>
<p id="en-us_topic_0112442490_en-us_topic_0110707086_p32803185293"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p32803185293"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p32803185293"></a></p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  field description

<a name="en-us_topic_0112442490_en-us_topic_0110707086_table311544113295"></a>
<table><thead align="left"><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row17115144111296"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p965615311307"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p965615311307"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p965615311307"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p26567318304"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p26567318304"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p26567318304"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1865619317303"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1865619317303"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1865619317303"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p56560393020"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p56560393020"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p56560393020"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row31150413297"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p156565383013"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p156565383013"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p156565383013"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1965613173011"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1965613173011"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1965613173011"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p665653123011"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p665653123011"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p665653123011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p2065615393019"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p2065615393019"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p2065615393019"></a>Key. It contains a maximum of 127 Unicode characters. It cannot be left empty. (This parameter is not verified in the search process.)</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_en-us_topic_0110707086_row2011514114292"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p56577317309"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p56577317309"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p56577317309"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p765720363016"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p765720363016"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p765720363016"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1465712303010"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1465712303010"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1465712303010"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p265773143019"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p265773143019"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p265773143019"></a>List of values. A value contains a maximum of 255 Unicode characters.</p>
<p id="en-us_topic_0112442490_en-us_topic_0110707086_p176579314309"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p176579314309"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p176579314309"></a>If the values are null, it indicates <strong id="b842352706175623"><a name="b842352706175623"></a><a name="b842352706175623"></a>any_value</strong>. The relationship between values is OR. By default, only the first value is used for search.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **match**  field description

<a name="en-us_topic_0112442490_en-us_topic_0110707086_table9181927193012"></a>
<table><thead align="left"><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row218216277305"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p156795563011"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p156795563011"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p156795563011"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p056719556302"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p056719556302"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p056719556302"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p175678554306"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p175678554306"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p175678554306"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p18567155513307"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p18567155513307"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p18567155513307"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row181821127133011"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p856713553306"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p856713553306"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p856713553306"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p356905583013"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p356905583013"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p356905583013"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p175691655153016"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p175691655153016"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p175691655153016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p12569355173015"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p12569355173015"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p12569355173015"></a>Key. Currently, only <strong id="b842352706185659"><a name="b842352706185659"></a><a name="b842352706185659"></a>resource_name</strong> is available, indicating a cluster name. Other keys will be supported later.</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_en-us_topic_0110707086_row61821327173012"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1256910557306"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1256910557306"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1256910557306"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p16569755193015"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p16569755193015"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p16569755193015"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p12569135533014"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p12569135533014"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p12569135533014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p1569255203020"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1569255203020"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p1569255203020"></a>Value. A value contains a maximum of 64 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0112442490_en-us_topic_0110707086_section1726123842419"></a>

**Response parameter**

The following table describes the response parameters.

**Table  5**  Response parameters

<a name="table1666228184315"></a>
<table><thead align="left"><tr id="row8666122824313"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p0782134354316"><a name="p0782134354316"></a><a name="p0782134354316"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p27821243184315"><a name="p27821243184315"></a><a name="p27821243184315"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p187822434436"><a name="p187822434436"></a><a name="p187822434436"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p12782144310437"><a name="p12782144310437"></a><a name="p12782144310437"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5666192816432"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p31761551154320"><a name="p31761551154320"></a><a name="p31761551154320"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1617616510433"><a name="p1617616510433"></a><a name="p1617616510433"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p0176351194320"><a name="p0176351194320"></a><a name="p0176351194320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p417695164316"><a name="p417695164316"></a><a name="p417695164316"></a>Resource list.</p>
</td>
</tr>
<tr id="row13666928154316"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16176115118434"><a name="p16176115118434"></a><a name="p16176115118434"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p117619515438"><a name="p117619515438"></a><a name="p117619515438"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p117695114311"><a name="p117695114311"></a><a name="p117695114311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p15176185116439"><a name="p15176185116439"></a><a name="p15176185116439"></a>Total number of records.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Description of the  **resource**  field data structure

<a name="table1294961854417"></a>
<table><thead align="left"><tr id="row1194971819441"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p18156634154417"><a name="p18156634154417"></a><a name="p18156634154417"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p215623412441"><a name="p215623412441"></a><a name="p215623412441"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p215693474414"><a name="p215693474414"></a><a name="p215693474414"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p91561734154412"><a name="p91561734154412"></a><a name="p91561734154412"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10949418184417"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p15156834144410"><a name="p15156834144410"></a><a name="p15156834144410"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p515683417447"><a name="p515683417447"></a><a name="p515683417447"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p915614341449"><a name="p915614341449"></a><a name="p915614341449"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p8156193444413"><a name="p8156193444413"></a><a name="p8156193444413"></a>Resource ID.</p>
</td>
</tr>
<tr id="row394921834412"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8156334184410"><a name="p8156334184410"></a><a name="p8156334184410"></a>resource_detail</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p15156193413448"><a name="p15156193413448"></a><a name="p15156193413448"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p615616349447"><a name="p615616349447"></a><a name="p615616349447"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p10156034184418"><a name="p10156034184418"></a><a name="p10156034184418"></a>Resource details. The value is a resource object used for extension. The value is left blank by default.</p>
</td>
</tr>
<tr id="row1694971816444"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6156173412444"><a name="p6156173412444"></a><a name="p6156173412444"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p4156183404418"><a name="p4156183404418"></a><a name="p4156183404418"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p11561634164420"><a name="p11561634164420"></a><a name="p11561634164420"></a>List&lt;resource_tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p41562344447"><a name="p41562344447"></a><a name="p41562344447"></a>Tag list. This parameter is left blank by default if there is no tag.</p>
</td>
</tr>
<tr id="row594915181446"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14156133494415"><a name="p14156133494415"></a><a name="p14156133494415"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p115610340447"><a name="p115610340447"></a><a name="p115610340447"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p19156163415445"><a name="p19156163415445"></a><a name="p19156163415445"></a>string</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p12156334184411"><a name="p12156334184411"></a><a name="p12156334184411"></a>Resource name. This parameter is left blank by default if there is no resource name.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Description of the  **resource\_tag**  field data structure

<a name="en-us_topic_0112442490_table1897413881916"></a>
<table><thead align="left"><tr id="en-us_topic_0112442490_row119761638141911"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112442490_p12976163881914"><a name="en-us_topic_0112442490_p12976163881914"></a><a name="en-us_topic_0112442490_p12976163881914"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112442490_p12976113871920"><a name="en-us_topic_0112442490_p12976113871920"></a><a name="en-us_topic_0112442490_p12976113871920"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112442490_p149764384199"><a name="en-us_topic_0112442490_p149764384199"></a><a name="en-us_topic_0112442490_p149764384199"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112442490_p1297663891913"><a name="en-us_topic_0112442490_p1297663891913"></a><a name="en-us_topic_0112442490_p1297663891913"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442490_row109791438171912"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_p79795386197"><a name="en-us_topic_0112442490_p79795386197"></a><a name="en-us_topic_0112442490_p79795386197"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_p097915383192"><a name="en-us_topic_0112442490_p097915383192"></a><a name="en-us_topic_0112442490_p097915383192"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_p597912387197"><a name="en-us_topic_0112442490_p597912387197"></a><a name="en-us_topic_0112442490_p597912387197"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p4415154717299"><a name="p4415154717299"></a><a name="p4415154717299"></a>Key. </p>
<p id="p195815219290"><a name="p195815219290"></a><a name="p195815219290"></a>A tag key consists of a maximum of 36 characters, including A-Z, a-z, 0-9, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="en-us_topic_0112442490_row1198017388192"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442490_p109806384196"><a name="en-us_topic_0112442490_p109806384196"></a><a name="en-us_topic_0112442490_p109806384196"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442490_p1898023812195"><a name="en-us_topic_0112442490_p1898023812195"></a><a name="en-us_topic_0112442490_p1898023812195"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442490_p12980438111912"><a name="en-us_topic_0112442490_p12980438111912"></a><a name="en-us_topic_0112442490_p12980438111912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p1773216109300"><a name="p1773216109300"></a><a name="p1773216109300"></a>Value.</p>
<p id="en-us_topic_0112442490_p898083871913"><a name="en-us_topic_0112442490_p898083871913"></a><a name="en-us_topic_0112442490_p898083871913"></a>The value consists of a maximum of 43 characters, including A-Z, a-z, 0-9, periods (.), hyphens (-), and underscores (_), and can be an empty string.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="en-us_topic_0112442490_en-us_topic_0110707086_section7518458264"></a>

-   Request example

Filter request example

```
POST /{version}/{project_id}/{resource_type}/resource_instances/action
```

Request body when  **action**  is set to  **filter**

```
{
  "offset": "100", 
  "limit": "100", 
"action": "filter", 
  "matches":[
{
        "key": "resource_name", 
        "value": "streamA"
       }
], 
   "not_tags": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
      ]
    }
  ], 
  "tags": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
      ]
    }
  ], 
  "tags_any": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
      ]
    }
  ],
"not_tags_any": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
      ]
    }
  ]
}
```

Request body when  **action**  is set to  **count**

```
{
  "action": "count", 
  "not_tags": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
      ]
    }
  ], 
  "tags": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
      ]
    },
  {
      "key": "key2", 
      "values": [
        "value1", 
        "value2"
      ]
    }
  ], 
  "tags_any": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
      ]
    }
  ],
"not_tags_any": [
    {
      "key": "key1", 
      "values": [
        "value1", 
        "value2"
      ]
    }
   ],
"matches":[
{
        "key": "resource_name", 
        "value": "streamA"
       }
]
}
```

-   Response example

Response body when  **action**  is set to  **filter**

```
    { 
      "resources": [
         {
            "resource_detail": null, 
            "resource_id": "cdfs_cefs_wesas_12_dsad", 
            "resource_name": "streamA", 
            "tags": [
                {
                   "key": "key1",
                   "value": "value1"
                },
                {
                   "key": "key2",
                   "value": "value1"
                }
             ]
         }
       ], 
      "total_count": 1000
}
```

Response body when  **action**  is set to  **count**

```
{
       "total_count": 1000
}
```

## Status Code<a name="en-us_topic_0112442490_en-us_topic_0110707086_section236812132267"></a>

[Table 8](#en-us_topic_0112442490_en-us_topic_0110707086_table5043525610328)  lists the status code of this API.

**Table  8**  Status code

<a name="en-us_topic_0112442490_en-us_topic_0110707086_table5043525610328"></a>
<table><thead align="left"><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row1549446910328"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p4709251510328"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p4709251510328"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p4709251510328"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="en-us_topic_0112442490_en-us_topic_0110707086_p5639738110328"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p5639738110328"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p5639738110328"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442490_en-us_topic_0110707086_row478517210328"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p5205464710328"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p5205464710328"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p5205464710328"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0112442490_en-us_topic_0110707086_p39771881331"><a name="en-us_topic_0112442490_en-us_topic_0110707086_p39771881331"></a><a name="en-us_topic_0112442490_en-us_topic_0110707086_p39771881331"></a>OK</p>
</td>
</tr>
</tbody>
</table>

