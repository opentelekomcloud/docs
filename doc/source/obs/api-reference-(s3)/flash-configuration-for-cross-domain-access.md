# Flash Configuration for Cross-Domain Access<a name="EN-US_TOPIC_0125560477"></a>

By default, OBS system is configured to support cross-domain access using the root domain name. This allows access from all domains, so clients are likely to be attacked.

To address this issue, you can create a  **crossdomain.xml** file with specific rules in the bucket for each client, and add **Security.loadPolicyFile\(http://obs.example.com/bucket/crossdomain.xml\)**  in the file's flash code to prevent attacks.

The following is an example of the  **crossdomain.xml**  file:

```
<?xml version="1.0"?>
<cross-domain-policy>
<allow-access-from domain="*" to-ports="80,443" secure="false"/>
<site-control permitted-cross-domain-policies="master-only" />
</cross-domain-policy>
```

**crossdomain.xml**  needs to comply with the XML syntax rules, and there is only one root node  **cross-domain-policy**  without any attribute. The root node can contain only the following sub-nodes: site-control, allow-access-from, allow-access-from-identity, and allow-http-request-headers-from. The following table lists description about sub-nodes.

**Table  1** 

<a name="table127711534194913"></a>
<table><thead align="left"><tr id="row1577243484911"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.3.1.1"><p id="p97722341492"><a name="p97722341492"></a><a name="p97722341492"></a><strong id="b1334055017505"><a name="b1334055017505"></a><a name="b1334055017505"></a>Sub-node</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.3.1.2"><p id="p11772634124917"><a name="p11772634124917"></a><a name="p11772634124917"></a><strong id="b8344205014508"><a name="b8344205014508"></a><a name="b8344205014508"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row27728341498"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1277243444913"><a name="p1277243444913"></a><a name="p1277243444913"></a><strong id="b4969559506"><a name="b4969559506"></a><a name="b4969559506"></a>site-control</strong></p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p15772133414917"><a name="p15772133414917"></a><a name="p15772133414917"></a>Checks the attribute value and determines whether other policy files can be loaded.</p>
<p id="p1590723195114"><a name="p1590723195114"></a><a name="p1590723195114"></a>The attribute value can be:</p>
<p id="p228417523515"><a name="p228417523515"></a><a name="p228417523515"></a><strong id="b1436115123528"><a name="b1436115123528"></a><a name="b1436115123528"></a>none</strong>: <strong id="b61800216576"><a name="b61800216576"></a><a name="b61800216576"></a>loadPolicyFile</strong> cannot be used to load any policy file.</p>
<p id="p3559191718520"><a name="p3559191718520"></a><a name="p3559191718520"></a><strong id="b37377048161524"><a name="b37377048161524"></a><a name="b37377048161524"></a>master-only</strong>: Only the master policy file [default] can be used.</p>
<p id="p7130141215215"><a name="p7130141215215"></a><a name="p7130141215215"></a><strong id="b1313015121124"><a name="b1313015121124"></a><a name="b1313015121124"></a>by-content-type</strong>: Only <strong id="b73646391122"><a name="b73646391122"></a><a name="b73646391122"></a>loadPolicyFile</strong> can be used to load the file whose <strong id="b1102133912818"><a name="b1102133912818"></a><a name="b1102133912818"></a>Content-Type</strong> is <strong id="b1493914534810"><a name="b1493914534810"></a><a name="b1493914534810"></a>text/x-cross-domain-policy</strong> over HTTP/HTTPS as the cross-domainpolicy file.</p>
<p id="p129071016185519"><a name="p129071016185519"></a><a name="p129071016185519"></a><strong id="b1587731216912"><a name="b1587731216912"></a><a name="b1587731216912"></a>by-ftp-filename</strong>: Only <strong id="b16665123615111"><a name="b16665123615111"></a><a name="b16665123615111"></a>loadPolicyFile</strong> can be used to load file <strong id="b5866144515115"><a name="b5866144515115"></a><a name="b5866144515115"></a>crossdomain.xml</strong> over FTP as the cross-domain policy file.</p>
<p id="p58274322566"><a name="p58274322566"></a><a name="p58274322566"></a><strong id="b783410501392"><a name="b783410501392"></a><a name="b783410501392"></a>all</strong>: <strong id="b148722045131211"><a name="b148722045131211"></a><a name="b148722045131211"></a>loadPolicyFile</strong> can be used to load any file of the target domain as the cross-domain policy file.</p>
</td>
</tr>
<tr id="row1777273416493"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1677263404913"><a name="p1677263404913"></a><a name="p1677263404913"></a><strong id="b119755515506"><a name="b119755515506"></a><a name="b119755515506"></a>allow-access-from</strong></p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p31020503161450"><a name="p31020503161450"></a><a name="p31020503161450"></a>Checks the attribute value and determines the source domain of the flash file that can access content of the domain.</p>
<p id="p10749076161450"><a name="p10749076161450"></a><a name="p10749076161450"></a>The attribute value can be:</p>
<p id="p29632828161450"><a name="p29632828161450"></a><a name="p29632828161450"></a><strong id="b17372877161625"><a name="b17372877161625"></a><a name="b17372877161625"></a>domain</strong>: This attribute specifies an IP address, a domain, and a wildcard domain (any domain). Only domains specified in <strong id="b7115914135719"><a name="b7115914135719"></a><a name="b7115914135719"></a>domain</strong> have the permission to access content of the domain using the flash file.</p>
<p id="p65368862161450"><a name="p65368862161450"></a><a name="p65368862161450"></a><strong id="b27480397161628"><a name="b27480397161628"></a><a name="b27480397161628"></a>to-ports</strong>: Socket connection ports that can access content of the domain.</p>
<p id="p51448853161450"><a name="p51448853161450"></a><a name="p51448853161450"></a><strong id="b36865975161631"><a name="b36865975161631"></a><a name="b36865975161631"></a>secure</strong>: Specifies whether information is transmitted through encryption.</p>
</td>
</tr>
<tr id="row14772434204918"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p3772193412499"><a name="p3772193412499"></a><a name="p3772193412499"></a><strong id="b9991455195010"><a name="b9991455195010"></a><a name="b9991455195010"></a>allow-access-from-identity</strong></p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p66168651161450"><a name="p66168651161450"></a><a name="p66168651161450"></a>Allows cross-domain sources with certain certificates to access resources in this domain.</p>
</td>
</tr>
<tr id="row9772133416497"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1772734204920"><a name="p1772734204920"></a><a name="p1772734204920"></a><strong id="b12100165517506"><a name="b12100165517506"></a><a name="b12100165517506"></a>allow-http-request-headers-from</strong></p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p25106258161450"><a name="p25106258161450"></a><a name="p25106258161450"></a>Grants permission to a third-party domain to sent data to the domain in <strong id="b18527132614248"><a name="b18527132614248"></a><a name="b18527132614248"></a>http</strong> header format.</p>
<p id="p24629731161450"><a name="p24629731161450"></a><a name="p24629731161450"></a>The attribute value can be:</p>
<p id="p20340992161450"><a name="p20340992161450"></a><a name="p20340992161450"></a><strong id="b12927463161636"><a name="b12927463161636"></a><a name="b12927463161636"></a>domain</strong>: This attribute specifies an IP address, a domain, and a wildcard domain (any domain). Only domains specified in <strong id="b12243122011575"><a name="b12243122011575"></a><a name="b12243122011575"></a>domain</strong> have the permission to access content of the domain using the flash file.</p>
<p id="p14678175610277"><a name="p14678175610277"></a><a name="p14678175610277"></a><strong id="b106787563271"><a name="b106787563271"></a><a name="b106787563271"></a>headers</strong>: Specifies a list of http headers separated by commas. Wildcard (*) can be used to indicate the http header.</p>
<p id="p48851200161450"><a name="p48851200161450"></a><a name="p48851200161450"></a><strong id="b721211317288"><a name="b721211317288"></a><a name="b721211317288"></a>secure</strong>: Specifies whether information is transmitted through encryption.</p>
</td>
</tr>
</tbody>
</table>

