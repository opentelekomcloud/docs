# Conditions<a name="obs_03_0120"></a>

In addition to the effect, principal, resources, and actions, you can also specify the conditions under which the bucket policy takes effect. A bucket policy takes effect only when its condition expressions match values contained in the request.  **Conditions**  is an optional parameter. You can determine whether to use this parameter based on service requirements. For example, if account  **A**  needs to be granted with full control permissions for an object uploaded by account  **B**  in bucket  **example**, you can specify that the upload request must contain the  **acl**  key and set the policy effect to  **Allow**  for account  **A**. The complete condition expression is as follows:

<a name="table4665122635716"></a>
<table><thead align="left"><tr id="row18929192605713"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.1"><p id="p1692982625718"><a name="p1692982625718"></a><a name="p1692982625718"></a>Condition Operator</p>
</th>
<th class="cellrowborder" valign="top" width="35.709999999999994%" id="mcps1.1.4.1.2"><p id="p1192982612571"><a name="p1192982612571"></a><a name="p1192982612571"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="37.76%" id="mcps1.1.4.1.3"><p id="p792920265579"><a name="p792920265579"></a><a name="p792920265579"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row1793012695713"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.1 "><p id="p09301626135716"><a name="p09301626135716"></a><a name="p09301626135716"></a>StringEquals</p>
</td>
<td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.1.4.1.2 "><p id="p12930192616574"><a name="p12930192616574"></a><a name="p12930192616574"></a>acl</p>
</td>
<td class="cellrowborder" valign="top" width="37.76%" headers="mcps1.1.4.1.3 "><p id="p693019269573"><a name="p693019269573"></a><a name="p693019269573"></a>bucket-owner-full-control</p>
</td>
</tr>
</tbody>
</table>

A condition consists of three parts: condition operator, key, and value. Condition operators and keys are associated with each other. For example:

-   If a string type condition operator is selected, such as  **StringEquals**, the key can only be of the string type, such as  **UserAgent**.
-   If a date type key is selected, such as  **CurrentTime**, the condition operator can only be of the date type, such as  **DateEquals**.

[Table 1](#table16670126115713)  describes the predefined condition operators provided by OBS.

**Table  1**  Condition operators

<a name="table16670126115713"></a>
<table><thead align="left"><tr id="row15930026105710"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.1"><p id="p18930526125711"><a name="p18930526125711"></a><a name="p18930526125711"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="34.69%" id="mcps1.2.4.1.2"><p id="p2930326195720"><a name="p2930326195720"></a><a name="p2930326195720"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="47.96%" id="mcps1.2.4.1.3"><p id="p11930826135715"><a name="p11930826135715"></a><a name="p11930826135715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4930826175711"><td class="cellrowborder" rowspan="6" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p993072619572"><a name="p993072619572"></a><a name="p993072619572"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.4.1.2 "><p id="p1393042619575"><a name="p1393042619575"></a><a name="p1393042619575"></a>StringEquals</p>
</td>
<td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.2.4.1.3 "><p id="p109301126185714"><a name="p109301126185714"></a><a name="p109301126185714"></a>Strict matching. Short version: streq</p>
</td>
</tr>
<tr id="row129306265578"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p13930112613578"><a name="p13930112613578"></a><a name="p13930112613578"></a>StringNotEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6930926185718"><a name="p6930926185718"></a><a name="p6930926185718"></a>Strict negated matching. Short version: strneq</p>
</td>
</tr>
<tr id="row15930172675712"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1293032614572"><a name="p1293032614572"></a><a name="p1293032614572"></a>StringEqualsIgnoreCase</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p20930526205719"><a name="p20930526205719"></a><a name="p20930526205719"></a>Strict matching, ignoring case. Short version: streqi</p>
</td>
</tr>
<tr id="row1393082612571"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p9930726115720"><a name="p9930726115720"></a><a name="p9930726115720"></a>StringNotEqualsIgnoreCase</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p49314263574"><a name="p49314263574"></a><a name="p49314263574"></a>Strict negated matching, ignoring case. Short version: strneqi</p>
</td>
</tr>
<tr id="row19931626165720"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p0931122625713"><a name="p0931122625713"></a><a name="p0931122625713"></a>StringLike</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1693112615575"><a name="p1693112615575"></a><a name="p1693112615575"></a>Loose case-insensitive matching. The values can include a multi-character match wildcard (*) or a single-character match wildcard (?) anywhere in the string. Short version: strl</p>
</td>
</tr>
<tr id="row1993192617571"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p8931526155711"><a name="p8931526155711"></a><a name="p8931526155711"></a>StringNotLike</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1393116268577"><a name="p1393116268577"></a><a name="p1393116268577"></a>Negated loose case-insensitive matching. The values can include a multi-character match wildcard (*) or a single-character match wildcard (?) anywhere in the string. Short version: strnl</p>
</td>
</tr>
<tr id="row1093132635715"><td class="cellrowborder" rowspan="6" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p18931626155713"><a name="p18931626155713"></a><a name="p18931626155713"></a>Numeric</p>
</td>
<td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.4.1.2 "><p id="p199311126105710"><a name="p199311126105710"></a><a name="p199311126105710"></a>NumericEquals</p>
</td>
<td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.2.4.1.3 "><p id="p139316261570"><a name="p139316261570"></a><a name="p139316261570"></a>Strict matching. Short version: numeq</p>
</td>
</tr>
<tr id="row9931192612579"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p8931826185719"><a name="p8931826185719"></a><a name="p8931826185719"></a>NumericNotEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p69311426125717"><a name="p69311426125717"></a><a name="p69311426125717"></a>Strict negated matching. Short version: numneq</p>
</td>
</tr>
<tr id="row1893119263574"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p169314269573"><a name="p169314269573"></a><a name="p169314269573"></a>NumericLessThan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p793152615579"><a name="p793152615579"></a><a name="p793152615579"></a>"Less than" matching. Short version: numlt</p>
</td>
</tr>
<tr id="row8931626175713"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1293162612577"><a name="p1293162612577"></a><a name="p1293162612577"></a>NumericLessThanEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p13931026105713"><a name="p13931026105713"></a><a name="p13931026105713"></a>"Less than or equals" matching. Short version: numlteq</p>
</td>
</tr>
<tr id="row1593117265574"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p129311265575"><a name="p129311265575"></a><a name="p129311265575"></a>NumericGreaterThan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p11931192605715"><a name="p11931192605715"></a><a name="p11931192605715"></a>"Greater than" matching. Short version: numgt</p>
</td>
</tr>
<tr id="row11931102611577"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1693262617575"><a name="p1693262617575"></a><a name="p1693262617575"></a>NumericGreaterThanEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2932526165713"><a name="p2932526165713"></a><a name="p2932526165713"></a>"Greater than or equals" matching. Short version: numgteq</p>
</td>
</tr>
<tr id="row1993272655712"><td class="cellrowborder" rowspan="6" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p39327261574"><a name="p39327261574"></a><a name="p39327261574"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.4.1.2 "><p id="p14932826105710"><a name="p14932826105710"></a><a name="p14932826105710"></a>DateEquals</p>
</td>
<td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.2.4.1.3 "><p id="p493220267579"><a name="p493220267579"></a><a name="p493220267579"></a>Strict matching. Short version: dateeq</p>
</td>
</tr>
<tr id="row17932132675710"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1693252695711"><a name="p1693252695711"></a><a name="p1693252695711"></a>DateNotEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p119321826185717"><a name="p119321826185717"></a><a name="p119321826185717"></a>Strict negated matching. Short version: dateneq</p>
</td>
</tr>
<tr id="row5932926145714"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1593215265571"><a name="p1593215265571"></a><a name="p1593215265571"></a>DateLessThan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p29322026115711"><a name="p29322026115711"></a><a name="p29322026115711"></a>Indicates that the date is earlier than a specific date. Short version: datelt</p>
</td>
</tr>
<tr id="row13932926155717"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p209328269579"><a name="p209328269579"></a><a name="p209328269579"></a>DateLessThanEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p19321267573"><a name="p19321267573"></a><a name="p19321267573"></a>Indicates that the date is earlier than or equal to a specific date. Short version: datelteq</p>
</td>
</tr>
<tr id="row293292635719"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p17934102685717"><a name="p17934102685717"></a><a name="p17934102685717"></a>DateGreaterThan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p20934126185717"><a name="p20934126185717"></a><a name="p20934126185717"></a>Indicates that the date is later than a specific date. Short version: dategt</p>
</td>
</tr>
<tr id="row59341726195716"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p19341826105716"><a name="p19341826105716"></a><a name="p19341826105716"></a>DateGreaterThanEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1293572625720"><a name="p1293572625720"></a><a name="p1293572625720"></a>Indicates that the date is later than or equal to a specific date. Short version: dategteq</p>
</td>
</tr>
<tr id="row2935026205719"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p1293582695717"><a name="p1293582695717"></a><a name="p1293582695717"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.4.1.2 "><p id="p793572615710"><a name="p793572615710"></a><a name="p793572615710"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.2.4.1.3 "><p id="p1793542616575"><a name="p1793542616575"></a><a name="p1793542616575"></a>Strict Boolean matching</p>
</td>
</tr>
<tr id="row14935112613574"><td class="cellrowborder" rowspan="2" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p1893512695720"><a name="p1893512695720"></a><a name="p1893512695720"></a>IP address</p>
</td>
<td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.4.1.2 "><p id="p39351726205718"><a name="p39351726205718"></a><a name="p39351726205718"></a>IpAddress</p>
</td>
<td class="cellrowborder" valign="top" width="47.96%" headers="mcps1.2.4.1.3 "><p id="p13935426185714"><a name="p13935426185714"></a><a name="p13935426185714"></a>Takes effect only on specified IP address or IP address range. Example: <strong id="b173971220179"><a name="b173971220179"></a><a name="b173971220179"></a>x.x.x.x/24</strong></p>
</td>
</tr>
<tr id="row1193542665711"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p9935142635716"><a name="p9935142635716"></a><a name="p9935142635716"></a>NotIpAddress</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p15935826105715"><a name="p15935826105715"></a><a name="p15935826105715"></a>Take effect only on all except specified IP address or IP address range. Example: <strong id="b117663565187"><a name="b117663565187"></a><a name="b117663565187"></a>x.x.x.x/24</strong></p>
</td>
</tr>
</tbody>
</table>

A condition can contain any of the three types of keys: general keys, keys related to bucket actions, and keys related to object actions.

**Table  2**  General keys

<a name="table6707152645718"></a>
<table><thead align="left"><tr id="row1935926135711"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p1793592611576"><a name="p1793592611576"></a><a name="p1793592611576"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.2"><p id="p793514267571"><a name="p793514267571"></a><a name="p793514267571"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="p3935122615719"><a name="p3935122615719"></a><a name="p3935122615719"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3935172613579"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p89351926115716"><a name="p89351926115716"></a><a name="p89351926115716"></a>CurrentTime</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p8935226155711"><a name="p8935226155711"></a><a name="p8935226155711"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p129353268579"><a name="p129353268579"></a><a name="p129353268579"></a>Indicates the date when the request is received by the server. The date format must comply with ISO 8601.</p>
</td>
</tr>
<tr id="row99361826135711"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p893662675713"><a name="p893662675713"></a><a name="p893662675713"></a>EpochTime</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p17936626155716"><a name="p17936626155716"></a><a name="p17936626155716"></a>Numeric</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p893610266576"><a name="p893610266576"></a><a name="p893610266576"></a>Indicates the time when the request is received by the server, which is expressed as seconds since 1970.01.01 00:00:00 UTC, regardless of the leap seconds.</p>
</td>
</tr>
<tr id="row159361226145714"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p893692618570"><a name="p893692618570"></a><a name="p893692618570"></a>SecureTransport</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p4936182635719"><a name="p4936182635719"></a><a name="p4936182635719"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p1936172613574"><a name="p1936172613574"></a><a name="p1936172613574"></a>Requests whether to use SSL.</p>
</td>
</tr>
<tr id="row1936326155719"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1693616267579"><a name="p1693616267579"></a><a name="p1693616267579"></a>SourceIp</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p1993652625717"><a name="p1993652625717"></a><a name="p1993652625717"></a>IP address</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p1693692615716"><a name="p1693692615716"></a><a name="p1693692615716"></a>Source IP address from which the request is sent</p>
</td>
</tr>
<tr id="row1193652695714"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p129361426125712"><a name="p129361426125712"></a><a name="p129361426125712"></a>UserAgent</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p393662612574"><a name="p393662612574"></a><a name="p393662612574"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p159364265574"><a name="p159364265574"></a><a name="p159364265574"></a>Requested client software agent</p>
</td>
</tr>
<tr id="row293620261576"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p493602675716"><a name="p493602675716"></a><a name="p493602675716"></a>Referer</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p14936172685719"><a name="p14936172685719"></a><a name="p14936172685719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p893617261578"><a name="p893617261578"></a><a name="p893617261578"></a>Indicates the link from which the request is sent.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Keys related to bucket actions

<a name="table1972610267573"></a>
<table><thead align="left"><tr id="row6936152645711"><th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.4.1.1"><p id="p8937726175712"><a name="p8937726175712"></a><a name="p8937726175712"></a>Action</p>
</th>
<th class="cellrowborder" valign="top" width="27.55%" id="mcps1.2.4.1.2"><p id="p9937182635715"><a name="p9937182635715"></a><a name="p9937182635715"></a>Optional Key</p>
</th>
<th class="cellrowborder" valign="top" width="48.980000000000004%" id="mcps1.2.4.1.3"><p id="p10937826175712"><a name="p10937826175712"></a><a name="p10937826175712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row593712616576"><td class="cellrowborder" rowspan="3" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p59379267576"><a name="p59379267576"></a><a name="p59379267576"></a>ListBucket</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p13937182675716"><a name="p13937182675716"></a><a name="p13937182675716"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p9937926155719"><a name="p9937926155719"></a><a name="p9937926155719"></a>Type: String. Lists objects that begin with the specified prefix.</p>
</td>
</tr>
<tr id="row993792685715"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p69371126115716"><a name="p69371126115716"></a><a name="p69371126115716"></a>delimiter</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p7937172675719"><a name="p7937172675719"></a><a name="p7937172675719"></a>Type: String. Groups objects in a bucket.</p>
</td>
</tr>
<tr id="row13937226115711"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p293712266579"><a name="p293712266579"></a><a name="p293712266579"></a>max-keys</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2093752619576"><a name="p2093752619576"></a><a name="p2093752619576"></a>Type: Numeric. Sets the maximum number of objects. Returned objects are listed in alphabetic order.</p>
</td>
</tr>
<tr id="row8937926195711"><td class="cellrowborder" rowspan="3" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p393712675711"><a name="p393712675711"></a><a name="p393712675711"></a>ListBucketVersions</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p09372264575"><a name="p09372264575"></a><a name="p09372264575"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p693772615577"><a name="p693772615577"></a><a name="p693772615577"></a>Type: String. Lists multi-version objects whose name starts with the specified prefix.</p>
</td>
</tr>
<tr id="row993715262572"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p119371326175713"><a name="p119371326175713"></a><a name="p119371326175713"></a>delimiter</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6937162615576"><a name="p6937162615576"></a><a name="p6937162615576"></a>Type: String. String used to group multi-version objects in a bucket.</p>
</td>
</tr>
<tr id="row693722612571"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p15937326155717"><a name="p15937326155717"></a><a name="p15937326155717"></a>max-keys</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p12938122617571"><a name="p12938122617571"></a><a name="p12938122617571"></a>Type: Numeric. Sets the maximum number of objects. Returned objects are listed in alphabetic order.</p>
</td>
</tr>
<tr id="row193842612574"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p1793819263575"><a name="p1793819263575"></a><a name="p1793819263575"></a>PutBucketAcl</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p139381226195719"><a name="p139381226195719"></a><a name="p139381226195719"></a>acl</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p793892605711"><a name="p793892605711"></a><a name="p793892605711"></a>Type: String. Configures the bucket ACL. When modifying a bucket ACL, you can use the request that contains a canned ACL setting in its header. Value options of a canned ACL setting: <strong id="b316331120554"><a name="b316331120554"></a><a name="b316331120554"></a>private|public-read|public-read-write|authenticated-read|bucket-owner-read|bucket-owner-full-control|log-delivery-write</strong></p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Keys related to object actions

<a name="table14742526145718"></a>
<table><thead align="left"><tr id="row293802635716"><th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.4.1.1"><p id="p99381026135710"><a name="p99381026135710"></a><a name="p99381026135710"></a>Action</p>
</th>
<th class="cellrowborder" valign="top" width="27.55%" id="mcps1.2.4.1.2"><p id="p2938132618576"><a name="p2938132618576"></a><a name="p2938132618576"></a>Optional Key</p>
</th>
<th class="cellrowborder" valign="top" width="48.980000000000004%" id="mcps1.2.4.1.3"><p id="p19938726175710"><a name="p19938726175710"></a><a name="p19938726175710"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19939182618579"><td class="cellrowborder" rowspan="3" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p893942695710"><a name="p893942695710"></a><a name="p893942695710"></a>PutObject</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p493902613571"><a name="p493902613571"></a><a name="p493902613571"></a>acl</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p861813885512"><a name="p861813885512"></a><a name="p861813885512"></a>Type: String. Configures the object ACL. When uploading an object, you can use the request that contains a canned ACL setting in its header. Value options of a canned ACL setting: <strong id="b890214564120"><a name="b890214564120"></a><a name="b890214564120"></a>private|public-read|public-read-write|authenticated-read|bucketowner-read|bucket-owner-full-control|log-delivery-write</strong>.</p>
</td>
</tr>
<tr id="row293932619571"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p19391026155720"><a name="p19391026155720"></a><a name="p19391026155720"></a>copysource</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p393942620578"><a name="p393942620578"></a><a name="p393942620578"></a>Type: String. Specifies names of the source bucket and the source object. Format: <strong id="b1808605689113241"><a name="b1808605689113241"></a><a name="b1808605689113241"></a>/bucketname/keyname</strong></p>
</td>
</tr>
<tr id="row3939626125711"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p15939726165718"><a name="p15939726165718"></a><a name="p15939726165718"></a>metadatadirective</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1293962614575"><a name="p1293962614575"></a><a name="p1293962614575"></a>Type: String. Specifies whether to copy the metadata from the source object or replace with the metadata in the request. Values: <strong id="b89226088811330"><a name="b89226088811330"></a><a name="b89226088811330"></a>COPY|REPLACE</strong></p>
</td>
</tr>
<tr id="row159391126185711"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p6939202611579"><a name="p6939202611579"></a><a name="p6939202611579"></a>PutObjectAcl</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p293992675713"><a name="p293992675713"></a><a name="p293992675713"></a>acl</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p26111442185511"><a name="p26111442185511"></a><a name="p26111442185511"></a>Type: String. Configures the object ACL. When uploading an object, you can use the request that contains a canned ACL setting in its header. Value options of a canned ACL setting: <strong id="b114629269218"><a name="b114629269218"></a><a name="b114629269218"></a>private|public-read|public-read-write|authenticated-read|bucketowner-read|bucket-owner-full-control|log-delivery-write</strong>.</p>
</td>
</tr>
<tr id="row14939172645713"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p16939142613573"><a name="p16939142613573"></a><a name="p16939142613573"></a>GetObjectVersion</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p1294002655714"><a name="p1294002655714"></a><a name="p1294002655714"></a>VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p1494016264579"><a name="p1494016264579"></a><a name="p1494016264579"></a>Type: String. Obtains the object with the specified version ID.</p>
</td>
</tr>
<tr id="row19940172645714"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p2094002613577"><a name="p2094002613577"></a><a name="p2094002613577"></a>GetObjectVersionAcl</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p14940162685715"><a name="p14940162685715"></a><a name="p14940162685715"></a>VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p13940192615574"><a name="p13940192615574"></a><a name="p13940192615574"></a>Type: String. Obtains the ACL of the object with specified version ID.</p>
</td>
</tr>
<tr id="row99401326105715"><td class="cellrowborder" rowspan="2" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p994016263575"><a name="p994016263575"></a><a name="p994016263575"></a>PutObjectVersionAcl</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p7940122655716"><a name="p7940122655716"></a><a name="p7940122655716"></a>VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p1394042615579"><a name="p1394042615579"></a><a name="p1394042615579"></a>Type: String. Specifies a version ID.</p>
</td>
</tr>
<tr id="row1794032615574"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p10940162695719"><a name="p10940162695719"></a><a name="p10940162695719"></a>acl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1392195113554"><a name="p1392195113554"></a><a name="p1392195113554"></a>Type: String. Configures the ACL of the object with the specified version ID. When uploading an object, you can use the request that contains a canned ACL setting in its header. Value options of a canned ACL setting: <strong id="b39801571463"><a name="b39801571463"></a><a name="b39801571463"></a>private|public-read|public-read-write|authenticated-read|bucketowner-read|bucket-owner-full-control|log-delivery-write</strong>.</p>
</td>
</tr>
<tr id="row1394092635717"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p179406267573"><a name="p179406267573"></a><a name="p179406267573"></a>DeleteObjectVersion</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.4.1.2 "><p id="p16940192615577"><a name="p16940192615577"></a><a name="p16940192615577"></a>VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="48.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p13941726185718"><a name="p13941726185718"></a><a name="p13941726185718"></a>Type: String. Deletes the object with the specified version ID.</p>
</td>
</tr>
</tbody>
</table>

