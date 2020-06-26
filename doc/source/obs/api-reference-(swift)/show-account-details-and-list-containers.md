# Show Account Details and List Containers<a name="obs_03_0016"></a>

This operation obtains account metadata and the list of containers in the account.

In the container list, container names are sorted in ascending order based on ASCII code.

>![](/images/icon-note.gif) **NOTE:**   
>OBS \(compatible with OpenStack Swift\) employs a mechanism that automatically deletes accounts and their data in the background. Therefore, there is no account deletion status corresponding to OpenStack Swift.  
>The specific differences are as follows:  
>Account metadata does not include the X-Account-Status.  
>Showing account details does not involve the 410 Gone return code.  

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
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52757727113245"><a name="p52757727113245"></a><a name="p52757727113245"></a>/v1/{account}{?limit,marker,end_marker,format,prefix,delimiter}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19784190113016"><a name="p19784190113016"></a><a name="p19784190113016"></a>Shows details of a specified account and lists the containers, sorted by name in ascending order, in the account.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

This operation does not involve a request body.

## Example Request<a name="section16623225"></a>

Show account details and list containers, and ask for a JSON response:

```
curl -i $publicURL?format=json -X GET -H "X-Auth-Token:$token"
```

## Request Headers<a name="section25088150142916"></a>

Request URI parameters

<a name="table46142002143624"></a>
<table><thead align="left"><tr id="row38562591143624"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p36562205143624"><a name="p36562205143624"></a><a name="p36562205143624"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p11628894143624"><a name="p11628894143624"></a><a name="p11628894143624"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p21746897143624"><a name="p21746897143624"></a><a name="p21746897143624"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15796443143624"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p4443488143624"><a name="p4443488143624"></a><a name="p4443488143624"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p24378262143624"><a name="p24378262143624"></a><a name="p24378262143624"></a>String</p>
<p id="p18077771143624"><a name="p18077771143624"></a><a name="p18077771143624"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p55013324143624"><a name="p55013324143624"></a><a name="p55013324143624"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
</tbody>
</table>

Request header parameters

<a name="table34204931143044"></a>
<table><thead align="left"><tr id="row58034645143044"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p3185823143044"><a name="p3185823143044"></a><a name="p3185823143044"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p40763865143044"><a name="p40763865143044"></a><a name="p40763865143044"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p54740279143044"><a name="p54740279143044"></a><a name="p54740279143044"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42998427143044"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p60320524143044"><a name="p60320524143044"></a><a name="p60320524143044"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p54124270143044"><a name="p54124270143044"></a><a name="p54124270143044"></a>String</p>
<p id="p63510313143110"><a name="p63510313143110"></a><a name="p63510313143110"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p21989736143044"><a name="p21989736143044"></a><a name="p21989736143044"></a>Authentication token.</p>
</td>
</tr>
<tr id="row63689902143044"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p42395927143148"><a name="p42395927143148"></a><a name="p42395927143148"></a>Accept</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p49885939143148"><a name="p49885939143148"></a><a name="p49885939143148"></a>String</p>
<p id="p3912167714320"><a name="p3912167714320"></a><a name="p3912167714320"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p45612269143233"><a name="p45612269143233"></a><a name="p45612269143233"></a>Similar to the <strong id="b45314905"><a name="b45314905"></a><a name="b45314905"></a>format</strong> query parameter, set this header to <strong id="b5180964"><a name="b5180964"></a><a name="b5180964"></a>application/json</strong>, <strong id="b46628683"><a name="b46628683"></a><a name="b46628683"></a>application/xml</strong>, or <strong id="b17004965"><a name="b17004965"></a><a name="b17004965"></a>text/xml</strong>.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>If the value of  **Accept**  is invalid, OBS \(compatible with OpenStack Swift\) returns the 406 \(Not Acceptable\) error code. Then, OpenStack Swift will process the request based on the default value of  **Accept**.  

## Request Query Parameters<a name="section5103708"></a>

**Table  2**  Request query parameters

<a name="table2272850011511"></a>
<table><thead align="left"><tr id="row6616787111511"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.2.4.1.1"><p id="p5221421211511"><a name="p5221421211511"></a><a name="p5221421211511"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.2.4.1.2"><p id="p149275011511"><a name="p149275011511"></a><a name="p149275011511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.2.4.1.3"><p id="p5380390811511"><a name="p5380390811511"></a><a name="p5380390811511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1447313211511"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p3147304011511"><a name="p3147304011511"></a><a name="p3147304011511"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p6628834111511"><a name="p6628834111511"></a><a name="p6628834111511"></a>Int</p>
<p id="p3455555314396"><a name="p3455555314396"></a><a name="p3455555314396"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p64656311511"><a name="p64656311511"></a><a name="p64656311511"></a>Limits the number of containers in a query result. The value ranges from 0 to 10000. If the value is larger than 10000, an error is reported. The default value is <strong id="b75978479175449"><a name="b75978479175449"></a><a name="b75978479175449"></a>10000</strong>.</p>
</td>
</tr>
<tr id="row581906811511"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p158250511511"><a name="p158250511511"></a><a name="p158250511511"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p6107409911511"><a name="p6107409911511"></a><a name="p6107409911511"></a>String</p>
<p id="p30504646143919"><a name="p30504646143919"></a><a name="p30504646143919"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p4805497711511"><a name="p4805497711511"></a><a name="p4805497711511"></a>Returns container names that are greater than the specified marker.</p>
</td>
</tr>
<tr id="row2984161311511"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p125161311511"><a name="p125161311511"></a><a name="p125161311511"></a>end_marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p27063604115613"><a name="p27063604115613"></a><a name="p27063604115613"></a>String</p>
<p id="p58024375143921"><a name="p58024375143921"></a><a name="p58024375143921"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p2455611111511"><a name="p2455611111511"></a><a name="p2455611111511"></a>Returns container names that are smaller than the specified marker.</p>
</td>
</tr>
<tr id="row1967840711511"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p5044710711511"><a name="p5044710711511"></a><a name="p5044710711511"></a>format</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p40147841115613"><a name="p40147841115613"></a><a name="p40147841115613"></a>String</p>
<p id="p42315028143925"><a name="p42315028143925"></a><a name="p42315028143925"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p255712211511"><a name="p255712211511"></a><a name="p255712211511"></a>Sets the format of the returned container list. The valid values are <strong id="b50404064216283"><a name="b50404064216283"></a><a name="b50404064216283"></a>plain</strong> (default), <strong id="b842352706162717"><a name="b842352706162717"></a><a name="b842352706162717"></a>json</strong>, and <strong id="b842352706162722"><a name="b842352706162722"></a><a name="b842352706162722"></a>xml</strong>. Its function is the same as <strong id="b842352706162739"><a name="b842352706162739"></a><a name="b842352706162739"></a>Accept</strong>.</p>
</td>
</tr>
<tr id="row2301410311511"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p5220306711511"><a name="p5220306711511"></a><a name="p5220306711511"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p16654175115613"><a name="p16654175115613"></a><a name="p16654175115613"></a>String</p>
<p id="p14938020143938"><a name="p14938020143938"></a><a name="p14938020143938"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p4778991511511"><a name="p4778991511511"></a><a name="p4778991511511"></a>Returns containers that have the specified prefix.</p>
</td>
</tr>
<tr id="row2745605411511"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.2.4.1.1 "><p id="p934788211511"><a name="p934788211511"></a><a name="p934788211511"></a>delimiter</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.2.4.1.2 "><p id="p1898097111511"><a name="p1898097111511"></a><a name="p1898097111511"></a>Char</p>
<p id="p18750875144242"><a name="p18750875144242"></a><a name="p18750875144242"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p6106364811511"><a name="p6106364811511"></a><a name="p6106364811511"></a>Returns the container names that are nested in the account.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section30570743"></a>

**Table  3**  Response header parameters

<a name="table59658522144238"></a>
<table><thead align="left"><tr id="row55181501144238"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.4.1.1"><p id="p29104717144238"><a name="p29104717144238"></a><a name="p29104717144238"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.2.4.1.2"><p id="p8671853144238"><a name="p8671853144238"></a><a name="p8671853144238"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.75%" id="mcps1.2.4.1.3"><p id="p31331502144238"><a name="p31331502144238"></a><a name="p31331502144238"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13548066144238"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p23651575144238"><a name="p23651575144238"></a><a name="p23651575144238"></a>Accept-Ranges</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p36729408144238"><a name="p36729408144238"></a><a name="p36729408144238"></a>String</p>
<p id="p19868159191351"><a name="p19868159191351"></a><a name="p19868159191351"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p22292070144238"><a name="p22292070144238"></a><a name="p22292070144238"></a>Type of ranges that the object accepts.</p>
</td>
</tr>
<tr id="row66410903144238"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p4540407515255"><a name="p4540407515255"></a><a name="p4540407515255"></a>X-Account-Bytes-Used</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p51190430144238"><a name="p51190430144238"></a><a name="p51190430144238"></a>Int</p>
<p id="p35340739191356"><a name="p35340739191356"></a><a name="p35340739191356"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p52784162144238"><a name="p52784162144238"></a><a name="p52784162144238"></a>Total number of bytes that are stored in OBS for the account.</p>
</td>
</tr>
<tr id="row5295417144238"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p26275653144238"><a name="p26275653144238"></a><a name="p26275653144238"></a>X-Account-Container-Count</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p47953182144238"><a name="p47953182144238"></a><a name="p47953182144238"></a>Int</p>
<p id="p22820231191359"><a name="p22820231191359"></a><a name="p22820231191359"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p59002539144238"><a name="p59002539144238"></a><a name="p59002539144238"></a>Number of containers in the account.</p>
</td>
</tr>
<tr id="row178807761556"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p390567281556"><a name="p390567281556"></a><a name="p390567281556"></a>X-Account-Object-Count</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p94784091556"><a name="p94784091556"></a><a name="p94784091556"></a>Int</p>
<p id="p6187295419141"><a name="p6187295419141"></a><a name="p6187295419141"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p295536661556"><a name="p295536661556"></a><a name="p295536661556"></a>Number of objects in the account.</p>
</td>
</tr>
<tr id="row6423655915944"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p3577876015944"><a name="p3577876015944"></a><a name="p3577876015944"></a>X-Account-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p1239840915944"><a name="p1239840915944"></a><a name="p1239840915944"></a>String</p>
<p id="p2381648719145"><a name="p2381648719145"></a><a name="p2381648719145"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p6474706715944"><a name="p6474706715944"></a><a name="p6474706715944"></a>Custom account metadata item, where <strong id="b52213166"><a name="b52213166"></a><a name="b52213166"></a>{name}</strong> is the name of the metadata item.</p>
</td>
</tr>
<tr id="row37906154201550"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p50499596201550"><a name="p50499596201550"></a><a name="p50499596201550"></a>X-Account-Meta-Quota-Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p8465208201615"><a name="p8465208201615"></a><a name="p8465208201615"></a>Int</p>
<p id="p9078015201615"><a name="p9078015201615"></a><a name="p9078015201615"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p11392311201550"><a name="p11392311201550"></a><a name="p11392311201550"></a>Quota of the account.</p>
</td>
</tr>
<tr id="row52232919105750"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p45638582105758"><a name="p45638582105758"></a><a name="p45638582105758"></a>X-Account-Meta-Temp-URL-Key</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p5737700105758"><a name="p5737700105758"></a><a name="p5737700105758"></a>String</p>
<p id="p2434462191419"><a name="p2434462191419"></a><a name="p2434462191419"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p62100566105758"><a name="p62100566105758"></a><a name="p62100566105758"></a>Secret key value for TempURL.</p>
</td>
</tr>
<tr id="row48861833105755"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p13821293105758"><a name="p13821293105758"></a><a name="p13821293105758"></a>X-Account-Meta-Temp-URL-Key-2</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p45782938105758"><a name="p45782938105758"></a><a name="p45782938105758"></a>String</p>
<p id="p52134397191443"><a name="p52134397191443"></a><a name="p52134397191443"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p17430479105758"><a name="p17430479105758"></a><a name="p17430479105758"></a>A second secret key value for TempURL.</p>
</td>
</tr>
<tr id="row3636297215548"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p5971961115548"><a name="p5971961115548"></a><a name="p5971961115548"></a>X-Account-Project-Domain-Id</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p545034715548"><a name="p545034715548"></a><a name="p545034715548"></a>String</p>
<p id="p21350323191449"><a name="p21350323191449"></a><a name="p21350323191449"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p3882498015548"><a name="p3882498015548"></a><a name="p3882498015548"></a>ID of the domain to which the account belongs.</p>
</td>
</tr>
<tr id="row22274331191328"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p25128479191336"><a name="p25128479191336"></a><a name="p25128479191336"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p22140918191336"><a name="p22140918191336"></a><a name="p22140918191336"></a>String</p>
<p id="p65050537191336"><a name="p65050537191336"></a><a name="p65050537191336"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p181299280512"><a name="p181299280512"></a><a name="p181299280512"></a>If the operation succeeds, the value is the length of the container list information.</p>
<p id="p42983877191336"><a name="p42983877191336"></a><a name="p42983877191336"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row21527884191330"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p13007484191336"><a name="p13007484191336"></a><a name="p13007484191336"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p46973307191336"><a name="p46973307191336"></a><a name="p46973307191336"></a>String</p>
<p id="p20106582191336"><a name="p20106582191336"></a><a name="p20106582191336"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p18020483191336"><a name="p18020483191336"></a><a name="p18020483191336"></a>Type of the text in the response body.</p>
</td>
</tr>
<tr id="row37183535191330"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p50703890191336"><a name="p50703890191336"></a><a name="p50703890191336"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p13374419191336"><a name="p13374419191336"></a><a name="p13374419191336"></a>Datetime</p>
<p id="p53260907191336"><a name="p53260907191336"></a><a name="p53260907191336"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p19166217191336"><a name="p19166217191336"></a><a name="p19166217191336"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row56276345191331"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p13529200191336"><a name="p13529200191336"></a><a name="p13529200191336"></a>X-Trans-Id</p>
<p id="p56739906191336"><a name="p56739906191336"></a><a name="p56739906191336"></a></p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p22123378191336"><a name="p22123378191336"></a><a name="p22123378191336"></a>Uuid</p>
<p id="p64892680191336"><a name="p64892680191336"></a><a name="p64892680191336"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p21815704191336"><a name="p21815704191336"></a><a name="p21815704191336"></a>Unique transaction identifier.</p>
<p id="p21232114191336"><a name="p21232114191336"></a><a name="p21232114191336"></a></p>
</td>
</tr>
<tr id="row1691878919160"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.4.1.1 "><p id="p2824464619160"><a name="p2824464619160"></a><a name="p2824464619160"></a>X-Timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.2.4.1.2 "><p id="p25289134191624"><a name="p25289134191624"></a><a name="p25289134191624"></a>Datetime</p>
<p id="p26275621191624"><a name="p26275621191624"></a><a name="p26275621191624"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="40.75%" headers="mcps1.2.4.1.3 "><p id="p31569453191628"><a name="p31569453191628"></a><a name="p31569453191628"></a>Object creation time and date, in UNIX Epoch timestamp format.</p>
</td>
</tr>
</tbody>
</table>

## Response Body Parameters<a name="section29255058162616"></a>

If the response format is json or xml, container details are shown. The following table describes the response body parameters:

**Table  4**  Response body parameters

<a name="table64595445162712"></a>
<table><thead align="left"><tr id="row9655044162712"><th class="cellrowborder" valign="top" width="19.38%" id="mcps1.2.4.1.1"><p id="p59205779162712"><a name="p59205779162712"></a><a name="p59205779162712"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="9.51%" id="mcps1.2.4.1.2"><p id="p30938800162712"><a name="p30938800162712"></a><a name="p30938800162712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71.11%" id="mcps1.2.4.1.3"><p id="p23014890162712"><a name="p23014890162712"></a><a name="p23014890162712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5807421162712"><td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.4.1.1 "><p id="p639084162712"><a name="p639084162712"></a><a name="p639084162712"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="9.51%" headers="mcps1.2.4.1.2 "><p id="p51765868162712"><a name="p51765868162712"></a><a name="p51765868162712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71.11%" headers="mcps1.2.4.1.3 "><p id="p32285797162712"><a name="p32285797162712"></a><a name="p32285797162712"></a>Name of the container.</p>
</td>
</tr>
<tr id="row22136718162712"><td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.4.1.1 "><p id="p48243694162712"><a name="p48243694162712"></a><a name="p48243694162712"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="9.51%" headers="mcps1.2.4.1.2 "><p id="p15425114162712"><a name="p15425114162712"></a><a name="p15425114162712"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="71.11%" headers="mcps1.2.4.1.3 "><p id="p41474747162712"><a name="p41474747162712"></a><a name="p41474747162712"></a>Number of objects in the container.</p>
</td>
</tr>
<tr id="row37728411162712"><td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.4.1.1 "><p id="p36102470162712"><a name="p36102470162712"></a><a name="p36102470162712"></a>bytes</p>
</td>
<td class="cellrowborder" valign="top" width="9.51%" headers="mcps1.2.4.1.2 "><p id="p38618970162712"><a name="p38618970162712"></a><a name="p38618970162712"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="71.11%" headers="mcps1.2.4.1.3 "><p id="p41128829162712"><a name="p41128829162712"></a><a name="p41128829162712"></a>Total number of bytes that are stored in OBS for objects.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>For performance purpose, among the response headers, OBS \(compatible with OpenStack Swift\) does not update  **X-Account-Bytes-Used**,  **X-Account-Container-Count**, and  **X-Account-Object-Count**  in real time.  

## Show Account Details and List Containers \(Asking for a Plain Response\)<a name="section2201390"></a>

Show account details and list containers. Do not set a query parameter. Use the default plain response format.

```
curl -i -H "X-auth-token:b8b574e33b0a4f74a1961bed1b4784b8" "http://172.28.5.30:80/v1/AUTH_0ce042a9be6140769b12c1001d41bcf9" -X GET
```

```
HTTP/1.1 200 OK
X-Trans-Id: tx19cbb9377b2eb8a164ac8-c40e979e9b
Accept-Ranges: bytes
Content-Type: text/plain;charset=UTF-8
Date: Wed, 16 Sep 2015 07:10:18 GMT
X-Account-Bytes-Used: 0
X-Account-Container-Count: 3
X-Account-Object-Count: 0
X-Account-Project-Domain-Id: default
X-Timestamp: 1442371465.946
Content-Length: 23

[23 Byte data content]
```

## Show Account Details and List Containers \(Asking for an XML Response\)<a name="section60098234144536"></a>

Show account details and list containers. Use the  **prefix=abc**  query parameter, and set the response format to  **xml**.

```
curl -i -H "X-auth-token:b8b574e33b0a4f74a1961bed1b4784b8" "http://172.28.5.30:80/v1/AUTH_0ce042a9be6140769b12c1001d41bcf9?format=xml&prefix=abc"      -X GET
```

```
HTTP/1.1 200 OK
X-Trans-Id: tx200c074b35f50910061e7-067ab2f1d4
Accept-Ranges: bytes
Content-Type: application/xml;charset=UTF-8
Date: Wed, 16 Sep 2015 07:12:09 GMT
X-Account-Bytes-Used: 0
X-Account-Container-Count: 3
X-Account-Object-Count: 0
X-Account-Project-Domain-Id: default
X-timestamp: 1442371465.946
Content-Length: 256

<?xml version="1.0" encoding="UTF-8"?>
<account name="AUTH_0ce042a9be6140769b12c1001d41bcf9">
<container><name>abcc122</name><count>0</count><bytes>0</bytes></container>
<container><name>abcd123</name><count>0</count><bytes>0</bytes></container>
</account>
```

