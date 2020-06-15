# Global-level Key Operations on DNS<a name="en-us_topic_0100629908"></a>

Domain Name Service \(DNS\) provides highly available and scalable authoritative DNS services and domain name management services. It translates domain names or application resources into IP addresses required for network connection. By doing so, visitors' access requests are directed to the desired resources.

With CTS, you can record operations associated with DNS for future query, audit, and backtrack operations.

**Table  1**  DNS operations that can be recorded by CTS \(global level\)

<a name="table3646706020219"></a>
<table><thead align="left"><tr id="r9359867e1ea8438b9189f1ba04951e4b"><th class="cellrowborder" valign="top" width="35.23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0109830566_p892144117015"><a name="en-us_topic_0109830566_p892144117015"></a><a name="en-us_topic_0109830566_p892144117015"></a><strong id="b204181126163314"><a name="b204181126163314"></a><a name="b204181126163314"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.97%" id="mcps1.2.4.1.2"><p id="a40fc0cc6883649abb277e96ea9a769ea"><a name="a40fc0cc6883649abb277e96ea9a769ea"></a><a name="a40fc0cc6883649abb277e96ea9a769ea"></a><strong id="b2918133018330"><a name="b2918133018330"></a><a name="b2918133018330"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.3"><p id="en-us_topic_0109830566_p11946413018"><a name="en-us_topic_0109830566_p11946413018"></a><a name="en-us_topic_0109830566_p11946413018"></a><strong id="b105751634133319"><a name="b105751634133319"></a><a name="b105751634133319"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r5e3ed143cb754fa384829b3f62e36be7"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p9102741704"><a name="en-us_topic_0109830566_p9102741704"></a><a name="en-us_topic_0109830566_p9102741704"></a>Creating a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p161029416011"><a name="en-us_topic_0109830566_p161029416011"></a><a name="en-us_topic_0109830566_p161029416011"></a>publicRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p210274111018"><a name="en-us_topic_0109830566_p210274111018"></a><a name="en-us_topic_0109830566_p210274111018"></a>createPublicRecordSet</p>
</td>
</tr>
<tr id="re3e135da141b4d37aa3d09499e1ce814"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p710218418018"><a name="en-us_topic_0109830566_p710218418018"></a><a name="en-us_topic_0109830566_p710218418018"></a>Deleting a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="a0773501b6e814ec09cba20ccd4d793cb"><a name="a0773501b6e814ec09cba20ccd4d793cb"></a><a name="a0773501b6e814ec09cba20ccd4d793cb"></a>publicRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p81034418014"><a name="en-us_topic_0109830566_p81034418014"></a><a name="en-us_topic_0109830566_p81034418014"></a>deletePublicRecordSet</p>
</td>
</tr>
<tr id="r4269ffaa86574c89909203e740bd4b3a"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="a2a7e3ffb8eeb42d88f0bbfa5490720ef"><a name="a2a7e3ffb8eeb42d88f0bbfa5490720ef"></a><a name="a2a7e3ffb8eeb42d88f0bbfa5490720ef"></a>Modifying a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p11038414014"><a name="en-us_topic_0109830566_p11038414014"></a><a name="en-us_topic_0109830566_p11038414014"></a>publicRecordSet</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="ae09af46a66b04022ab7229998339c6ab"><a name="ae09af46a66b04022ab7229998339c6ab"></a><a name="ae09af46a66b04022ab7229998339c6ab"></a>updatePublicRecordSet</p>
</td>
</tr>
<tr id="r7d3f76849b4746b89550ef5c90e2761b"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p12104541301"><a name="en-us_topic_0109830566_p12104541301"></a><a name="en-us_topic_0109830566_p12104541301"></a>Creating a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p110474116014"><a name="en-us_topic_0109830566_p110474116014"></a><a name="en-us_topic_0109830566_p110474116014"></a>publicZone</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p71073411306"><a name="en-us_topic_0109830566_p71073411306"></a><a name="en-us_topic_0109830566_p71073411306"></a>createPublicZone</p>
</td>
</tr>
<tr id="r3b825161d9e84c44bf3b0cef78c77003"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p151073411406"><a name="en-us_topic_0109830566_p151073411406"></a><a name="en-us_topic_0109830566_p151073411406"></a>Modifying a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="aa0ccd886ceaf453abe04e378a2cf88b4"><a name="aa0ccd886ceaf453abe04e378a2cf88b4"></a><a name="aa0ccd886ceaf453abe04e378a2cf88b4"></a>publicZone</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p151071141605"><a name="en-us_topic_0109830566_p151071141605"></a><a name="en-us_topic_0109830566_p151071141605"></a>updatePublicZone</p>
</td>
</tr>
<tr id="r7c9d4fab123048a99adc1e52bc12b087"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="aff4786fe44ab407a9e87ae3434914316"><a name="aff4786fe44ab407a9e87ae3434914316"></a><a name="aff4786fe44ab407a9e87ae3434914316"></a>Deleting a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p151124417013"><a name="en-us_topic_0109830566_p151124417013"></a><a name="en-us_topic_0109830566_p151124417013"></a>publicZone</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="ad390aa1635c646f8a483652f8a9cdad0"><a name="ad390aa1635c646f8a483652f8a9cdad0"></a><a name="ad390aa1635c646f8a483652f8a9cdad0"></a>deletePublicZone</p>
</td>
</tr>
<tr id="r2d392fec90164e1f879c7184b5f34046"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p131139415016"><a name="en-us_topic_0109830566_p131139415016"></a><a name="en-us_topic_0109830566_p131139415016"></a>Adding tags to a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p91130412018"><a name="en-us_topic_0109830566_p91130412018"></a><a name="en-us_topic_0109830566_p91130412018"></a>publicZoneTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p311314413019"><a name="en-us_topic_0109830566_p311314413019"></a><a name="en-us_topic_0109830566_p311314413019"></a>createPublicZoneTag</p>
</td>
</tr>
<tr id="rd58ee437bd62496687952c913745535a"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p171134411203"><a name="en-us_topic_0109830566_p171134411203"></a><a name="en-us_topic_0109830566_p171134411203"></a>Deleting tags of a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="ab12ed043d59e49fb9a356fcf4f7632fa"><a name="ab12ed043d59e49fb9a356fcf4f7632fa"></a><a name="ab12ed043d59e49fb9a356fcf4f7632fa"></a>publicZoneTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p91139418015"><a name="en-us_topic_0109830566_p91139418015"></a><a name="en-us_topic_0109830566_p91139418015"></a>deletePublicZoneTag</p>
</td>
</tr>
<tr id="rdc145bc821004a48bef133382d83a6d7"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="ac77a80ddabcf456ba44fff655a67e165"><a name="ac77a80ddabcf456ba44fff655a67e165"></a><a name="ac77a80ddabcf456ba44fff655a67e165"></a>Adding tags to a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p411410415020"><a name="en-us_topic_0109830566_p411410415020"></a><a name="en-us_topic_0109830566_p411410415020"></a>publicRecordSetTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p181141841603"><a name="en-us_topic_0109830566_p181141841603"></a><a name="en-us_topic_0109830566_p181141841603"></a>createPublicRecordSetTag</p>
</td>
</tr>
<tr id="r4acd7ff1e00c42a5abaf3a6d89164012"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p011517411008"><a name="en-us_topic_0109830566_p011517411008"></a><a name="en-us_topic_0109830566_p011517411008"></a>Deleting tags of a record set in a public zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p911554113010"><a name="en-us_topic_0109830566_p911554113010"></a><a name="en-us_topic_0109830566_p911554113010"></a>publicRecordSetTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p41150411102"><a name="en-us_topic_0109830566_p41150411102"></a><a name="en-us_topic_0109830566_p41150411102"></a>deletePublicRecordSetTag</p>
</td>
</tr>
<tr id="rf5be7fba78e4411dabda6bf496cf9531"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="a605db9cc85254059a64d5128cbe95ed7"><a name="a605db9cc85254059a64d5128cbe95ed7"></a><a name="a605db9cc85254059a64d5128cbe95ed7"></a>Adding tags to a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="a48bc2b6c3af948cd8d49f225c7b3a79a"><a name="a48bc2b6c3af948cd8d49f225c7b3a79a"></a><a name="a48bc2b6c3af948cd8d49f225c7b3a79a"></a>privateZoneTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="acc0f0e4f7d144c5dbff23f6f69cba50c"><a name="acc0f0e4f7d144c5dbff23f6f69cba50c"></a><a name="acc0f0e4f7d144c5dbff23f6f69cba50c"></a>createPrivateZoneTag</p>
</td>
</tr>
<tr id="rb23fcc713f0f4c5c95c6d8a4d394568a"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p411844115011"><a name="en-us_topic_0109830566_p411844115011"></a><a name="en-us_topic_0109830566_p411844115011"></a>Deleting tags of a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p6118241303"><a name="en-us_topic_0109830566_p6118241303"></a><a name="en-us_topic_0109830566_p6118241303"></a>privateZoneTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p191182411503"><a name="en-us_topic_0109830566_p191182411503"></a><a name="en-us_topic_0109830566_p191182411503"></a>deletePrivateZoneTag</p>
</td>
</tr>
<tr id="rc597325b93154d61a0c5dd5ec4bc760a"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p111913416010"><a name="en-us_topic_0109830566_p111913416010"></a><a name="en-us_topic_0109830566_p111913416010"></a>Adding tags to a record set in a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p911919414013"><a name="en-us_topic_0109830566_p911919414013"></a><a name="en-us_topic_0109830566_p911919414013"></a>privateRecordSetTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p21192415010"><a name="en-us_topic_0109830566_p21192415010"></a><a name="en-us_topic_0109830566_p21192415010"></a>createPrivateRecordSetTag</p>
</td>
</tr>
<tr id="rf2812b1dc10e4b31bfdede117d6da0ae"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p512124111013"><a name="en-us_topic_0109830566_p512124111013"></a><a name="en-us_topic_0109830566_p512124111013"></a>Deleting tags of a record set in a private zone</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p181211741400"><a name="en-us_topic_0109830566_p181211741400"></a><a name="en-us_topic_0109830566_p181211741400"></a>privateRecordSetTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="aa07d82f33ab040349403ab221d12163c"><a name="aa07d82f33ab040349403ab221d12163c"></a><a name="aa07d82f33ab040349403ab221d12163c"></a>deletePrivateRecordSetTag</p>
</td>
</tr>
<tr id="r9ee93b584cc0471d9f76d97ada867137"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0109830566_p171211641306"><a name="en-us_topic_0109830566_p171211641306"></a><a name="en-us_topic_0109830566_p171211641306"></a>Adding tags to a PTR record</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p181211941801"><a name="en-us_topic_0109830566_p181211941801"></a><a name="en-us_topic_0109830566_p181211941801"></a>ptrRecordTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p51234411303"><a name="en-us_topic_0109830566_p51234411303"></a><a name="en-us_topic_0109830566_p51234411303"></a>createPTRRecordSetTag</p>
</td>
</tr>
<tr id="r16ed4f31d2b9476ebbf97dec6d24f99e"><td class="cellrowborder" valign="top" width="35.23%" headers="mcps1.2.4.1.1 "><p id="a35ea2944198a46de9acec1bc8e1d909f"><a name="a35ea2944198a46de9acec1bc8e1d909f"></a><a name="a35ea2944198a46de9acec1bc8e1d909f"></a>Deleting tags of a PTR record</p>
</td>
<td class="cellrowborder" valign="top" width="24.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0109830566_p81238411402"><a name="en-us_topic_0109830566_p81238411402"></a><a name="en-us_topic_0109830566_p81238411402"></a>ptrRecordTag</p>
</td>
<td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0109830566_p41232411502"><a name="en-us_topic_0109830566_p41232411502"></a><a name="en-us_topic_0109830566_p41232411502"></a>deletePTRRecordTag</p>
</td>
</tr>
</tbody>
</table>

