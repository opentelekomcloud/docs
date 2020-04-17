# Error Codes<a name="evs_04_0038"></a>

<a name="table20837153263014"></a>
<table><thead align="left"><tr id="row483773210306"><th class="cellrowborder" valign="top" width="11.353535353535353%" id="mcps1.1.6.1.1"><p id="p12838123215305"><a name="p12838123215305"></a><a name="p12838123215305"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="16.31313131313131%" id="mcps1.1.6.1.2"><p id="p583873243014"><a name="p583873243014"></a><a name="p583873243014"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="21.29292929292929%" id="mcps1.1.6.1.3"><p id="p1983853215306"><a name="p1983853215306"></a><a name="p1983853215306"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="23.303030303030305%" id="mcps1.1.6.1.4"><p id="p4838032183014"><a name="p4838032183014"></a><a name="p4838032183014"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="27.737373737373737%" id="mcps1.1.6.1.5"><p id="p1283819326308"><a name="p1283819326308"></a><a name="p1283819326308"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="row1783823217302"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p13838732183011"><a name="p13838732183011"></a><a name="p13838732183011"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1683811325304"><a name="p1683811325304"></a><a name="p1683811325304"></a>EVS.0001</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p96421849458"><a name="p96421849458"></a><a name="p96421849458"></a>Incorrect tenant ID in the URI.</p>
<p id="p8838143283011"><a name="p8838143283011"></a><a name="p8838143283011"></a><span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p178385328302"><a name="p178385328302"></a><a name="p178385328302"></a>invalid tenant id!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p283803293016"><a name="p283803293016"></a><a name="p283803293016"></a>Use the correct tenant ID.</p>
</td>
</tr>
<tr id="row683819321300"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p883893213301"><a name="p883893213301"></a><a name="p883893213301"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1783833219302"><a name="p1783833219302"></a><a name="p1783833219302"></a>EVS.0002</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p9838432173011"><a name="p9838432173011"></a><a name="p9838432173011"></a>Header parameters in the HTTP request are incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p283812328304"><a name="p283812328304"></a><a name="p283812328304"></a>invalid token!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p9838153215308"><a name="p9838153215308"></a><a name="p9838153215308"></a>Use the correct token.</p>
</td>
</tr>
<tr id="row1883811322304"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p283823211303"><a name="p283823211303"></a><a name="p283823211303"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p198387321309"><a name="p198387321309"></a><a name="p198387321309"></a>EVS.0003</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p78389327304"><a name="p78389327304"></a><a name="p78389327304"></a>The token used is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1383873263014"><a name="p1383873263014"></a><a name="p1383873263014"></a>invalid token roles!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p28391732133016"><a name="p28391732133016"></a><a name="p28391732133016"></a>The account permission set is empty. Add the required permissions to this account.</p>
</td>
</tr>
<tr id="row4115933194114"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p78551332153010"><a name="p78551332153010"></a><a name="p78551332153010"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p885663218304"><a name="p885663218304"></a><a name="p885663218304"></a>EVS.1001</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p4856143211302"><a name="p4856143211302"></a><a name="p4856143211302"></a>The name and description formats set in the request to update the disk are incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p685623223020"><a name="p685623223020"></a><a name="p685623223020"></a>null volume!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p13856193214304"><a name="p13856193214304"></a><a name="p13856193214304"></a>Enter the disk name and description in the correct format.</p>
</td>
</tr>
<tr id="row1586573465012"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1629940165010"><a name="p1629940165010"></a><a name="p1629940165010"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1629144013503"><a name="p1629144013503"></a><a name="p1629144013503"></a>EVS.1002</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p58661134185012"><a name="p58661134185012"></a><a name="p58661134185012"></a>Incorrect disk ID.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p128561632133011"><a name="p128561632133011"></a><a name="p128561632133011"></a>invalid volume id!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1586633425012"><a name="p1586633425012"></a><a name="p1586633425012"></a>Enter the disk ID in the correct format.</p>
</td>
</tr>
<tr id="row15461426194117"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p38561032133017"><a name="p38561032133017"></a><a name="p38561032133017"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p12856163243013"><a name="p12856163243013"></a><a name="p12856163243013"></a>EVS.1003</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1585603214301"><a name="p1585603214301"></a><a name="p1585603214301"></a>Incorrect disk name format.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p12733185514504"><a name="p12733185514504"></a><a name="p12733185514504"></a>invalid volume name!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p2085614326302"><a name="p2085614326302"></a><a name="p2085614326302"></a>Enter the disk name in the correct format.</p>
</td>
</tr>
<tr id="row7471726144114"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1185653211305"><a name="p1185653211305"></a><a name="p1185653211305"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p5856193219306"><a name="p5856193219306"></a><a name="p5856193219306"></a>EVS.1004</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p6856232143013"><a name="p6856232143013"></a><a name="p6856232143013"></a>Incorrect disk description format.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1856123219308"><a name="p1856123219308"></a><a name="p1856123219308"></a>invalid volume description!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p585612328301"><a name="p585612328301"></a><a name="p585612328301"></a>Enter the disk description in the correct format.</p>
</td>
</tr>
<tr id="row1689511358338"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p11846173213010"><a name="p11846173213010"></a><a name="p11846173213010"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p7846173212307"><a name="p7846173212307"></a><a name="p7846173212307"></a>EVS.1005</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1184613273017"><a name="p1184613273017"></a><a name="p1184613273017"></a>The size of the metadata set in the request to create the disk exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p8846103203013"><a name="p8846103203013"></a><a name="p8846103203013"></a>size of metadata is too large!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p2084683214309"><a name="p2084683214309"></a><a name="p2084683214309"></a>Check whether the metadata is too large. The metadata size must be smaller than 1048576 bytes.</p>
</td>
</tr>
<tr id="row208951035193317"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p884673273019"><a name="p884673273019"></a><a name="p884673273019"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p984663212302"><a name="p984663212302"></a><a name="p984663212302"></a>EVS.1006</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p8846133218307"><a name="p8846133218307"></a><a name="p8846133218307"></a>The ID of the backup used to create the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p15846113219305"><a name="p15846113219305"></a><a name="p15846113219305"></a>invalid backup id!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p184693214303"><a name="p184693214303"></a><a name="p184693214303"></a>Enter the correct backup ID.</p>
</td>
</tr>
<tr id="row1989633516338"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p88461332163015"><a name="p88461332163015"></a><a name="p88461332163015"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p118461132203011"><a name="p118461132203011"></a><a name="p118461132203011"></a>EVS.1007</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p484693210304"><a name="p484693210304"></a><a name="p484693210304"></a>Parameters <strong id="b616291511499"><a name="b616291511499"></a><a name="b616291511499"></a>name</strong> and <strong id="b5546624211499"><a name="b5546624211499"></a><a name="b5546624211499"></a>description</strong> are incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p14847173215303"><a name="p14847173215303"></a><a name="p14847173215303"></a>volume name and description can not both be empty!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p384773216306"><a name="p384773216306"></a><a name="p384773216306"></a>Enter the correct disk name and description.</p>
</td>
</tr>
<tr id="row20918935183318"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p168471532103013"><a name="p168471532103013"></a><a name="p168471532103013"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p118470327309"><a name="p118470327309"></a><a name="p118470327309"></a>EVS.1008</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p12847132153020"><a name="p12847132153020"></a><a name="p12847132153020"></a>The format of the request to create the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p484711322300"><a name="p484711322300"></a><a name="p484711322300"></a>null createVolumeReq!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p684723263020"><a name="p684723263020"></a><a name="p684723263020"></a>Use the correct request format.</p>
</td>
</tr>
<tr id="row89195355333"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p284753216309"><a name="p284753216309"></a><a name="p284753216309"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p7847143217308"><a name="p7847143217308"></a><a name="p7847143217308"></a>EVS.1009</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p148475329300"><a name="p148475329300"></a><a name="p148475329300"></a>The body of the request to create the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p16847163233011"><a name="p16847163233011"></a><a name="p16847163233011"></a>invalid volumeForCreate!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p11847832183014"><a name="p11847832183014"></a><a name="p11847832183014"></a>Check the body of the request used to create the disk.</p>
</td>
</tr>
<tr id="row2919183563319"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p684733253016"><a name="p684733253016"></a><a name="p684733253016"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1584793213013"><a name="p1584793213013"></a><a name="p1584793213013"></a>EVS.1010</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p884793213019"><a name="p884793213019"></a><a name="p884793213019"></a>Parameter <strong id="b683664311499"><a name="b683664311499"></a><a name="b683664311499"></a>size</strong> set in the request to create the disk is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p12847103273016"><a name="p12847103273016"></a><a name="p12847103273016"></a>invalid volume size!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1784811329306"><a name="p1784811329306"></a><a name="p1784811329306"></a>Enter a valid <strong id="b84235270617350"><a name="b84235270617350"></a><a name="b84235270617350"></a>size</strong> value.</p>
</td>
</tr>
<tr id="row29444586352"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1985220329306"><a name="p1985220329306"></a><a name="p1985220329306"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p188521232193011"><a name="p188521232193011"></a><a name="p188521232193011"></a>EVS.1011</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p2852632123012"><a name="p2852632123012"></a><a name="p2852632123012"></a>The format of the request to expand the disk capacity is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p118521832143011"><a name="p118521832143011"></a><a name="p118521832143011"></a>null extendVolumeReq!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p485316321301"><a name="p485316321301"></a><a name="p485316321301"></a>Use the correct request format.</p>
</td>
</tr>
<tr id="row1883914326303"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p5839932133010"><a name="p5839932133010"></a><a name="p5839932133010"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1283918323303"><a name="p1283918323303"></a><a name="p1283918323303"></a>EVS.1012</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p0839193223016"><a name="p0839193223016"></a><a name="p0839193223016"></a>You do not have the permission to access this disk.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p6839173215306"><a name="p6839173215306"></a><a name="p6839173215306"></a>temporary volume!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p983973283013"><a name="p983973283013"></a><a name="p983973283013"></a>Do not perform operations for a temporary disk as it does not allow any operation.</p>
</td>
</tr>
<tr id="row21971935858"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p520524016518"><a name="p520524016518"></a><a name="p520524016518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p2020514406514"><a name="p2020514406514"></a><a name="p2020514406514"></a>EVS.1013</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p82057401652"><a name="p82057401652"></a><a name="p82057401652"></a>Request conversion error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1220520402511"><a name="p1220520402511"></a><a name="p1220520402511"></a>request transforming failed!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1820512405515"><a name="p1820512405515"></a><a name="p1820512405515"></a>Check whether the request body is correct.</p>
</td>
</tr>
<tr id="row13197113514519"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p18205134013517"><a name="p18205134013517"></a><a name="p18205134013517"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1020619405517"><a name="p1020619405517"></a><a name="p1020619405517"></a>EVS.1014</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p220618402056"><a name="p220618402056"></a><a name="p220618402056"></a>Failed to meet the capacity expansion requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p92067403513"><a name="p92067403513"></a><a name="p92067403513"></a>volume can not be extended!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p12206140451"><a name="p12206140451"></a><a name="p12206140451"></a>Ensure that the disk meets the expansion requirements.</p>
</td>
</tr>
<tr id="row134895266395"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p385393215303"><a name="p385393215303"></a><a name="p385393215303"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p19853123273010"><a name="p19853123273010"></a><a name="p19853123273010"></a>EVS.1015</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1785353212309"><a name="p1785353212309"></a><a name="p1785353212309"></a>The new size of the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p78534329305"><a name="p78534329305"></a><a name="p78534329305"></a>new volume Size must be greater than old Size!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p16853143253017"><a name="p16853143253017"></a><a name="p16853143253017"></a>Ensure that the new disk capacity is larger than the original disk capacity.</p>
</td>
</tr>
<tr id="row46361345950"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p62061440855"><a name="p62061440855"></a><a name="p62061440855"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p6206104016515"><a name="p6206104016515"></a><a name="p6206104016515"></a>EVS.1016</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p220612409514"><a name="p220612409514"></a><a name="p220612409514"></a>Only one data source among image, snapshot, and backup can be selected when creating a disk from a data source.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1220616405510"><a name="p1220616405510"></a><a name="p1220616405510"></a>Invalid input received: May specify only one of imageRef, snapshot_id, backup_id!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p102062401554"><a name="p102062401554"></a><a name="p102062401554"></a>Select one data source.</p>
</td>
</tr>
<tr id="row18917131164315"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1385613233013"><a name="p1385613233013"></a><a name="p1385613233013"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p6857432193015"><a name="p6857432193015"></a><a name="p6857432193015"></a>EVS.1018</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p13857203233015"><a name="p13857203233015"></a><a name="p13857203233015"></a>Type conversion error. The parameter type is unexpected.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1285793213300"><a name="p1285793213300"></a><a name="p1285793213300"></a>Type conversion error , parameter type is unexpected</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p14857173233011"><a name="p14857173233011"></a><a name="p14857173233011"></a>Check whether the input parameters are correct. For details about the parameter requirements, see the <em id="i84235269717349"><a name="i84235269717349"></a><a name="i84235269717349"></a>Elastic Volume Service API Reference</em>.</p>
</td>
</tr>
<tr id="row2797115733311"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p78480327300"><a name="p78480327300"></a><a name="p78480327300"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p684813263016"><a name="p684813263016"></a><a name="p684813263016"></a>EVS.1020</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p20848332183011"><a name="p20848332183011"></a><a name="p20848332183011"></a>The disk type set in the request to create the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p3848532193019"><a name="p3848532193019"></a><a name="p3848532193019"></a>invalid volume type!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p188481832203014"><a name="p188481832203014"></a><a name="p188481832203014"></a>Enter a valid disk type.</p>
</td>
</tr>
<tr id="row157981757163310"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p3848232123020"><a name="p3848232123020"></a><a name="p3848232123020"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1184873233017"><a name="p1184873233017"></a><a name="p1184873233017"></a>EVS.1021</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p4848193213015"><a name="p4848193213015"></a><a name="p4848193213015"></a>The disk quantity set in the request to batch create disks is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p14848203263012"><a name="p14848203263012"></a><a name="p14848203263012"></a>the quantity of volume is invalid!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p16848132113015"><a name="p16848132113015"></a><a name="p16848132113015"></a>Enter a valid disk quantity.</p>
</td>
</tr>
<tr id="row1979811574338"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p108481732173019"><a name="p108481732173019"></a><a name="p108481732173019"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p198497322307"><a name="p198497322307"></a><a name="p198497322307"></a>EVS.1022</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p484993243015"><a name="p484993243015"></a><a name="p484993243015"></a>Parameter <strong id="b3533424411499"><a name="b3533424411499"></a><a name="b3533424411499"></a>size</strong> set in the request to create the disk using a backup is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p188492325307"><a name="p188492325307"></a><a name="p188492325307"></a>the size param is less than backup size!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p148498322304"><a name="p148498322304"></a><a name="p148498322304"></a>Ensure that the entered disk size is larger than the backup size.</p>
</td>
</tr>
<tr id="row796719109447"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1885793243011"><a name="p1885793243011"></a><a name="p1885793243011"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1985713327306"><a name="p1985713327306"></a><a name="p1985713327306"></a>EVS.1023</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p5857732153011"><a name="p5857732153011"></a><a name="p5857732153011"></a>Parameter <strong id="b5490150911499"><a name="b5490150911499"></a><a name="b5490150911499"></a>limit</strong> in the URL for querying the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p5858103219303"><a name="p5858103219303"></a><a name="p5858103219303"></a>invalid filter limit!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p14858932123019"><a name="p14858932123019"></a><a name="p14858932123019"></a>Ensure that the <strong id="b162171639183120"><a name="b162171639183120"></a><a name="b162171639183120"></a>limit</strong> value ranges from <strong id="b18473444113113"><a name="b18473444113113"></a><a name="b18473444113113"></a>1</strong> to <strong id="b113761746153110"><a name="b113761746153110"></a><a name="b113761746153110"></a>1000</strong>. The default value is <strong id="b7946748163115"><a name="b7946748163115"></a><a name="b7946748163115"></a>1000</strong>.</p>
</td>
</tr>
<tr id="row139681410104414"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p148588329309"><a name="p148588329309"></a><a name="p148588329309"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p2859732103017"><a name="p2859732103017"></a><a name="p2859732103017"></a>EVS.1024</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1385953223015"><a name="p1385953223015"></a><a name="p1385953223015"></a>Parameter <strong id="b5918630611499"><a name="b5918630611499"></a><a name="b5918630611499"></a>marker</strong> in the URL for querying the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p19859133253020"><a name="p19859133253020"></a><a name="p19859133253020"></a>invalid filter marker!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p88594323301"><a name="p88594323301"></a><a name="p88594323301"></a>Ensure that the <strong id="b1849277043173537"><a name="b1849277043173537"></a><a name="b1849277043173537"></a>marker</strong> value is in the UUID format.</p>
</td>
</tr>
<tr id="row31951817865"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1413014281866"><a name="p1413014281866"></a><a name="p1413014281866"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p16130132814614"><a name="p16130132814614"></a><a name="p16130132814614"></a>EVS.1025</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p813017288613"><a name="p813017288613"></a><a name="p813017288613"></a>Metadata decoding error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p213015281167"><a name="p213015281167"></a><a name="p213015281167"></a>url encoding failed!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p013082811611"><a name="p013082811611"></a><a name="p013082811611"></a>Check whether parameter <strong id="b1789214165101"><a name="b1789214165101"></a><a name="b1789214165101"></a>metadata</strong> is correctly specified.</p>
</td>
</tr>
<tr id="row108391132173010"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p183917328304"><a name="p183917328304"></a><a name="p183917328304"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p11839203211309"><a name="p11839203211309"></a><a name="p11839203211309"></a>EVS.1027</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p19839183219304"><a name="p19839183219304"></a><a name="p19839183219304"></a>You do not have the rights to perform the operation.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p148397327301"><a name="p148397327301"></a><a name="p148397327301"></a>user role is not allowed for this action!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p08391332123013"><a name="p08391332123013"></a><a name="p08391332123013"></a>Check whether the account has relevant permissions, or the account is in arrears, does not pass real-name authentication, or has violations.</p>
</td>
</tr>
<tr id="row748745519618"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1846595815617"><a name="p1846595815617"></a><a name="p1846595815617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1465105819618"><a name="p1465105819618"></a><a name="p1465105819618"></a>EVS.1031</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p346515589617"><a name="p346515589617"></a><a name="p346515589617"></a>Input value of parameter <strong id="b125022452347"><a name="b125022452347"></a><a name="b125022452347"></a>resources status</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p846512583614"><a name="p846512583614"></a><a name="p846512583614"></a>invalid resources status!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p546515581565"><a name="p546515581565"></a><a name="p546515581565"></a>Specify a valid value for <strong id="b102345514221"><a name="b102345514221"></a><a name="b102345514221"></a>resources status</strong>.</p>
</td>
</tr>
<tr id="row14487115514610"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p16466158369"><a name="p16466158369"></a><a name="p16466158369"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p046619581568"><a name="p046619581568"></a><a name="p046619581568"></a>EVS.1032</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1146695815615"><a name="p1146695815615"></a><a name="p1146695815615"></a>Parameter <strong id="b1886315073114"><a name="b1886315073114"></a><a name="b1886315073114"></a>resources id</strong> cannot be left empty.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p446645811614"><a name="p446645811614"></a><a name="p446645811614"></a>invalid resources ID!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p44661358868"><a name="p44661358868"></a><a name="p44661358868"></a>Specify a valid value for <strong id="b1233745210318"><a name="b1233745210318"></a><a name="b1233745210318"></a>resources id</strong>.</p>
</td>
</tr>
<tr id="row3839432163016"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p10839332113018"><a name="p10839332113018"></a><a name="p10839332113018"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p08391532113017"><a name="p08391532113017"></a><a name="p08391532113017"></a>EVS.1033</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p17839732133013"><a name="p17839732133013"></a><a name="p17839732133013"></a>Failed to query the tenant quota.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p68397327306"><a name="p68397327306"></a><a name="p68397327306"></a>query quota failed!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p58391132203015"><a name="p58391132203015"></a><a name="p58391132203015"></a>Check whether the tenant quota is configured.</p>
</td>
</tr>
<tr id="row138391832113015"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p15839632163020"><a name="p15839632163020"></a><a name="p15839632163020"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p783912326304"><a name="p783912326304"></a><a name="p783912326304"></a>EVS.1034</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1483983217302"><a name="p1483983217302"></a><a name="p1483983217302"></a>Insufficient disk quantity quota assigned to the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p13839163203010"><a name="p13839163203010"></a><a name="p13839163203010"></a>volume count exceeded volume count quota!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1683983283019"><a name="p1683983283019"></a><a name="p1683983283019"></a>Increase the disk quantity quota.</p>
</td>
</tr>
<tr id="row107471219183417"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p188491332193012"><a name="p188491332193012"></a><a name="p188491332193012"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p2084915323305"><a name="p2084915323305"></a><a name="p2084915323305"></a>EVS.1036</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p188496321307"><a name="p188496321307"></a><a name="p188496321307"></a>Parameter <strong id="b6673544511499"><a name="b6673544511499"></a><a name="b6673544511499"></a>availability_zone</strong> set in the request to create the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p7849163223017"><a name="p7849163223017"></a><a name="p7849163223017"></a>invalid availability zone!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p6849153219305"><a name="p6849153219305"></a><a name="p6849153219305"></a>Enter the correct AZ.</p>
</td>
</tr>
<tr id="row15707141875"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p12667101819711"><a name="p12667101819711"></a><a name="p12667101819711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1667111812715"><a name="p1667111812715"></a><a name="p1667111812715"></a>EVS.1039</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p666713181776"><a name="p666713181776"></a><a name="p666713181776"></a>Input parameter <strong id="b136236399382"><a name="b136236399382"></a><a name="b136236399382"></a>sort_key</strong> is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p166671918672"><a name="p166671918672"></a><a name="p166671918672"></a>invalid sort_key!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p666714181777"><a name="p666714181777"></a><a name="p666714181777"></a>Check whether parameter <strong id="b1916354453910"><a name="b1916354453910"></a><a name="b1916354453910"></a>sort_key</strong> is correctly specified.</p>
</td>
</tr>
<tr id="row16278421443"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p885920322308"><a name="p885920322308"></a><a name="p885920322308"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p585963218308"><a name="p585963218308"></a><a name="p585963218308"></a>EVS.1040</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p9859153212305"><a name="p9859153212305"></a><a name="p9859153212305"></a>Parameter <strong id="b3799892711499"><a name="b3799892711499"></a><a name="b3799892711499"></a>sort_dir</strong> in the URL for querying the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p15859732103011"><a name="p15859732103011"></a><a name="p15859732103011"></a>invalid sort_dir!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p38591732113013"><a name="p38591732113013"></a><a name="p38591732113013"></a>Ensure that the <strong id="b1152445817173622"><a name="b1152445817173622"></a><a name="b1152445817173622"></a>sort_dir</strong> value is <strong id="b842352706173630"><a name="b842352706173630"></a><a name="b842352706173630"></a>desc</strong> or <strong id="b842352706173638"><a name="b842352706173638"></a><a name="b842352706173638"></a>asc</strong>.</p>
</td>
</tr>
<tr id="row1062718429441"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p148606321307"><a name="p148606321307"></a><a name="p148606321307"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p08601432193018"><a name="p08601432193018"></a><a name="p08601432193018"></a>EVS.1041</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p486019324307"><a name="p486019324307"></a><a name="p486019324307"></a>Parameter <strong id="b5711114111499"><a name="b5711114111499"></a><a name="b5711114111499"></a>availability-zone</strong> in the URL for querying the disk is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p78602032143019"><a name="p78602032143019"></a><a name="p78602032143019"></a>invalid filter availablity-zone!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p386019323302"><a name="p386019323302"></a><a name="p386019323302"></a>Check whether the AZ specified in the request is valid.</p>
</td>
</tr>
<tr id="row17839203213307"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p38404328306"><a name="p38404328306"></a><a name="p38404328306"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1284023216308"><a name="p1284023216308"></a><a name="p1284023216308"></a>EVS.1042</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p2840332183019"><a name="p2840332183019"></a><a name="p2840332183019"></a>Insufficient disk capacity quota assigned to the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p6840103233010"><a name="p6840103233010"></a><a name="p6840103233010"></a>volume gigabytes exceeded volume gigabytes quota!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1384014325303"><a name="p1384014325303"></a><a name="p1384014325303"></a>Increase the disk capacity quota.</p>
</td>
</tr>
<tr id="row97111610689"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p88991916485"><a name="p88991916485"></a><a name="p88991916485"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p28992161887"><a name="p28992161887"></a><a name="p28992161887"></a>EVS.1043</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p5900161620811"><a name="p5900161620811"></a><a name="p5900161620811"></a>Parameters <strong id="b85131145194215"><a name="b85131145194215"></a><a name="b85131145194215"></a>__system__encrypted</strong>, <strong id="b18495174934218"><a name="b18495174934218"></a><a name="b18495174934218"></a>__system__cmkid</strong>, and <strong id="b131969521424"><a name="b131969521424"></a><a name="b131969521424"></a>hw:passthrough</strong> are not supported when a disk is created from an image or a snapshot.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p89001816881"><a name="p89001816881"></a><a name="p89001816881"></a>encrypt and cmk and passthrougth in metadata is not support when create volume from snapshot or image!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p199001416285"><a name="p199001416285"></a><a name="p199001416285"></a>Check whether the request body is correct. For details, see the <strong id="b183070488442"><a name="b183070488442"></a><a name="b183070488442"></a>metadata</strong> field description for creating disks.</p>
</td>
</tr>
<tr id="row1499794614327"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1384993233014"><a name="p1384993233014"></a><a name="p1384993233014"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p884913293020"><a name="p884913293020"></a><a name="p884913293020"></a>EVS.1044</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p584943283013"><a name="p584943283013"></a><a name="p584943283013"></a>The backup cannot be used to create a disk.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p16849103218304"><a name="p16849103218304"></a><a name="p16849103218304"></a>backup status must be available when create a volume from it!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p16849932113011"><a name="p16849932113011"></a><a name="p16849932113011"></a>The backup is unavailable.</p>
</td>
</tr>
<tr id="row099814617329"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1384963216305"><a name="p1384963216305"></a><a name="p1384963216305"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p13849232143014"><a name="p13849232143014"></a><a name="p13849232143014"></a>EVS.1045</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p485093210300"><a name="p485093210300"></a><a name="p485093210300"></a>Failed to query the backup details.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p6850132153012"><a name="p6850132153012"></a><a name="p6850132153012"></a>backupDetail returned by FSP is null!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p48508325309"><a name="p48508325309"></a><a name="p48508325309"></a>Check whether the backup exists. Contact <span id="text184875403160"><a name="text184875403160"></a><a name="text184875403160"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row957845794015"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p6854163203017"><a name="p6854163203017"></a><a name="p6854163203017"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p118541132183013"><a name="p118541132183013"></a><a name="p118541132183013"></a>EVS.1046</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1285414329308"><a name="p1285414329308"></a><a name="p1285414329308"></a>Failed to delete the disk because the disk status is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1485453214309"><a name="p1485453214309"></a><a name="p1485453214309"></a>volume status must be available, error,  error_extending, error_restoring, error_rollbacking when delete volume!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p12854123203014"><a name="p12854123203014"></a><a name="p12854123203014"></a>Contact <span id="text126231430111719"><a name="text126231430111719"></a><a name="text126231430111719"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row6578105724020"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p118551032163011"><a name="p118551032163011"></a><a name="p118551032163011"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p48550327302"><a name="p48550327302"></a><a name="p48550327302"></a>EVS.1047</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p18551832123019"><a name="p18551832123019"></a><a name="p18551832123019"></a>Failed to delete the snapshot because the snapshot status is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1185512329301"><a name="p1185512329301"></a><a name="p1185512329301"></a>snapshot status must be available or error when delete snapshot!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p208558326306"><a name="p208558326306"></a><a name="p208558326306"></a>Contact <span id="text59143551713"><a name="text59143551713"></a><a name="text59143551713"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row1895013316406"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1485343223019"><a name="p1485343223019"></a><a name="p1485343223019"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p198541732113016"><a name="p198541732113016"></a><a name="p198541732113016"></a>EVS.1048</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p3854153283015"><a name="p3854153283015"></a><a name="p3854153283015"></a>Failed to expand the disk capacity because the disk status is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p13854153210303"><a name="p13854153210303"></a><a name="p13854153210303"></a>volume status must be available when extend volume!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p18854103253016"><a name="p18854103253016"></a><a name="p18854103253016"></a>Ensure that the disk status meets the expansion requirements.</p>
</td>
</tr>
<tr id="row8998146123211"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p5850932143012"><a name="p5850932143012"></a><a name="p5850932143012"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p385033213308"><a name="p385033213308"></a><a name="p385033213308"></a>EVS.1049</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p15850632163014"><a name="p15850632163014"></a><a name="p15850632163014"></a>The backup used to create the disk is in the incorrect AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p4850173219302"><a name="p4850173219302"></a><a name="p4850173219302"></a>available-zone is not equal to backup available-zone!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p885083211303"><a name="p885083211303"></a><a name="p885083211303"></a>The backup and the disk to be created must in the same AZ.</p>
</td>
</tr>
<tr id="row371820557820"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p560634491"><a name="p560634491"></a><a name="p560634491"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p9606141493"><a name="p9606141493"></a><a name="p9606141493"></a>EVS.1051</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p16061845910"><a name="p16061845910"></a><a name="p16061845910"></a>Batch creating disks from a backup is not available.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p76068415916"><a name="p76068415916"></a><a name="p76068415916"></a>can not batch create volume from backup!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p8606842914"><a name="p8606842914"></a><a name="p8606842914"></a>Batch creating disks from a backup is not available.</p>
</td>
</tr>
<tr id="row147191355080"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p106061748919"><a name="p106061748919"></a><a name="p106061748919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1960614291"><a name="p1960614291"></a><a name="p1960614291"></a>EVS.1052</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1860784092"><a name="p1860784092"></a><a name="p1860784092"></a>Request conversion error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p156071541395"><a name="p156071541395"></a><a name="p156071541395"></a>invalid http body!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1560754991"><a name="p1560754991"></a><a name="p1560754991"></a>Check whether the request body is correct.</p>
</td>
</tr>
<tr id="row07192055088"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p160744891"><a name="p160744891"></a><a name="p160744891"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p126071349915"><a name="p126071349915"></a><a name="p126071349915"></a>EVS.1053</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p0607341491"><a name="p0607341491"></a><a name="p0607341491"></a>Too many disks are specified in the request for batch deleting disks.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p16071441794"><a name="p16071441794"></a><a name="p16071441794"></a>the size of volumes to be deleted is too large!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1607440912"><a name="p1607440912"></a><a name="p1607440912"></a>Reduce the number of disks specified in the batch.</p>
</td>
</tr>
<tr id="row971920551280"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p20607164492"><a name="p20607164492"></a><a name="p20607164492"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p36071442913"><a name="p36071442913"></a><a name="p36071442913"></a>EVS.1054</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1260714190"><a name="p1260714190"></a><a name="p1260714190"></a>Input parameter <strong id="b161111281798"><a name="b161111281798"></a><a name="b161111281798"></a>shareable</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p7607647919"><a name="p7607647919"></a><a name="p7607647919"></a>invalid shareable parameter!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p66082416913"><a name="p66082416913"></a><a name="p66082416913"></a>Check whether parameter <strong id="b72463010913"><a name="b72463010913"></a><a name="b72463010913"></a>shareable</strong> is correctly specified.</p>
</td>
</tr>
<tr id="row207207551687"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p16087416915"><a name="p16087416915"></a><a name="p16087416915"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p19608541393"><a name="p19608541393"></a><a name="p19608541393"></a>EVS.1057</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p76081341395"><a name="p76081341395"></a><a name="p76081341395"></a>Input parameter <strong id="b11997131121415"><a name="b11997131121415"></a><a name="b11997131121415"></a>hw:passthrough</strong> under <strong id="b142583413144"><a name="b142583413144"></a><a name="b142583413144"></a>metadata</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p160819410920"><a name="p160819410920"></a><a name="p160819410920"></a>invalid hw:passthrough in metadata!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p260884698"><a name="p260884698"></a><a name="p260884698"></a>Check whether parameter <strong id="b68031740151416"><a name="b68031740151416"></a><a name="b68031740151416"></a>hw:passthrough</strong> is correctly specified.</p>
</td>
</tr>
<tr id="row87201255789"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p18608134799"><a name="p18608134799"></a><a name="p18608134799"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1160874498"><a name="p1160874498"></a><a name="p1160874498"></a>EVS.1058</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p11608114794"><a name="p11608114794"></a><a name="p11608114794"></a>Metadata decoding error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1860810417917"><a name="p1860810417917"></a><a name="p1860810417917"></a>invalid metadata filter!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p16088418915"><a name="p16088418915"></a><a name="p16088418915"></a>Check whether parameter <strong id="b152231052111418"><a name="b152231052111418"></a><a name="b152231052111418"></a>metadata</strong> is correctly specified.</p>
</td>
</tr>
<tr id="row7457141416373"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p485110324303"><a name="p485110324303"></a><a name="p485110324303"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p13851173219308"><a name="p13851173219308"></a><a name="p13851173219308"></a>EVS.1061</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p485193219305"><a name="p485193219305"></a><a name="p485193219305"></a>The tag quantity of this EVS disk exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p485183253010"><a name="p485183253010"></a><a name="p485183253010"></a>The Volume Tags is Exceed Max Limit Num.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p085113323300"><a name="p085113323300"></a><a name="p085113323300"></a>Ensure that the tag quantity of the disk is within the upper limit.</p>
</td>
</tr>
<tr id="row7809101643717"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p585112328304"><a name="p585112328304"></a><a name="p585112328304"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p9851153213306"><a name="p9851153213306"></a><a name="p9851153213306"></a>EVS.1062</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p38521132133018"><a name="p38521132133018"></a><a name="p38521132133018"></a>Invalid tag.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1285233283014"><a name="p1285233283014"></a><a name="p1285233283014"></a>invalid tag!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1985273203018"><a name="p1985273203018"></a><a name="p1985273203018"></a>Check the formats of the tag key and tag value and ensure that the formats are correct.</p>
</td>
</tr>
<tr id="row13929423593"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p14681454296"><a name="p14681454296"></a><a name="p14681454296"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p068175416913"><a name="p068175416913"></a><a name="p068175416913"></a>EVS.1063</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p46813541393"><a name="p46813541393"></a><a name="p46813541393"></a>Input parameter <strong id="b1255231211512"><a name="b1255231211512"></a><a name="b1255231211512"></a>full_clone</strong> under <strong id="b9553612121512"><a name="b9553612121512"></a><a name="b9553612121512"></a>metadata</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p56895413916"><a name="p56895413916"></a><a name="p56895413916"></a>invalid full_clone in metadata!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p9695541699"><a name="p9695541699"></a><a name="p9695541699"></a>Check whether parameter <strong id="b424765081517"><a name="b424765081517"></a><a name="b424765081517"></a>full_clone</strong> in <strong id="b9799174811218"><a name="b9799174811218"></a><a name="b9799174811218"></a>metadata</strong> is correctly specified.</p>
</td>
</tr>
<tr id="row292932320912"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p469254796"><a name="p469254796"></a><a name="p469254796"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p196917541595"><a name="p196917541595"></a><a name="p196917541595"></a>EVS.1064</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p36920541799"><a name="p36920541799"></a><a name="p36920541799"></a>A disk can be expanded only when its status is <strong id="b52742012102019"><a name="b52742012102019"></a><a name="b52742012102019"></a>available</strong> or <strong id="b10781715142012"><a name="b10781715142012"></a><a name="b10781715142012"></a>in-use</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p26935419920"><a name="p26935419920"></a><a name="p26935419920"></a>volume status must be available or in-use when extending!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p7693543920"><a name="p7693543920"></a><a name="p7693543920"></a>Ensure that the disk is in the <strong id="b1364104320206"><a name="b1364104320206"></a><a name="b1364104320206"></a>available</strong> or <strong id="b2064134372018"><a name="b2064134372018"></a><a name="b2064134372018"></a>in-use</strong> state before expansion.</p>
</td>
</tr>
<tr id="row2929423294"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p18691154794"><a name="p18691154794"></a><a name="p18691154794"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1769105416911"><a name="p1769105416911"></a><a name="p1769105416911"></a>EVS.1065</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p2691546912"><a name="p2691546912"></a><a name="p2691546912"></a>A shared disk can be expanded only when its status is <strong id="b7244417122310"><a name="b7244417122310"></a><a name="b7244417122310"></a>available</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p86945412914"><a name="p86945412914"></a><a name="p86945412914"></a>multiattach volume status must be available when extending!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p166905417914"><a name="p166905417914"></a><a name="p166905417914"></a>Ensure that the shared disk is in the <strong id="b11778151452419"><a name="b11778151452419"></a><a name="b11778151452419"></a>available</strong> state before expansion.</p>
</td>
</tr>
<tr id="row137445360918"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1369954599"><a name="p1369954599"></a><a name="p1369954599"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p7700545911"><a name="p7700545911"></a><a name="p7700545911"></a>EVS.1066</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p7701954792"><a name="p7701954792"></a><a name="p7701954792"></a>The ECS or BMS status fails to meet the requirement of online disk expansion.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1971354392"><a name="p1971354392"></a><a name="p1971354392"></a>status of ECS or BMS does not support volume online extension!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p16711754293"><a name="p16711754293"></a><a name="p16711754293"></a>Ensure that the ECS or BMS status meets the requirement.</p>
</td>
</tr>
<tr id="row197451936291"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p8722548919"><a name="p8722548919"></a><a name="p8722548919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1972185414915"><a name="p1972185414915"></a><a name="p1972185414915"></a>EVS.1070</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p187214541994"><a name="p187214541994"></a><a name="p187214541994"></a>Request conversion error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p77485413919"><a name="p77485413919"></a><a name="p77485413919"></a>invalid request.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p4741954697"><a name="p4741954697"></a><a name="p4741954697"></a>Check whether the request body is correct.</p>
</td>
</tr>
<tr id="row158401932163016"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1084017322309"><a name="p1084017322309"></a><a name="p1084017322309"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p158402329307"><a name="p158402329307"></a><a name="p158402329307"></a>EVS.2001</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1384033263015"><a name="p1384033263015"></a><a name="p1384033263015"></a>Failed to submit the task.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p884063214302"><a name="p884063214302"></a><a name="p884063214302"></a>submit job failed!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p8840183283013"><a name="p8840183283013"></a><a name="p8840183283013"></a>Contact <span id="text476112437178"><a name="text476112437178"></a><a name="text476112437178"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row18840183217307"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p984013324304"><a name="p984013324304"></a><a name="p984013324304"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1840193212306"><a name="p1840193212306"></a><a name="p1840193212306"></a>EVS.2002</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p17840123211306"><a name="p17840123211306"></a><a name="p17840123211306"></a>The system is currently unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p884033217307"><a name="p884033217307"></a><a name="p884033217307"></a>internal error!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1584023203015"><a name="p1584023203015"></a><a name="p1584023203015"></a>Contact <span id="text27646452172"><a name="text27646452172"></a><a name="text27646452172"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row1484013323305"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p208401332173019"><a name="p208401332173019"></a><a name="p208401332173019"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p58402032193010"><a name="p58402032193010"></a><a name="p58402032193010"></a>EVS.2005</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p108401232163012"><a name="p108401232163012"></a><a name="p108401232163012"></a>A connection exception occurs.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1284013218309"><a name="p1284013218309"></a><a name="p1284013218309"></a>client exception!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p484083215300"><a name="p484083215300"></a><a name="p484083215300"></a>Contact <span id="text12748247131716"><a name="text12748247131716"></a><a name="text12748247131716"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row7840153217302"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p984117321306"><a name="p984117321306"></a><a name="p984117321306"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1084115328305"><a name="p1084115328305"></a><a name="p1084115328305"></a>EVS.2007</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p20841173293012"><a name="p20841173293012"></a><a name="p20841173293012"></a>Updating the metadata of the disk timed out.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p8841532153013"><a name="p8841532153013"></a><a name="p8841532153013"></a>update volume timeout!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p12841123223010"><a name="p12841123223010"></a><a name="p12841123223010"></a>Try again later or contact <span id="text5733185711715"><a name="text5733185711715"></a><a name="text5733185711715"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row484173215304"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p284143243014"><a name="p284143243014"></a><a name="p284143243014"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p5841232133016"><a name="p5841232133016"></a><a name="p5841232133016"></a>EVS.2010</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1784119323306"><a name="p1784119323306"></a><a name="p1784119323306"></a>Failed to obtain the token for the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p484113216305"><a name="p484113216305"></a><a name="p484113216305"></a>exchange token failed!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p48411132193018"><a name="p48411132193018"></a><a name="p48411132193018"></a>Check the user permissions.</p>
</td>
</tr>
<tr id="row884133233017"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1841732113015"><a name="p1841732113015"></a><a name="p1841732113015"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p7841732103015"><a name="p7841732103015"></a><a name="p7841732103015"></a>EVS.2011</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p128411932183017"><a name="p128411932183017"></a><a name="p128411932183017"></a>Deleting order information from the disk metadata timed out.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p88411032103012"><a name="p88411032103012"></a><a name="p88411032103012"></a>delete orderId and productId timeout!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1684113324301"><a name="p1684113324301"></a><a name="p1684113324301"></a>Try again later or contact <span id="text744016141819"><a name="text744016141819"></a><a name="text744016141819"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row12841532113013"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p98421132153015"><a name="p98421132153015"></a><a name="p98421132153015"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p18842103213302"><a name="p18842103213302"></a><a name="p18842103213302"></a>EVS.2013</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1584283216301"><a name="p1584283216301"></a><a name="p1584283216301"></a>Failed to elevate the permissions.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1984212329304"><a name="p1984212329304"></a><a name="p1984212329304"></a>assume role error!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p384233220303"><a name="p384233220303"></a><a name="p384233220303"></a>Contact <span id="text1764413141815"><a name="text1764413141815"></a><a name="text1764413141815"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row8343123610114"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p935834471115"><a name="p935834471115"></a><a name="p935834471115"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p12358644201110"><a name="p12358644201110"></a><a name="p12358644201110"></a>EVS.2014</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p10358174491120"><a name="p10358174491120"></a><a name="p10358174491120"></a>Failed to escalate rights.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p935814418114"><a name="p935814418114"></a><a name="p935814418114"></a>thread is interrupted when sleep!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1835804410119"><a name="p1835804410119"></a><a name="p1835804410119"></a>Try again later or contact <span id="text208341957183"><a name="text208341957183"></a><a name="text208341957183"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row56581327174219"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1985510328307"><a name="p1985510328307"></a><a name="p1985510328307"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p3855332103013"><a name="p3855332103013"></a><a name="p3855332103013"></a>EVS.2019</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p9855532113016"><a name="p9855532113016"></a><a name="p9855532113016"></a>Failed to delete the snapshot because the snapshot is in the <strong id="b1997569111499"><a name="b1997569111499"></a><a name="b1997569111499"></a>error_deleting</strong> status.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p188551232173012"><a name="p188551232173012"></a><a name="p188551232173012"></a>snapshot is error_deleting!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p48552328306"><a name="p48552328306"></a><a name="p48552328306"></a>Contact <span id="text11565775189"><a name="text11565775189"></a><a name="text11565775189"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row2659152713425"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p13855532113011"><a name="p13855532113011"></a><a name="p13855532113011"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p15855173243010"><a name="p15855173243010"></a><a name="p15855173243010"></a>EVS.2020</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p985573218309"><a name="p985573218309"></a><a name="p985573218309"></a>Failed to delete the disk because the disk is in the <strong id="b1715599111499"><a name="b1715599111499"></a><a name="b1715599111499"></a>error_deleting</strong> status.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p4855103213014"><a name="p4855103213014"></a><a name="p4855103213014"></a>volume is error_deleting!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p168557321305"><a name="p168557321305"></a><a name="p168557321305"></a>Contact <span id="text185410911188"><a name="text185410911188"></a><a name="text185410911188"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row12452125015117"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p48071355111112"><a name="p48071355111112"></a><a name="p48071355111112"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1180713551114"><a name="p1180713551114"></a><a name="p1180713551114"></a>EVS.2021</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p178073552114"><a name="p178073552114"></a><a name="p178073552114"></a>The disk status is <strong id="b691454414339"><a name="b691454414339"></a><a name="b691454414339"></a>error_detaching</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p13808255161117"><a name="p13808255161117"></a><a name="p13808255161117"></a>volume is error_detaching!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p38086551115"><a name="p38086551115"></a><a name="p38086551115"></a>Try again later or contact <span id="text1172871017181"><a name="text1172871017181"></a><a name="text1172871017181"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row12842193223014"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1484211324308"><a name="p1484211324308"></a><a name="p1484211324308"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p128421532153016"><a name="p128421532153016"></a><a name="p128421532153016"></a>EVS.2023</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p11842183223010"><a name="p11842183223010"></a><a name="p11842183223010"></a>Network connection timed out.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p68420320308"><a name="p68420320308"></a><a name="p68420320308"></a>ConnectException happened!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p48491918105319"><a name="p48491918105319"></a><a name="p48491918105319"></a>Try again. If the network fails, check the network status.</p>
<p id="p4842103217303"><a name="p4842103217303"></a><a name="p4842103217303"></a>If the network status is abnormal, contact <span id="text14865101471810"><a name="text14865101471810"></a><a name="text14865101471810"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row1993975053611"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p285010326305"><a name="p285010326305"></a><a name="p285010326305"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p785193219301"><a name="p785193219301"></a><a name="p785193219301"></a>EVS.2024</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p485112325306"><a name="p485112325306"></a><a name="p485112325306"></a>The status of the created disk is <strong id="b1507986011499"><a name="b1507986011499"></a><a name="b1507986011499"></a>error</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1485153293019"><a name="p1485153293019"></a><a name="p1485153293019"></a>volume is error!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p38511032183016"><a name="p38511032183016"></a><a name="p38511032183016"></a>Contact <span id="text3648416181816"><a name="text3648416181816"></a><a name="text3648416181816"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row62051653153615"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p585183273014"><a name="p585183273014"></a><a name="p585183273014"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p78519328308"><a name="p78519328308"></a><a name="p78519328308"></a>EVS.2025</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p16851193273018"><a name="p16851193273018"></a><a name="p16851193273018"></a>The status of the created disk is <strong id="b4955814511499"><a name="b4955814511499"></a><a name="b4955814511499"></a>error_restoring</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p18851143253018"><a name="p18851143253018"></a><a name="p18851143253018"></a>volume is error_restoring!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p78511732163020"><a name="p78511732163020"></a><a name="p78511732163020"></a>Contact <span id="text1442861811182"><a name="text1442861811182"></a><a name="text1442861811182"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row07444384220"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p68541732123013"><a name="p68541732123013"></a><a name="p68541732123013"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p185493218305"><a name="p185493218305"></a><a name="p185493218305"></a>EVS.2026</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p20854123212304"><a name="p20854123212304"></a><a name="p20854123212304"></a>Failed to expand the disk capacity because the disk is in the <strong id="b1143031911499"><a name="b1143031911499"></a><a name="b1143031911499"></a>error_extending</strong> state.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p58545327307"><a name="p58545327307"></a><a name="p58545327307"></a>volume is error_extending!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p15854193216302"><a name="p15854193216302"></a><a name="p15854193216302"></a>Contact <span id="text1912552013181"><a name="text1912552013181"></a><a name="text1912552013181"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row10842103213014"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p4842193213019"><a name="p4842193213019"></a><a name="p4842193213019"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p118425324300"><a name="p118425324300"></a><a name="p118425324300"></a>EVS.2029</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1684223213020"><a name="p1684223213020"></a><a name="p1684223213020"></a>Incorrect subtask quantity.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p484253219304"><a name="p484253219304"></a><a name="p484253219304"></a>The size of joIdList and resultList are mismatched!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p10842203212308"><a name="p10842203212308"></a><a name="p10842203212308"></a>Contact <span id="text133091224131818"><a name="text133091224131818"></a><a name="text133091224131818"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row17842113223020"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p108421632193010"><a name="p108421632193010"></a><a name="p108421632193010"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p18431432183019"><a name="p18431432183019"></a><a name="p18431432183019"></a>EVS.2030</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p7843132163019"><a name="p7843132163019"></a><a name="p7843132163019"></a>Failed to submit the subtask again.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p38439322306"><a name="p38439322306"></a><a name="p38439322306"></a>query context based on parent jobId exception!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p188436329302"><a name="p188436329302"></a><a name="p188436329302"></a>Contact <span id="text2762132912184"><a name="text2762132912184"></a><a name="text2762132912184"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row3843143213301"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1984323214307"><a name="p1984323214307"></a><a name="p1984323214307"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p148431132123016"><a name="p148431132123016"></a><a name="p148431132123016"></a>EVS.2031</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p184363293020"><a name="p184363293020"></a><a name="p184363293020"></a>Failed to query the context.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p784343217309"><a name="p784343217309"></a><a name="p784343217309"></a>result queried from context is null!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p4843103210308"><a name="p4843103210308"></a><a name="p4843103210308"></a>Contact <span id="text94715311183"><a name="text94715311183"></a><a name="text94715311183"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row138431332123012"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p3843163263020"><a name="p3843163263020"></a><a name="p3843163263020"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1784323219302"><a name="p1784323219302"></a><a name="p1784323219302"></a>EVS.2032</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p178431323302"><a name="p178431323302"></a><a name="p178431323302"></a>Failed to query the disk quantity quota assigned to the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p10843123273011"><a name="p10843123273011"></a><a name="p10843123273011"></a>some volume count quota usage params are null!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p88436328301"><a name="p88436328301"></a><a name="p88436328301"></a>Try again later or contact <span id="text1698413211184"><a name="text1698413211184"></a><a name="text1698413211184"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row188435322309"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p128431932113018"><a name="p128431932113018"></a><a name="p128431932113018"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1844153283016"><a name="p1844153283016"></a><a name="p1844153283016"></a>EVS.2033</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p4844832193016"><a name="p4844832193016"></a><a name="p4844832193016"></a>Failed to query the disk capacity quota assigned to the tenant.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p16844153210304"><a name="p16844153210304"></a><a name="p16844153210304"></a>some volume gigabytes quota usage params are null!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p684443233011"><a name="p684443233011"></a><a name="p684443233011"></a>Try again later or contact <span id="text12721234111810"><a name="text12721234111810"></a><a name="text12721234111810"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row950974416124"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p846218518131"><a name="p846218518131"></a><a name="p846218518131"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p146316510138"><a name="p146316510138"></a><a name="p146316510138"></a>EVS.2034</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p14463359133"><a name="p14463359133"></a><a name="p14463359133"></a>Token resolution failure.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1546316551313"><a name="p1546316551313"></a><a name="p1546316551313"></a>domainId decoded from token is null or empty!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p2046310511138"><a name="p2046310511138"></a><a name="p2046310511138"></a>Check whether the account information is correct.</p>
</td>
</tr>
<tr id="row2510184416122"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p15463205131312"><a name="p15463205131312"></a><a name="p15463205131312"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p546313510138"><a name="p546313510138"></a><a name="p546313510138"></a>EVS.2035</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1046314571313"><a name="p1046314571313"></a><a name="p1046314571313"></a>Token resolution failure.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p3463052136"><a name="p3463052136"></a><a name="p3463052136"></a>domainName decoded from token is null or empty!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p646313516135"><a name="p646313516135"></a><a name="p646313516135"></a>Check whether the account information is correct.</p>
</td>
</tr>
<tr id="row351074471212"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1046313512135"><a name="p1046313512135"></a><a name="p1046313512135"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p11463105151316"><a name="p11463105151316"></a><a name="p11463105151316"></a>EVS.2036</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p04631154136"><a name="p04631154136"></a><a name="p04631154136"></a>Empty token.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1646365121311"><a name="p1646365121311"></a><a name="p1646365121311"></a>the result of decode token is null!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p5463125171311"><a name="p5463125171311"></a><a name="p5463125171311"></a>Check whether the account information is correct.</p>
</td>
</tr>
<tr id="row45112446122"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p04643510137"><a name="p04643510137"></a><a name="p04643510137"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p124641558136"><a name="p124641558136"></a><a name="p124641558136"></a>EVS.2040</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p104641352139"><a name="p104641352139"></a><a name="p104641352139"></a>Incorrect key status.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p94641259132"><a name="p94641259132"></a><a name="p94641259132"></a>The status of encrypt Key is not enable!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p146417519139"><a name="p146417519139"></a><a name="p146417519139"></a>Ensure that the key status is correct.</p>
</td>
</tr>
<tr id="row145121044131217"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p8464135101320"><a name="p8464135101320"></a><a name="p8464135101320"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1446418511315"><a name="p1446418511315"></a><a name="p1446418511315"></a>EVS.2041</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p164642516132"><a name="p164642516132"></a><a name="p164642516132"></a>The input encryption parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p5464145121316"><a name="p5464145121316"></a><a name="p5464145121316"></a>The encrypt Param is invalid!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p15464125141315"><a name="p15464125141315"></a><a name="p15464125141315"></a>Check whether the encryption parameter in the request body is correct.</p>
</td>
</tr>
<tr id="row1851216445124"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p846415201320"><a name="p846415201320"></a><a name="p846415201320"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p134642516130"><a name="p134642516130"></a><a name="p134642516130"></a>EVS.2042</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p12464195141317"><a name="p12464195141317"></a><a name="p12464195141317"></a>Failed to create the CMK.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p946416516137"><a name="p946416516137"></a><a name="p946416516137"></a>Failed to create cmk.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p546475191320"><a name="p546475191320"></a><a name="p546475191320"></a>Try again later or contact <span id="text166382563184"><a name="text166382563184"></a><a name="text166382563184"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row10957153019129"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p34648518138"><a name="p34648518138"></a><a name="p34648518138"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1746416519131"><a name="p1746416519131"></a><a name="p1746416519131"></a>EVS.2043</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p13464125121314"><a name="p13464125121314"></a><a name="p13464125121314"></a>The snapshot status is in correct.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p94647517139"><a name="p94647517139"></a><a name="p94647517139"></a>The status of snapshot is not available or backing-up.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p16464958133"><a name="p16464958133"></a><a name="p16464958133"></a>Ensure that the snapshot status is <strong id="b736481915118"><a name="b736481915118"></a><a name="b736481915118"></a>available</strong> or <strong id="b143415227119"><a name="b143415227119"></a><a name="b143415227119"></a>backing-up</strong>.</p>
</td>
</tr>
<tr id="row139571630101214"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p74641057131"><a name="p74641057131"></a><a name="p74641057131"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p164641531314"><a name="p164641531314"></a><a name="p164641531314"></a>EVS.2044</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p104648516135"><a name="p104648516135"></a><a name="p104648516135"></a>Failed to check KMS.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p2464165181312"><a name="p2464165181312"></a><a name="p2464165181312"></a>Failed to check the role of kms.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p174641957135"><a name="p174641957135"></a><a name="p174641957135"></a>Try again later or contact <span id="text4559125815184"><a name="text4559125815184"></a><a name="text4559125815184"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row9957203041217"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p17464195201319"><a name="p17464195201319"></a><a name="p17464195201319"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p124647531314"><a name="p124647531314"></a><a name="p124647531314"></a>EVS.2045</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p54642513138"><a name="p54642513138"></a><a name="p54642513138"></a>Input parameter <strong id="b181321891417"><a name="b181321891417"></a><a name="b181321891417"></a>snapshot_id</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p184647521311"><a name="p184647521311"></a><a name="p184647521311"></a>invalid snapshot_id!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p94644561310"><a name="p94644561310"></a><a name="p94644561310"></a>Ensure that the input <strong id="b17559162171513"><a name="b17559162171513"></a><a name="b17559162171513"></a>snapshot_id</strong> value is correct.</p>
</td>
</tr>
<tr id="row49573302127"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1646417511317"><a name="p1646417511317"></a><a name="p1646417511317"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p154647512134"><a name="p154647512134"></a><a name="p154647512134"></a>EVS.2046</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1346416517130"><a name="p1346416517130"></a><a name="p1346416517130"></a>Input parameter <strong id="b643912222152"><a name="b643912222152"></a><a name="b643912222152"></a>imageRef</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1946416561311"><a name="p1946416561311"></a><a name="p1946416561311"></a>invalid imageRef!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p16465652135"><a name="p16465652135"></a><a name="p16465652135"></a>Ensure that the input <strong id="b4775183214156"><a name="b4775183214156"></a><a name="b4775183214156"></a>imageRef</strong> value is correct.</p>
</td>
</tr>
<tr id="row11957630111211"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1046519519134"><a name="p1046519519134"></a><a name="p1046519519134"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p546513541316"><a name="p546513541316"></a><a name="p546513541316"></a>EVS.2047</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p34651457134"><a name="p34651457134"></a><a name="p34651457134"></a>The <strong id="b10626152561610"><a name="b10626152561610"></a><a name="b10626152561610"></a>metadata</strong> field cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p4465115121313"><a name="p4465115121313"></a><a name="p4465115121313"></a>the metadata Param is not allowed to be updated!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p646515181319"><a name="p646515181319"></a><a name="p646515181319"></a>Ensure that the input <strong id="b5153827121611"><a name="b5153827121611"></a><a name="b5153827121611"></a>metadata</strong> value is correct.</p>
</td>
</tr>
<tr id="row12272102691219"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p94651457139"><a name="p94651457139"></a><a name="p94651457139"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p14465105151318"><a name="p14465105151318"></a><a name="p14465105151318"></a>EVS.2050</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p20465658133"><a name="p20465658133"></a><a name="p20465658133"></a>Failed to set the disk QoS.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p154651353138"><a name="p154651353138"></a><a name="p154651353138"></a>set volume Qos failed!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1546555181311"><a name="p1546555181311"></a><a name="p1546555181311"></a>Ensure that the input <strong id="b050312910182"><a name="b050312910182"></a><a name="b050312910182"></a>qos</strong> value is correct.</p>
</td>
</tr>
<tr id="row1927322613121"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p44662520138"><a name="p44662520138"></a><a name="p44662520138"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p134669551320"><a name="p134669551320"></a><a name="p134669551320"></a>EVS.2052</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p3466195181311"><a name="p3466195181311"></a><a name="p3466195181311"></a>The job corresponding to the order ID is not unique.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p4466854133"><a name="p4466854133"></a><a name="p4466854133"></a>the job result using order id to query is invalid!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p346615541316"><a name="p346615541316"></a><a name="p346615541316"></a>Try again later or contact <span id="text174481022192"><a name="text174481022192"></a><a name="text174481022192"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row0273172618127"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p64664513136"><a name="p64664513136"></a><a name="p64664513136"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p20466258131"><a name="p20466258131"></a><a name="p20466258131"></a>EVS.2053</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p4466157137"><a name="p4466157137"></a><a name="p4466157137"></a>Input parameter <strong id="b4193101282111"><a name="b4193101282111"></a><a name="b4193101282111"></a>availability_zone</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p246665181316"><a name="p246665181316"></a><a name="p246665181316"></a>The az information from request is invalid!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p94661753134"><a name="p94661753134"></a><a name="p94661753134"></a>Ensure that the input <strong id="b19839183682114"><a name="b19839183682114"></a><a name="b19839183682114"></a>availability_zone</strong> value is correct.</p>
</td>
</tr>
<tr id="row227315264122"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p18466155131311"><a name="p18466155131311"></a><a name="p18466155131311"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p547018541316"><a name="p547018541316"></a><a name="p547018541316"></a>EVS.2054</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1647118518133"><a name="p1647118518133"></a><a name="p1647118518133"></a>When the disk is created from a snapshot, the input <strong id="b1062572362313"><a name="b1062572362313"></a><a name="b1062572362313"></a>availability_zone</strong> value of the disk is inconsistent with that of the snapshot.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1047114591318"><a name="p1047114591318"></a><a name="p1047114591318"></a>Cannot create volume from snapshot as the az is invalid!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p347113521313"><a name="p347113521313"></a><a name="p347113521313"></a>Ensure that the <strong id="b23701537172613"><a name="b23701537172613"></a><a name="b23701537172613"></a>availability_zone</strong> value of the disk is consistent with that of the snapshot.</p>
</td>
</tr>
<tr id="row33471252451"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p12862143212303"><a name="p12862143212303"></a><a name="p12862143212303"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p3862143213014"><a name="p3862143213014"></a><a name="p3862143213014"></a>EVS.2055</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p686253213300"><a name="p686253213300"></a><a name="p686253213300"></a>KMS access rights have not been granted to EVS.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p188621032113010"><a name="p188621032113010"></a><a name="p188621032113010"></a>can not create encrypt volume because hasn't xrole.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p118624328309"><a name="p118624328309"></a><a name="p118624328309"></a>Before you use the disk encryption function, KMS access rights need to be granted to EVS. Grant the KMS access rights to EVS on the management console. After the rights have been granted, EVS can obtain KMS keys to encrypt or decrypt EVS disks.</p>
<p id="p138639325301"><a name="p138639325301"></a><a name="p138639325301"></a>For details about how to grant the KMS access rights, see <strong id="b84235270611461"><a name="b84235270611461"></a><a name="b84235270611461"></a>EVS Disk Encryption</strong> in the <em id="i842352697114612"><a name="i842352697114612"></a><a name="i842352697114612"></a>Elastic Volume Service User Guide</em>.</p>
</td>
</tr>
<tr id="row12389657144620"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p38601632163016"><a name="p38601632163016"></a><a name="p38601632163016"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p8860232103018"><a name="p8860232103018"></a><a name="p8860232103018"></a>EVS.2056</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p20860163210308"><a name="p20860163210308"></a><a name="p20860163210308"></a>Fine-grained PDP authentication failed.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p188610327307"><a name="p188610327307"></a><a name="p188610327307"></a>action in pdp check deny!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p16861143216300"><a name="p16861143216300"></a><a name="p16861143216300"></a>Check whether the account has relevant permissions, or the account is in arrears, does not pass real-name authentication, or has violations.</p>
</td>
</tr>
<tr id="row167931430191610"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p54461837191610"><a name="p54461837191610"></a><a name="p54461837191610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p444710374163"><a name="p444710374163"></a><a name="p444710374163"></a>EVS.2068</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p124471037101613"><a name="p124471037101613"></a><a name="p124471037101613"></a>Operations cannot be performed on locked resources.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p44471637151614"><a name="p44471637151614"></a><a name="p44471637151614"></a>operation failed because of volume be locked</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p644753731611"><a name="p644753731611"></a><a name="p644753731611"></a>Unlock the resource and then perform the operation.</p>
</td>
</tr>
<tr id="row14793113019162"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p5447143731612"><a name="p5447143731612"></a><a name="p5447143731612"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p16447183717162"><a name="p16447183717162"></a><a name="p16447183717162"></a>EVS.2070</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p164472372165"><a name="p164472372165"></a><a name="p164472372165"></a>Disk type does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p124471937161612"><a name="p124471937161612"></a><a name="p124471937161612"></a>VolumeTypes are not supported !</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1344763719160"><a name="p1344763719160"></a><a name="p1344763719160"></a>Try again later or contact <span id="text15455204121913"><a name="text15455204121913"></a><a name="text15455204121913"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row1679453071612"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p5447123751620"><a name="p5447123751620"></a><a name="p5447123751620"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p12447037131613"><a name="p12447037131613"></a><a name="p12447037131613"></a>EVS.2071</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p134471372162"><a name="p134471372162"></a><a name="p134471372162"></a>This type of disks in the current AZ is sold out.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p17447537161617"><a name="p17447537161617"></a><a name="p17447537161617"></a>Invalid input received: Availability zone [%s] do not have volume type [%s]</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p2044703711161"><a name="p2044703711161"></a><a name="p2044703711161"></a>Try again later or contact <span id="text1314726101916"><a name="text1314726101916"></a><a name="text1314726101916"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row1186215456486"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1786753253018"><a name="p1786753253018"></a><a name="p1786753253018"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1187411327309"><a name="p1187411327309"></a><a name="p1187411327309"></a>EVS.2072</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p0875183216307"><a name="p0875183216307"></a><a name="p0875183216307"></a>Disks of the ultra-high I/O type in AZ1 are sold out.</p>
<div class="note" id="note1687563219305"><a name="note1687563219305"></a><a name="note1687563219305"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5875432173011"><a name="p5875432173011"></a><a name="p5875432173011"></a>The ultra-high I/O disk type and AZ1 are used as the sample disk type and AZ. The disk type and AZ vary depending on the actual condition.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p0875173217307"><a name="p0875173217307"></a><a name="p0875173217307"></a>Volume type [SSD] in availability zone [AZ1] is sold out !</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p58751632143015"><a name="p58751632143015"></a><a name="p58751632143015"></a>Select another disk type or contact <span id="text2024112841918"><a name="text2024112841918"></a><a name="text2024112841918"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row167010282171"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1999934013170"><a name="p1999934013170"></a><a name="p1999934013170"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p129995408174"><a name="p129995408174"></a><a name="p129995408174"></a>EVS.2078</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p49990401176"><a name="p49990401176"></a><a name="p49990401176"></a>Request conversion error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p119991840111716"><a name="p119991840111716"></a><a name="p119991840111716"></a>checkQuotaCapacity request body is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p119991440131719"><a name="p119991440131719"></a><a name="p119991440131719"></a>Check whether the request body is empty.</p>
</td>
</tr>
<tr id="row271132861719"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p15999194071716"><a name="p15999194071716"></a><a name="p15999194071716"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p699911401174"><a name="p699911401174"></a><a name="p699911401174"></a>EVS.2083</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p39991408173"><a name="p39991408173"></a><a name="p39991408173"></a>The AZ or disk type parameter in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p209991640201715"><a name="p209991640201715"></a><a name="p209991640201715"></a>AZ and volume type must not be empty or null!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p599994013178"><a name="p599994013178"></a><a name="p599994013178"></a>Ensure that the input AZ and disk type parameters are correct.</p>
</td>
</tr>
<tr id="row9711289170"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p14999240171718"><a name="p14999240171718"></a><a name="p14999240171718"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p199991840191719"><a name="p199991840191719"></a><a name="p199991840191719"></a>EVS.2084</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p999934010179"><a name="p999934010179"></a><a name="p999934010179"></a>The disk size parameter in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1999994021710"><a name="p1999994021710"></a><a name="p1999994021710"></a>resource size must greater than zero!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p4999340191712"><a name="p4999340191712"></a><a name="p4999340191712"></a>Check whether the disk size specified in the request body is correct.</p>
</td>
</tr>
<tr id="row4711128151710"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p100124131714"><a name="p100124131714"></a><a name="p100124131714"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p11014412172"><a name="p11014412172"></a><a name="p11014412172"></a>EVS.2085</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p130204119170"><a name="p130204119170"></a><a name="p130204119170"></a>The disk ID is invalid during expansion.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1101741101717"><a name="p1101741101717"></a><a name="p1101741101717"></a>when operation type is SPEC_CHG, resource id must not be empty or null!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p200741181715"><a name="p200741181715"></a><a name="p200741181715"></a>Check whether the disk ID specified in the request body is correct.</p>
</td>
</tr>
<tr id="row1071172812179"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p90114151716"><a name="p90114151716"></a><a name="p90114151716"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p601741201716"><a name="p601741201716"></a><a name="p601741201716"></a>EVS.2087</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1501441161718"><a name="p1501441161718"></a><a name="p1501441161718"></a>Invalid request parameter.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p13034112173"><a name="p13034112173"></a><a name="p13034112173"></a>retype failed. please make sure that type is supported and the new one is higher then origin</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p7018418173"><a name="p7018418173"></a><a name="p7018418173"></a>Ensure that the new type has higher specifications than the old type.</p>
</td>
</tr>
<tr id="row1171112814175"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p170154111170"><a name="p170154111170"></a><a name="p170154111170"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p30104115177"><a name="p30104115177"></a><a name="p30104115177"></a>EVS.2089</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1101841181716"><a name="p1101841181716"></a><a name="p1101841181716"></a>The disk is used by the SDRS service.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p17044117177"><a name="p17044117177"></a><a name="p17044117177"></a>operation failed because the volume is belong to SDRS</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p70114116171"><a name="p70114116171"></a><a name="p70114116171"></a>Free the disk from SDRS or select another disk.</p>
</td>
</tr>
<tr id="row17763923191718"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p901241171712"><a name="p901241171712"></a><a name="p901241171712"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1084191719"><a name="p1084191719"></a><a name="p1084191719"></a>EVS.2093</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p902412171"><a name="p902412171"></a><a name="p902412171"></a>The disk is not an EVS disk.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p7015412175"><a name="p7015412175"></a><a name="p7015412175"></a>operation failed because the volume is not EVS</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p201341181715"><a name="p201341181715"></a><a name="p201341181715"></a>This operation cannot be performed because the disk is not an EVS disk.</p>
</td>
</tr>
<tr id="row10764182318178"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p701841141715"><a name="p701841141715"></a><a name="p701841141715"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p90341171715"><a name="p90341171715"></a><a name="p90341171715"></a>EVS.2094</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p30241101719"><a name="p30241101719"></a><a name="p30241101719"></a>A shared disk cannot be created from a system disk image.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1901141181716"><a name="p1901141181716"></a><a name="p1901141181716"></a>system image is not support to create  Multiattach/shareable volume !</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p15084191716"><a name="p15084191716"></a><a name="p15084191716"></a>A shared disk cannot be created from a system disk image.</p>
</td>
</tr>
<tr id="row6764152391710"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p20141111711"><a name="p20141111711"></a><a name="p20141111711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p30941111710"><a name="p30941111710"></a><a name="p30941111710"></a>EVS.2096</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p150104181710"><a name="p150104181710"></a><a name="p150104181710"></a>When a disk is created from a snapshot, the disk type of the snapshot's source disk is inconsistent with that of the new disk.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p0004191710"><a name="p0004191710"></a><a name="p0004191710"></a>Target volumeType[%s] is not matched with snapshot[%s] !</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p190154181716"><a name="p190154181716"></a><a name="p190154181716"></a>Ensure that the disk type of the snapshot's source disk is consistent with that of the new disk.</p>
</td>
</tr>
<tr id="row1412247112717"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p16155824297"><a name="p16155824297"></a><a name="p16155824297"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p415516215292"><a name="p415516215292"></a><a name="p415516215292"></a>EVS.2105</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p61552028296"><a name="p61552028296"></a><a name="p61552028296"></a>The ID of the CMK used to encrypt the disk does not exist, or has been deleted and cannot be restored.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p91551128297"><a name="p91551128297"></a><a name="p91551128297"></a>Volume can not be reverted, because the encrypt volume's __system__cmkid is not exist!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p815512220294"><a name="p815512220294"></a><a name="p815512220294"></a>Contact <span id="text341331019196"><a name="text341331019196"></a><a name="text341331019196"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row15141135572712"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1315519262918"><a name="p1315519262918"></a><a name="p1315519262918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p11155727295"><a name="p11155727295"></a><a name="p11155727295"></a>EVS.2108</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p715515212290"><a name="p715515212290"></a><a name="p715515212290"></a>Request conversion error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p14155324296"><a name="p14155324296"></a><a name="p14155324296"></a>Request body is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p71551223298"><a name="p71551223298"></a><a name="p71551223298"></a>Check whether the request body is correct.</p>
</td>
</tr>
<tr id="row141455218281"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p815642162916"><a name="p815642162916"></a><a name="p815642162916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p19156132192912"><a name="p19156132192912"></a><a name="p19156132192912"></a>EVS.2130</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p81561721299"><a name="p81561721299"></a><a name="p81561721299"></a>Failed to delete the disk because the snapshot is in the <strong id="b179395265566"><a name="b179395265566"></a><a name="b179395265566"></a>backing-up</strong> state when a disk backup is being created.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p11156192112910"><a name="p11156192112910"></a><a name="p11156192112910"></a>Volume is backing-up, forbidden deleting!</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p51564213293"><a name="p51564213293"></a><a name="p51564213293"></a>Wait until the backup is created or contact <span id="text728031291915"><a name="text728031291915"></a><a name="text728031291915"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row1241419524287"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1315613272916"><a name="p1315613272916"></a><a name="p1315613272916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1715618202911"><a name="p1715618202911"></a><a name="p1715618202911"></a>EVS.2131</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p8156102192919"><a name="p8156102192919"></a><a name="p8156102192919"></a>Failed to query the server details.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p515652142917"><a name="p515652142917"></a><a name="p515652142917"></a>Query server info from ecs fail</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p121569219296"><a name="p121569219296"></a><a name="p121569219296"></a>Try again later or contact <span id="text123511514191919"><a name="text123511514191919"></a><a name="text123511514191919"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row15142125512718"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p61566202916"><a name="p61566202916"></a><a name="p61566202916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p315762142912"><a name="p315762142912"></a><a name="p315762142912"></a>EVS.2134</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p16157182102913"><a name="p16157182102913"></a><a name="p16157182102913"></a>Failed to attach the disk.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p91577211298"><a name="p91577211298"></a><a name="p91577211298"></a>call ecs api - attach volume fail.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p161577210297"><a name="p161577210297"></a><a name="p161577210297"></a>Try again later or contact <span id="text1143111831911"><a name="text1143111831911"></a><a name="text1143111831911"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row64861275287"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p9157192192914"><a name="p9157192192914"></a><a name="p9157192192914"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p191571282911"><a name="p191571282911"></a><a name="p191571282911"></a>EVS.2142</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p12157227295"><a name="p12157227295"></a><a name="p12157227295"></a>Request parameter <strong id="b1485560175912"><a name="b1485560175912"></a><a name="b1485560175912"></a>limit</strong> cannot be greater than <strong id="b224612115915"><a name="b224612115915"></a><a name="b224612115915"></a>1000</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p19157122297"><a name="p19157122297"></a><a name="p19157122297"></a>invalid filter limit, can not greater than 1000.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p10157192122917"><a name="p10157192122917"></a><a name="p10157192122917"></a>Ensure that the <strong id="b5495322145912"><a name="b5495322145912"></a><a name="b5495322145912"></a>limit</strong> value ranges from <strong id="b649617225599"><a name="b649617225599"></a><a name="b649617225599"></a>1</strong> to <strong id="b124961225592"><a name="b124961225592"></a><a name="b124961225592"></a>1000</strong>. The default value is <strong id="b7497132275920"><a name="b7497132275920"></a><a name="b7497132275920"></a>1000</strong>.</p>
</td>
</tr>
<tr id="row4486627192812"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p18157172172914"><a name="p18157172172914"></a><a name="p18157172172914"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p41571529297"><a name="p41571529297"></a><a name="p41571529297"></a>EVS.2143</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p141571212298"><a name="p141571212298"></a><a name="p141571212298"></a>The account does not have the encryption permission.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p815772162919"><a name="p815772162919"></a><a name="p815772162919"></a>You need to create an agency for this project for the first time ever</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p2015717252911"><a name="p2015717252911"></a><a name="p2015717252911"></a>Create an agency.</p>
</td>
</tr>
<tr id="row115884211491"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p48771732113013"><a name="p48771732113013"></a><a name="p48771732113013"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1187733213018"><a name="p1187733213018"></a><a name="p1187733213018"></a>EVS.2144</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p128775326305"><a name="p128775326305"></a><a name="p128775326305"></a>Insufficient permission because the account is frozen.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p88778326302"><a name="p88778326302"></a><a name="p88778326302"></a>Your account is frozen and resources cannot be used.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><div class="p" id="p1487773210304"><a name="p1487773210304"></a><a name="p1487773210304"></a>Check whether either of the following conditions exists: (If no such condition exists, contact <span id="text117037203192"><a name="text117037203192"></a><a name="text117037203192"></a>customer service</span>.)<a name="ul17877632113013"></a><a name="ul17877632113013"></a><ul id="ul17877632113013"><li>The account does not pass real-name authentication.</li><li>The account is in arrears.</li></ul>
</div>
</td>
</tr>
<tr id="row19588621124915"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p0878532133016"><a name="p0878532133016"></a><a name="p0878532133016"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p587883215306"><a name="p587883215306"></a><a name="p587883215306"></a>EVS.2145</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p387823220303"><a name="p387823220303"></a><a name="p387823220303"></a>Insufficient permission because the account is suspended.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p16878143217302"><a name="p16878143217302"></a><a name="p16878143217302"></a>Your account is suspended and resources cannot be used.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><div class="p" id="p587814329301"><a name="p587814329301"></a><a name="p587814329301"></a>Check whether any of the following conditions exists: (If no such condition exists, contact <span id="text1886453416199"><a name="text1886453416199"></a><a name="text1886453416199"></a>customer service</span>.)<a name="ul13878832163014"></a><a name="ul13878832163014"></a><ul id="ul13878832163014"><li>The account payment method is not complete.</li><li>The account does not pass real-name authentication.</li><li>The account is in arrears.</li></ul>
</div>
</td>
</tr>
<tr id="row19863163213302"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p168631732113010"><a name="p168631732113010"></a><a name="p168631732113010"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p586313243015"><a name="p586313243015"></a><a name="p586313243015"></a>EVS.5400</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p20863123219308"><a name="p20863123219308"></a><a name="p20863123219308"></a>Incorrect request body parameter and format.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1863103217309"><a name="p1863103217309"></a><a name="p1863103217309"></a>Malformed request body.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p19863432133020"><a name="p19863432133020"></a><a name="p19863432133020"></a>Check whether the parameters and format of the request body are correct.</p>
</td>
</tr>
<tr id="row986315324307"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1286353293012"><a name="p1286353293012"></a><a name="p1286353293012"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p686315322304"><a name="p686315322304"></a><a name="p686315322304"></a>EVS.5400</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p0863132153017"><a name="p0863132153017"></a><a name="p0863132153017"></a>Incorrect request URL parameter and format.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p386413293015"><a name="p386413293015"></a><a name="p386413293015"></a>Malformed request url.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p148641832133019"><a name="p148641832133019"></a><a name="p148641832133019"></a>Check whether the parameters and format of the request URL are correct.</p>
</td>
</tr>
<tr id="row118643329300"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1386463223013"><a name="p1386463223013"></a><a name="p1386463223013"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p586420326302"><a name="p586420326302"></a><a name="p586420326302"></a>EVS.5400</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p38642322301"><a name="p38642322301"></a><a name="p38642322301"></a>Request body and URI mismatch.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p7864133217305"><a name="p7864133217305"></a><a name="p7864133217305"></a>Request body and URI mismatch.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p58641232113020"><a name="p58641232113020"></a><a name="p58641232113020"></a>Check whether the request body and URI belong to the same API.</p>
</td>
</tr>
<tr id="row148641532173011"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p20864132163019"><a name="p20864132163019"></a><a name="p20864132163019"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p086463233012"><a name="p086463233012"></a><a name="p086463233012"></a>EVS.5400</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1586513327307"><a name="p1586513327307"></a><a name="p1586513327307"></a>The image is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p178651232163018"><a name="p178651232163018"></a><a name="p178651232163018"></a>Invalid imageRef provided.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1286593217304"><a name="p1286593217304"></a><a name="p1286593217304"></a>Select another image.</p>
</td>
</tr>
<tr id="row1086533220304"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p28651632173013"><a name="p28651632173013"></a><a name="p28651632173013"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p68659324309"><a name="p68659324309"></a><a name="p68659324309"></a>EVS.5400</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p158651532133020"><a name="p158651532133020"></a><a name="p158651532133020"></a>The disk status is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p12865163293014"><a name="p12865163293014"></a><a name="p12865163293014"></a>Must specify a valid status.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p286515325307"><a name="p286515325307"></a><a name="p286515325307"></a>Specify a disk that is in the correct state.</p>
</td>
</tr>
<tr id="row18651032173017"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p148652328307"><a name="p148652328307"></a><a name="p148652328307"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p108651032153016"><a name="p108651032153016"></a><a name="p108651032153016"></a>EVS.5400</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p4865032163012"><a name="p4865032163012"></a><a name="p4865032163012"></a>The value of parameter <strong id="b842352706143734"><a name="b842352706143734"></a><a name="b842352706143734"></a>offset</strong> must be an integer.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p28650322308"><a name="p28650322308"></a><a name="p28650322308"></a>offset param must be an integer.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1386573219301"><a name="p1386573219301"></a><a name="p1386573219301"></a>Set the value of parameter <strong id="b885552902"><a name="b885552902"></a><a name="b885552902"></a>offset</strong> to an integer.</p>
</td>
</tr>
<tr id="row486613321302"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p13866113223012"><a name="p13866113223012"></a><a name="p13866113223012"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p17866232103010"><a name="p17866232103010"></a><a name="p17866232103010"></a>EVS.5400</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p148661032123011"><a name="p148661032123011"></a><a name="p148661032123011"></a>The value of parameter <strong id="b971091200"><a name="b971091200"></a><a name="b971091200"></a>limit</strong> must be set to an integer.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p186683263013"><a name="p186683263013"></a><a name="p186683263013"></a>limit param must be an integer.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p11866123219301"><a name="p11866123219301"></a><a name="p11866123219301"></a>Set the value of parameter <strong id="b1991258471"><a name="b1991258471"></a><a name="b1991258471"></a>limit</strong> to an integer.</p>
</td>
</tr>
<tr id="row1186612328307"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p4866632193012"><a name="p4866632193012"></a><a name="p4866632193012"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p138661632173018"><a name="p138661632173018"></a><a name="p138661632173018"></a>EVS.5400</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p2086683218308"><a name="p2086683218308"></a><a name="p2086683218308"></a>The value of parameter <strong id="b1835870016"><a name="b1835870016"></a><a name="b1835870016"></a>limit</strong> must be a positive number.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p58663327308"><a name="p58663327308"></a><a name="p58663327308"></a>limit param must be positive.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1286618328305"><a name="p1286618328305"></a><a name="p1286618328305"></a>Ensure that the <strong id="b164971505219"><a name="b164971505219"></a><a name="b164971505219"></a>limit</strong> value is an integer ranging from <strong id="b749915015214"><a name="b749915015214"></a><a name="b749915015214"></a>1</strong> to <strong id="b950118016215"><a name="b950118016215"></a><a name="b950118016215"></a>1000</strong>. The default value is <strong id="b1850290729"><a name="b1850290729"></a><a name="b1850290729"></a>1000</strong>.</p>
</td>
</tr>
<tr id="row1887533243013"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1987543203019"><a name="p1987543203019"></a><a name="p1987543203019"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p12875632173016"><a name="p12875632173016"></a><a name="p12875632173016"></a>EVS.5401</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p18875432173019"><a name="p18875432173019"></a><a name="p18875432173019"></a>This operation is unauthorized.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1876193218308"><a name="p1876193218308"></a><a name="p1876193218308"></a>Authentication required.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p787663213014"><a name="p787663213014"></a><a name="p787663213014"></a>Call the API after authorization.</p>
</td>
</tr>
<tr id="row1587617329308"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p188761432123012"><a name="p188761432123012"></a><a name="p188761432123012"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p2876143243012"><a name="p2876143243012"></a><a name="p2876143243012"></a>EVS.5403</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p68762032133013"><a name="p68762032133013"></a><a name="p68762032133013"></a>Insufficient permission.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p11876123233011"><a name="p11876123233011"></a><a name="p11876123233011"></a>Policy check failed.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1087683218304"><a name="p1087683218304"></a><a name="p1087683218304"></a>Add the permission and try again.</p>
</td>
</tr>
<tr id="row14876832133016"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p0876932183013"><a name="p0876932183013"></a><a name="p0876932183013"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1087611325307"><a name="p1087611325307"></a><a name="p1087611325307"></a>EVS.5403</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p58771032123014"><a name="p58771032123014"></a><a name="p58771032123014"></a>No operation permission.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p10877103233012"><a name="p10877103233012"></a><a name="p10877103233012"></a>metadata can not be operated.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p2087733223010"><a name="p2087733223010"></a><a name="p2087733223010"></a>Modifying parameter <strong id="b842352706144357"><a name="b842352706144357"></a><a name="b842352706144357"></a>metadata</strong> is forbidden.</p>
</td>
</tr>
<tr id="row14878183263018"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p0879173217307"><a name="p0879173217307"></a><a name="p0879173217307"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p13879173213303"><a name="p13879173213303"></a><a name="p13879173213303"></a>EVS.5404</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p4879123215302"><a name="p4879123215302"></a><a name="p4879123215302"></a>Resources, such as the disk, snapshot, and backup, do not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p1087953213016"><a name="p1087953213016"></a><a name="p1087953213016"></a>Resource(Volume, Snapshot, Backup .etc) cound not be found.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p9879103223018"><a name="p9879103223018"></a><a name="p9879103223018"></a>Check whether the resources are available.</p>
</td>
</tr>
<tr id="row987912325304"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p10879173210305"><a name="p10879173210305"></a><a name="p10879173210305"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p38791432183018"><a name="p38791432183018"></a><a name="p38791432183018"></a>EVS.5413</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1879532183015"><a name="p1879532183015"></a><a name="p1879532183015"></a>Insufficient disk quotas.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p28791932173011"><a name="p28791932173011"></a><a name="p28791932173011"></a>Insufficient volume quota.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p387915328309"><a name="p387915328309"></a><a name="p387915328309"></a>Check whether the disk capacity and quantity quotas are sufficient.</p>
</td>
</tr>
<tr id="row198807325306"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p5880932193010"><a name="p5880932193010"></a><a name="p5880932193010"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p168801732183012"><a name="p168801732183012"></a><a name="p168801732183012"></a>EVS.5500</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p7880193213012"><a name="p7880193213012"></a><a name="p7880193213012"></a>Internal server error.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p988011322301"><a name="p988011322301"></a><a name="p988011322301"></a>Internal server error.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1388033223019"><a name="p1388033223019"></a><a name="p1388033223019"></a>Try again later or contact <span id="text13928184014198"><a name="text13928184014198"></a><a name="text13928184014198"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row1188033216309"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p7880193219308"><a name="p7880193219308"></a><a name="p7880193219308"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p118800324306"><a name="p118800324306"></a><a name="p118800324306"></a>EVS.5503</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p11880832193015"><a name="p11880832193015"></a><a name="p11880832193015"></a>The service is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p11881732183019"><a name="p11881732183019"></a><a name="p11881732183019"></a>Service unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1088111322309"><a name="p1088111322309"></a><a name="p1088111322309"></a>Try again later or contact <span id="text364544217198"><a name="text364544217198"></a><a name="text364544217198"></a>customer service</span>.</p>
</td>
</tr>
<tr id="row0374175816498"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p1484419325303"><a name="p1484419325303"></a><a name="p1484419325303"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1484410329308"><a name="p1484410329308"></a><a name="p1484410329308"></a>Common.0011</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p1084512327309"><a name="p1084512327309"></a><a name="p1084512327309"></a>Incorrect tenant ID. <span id="text209641127105819"><a name="text209641127105819"></a><a name="text209641127105819"></a>The tenant ID is actually the project ID.</span></p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p18845532113020"><a name="p18845532113020"></a><a name="p18845532113020"></a>query job fail.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p10845153293010"><a name="p10845153293010"></a><a name="p10845153293010"></a>Use the correct tenant ID and ensure that the tenant has desired permissions. <span id="text2446173755812"><a name="text2446173755812"></a><a name="text2446173755812"></a>The tenant ID is actually the project ID.</span></p>
</td>
</tr>
<tr id="row1537455814495"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p484520322304"><a name="p484520322304"></a><a name="p484520322304"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p12845143283018"><a name="p12845143283018"></a><a name="p12845143283018"></a>Common.0011</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p6845183218309"><a name="p6845183218309"></a><a name="p6845183218309"></a><strong id="b84235270617337"><a name="b84235270617337"></a><a name="b84235270617337"></a>jobId</strong> is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p884515323304"><a name="p884515323304"></a><a name="p884515323304"></a>No jobs found.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p1284520320309"><a name="p1284520320309"></a><a name="p1284520320309"></a>Enter the correct <strong id="b138921584920831"><a name="b138921584920831"></a><a name="b138921584920831"></a>jobId</strong> value.</p>
</td>
</tr>
<tr id="row1037575817491"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p13845332103017"><a name="p13845332103017"></a><a name="p13845332103017"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p8845163283015"><a name="p8845163283015"></a><a name="p8845163283015"></a>Common.0011</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p284583223013"><a name="p284583223013"></a><a name="p284583223013"></a>Failed to query JobVO using <strong id="b8423527061745"><a name="b8423527061745"></a><a name="b8423527061745"></a>jobId</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p384563217301"><a name="p384563217301"></a><a name="p384563217301"></a>query job fail.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p10845113210302"><a name="p10845113210302"></a><a name="p10845113210302"></a>Check whether the <strong id="b1458961553191538"><a name="b1458961553191538"></a><a name="b1458961553191538"></a>jobId</strong> value is correct. If the <strong id="b514076150191543"><a name="b514076150191543"></a><a name="b514076150191543"></a>jobId</strong> value is correct, check whether the request is delivered to the target EVS service node. If the request has been delivered, contact <span id="text84085469193"><a name="text84085469193"></a><a name="text84085469193"></a>customer service</span> to locate the fault. If the request has not been delivered, contact <span id="text786105517193"><a name="text786105517193"></a><a name="text786105517193"></a>customer service</span> to deliver the request to the target EVS service node.</p>
</td>
</tr>
<tr id="row167471225121318"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p874842521319"><a name="p874842521319"></a><a name="p874842521319"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p1674852511137"><a name="p1674852511137"></a><a name="p1674852511137"></a>Common.0013</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p07487254138"><a name="p07487254138"></a><a name="p07487254138"></a>Failed to parse the token because the token expires or the token string is incomplete.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p18748102561314"><a name="p18748102561314"></a><a name="p18748102561314"></a>Invalid token in the header.</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p77481725101319"><a name="p77481725101319"></a><a name="p77481725101319"></a>Obtain the token again and ensure that the token string is complete.</p>
</td>
</tr>
<tr id="row16596301882"><td class="cellrowborder" valign="top" width="11.353535353535353%" headers="mcps1.1.6.1.1 "><p id="p3660130987"><a name="p3660130987"></a><a name="p3660130987"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.1.6.1.2 "><p id="p18660173015810"><a name="p18660173015810"></a><a name="p18660173015810"></a>Common.0018</p>
</td>
<td class="cellrowborder" valign="top" width="21.29292929292929%" headers="mcps1.1.6.1.3 "><p id="p866014302083"><a name="p866014302083"></a><a name="p866014302083"></a>The project ID in the URI is different from the project ID in the token.</p>
</td>
<td class="cellrowborder" valign="top" width="23.303030303030305%" headers="mcps1.1.6.1.4 "><p id="p666011301581"><a name="p666011301581"></a><a name="p666011301581"></a>Invalid token in the header</p>
</td>
<td class="cellrowborder" valign="top" width="27.737373737373737%" headers="mcps1.1.6.1.5 "><p id="p116604301182"><a name="p116604301182"></a><a name="p116604301182"></a>Ensure that the project ID in the URI is the same as that in the token and try again.</p>
</td>
</tr>
</tbody>
</table>

