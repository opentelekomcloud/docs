# Show Container Details and List Objects<a name="obs_03_0029"></a>

This operation obtains container metadata and the list of objects in the container.

In an object list, objects are sorted by name in ascending order based on the comparison of binary memcmp\(\) functions.

## Method<a name="section39869956112928"></a>

**Table  1**  Method description

<a name="table36630378113016"></a>
<table><thead align="left"><tr id="row48730343113016"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5336715811413"><a name="p5336715811413"></a><a name="p5336715811413"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p51296332113016"><a name="p51296332113016"></a><a name="p51296332113016"></a><strong id="b39273688114629"><a name="b39273688114629"></a><a name="b39273688114629"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p61362190113016"><a name="p61362190113016"></a><a name="p61362190113016"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15388804113016"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38533588113016"><a name="p38533588113016"></a><a name="p38533588113016"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p66153545194815"><a name="p66153545194815"></a><a name="p66153545194815"></a>/v1/{account}/{container}{?limit,marker,end_marker,prefix,format,delimiter,path}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19784190113016"><a name="p19784190113016"></a><a name="p19784190113016"></a>Shows metadata of a specified container and lists objects, sorted by name in ascending order, in the container.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

**\{container\}**  indicates the name of a container.

This operation does not involve a request body.

## Example Request<a name="section16623225"></a>

Show container details for and list objects in the  **marktwain**  container, and ask for a JSON response:

```
curl -i $publicURL/marktwain?format=json -X GET -H "X-Auth-Token:$token"
```

## Request Headers<a name="section935707417105"></a>

Request URI parameters

<a name="table6312612217105"></a>
<table><thead align="left"><tr id="row2152913417105"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p6613826417105"><a name="p6613826417105"></a><a name="p6613826417105"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p3063031017105"><a name="p3063031017105"></a><a name="p3063031017105"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p4935347317105"><a name="p4935347317105"></a><a name="p4935347317105"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row833126117105"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p374351517105"><a name="p374351517105"></a><a name="p374351517105"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p3478926517105"><a name="p3478926517105"></a><a name="p3478926517105"></a>String</p>
<p id="p4466793317105"><a name="p4466793317105"></a><a name="p4466793317105"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p6133281117105"><a name="p6133281117105"></a><a name="p6133281117105"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row11460429171056"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p36034999171056"><a name="p36034999171056"></a><a name="p36034999171056"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p5541649117111"><a name="p5541649117111"></a><a name="p5541649117111"></a>String</p>
<p id="p2898637717111"><a name="p2898637717111"></a><a name="p2898637717111"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p1106935171056"><a name="p1106935171056"></a><a name="p1106935171056"></a>Unique name of the container.</p>
<p id="p33068020171218"><a name="p33068020171218"></a><a name="p33068020171218"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

Request header parameters

<a name="table4331219617105"></a>
<table><thead align="left"><tr id="row616552117105"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p2964523117105"><a name="p2964523117105"></a><a name="p2964523117105"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p231964817105"><a name="p231964817105"></a><a name="p231964817105"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p1330182717105"><a name="p1330182717105"></a><a name="p1330182717105"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3335590117105"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p1747344217105"><a name="p1747344217105"></a><a name="p1747344217105"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p606271217105"><a name="p606271217105"></a><a name="p606271217105"></a>String</p>
<p id="p5456441317105"><a name="p5456441317105"></a><a name="p5456441317105"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p5764131017105"><a name="p5764131017105"></a><a name="p5764131017105"></a>Authentication token.</p>
</td>
</tr>
<tr id="row4900974917105"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p1036676517105"><a name="p1036676517105"></a><a name="p1036676517105"></a>Accept</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p3440162117105"><a name="p3440162117105"></a><a name="p3440162117105"></a>String</p>
<p id="p4117913417105"><a name="p4117913417105"></a><a name="p4117913417105"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p4717558617105"><a name="p4717558617105"></a><a name="p4717558617105"></a>Similar to the <strong id="b60335392"><a name="b60335392"></a><a name="b60335392"></a>format</strong> query parameter, set this header to <strong id="b6147620"><a name="b6147620"></a><a name="b6147620"></a>application/json</strong>, <strong id="b55328585"><a name="b55328585"></a><a name="b55328585"></a>application/xml</strong>, or <strong id="b28195225"><a name="b28195225"></a><a name="b28195225"></a>text/xml</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request Query Parameters<a name="section58545636171022"></a>

[Table 2](#table53889649171022)  describes the query parameters of "Show Container Details and List Objects":

**Table  2**  Request query parameters

<a name="table53889649171022"></a>
<table><thead align="left"><tr id="row59416866171022"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.2.4.1.1"><p id="p48036802171022"><a name="p48036802171022"></a><a name="p48036802171022"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.2.4.1.2"><p id="p55110629171022"><a name="p55110629171022"></a><a name="p55110629171022"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.2.4.1.3"><p id="p44548109171022"><a name="p44548109171022"></a><a name="p44548109171022"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61990606171022"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p55183153171022"><a name="p55183153171022"></a><a name="p55183153171022"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p40650446171022"><a name="p40650446171022"></a><a name="p40650446171022"></a>Int</p>
<p id="p30309697171022"><a name="p30309697171022"></a><a name="p30309697171022"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p39166373171022"><a name="p39166373171022"></a><a name="p39166373171022"></a>Limits the number of objects in a query result. The value ranges from 0 to 10000. If the value is larger than 10000, an error is reported. The default value is <strong id="b1940750692104345"><a name="b1940750692104345"></a><a name="b1940750692104345"></a>10000</strong>.</p>
</td>
</tr>
<tr id="row16953040171022"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p31019014171022"><a name="p31019014171022"></a><a name="p31019014171022"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p29512212171022"><a name="p29512212171022"></a><a name="p29512212171022"></a>String</p>
<p id="p64283324171022"><a name="p64283324171022"></a><a name="p64283324171022"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p39566787171022"><a name="p39566787171022"></a><a name="p39566787171022"></a>Returns object names that are greater than the specified marker.</p>
</td>
</tr>
<tr id="row20556763171022"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p54485091171022"><a name="p54485091171022"></a><a name="p54485091171022"></a>end_marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p51216227171022"><a name="p51216227171022"></a><a name="p51216227171022"></a>String</p>
<p id="p58292864171022"><a name="p58292864171022"></a><a name="p58292864171022"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p24101544171022"><a name="p24101544171022"></a><a name="p24101544171022"></a>Returns object names that are smaller than the specified marker.</p>
</td>
</tr>
<tr id="row15587309171022"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p54612551171022"><a name="p54612551171022"></a><a name="p54612551171022"></a>format</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p61540538171022"><a name="p61540538171022"></a><a name="p61540538171022"></a>String</p>
<p id="p16993932171022"><a name="p16993932171022"></a><a name="p16993932171022"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p34331222171022"><a name="p34331222171022"></a><a name="p34331222171022"></a>Sets the format of the returned object list. The valid values are <strong id="b50404064216283"><a name="b50404064216283"></a><a name="b50404064216283"></a>plain</strong> (default), <strong id="b842352706162717"><a name="b842352706162717"></a><a name="b842352706162717"></a>json</strong>, and <strong id="b842352706162722"><a name="b842352706162722"></a><a name="b842352706162722"></a>xml</strong>. Its function is the same as <strong id="b842352706162739"><a name="b842352706162739"></a><a name="b842352706162739"></a>Accept</strong>.</p>
</td>
</tr>
<tr id="row40545544171022"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p62963636171022"><a name="p62963636171022"></a><a name="p62963636171022"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p66889752171022"><a name="p66889752171022"></a><a name="p66889752171022"></a>String</p>
<p id="p65136863171022"><a name="p65136863171022"></a><a name="p65136863171022"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p41594571171022"><a name="p41594571171022"></a><a name="p41594571171022"></a>Returns objects that have the specified prefix.</p>
</td>
</tr>
<tr id="row38806827171022"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p56345257171022"><a name="p56345257171022"></a><a name="p56345257171022"></a>delimiter</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p563071171022"><a name="p563071171022"></a><a name="p563071171022"></a>Char</p>
<p id="p5067643171022"><a name="p5067643171022"></a><a name="p5067643171022"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p7825929171022"><a name="p7825929171022"></a><a name="p7825929171022"></a>Returns the object names that are nested in the container.</p>
</td>
</tr>
<tr id="row3324501171022"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p849189171022"><a name="p849189171022"></a><a name="p849189171022"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p1675502171022"><a name="p1675502171022"></a><a name="p1675502171022"></a>String</p>
<p id="p15079519171022"><a name="p15079519171022"></a><a name="p15079519171022"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p13481487171022"><a name="p13481487171022"></a><a name="p13481487171022"></a>Returns the object names that are nested in the specified path. Equivalent to setting <strong id="b14393865"><a name="b14393865"></a><a name="b14393865"></a>delimiter</strong> to <strong id="b62435929"><a name="b62435929"></a><a name="b62435929"></a>/</strong> and <strong id="b25052449"><a name="b25052449"></a><a name="b25052449"></a>prefix</strong> to the path with a slash (/) at the end.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>OBS \(compatible with OpenStack Swift\) does not have the following issue that exists in OpenStack Swift: If the first character of an object is set to the  **delimiter**  parameter, the expected result cannot be correctly returned.  
>Example:  
>bucket01 contains the following object:  
>obj0  
>If the  **delimiter=o**  parameter is used in the query, OBS \(compatible with OpenStack Swift\) returns the following information:  
>o  
>OpenStack Swift, however, returns the following information \(which is incorrect, equivalent to a failure to impalement the function\):  
>obj0  

>![](/images/icon-note.gif) **NOTE:**   
>In terms of setting the  **path**  parameter, OBS \(compatible with OpenStack Swift\) does not have the following issue that exists in OpenStack Swift: When the  **path**  parameter is used, subdirectories cannot be shown. The specific difference is as follows:  

<a name="table5725145215345"></a>
<table><thead align="left"><tr id="row3927369915345"><th class="cellrowborder" colspan="3" valign="top" id="mcps1.1.4.1.1"><p id="p31265954153436"><a name="p31265954153436"></a><a name="p31265954153436"></a>Same prerequisites:</p>
<p id="p1330570215358"><a name="p1330570215358"></a><a name="p1330570215358"></a>The following objects exist in a container:</p>
<p id="p13123997153530"><a name="p13123997153530"></a><a name="p13123997153530"></a>o/1</p>
<p id="p51007114153530"><a name="p51007114153530"></a><a name="p51007114153530"></a>o/2</p>
<p id="p56410842153530"><a name="p56410842153530"></a><a name="p56410842153530"></a>o/subdir1/1</p>
<p id="p10422185153548"><a name="p10422185153548"></a><a name="p10422185153548"></a>If the same request is sent to OpenStack Swift and OBS (compatible with OpenStack Swift), the results are different as follows:</p>
</th>
</tr>
</thead>
<tbody><tr id="row2931161715345"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p2543073915345"><a name="p2543073915345"></a><a name="p2543073915345"></a>OpenStack Swift</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.1.4.1.1 "><p id="p20359220153717"><a name="p20359220153717"></a><a name="p20359220153717"></a>The result is as follows:</p>
<p id="p49015254153717"><a name="p49015254153717"></a><a name="p49015254153717"></a>o/1</p>
<p id="p38484108153717"><a name="p38484108153717"></a><a name="p38484108153717"></a>o/2</p>
<p id="p10812653153717"><a name="p10812653153717"></a><a name="p10812653153717"></a><em id="i47843365"><a name="i47843365"></a><a name="i47843365"></a>(Lack of o/subdir1/1)</em></p>
</td>
</tr>
<tr id="row3180705815345"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p2623490715345"><a name="p2623490715345"></a><a name="p2623490715345"></a>OBS</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.1.4.1.1 "><p id="p63100707153751"><a name="p63100707153751"></a><a name="p63100707153751"></a>The result is as follows:</p>
<p id="p31035452153751"><a name="p31035452153751"></a><a name="p31035452153751"></a>o/1</p>
<p id="p10883614153751"><a name="p10883614153751"></a><a name="p10883614153751"></a>o/2</p>
<p id="p30843666153751"><a name="p30843666153751"></a><a name="p30843666153751"></a>o/subdir1/1</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section30570743"></a>

<a name="table59658522144238"></a>
<table><thead align="left"><tr id="row55181501144238"><th class="cellrowborder" valign="top" width="38.279999999999994%" id="mcps1.1.4.1.1"><p id="p16639091195249"><a name="p16639091195249"></a><a name="p16639091195249"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="15.509999999999998%" id="mcps1.1.4.1.2"><p id="p7217399195249"><a name="p7217399195249"></a><a name="p7217399195249"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.21%" id="mcps1.1.4.1.3"><p id="p43692246195249"><a name="p43692246195249"></a><a name="p43692246195249"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13548066144238"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p23651575144238"><a name="p23651575144238"></a><a name="p23651575144238"></a>Accept-Ranges</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p36729408144238"><a name="p36729408144238"></a><a name="p36729408144238"></a>String</p>
<p id="p5978127319524"><a name="p5978127319524"></a><a name="p5978127319524"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p22292070144238"><a name="p22292070144238"></a><a name="p22292070144238"></a>Type of ranges that the object accepts.</p>
</td>
</tr>
<tr id="row66410903144238"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p4540407515255"><a name="p4540407515255"></a><a name="p4540407515255"></a>X-Container-Bytes-Used</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p51190430144238"><a name="p51190430144238"></a><a name="p51190430144238"></a>Int</p>
<p id="p18583729195212"><a name="p18583729195212"></a><a name="p18583729195212"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p52784162144238"><a name="p52784162144238"></a><a name="p52784162144238"></a>Total number of bytes that are stored in OBS for the container.</p>
</td>
</tr>
<tr id="row178807761556"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p390567281556"><a name="p390567281556"></a><a name="p390567281556"></a>X-Container-Object-Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p94784091556"><a name="p94784091556"></a><a name="p94784091556"></a>Int</p>
<p id="p1596410195214"><a name="p1596410195214"></a><a name="p1596410195214"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p295536661556"><a name="p295536661556"></a><a name="p295536661556"></a>Number of objects in the container.</p>
</td>
</tr>
<tr id="row6423655915944"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p3577876015944"><a name="p3577876015944"></a><a name="p3577876015944"></a>X-Container-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p1239840915944"><a name="p1239840915944"></a><a name="p1239840915944"></a>String</p>
<p id="p23252487195217"><a name="p23252487195217"></a><a name="p23252487195217"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p6474706715944"><a name="p6474706715944"></a><a name="p6474706715944"></a>Custom container metadata item, where <strong id="b2615989"><a name="b2615989"></a><a name="b2615989"></a>{name}</strong> is the name of the metadata item.</p>
</td>
</tr>
<tr id="row40213248195138"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p1948451195156"><a name="p1948451195156"></a><a name="p1948451195156"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p23606827195156"><a name="p23606827195156"></a><a name="p23606827195156"></a>String</p>
<p id="p11134852195156"><a name="p11134852195156"></a><a name="p11134852195156"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p29507848195156"><a name="p29507848195156"></a><a name="p29507848195156"></a>If the operation succeeds, the value is the length of the object list information.</p>
<p id="p64244044195156"><a name="p64244044195156"></a><a name="p64244044195156"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row12189558195139"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p59030245195156"><a name="p59030245195156"></a><a name="p59030245195156"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p16720526195156"><a name="p16720526195156"></a><a name="p16720526195156"></a>String</p>
<p id="p16267010195156"><a name="p16267010195156"></a><a name="p16267010195156"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p42559413195156"><a name="p42559413195156"></a><a name="p42559413195156"></a>MIME type of the text in the response body.</p>
</td>
</tr>
<tr id="row55397376195139"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p21517012195156"><a name="p21517012195156"></a><a name="p21517012195156"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p65156448195156"><a name="p65156448195156"></a><a name="p65156448195156"></a>Datetime</p>
<p id="p49537120195156"><a name="p49537120195156"></a><a name="p49537120195156"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p53083813195156"><a name="p53083813195156"></a><a name="p53083813195156"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row64699794195139"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p43394572195156"><a name="p43394572195156"></a><a name="p43394572195156"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p25299449195156"><a name="p25299449195156"></a><a name="p25299449195156"></a>Uuid</p>
<p id="p26368455195156"><a name="p26368455195156"></a><a name="p26368455195156"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p55470110195156"><a name="p55470110195156"></a><a name="p55470110195156"></a>Unique transaction identifier.</p>
</td>
</tr>
<tr id="row7304758203017"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.1.4.1.1 "><p id="p18306458183016"><a name="p18306458183016"></a><a name="p18306458183016"></a>X-Timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p45791557183114"><a name="p45791557183114"></a><a name="p45791557183114"></a>Datetime</p>
<p id="p022164513314"><a name="p022164513314"></a><a name="p022164513314"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.1.4.1.3 "><p id="p28471953216"><a name="p28471953216"></a><a name="p28471953216"></a>Indicates the time when the container was created.</p>
<p id="p1784717919328"><a name="p1784717919328"></a><a name="p1784717919328"></a>The format is a UNIX Epoch timestamp.</p>
</td>
</tr>
</tbody>
</table>

## Response Body Parameters<a name="section29255058162616"></a>

If the response format is json or xml, object details are shown.  [Table 3](#table64595445162712)  describes the response body parameters:

**Table  3**  Response body parameters

<a name="table64595445162712"></a>
<table><thead align="left"><tr id="row9655044162712"><th class="cellrowborder" valign="top" width="19.38%" id="mcps1.2.4.1.1"><p id="p59205779162712"><a name="p59205779162712"></a><a name="p59205779162712"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.64%" id="mcps1.2.4.1.2"><p id="p30938800162712"><a name="p30938800162712"></a><a name="p30938800162712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.97999999999999%" id="mcps1.2.4.1.3"><p id="p23014890162712"><a name="p23014890162712"></a><a name="p23014890162712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5807421162712"><td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.4.1.1 "><p id="p639084162712"><a name="p639084162712"></a><a name="p639084162712"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.4.1.2 "><p id="p51765868162712"><a name="p51765868162712"></a><a name="p51765868162712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.97999999999999%" headers="mcps1.2.4.1.3 "><p id="p32285797162712"><a name="p32285797162712"></a><a name="p32285797162712"></a>Name of the object.</p>
</td>
</tr>
<tr id="row22136718162712"><td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.4.1.1 "><p id="p48243694162712"><a name="p48243694162712"></a><a name="p48243694162712"></a>hash</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.4.1.2 "><p id="p15425114162712"><a name="p15425114162712"></a><a name="p15425114162712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.97999999999999%" headers="mcps1.2.4.1.3 "><p id="p41474747162712"><a name="p41474747162712"></a><a name="p41474747162712"></a>MD5 checksum value of the object content.</p>
</td>
</tr>
<tr id="row37728411162712"><td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.4.1.1 "><p id="p36102470162712"><a name="p36102470162712"></a><a name="p36102470162712"></a>bytes</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.4.1.2 "><p id="p38618970162712"><a name="p38618970162712"></a><a name="p38618970162712"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="67.97999999999999%" headers="mcps1.2.4.1.3 "><p id="p41128829162712"><a name="p41128829162712"></a><a name="p41128829162712"></a>Total number of bytes that are stored in OBS for the object.</p>
</td>
</tr>
<tr id="row5296068385733"><td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.4.1.1 "><p id="p6195689485733"><a name="p6195689485733"></a><a name="p6195689485733"></a>content_type</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.4.1.2 "><p id="p5245255585733"><a name="p5245255585733"></a><a name="p5245255585733"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.97999999999999%" headers="mcps1.2.4.1.3 "><p id="p2079855285733"><a name="p2079855285733"></a><a name="p2079855285733"></a>Content type of the object.</p>
</td>
</tr>
<tr id="row6337366785858"><td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.4.1.1 "><p id="p3299339285858"><a name="p3299339285858"></a><a name="p3299339285858"></a>last_modified</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.4.1.2 "><p id="p5521907785858"><a name="p5521907785858"></a><a name="p5521907785858"></a>Datetime</p>
</td>
<td class="cellrowborder" valign="top" width="67.97999999999999%" headers="mcps1.2.4.1.3 "><p id="p4356026785858"><a name="p4356026785858"></a><a name="p4356026785858"></a>Date and time when the object was last modified.</p>
</td>
</tr>
</tbody>
</table>

## Show Container Details: Plain Format<a name="section2201390"></a>

Show metadata of the  **testcontainer**  container and list objects. Do not set a query parameter. Use the default plain response format.

```
curl -i http://172.28.54.10:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/testcontainer -H "x-auth-token:c1f21a34cce442efbd4957018263cc2c" -X GET
```

```
HTTP/1.1 200 OK
X-Trans-Id: tx0000015133a73737370a1-35e31d5be7
Accept-Ranges: bytes
Content-Length: 10
Content-Type: text/plain;charset=UTF-8
Date: Mon, 23 Nov 2015 09:22:58 GMT
X-Container-Bytes-Used: 5027
X-Container-Object-Count: 2
X-Timestamp: 1448270495.79460

[10 Byte data content]
```

## Show Container Details: JSON Format<a name="section60098234144536"></a>

Show metadata of the  **testcontainer**  container and list objects. Specify the JSON response format.

```
curl -i http://172.28.54.10:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/testcontainer?format=json -H "x-auth-token:c1f21a34cce442efbd4957018263cc2c" -X GET
```

A JSON response is returned. The response body contains object information such as  **hash**,  **bytes**, and  **content\_type**.

```
HTTP/1.1 200 OK
X-Trans-Id: tx0000015133aa2422370a1-13b8629ff1
Accept-Ranges: bytes
Content-Length: 335
Content-Type: application/json;charset=UTF-8
Date: Mon, 23 Nov 2015 09:26:09 GMT
X-Container-Bytes-Used: 5027
X-Container-Object-Count: 2
X-Timestamp: 1448270495.79460

[
    {
        "hash": "0481164fe6931fb86ca4d8e8b3689efb", 
        "bytes": 4337, 
        "content_type": "application/octet-stream", 
        "last_modified": "2015-11-23T09:22:22.859650", 
        "name": "jack"
    },
    {
        "hash": "1e5d213baf0069e26805f5d4efc900fe", 
        "bytes": 690, 
        "content_type": "application/octet-stream", 
        "last_modified": "2015-11-23T09:22:44.748920", 
        "name": "rose"
    }
]
```

