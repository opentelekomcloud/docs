# Key Operations on SWR<a name="cts_0827"></a>

Software Repository for Container \(SWR\) provides easy, secure, and reliable management of container images throughout their lifecycles, facilitating quick deployment of containerized services.

With CTS, you can record operations associated with SWR for future query, audit, and backtrack operations.

**Table  1**  SWR operations that can be recorded by CTS

<a name="table123236101120"></a>
<table><thead align="left"><tr id="row32363691118"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p18233366115"><a name="p18233366115"></a><a name="p18233366115"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1233367115"><a name="p1233367115"></a><a name="p1233367115"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p52323691111"><a name="p52323691111"></a><a name="p52323691111"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="row182383611111"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16955715492"><a name="p16955715492"></a><a name="p16955715492"></a>Creating an image repository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p659722474912"><a name="p659722474912"></a><a name="p659722474912"></a>imagerepository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18277184014919"><a name="p18277184014919"></a><a name="p18277184014919"></a>createImageRepository</p>
</td>
</tr>
<tr id="row1023173611119"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10695157134915"><a name="p10695157134915"></a><a name="p10695157134915"></a>Modifying an image repository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p35971924134917"><a name="p35971924134917"></a><a name="p35971924134917"></a>imagerepository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p627714084919"><a name="p627714084919"></a><a name="p627714084919"></a>updateImageRepository</p>
</td>
</tr>
<tr id="row13249365117"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p769567164916"><a name="p769567164916"></a><a name="p769567164916"></a>Deleting an image repository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p155971024144920"><a name="p155971024144920"></a><a name="p155971024144920"></a>imagerepository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1827864010494"><a name="p1827864010494"></a><a name="p1827864010494"></a>deleteImageRepository</p>
</td>
</tr>
<tr id="row172473610111"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8695576490"><a name="p8695576490"></a><a name="p8695576490"></a>Uploading an image package</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p105976243497"><a name="p105976243497"></a><a name="p105976243497"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8278124064918"><a name="p8278124064918"></a><a name="p8278124064918"></a>uploadImagePackage</p>
</td>
</tr>
<tr id="row02443618115"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p86954720495"><a name="p86954720495"></a><a name="p86954720495"></a>Deleting an image tag</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p13597172412498"><a name="p13597172412498"></a><a name="p13597172412498"></a>imagetag</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11278124034916"><a name="p11278124034916"></a><a name="p11278124034916"></a>deleteImageTag</p>
</td>
</tr>
<tr id="row1724123616114"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p186951712497"><a name="p186951712497"></a><a name="p186951712497"></a>Granting permissions for an image repository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p105971324174910"><a name="p105971324174910"></a><a name="p105971324174910"></a>userrepositoryauth</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1127816408499"><a name="p1127816408499"></a><a name="p1127816408499"></a>createUserRepositoryAuth</p>
</td>
</tr>
<tr id="row95383721914"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5695670490"><a name="p5695670490"></a><a name="p5695670490"></a>Modifying permissions for an image repository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55985247493"><a name="p55985247493"></a><a name="p55985247493"></a>userrepositoryauth</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p122781940144919"><a name="p122781940144919"></a><a name="p122781940144919"></a>updateUserRepositoryAuth</p>
</td>
</tr>
<tr id="row188251051918"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p186952711497"><a name="p186952711497"></a><a name="p186952711497"></a>Deleting permissions for an image repository</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1059822434913"><a name="p1059822434913"></a><a name="p1059822434913"></a>userrepositoryauth</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1627874084917"><a name="p1627874084917"></a><a name="p1627874084917"></a>deleteUserRepositoryAuth</p>
</td>
</tr>
<tr id="row18709435198"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1569517720495"><a name="p1569517720495"></a><a name="p1569517720495"></a>Creating an organization</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1259882414495"><a name="p1259882414495"></a><a name="p1259882414495"></a>usernamespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7278144064910"><a name="p7278144064910"></a><a name="p7278144064910"></a>createUserNamespace</p>
</td>
</tr>
<tr id="row18782144531911"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p769510717491"><a name="p769510717491"></a><a name="p769510717491"></a>Deleting an organization</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p05989247490"><a name="p05989247490"></a><a name="p05989247490"></a>usernamespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p32786400498"><a name="p32786400498"></a><a name="p32786400498"></a>deleteUserNamesapce</p>
</td>
</tr>
<tr id="row2252194914198"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p96950717491"><a name="p96950717491"></a><a name="p96950717491"></a>Granting permissions for an organization</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p659852411492"><a name="p659852411492"></a><a name="p659852411492"></a>usernamespaceauth</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p132781640174919"><a name="p132781640174919"></a><a name="p132781640174919"></a>createUserNamespaceAuth</p>
</td>
</tr>
<tr id="row6793145118192"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18695774498"><a name="p18695774498"></a><a name="p18695774498"></a>Modifying permissions for an organization</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1959817247495"><a name="p1959817247495"></a><a name="p1959817247495"></a>usernamespaceauth</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1227884020495"><a name="p1227884020495"></a><a name="p1227884020495"></a>updateUserNamespaceAuth</p>
</td>
</tr>
<tr id="row1445115431919"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1169610718495"><a name="p1169610718495"></a><a name="p1169610718495"></a>Deleting permissions for an organization</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45981424204920"><a name="p45981424204920"></a><a name="p45981424204920"></a>usernamespaceauth</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8278114011498"><a name="p8278114011498"></a><a name="p8278114011498"></a>deleteUserNamespaceAuth</p>
</td>
</tr>
<tr id="row1073817573193"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p146965715497"><a name="p146965715497"></a><a name="p146965715497"></a>Generating login command</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1459872444912"><a name="p1459872444912"></a><a name="p1459872444912"></a>dockerlogincmd</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18278194004910"><a name="p18278194004910"></a><a name="p18278194004910"></a>createDockerConfig</p>
</td>
</tr>
</tbody>
</table>

