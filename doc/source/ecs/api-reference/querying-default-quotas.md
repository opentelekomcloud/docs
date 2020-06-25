# Querying Default Quotas<a name="EN-US_TOPIC_0065817716"></a>

## Function<a name="en-us_topic_0057973201_section4302370"></a>

This API is used to query default quotas.

## URI<a name="en-us_topic_0057973201_section38721337"></a>

GET /v2/\{project\_id\}/os-quota-sets/\{project\_id\}/defaults

GET /v2.1/\{project\_id\}/os-quota-sets/\{project\_id\}/defaults

[Table 1](#en-us_topic_0057973201_table258804192629)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973201_table258804192629"></a>
<table><thead align="left"><tr id="en-us_topic_0057973201_row33277594192629"><th class="cellrowborder" valign="top" width="16.74%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.740000000000002%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.52%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973201_row56232837192629"><td class="cellrowborder" valign="top" width="16.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p58565959192629"><a name="en-us_topic_0057973201_p58565959192629"></a><a name="en-us_topic_0057973201_p58565959192629"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.740000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p46222262192629"><a name="en-us_topic_0057973201_p46222262192629"></a><a name="en-us_topic_0057973201_p46222262192629"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.52%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973201_section42132238"></a>

None

## Response<a name="en-us_topic_0057973201_section43645827"></a>

[Table 2](#en-us_topic_0057973201_en-us_topic_0057973197_table62068690)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973201_en-us_topic_0057973197_table62068690"></a>
<table><thead align="left"><tr id="en-us_topic_0057973201_en-us_topic_0057973197_row56098908"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973197_p47717737"><a name="en-us_topic_0057973197_p47717737"></a><a name="en-us_topic_0057973197_p47717737"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973197_p39931478"><a name="en-us_topic_0057973197_p39931478"></a><a name="en-us_topic_0057973197_p39931478"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.60000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973197_p64532721"><a name="en-us_topic_0057973197_p64532721"></a><a name="en-us_topic_0057973197_p64532721"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973201_en-us_topic_0057973197_row59767919"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_en-us_topic_0057973197_p9363310"><a name="en-us_topic_0057973201_en-us_topic_0057973197_p9363310"></a><a name="en-us_topic_0057973201_en-us_topic_0057973197_p9363310"></a>quota_set</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_en-us_topic_0057973197_p20230678"><a name="en-us_topic_0057973201_en-us_topic_0057973197_p20230678"></a><a name="en-us_topic_0057973201_en-us_topic_0057973197_p20230678"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973201_en-us_topic_0057973197_p59256190"><a name="en-us_topic_0057973201_en-us_topic_0057973197_p59256190"></a><a name="en-us_topic_0057973201_en-us_topic_0057973197_p59256190"></a>Specifies the <strong id="en-us_topic_0057973201_en-us_topic_0064390806_b842352706183813"><a name="en-us_topic_0057973201_en-us_topic_0064390806_b842352706183813"></a><a name="en-us_topic_0057973201_en-us_topic_0064390806_b842352706183813"></a>quota_set</strong> object.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **quota\_set**  parameter description

<a name="en-us_topic_0057973201_table29589013"></a>
<table><thead align="left"><tr id="en-us_topic_0057973201_row16562342"><th class="cellrowborder" valign="top" width="18.17%" id="mcps1.2.4.1.1"><p id="p6588045163210"><a name="p6588045163210"></a><a name="p6588045163210"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.2%" id="mcps1.2.4.1.2"><p id="p15588245163210"><a name="p15588245163210"></a><a name="p15588245163210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.63%" id="mcps1.2.4.1.3"><p id="p5588145183211"><a name="p5588145183211"></a><a name="p5588145183211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973201_row28465510"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p24004958"><a name="en-us_topic_0057973201_p24004958"></a><a name="en-us_topic_0057973201_p24004958"></a>cores</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p72501227151510"><a name="en-us_topic_0057973201_p72501227151510"></a><a name="en-us_topic_0057973201_p72501227151510"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p47666411392"><a name="en-us_topic_0057973199_p47666411392"></a><a name="en-us_topic_0057973199_p47666411392"></a>Specifies the quantity quota of vCPUs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row26136320"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p36667161"><a name="en-us_topic_0057973201_p36667161"></a><a name="en-us_topic_0057973201_p36667161"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p186841317111619"><a name="en-us_topic_0057973201_p186841317111619"></a><a name="en-us_topic_0057973201_p186841317111619"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p7766144103912"><a name="en-us_topic_0057973199_p7766144103912"></a><a name="en-us_topic_0057973199_p7766144103912"></a>Specifies the quantity quota of fixed IP addresses. This parameter is not supported.</p>
<p id="p864017413393"><a name="p864017413393"></a><a name="p864017413393"></a>This field is not supported in microversions later than 2.36.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row20639791"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p61210371"><a name="en-us_topic_0057973201_p61210371"></a><a name="en-us_topic_0057973201_p61210371"></a>floating_ips</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p3913118111613"><a name="en-us_topic_0057973201_p3913118111613"></a><a name="en-us_topic_0057973201_p3913118111613"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p16766740399"><a name="en-us_topic_0057973199_p16766740399"></a><a name="en-us_topic_0057973199_p16766740399"></a>Specifies the quantity quota of floating IP addresses. This parameter is not supported.</p>
<p id="p7399125517139"><a name="p7399125517139"></a><a name="p7399125517139"></a>This field is not supported in microversions later than 2.36.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row60052996"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p32454526"><a name="en-us_topic_0057973201_p32454526"></a><a name="en-us_topic_0057973201_p32454526"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p11570940"><a name="en-us_topic_0057973201_p11570940"></a><a name="en-us_topic_0057973201_p11570940"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p107671041392"><a name="en-us_topic_0057973199_p107671041392"></a><a name="en-us_topic_0057973199_p107671041392"></a>Specifies the project UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row17123161"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p44798770"><a name="en-us_topic_0057973201_p44798770"></a><a name="en-us_topic_0057973201_p44798770"></a>injected_file_content_bytes</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p158711821181614"><a name="en-us_topic_0057973201_p158711821181614"></a><a name="en-us_topic_0057973201_p158711821181614"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p19767154163911"><a name="en-us_topic_0057973199_p19767154163911"></a><a name="en-us_topic_0057973199_p19767154163911"></a>Specifies the size quota (bytes) of the files to be injected.</p>
<p id="p145744641219"><a name="p145744641219"></a><a name="p145744641219"></a>This field is not supported in microversions later than 2.57.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row41672973"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p20067663"><a name="en-us_topic_0057973201_p20067663"></a><a name="en-us_topic_0057973201_p20067663"></a>injected_file_path_bytes</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p619932461614"><a name="en-us_topic_0057973201_p619932461614"></a><a name="en-us_topic_0057973201_p619932461614"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p1176715413396"><a name="en-us_topic_0057973199_p1176715413396"></a><a name="en-us_topic_0057973199_p1176715413396"></a>Specifies the size quota (bytes) of the path for the files to be injected.</p>
<p id="p85781638204113"><a name="p85781638204113"></a><a name="p85781638204113"></a>This field is not supported in microversions later than 2.57.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row24170571"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p11659216"><a name="en-us_topic_0057973201_p11659216"></a><a name="en-us_topic_0057973201_p11659216"></a>injected_files</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p967412256162"><a name="en-us_topic_0057973201_p967412256162"></a><a name="en-us_topic_0057973201_p967412256162"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p9767246391"><a name="en-us_topic_0057973199_p9767246391"></a><a name="en-us_topic_0057973199_p9767246391"></a>Specifies the quantity quota of the files to be injected.</p>
<p id="p810984210419"><a name="p810984210419"></a><a name="p810984210419"></a>This field is not supported in microversions later than 2.57.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row17870531"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p38226869"><a name="en-us_topic_0057973201_p38226869"></a><a name="en-us_topic_0057973201_p38226869"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p1375472610167"><a name="en-us_topic_0057973201_p1375472610167"></a><a name="en-us_topic_0057973201_p1375472610167"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p1876714183917"><a name="en-us_topic_0057973199_p1876714183917"></a><a name="en-us_topic_0057973199_p1876714183917"></a>Specifies the quantity quota of ECSs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row34050285"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p6609735"><a name="en-us_topic_0057973201_p6609735"></a><a name="en-us_topic_0057973201_p6609735"></a>key_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p18933527131610"><a name="en-us_topic_0057973201_p18933527131610"></a><a name="en-us_topic_0057973201_p18933527131610"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p1876716493911"><a name="en-us_topic_0057973199_p1876716493911"></a><a name="en-us_topic_0057973199_p1876716493911"></a>Specifies the quota of key pairs. This parameter is not supported.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row48158284"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p8506968"><a name="en-us_topic_0057973201_p8506968"></a><a name="en-us_topic_0057973201_p8506968"></a>metadata_items</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p616716297166"><a name="en-us_topic_0057973201_p616716297166"></a><a name="en-us_topic_0057973201_p616716297166"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p187671742393"><a name="en-us_topic_0057973199_p187671742393"></a><a name="en-us_topic_0057973199_p187671742393"></a>Specifies the metadata quantity quota.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row57789353"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p50425983"><a name="en-us_topic_0057973201_p50425983"></a><a name="en-us_topic_0057973201_p50425983"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p45674313166"><a name="en-us_topic_0057973201_p45674313166"></a><a name="en-us_topic_0057973201_p45674313166"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p17670483911"><a name="en-us_topic_0057973199_p17670483911"></a><a name="en-us_topic_0057973199_p17670483911"></a>Specifies the memory quota (MB).</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row14036819"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p63240543"><a name="en-us_topic_0057973201_p63240543"></a><a name="en-us_topic_0057973201_p63240543"></a>security_group_rules</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p996283313164"><a name="en-us_topic_0057973201_p996283313164"></a><a name="en-us_topic_0057973201_p996283313164"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p97671453913"><a name="en-us_topic_0057973199_p97671453913"></a><a name="en-us_topic_0057973199_p97671453913"></a>Specifies the quota of security group rules. This parameter is not supported.</p>
<p id="p17933151191416"><a name="p17933151191416"></a><a name="p17933151191416"></a>This field is not supported in microversions later than 2.36.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row55715684"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p16676575"><a name="en-us_topic_0057973201_p16676575"></a><a name="en-us_topic_0057973201_p16676575"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p897113510165"><a name="en-us_topic_0057973201_p897113510165"></a><a name="en-us_topic_0057973201_p897113510165"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p10769114153919"><a name="en-us_topic_0057973199_p10769114153919"></a><a name="en-us_topic_0057973199_p10769114153919"></a>Specifies the quota of security groups. This parameter is not supported.</p>
<p id="p114411611140"><a name="p114411611140"></a><a name="p114411611140"></a>This field is not supported in microversions later than 2.36.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row28948990"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p63166834"><a name="en-us_topic_0057973201_p63166834"></a><a name="en-us_topic_0057973201_p63166834"></a>server_groups</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p8691183631616"><a name="en-us_topic_0057973201_p8691183631616"></a><a name="en-us_topic_0057973201_p8691183631616"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p7769944391"><a name="en-us_topic_0057973199_p7769944391"></a><a name="en-us_topic_0057973199_p7769944391"></a>Specifies the quantity quota of ECS groups.</p>
</td>
</tr>
<tr id="en-us_topic_0057973201_row32659336"><td class="cellrowborder" valign="top" width="18.17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973201_p28160592"><a name="en-us_topic_0057973201_p28160592"></a><a name="en-us_topic_0057973201_p28160592"></a>server_group_members</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973201_p1186383713163"><a name="en-us_topic_0057973201_p1186383713163"></a><a name="en-us_topic_0057973201_p1186383713163"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p5769134203914"><a name="en-us_topic_0057973199_p5769134203914"></a><a name="en-us_topic_0057973199_p5769134203914"></a>Specifies the size quota of ECS groups.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973201_section57268131"></a>

```
GET https://{endpoint}/v2/d9ebe43510414ef590a4aa158605329e/os-quota-sets/d9ebe43510414ef590a4aa158605329e/defaults
GET https://{endpoint}/v2.1/d9ebe43510414ef590a4aa158605329e/os-quota-sets/d9ebe43510414ef590a4aa158605329e/defaults
```

## Example Response<a name="section18547143234913"></a>

```
{
    "quota_set": {
	"injected_file_content_bytes": 10240,
        "metadata_items": 128,
        "server_group_members": 10,
        "server_groups": 10,
        "ram": 51200,
        "floating_ips": 10,
        "key_pairs": 100,
        "injected_file_path_bytes": 255,
        "instances": 10,
        "security_group_rules": 20,
        "injected_files": 5,
        "cores": 20,
        "fixed_ips": -1,
        "id": "474eff20eee84b2e87b5717cc7f34dd8",
        "security_groups": 10
    }
}
```

## Returned Values<a name="en-us_topic_0057973201_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

