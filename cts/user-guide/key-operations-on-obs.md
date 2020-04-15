# Key Operations on OBS<a name="en-us_topic_0100273717"></a>

Object Storage Service \(OBS\) is a stable, secure, efficient, and easy-to-use cloud storage service. With the Representational State Transfer \(REST\) application programming interface \(API\), OBS is able to store any amount and form of unstructured data.

With CTS, you can record operations associated with OBS for future query, audit, and backtrack operations.

-   For details about operations on OBS buckets, see "Viewing Tracing Events" in the  _Cloud Trace Service Quick Start_. For details about the bucket operations supported by CTS, see  [Table 1](#table1492215471614).
-   After the CTS data tracker is enabled, operations on objects in OBS buckets can be recorded. You can view these records in the OBS bucket configured for the data tracker. In addition, you can enable the  **Trace Analysis**  function to analyze and process data-related trace files generated in the last seven days on the LTS server. For the operations on objects in the OBS bucket that are recorded by CTS, see  [Table 2](#table23254387566).

    **Table  1**  OBS operations that can be recorded by CTS

    <a name="table1492215471614"></a>
    <table><thead align="left"><tr id="row19161854141615"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.4.1.1"><p id="p1191555491613"><a name="p1191555491613"></a><a name="p1191555491613"></a><strong id="b842352706103557_1"><a name="b842352706103557_1"></a><a name="b842352706103557_1"></a>Operation</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p891615417164"><a name="p891615417164"></a><a name="p891615417164"></a><strong id="b84235270610360_1"><a name="b84235270610360_1"></a><a name="b84235270610360_1"></a>Resource Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p159164540166"><a name="p159164540166"></a><a name="p159164540166"></a><strong id="b842352706182955_1"><a name="b842352706182955_1"></a><a name="b842352706182955_1"></a>Trace Name</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17916155471613"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p7916105481614"><a name="p7916105481614"></a><a name="p7916105481614"></a>Deleting a bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1591645441613"><a name="p1591645441613"></a><a name="p1591645441613"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p199160542163"><a name="p199160542163"></a><a name="p199160542163"></a>deleteBucket</p>
    </td>
    </tr>
    <tr id="row6917145410167"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p191716545167"><a name="p191716545167"></a><a name="p191716545167"></a>Deleting the bucket CORS configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p891755471615"><a name="p891755471615"></a><a name="p891755471615"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p991785411169"><a name="p991785411169"></a><a name="p991785411169"></a>deleteBucketCors</p>
    </td>
    </tr>
    <tr id="row17917154141618"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p1291775417165"><a name="p1291775417165"></a><a name="p1291775417165"></a>Deleting the custom domain configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p19917454121613"><a name="p19917454121613"></a><a name="p19917454121613"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1091720542165"><a name="p1091720542165"></a><a name="p1091720542165"></a>deleteBucketCustomdomain</p>
    </td>
    </tr>
    <tr id="row7918654151614"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p1191725420160"><a name="p1191725420160"></a><a name="p1191725420160"></a>Deleting the bucket lifecycle configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p09171554131610"><a name="p09171554131610"></a><a name="p09171554131610"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1591755415165"><a name="p1591755415165"></a><a name="p1591755415165"></a>deleteBucketLifecycle</p>
    </td>
    </tr>
    <tr id="row1291819546168"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p691855414164"><a name="p691855414164"></a><a name="p691855414164"></a>Deleting the bucket policy configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p12918155414162"><a name="p12918155414162"></a><a name="p12918155414162"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1891815416168"><a name="p1891815416168"></a><a name="p1891815416168"></a>deleteBucketPolicy</p>
    </td>
    </tr>
    <tr id="row1891845413168"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p1918954131619"><a name="p1918954131619"></a><a name="p1918954131619"></a>Deleting the bucket cross-region replication configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p891812542165"><a name="p891812542165"></a><a name="p891812542165"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1891865411168"><a name="p1891865411168"></a><a name="p1891865411168"></a>deleteBucketReplication</p>
    </td>
    </tr>
    <tr id="row1791865421612"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p79181554141611"><a name="p79181554141611"></a><a name="p79181554141611"></a>Deleting the bucket tagging configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p11918205412167"><a name="p11918205412167"></a><a name="p11918205412167"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11918155461618"><a name="p11918155461618"></a><a name="p11918155461618"></a>deleteBucketTagging</p>
    </td>
    </tr>
    <tr id="row1891945401612"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p9918654141610"><a name="p9918654141610"></a><a name="p9918654141610"></a>Deleting the bucket website configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p169191654111612"><a name="p169191654111612"></a><a name="p169191654111612"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p189191954141610"><a name="p189191954141610"></a><a name="p189191954141610"></a>deleteBucketWebsite</p>
    </td>
    </tr>
    <tr id="row1891985419162"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p8919135481618"><a name="p8919135481618"></a><a name="p8919135481618"></a>Deleting bucket data</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p591915411617"><a name="p591915411617"></a><a name="p591915411617"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1791955416168"><a name="p1791955416168"></a><a name="p1791955416168"></a>deleteBucketdata</p>
    </td>
    </tr>
    <tr id="row15919854111614"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p12919954171617"><a name="p12919954171617"></a><a name="p12919954171617"></a>Creating a bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1919185421611"><a name="p1919185421611"></a><a name="p1919185421611"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p09191554181610"><a name="p09191554181610"></a><a name="p09191554181610"></a>createBucket</p>
    </td>
    </tr>
    <tr id="row1392011542169"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p15919115412166"><a name="p15919115412166"></a><a name="p15919115412166"></a>Setting the bucket ACL</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p149191454111618"><a name="p149191454111618"></a><a name="p149191454111618"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p8919454121618"><a name="p8919454121618"></a><a name="p8919454121618"></a>setBucketAcl</p>
    </td>
    </tr>
    <tr id="row292035420163"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p149201454201619"><a name="p149201454201619"></a><a name="p149201454201619"></a>Setting the bucket CORS</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p189200541162"><a name="p189200541162"></a><a name="p189200541162"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p69201854191616"><a name="p69201854191616"></a><a name="p69201854191616"></a>setBucketCors</p>
    </td>
    </tr>
    <tr id="row7920115441619"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p179201454151612"><a name="p179201454151612"></a><a name="p179201454151612"></a>Setting the bucket's user-defined domain name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p4920145410167"><a name="p4920145410167"></a><a name="p4920145410167"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p15920254161612"><a name="p15920254161612"></a><a name="p15920254161612"></a>setBucketCustomdomain</p>
    </td>
    </tr>
    <tr id="row15920175414163"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p18920105431611"><a name="p18920105431611"></a><a name="p18920105431611"></a>Setting the bucket lifecycle</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p392017543165"><a name="p392017543165"></a><a name="p392017543165"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p20920454161615"><a name="p20920454161615"></a><a name="p20920454161615"></a>setBucketLifecycle</p>
    </td>
    </tr>
    <tr id="row13921115471617"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p2920554181615"><a name="p2920554181615"></a><a name="p2920554181615"></a>Setting the bucket logging configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p9921185420167"><a name="p9921185420167"></a><a name="p9921185420167"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1921654141618"><a name="p1921654141618"></a><a name="p1921654141618"></a>setBucketLogging</p>
    </td>
    </tr>
    <tr id="row18921175441610"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p5921554131611"><a name="p5921554131611"></a><a name="p5921554131611"></a>Setting the bucket notification</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p99212054201613"><a name="p99212054201613"></a><a name="p99212054201613"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p119211454101619"><a name="p119211454101619"></a><a name="p119211454101619"></a>setBucketNotification</p>
    </td>
    </tr>
    <tr id="row19921354101614"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p792112545164"><a name="p792112545164"></a><a name="p792112545164"></a>Setting the bucket policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p19921205411619"><a name="p19921205411619"></a><a name="p19921205411619"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p149219541163"><a name="p149219541163"></a><a name="p149219541163"></a>setBucketPolicy</p>
    </td>
    </tr>
    <tr id="row0921205414169"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p1921125461619"><a name="p1921125461619"></a><a name="p1921125461619"></a>Setting the bucket quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p15921165441617"><a name="p15921165441617"></a><a name="p15921165441617"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p99211954121613"><a name="p99211954121613"></a><a name="p99211954121613"></a>setBucketQuota</p>
    </td>
    </tr>
    <tr id="row12921654141614"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p1192125421612"><a name="p1192125421612"></a><a name="p1192125421612"></a>Setting the bucket's cross-domain replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1592175418165"><a name="p1592175418165"></a><a name="p1592175418165"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p199218540163"><a name="p199218540163"></a><a name="p199218540163"></a>setBucketReplication</p>
    </td>
    </tr>
    <tr id="row1192225461619"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p1992165419163"><a name="p1992165419163"></a><a name="p1992165419163"></a>Setting the bucket storage class</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p892114547162"><a name="p892114547162"></a><a name="p892114547162"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1792275419165"><a name="p1792275419165"></a><a name="p1792275419165"></a>setBucketStorageclass</p>
    </td>
    </tr>
    <tr id="row1192216547168"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p59221454201611"><a name="p59221454201611"></a><a name="p59221454201611"></a>Setting the bucket tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p09221154131613"><a name="p09221154131613"></a><a name="p09221154131613"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6922135414166"><a name="p6922135414166"></a><a name="p6922135414166"></a>setBucketTagging</p>
    </td>
    </tr>
    <tr id="row7922155418165"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p1292219548163"><a name="p1292219548163"></a><a name="p1292219548163"></a>Setting bucket versioning</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1492217546168"><a name="p1492217546168"></a><a name="p1492217546168"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p89221854171613"><a name="p89221854171613"></a><a name="p89221854171613"></a>setBucketVersioning</p>
    </td>
    </tr>
    <tr id="row1922155421610"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="p16922054121617"><a name="p16922054121617"></a><a name="p16922054121617"></a>Setting the bucket's static domain name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p692217549165"><a name="p692217549165"></a><a name="p692217549165"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1092255461618"><a name="p1092255461618"></a><a name="p1092255461618"></a>setBucketWebsite</p>
    </td>
    </tr>
    </tbody>
    </table>


**Table  2**  OBS object-related operations that can be recorded by CTS

<a name="table23254387566"></a>
<table><thead align="left"><tr id="row2325638115612"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.4.1.1"><p id="p1132553810566"><a name="p1132553810566"></a><a name="p1132553810566"></a><strong id="b842352706103557_3"><a name="b842352706103557_3"></a><a name="b842352706103557_3"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p832517386564"><a name="p832517386564"></a><a name="p832517386564"></a><strong id="b84235270610360_3"><a name="b84235270610360_3"></a><a name="b84235270610360_3"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p1532573810563"><a name="p1532573810563"></a><a name="p1532573810563"></a><strong id="b842352706182955_3"><a name="b842352706182955_3"></a><a name="b842352706182955_3"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2341338165612"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="a1cf58eaefab94121ad2ab0119b770cb2"><a name="a1cf58eaefab94121ad2ab0119b770cb2"></a><a name="a1cf58eaefab94121ad2ab0119b770cb2"></a>Downloading an object</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p18467755162319"><a name="p18467755162319"></a><a name="p18467755162319"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p769032316340"><a name="en-us_topic_0100240354_p769032316340"></a><a name="en-us_topic_0100240354_p769032316340"></a>GET.OBJECT</p>
</td>
</tr>
<tr id="row6912454105615"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="a9737632e6b1a4038b75b4d7ffd9b575e"><a name="a9737632e6b1a4038b75b4d7ffd9b575e"></a><a name="a9737632e6b1a4038b75b4d7ffd9b575e"></a>Querying the object ACL</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p2467115519234"><a name="p2467115519234"></a><a name="p2467115519234"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a92824a2e405e4287a5231af1319425d7"><a name="a92824a2e405e4287a5231af1319425d7"></a><a name="a92824a2e405e4287a5231af1319425d7"></a>GET.OBJECT.ACL</p>
</td>
</tr>
<tr id="row45837117576"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="ac0952ca32117404f8fc3449ca900e9d4"><a name="ac0952ca32117404f8fc3449ca900e9d4"></a><a name="ac0952ca32117404f8fc3449ca900e9d4"></a>Querying the bucket website</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p124671655172318"><a name="p124671655172318"></a><a name="p124671655172318"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a08eb5c84a09e4b93995c044e8eba440c"><a name="a08eb5c84a09e4b93995c044e8eba440c"></a><a name="a08eb5c84a09e4b93995c044e8eba440c"></a>GET.OBJECT.WEBSITE</p>
</td>
</tr>
<tr id="row18583312575"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="a1d26818768ea4686b86ae9e0c302a863"><a name="a1d26818768ea4686b86ae9e0c302a863"></a><a name="a1d26818768ea4686b86ae9e0c302a863"></a>Accessing an object using the website</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1046785514236"><a name="p1046785514236"></a><a name="p1046785514236"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p849204816340"><a name="en-us_topic_0100240354_p849204816340"></a><a name="en-us_topic_0100240354_p849204816340"></a>HEAD.OBJECT.WEBSITE</p>
</td>
</tr>
<tr id="row198413514571"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="a10288b873bdd4b7b82a6ed3882fb2e16"><a name="a10288b873bdd4b7b82a6ed3882fb2e16"></a><a name="a10288b873bdd4b7b82a6ed3882fb2e16"></a>Querying the object metadata</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p746715513238"><a name="p746715513238"></a><a name="p746715513238"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a964f7aa6bbc646df865852dfbc69cd66"><a name="a964f7aa6bbc646df865852dfbc69cd66"></a><a name="a964f7aa6bbc646df865852dfbc69cd66"></a>HEAD.OBJECT</p>
</td>
</tr>
<tr id="row1584954572"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="acb6bc1f225584523adcb697eaa282cc5"><a name="acb6bc1f225584523adcb697eaa282cc5"></a><a name="acb6bc1f225584523adcb697eaa282cc5"></a>Listing part data</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p54671557235"><a name="p54671557235"></a><a name="p54671557235"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2da3e0527dd9416bbd772daf5d51a45b"><a name="a2da3e0527dd9416bbd772daf5d51a45b"></a><a name="a2da3e0527dd9416bbd772daf5d51a45b"></a>LIST.OBJECT.UPLOAD</p>
</td>
</tr>
<tr id="row0841656579"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="a23d42f626054444598ed9010dd9f8b58"><a name="a23d42f626054444598ed9010dd9f8b58"></a><a name="a23d42f626054444598ed9010dd9f8b58"></a>Deleting an object</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1646715572311"><a name="p1646715572311"></a><a name="p1646715572311"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2739edd5797e4a6298ff36781b986291"><a name="a2739edd5797e4a6298ff36781b986291"></a><a name="a2739edd5797e4a6298ff36781b986291"></a>DELETE.OBJECT</p>
</td>
</tr>
<tr id="row3841053578"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="ac4307c47b2e84a27bdb81561be32ac45"><a name="ac4307c47b2e84a27bdb81561be32ac45"></a><a name="ac4307c47b2e84a27bdb81561be32ac45"></a>Canceling a part</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p12467155513231"><a name="p12467155513231"></a><a name="p12467155513231"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p651661516340"><a name="en-us_topic_0100240354_p651661516340"></a><a name="en-us_topic_0100240354_p651661516340"></a>DELETE.UPLOAD</p>
</td>
</tr>
<tr id="row1811618136574"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="ab5d4f22b61e4402391a6bee10e0ca619"><a name="ab5d4f22b61e4402391a6bee10e0ca619"></a><a name="ab5d4f22b61e4402391a6bee10e0ca619"></a>Querying the object cross-domain request</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p84676554237"><a name="p84676554237"></a><a name="p84676554237"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad26476a23a5d4838947b840c554d027d"><a name="ad26476a23a5d4838947b840c554d027d"></a><a name="ad26476a23a5d4838947b840c554d027d"></a>OPTIONS.OBJECT</p>
</td>
</tr>
<tr id="row1811671355714"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="a89eeb83ef65246f0a0ede42aed49135c"><a name="a89eeb83ef65246f0a0ede42aed49135c"></a><a name="a89eeb83ef65246f0a0ede42aed49135c"></a>Uploading an object</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1146705522313"><a name="p1146705522313"></a><a name="p1146705522313"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a74ca1a77770149d8bb84c275dfcd504d"><a name="a74ca1a77770149d8bb84c275dfcd504d"></a><a name="a74ca1a77770149d8bb84c275dfcd504d"></a>POST.OBJECT</p>
</td>
</tr>
<tr id="row111641319577"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="affc3e7a2c5214567af5208b64fbbe34e"><a name="affc3e7a2c5214567af5208b64fbbe34e"></a><a name="affc3e7a2c5214567af5208b64fbbe34e"></a>Batch deleting objects</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p7467145522313"><a name="p7467145522313"></a><a name="p7467145522313"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab69c003d744a4e4dbce14a2533dc1f66"><a name="ab69c003d744a4e4dbce14a2533dc1f66"></a><a name="ab69c003d744a4e4dbce14a2533dc1f66"></a>POST.OBJECT.MULTIDELETE</p>
</td>
</tr>
<tr id="row13116171365718"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="aeb3c4288d3a9444a82ccb67e73186546"><a name="aeb3c4288d3a9444a82ccb67e73186546"></a><a name="aeb3c4288d3a9444a82ccb67e73186546"></a>Restoring cold objects</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p144671555172318"><a name="p144671555172318"></a><a name="p144671555172318"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a0c952dcac28542898537991fd63b9764"><a name="a0c952dcac28542898537991fd63b9764"></a><a name="a0c952dcac28542898537991fd63b9764"></a>POST.OBJECT.RESTORE</p>
</td>
</tr>
<tr id="row511691310577"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="a3e8b9cb3b98e484781dcfaaee70f029c"><a name="a3e8b9cb3b98e484781dcfaaee70f029c"></a><a name="a3e8b9cb3b98e484781dcfaaee70f029c"></a>Combining parts</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p13467125519236"><a name="p13467125519236"></a><a name="p13467125519236"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a38c98dcccfd74e23b2962eda255c52f5"><a name="a38c98dcccfd74e23b2962eda255c52f5"></a><a name="a38c98dcccfd74e23b2962eda255c52f5"></a>POST.UPLOAD.COMPLETE</p>
</td>
</tr>
<tr id="row0116121325715"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p803666916317"><a name="en-us_topic_0100240354_p803666916317"></a><a name="en-us_topic_0100240354_p803666916317"></a>Initializing a part</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p204671555142313"><a name="p204671555142313"></a><a name="p204671555142313"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="abf1a39674b0e46efac2da864331a9cf0"><a name="abf1a39674b0e46efac2da864331a9cf0"></a><a name="abf1a39674b0e46efac2da864331a9cf0"></a>POST.UPLOAD.INIT</p>
</td>
</tr>
<tr id="row411621355710"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="abaeb99dcc1f9418082813e1bc6d5d56d"><a name="abaeb99dcc1f9418082813e1bc6d5d56d"></a><a name="abaeb99dcc1f9418082813e1bc6d5d56d"></a>Uploading an object</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p7467125510231"><a name="p7467125510231"></a><a name="p7467125510231"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p206037616340"><a name="en-us_topic_0100240354_p206037616340"></a><a name="en-us_topic_0100240354_p206037616340"></a>PUT.OBJECT</p>
</td>
</tr>
<tr id="row1411671335713"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p624523516317"><a name="en-us_topic_0100240354_p624523516317"></a><a name="en-us_topic_0100240354_p624523516317"></a>Setting the object ACL</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p144671855122318"><a name="p144671855122318"></a><a name="p144671855122318"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a28380384ba9944c382d2de15aad1f216"><a name="a28380384ba9944c382d2de15aad1f216"></a><a name="a28380384ba9944c382d2de15aad1f216"></a>PUT.OBJECT.ACL</p>
</td>
</tr>
<tr id="row788014171578"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="aef1c0d2c83754c6aa0af97e222acb539"><a name="aef1c0d2c83754c6aa0af97e222acb539"></a><a name="aef1c0d2c83754c6aa0af97e222acb539"></a>Copying an object</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p446745512237"><a name="p446745512237"></a><a name="p446745512237"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a83da4f0b8ad44b50ba77e627b4156539"><a name="a83da4f0b8ad44b50ba77e627b4156539"></a><a name="a83da4f0b8ad44b50ba77e627b4156539"></a>PUT.OBJECT.COPY</p>
</td>
</tr>
<tr id="row16880121713571"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="a5a8b079e714b45769d64acc5ba736c6c"><a name="a5a8b079e714b45769d64acc5ba736c6c"></a><a name="a5a8b079e714b45769d64acc5ba736c6c"></a>Setting the object storage class</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p7467135502320"><a name="p7467135502320"></a><a name="p7467135502320"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a4837c690a7e34de0837025fa52d73022"><a name="a4837c690a7e34de0837025fa52d73022"></a><a name="a4837c690a7e34de0837025fa52d73022"></a>PUT.OBJECT.STORAGECLASS</p>
</td>
</tr>
<tr id="row1988011720573"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p185105316317"><a name="en-us_topic_0100240354_p185105316317"></a><a name="en-us_topic_0100240354_p185105316317"></a>Uploading a part</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p5467125515232"><a name="p5467125515232"></a><a name="p5467125515232"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="af19ab2413c8e4b80893f42beae91bf04"><a name="af19ab2413c8e4b80893f42beae91bf04"></a><a name="af19ab2413c8e4b80893f42beae91bf04"></a>PUT.PART</p>
</td>
</tr>
<tr id="row16880217175710"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p724098416317"><a name="en-us_topic_0100240354_p724098416317"></a><a name="en-us_topic_0100240354_p724098416317"></a>Copying a part</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1046715551236"><a name="p1046715551236"></a><a name="p1046715551236"></a>object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa7d21bf04678438bbb28cf48db2e537b"><a name="aa7d21bf04678438bbb28cf48db2e537b"></a><a name="aa7d21bf04678438bbb28cf48db2e537b"></a>PUT.PART.COPY</p>
</td>
</tr>
</tbody>
</table>

