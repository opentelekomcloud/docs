# Create/Update/Delete Account Metadata<a name="obs_03_0020"></a>

Users can send requests to create, update, or delete account metadata.

For details about metadata rules, see  [Naming Rules](naming-rules.md).

## Method<a name="section3051751717825"></a>

**Table  1**  Method description

<a name="table5599981617825"></a>
<table><thead align="left"><tr id="row1708100417825"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p4138407817825"><a name="p4138407817825"></a><a name="p4138407817825"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3711316617825"><a name="p3711316617825"></a><a name="p3711316617825"></a><strong id="b6558304317825"><a name="b6558304317825"></a><a name="b6558304317825"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1062627917825"><a name="p1062627917825"></a><a name="p1062627917825"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2903806617825"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p327315417825"><a name="p327315417825"></a><a name="p327315417825"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6379890217825"><a name="p6379890217825"></a><a name="p6379890217825"></a>/v1/{account}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p32856717825"><a name="p32856717825"></a><a name="p32856717825"></a>Creates, updates, or deletes account metadata.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

Metadata creation or update depends on whether the specified metadata exists. Metadata is created if it does not exist. Metadata is updated if it exists.

This operation does not involve a request body.

## Example Request<a name="section58521383"></a>

Create or update metadata:

```
curl -i $publicURL -X POST -H "X-Auth-Token:$token" -H "X-Account-Meta-name:value"
```

Delete metadata:

```
curl -i $publicURL -X POST -H "X-Auth-Token:$token" -H "X-Remove-Account-Meta-name:value"
```

## Request Query Parameters<a name="section45363461144314"></a>

<a name="table50561716144314"></a>
<table><thead align="left"><tr id="row45973958144314"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p32903079144314"><a name="p32903079144314"></a><a name="p32903079144314"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p28480451144314"><a name="p28480451144314"></a><a name="p28480451144314"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p25610510144314"><a name="p25610510144314"></a><a name="p25610510144314"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13798066144314"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p43901557144314"><a name="p43901557144314"></a><a name="p43901557144314"></a>bulk-delete</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p66365237144314"><a name="p66365237144314"></a><a name="p66365237144314"></a>String</p>
<p id="p60416223144314"><a name="p60416223144314"></a><a name="p60416223144314"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p61875876144314"><a name="p61875876144314"></a><a name="p61875876144314"></a>Bulk-deletes containers. This parameter is used with the deletion list file.</p>
<p id="p20011978144314"><a name="p20011978144314"></a><a name="p20011978144314"></a>A maximum of 10,000 empty containers can be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section39956945"></a>

Request URI parameters

<a name="table17760770152418"></a>
<table><thead align="left"><tr id="row7106630152418"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p38766128152418"><a name="p38766128152418"></a><a name="p38766128152418"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p7675774152418"><a name="p7675774152418"></a><a name="p7675774152418"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p25603865152418"><a name="p25603865152418"></a><a name="p25603865152418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8953941152418"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p54180595152418"><a name="p54180595152418"></a><a name="p54180595152418"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p26552041152418"><a name="p26552041152418"></a><a name="p26552041152418"></a>String</p>
<p id="p37641781152418"><a name="p37641781152418"></a><a name="p37641781152418"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p29085411152418"><a name="p29085411152418"></a><a name="p29085411152418"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
</tbody>
</table>

Request header parameters

<a name="table36367452152418"></a>
<table><thead align="left"><tr id="row3553961152418"><th class="cellrowborder" valign="top" width="28.74%" id="mcps1.1.4.1.1"><p id="p19435463152418"><a name="p19435463152418"></a><a name="p19435463152418"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.97%" id="mcps1.1.4.1.2"><p id="p8482680152418"><a name="p8482680152418"></a><a name="p8482680152418"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.290000000000006%" id="mcps1.1.4.1.3"><p id="p9858267152418"><a name="p9858267152418"></a><a name="p9858267152418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6028629152418"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p18556922152418"><a name="p18556922152418"></a><a name="p18556922152418"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.4.1.2 "><p id="p26715728152418"><a name="p26715728152418"></a><a name="p26715728152418"></a>String</p>
<p id="p39114965152418"><a name="p39114965152418"></a><a name="p39114965152418"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="53.290000000000006%" headers="mcps1.1.4.1.3 "><p id="p14195574152418"><a name="p14195574152418"></a><a name="p14195574152418"></a>Authentication token.</p>
</td>
</tr>
<tr id="row60651309152418"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p60891321152620"><a name="p60891321152620"></a><a name="p60891321152620"></a>X-Account-Meta-Temp-URL-Key</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.4.1.2 "><p id="p33249987152620"><a name="p33249987152620"></a><a name="p33249987152620"></a>String</p>
<p id="p48214753152625"><a name="p48214753152625"></a><a name="p48214753152625"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="53.290000000000006%" headers="mcps1.1.4.1.3 "><p id="p8894417152620"><a name="p8894417152620"></a><a name="p8894417152620"></a>Secret key value for TempURL.</p>
</td>
</tr>
<tr id="row28489674152543"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p41579437152620"><a name="p41579437152620"></a><a name="p41579437152620"></a>X-Account-Meta-Temp-URL-Key-2</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.4.1.2 "><p id="p12491254152620"><a name="p12491254152620"></a><a name="p12491254152620"></a>String</p>
<p id="p24077077152634"><a name="p24077077152634"></a><a name="p24077077152634"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="53.290000000000006%" headers="mcps1.1.4.1.3 "><p id="p5158623152620"><a name="p5158623152620"></a><a name="p5158623152620"></a>A second secret key value for TempURL.</p>
</td>
</tr>
<tr id="row63573785152554"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p2539795152620"><a name="p2539795152620"></a><a name="p2539795152620"></a>X-Account-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.4.1.2 "><p id="p4396868152620"><a name="p4396868152620"></a><a name="p4396868152620"></a>String</p>
<p id="p39948648152636"><a name="p39948648152636"></a><a name="p39948648152636"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="53.290000000000006%" headers="mcps1.1.4.1.3 "><p id="p20602066152620"><a name="p20602066152620"></a><a name="p20602066152620"></a>Account metadata. <strong id="b5636878"><a name="b5636878"></a><a name="b5636878"></a>{name}</strong> is the name of metadata item that you want to add, update, or delete. To delete this item, send an empty value in this header. You must specify an <strong id="b151859853693931"><a name="b151859853693931"></a><a name="b151859853693931"></a>X-Account-Meta-{name}</strong> header for each metadata item (for each <strong id="b162145756393931"><a name="b162145756393931"></a><a name="b162145756393931"></a>{name}</strong>) that you want to add, update, or delete.</p>
</td>
</tr>
<tr id="row48993042152554"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p53629899152620"><a name="p53629899152620"></a><a name="p53629899152620"></a>X-Remove-Account-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.4.1.2 "><p id="p49054526152620"><a name="p49054526152620"></a><a name="p49054526152620"></a>String</p>
<p id="p4576070152638"><a name="p4576070152638"></a><a name="p4576070152638"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="53.290000000000006%" headers="mcps1.1.4.1.3 "><p id="p13993707152620"><a name="p13993707152620"></a><a name="p13993707152620"></a>Deletes metadata. If a tool does not support empty headers, such as an earlier version of cURL, send this header to delete metadata. <strong id="b28240785"><a name="b28240785"></a><a name="b28240785"></a>{name}</strong> indicates the metadata to delete. Set <strong id="b34741661593953"><a name="b34741661593953"></a><a name="b34741661593953"></a>{name}</strong> to a non-empty value.</p>
</td>
</tr>
<tr id="row8411726201748"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p10261199201748"><a name="p10261199201748"></a><a name="p10261199201748"></a>X-Account-Meta-Quota-Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.4.1.2 "><p id="p22204726201816"><a name="p22204726201816"></a><a name="p22204726201816"></a>Int</p>
<p id="p65624812201816"><a name="p65624812201816"></a><a name="p65624812201816"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="53.290000000000006%" headers="mcps1.1.4.1.3 "><p id="p13536469201748"><a name="p13536469201748"></a><a name="p13536469201748"></a>Configures the tenant quota. The value ranges from 0 to 9223372036854775807. After setting the quota, the quota will be checked each time you upload or copy an object, or modify the metadata of an object or bucket. A quota fails to be checked with status code 413 returned.</p>
</td>
</tr>
<tr id="row8839337201751"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p44897679201751"><a name="p44897679201751"></a><a name="p44897679201751"></a>X-Remove-Account-Meta-Quota-Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.4.1.2 "><p id="p28351766201824"><a name="p28351766201824"></a><a name="p28351766201824"></a>String</p>
<p id="p53839309201824"><a name="p53839309201824"></a><a name="p53839309201824"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="53.290000000000006%" headers="mcps1.1.4.1.3 "><p id="p32873986201751"><a name="p32873986201751"></a><a name="p32873986201751"></a>Deletes the quota. This parameter can be set to any non-empty value. If you delete a quota without setting it first, status code 403 is returned.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section46595788165128"></a>

<a name="table38077202192918"></a>
<table><thead align="left"><tr id="row47910623192918"><th class="cellrowborder" valign="top" width="20.419999999999998%" id="mcps1.1.4.1.1"><p id="p55555255192918"><a name="p55555255192918"></a><a name="p55555255192918"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="19.55%" id="mcps1.1.4.1.2"><p id="p3681820192918"><a name="p3681820192918"></a><a name="p3681820192918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.029999999999994%" id="mcps1.1.4.1.3"><p id="p29791989192918"><a name="p29791989192918"></a><a name="p29791989192918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64340907192918"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.1.4.1.1 "><p id="p44230949192918"><a name="p44230949192918"></a><a name="p44230949192918"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.1.4.1.2 "><p id="p25937099192918"><a name="p25937099192918"></a><a name="p25937099192918"></a>String</p>
<p id="p32107307192918"><a name="p32107307192918"></a><a name="p32107307192918"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="60.029999999999994%" headers="mcps1.1.4.1.3 "><p id="p50555071192918"><a name="p50555071192918"></a><a name="p50555071192918"></a>If the operation succeeds, this value is 0.</p>
<p id="p52342462192918"><a name="p52342462192918"></a><a name="p52342462192918"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row64886044192918"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.1.4.1.1 "><p id="p21278236192918"><a name="p21278236192918"></a><a name="p21278236192918"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.1.4.1.2 "><p id="p45815573192918"><a name="p45815573192918"></a><a name="p45815573192918"></a>String</p>
<p id="p9686974192918"><a name="p9686974192918"></a><a name="p9686974192918"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="60.029999999999994%" headers="mcps1.1.4.1.3 "><p id="p46447390192918"><a name="p46447390192918"></a><a name="p46447390192918"></a>MIME type of the text in the response body.</p>
</td>
</tr>
<tr id="row15373327192918"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.1.4.1.1 "><p id="p37279969192918"><a name="p37279969192918"></a><a name="p37279969192918"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.1.4.1.2 "><p id="p66887499192918"><a name="p66887499192918"></a><a name="p66887499192918"></a>Datetime</p>
<p id="p65116585192918"><a name="p65116585192918"></a><a name="p65116585192918"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="60.029999999999994%" headers="mcps1.1.4.1.3 "><p id="p39952043192918"><a name="p39952043192918"></a><a name="p39952043192918"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row24024074192918"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.1.4.1.1 "><p id="p66901805192918"><a name="p66901805192918"></a><a name="p66901805192918"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.1.4.1.2 "><p id="p50337162192918"><a name="p50337162192918"></a><a name="p50337162192918"></a>Uuid</p>
<p id="p50381277192918"><a name="p50381277192918"></a><a name="p50381277192918"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="60.029999999999994%" headers="mcps1.1.4.1.3 "><p id="p54351617192918"><a name="p54351617192918"></a><a name="p54351617192918"></a>Unique transaction identifier.</p>
<p id="p19402508192918"><a name="p19402508192918"></a><a name="p19402508192918"></a></p>
</td>
</tr>
</tbody>
</table>

## Create Account Metadata<a name="section31331064"></a>

Create Book and Subject metadata:

```
curl -i -H "X-auth-token:b8b574e33b0a4f74a1961bed1b4784b8" "http://172.28.5.31:80/v1/AUTH_0ce042a9be6140769b12c1001d41bcf9" -X POST -H "X-Account-Meta-Book:MobyDick" -H "X-Account-Meta-Subject:Literature"
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx000001513971bc1a370c0-93967ab85f
Content-Length: 0
Content-Type: text/html;charset=UTF-8
Date: Tue, 24 Nov 2015 12:22:13 GMT
```

## Update Account Metadata<a name="section3117276019246"></a>

Update the Subject metadata:

```
curl -i -H "X-auth-token:b8b574e33b0a4f74a1961bed1b4784b8" "http://172.28.5.31:80/v1/AUTH_0ce042a9be6140769b12c1001d41bcf9" -X POST -H "X-Account-Meta-Subject:ChineseLiterature"
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx0000015139725538370c0-f6e0c56435
Content-Length: 0
Content-Type: text/html;charset=UTF-8
Date: Tue, 24 Nov 2015 12:22:53 GMT
```

## Delete Account Metadata<a name="section21941182181512"></a>

Delete the Subject metadata:

```
curl -i -H "X-auth-token:b8b574e33b0a4f74a1961bed1b4784b8" "http://172.28.5.31:80/v1/AUTH_0ce042a9be6140769b12c1001d41bcf9" -X POST -H "X-Remove-Account-Meta-Subject:d"
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx000001513972ce7c370c0-40b77d13e2
Content-Length: 0
Content-Type: text/html;charset=UTF-8
Date: Tue, 24 Nov 2015 12:23:24 GMT
```

