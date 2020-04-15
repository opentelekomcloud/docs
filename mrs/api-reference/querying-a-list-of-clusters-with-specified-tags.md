# Querying a List of Clusters with Specified Tags<a name="EN-US_TOPIC_0172486234"></a>

## Function<a name="s975f80145897467fbf42c1c56b6f2c1a"></a>

This API is used to filter clusters by tag.

By default, clusters and tags are sorted in descending order of creation time.

## URI<a name="s12a41512711844f69adab29fde692b19"></a>

-   Format

    POST /v1.1/\{project\_id\}/clusters/resource\_instances/action

-   Parameter description

    **Table  1**  URI parameter description

    <a name="td6df3112b0d041f6918c19cbb2a9e47f"></a>
    <table><thead align="left"><tr id="r8ace0f816c4946d3b1207ce91e8deb96"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="a6c3e03563d5847089614adcfebfeeaf3"><a name="a6c3e03563d5847089614adcfebfeeaf3"></a><a name="a6c3e03563d5847089614adcfebfeeaf3"></a><strong id="b1932805122515"><a name="b1932805122515"></a><a name="b1932805122515"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110707086_p388412816227"><a name="en-us_topic_0110707086_p388412816227"></a><a name="en-us_topic_0110707086_p388412816227"></a><strong id="b369513153254"><a name="b369513153254"></a><a name="b369513153254"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="afa14c87427234bd08c0662ed5b71bd1e"><a name="afa14c87427234bd08c0662ed5b71bd1e"></a><a name="afa14c87427234bd08c0662ed5b71bd1e"></a><strong id="b72891534122514"><a name="b72891534122514"></a><a name="b72891534122514"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r0358327852bf48adae268af0444ee1e8"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aad2ee153ccb44e60a057bfb5e1ed115f"><a name="aad2ee153ccb44e60a057bfb5e1ed115f"></a><a name="aad2ee153ccb44e60a057bfb5e1ed115f"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a18f009f2775e4efd952b766fbe963474"><a name="a18f009f2775e4efd952b766fbe963474"></a><a name="a18f009f2775e4efd952b766fbe963474"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a71ac2c0980594830976a312e3291a220"><a name="a71ac2c0980594830976a312e3291a220"></a><a name="a71ac2c0980594830976a312e3291a220"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s5b360e3dcff844d6b64a41875596f7f0"></a>

**Table  2**  Request parameter description

<a name="t28dba73d72a94b648ef5179a95eb71f6"></a>
<table><thead align="left"><tr id="re9f5c9bc8f3743519030bc48bfc37db1"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="a82ae57ba67244665a7cfdcea834b164a"><a name="a82ae57ba67244665a7cfdcea834b164a"></a><a name="a82ae57ba67244665a7cfdcea834b164a"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0110707086_p359718019240"><a name="en-us_topic_0110707086_p359718019240"></a><a name="en-us_topic_0110707086_p359718019240"></a><strong id="b1971344193217"><a name="b1971344193217"></a><a name="b1971344193217"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0110707086_p35978012418"><a name="en-us_topic_0110707086_p35978012418"></a><a name="en-us_topic_0110707086_p35978012418"></a><strong id="b10672248183215"><a name="b10672248183215"></a><a name="b10672248183215"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="a0ae1fb86756645718a06e417f8758f4c"><a name="a0ae1fb86756645718a06e417f8758f4c"></a><a name="a0ae1fb86756645718a06e417f8758f4c"></a><strong id="b139905333210"><a name="b139905333210"></a><a name="b139905333210"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r9cedbfdb1a9b48a5b3b217b3fe2cd4aa"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1575715772816"><a name="p1575715772816"></a><a name="p1575715772816"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p7758165732819"><a name="p7758165732819"></a><a name="p7758165732819"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p275835732812"><a name="p275835732812"></a><a name="p275835732812"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p4758257172813"><a name="p4758257172813"></a><a name="p4758257172813"></a>The return result contains resources corresponding to all tags in this parameter. This parameter contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string.</p>
</td>
</tr>
<tr id="row17786165614171"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16656934491"><a name="p16656934491"></a><a name="p16656934491"></a>tags_any</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p5656734297"><a name="p5656734297"></a><a name="p5656734297"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1552517316103"><a name="p1552517316103"></a><a name="p1552517316103"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p8656153420912"><a name="p8656153420912"></a><a name="p8656153420912"></a>The return result contains resources corresponding to any tag in this parameter. This parameter contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string. Keys must be unique and values of a key must be unique.</p>
</td>
</tr>
<tr id="row1829235651717"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p89561301799"><a name="p89561301799"></a><a name="p89561301799"></a>not_tags</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p49567301595"><a name="p49567301595"></a><a name="p49567301595"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p555763231010"><a name="p555763231010"></a><a name="p555763231010"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p16956230793"><a name="p16956230793"></a><a name="p16956230793"></a>The return result does not contain resources corresponding to all tags in this parameter. This parameter contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string. Keys must be unique and values of a key must be unique.</p>
</td>
</tr>
<tr id="row15171115419176"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1384616271395"><a name="p1384616271395"></a><a name="p1384616271395"></a>not_tags_any</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p6846102716912"><a name="p6846102716912"></a><a name="p6846102716912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p143919332103"><a name="p143919332103"></a><a name="p143919332103"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p784672718910"><a name="p784672718910"></a><a name="p784672718910"></a>The return result does not contain resources corresponding to any tag in this parameter. This parameter contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string. Keys must be unique and values of a key must be unique.</p>
</td>
</tr>
<tr id="rfbb78dcf8ecd4667b5f07d598200d1e7"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="a41e699634a244ace97e50a978466453c"><a name="a41e699634a244ace97e50a978466453c"></a><a name="a41e699634a244ace97e50a978466453c"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="aa2bf2615678546ec93ced4cef7c1e1c9"><a name="aa2bf2615678546ec93ced4cef7c1e1c9"></a><a name="aa2bf2615678546ec93ced4cef7c1e1c9"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="a49a6fff13e5a4735a943b404d000c21a"><a name="a49a6fff13e5a4735a943b404d000c21a"></a><a name="a49a6fff13e5a4735a943b404d000c21a"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="aa575c1d4ec3a4922be9f3509ac5ea303"><a name="aa575c1d4ec3a4922be9f3509ac5ea303"></a><a name="aa575c1d4ec3a4922be9f3509ac5ea303"></a>Number of records. This parameter is not available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> when <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The maximum value is <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="r03cbf29cf4d94468b2d1e8f5f40b5e42"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0110707086_p027813183295"><a name="en-us_topic_0110707086_p027813183295"></a><a name="en-us_topic_0110707086_p027813183295"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="ac6b11491637a40908b18d3206083aa16"><a name="ac6b11491637a40908b18d3206083aa16"></a><a name="ac6b11491637a40908b18d3206083aa16"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="aa50fcceb99d14612be145b78439bc9f0"><a name="aa50fcceb99d14612be145b78439bc9f0"></a><a name="aa50fcceb99d14612be145b78439bc9f0"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="a30af70e2c44d4463a61badbe9e3267f7"><a name="a30af70e2c44d4463a61badbe9e3267f7"></a><a name="a30af70e2c44d4463a61badbe9e3267f7"></a>Index position. The query starts from the next piece of data specified by the <strong id="b1681212791610"><a name="b1681212791610"></a><a name="b1681212791610"></a>offset</strong> parameter. This parameter is not required when you query data on the first page. The value in the response body returned for querying data on the previous page will be included in this parameter for querying data on subsequent pages. This parameter is not available when <strong id="b84235270621521"><a name="b84235270621521"></a><a name="b84235270621521"></a>action</strong> is set to <strong id="b84235270621525"><a name="b84235270621525"></a><a name="b84235270621525"></a>count</strong>. If <strong id="b84235270621528"><a name="b84235270621528"></a><a name="b84235270621528"></a>action</strong> is set to <strong id="b84235270621532"><a name="b84235270621532"></a><a name="b84235270621532"></a>filter</strong>, the value must be a number, and the default value is <strong id="b84235270621539"><a name="b84235270621539"></a><a name="b84235270621539"></a>0</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="refddb3f568b342778ceb773210c8cf0a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0110707086_p928051819292"><a name="en-us_topic_0110707086_p928051819292"></a><a name="en-us_topic_0110707086_p928051819292"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="a422491cd50f44313828ba719f584f78a"><a name="a422491cd50f44313828ba719f584f78a"></a><a name="a422491cd50f44313828ba719f584f78a"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0110707086_p628011814294"><a name="en-us_topic_0110707086_p628011814294"></a><a name="en-us_topic_0110707086_p628011814294"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0110707086_p228061852911"><a name="en-us_topic_0110707086_p228061852911"></a><a name="en-us_topic_0110707086_p228061852911"></a>Operation to be performed. The value can be <strong id="b84235270616546"><a name="b84235270616546"></a><a name="b84235270616546"></a>filter</strong> or <strong id="b84235270616552"><a name="b84235270616552"></a><a name="b84235270616552"></a>count</strong>.</p>
<p id="aa6c2ff26ee0b4cb282492af848e0781a"><a name="aa6c2ff26ee0b4cb282492af848e0781a"></a><a name="aa6c2ff26ee0b4cb282492af848e0781a"></a>The value <strong id="b842352706112921"><a name="b842352706112921"></a><a name="b842352706112921"></a>filter</strong> indicates pagination query. The value <strong id="b84235270611312"><a name="b84235270611312"></a><a name="b84235270611312"></a>count</strong> indicates that the total number of query results meeting the search criteria will be returned.</p>
</td>
</tr>
<tr id="r0a8e02970a3a42569bf5508f8e4c30c8"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="af6f197f69f414002b339ede74a89154f"><a name="af6f197f69f414002b339ede74a89154f"></a><a name="af6f197f69f414002b339ede74a89154f"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="a58910123e42f4369ae069f346ccb920b"><a name="a58910123e42f4369ae069f346ccb920b"></a><a name="a58910123e42f4369ae069f346ccb920b"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0110707086_p428031819290"><a name="en-us_topic_0110707086_p428031819290"></a><a name="en-us_topic_0110707086_p428031819290"></a>List&lt;match&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="af5f4f778b50f4beebf058e7b63666e68"><a name="af5f4f778b50f4beebf058e7b63666e68"></a><a name="af5f4f778b50f4beebf058e7b63666e68"></a>Search field. <strong id="b139191241144216"><a name="b139191241144216"></a><a name="b139191241144216"></a>key</strong> indicates the field to be matched, for example, <strong id="b1815994217155439"><a name="b1815994217155439"></a><a name="b1815994217155439"></a>resource_name</strong>. <strong id="b383113710436"><a name="b383113710436"></a><a name="b383113710436"></a>value</strong> indicates the matched value. This field is a fixed dictionary value.</p>
<p id="en-us_topic_0110707086_p152805187296"><a name="en-us_topic_0110707086_p152805187296"></a><a name="en-us_topic_0110707086_p152805187296"></a>Determine whether fuzzy match is required based on different fields. For example, if <strong id="b8423527062245"><a name="b8423527062245"></a><a name="b8423527062245"></a>key</strong> is <strong id="b842352706123028"><a name="b842352706123028"></a><a name="b842352706123028"></a>resource_name</strong>, fuzzy search is used by default. If <strong id="b842352706123110"><a name="b842352706123110"></a><a name="b842352706123110"></a>value</strong> is an empty string, exact match is used.</p>
<p id="en-us_topic_0110707086_p32803185293"><a name="en-us_topic_0110707086_p32803185293"></a><a name="en-us_topic_0110707086_p32803185293"></a></p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  field description

<a name="t7c877f5edc884ebdaa77ed73c072ffc1"></a>
<table><thead align="left"><tr id="r994b292f5cb0404d9ebd6c59c2f15010"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0110707086_p965615311307"><a name="en-us_topic_0110707086_p965615311307"></a><a name="en-us_topic_0110707086_p965615311307"></a><strong id="b8918258192612"><a name="b8918258192612"></a><a name="b8918258192612"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0110707086_p26567318304"><a name="en-us_topic_0110707086_p26567318304"></a><a name="en-us_topic_0110707086_p26567318304"></a><strong id="b193341010102713"><a name="b193341010102713"></a><a name="b193341010102713"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="ade84da15268449538e4df4912656b3c7"><a name="ade84da15268449538e4df4912656b3c7"></a><a name="ade84da15268449538e4df4912656b3c7"></a><strong id="b161912179279"><a name="b161912179279"></a><a name="b161912179279"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="en-us_topic_0110707086_p56560393020"><a name="en-us_topic_0110707086_p56560393020"></a><a name="en-us_topic_0110707086_p56560393020"></a><strong id="b2051530122714"><a name="b2051530122714"></a><a name="b2051530122714"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rfef7dd2f989442d79e1801ca89dba6d8"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0110707086_p156565383013"><a name="en-us_topic_0110707086_p156565383013"></a><a name="en-us_topic_0110707086_p156565383013"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="a653a141d1b7d4c42a3e2becac09ec526"><a name="a653a141d1b7d4c42a3e2becac09ec526"></a><a name="a653a141d1b7d4c42a3e2becac09ec526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0110707086_p665653123011"><a name="en-us_topic_0110707086_p665653123011"></a><a name="en-us_topic_0110707086_p665653123011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="a1772baac039a48a6a7a82876b2403c71"><a name="a1772baac039a48a6a7a82876b2403c71"></a><a name="a1772baac039a48a6a7a82876b2403c71"></a>Key. It contains a maximum of 127 Unicode characters. It cannot be left empty. (This parameter is not verified in the search process.)</p>
</td>
</tr>
<tr id="r01f35d83609f44a8b7ccdd8b36ed4310"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0110707086_p56577317309"><a name="en-us_topic_0110707086_p56577317309"></a><a name="en-us_topic_0110707086_p56577317309"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0110707086_p765720363016"><a name="en-us_topic_0110707086_p765720363016"></a><a name="en-us_topic_0110707086_p765720363016"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="ad74c05f569ea46189263174d3c05d656"><a name="ad74c05f569ea46189263174d3c05d656"></a><a name="ad74c05f569ea46189263174d3c05d656"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0110707086_p265773143019"><a name="en-us_topic_0110707086_p265773143019"></a><a name="en-us_topic_0110707086_p265773143019"></a>List of values. A value contains a maximum of 255 Unicode characters.</p>
<p id="en-us_topic_0110707086_p176579314309"><a name="en-us_topic_0110707086_p176579314309"></a><a name="en-us_topic_0110707086_p176579314309"></a>If the values are null, it indicates <strong id="b842352706175623"><a name="b842352706175623"></a><a name="b842352706175623"></a>any_value</strong>. The relationship between values is OR. By default, only the first value is used for search.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **match**  field description

<a name="tf07fcd1f07994fc099e990a2aafead97"></a>
<table><thead align="left"><tr id="ra306570ff3de452ba10d15a70009db1b"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0110707086_p156795563011"><a name="en-us_topic_0110707086_p156795563011"></a><a name="en-us_topic_0110707086_p156795563011"></a><strong id="b1518515122719"><a name="b1518515122719"></a><a name="b1518515122719"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0110707086_p056719556302"><a name="en-us_topic_0110707086_p056719556302"></a><a name="en-us_topic_0110707086_p056719556302"></a><strong id="b47461914112719"><a name="b47461914112719"></a><a name="b47461914112719"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0110707086_p175678554306"><a name="en-us_topic_0110707086_p175678554306"></a><a name="en-us_topic_0110707086_p175678554306"></a><strong id="b3680522142713"><a name="b3680522142713"></a><a name="b3680522142713"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="aec862b3585134e4fbd90de25f3525d66"><a name="aec862b3585134e4fbd90de25f3525d66"></a><a name="aec862b3585134e4fbd90de25f3525d66"></a><strong id="b94126336273"><a name="b94126336273"></a><a name="b94126336273"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc0a202d941f041508ec064469f49198d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0110707086_p856713553306"><a name="en-us_topic_0110707086_p856713553306"></a><a name="en-us_topic_0110707086_p856713553306"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0110707086_p356905583013"><a name="en-us_topic_0110707086_p356905583013"></a><a name="en-us_topic_0110707086_p356905583013"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="ab6f5eb5e96f34c83a93e25f6ea580545"><a name="ab6f5eb5e96f34c83a93e25f6ea580545"></a><a name="ab6f5eb5e96f34c83a93e25f6ea580545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="a5beefb9a59ab4a5ea6caffbfada8ee60"><a name="a5beefb9a59ab4a5ea6caffbfada8ee60"></a><a name="a5beefb9a59ab4a5ea6caffbfada8ee60"></a>Key. The value is fixed to <strong id="b3320648193614"><a name="b3320648193614"></a><a name="b3320648193614"></a>resource_name</strong>, indicating a cluster name.</p>
</td>
</tr>
<tr id="r08e5024ddf464d7485053af2f0a9b711"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="a229a24249194411fbfc866d33563e4ff"><a name="a229a24249194411fbfc866d33563e4ff"></a><a name="a229a24249194411fbfc866d33563e4ff"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="a0adbf3da2e604c3887bb77f1eaf9d3a8"><a name="a0adbf3da2e604c3887bb77f1eaf9d3a8"></a><a name="a0adbf3da2e604c3887bb77f1eaf9d3a8"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="aeb53bbc0ff494aecb0c27c7d978c8208"><a name="aeb53bbc0ff494aecb0c27c7d978c8208"></a><a name="aeb53bbc0ff494aecb0c27c7d978c8208"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="a8aaf951ed75a4118b11ec420947cc370"><a name="a8aaf951ed75a4118b11ec420947cc370"></a><a name="a8aaf951ed75a4118b11ec420947cc370"></a>Value. A value contains a maximum of 64 Unicode characters. Enter a cluster name.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="s2040a1585bda451d81def621572c0b17"></a>

**Table  5**  Response parameter description

<a name="table1897413881916"></a>
<table><thead align="left"><tr id="row119761638141911"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p12976163881914"><a name="p12976163881914"></a><a name="p12976163881914"></a><strong id="b10495131214258"><a name="b10495131214258"></a><a name="b10495131214258"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p149764384199"><a name="p149764384199"></a><a name="p149764384199"></a><strong id="b66182710275"><a name="b66182710275"></a><a name="b66182710275"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p1297663891913"><a name="p1297663891913"></a><a name="p1297663891913"></a><strong id="b11871506817"><a name="b11871506817"></a><a name="b11871506817"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row109791438171912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p79795386197"><a name="p79795386197"></a><a name="p79795386197"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p597912387197"><a name="p597912387197"></a><a name="p597912387197"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p797912380198"><a name="p797912380198"></a><a name="p797912380198"></a>Key. A tag key can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row1198017388192"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p109806384196"><a name="p109806384196"></a><a name="p109806384196"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p12980438111912"><a name="p12980438111912"></a><a name="p12980438111912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p898083871913"><a name="p898083871913"></a><a name="p898083871913"></a>Tag value. A tag value can contain only uppercase letters, lowercase letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="se3cbf579c5644af99fea81d2f4ed375c"></a>

-   Example request

    Request body when  **action**  is set to  **filter**

    ```
    {
      "offset": "100", 
      "limit": "100", 
    "action": "filter", 
      "matches":[
    {
            "key": "resource_name", 
            "value": "clusterA"
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
            "value": "clusterA"
           }
    ]
    }
    ```


-   Example response

    Response body when  **action**  is set to  **filter**

    ```
        { 
          "resources": [
             {
                "resource_detail": null, 
                "resource_id": "cdfs_cefs_wesas_12_dsad", 
                "resource_name": "clusterA", 
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


## Status Code<a name="s48bb8c114a1e4e77b89ba12806974365"></a>

[Table 6](#t31bfd33136f84cd88b311dc479046586)  describes the status code of this API.

**Table  6**  Status code

<a name="t31bfd33136f84cd88b311dc479046586"></a>
<table><thead align="left"><tr id="ra0a28b8e4bfb49cb90d4029a28a701a3"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="a077251d86ed84b13b556d282dc52fdea"><a name="a077251d86ed84b13b556d282dc52fdea"></a><a name="a077251d86ed84b13b556d282dc52fdea"></a><strong id="b107830476819"><a name="b107830476819"></a><a name="b107830476819"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="ac2051ec31a884ffd9508519c0b28911e"><a name="ac2051ec31a884ffd9508519c0b28911e"></a><a name="ac2051ec31a884ffd9508519c0b28911e"></a><strong id="b1568695087"><a name="b1568695087"></a><a name="b1568695087"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc843f429b9f94186af21f19586b767cf"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="a9470033483954e6cb4abd85311e7547f"><a name="a9470033483954e6cb4abd85311e7547f"></a><a name="a9470033483954e6cb4abd85311e7547f"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110707086_p39771881331"><a name="en-us_topic_0110707086_p39771881331"></a><a name="en-us_topic_0110707086_p39771881331"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

