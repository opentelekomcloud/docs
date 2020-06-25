# Querying Tenant Quotas<a name="EN-US_TOPIC_0067298110"></a>

## Function<a name="en-us_topic_0057973199_section15804956"></a>

This API is used to query quotas, including specifications of ECSs, vCPUs, and memory.

This API provides the  **user\_id**  parameter for obtaining the quota configuration of a specified user.

## URI<a name="en-us_topic_0057973199_section8026877"></a>

GET /v2/\{project\_id\}/os-quota-sets/\{project\_id\}?user\_id=\{user\_id\}

GET /v2.1/\{project\_id\}/os-quota-sets/\{project\_id\}?user\_id=\{user\_id\}

[Table 1](#en-us_topic_0057973199_table12637461156)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973199_table12637461156"></a>
<table><thead align="left"><tr id="en-us_topic_0057973199_row15273164612514"><th class="cellrowborder" valign="top" width="16.55%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.24%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.21000000000001%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973199_row828511468510"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p6287184613518"><a name="en-us_topic_0057973199_p6287184613518"></a><a name="en-us_topic_0057973199_p6287184613518"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p22901046657"><a name="en-us_topic_0057973199_p22901046657"></a><a name="en-us_topic_0057973199_p22901046657"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.21000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p1129212464514"><a name="en-us_topic_0057973199_p1129212464514"></a><a name="en-us_topic_0057973199_p1129212464514"></a>Specifies the project ID. If the specified project does not exist, the default quota in the system is returned.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row132920461656"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p102952462511"><a name="en-us_topic_0057973199_p102952462511"></a><a name="en-us_topic_0057973199_p102952462511"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p1629820467514"><a name="en-us_topic_0057973199_p1629820467514"></a><a name="en-us_topic_0057973199_p1629820467514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="66.21000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p1529916466519"><a name="en-us_topic_0057973199_p1529916466519"></a><a name="en-us_topic_0057973199_p1529916466519"></a>Specifies the user ID. If the specified user does not exist, the default quota in the system is returned.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973199_section13122166"></a>

None

## Response<a name="en-us_topic_0057973199_section50990633"></a>

[Table 2](#en-us_topic_0057973199_en-us_topic_0057973197_table62068690)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973199_en-us_topic_0057973197_table62068690"></a>
<table><thead align="left"><tr id="en-us_topic_0057973199_en-us_topic_0057973197_row56098908"><th class="cellrowborder" valign="top" width="16.55%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973197_p47717737"><a name="en-us_topic_0057973197_p47717737"></a><a name="en-us_topic_0057973197_p47717737"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973197_p39931478"><a name="en-us_topic_0057973197_p39931478"></a><a name="en-us_topic_0057973197_p39931478"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.14999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973197_p64532721"><a name="en-us_topic_0057973197_p64532721"></a><a name="en-us_topic_0057973197_p64532721"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973199_en-us_topic_0057973197_row59767919"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_en-us_topic_0057973197_p9363310"><a name="en-us_topic_0057973199_en-us_topic_0057973197_p9363310"></a><a name="en-us_topic_0057973199_en-us_topic_0057973197_p9363310"></a>quota_set</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_en-us_topic_0057973197_p20230678"><a name="en-us_topic_0057973199_en-us_topic_0057973197_p20230678"></a><a name="en-us_topic_0057973199_en-us_topic_0057973197_p20230678"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="66.14999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_en-us_topic_0057973197_p59256190"><a name="en-us_topic_0057973199_en-us_topic_0057973197_p59256190"></a><a name="en-us_topic_0057973199_en-us_topic_0057973197_p59256190"></a>Specifies the <strong id="en-us_topic_0057973199_en-us_topic_0064390806_b842352706183813"><a name="en-us_topic_0057973199_en-us_topic_0064390806_b842352706183813"></a><a name="en-us_topic_0057973199_en-us_topic_0064390806_b842352706183813"></a>quota_set</strong> object.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **quota\_set**  parameter description

<a name="en-us_topic_0057973199_table30231561"></a>
<table><thead align="left"><tr id="en-us_topic_0057973199_row25113310"><th class="cellrowborder" valign="top" width="18.548145185481452%" id="mcps1.2.4.1.1"><p id="p9963183415323"><a name="p9963183415323"></a><a name="p9963183415323"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.258474152584741%" id="mcps1.2.4.1.2"><p id="p0963133410326"><a name="p0963133410326"></a><a name="p0963133410326"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.19338066193382%" id="mcps1.2.4.1.3"><p id="p996317342321"><a name="p996317342321"></a><a name="p996317342321"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973199_row30393275"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p45936220"><a name="en-us_topic_0057973199_p45936220"></a><a name="en-us_topic_0057973199_p45936220"></a>cores</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p29846341"><a name="en-us_topic_0057973199_p29846341"></a><a name="en-us_topic_0057973199_p29846341"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p47666411392"><a name="en-us_topic_0057973199_p47666411392"></a><a name="en-us_topic_0057973199_p47666411392"></a>Specifies the quantity quota of vCPUs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row50766756"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p18466542"><a name="en-us_topic_0057973199_p18466542"></a><a name="en-us_topic_0057973199_p18466542"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p1691612101512"><a name="en-us_topic_0057973199_p1691612101512"></a><a name="en-us_topic_0057973199_p1691612101512"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p7766144103912"><a name="en-us_topic_0057973199_p7766144103912"></a><a name="en-us_topic_0057973199_p7766144103912"></a>Specifies the quantity quota of fixed IP addresses. This parameter is not supported.</p>
<p id="p864017413393"><a name="p864017413393"></a><a name="p864017413393"></a>This field is not supported in microversions later than 2.36.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row37686197"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p32683139"><a name="en-us_topic_0057973199_p32683139"></a><a name="en-us_topic_0057973199_p32683139"></a>floating_ips</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p158282315153"><a name="en-us_topic_0057973199_p158282315153"></a><a name="en-us_topic_0057973199_p158282315153"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p16766740399"><a name="en-us_topic_0057973199_p16766740399"></a><a name="en-us_topic_0057973199_p16766740399"></a>Specifies the quantity quota of floating IP addresses. This parameter is not supported.</p>
<p id="p2171103013411"><a name="p2171103013411"></a><a name="p2171103013411"></a>This field is not supported in microversions later than 2.36.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row60322465"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p54281500"><a name="en-us_topic_0057973199_p54281500"></a><a name="en-us_topic_0057973199_p54281500"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p34725355"><a name="en-us_topic_0057973199_p34725355"></a><a name="en-us_topic_0057973199_p34725355"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p107671041392"><a name="en-us_topic_0057973199_p107671041392"></a><a name="en-us_topic_0057973199_p107671041392"></a>Specifies the project UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row53277152"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p20482050"><a name="en-us_topic_0057973199_p20482050"></a><a name="en-us_topic_0057973199_p20482050"></a>injected_file_content_bytes</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p193011246151"><a name="en-us_topic_0057973199_p193011246151"></a><a name="en-us_topic_0057973199_p193011246151"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p19767154163911"><a name="en-us_topic_0057973199_p19767154163911"></a><a name="en-us_topic_0057973199_p19767154163911"></a>Specifies the size quota (bytes) of the files to be injected.</p>
<p id="p171873367419"><a name="p171873367419"></a><a name="p171873367419"></a>This field is not supported in microversions later than 2.56.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row28988915"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p66400774"><a name="en-us_topic_0057973199_p66400774"></a><a name="en-us_topic_0057973199_p66400774"></a>injected_file_path_bytes</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p72501227151510"><a name="en-us_topic_0057973199_p72501227151510"></a><a name="en-us_topic_0057973199_p72501227151510"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p1176715413396"><a name="en-us_topic_0057973199_p1176715413396"></a><a name="en-us_topic_0057973199_p1176715413396"></a>Specifies the size quota (bytes) of the path for the files to be injected.</p>
<p id="p69816710121"><a name="p69816710121"></a><a name="p69816710121"></a>This field is not supported in microversions later than 2.56.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row13369507"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p9188289"><a name="en-us_topic_0057973199_p9188289"></a><a name="en-us_topic_0057973199_p9188289"></a>injected_files</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p1460345412151"><a name="en-us_topic_0057973199_p1460345412151"></a><a name="en-us_topic_0057973199_p1460345412151"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p9767246391"><a name="en-us_topic_0057973199_p9767246391"></a><a name="en-us_topic_0057973199_p9767246391"></a>Specifies the quantity quota of the files to be injected.</p>
<p id="p167581619128"><a name="p167581619128"></a><a name="p167581619128"></a>This field is not supported in microversions later than 2.56.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row59944257"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p23646677"><a name="en-us_topic_0057973199_p23646677"></a><a name="en-us_topic_0057973199_p23646677"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p97481655101511"><a name="en-us_topic_0057973199_p97481655101511"></a><a name="en-us_topic_0057973199_p97481655101511"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p1876714183917"><a name="en-us_topic_0057973199_p1876714183917"></a><a name="en-us_topic_0057973199_p1876714183917"></a>Specifies the quantity quota of ECSs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row5482215"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p41406250"><a name="en-us_topic_0057973199_p41406250"></a><a name="en-us_topic_0057973199_p41406250"></a>key_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p152511579158"><a name="en-us_topic_0057973199_p152511579158"></a><a name="en-us_topic_0057973199_p152511579158"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p1876716493911"><a name="en-us_topic_0057973199_p1876716493911"></a><a name="en-us_topic_0057973199_p1876716493911"></a>Specifies the quantity quota of key pairs. This parameter is not supported.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row43614388"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p43104560"><a name="en-us_topic_0057973199_p43104560"></a><a name="en-us_topic_0057973199_p43104560"></a>metadata_items</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p5274115911512"><a name="en-us_topic_0057973199_p5274115911512"></a><a name="en-us_topic_0057973199_p5274115911512"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p187671742393"><a name="en-us_topic_0057973199_p187671742393"></a><a name="en-us_topic_0057973199_p187671742393"></a>Specifies the metadata quantity quota.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row20242451"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p29025826"><a name="en-us_topic_0057973199_p29025826"></a><a name="en-us_topic_0057973199_p29025826"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p23505391618"><a name="en-us_topic_0057973199_p23505391618"></a><a name="en-us_topic_0057973199_p23505391618"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p17670483911"><a name="en-us_topic_0057973199_p17670483911"></a><a name="en-us_topic_0057973199_p17670483911"></a>Specifies the memory quota (MB).</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row46426356"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p2438464"><a name="en-us_topic_0057973199_p2438464"></a><a name="en-us_topic_0057973199_p2438464"></a>security_group_rules</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p19881144163"><a name="en-us_topic_0057973199_p19881144163"></a><a name="en-us_topic_0057973199_p19881144163"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p97671453913"><a name="en-us_topic_0057973199_p97671453913"></a><a name="en-us_topic_0057973199_p97671453913"></a>Specifies the quota of security group rules. This parameter is not supported.</p>
<p id="p19247528171210"><a name="p19247528171210"></a><a name="p19247528171210"></a>This field is not supported in microversions later than 2.36.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row50813968"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p22290707"><a name="en-us_topic_0057973199_p22290707"></a><a name="en-us_topic_0057973199_p22290707"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p181921769166"><a name="en-us_topic_0057973199_p181921769166"></a><a name="en-us_topic_0057973199_p181921769166"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p10769114153919"><a name="en-us_topic_0057973199_p10769114153919"></a><a name="en-us_topic_0057973199_p10769114153919"></a>Specifies the quantity quota of security groups. This parameter is not supported.</p>
<p id="p14918173751212"><a name="p14918173751212"></a><a name="p14918173751212"></a>This field is not supported in microversions later than 2.36.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row47118120"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p58471341"><a name="en-us_topic_0057973199_p58471341"></a><a name="en-us_topic_0057973199_p58471341"></a>server_groups</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p819119817166"><a name="en-us_topic_0057973199_p819119817166"></a><a name="en-us_topic_0057973199_p819119817166"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p7769944391"><a name="en-us_topic_0057973199_p7769944391"></a><a name="en-us_topic_0057973199_p7769944391"></a>Specifies the quantity quota of ECS groups.</p>
</td>
</tr>
<tr id="en-us_topic_0057973199_row18294597"><td class="cellrowborder" valign="top" width="18.548145185481452%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973199_p5467365"><a name="en-us_topic_0057973199_p5467365"></a><a name="en-us_topic_0057973199_p5467365"></a>server_group_members</p>
</td>
<td class="cellrowborder" valign="top" width="15.258474152584741%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973199_p172754921610"><a name="en-us_topic_0057973199_p172754921610"></a><a name="en-us_topic_0057973199_p172754921610"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.19338066193382%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973199_p5769134203914"><a name="en-us_topic_0057973199_p5769134203914"></a><a name="en-us_topic_0057973199_p5769134203914"></a>Specifies the size quota of ECS groups.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973199_section56262520"></a>

```
GET https://{endpoint}/v2/d9ebe43510414ef590a4aa158605329e/os-quota-sets/d9ebe43510414ef590a4aa158605329e
GET https://{endpoint}/v2.1/d9ebe43510414ef590a4aa158605329e/os-quota-sets/d9ebe43510414ef590a4aa158605329e
```

## Example Response<a name="section1965011613499"></a>

```
{
    "quota_set": {
        "cores": 20,
        "fixed_ips": 40,
        "floating_ips": 10,
        "id": "d9ebe43510414ef590a4aa158605329e",
        "injected_file_content_bytes": 10240,
        "injected_file_path_bytes": 255,
        "injected_files": 5,
        "instances": 20,
        "key_pairs": 100,
        "metadata_items": 128,
        "ram": 51200,
        "security_group_rules": 20,
        "security_groups": 50,
        "server_group_members": 10,
        "server_groups": 10
    }
}
```

## Returned Values<a name="en-us_topic_0057973199_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

