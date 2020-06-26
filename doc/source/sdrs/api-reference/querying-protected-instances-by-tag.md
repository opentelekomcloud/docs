# Querying Protected Instances by Tag<a name="sdrs_05_0801"></a>

## Function<a name="section75281345423"></a>

This interface is used to query protected instances by tag.

## URI<a name="section2053494516212"></a>

-   URI format

    POST /v1/\{project\_id\}/protected-instances/resource\_instances/action

-   Parameter description

    <a name="table195411245327"></a>
    <table><thead align="left"><tr id="row99813451229"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.1.5.1.1"><p id="p6981745727"><a name="p6981745727"></a><a name="p6981745727"></a><strong id="b842352706162023"><a name="b842352706162023"></a><a name="b842352706162023"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.1.5.1.2"><p id="p698115451228"><a name="p698115451228"></a><a name="p698115451228"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.268673132686734%" id="mcps1.1.5.1.3"><p id="p39812450214"><a name="p39812450214"></a><a name="p39812450214"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.1.5.1.4"><p id="p198118457218"><a name="p198118457218"></a><a name="p198118457218"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20981124517215"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.1 "><p id="p89815454216"><a name="p89815454216"></a><a name="p89815454216"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.2 "><p id="p1498116452216"><a name="p1498116452216"></a><a name="p1498116452216"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.1.5.1.3 "><p id="p29811145523"><a name="p29811145523"></a><a name="p29811145523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p139815451322"><a name="p139815451322"></a><a name="p139815451322"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section655512453211"></a>

-   Parameter description

    <a name="table1756210450219"></a>
    <table><thead align="left"><tr id="row169811445823"><th class="cellrowborder" valign="top" width="17.53%" id="mcps1.1.5.1.1"><p id="p69816451621"><a name="p69816451621"></a><a name="p69816451621"></a><strong id="b842352706162023_1"><a name="b842352706162023_1"></a><a name="b842352706162023_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.459999999999999%" id="mcps1.1.5.1.2"><p id="p159819451727"><a name="p159819451727"></a><a name="p159819451727"></a><strong id="b84235270615447_1"><a name="b84235270615447_1"></a><a name="b84235270615447_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.49%" id="mcps1.1.5.1.3"><p id="p09811145723"><a name="p09811145723"></a><a name="p09811145723"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.519999999999996%" id="mcps1.1.5.1.4"><p id="p1598114453218"><a name="p1598114453218"></a><a name="p1598114453218"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1051613813442"><td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.1 "><p id="p8982145121"><a name="p8982145121"></a><a name="p8982145121"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.2 "><p id="p098219451727"><a name="p098219451727"></a><a name="p098219451727"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.1.5.1.3 "><p id="p698213451523"><a name="p698213451523"></a><a name="p698213451523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p69829451326"><a name="p69829451326"></a><a name="p69829451326"></a>Specifies the index position. This parameter is unavailable when <strong id="b842352706102654"><a name="b842352706102654"></a><a name="b842352706102654"></a>action</strong> is set to <strong id="b84235270610271"><a name="b84235270610271"></a><a name="b84235270610271"></a>count</strong>. If <strong id="b70205942519474"><a name="b70205942519474"></a><a name="b70205942519474"></a>offset</strong> is set to <em id="i84235269720751"><a name="i84235269720751"></a><a name="i84235269720751"></a>N</em>, the resource query starts from the N+1 piece of data. If <strong id="b842352706102717"><a name="b842352706102717"></a><a name="b842352706102717"></a>action</strong> is set to <strong id="b842352706102722"><a name="b842352706102722"></a><a name="b842352706102722"></a>filter</strong>, the value of <strong id="b84235270620648"><a name="b84235270620648"></a><a name="b84235270620648"></a>offset</strong> is <strong id="b84235270620630"><a name="b84235270620630"></a><a name="b84235270620630"></a>0</strong> by default, indicating that the query starts from the first piece of data. The <strong id="b84235270620744"><a name="b84235270620744"></a><a name="b84235270620744"></a>offset</strong> value must be a number and cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="row2587111716443"><td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.1 "><p id="p39821445429"><a name="p39821445429"></a><a name="p39821445429"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.2 "><p id="p598217451923"><a name="p598217451923"></a><a name="p598217451923"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.1.5.1.3 "><p id="p149828452210"><a name="p149828452210"></a><a name="p149828452210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p1598224515216"><a name="p1598224515216"></a><a name="p1598224515216"></a>Specifies the number of limited queries. This parameter is not available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> when <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The maximum value is <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="row2097913301442"><td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.1 "><p id="p209821145926"><a name="p209821145926"></a><a name="p209821145926"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.2 "><p id="p10982104513212"><a name="p10982104513212"></a><a name="p10982104513212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.1.5.1.3 "><p id="p17984945927"><a name="p17984945927"></a><a name="p17984945927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p1198417453211"><a name="p1198417453211"></a><a name="p1198417453211"></a>Specifies the operation to be performed. The value can be <strong id="b84235270616546"><a name="b84235270616546"></a><a name="b84235270616546"></a>filter</strong> (filtering) or <strong id="b84235270616552"><a name="b84235270616552"></a><a name="b84235270616552"></a>count</strong> (querying the total number).</p>
    <p id="p19844450212"><a name="p19844450212"></a><a name="p19844450212"></a>If <strong id="b8423527061184"><a name="b8423527061184"></a><a name="b8423527061184"></a>action</strong> is set to <strong id="b84235270611747"><a name="b84235270611747"></a><a name="b84235270611747"></a>filter</strong>, the query is performed based on the filter conditions. If <strong id="b1158078253111040"><a name="b1158078253111040"></a><a name="b1158078253111040"></a>action</strong> is set to <strong id="b1717869715111040"><a name="b1717869715111040"></a><a name="b1717869715111040"></a>count</strong>, only the total number of records is returned.</p>
    </td>
    </tr>
    <tr id="row1958125584416"><td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.1 "><p id="p99840451329"><a name="p99840451329"></a><a name="p99840451329"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.2 "><p id="p129840455215"><a name="p129840455215"></a><a name="p129840455215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.1.5.1.3 "><p id="p1498417451124"><a name="p1498417451124"></a><a name="p1498417451124"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p159841145527"><a name="p159841145527"></a><a name="p159841145527"></a>Specifies the search field. The tag key is the field to be matched, for example, <strong id="b1815994217155439"><a name="b1815994217155439"></a><a name="b1815994217155439"></a>resource_name</strong>. The tag value indicates the value to be matched. The key is a fixed dictionary value and cannot contain duplicate keys or unsupported keys.</p>
    <p id="p6984145925"><a name="p6984145925"></a><a name="p6984145925"></a>Determine whether fuzzy match is required based on the keys. For example, if <strong id="b8423527062245"><a name="b8423527062245"></a><a name="b8423527062245"></a>key</strong> is <strong id="b842352706123028"><a name="b842352706123028"></a><a name="b842352706123028"></a>resource_name</strong>, fuzzy search (case insensitive) is used by default. If <strong id="b842352706123110"><a name="b842352706123110"></a><a name="b842352706123110"></a>value</strong> is an empty string, exact match is used. Currently, only <strong id="b842352706123249"><a name="b842352706123249"></a><a name="b842352706123249"></a>resource_name</strong> for <strong id="b842352706201429"><a name="b842352706201429"></a><a name="b842352706201429"></a>key</strong> is supported. Other <strong id="b842352706201455"><a name="b842352706201455"></a><a name="b842352706201455"></a>key</strong> values will be available later.</p>
    <p id="p5497131161018"><a name="p5497131161018"></a><a name="p5497131161018"></a>For details, see <a href="#table16621174514217">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row185782162452"><td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.1 "><p id="p119819459217"><a name="p119819459217"></a><a name="p119819459217"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.2 "><p id="p998119451216"><a name="p998119451216"></a><a name="p998119451216"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.1.5.1.3 "><p id="p79815451216"><a name="p79815451216"></a><a name="p79815451216"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p998144515217"><a name="p998144515217"></a><a name="p998144515217"></a>The resources to be queried do not contain tags listed in <strong id="b548729334194419"><a name="b548729334194419"></a><a name="b548729334194419"></a>not_tags</strong>. Each resource to be queried contains a maximum of 20 keys. Each tag key can have a maximum of 20 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key must be unique, and each tag value in a tag must be unique. The response returns resources containing no tags in this list. Keys in this list are in an AND relationship while values in each key-value structure are in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    <p id="p117770538101"><a name="p117770538101"></a><a name="p117770538101"></a>For details, see <a href="#table9607445020">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row15981144512219"><td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.1 "><p id="p1981114511217"><a name="p1981114511217"></a><a name="p1981114511217"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.2 "><p id="p298164511216"><a name="p298164511216"></a><a name="p298164511216"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.1.5.1.3 "><p id="p298115457218"><a name="p298115457218"></a><a name="p298115457218"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p3981174513214"><a name="p3981174513214"></a><a name="p3981174513214"></a>The resources to be queried contain tags listed in <strong id="b1382599853193448"><a name="b1382599853193448"></a><a name="b1382599853193448"></a>tags</strong>. Each resource to be queried contains a maximum of 20 keys. Each tag key can have a maximum of 20 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key must be unique, and each tag value in a tag must be unique. The response returns resources containing all tags in this list. Keys in this list are in an AND relationship while values in each key-value structure are in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    <p id="p165152013151016"><a name="p165152013151016"></a><a name="p165152013151016"></a>For details, see <a href="#table9607445020">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row498118451921"><td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.1 "><p id="p998114456219"><a name="p998114456219"></a><a name="p998114456219"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.2 "><p id="p198194510218"><a name="p198194510218"></a><a name="p198194510218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.1.5.1.3 "><p id="p149811845121"><a name="p149811845121"></a><a name="p149811845121"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p1398154512210"><a name="p1398154512210"></a><a name="p1398154512210"></a>The resources to be queried contain any tags listed in <strong id="b2119851361193951"><a name="b2119851361193951"></a><a name="b2119851361193951"></a>tags_any</strong>. Each resource to be queried contains a maximum of 20 keys. Each tag key can have a maximum of 20 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key must be unique, and each tag value in a tag must be unique. The response returns resources containing the tags in this list. Keys in this list are in an OR relationship and values in each key-value structure are also in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    <p id="p48641207817"><a name="p48641207817"></a><a name="p48641207817"></a>For details, see <a href="#table9607445020">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row59817454218"><td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.1 "><p id="p119811145628"><a name="p119811145628"></a><a name="p119811145628"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.2 "><p id="p598118451524"><a name="p598118451524"></a><a name="p598118451524"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.1.5.1.3 "><p id="p129813451420"><a name="p129813451420"></a><a name="p129813451420"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p69821645122"><a name="p69821645122"></a><a name="p69821645122"></a>The resources to be queried do not contain any tags listed in <strong id="b4747911122210"><a name="b4747911122210"></a><a name="b4747911122210"></a>not_tags_any</strong>. Each resource to be queried contains a maximum of 20 keys. Each tag key can have a maximum of 20 tag values. The tag value corresponding to each tag key can be an empty array but the structure cannot be missing. Each tag key must be unique, and each tag value in a tag must be unique. The response returns resources containing no tags in this list. Keys in this list are in an OR relationship and values in each key-value structure are also in an OR relationship. If no tag filtering condition is specified, full data is returned.</p>
    <p id="p1280271121112"><a name="p1280271121112"></a><a name="p1280271121112"></a>For details, see <a href="#table9607445020">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Data structure of field  **tag**

    <a name="table9607445020"></a>
    <table><thead align="left"><tr id="row1598494519217"><th class="cellrowborder" valign="top" width="10.100000000000001%" id="mcps1.2.5.1.1"><p id="p1198416456218"><a name="p1198416456218"></a><a name="p1198416456218"></a><strong id="b842352706162023_2"><a name="b842352706162023_2"></a><a name="b842352706162023_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.5.1.2"><p id="p13984194517210"><a name="p13984194517210"></a><a name="p13984194517210"></a><strong id="b84235270615447_2"><a name="b84235270615447_2"></a><a name="b84235270615447_2"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.5.1.3"><p id="p17984345226"><a name="p17984345226"></a><a name="p17984345226"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.51%" id="mcps1.2.5.1.4"><p id="p7984104516214"><a name="p7984104516214"></a><a name="p7984104516214"></a><strong id="b84235270615457_2"><a name="b84235270615457_2"></a><a name="b84235270615457_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9984184519215"><td class="cellrowborder" valign="top" width="10.100000000000001%" headers="mcps1.2.5.1.1 "><p id="p19845452218"><a name="p19845452218"></a><a name="p19845452218"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.5.1.2 "><p id="p1398416459217"><a name="p1398416459217"></a><a name="p1398416459217"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p49848451326"><a name="p49848451326"></a><a name="p49848451326"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.5.1.4 "><p id="p189848451210"><a name="p189848451210"></a><a name="p189848451210"></a>Specifies the tag key. It contains a maximum of 127 Unicode characters. It cannot be left blank. <strong id="b842352706195333"><a name="b842352706195333"></a><a name="b842352706195333"></a>key</strong> cannot be empty, an empty string, or spaces. Before using <strong id="b842352706202438"><a name="b842352706202438"></a><a name="b842352706202438"></a>key</strong>, delete spaces of single-byte character (SBC) before and after the value.</p>
    </td>
    </tr>
    <tr id="row1198434513215"><td class="cellrowborder" valign="top" width="10.100000000000001%" headers="mcps1.2.5.1.1 "><p id="p169849451426"><a name="p169849451426"></a><a name="p169849451426"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.5.1.2 "><p id="p1898410451125"><a name="p1898410451125"></a><a name="p1898410451125"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p29841845724"><a name="p29841845724"></a><a name="p29841845724"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.5.1.4 "><p id="p617715315531"><a name="p617715315531"></a><a name="p617715315531"></a>Lists the tag values. Each value contains a maximum of 255 Unicode characters. Before using <strong id="b842352706195530"><a name="b842352706195530"></a><a name="b842352706195530"></a>values</strong>, delete SBC spaces before and after the value.</p>
    <p id="p39841545625"><a name="p39841545625"></a><a name="p39841545625"></a>The asterisk (*) is reserved for the system. If the value starts with *, it indicates that fuzzy match is performed based on the value following *. The value cannot contain only asterisks (*).</p>
    <p id="p109845451721"><a name="p109845451721"></a><a name="p109845451721"></a>If the values are null, it indicates <strong id="b842352706175623"><a name="b842352706175623"></a><a name="b842352706175623"></a>any_value</strong> (querying any value). The resources containing one or more values listed in <strong>values</strong> will be found and displayed.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Description of the  **match**  field

    <a name="table16621174514217"></a>
    <table><thead align="left"><tr id="row49842045727"><th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.5.1.1"><p id="p69841456213"><a name="p69841456213"></a><a name="p69841456213"></a><strong id="b842352706162023_3"><a name="b842352706162023_3"></a><a name="b842352706162023_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.65%" id="mcps1.2.5.1.2"><p id="p6984345728"><a name="p6984345728"></a><a name="p6984345728"></a><strong id="b84235270615447_3"><a name="b84235270615447_3"></a><a name="b84235270615447_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.49%" id="mcps1.2.5.1.3"><p id="p7984134515212"><a name="p7984134515212"></a><a name="p7984134515212"></a><strong id="b84235270615453_3"><a name="b84235270615453_3"></a><a name="b84235270615453_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.55%" id="mcps1.2.5.1.4"><p id="p12984645322"><a name="p12984645322"></a><a name="p12984645322"></a><strong id="b84235270615457_3"><a name="b84235270615457_3"></a><a name="b84235270615457_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39841245723"><td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.5.1.1 "><p id="p39841145426"><a name="p39841145426"></a><a name="p39841145426"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.2.5.1.2 "><p id="p209846451928"><a name="p209846451928"></a><a name="p209846451928"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.2.5.1.3 "><p id="p39841745424"><a name="p39841745424"></a><a name="p39841745424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.55%" headers="mcps1.2.5.1.4 "><p id="p193447512163"><a name="p193447512163"></a><a name="p193447512163"></a>Specifies the tag key.</p>
    <p id="p098416451524"><a name="p098416451524"></a><a name="p098416451524"></a>Currently, only <strong id="b842352706123249_1"><a name="b842352706123249_1"></a><a name="b842352706123249_1"></a>resource_name</strong> for <strong id="b842352706201429_1"><a name="b842352706201429_1"></a><a name="b842352706201429_1"></a>key</strong> is supported. Other <strong id="b842352706201455_1"><a name="b842352706201455_1"></a><a name="b842352706201455_1"></a>key</strong> values will be available later.</p>
    </td>
    </tr>
    <tr id="row1498415452022"><td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.5.1.1 "><p id="p129841945125"><a name="p129841945125"></a><a name="p129841945125"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.2.5.1.2 "><p id="p498424512218"><a name="p498424512218"></a><a name="p498424512218"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.49%" headers="mcps1.2.5.1.3 "><p id="p098418451523"><a name="p098418451523"></a><a name="p098418451523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.55%" headers="mcps1.2.5.1.4 "><p id="p174441601614"><a name="p174441601614"></a><a name="p174441601614"></a>Specifies the tag value.</p>
    <p id="p398414451521"><a name="p398414451521"></a><a name="p398414451521"></a>Each value can contain a maximum of 255 Unicode characters.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request when  **action**  is set to  **filter**

    POST https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/resource\_instances/action

    ```
    {
        "offset": "100",
        "limit": "100",
        "action": "filter",
        "matches": [
            {
                "key": "resource_name",
                "value": "resource1"
            }
        ],
        "not_tags": [
            {
                "key": "key1",
                "values": [
                    "*value1",
                    "value2"
                ]
            }
        ],
        "tags": [
            {
                "key": "key1",
                "values": [
                    "*value1",
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

-   Sample request when  **action**  is set to  **count**

    POST https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/resource\_instances/action

    ```
    {
        "action": "count",
        "not_tags": [
            {
                "key": "key1",
                "values": [
                    "value1",
                    "*value2"
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
        "matches": [
            {
                "key": "resource_name",
                "value": "resource1"
            }
        ]
    }
    ```


## Response<a name="section963210457217"></a>

-   Parameter description

    <a name="table12636124519210"></a>
    <table><thead align="left"><tr id="row998514451324"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.1.5.1.1"><p id="p698518451326"><a name="p698518451326"></a><a name="p698518451326"></a><strong id="b842352706162023_4"><a name="b842352706162023_4"></a><a name="b842352706162023_4"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.1.5.1.2"><p id="p3985144510211"><a name="p3985144510211"></a><a name="p3985144510211"></a><strong id="b84235270615447_4"><a name="b84235270615447_4"></a><a name="b84235270615447_4"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.3"><p id="p29857458213"><a name="p29857458213"></a><a name="p29857458213"></a><strong id="b84235270615453_4"><a name="b84235270615453_4"></a><a name="b84235270615453_4"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.1.5.1.4"><p id="p15985194518220"><a name="p15985194518220"></a><a name="p15985194518220"></a><strong id="b84235270615457_4"><a name="b84235270615457_4"></a><a name="b84235270615457_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1298519455213"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.5.1.1 "><p id="p169851457213"><a name="p169851457213"></a><a name="p169851457213"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.2 "><p id="p1598516451723"><a name="p1598516451723"></a><a name="p1598516451723"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.3 "><p id="p2985154512214"><a name="p2985154512214"></a><a name="p2985154512214"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.1.5.1.4 "><p id="p115971253191112"><a name="p115971253191112"></a><a name="p115971253191112"></a>Specifies the returned protected instances.</p>
    <p id="p1898554513211"><a name="p1898554513211"></a><a name="p1898554513211"></a>For details, see <a href="#table16443451223">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row19985134511216"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.1.5.1.1 "><p id="p79857459215"><a name="p79857459215"></a><a name="p79857459215"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.1.5.1.2 "><p id="p1985124518215"><a name="p1985124518215"></a><a name="p1985124518215"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.3 "><p id="p9985134514217"><a name="p9985134514217"></a><a name="p9985134514217"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.1.5.1.4 "><p id="p1985345126"><a name="p1985345126"></a><a name="p1985345126"></a>Specifies the total number of resources.</p>
    <p id="p216434311222"><a name="p216434311222"></a><a name="p216434311222"></a>The value is not affected by the filtering criteria.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of field  **resource**

    <a name="table16443451223"></a>
    <table><thead align="left"><tr id="row79851245328"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p1598511451923"><a name="p1598511451923"></a><a name="p1598511451923"></a><strong id="b842352706162023_5"><a name="b842352706162023_5"></a><a name="b842352706162023_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.2"><p id="p5985184513215"><a name="p5985184513215"></a><a name="p5985184513215"></a><strong id="b84235270615447_5"><a name="b84235270615447_5"></a><a name="b84235270615447_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p29851445828"><a name="p29851445828"></a><a name="p29851445828"></a><strong id="b84235270615453_5"><a name="b84235270615453_5"></a><a name="b84235270615453_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p598613451126"><a name="p598613451126"></a><a name="p598613451126"></a><strong id="b84235270615457_5"><a name="b84235270615457_5"></a><a name="b84235270615457_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row998644510219"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p298694513216"><a name="p298694513216"></a><a name="p298694513216"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.2 "><p id="p798664510215"><a name="p798664510215"></a><a name="p798664510215"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p129861045121"><a name="p129861045121"></a><a name="p129861045121"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p49863451220"><a name="p49863451220"></a><a name="p49863451220"></a>Specifies the ID of a protected instance.</p>
    </td>
    </tr>
    <tr id="row4451926174117"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p398613455217"><a name="p398613455217"></a><a name="p398613455217"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.2 "><p id="p17986194511211"><a name="p17986194511211"></a><a name="p17986194511211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p9986204520212"><a name="p9986204520212"></a><a name="p9986204520212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p19986945826"><a name="p19986945826"></a><a name="p19986945826"></a>Specifies the protected instance name. This parameter is left blank by default if there is no name.</p>
    </td>
    </tr>
    <tr id="row16986184514217"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p1986164513218"><a name="p1986164513218"></a><a name="p1986164513218"></a>resource_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.2 "><p id="p209868453211"><a name="p209868453211"></a><a name="p209868453211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p69861452217"><a name="p69861452217"></a><a name="p69861452217"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p189868451527"><a name="p189868451527"></a><a name="p189868451527"></a>Specifies the details of a protected instance.</p>
    </td>
    </tr>
    <tr id="row18986144515210"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p19866451225"><a name="p19866451225"></a><a name="p19866451225"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.2 "><p id="p1986124516215"><a name="p1986124516215"></a><a name="p1986124516215"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p109861245728"><a name="p109861245728"></a><a name="p109861245728"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p498610454215"><a name="p498610454215"></a><a name="p498610454215"></a>Specifies the tag list. If there is no tag in the list, <strong id="b84235270620128"><a name="b84235270620128"></a><a name="b84235270620128"></a>tags</strong> is taken as an empty array.</p>
    <p id="p363479181219"><a name="p363479181219"></a><a name="p363479181219"></a>For details, see <a href="#table7656144514216">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Parameter description of field  **resource\_tag**

    <a name="table7656144514216"></a>
    <table><thead align="left"><tr id="row1986124513214"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p209865451824"><a name="p209865451824"></a><a name="p209865451824"></a><strong id="b842352706162023_6"><a name="b842352706162023_6"></a><a name="b842352706162023_6"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.2"><p id="p4986045129"><a name="p4986045129"></a><a name="p4986045129"></a><strong id="b84235270615447_6"><a name="b84235270615447_6"></a><a name="b84235270615447_6"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.3"><p id="p1598620451722"><a name="p1598620451722"></a><a name="p1598620451722"></a><strong id="b84235270615453_6"><a name="b84235270615453_6"></a><a name="b84235270615453_6"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.40404040404041%" id="mcps1.2.5.1.4"><p id="p1698611451928"><a name="p1698611451928"></a><a name="p1698611451928"></a><strong id="b84235270615457_6"><a name="b84235270615457_6"></a><a name="b84235270615457_6"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17986145228"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p298624512214"><a name="p298624512214"></a><a name="p298624512214"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.2 "><p id="p189861451729"><a name="p189861451729"></a><a name="p189861451729"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.3 "><p id="p5986194516217"><a name="p5986194516217"></a><a name="p5986194516217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.40404040404041%" headers="mcps1.2.5.1.4 "><p id="p6239864018"><a name="p6239864018"></a><a name="p6239864018"></a>Specifies the tag key. The tag key of a resource must be unique.</p>
    </td>
    </tr>
    <tr id="row119874451729"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p179876451323"><a name="p179876451323"></a><a name="p179876451323"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.2 "><p id="p139872451226"><a name="p139872451226"></a><a name="p139872451226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.3 "><p id="p7987845921"><a name="p7987845921"></a><a name="p7987845921"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.40404040404041%" headers="mcps1.2.5.1.4 "><p id="p142315716011"><a name="p142315716011"></a><a name="p142315716011"></a>Specifies the value.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    Example response when  **action**  is set to  **filter**

    ```
    {
        "resources": [
            {
                "resource_id": "d5a00c87-6b82-414a-a09e-59c37fff44d0",
                "resource_name": "Protected-Instance-c801",
                "resource_detail": {
                    "id": "d5a00c87-6b82-414a-a09e-59c37fff44d0",
                    "name": "Protected-Instance-c801",
                    "description": null,
                    "server_group_id": "525fbd01-d4d1-44fc-b341-6d734bcce245",
                    "status": "protected",
                    "progress": 100,
                    "source_server": "73aff1d7-48d2-494e-a9f1-a7d3ffad31ff",
                    "target_server": "0f6bc56b-a3bb-4707-a4fb-ccd4db5fac59",
                    "created_at": "2019-05-28 08:17:50.066",
                    "updated_at": "2019-05-30 01:40:00.74",
                    "priority_station": "source",
                    "attachment": [
                        {
                            "replication": "42e2016e-b96e-4f75-aa57-1377a9cb45e4",
                            "device": "/dev/vda"
                        }
                    ],
                    "tags": [
                        {
                            "key": "GH1111113fffffKdddddd",
                            "value": "aaappppppppddddddd"
                        }
                    ],
                    "metadata": {}
                },
                "tags": [
                    {
                        "key": "GH1111113fffffKdddddd",
                        "value": "aaappppppppddddddd"
                    }
                ]
            }
        ],
        "total_count": 1
    }
    ```

-   Example response when  **action**  is set to  **count**

    ```
    {
        "total_count": 1000
    }
    ```


## **Returned Value**<a name="section567644518219"></a>

-   Normal

    <a name="table667715456216"></a>
    <table><thead align="left"><tr id="row298714510212"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1198734518211"><a name="p1198734518211"></a><a name="p1198734518211"></a><strong id="b842352706175024_1"><a name="b842352706175024_1"></a><a name="b842352706175024_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p1498734512215"><a name="p1498734512215"></a><a name="p1498734512215"></a><strong id="b84235270615457_7"><a name="b84235270615457_7"></a><a name="b84235270615457_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7987164514218"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p129882451523"><a name="p129882451523"></a><a name="p129882451523"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p298834512212"><a name="p298834512212"></a><a name="p298834512212"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    <a name="table1867918454217"></a>
    <table><thead align="left"><tr id="row59881459212"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1598814451024"><a name="p1598814451024"></a><a name="p1598814451024"></a><strong id="b842352706175024_2"><a name="b842352706175024_2"></a><a name="b842352706175024_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p1798814516220"><a name="p1798814516220"></a><a name="p1798814516220"></a><strong id="b84235270615457_8"><a name="b84235270615457_8"></a><a name="b84235270615457_8"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19988144513218"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p098810454218"><a name="p098810454218"></a><a name="p098810454218"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p12988645627"><a name="p12988645627"></a><a name="p12988645627"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row12988104519214"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p189881845321"><a name="p189881845321"></a><a name="p189881845321"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1698815452212"><a name="p1698815452212"></a><a name="p1698815452212"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row898815451212"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p8988945429"><a name="p8988945429"></a><a name="p8988945429"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p7988124513214"><a name="p7988124513214"></a><a name="p7988124513214"></a>Insufficient permission.</p>
    </td>
    </tr>
    <tr id="row19885455216"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p179888451821"><a name="p179888451821"></a><a name="p179888451821"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1498813451215"><a name="p1498813451215"></a><a name="p1498813451215"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row16988154515213"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p69882455210"><a name="p69882455210"></a><a name="p69882455210"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2988144518212"><a name="p2988144518212"></a><a name="p2988144518212"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


