# Permissions Management<a name="obs_03_0045"></a>

If you have OBS resources and you need to grant different access permissions to different user roles, you can leverage the Identity and Access Management \(IAM\) service for fine-grained permission control. IAM provides identity authentication, permissions management, and access control, helping you provide secure access to your cloud resources.

With IAM, you can use your account to create IAM users, and assign permissions to the users to control their access to specific resources. For example, if you have software developers and you want to grant them the permission to only access OBS but not delete OBS resources, you can create an IAM policy that only grants the developers the permission to access OBS.

If your service account does not have individual IAM users, please skip this section.

## OBS Permissions<a name="section9905344171915"></a>

By default, new IAM users do not have any permissions assigned. You need to add a user to one or more user groups, and assign permission policies to the user groups. The user then inherits permissions from the user groups. This process is known as authorization. After authorization, the user can perform specific operations on cloud services based on permission policies. IAM provides preset system policies that define common permissions for different services.

OBS is a global service because it is available for all physical regions. OBS permissions are assigned to users in the Global project, and users do not need to switch the region when accessing OBS.

RBAC policy: An RBAC policy consists of permissions for an entire service. Users in a group with such a policy assigned are granted all the required permissions, including permissions for accessing and managing that service. RBAC policies do not support operation-specific permission control.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>Due to the cache mechanism, it takes about 13 minutes for an RBAC policy to take effect after being granted to users and user groups.

[Table 1](#table358116162418)  lists all system policies of OBS.

**Table  1**  OBS system policies

<a name="table358116162418"></a>
<table><thead align="left"><tr id="row175981662412"><th class="cellrowborder" valign="top" width="25.16251625162516%" id="mcps1.2.4.1.1"><p id="p15751162118241"><a name="p15751162118241"></a><a name="p15751162118241"></a>Policy</p>
</th>
<th class="cellrowborder" valign="top" width="53.63536353635363%" id="mcps1.2.4.1.2"><p id="p575202118246"><a name="p575202118246"></a><a name="p575202118246"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="21.202120212021203%" id="mcps1.2.4.1.3"><p id="p2075272162417"><a name="p2075272162417"></a><a name="p2075272162417"></a>Policy Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row185915168243"><td class="cellrowborder" valign="top" width="25.16251625162516%" headers="mcps1.2.4.1.1 "><p id="p1955018391441"><a name="p1955018391441"></a><a name="p1955018391441"></a>Tenant Administrator</p>
</td>
<td class="cellrowborder" valign="top" width="53.63536353635363%" headers="mcps1.2.4.1.2 "><p id="p2098032784834"><a name="p2098032784834"></a><a name="p2098032784834"></a>Operation permissions: any operation on all cloud resources owned by the account</p>
<p id="p1572511180216"><a name="p1572511180216"></a><a name="p1572511180216"></a>OBS policies are configured under <strong id="b1065312263712"><a name="b1065312263712"></a><a name="b1065312263712"></a>Global service</strong> &gt; <strong id="b1410043533719"><a name="b1410043533719"></a><a name="b1410043533719"></a>OBS</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="21.202120212021203%" headers="mcps1.2.4.1.3 "><p id="p559161618249"><a name="p559161618249"></a><a name="p559161618249"></a>RBAC policy</p>
</td>
</tr>
<tr id="row165901622410"><td class="cellrowborder" valign="top" width="25.16251625162516%" headers="mcps1.2.4.1.1 "><p id="p13562139348"><a name="p13562139348"></a><a name="p13562139348"></a>Tenant Guest</p>
</td>
<td class="cellrowborder" valign="top" width="53.63536353635363%" headers="mcps1.2.4.1.2 "><p id="p1656510396414"><a name="p1656510396414"></a><a name="p1656510396414"></a>Operation permissions: read-only access permission to all cloud resources owned by the account</p>
<p id="p109361864413"><a name="p109361864413"></a><a name="p109361864413"></a>OBS policies are configured under <strong id="obs_03_0045_b1065312263712"><a name="obs_03_0045_b1065312263712"></a><a name="obs_03_0045_b1065312263712"></a>Global service</strong> &gt; <strong id="obs_03_0045_b1410043533719"><a name="obs_03_0045_b1410043533719"></a><a name="obs_03_0045_b1410043533719"></a>OBS</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="21.202120212021203%" headers="mcps1.2.4.1.3 "><p id="p059191620245"><a name="p059191620245"></a><a name="p059191620245"></a>RBAC policy</p>
</td>
</tr>
<tr id="row859151682419"><td class="cellrowborder" valign="top" width="25.16251625162516%" headers="mcps1.2.4.1.1 "><p id="p10210182816543"><a name="p10210182816543"></a><a name="p10210182816543"></a>OBS Buckets Viewer</p>
</td>
<td class="cellrowborder" valign="top" width="53.63536353635363%" headers="mcps1.2.4.1.2 "><p id="p1421032875416"><a name="p1421032875416"></a><a name="p1421032875416"></a>Operation permissions: listing buckets, obtaining basic bucket information, obtaining bucket metadata information, and listing objects</p>
<p id="p837445918612"><a name="p837445918612"></a><a name="p837445918612"></a>OBS policies are configured under <strong id="obs_03_0045_b1065312263712_1"><a name="obs_03_0045_b1065312263712_1"></a><a name="obs_03_0045_b1065312263712_1"></a>Global service</strong> &gt; <strong id="obs_03_0045_b1410043533719_1"><a name="obs_03_0045_b1410043533719_1"></a><a name="obs_03_0045_b1410043533719_1"></a>OBS</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="21.202120212021203%" headers="mcps1.2.4.1.3 "><p id="p5210102816548"><a name="p5210102816548"></a><a name="p5210102816548"></a>RBAC policy</p>
</td>
</tr>
</tbody>
</table>

The following table lists operations that can be performed under each set of OBS permission.

**Table  2**  Permissions and the allowed operations on OBS resources

<a name="table487418345322"></a>
<table><thead align="left"><tr id="row18752034153214"><th class="cellrowborder" valign="top" width="35.75714285714287%" id="mcps1.2.5.1.1"><p id="p19875183413211"><a name="p19875183413211"></a><a name="p19875183413211"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="21.385714285714286%" id="mcps1.2.5.1.2"><p id="p1787543415321"><a name="p1787543415321"></a><a name="p1787543415321"></a>Tenant Administrator</p>
</th>
<th class="cellrowborder" valign="top" width="21.45714285714286%" id="mcps1.2.5.1.3"><p id="p17875183453217"><a name="p17875183453217"></a><a name="p17875183453217"></a>Tenant Guest</p>
</th>
<th class="cellrowborder" valign="top" width="21.4%" id="mcps1.2.5.1.4"><p id="p1875143419322"><a name="p1875143419322"></a><a name="p1875143419322"></a>OBS Buckets Viewer</p>
</th>
</tr>
</thead>
<tbody><tr id="row38751334123213"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p4875334173218"><a name="p4875334173218"></a><a name="p4875334173218"></a>Listing buckets</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p158751234193220"><a name="p158751234193220"></a><a name="p158751234193220"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p17875934133211"><a name="p17875934133211"></a><a name="p17875934133211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p3875123473211"><a name="p3875123473211"></a><a name="p3875123473211"></a>Yes</p>
</td>
</tr>
<tr id="row1687563493217"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p287513414329"><a name="p287513414329"></a><a name="p287513414329"></a>Creating buckets</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p3875203413327"><a name="p3875203413327"></a><a name="p3875203413327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p1587593413213"><a name="p1587593413213"></a><a name="p1587593413213"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1487512349322"><a name="p1487512349322"></a><a name="p1487512349322"></a>No</p>
</td>
</tr>
<tr id="row11875183410322"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p13875134133219"><a name="p13875134133219"></a><a name="p13875134133219"></a>Deleting buckets</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p1687515347324"><a name="p1687515347324"></a><a name="p1687515347324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p17875434193217"><a name="p17875434193217"></a><a name="p17875434193217"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p387503415322"><a name="p387503415322"></a><a name="p387503415322"></a>No</p>
</td>
</tr>
<tr id="row987573417327"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p148751134173213"><a name="p148751134173213"></a><a name="p148751134173213"></a>Obtaining basic bucket information</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p138751334113219"><a name="p138751334113219"></a><a name="p138751334113219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p1087523483213"><a name="p1087523483213"></a><a name="p1087523483213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p987573463218"><a name="p987573463218"></a><a name="p987573463218"></a>Yes</p>
<div class="note" id="note8654185219"><a name="note8654185219"></a><a name="note8654185219"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p0654118329"><a name="p0654118329"></a><a name="p0654118329"></a>The statistics of used storage space and number of objects cannot be obtained.</p>
</div></div>
</td>
</tr>
<tr id="row4876113433212"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p4876183473211"><a name="p4876183473211"></a><a name="p4876183473211"></a>Controlling bucket access</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p9876193415323"><a name="p9876193415323"></a><a name="p9876193415323"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p17876133418322"><a name="p17876133418322"></a><a name="p17876133418322"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p987673410324"><a name="p987673410324"></a><a name="p987673410324"></a>No</p>
</td>
</tr>
<tr id="row1387615347325"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p15876133413320"><a name="p15876133413320"></a><a name="p15876133413320"></a>Managing bucket policies</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p6876113418328"><a name="p6876113418328"></a><a name="p6876113418328"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p88761434143216"><a name="p88761434143216"></a><a name="p88761434143216"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p9876113443216"><a name="p9876113443216"></a><a name="p9876113443216"></a>No</p>
</td>
</tr>
<tr id="row16876634103218"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p0876153433214"><a name="p0876153433214"></a><a name="p0876153433214"></a>Modifying bucket storage classes</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p387643423218"><a name="p387643423218"></a><a name="p387643423218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p6876103423217"><a name="p6876103423217"></a><a name="p6876103423217"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p16876634123220"><a name="p16876634123220"></a><a name="p16876634123220"></a>No</p>
</td>
</tr>
<tr id="row158761634103210"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p188762034103218"><a name="p188762034103218"></a><a name="p188762034103218"></a>Listing objects</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p587663411323"><a name="p587663411323"></a><a name="p587663411323"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p287673417327"><a name="p287673417327"></a><a name="p287673417327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p415417192586"><a name="p415417192586"></a><a name="p415417192586"></a>Yes</p>
</td>
</tr>
<tr id="row28761934203219"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p18876123453215"><a name="p18876123453215"></a><a name="p18876123453215"></a>Listing objects with multiple versions</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p38777342320"><a name="p38777342320"></a><a name="p38777342320"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p158771134153210"><a name="p158771134153210"></a><a name="p158771134153210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1787710348327"><a name="p1787710348327"></a><a name="p1787710348327"></a>No</p>
</td>
</tr>
<tr id="row08771934103210"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p287723417322"><a name="p287723417322"></a><a name="p287723417322"></a>Uploading files</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p187753413215"><a name="p187753413215"></a><a name="p187753413215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p78771134103215"><a name="p78771134103215"></a><a name="p78771134103215"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1687713413215"><a name="p1687713413215"></a><a name="p1687713413215"></a>No</p>
</td>
</tr>
<tr id="row13877153414323"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p1877103443215"><a name="p1877103443215"></a><a name="p1877103443215"></a>Creating folders</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p11877173419320"><a name="p11877173419320"></a><a name="p11877173419320"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p087733433213"><a name="p087733433213"></a><a name="p087733433213"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p13877634133219"><a name="p13877634133219"></a><a name="p13877634133219"></a>No</p>
</td>
</tr>
<tr id="row6877234123218"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p987713349327"><a name="p987713349327"></a><a name="p987713349327"></a>Deleting files</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p158772342328"><a name="p158772342328"></a><a name="p158772342328"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p1687853413212"><a name="p1687853413212"></a><a name="p1687853413212"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p12878334153217"><a name="p12878334153217"></a><a name="p12878334153217"></a>No</p>
</td>
</tr>
<tr id="row2087803443216"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p287811343321"><a name="p287811343321"></a><a name="p287811343321"></a>Deleting folders</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p148782034193217"><a name="p148782034193217"></a><a name="p148782034193217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p187813423210"><a name="p187813423210"></a><a name="p187813423210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p387833412329"><a name="p387833412329"></a><a name="p387833412329"></a>No</p>
</td>
</tr>
<tr id="row887883443219"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p178781234133217"><a name="p178781234133217"></a><a name="p178781234133217"></a>Downloading files</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p1487873419324"><a name="p1487873419324"></a><a name="p1487873419324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p138781034103212"><a name="p138781034103212"></a><a name="p138781034103212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p14878534183210"><a name="p14878534183210"></a><a name="p14878534183210"></a>No</p>
</td>
</tr>
<tr id="row148786344325"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p38781534163214"><a name="p38781534163214"></a><a name="p38781534163214"></a>Deleting files with multiple versions</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p168781734153213"><a name="p168781734153213"></a><a name="p168781734153213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p287893433210"><a name="p287893433210"></a><a name="p287893433210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1587833473213"><a name="p1587833473213"></a><a name="p1587833473213"></a>No</p>
</td>
</tr>
<tr id="row2087817349322"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p287993411325"><a name="p287993411325"></a><a name="p287993411325"></a>Downloading files with multiple versions</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p188795346321"><a name="p188795346321"></a><a name="p188795346321"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p7879103419329"><a name="p7879103419329"></a><a name="p7879103419329"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p48791134133216"><a name="p48791134133216"></a><a name="p48791134133216"></a>No</p>
</td>
</tr>
<tr id="row987919344325"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p287953463220"><a name="p287953463220"></a><a name="p287953463220"></a>Modifying object storage classes</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p18879193483210"><a name="p18879193483210"></a><a name="p18879193483210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p10879134153219"><a name="p10879134153219"></a><a name="p10879134153219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1087913419325"><a name="p1087913419325"></a><a name="p1087913419325"></a>No</p>
</td>
</tr>
<tr id="row108790349328"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p7879203433218"><a name="p7879203433218"></a><a name="p7879203433218"></a>Restoring files</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p9879173411327"><a name="p9879173411327"></a><a name="p9879173411327"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p2087913346324"><a name="p2087913346324"></a><a name="p2087913346324"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p11879173416321"><a name="p11879173416321"></a><a name="p11879173416321"></a>No</p>
</td>
</tr>
<tr id="row2879153418326"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p1288033410329"><a name="p1288033410329"></a><a name="p1288033410329"></a>Canceling the deletion of files</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p1488018348328"><a name="p1488018348328"></a><a name="p1488018348328"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p19880634143210"><a name="p19880634143210"></a><a name="p19880634143210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1888093443212"><a name="p1888093443212"></a><a name="p1888093443212"></a>No</p>
</td>
</tr>
<tr id="row688093443220"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p1288014346328"><a name="p1288014346328"></a><a name="p1288014346328"></a>Deleting fragments</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p118801634153215"><a name="p118801634153215"></a><a name="p118801634153215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p12880734183213"><a name="p12880734183213"></a><a name="p12880734183213"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p48801334173211"><a name="p48801334173211"></a><a name="p48801334173211"></a>No</p>
</td>
</tr>
<tr id="row11880123463217"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p1288043414323"><a name="p1288043414323"></a><a name="p1288043414323"></a>Controlling object access</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p288003415323"><a name="p288003415323"></a><a name="p288003415323"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p0880173453213"><a name="p0880173453213"></a><a name="p0880173453213"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p17880113415327"><a name="p17880113415327"></a><a name="p17880113415327"></a>No</p>
</td>
</tr>
<tr id="row588113349321"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p2088123463216"><a name="p2088123463216"></a><a name="p2088123463216"></a>Configuring object metadata</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p888133416323"><a name="p888133416323"></a><a name="p888133416323"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p4881113417323"><a name="p4881113417323"></a><a name="p4881113417323"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p6881183420322"><a name="p6881183420322"></a><a name="p6881183420322"></a>No</p>
</td>
</tr>
<tr id="row1061717483135"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p1078225161310"><a name="p1078225161310"></a><a name="p1078225161310"></a>Obtaining object metadata</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p1617174815139"><a name="p1617174815139"></a><a name="p1617174815139"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p1261116718143"><a name="p1261116718143"></a><a name="p1261116718143"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1611977144"><a name="p1611977144"></a><a name="p1611977144"></a>No</p>
</td>
</tr>
<tr id="row1388123473217"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p16881234133216"><a name="p16881234133216"></a><a name="p16881234133216"></a>Managing versioning</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p7881143473210"><a name="p7881143473210"></a><a name="p7881143473210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p1588193483217"><a name="p1588193483217"></a><a name="p1588193483217"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p5881133413214"><a name="p5881133413214"></a><a name="p5881133413214"></a>No</p>
</td>
</tr>
<tr id="row18810349322"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p118811434163214"><a name="p118811434163214"></a><a name="p118811434163214"></a>Managing logging</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p388173433219"><a name="p388173433219"></a><a name="p388173433219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p98812348327"><a name="p98812348327"></a><a name="p98812348327"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1888283463214"><a name="p1888283463214"></a><a name="p1888283463214"></a>No</p>
</td>
</tr>
<tr id="row288263473212"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p158825342326"><a name="p158825342326"></a><a name="p158825342326"></a>Managing event notifications</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p78824343324"><a name="p78824343324"></a><a name="p78824343324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p1288273415323"><a name="p1288273415323"></a><a name="p1288273415323"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1588219345328"><a name="p1588219345328"></a><a name="p1588219345328"></a>No</p>
</td>
</tr>
<tr id="row19882153413329"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p88821934163215"><a name="p88821934163215"></a><a name="p88821934163215"></a>Managing tags</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p2882134113215"><a name="p2882134113215"></a><a name="p2882134113215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p16882143443218"><a name="p16882143443218"></a><a name="p16882143443218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p188213343323"><a name="p188213343323"></a><a name="p188213343323"></a>No</p>
</td>
</tr>
<tr id="row288263463213"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p3882193423217"><a name="p3882193423217"></a><a name="p3882193423217"></a>Managing lifecycle rules</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p1088223415325"><a name="p1088223415325"></a><a name="p1088223415325"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p11882163414328"><a name="p11882163414328"></a><a name="p11882163414328"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1188283453213"><a name="p1188283453213"></a><a name="p1188283453213"></a>No</p>
</td>
</tr>
<tr id="row68823341324"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p198821634123215"><a name="p198821634123215"></a><a name="p198821634123215"></a>Managing static website hosting</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p78821434163215"><a name="p78821434163215"></a><a name="p78821434163215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p16882143423219"><a name="p16882143423219"></a><a name="p16882143423219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p10882123413323"><a name="p10882123413323"></a><a name="p10882123413323"></a>No</p>
</td>
</tr>
<tr id="row1088313342325"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p2088320347328"><a name="p2088320347328"></a><a name="p2088320347328"></a>Managing CORS rules</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p14883134103218"><a name="p14883134103218"></a><a name="p14883134103218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p1188310342324"><a name="p1188310342324"></a><a name="p1188310342324"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p16883834163217"><a name="p16883834163217"></a><a name="p16883834163217"></a>No</p>
</td>
</tr>
<tr id="row128831834163213"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p14883143420323"><a name="p14883143420323"></a><a name="p14883143420323"></a>Managing URL validation</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p108838346326"><a name="p108838346326"></a><a name="p108838346326"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p98831834153211"><a name="p98831834153211"></a><a name="p98831834153211"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p168837347327"><a name="p168837347327"></a><a name="p168837347327"></a>No</p>
</td>
</tr>
<tr id="row14833159185118"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p168336590517"><a name="p168336590517"></a><a name="p168336590517"></a>Configuring object ACL</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p1783405916516"><a name="p1783405916516"></a><a name="p1783405916516"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p346217589522"><a name="p346217589522"></a><a name="p346217589522"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p94628586521"><a name="p94628586521"></a><a name="p94628586521"></a>No</p>
</td>
</tr>
<tr id="row61481058105113"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p121484582512"><a name="p121484582512"></a><a name="p121484582512"></a>Configuring the ACL for an object of a specified version</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p314895845112"><a name="p314895845112"></a><a name="p314895845112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p19462135805210"><a name="p19462135805210"></a><a name="p19462135805210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p17462105818522"><a name="p17462105818522"></a><a name="p17462105818522"></a>No</p>
</td>
</tr>
<tr id="row46051438185219"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p144112452527"><a name="p144112452527"></a><a name="p144112452527"></a>Obtaining object ACL information</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p760623825215"><a name="p760623825215"></a><a name="p760623825215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p8462958195214"><a name="p8462958195214"></a><a name="p8462958195214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p164629580527"><a name="p164629580527"></a><a name="p164629580527"></a>No</p>
</td>
</tr>
<tr id="row15514134118523"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p341154595212"><a name="p341154595212"></a><a name="p341154595212"></a>Obtaining the ACL information of a specified object version</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p951417411526"><a name="p951417411526"></a><a name="p951417411526"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p194621658125215"><a name="p194621658125215"></a><a name="p194621658125215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p12462558175212"><a name="p12462558175212"></a><a name="p12462558175212"></a>No</p>
</td>
</tr>
<tr id="row34981656105416"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p849865615548"><a name="p849865615548"></a><a name="p849865615548"></a>Uploading in the multipart mode</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p74519365510"><a name="p74519365510"></a><a name="p74519365510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p445163185519"><a name="p445163185519"></a><a name="p445163185519"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p12451365516"><a name="p12451365516"></a><a name="p12451365516"></a>No</p>
</td>
</tr>
<tr id="row46882362507"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p5688836145016"><a name="p5688836145016"></a><a name="p5688836145016"></a>Listing uploaded parts</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p399713018513"><a name="p399713018513"></a><a name="p399713018513"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p168936318512"><a name="p168936318512"></a><a name="p168936318512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p789315313510"><a name="p789315313510"></a><a name="p789315313510"></a>No</p>
</td>
</tr>
<tr id="row17345184735011"><td class="cellrowborder" valign="top" width="35.75714285714287%" headers="mcps1.2.5.1.1 "><p id="p9345114714501"><a name="p9345114714501"></a><a name="p9345114714501"></a>Canceling multipart tasks</p>
</td>
<td class="cellrowborder" valign="top" width="21.385714285714286%" headers="mcps1.2.5.1.2 "><p id="p352114115111"><a name="p352114115111"></a><a name="p352114115111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.45714285714286%" headers="mcps1.2.5.1.3 "><p id="p55481942513"><a name="p55481942513"></a><a name="p55481942513"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.4%" headers="mcps1.2.5.1.4 "><p id="p1954844135115"><a name="p1954844135115"></a><a name="p1954844135115"></a>No</p>
</td>
</tr>
</tbody>
</table>

## Managing OBS Resource Permissions<a name="section4856147369"></a>

Access to OBS buckets and objects can be controlled by IAM user permissions, bucket policies, and ACLs.

For more information, see  [Overview](permission-control-overview-(console).md).

