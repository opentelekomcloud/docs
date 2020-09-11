# Error Codes<a name="EN-US_TOPIC_0071888297"></a>

An example response error is returned as follows:

```
{
  "error_code": xxxx,//Error code
  "error_msg": xxxxx//Error description
}
```

[Table 1](#table112011569382)  describes the error codes.

**Table  1**  Error code description

<a name="table112011569382"></a>
<table><thead align="left"><tr id="row17202956193813"><th class="cellrowborder" valign="top" width="16.69666066786643%" id="mcps1.2.7.1.1"><p id="p220215615386"><a name="p220215615386"></a><a name="p220215615386"></a>Module</p>
</th>
<th class="cellrowborder" valign="top" width="16.636672665466907%" id="mcps1.2.7.1.2"><p id="p152021156113817"><a name="p152021156113817"></a><a name="p152021156113817"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="16.936612677464506%" id="mcps1.2.7.1.3"><p id="p9202115613813"><a name="p9202115613813"></a><a name="p9202115613813"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="16.326734653069387%" id="mcps1.2.7.1.4"><p id="p15202145614389"><a name="p15202145614389"></a><a name="p15202145614389"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16.736652669466107%" id="mcps1.2.7.1.5"><p id="p132021156133816"><a name="p132021156133816"></a><a name="p132021156133816"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="16.666666666666664%" id="mcps1.2.7.1.6"><p id="p14202556203817"><a name="p14202556203817"></a><a name="p14202556203817"></a>Measure</p>
</th>
</tr>
</thead>
<tbody><tr id="row1220295612382"><td class="cellrowborder" rowspan="17" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 "><p id="p199261136277"><a name="p199261136277"></a><a name="p199261136277"></a>Shared</p>
</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p592610360713"><a name="p592610360713"></a><a name="p592610360713"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p292615361378"><a name="p292615361378"></a><a name="p292615361378"></a>CSBS.0001</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p119264369717"><a name="p119264369717"></a><a name="p119264369717"></a>The number of backup policies has reached the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p189261369719"><a name="p189261369719"></a><a name="p189261369719"></a>Service over limit</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p1592773613715"><a name="p1592773613715"></a><a name="p1592773613715"></a>Delete an existing backup policy and try again.</p>
</td>
</tr>
<tr id="row8202185693820"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p292793618715"><a name="p292793618715"></a><a name="p292793618715"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p18927736477"><a name="p18927736477"></a><a name="p18927736477"></a>CSBS.6000</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p7927113619712"><a name="p7927113619712"></a><a name="p7927113619712"></a>The server does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p199271636472"><a name="p199271636472"></a><a name="p199271636472"></a>server do not exist</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p4927163619710"><a name="p4927163619710"></a><a name="p4927163619710"></a>Check whether the server exists.</p>
</td>
</tr>
<tr id="row4202456113818"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1892717361876"><a name="p1892717361876"></a><a name="p1892717361876"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p592712367713"><a name="p592712367713"></a><a name="p592712367713"></a>CSBS.6001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p109275361677"><a name="p109275361677"></a><a name="p109275361677"></a>The server has stopped.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p13927136872"><a name="p13927136872"></a><a name="p13927136872"></a>The server has stopped.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1292718361274"><a name="p1292718361274"></a><a name="p1292718361274"></a>Check whether the server has stopped.</p>
</td>
</tr>
<tr id="row1920213564382"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1092814361670"><a name="p1092814361670"></a><a name="p1092814361670"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p7928123612719"><a name="p7928123612719"></a><a name="p7928123612719"></a>CSBS.6003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p192833614717"><a name="p192833614717"></a><a name="p192833614717"></a>Currently, only cloud server backup is supported.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p10928183614718"><a name="p10928183614718"></a><a name="p10928183614718"></a>Resource (%s) type (%s) is not support protection.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p9928153619713"><a name="p9928153619713"></a><a name="p9928153619713"></a>Select servers and add them to the backup policy.</p>
</td>
</tr>
<tr id="row62023560381"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1928936976"><a name="p1928936976"></a><a name="p1928936976"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p492814367710"><a name="p492814367710"></a><a name="p492814367710"></a>CSBS.6005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p3928193612717"><a name="p3928193612717"></a><a name="p3928193612717"></a>The current server status does not allow backup.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p16928143617717"><a name="p16928143617717"></a><a name="p16928143617717"></a>Server (%s) is already in service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p492810361178"><a name="p492810361178"></a><a name="p492810361178"></a>Ensure that the server status allows restoration and try again.</p>
</td>
</tr>
<tr id="row18202155613386"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p209281361374"><a name="p209281361374"></a><a name="p209281361374"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p89287361274"><a name="p89287361274"></a><a name="p89287361274"></a>CSBS.6006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p129281736774"><a name="p129281736774"></a><a name="p129281736774"></a>This type of server does not support backup.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p199284368719"><a name="p199284368719"></a><a name="p199284368719"></a>Server (%s) status (%s) is not allowed to protect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p109286367719"><a name="p109286367719"></a><a name="p109286367719"></a>Select servers of a correct type.</p>
</td>
</tr>
<tr id="row620313566388"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1892811361674"><a name="p1892811361674"></a><a name="p1892811361674"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1892819361779"><a name="p1892819361779"></a><a name="p1892819361779"></a>CSBS.6007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p9928436171"><a name="p9928436171"></a><a name="p9928436171"></a>Servers without EVS disks do not support backup.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p892873610714"><a name="p892873610714"></a><a name="p892873610714"></a>No volume attached to the server (%s) for protect.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p11928113616714"><a name="p11928113616714"></a><a name="p11928113616714"></a>Check whether an EVS disk is attached to the server.</p>
</td>
</tr>
<tr id="row570173710433"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p149281636877"><a name="p149281636877"></a><a name="p149281636877"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p89280361377"><a name="p89280361377"></a><a name="p89280361377"></a>CSBS.6010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1692883615719"><a name="p1692883615719"></a><a name="p1692883615719"></a>The server does not support backup, because it hosts shared EVS disks.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1892813361478"><a name="p1892813361478"></a><a name="p1892813361478"></a>Volume (%s) attached to server (%s) is shareable volume.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1492816363714"><a name="p1492816363714"></a><a name="p1492816363714"></a>Remove the shared disk and perform the backup again.</p>
</td>
</tr>
<tr id="row219215404436"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p9928136876"><a name="p9928136876"></a><a name="p9928136876"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p5928336175"><a name="p5928336175"></a><a name="p5928336175"></a>CSBS.6013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p15928936078"><a name="p15928936078"></a><a name="p15928936078"></a>Only server restoration is supported currently.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p13929153610714"><a name="p13929153610714"></a><a name="p13929153610714"></a>Resource (%s) type (%s) is not support restoration.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p192917361575"><a name="p192917361575"></a><a name="p192917361575"></a>Select servers for restoration.</p>
</td>
</tr>
<tr id="row216420429431"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p7929123617710"><a name="p7929123617710"></a><a name="p7929123617710"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1192912361775"><a name="p1192912361775"></a><a name="p1192912361775"></a>CSBS.6014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1892923616714"><a name="p1892923616714"></a><a name="p1892923616714"></a>The specified EVS disk is not attached to the server to be restored.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p89294361471"><a name="p89294361471"></a><a name="p89294361471"></a>Volume(s) (%s) not found in target server.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1692911361176"><a name="p1692911361176"></a><a name="p1692911361176"></a>Select an EVS disk attached to the server to be restored.</p>
</td>
</tr>
<tr id="row1232924418436"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1892913618717"><a name="p1892913618717"></a><a name="p1892913618717"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p69291836674"><a name="p69291836674"></a><a name="p69291836674"></a>CSBS.6015</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p892915367713"><a name="p892915367713"></a><a name="p892915367713"></a>The server in the current status cannot be restored.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p492919362718"><a name="p492919362718"></a><a name="p492919362718"></a>The server is restoring.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p39291936277"><a name="p39291936277"></a><a name="p39291936277"></a>Ensure that the server status allows restoration and try again.</p>
</td>
</tr>
<tr id="row777943722710"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p192916369718"><a name="p192916369718"></a><a name="p192916369718"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p09291136176"><a name="p09291136176"></a><a name="p09291136176"></a>CSBS.9001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1692916361477"><a name="p1692916361477"></a><a name="p1692916361477"></a>Parameter verification failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p59291736774"><a name="p59291736774"></a><a name="p59291736774"></a>provider invalid</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p092933610715"><a name="p092933610715"></a><a name="p092933610715"></a>Enter the correct parameter.</p>
</td>
</tr>
<tr id="row16314104612437"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p592933612714"><a name="p592933612714"></a><a name="p592933612714"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p59291136675"><a name="p59291136675"></a><a name="p59291136675"></a>CSBS.9009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p29293361977"><a name="p29293361977"></a><a name="p29293361977"></a>The user is not authenticated by real name. Authenticate the user's real name and try again.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p59291236473"><a name="p59291236473"></a><a name="p59291236473"></a>User is unverified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p209291336676"><a name="p209291336676"></a><a name="p209291336676"></a>Authenticate the user's real name and try again.</p>
</td>
</tr>
<tr id="row8549648104311"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p18929123614716"><a name="p18929123614716"></a><a name="p18929123614716"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p209299361878"><a name="p209299361878"></a><a name="p209299361878"></a>CSBS.9009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p2929143618711"><a name="p2929143618711"></a><a name="p2929143618711"></a>The backup or replication space after applying for reduction is less than the used space.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p89297365720"><a name="p89297365720"></a><a name="p89297365720"></a>The backup or replication space after reduction cannot be less than the used space.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1093010368711"><a name="p1093010368711"></a><a name="p1093010368711"></a>Ensure that the remaining space is greater than the used space.</p>
</td>
</tr>
<tr id="row7926185019437"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p193018361379"><a name="p193018361379"></a><a name="p193018361379"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p16930133620713"><a name="p16930133620713"></a><a name="p16930133620713"></a>CSBS.9998</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p10930103610720"><a name="p10930103610720"></a><a name="p10930103610720"></a>Service unavailable</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p0930153615716"><a name="p0930153615716"></a><a name="p0930153615716"></a>System not support</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1593017365716"><a name="p1593017365716"></a><a name="p1593017365716"></a>Try later or contact technical support.</p>
</td>
</tr>
<tr id="row4108195418432"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p393010367719"><a name="p393010367719"></a><a name="p393010367719"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p493012361779"><a name="p493012361779"></a><a name="p493012361779"></a>CSBS.9999</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p69303361711"><a name="p69303361711"></a><a name="p69303361711"></a>System internal error</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p149301536975"><a name="p149301536975"></a><a name="p149301536975"></a>%s failed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p5930153612711"><a name="p5930153612711"></a><a name="p5930153612711"></a>Try later or contact technical support.</p>
</td>
</tr>
<tr id="row739375717436"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p79305361719"><a name="p79305361719"></a><a name="p79305361719"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p59306367718"><a name="p59306367718"></a><a name="p59306367718"></a>CSBS.0002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1293013361278"><a name="p1293013361278"></a><a name="p1293013361278"></a>The volumes of the server have different storage types. (Not used currently.)</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p119308363711"><a name="p119308363711"></a><a name="p119308363711"></a>Volume of services from different storagetype</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p18930133610712"><a name="p18930133610712"></a><a name="p18930133610712"></a>Use the same type of volumes.</p>
</td>
</tr>
<tr id="row6837163364417"><td class="cellrowborder" rowspan="4" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 "><p id="p193017361378"><a name="p193017361378"></a><a name="p193017361378"></a>Backup management</p>
<p id="p413732542014"><a name="p413732542014"></a><a name="p413732542014"></a></p>
<p id="p91371225192016"><a name="p91371225192016"></a><a name="p91371225192016"></a></p>
<p id="p101371325102018"><a name="p101371325102018"></a><a name="p101371325102018"></a></p>
</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p193073619711"><a name="p193073619711"></a><a name="p193073619711"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p3930103613714"><a name="p3930103613714"></a><a name="p3930103613714"></a>CSBS.1001</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p1093015361777"><a name="p1093015361777"></a><a name="p1093015361777"></a>The backup task cannot be executed, because a manual backup task is being executed.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p0930436071"><a name="p0930436071"></a><a name="p0930436071"></a>The policy is executing backup.</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p129304361675"><a name="p129304361675"></a><a name="p129304361675"></a>Re-execute the backup task after the manual backup task is complete.</p>
</td>
</tr>
<tr id="row490123612443"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p19311636274"><a name="p19311636274"></a><a name="p19311636274"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1693111361477"><a name="p1693111361477"></a><a name="p1693111361477"></a>CSBS.2003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1893115361075"><a name="p1893115361075"></a><a name="p1893115361075"></a>The selected backup is in the <strong id="b587872119611"><a name="b587872119611"></a><a name="b587872119611"></a>Backing up</strong>, <strong id="b1687816211612"><a name="b1687816211612"></a><a name="b1687816211612"></a>Restoring</strong>, or <strong id="b15878221361"><a name="b15878221361"></a><a name="b15878221361"></a>Deleting</strong> state.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p11931736274"><a name="p11931736274"></a><a name="p11931736274"></a>item in executing</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1493123617714"><a name="p1493123617714"></a><a name="p1493123617714"></a>Try again after the task is complete.</p>
</td>
</tr>
<tr id="row1486438144411"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p11931836476"><a name="p11931836476"></a><a name="p11931836476"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p593113361776"><a name="p593113361776"></a><a name="p593113361776"></a>CSBS.2004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p093111362079"><a name="p093111362079"></a><a name="p093111362079"></a>The policy is being executed for backup. Try again after the backup is complete.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p169312364713"><a name="p169312364713"></a><a name="p169312364713"></a>item in plan executing</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p2093115366718"><a name="p2093115366718"></a><a name="p2093115366718"></a>Try again after the task is complete.</p>
</td>
</tr>
<tr id="row1811794110449"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p99314361179"><a name="p99314361179"></a><a name="p99314361179"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1093120361578"><a name="p1093120361578"></a><a name="p1093120361578"></a>CSBS.3001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p193119361176"><a name="p193119361176"></a><a name="p193119361176"></a>The backup does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p19931153610717"><a name="p19931153610717"></a><a name="p19931153610717"></a>Checkpoint_item (%s) is not found.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p18931936877"><a name="p18931936877"></a><a name="p18931936877"></a>Check whether the backup exists.</p>
</td>
</tr>
<tr id="row9670124534410"><td class="cellrowborder" rowspan="5" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p139311365718"><a name="p139311365718"></a><a name="p139311365718"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p14931236876"><a name="p14931236876"></a><a name="p14931236876"></a>CSBS.6027</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p119311036579"><a name="p119311036579"></a><a name="p119311036579"></a>The AZ to which the ECS belongs does not support backup.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p993112362078"><a name="p993112362078"></a><a name="p993112362078"></a>The AZ where the resource (%s) is located does not support backup.</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p39311036672"><a name="p39311036672"></a><a name="p39311036672"></a>Contact the administrator to reconfigure the AZ.</p>
</td>
</tr>
<tr id="row1570620354612"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p39316361772"><a name="p39316361772"></a><a name="p39316361772"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p19311368711"><a name="p19311368711"></a><a name="p19311368711"></a>CSBS.6030</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1393112364715"><a name="p1393112364715"></a><a name="p1393112364715"></a>The backup task cannot be executed, because an automatic backup task is being executed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1493193610713"><a name="p1493193610713"></a><a name="p1493193610713"></a>auto plan executing</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1393118361974"><a name="p1393118361974"></a><a name="p1393118361974"></a>Re-execute the backup task after the automatic backup task is complete.</p>
</td>
</tr>
<tr id="row14137151044614"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p18931133612710"><a name="p18931133612710"></a><a name="p18931133612710"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p89315364713"><a name="p89315364713"></a><a name="p89315364713"></a>CSBS.6031</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p4931936773"><a name="p4931936773"></a><a name="p4931936773"></a>The replication task cannot be executed, because a manual replication task is being executed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p39316361873"><a name="p39316361873"></a><a name="p39316361873"></a>manual copy executing</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1293215369719"><a name="p1293215369719"></a><a name="p1293215369719"></a>Re-execute the replication task after the manual replication task is complete.</p>
</td>
</tr>
<tr id="row17767151374611"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p4932736679"><a name="p4932736679"></a><a name="p4932736679"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p179323368716"><a name="p179323368716"></a><a name="p179323368716"></a>CSBS.6032</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p193211361479"><a name="p193211361479"></a><a name="p193211361479"></a>There are no servers that can be backed up in the backup policy.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p9932836175"><a name="p9932836175"></a><a name="p9932836175"></a>plan has no resource backup</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p10932103611720"><a name="p10932103611720"></a><a name="p10932103611720"></a>Bind the policy to servers or wait until the bound server is restored to a state that supports backup.</p>
</td>
</tr>
<tr id="row1133172467"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p793212362078"><a name="p793212362078"></a><a name="p793212362078"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p13932133619713"><a name="p13932133619713"></a><a name="p13932133619713"></a>CSBS.6033</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p39327362711"><a name="p39327362711"></a><a name="p39327362711"></a>A server with DSS disks cannot be backed up.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p0932636378"><a name="p0932636378"></a><a name="p0932636378"></a>Service type of volume %s(belong to server %s) is dss.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1793253617712"><a name="p1793253617712"></a><a name="p1793253617712"></a>Check whether a dedicated storage disk has been attached to the server.</p>
</td>
</tr>
<tr id="row127522164616"><td class="cellrowborder" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p993311361974"><a name="p993311361974"></a><a name="p993311361974"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p139331736376"><a name="p139331736376"></a><a name="p139331736376"></a>CSBS.6061</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p159331236477"><a name="p159331236477"></a><a name="p159331236477"></a>The current server does not support backup or restoration.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p89338361179"><a name="p89338361179"></a><a name="p89338361179"></a>volume of server in this pod does not support backup</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p293343614715"><a name="p293343614715"></a><a name="p293343614715"></a>Deselect the disks that do not support backup and retry.</p>
</td>
</tr>
<tr id="row087452620468"><td class="cellrowborder" rowspan="2" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p169331336773"><a name="p169331336773"></a><a name="p169331336773"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p199330360713"><a name="p199330360713"></a><a name="p199330360713"></a>CSBS.8001</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p59333361179"><a name="p59333361179"></a><a name="p59333361179"></a>Backups in the current status cannot be registered as images.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p189331536274"><a name="p189331536274"></a><a name="p189331536274"></a>The backup status is not allowed to create image</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p19336360719"><a name="p19336360719"></a><a name="p19336360719"></a>Try later or contact technical support.</p>
</td>
</tr>
<tr id="row1037016526464"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p69344360712"><a name="p69344360712"></a><a name="p69344360712"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p159341836472"><a name="p159341836472"></a><a name="p159341836472"></a>CSBS.8007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p179344361172"><a name="p179344361172"></a><a name="p179344361172"></a>An image has been created by using the backup and the backup cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p593493611720"><a name="p593493611720"></a><a name="p593493611720"></a>The backup {checkpoint_item_id} has register to image, can't be delete</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p49344361717"><a name="p49344361717"></a><a name="p49344361717"></a>Delete the created image first and then the backup.</p>
</td>
</tr>
<tr id="row18521454104615"><td class="cellrowborder" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p893414361575"><a name="p893414361575"></a><a name="p893414361575"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p129343362071"><a name="p129343362071"></a><a name="p129343362071"></a>CSBS.8008</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p293416367711"><a name="p293416367711"></a><a name="p293416367711"></a>The current backup status does not support query.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p1993413616715"><a name="p1993413616715"></a><a name="p1993413616715"></a>The backup {checkpoint_item_id}'s status is not allowed query</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p393411361271"><a name="p393411361271"></a><a name="p393411361271"></a>Check whether the backup exists.</p>
</td>
</tr>
<tr id="row56775754618"><td class="cellrowborder" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p149341636371"><a name="p149341636371"></a><a name="p149341636371"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p893513361717"><a name="p893513361717"></a><a name="p893513361717"></a>CSBS.8009</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p139351436977"><a name="p139351436977"></a><a name="p139351436977"></a>The backup does not contain the system disk data and cannot be used to create an image.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p19935173610711"><a name="p19935173610711"></a><a name="p19935173610711"></a>The backup has not system disk backup is not allowed to create image</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p79359363716"><a name="p79359363716"></a><a name="p79359363716"></a>Check whether the backup contains a system disk.</p>
</td>
</tr>
<tr id="row2942532104714"><td class="cellrowborder" rowspan="3" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p1494413610719"><a name="p1494413610719"></a><a name="p1494413610719"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p994413362079"><a name="p994413362079"></a><a name="p994413362079"></a>CSBS.9006</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p39441362715"><a name="p39441362715"></a><a name="p39441362715"></a>Insufficient quota</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p494512361872"><a name="p494512361872"></a><a name="p494512361872"></a>Quota exceeded for resources: %s</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p394510361875"><a name="p394510361875"></a><a name="p394510361875"></a>Contact the administrator to change the quota or delete the backups that are no longer needed.</p>
</td>
</tr>
<tr id="row1532953512476"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p189453361072"><a name="p189453361072"></a><a name="p189453361072"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1694593613716"><a name="p1694593613716"></a><a name="p1694593613716"></a>CSBS.1002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p294516361875"><a name="p294516361875"></a><a name="p294516361875"></a>The selected server is being backed up. (Not used currently.)</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p18945133614711"><a name="p18945133614711"></a><a name="p18945133614711"></a>resource_in_protecting</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p99455366712"><a name="p99455366712"></a><a name="p99455366712"></a>Try again after the backup task is complete.</p>
</td>
</tr>
<tr id="row205141837114718"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p294617361478"><a name="p294617361478"></a><a name="p294617361478"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p194619361273"><a name="p194619361273"></a><a name="p194619361273"></a>CSBS.2001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p119468368715"><a name="p119468368715"></a><a name="p119468368715"></a>A task is being executed by using this backup policy. (Not used currently.)</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p89466363718"><a name="p89466363718"></a><a name="p89466363718"></a>item in plan is executing</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p994603611719"><a name="p994603611719"></a><a name="p994603611719"></a>Try again after the task is complete.</p>
</td>
</tr>
<tr id="row13759193904711"><td class="cellrowborder" rowspan="4" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 "><p id="p29469362716"><a name="p29469362716"></a><a name="p29469362716"></a>Backup policy management</p>
</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p194616361470"><a name="p194616361470"></a><a name="p194616361470"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p1694619361473"><a name="p1694619361473"></a><a name="p1694619361473"></a>CSBS.3000</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p109460361278"><a name="p109460361278"></a><a name="p109460361278"></a>The backup policy does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p694615361472"><a name="p694615361472"></a><a name="p694615361472"></a>plan not found</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p1946143619719"><a name="p1946143619719"></a><a name="p1946143619719"></a>Check whether the backup policy exists.</p>
</td>
</tr>
<tr id="row49941141194713"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p2946173613714"><a name="p2946173613714"></a><a name="p2946173613714"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p294673615716"><a name="p294673615716"></a><a name="p294673615716"></a>CSBS.5001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1494623610715"><a name="p1494623610715"></a><a name="p1494623610715"></a>Failed to stop the policy.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p69461361279"><a name="p69461361279"></a><a name="p69461361279"></a>Scheduel operation status can't be set unable</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p19947143610712"><a name="p19947143610712"></a><a name="p19947143610712"></a>Check the backup policy status.</p>
</td>
</tr>
<tr id="row107761147174714"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p119472361710"><a name="p119472361710"></a><a name="p119472361710"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p79471436372"><a name="p79471436372"></a><a name="p79471436372"></a>CSBS.6004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p294713361470"><a name="p294713361470"></a><a name="p294713361470"></a>The server has been bound to a backup policy and cannot be bound again.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p3947203612710"><a name="p3947203612710"></a><a name="p3947203612710"></a>Server (%s) is already in service.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p12947436777"><a name="p12947436777"></a><a name="p12947436777"></a>Check whether the server has been bound to a backup policy.</p>
</td>
</tr>
<tr id="row17394123618501"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p169478360713"><a name="p169478360713"></a><a name="p169478360713"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p49473365720"><a name="p49473365720"></a><a name="p49473365720"></a>CSBS.9007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p13947103618719"><a name="p13947103618719"></a><a name="p13947103618719"></a>The backup policy name already exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1094733611714"><a name="p1094733611714"></a><a name="p1094733611714"></a>duplicate service name</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p14947236773"><a name="p14947236773"></a><a name="p14947236773"></a>Change the name and try again.</p>
</td>
</tr>
<tr id="row14794143835016"><td class="cellrowborder" rowspan="2" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 "><p id="p1794720362710"><a name="p1794720362710"></a><a name="p1794720362710"></a>Tag management</p>
</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p209471336972"><a name="p209471336972"></a><a name="p209471336972"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p59471336374"><a name="p59471336374"></a><a name="p59471336374"></a>CSBS.7000</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p209473361270"><a name="p209473361270"></a><a name="p209473361270"></a>The resource's tags have reached the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p20947183615715"><a name="p20947183615715"></a><a name="p20947183615715"></a>request tags exceed the max allowed count: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p159471236678"><a name="p159471236678"></a><a name="p159471236678"></a>Delete unnecessary tags and try again.</p>
</td>
</tr>
<tr id="row161775413503"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p49471136178"><a name="p49471136178"></a><a name="p49471136178"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p194720365719"><a name="p194720365719"></a><a name="p194720365719"></a>CSBS.7001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1694812361718"><a name="p1694812361718"></a><a name="p1694812361718"></a>The resource tag to be deleted does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p59486364715"><a name="p59486364715"></a><a name="p59486364715"></a>The backup tag does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p9948836073"><a name="p9948836073"></a><a name="p9948836073"></a>Refresh the page to check whether the tag has been deleted.</p>
</td>
</tr>
<tr id="row51060599508"><td class="cellrowborder" rowspan="11" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 "><p id="p1094813610719"><a name="p1094813610719"></a><a name="p1094813610719"></a>Restoration management</p>
</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p12948236773"><a name="p12948236773"></a><a name="p12948236773"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p139480361679"><a name="p139480361679"></a><a name="p139480361679"></a>CSBS.4000</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p1948173618719"><a name="p1948173618719"></a><a name="p1948173618719"></a>The current backup status does not allow restoration.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p79482362713"><a name="p79482362713"></a><a name="p79482362713"></a>checkpoint item not available</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p16948103618712"><a name="p16948103618712"></a><a name="p16948103618712"></a>Try again later or contact technical support.</p>
</td>
</tr>
<tr id="row1194620155118"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p19948113611718"><a name="p19948113611718"></a><a name="p19948113611718"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1694833617712"><a name="p1694833617712"></a><a name="p1694833617712"></a>CSBS.6016</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1694816366711"><a name="p1694816366711"></a><a name="p1694816366711"></a>This type of server does not support restoration.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14948113617715"><a name="p14948113617715"></a><a name="p14948113617715"></a>can not restore server type is not allow</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p794816361079"><a name="p794816361079"></a><a name="p794816361079"></a>Select servers of a correct type.</p>
</td>
</tr>
<tr id="row19491033513"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p189501836574"><a name="p189501836574"></a><a name="p189501836574"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p395011368713"><a name="p395011368713"></a><a name="p395011368713"></a>CSBS.6017</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p169507361578"><a name="p169507361578"></a><a name="p169507361578"></a>The specified backup disk is not in the specified backup.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p89502361479"><a name="p89502361479"></a><a name="p89502361479"></a>Can not find backup(s) (%s) in checkpoint item (%s).</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p159507361271"><a name="p159507361271"></a><a name="p159507361271"></a>Select a backup disk in the specified backup for restoration.</p>
</td>
</tr>
<tr id="row103181714141414"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p995017367711"><a name="p995017367711"></a><a name="p995017367711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p149504361971"><a name="p149504361971"></a><a name="p149504361971"></a>CSBS.6018</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p16950163617716"><a name="p16950163617716"></a><a name="p16950163617716"></a>The system does not support the restoration of some backup disks in the backup.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p139501036478"><a name="p139501036478"></a><a name="p139501036478"></a>Not assign backup(s) (%s) to volume(s), partial restore is not supported."</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p19950836279"><a name="p19950836279"></a><a name="p19950836279"></a>Select all backup disks in the backup for restoration.</p>
</td>
</tr>
<tr id="row51745115115"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1395053613720"><a name="p1395053613720"></a><a name="p1395053613720"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p2095011361878"><a name="p2095011361878"></a><a name="p2095011361878"></a>CSBS.6019</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p49507368711"><a name="p49507368711"></a><a name="p49507368711"></a>The type of the target server is different from that of the source server.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1695013362714"><a name="p1695013362714"></a><a name="p1695013362714"></a>The source server (%s) type (%s) is not the same as the target server (%s) type (%s).</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p29504366710"><a name="p29504366710"></a><a name="p29504366710"></a>Select a target server of the same type as the source server.</p>
</td>
</tr>
<tr id="row11728042155214"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p12950103612715"><a name="p12950103612715"></a><a name="p12950103612715"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p49501436979"><a name="p49501436979"></a><a name="p49501436979"></a>CSBS.6020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p095013361479"><a name="p095013361479"></a><a name="p095013361479"></a>Servers without EVS disks do not support restoration.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1695043610720"><a name="p1695043610720"></a><a name="p1695043610720"></a>No volume attached to the server (%s) for restore.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p995013361576"><a name="p995013361576"></a><a name="p995013361576"></a>Check whether an EVS disk is attached to the server.</p>
</td>
</tr>
<tr id="row18617104415214"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p2950193613719"><a name="p2950193613719"></a><a name="p2950193613719"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1695017364716"><a name="p1695017364716"></a><a name="p1695017364716"></a>CSBS.6021</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p19505365719"><a name="p19505365719"></a><a name="p19505365719"></a>The backup cannot be restored to a shared EVS disk of the server.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p895019361274"><a name="p895019361274"></a><a name="p895019361274"></a>Volume (%s) attached to server (%s) is shareable volume.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1695012361071"><a name="p1695012361071"></a><a name="p1695012361071"></a>Restore the backup to a non-shared EVS disk of the server.</p>
</td>
</tr>
<tr id="row165104715218"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p8950193616719"><a name="p8950193616719"></a><a name="p8950193616719"></a>500</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p29501369717"><a name="p29501369717"></a><a name="p29501369717"></a>CSBS.6023</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p20950183612713"><a name="p20950183612713"></a><a name="p20950183612713"></a>The backup for a data disk cannot be restored to a system disk of the server.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p109501536177"><a name="p109501536177"></a><a name="p109501536177"></a>Can not restore data volume to system volume. server id is (%s).</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p149511836672"><a name="p149511836672"></a><a name="p149511836672"></a>Restore the backup to a data disk of the server.</p>
</td>
</tr>
<tr id="row6447849105212"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p18951183619714"><a name="p18951183619714"></a><a name="p18951183619714"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p9951203617717"><a name="p9951203617717"></a><a name="p9951203617717"></a>CSBS.6024</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p169510361878"><a name="p169510361878"></a><a name="p169510361878"></a>Restoration cannot be executed because the capacity of the specified EVS disk attached to the server is less than that of the backed-up disk.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p15951836875"><a name="p15951836875"></a><a name="p15951836875"></a>Target volume (%s) size (%s) small than volume backup (%s) size (%s).</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p7951143617715"><a name="p7951143617715"></a><a name="p7951143617715"></a>Expand the EVS disk and try again, or restore data of the backup disk to a disk that has a larger capacity.</p>
</td>
</tr>
<tr id="row4368144417321"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1495117361079"><a name="p1495117361079"></a><a name="p1495117361079"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p195117361776"><a name="p195117361776"></a><a name="p195117361776"></a>CSBS.6025</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p5951173613718"><a name="p5951173613718"></a><a name="p5951173613718"></a>Restoration is not supported between the AZ to which the specified backup belongs and the AZ to which the server belongs.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p149517361679"><a name="p149517361679"></a><a name="p149517361679"></a>The AZ of local checkpoint item (%s) is not support to restore the resource (%s).</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p795163618717"><a name="p795163618717"></a><a name="p795163618717"></a>Contact the administrator to reconfigure the AZ.</p>
</td>
</tr>
<tr id="row1199545115214"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p139518364717"><a name="p139518364717"></a><a name="p139518364717"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p3951236475"><a name="p3951236475"></a><a name="p3951236475"></a>CSBS.9008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1195163618720"><a name="p1195163618720"></a><a name="p1195163618720"></a>Only backups in the <strong id="b84235270615638"><a name="b84235270615638"></a><a name="b84235270615638"></a>Available</strong> state can be used to create ECSs.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p16951113612716"><a name="p16951113612716"></a><a name="p16951113612716"></a>Checkpoint Item Status Not Support Create VM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p49515361175"><a name="p49515361175"></a><a name="p49515361175"></a>Check whether the backup is available.</p>
</td>
</tr>
<tr id="row10671810125315"><td class="cellrowborder" valign="top" width="16.69666066786643%" headers="mcps1.2.7.1.1 "><p id="p695118361716"><a name="p695118361716"></a><a name="p695118361716"></a>Task management</p>
</td>
<td class="cellrowborder" valign="top" width="16.636672665466907%" headers="mcps1.2.7.1.2 "><p id="p29516369711"><a name="p29516369711"></a><a name="p29516369711"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.936612677464506%" headers="mcps1.2.7.1.3 "><p id="p79512361977"><a name="p79512361977"></a><a name="p79512361977"></a>CSBS.6040</p>
</td>
<td class="cellrowborder" valign="top" width="16.326734653069387%" headers="mcps1.2.7.1.4 "><p id="p595143615711"><a name="p595143615711"></a><a name="p595143615711"></a>The backup job to be deleted does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="16.736652669466107%" headers="mcps1.2.7.1.5 "><p id="p09511936371"><a name="p09511936371"></a><a name="p09511936371"></a>task not found</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p19515361470"><a name="p19515361470"></a><a name="p19515361470"></a>Check whether the backup job exists.</p>
</td>
</tr>
</tbody>
</table>

Karbor native APIs:

http://developer.openstack.org/api-ref/data-protection-orchestration/v1/index.html

