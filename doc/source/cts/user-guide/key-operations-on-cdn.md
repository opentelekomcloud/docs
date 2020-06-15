# Key Operations on CDN<a name="en-us_topic_0128329663"></a>

Content Delivery Network \(CDN\) is an intelligent virtual network layer based on the existing Internet infrastructure. It delivers network content from origin servers to edge node servers distributed across a country, enabling end users to obtain desired content from the proximal node.

With CTS, you can record operations associated with CDN for later query, audit, and backtrack operations.

>![](/images/icon-note.gif) **NOTE:**   
>CDN is a Global service and CDN traces are only displayed in the central Region of the current site.  

**Table  1**  CDN operations that can be recorded by CTS

<a name="table49034461175736"></a>
<table><thead align="left"><tr id="r850cd323ae874970b9f4bb2c9e8b1fb3"><th class="cellrowborder" valign="top" width="31.630000000000003%" id="mcps1.2.4.1.1"><p id="aa4c26b5581cc46a3beb1c040d4005d13"><a name="aa4c26b5581cc46a3beb1c040d4005d13"></a><a name="aa4c26b5581cc46a3beb1c040d4005d13"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.59%" id="mcps1.2.4.1.2"><p id="a8f5b1bc05a4f48c19dce85bb82bf531e"><a name="a8f5b1bc05a4f48c19dce85bb82bf531e"></a><a name="a8f5b1bc05a4f48c19dce85bb82bf531e"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.78%" id="mcps1.2.4.1.3"><p id="a2dce7591f663405ba573ddf09233aa6b"><a name="a2dce7591f663405ba573ddf09233aa6b"></a><a name="a2dce7591f663405ba573ddf09233aa6b"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="re31200c810c645e6a9a2a4ff40202569"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="acce3abfd23644d1cb7cb6319280c19ae"><a name="acce3abfd23644d1cb7cb6319280c19ae"></a><a name="acce3abfd23644d1cb7cb6319280c19ae"></a>Creating an acceleration domain name</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a0eaee9f7409146cd849cda8c66a34f94"><a name="a0eaee9f7409146cd849cda8c66a34f94"></a><a name="a0eaee9f7409146cd849cda8c66a34f94"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="aefe5fcc0aedc4c44af93401155a9949d"><a name="aefe5fcc0aedc4c44af93401155a9949d"></a><a name="aefe5fcc0aedc4c44af93401155a9949d"></a>createDomain</p>
</td>
</tr>
<tr id="r99c444e4c6f5428c9aefc0e7472fc429"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a6f8d0d43a1844a01b834346458844b09"><a name="a6f8d0d43a1844a01b834346458844b09"></a><a name="a6f8d0d43a1844a01b834346458844b09"></a>Updating an acceleration domain name</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a506930769a8b47d1864b92eb2f0c3d18"><a name="a506930769a8b47d1864b92eb2f0c3d18"></a><a name="a506930769a8b47d1864b92eb2f0c3d18"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a88bbd1fb447a4613909974c1e6ec12df"><a name="a88bbd1fb447a4613909974c1e6ec12df"></a><a name="a88bbd1fb447a4613909974c1e6ec12df"></a>updateDomain</p>
</td>
</tr>
<tr id="r282aa9483e95445587f1266d58cdb4b4"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="af3850fc2e1dc43a78f7539ada41b64da"><a name="af3850fc2e1dc43a78f7539ada41b64da"></a><a name="af3850fc2e1dc43a78f7539ada41b64da"></a>Deleting an acceleration domain name</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a9caeef52037d4ca68694465c6186d5fb"><a name="a9caeef52037d4ca68694465c6186d5fb"></a><a name="a9caeef52037d4ca68694465c6186d5fb"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p732644318052"><a name="en-us_topic_0100240354_p732644318052"></a><a name="en-us_topic_0100240354_p732644318052"></a>deleteDomain</p>
</td>
</tr>
<tr id="r4d6e4680bef448a8bfc2fffd20cace39"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p700575218027"><a name="en-us_topic_0100240354_p700575218027"></a><a name="en-us_topic_0100240354_p700575218027"></a>Enabling an acceleration domain name</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="aefc3fcbf090a41888f4472cd413a21c9"><a name="aefc3fcbf090a41888f4472cd413a21c9"></a><a name="aefc3fcbf090a41888f4472cd413a21c9"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a2541ce5545fa4957af053f717ebbb2d9"><a name="a2541ce5545fa4957af053f717ebbb2d9"></a><a name="a2541ce5545fa4957af053f717ebbb2d9"></a>enableDomain</p>
</td>
</tr>
<tr id="ra429512d920b4815ad11f78539d6419d"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p692013718027"><a name="en-us_topic_0100240354_p692013718027"></a><a name="en-us_topic_0100240354_p692013718027"></a>Disabling an acceleration domain name</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="aaedf5ce4355a41c49c8fb2d51d230edd"><a name="aaedf5ce4355a41c49c8fb2d51d230edd"></a><a name="aaedf5ce4355a41c49c8fb2d51d230edd"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a69016cecd5ab4f1db8ba00aea11d037c"><a name="a69016cecd5ab4f1db8ba00aea11d037c"></a><a name="a69016cecd5ab4f1db8ba00aea11d037c"></a>disableDomain</p>
</td>
</tr>
<tr id="refb8de1628a443dc9ffa5e113d8e93e5"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a1389b85fc56a4435b73feaf32233185a"><a name="a1389b85fc56a4435b73feaf32233185a"></a><a name="a1389b85fc56a4435b73feaf32233185a"></a>Configuring a retrieval host</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a365daf240c3141799dfb0b8f444db67d"><a name="a365daf240c3141799dfb0b8f444db67d"></a><a name="a365daf240c3141799dfb0b8f444db67d"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a6892978c3a764f9ea899874b50e10b9c"><a name="a6892978c3a764f9ea899874b50e10b9c"></a><a name="a6892978c3a764f9ea899874b50e10b9c"></a>updateOriginHost</p>
</td>
</tr>
<tr id="r9b72025f0230429c82fcad6afc99b408"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a2cc9d792a7af4507a7c96cab8e6b6d0b"><a name="a2cc9d792a7af4507a7c96cab8e6b6d0b"></a><a name="a2cc9d792a7af4507a7c96cab8e6b6d0b"></a>Creating a Referer rule</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a44e86253e8134d66a1862e259aa69cac"><a name="a44e86253e8134d66a1862e259aa69cac"></a><a name="a44e86253e8134d66a1862e259aa69cac"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="ad5503a784d804725a40312a224c8c07a"><a name="ad5503a784d804725a40312a224c8c07a"></a><a name="ad5503a784d804725a40312a224c8c07a"></a>createRefer</p>
</td>
</tr>
<tr id="r225dfcb5a84b4e89a280a013d34c54a5"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p242375518027"><a name="en-us_topic_0100240354_p242375518027"></a><a name="en-us_topic_0100240354_p242375518027"></a>Configuring an acceleration domain name certificate</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a7bdbe37eaa6a4a3c8f459bc90423412f"><a name="a7bdbe37eaa6a4a3c8f459bc90423412f"></a><a name="a7bdbe37eaa6a4a3c8f459bc90423412f"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a5c847f049bcf4d40b26060f845ed3fd8"><a name="a5c847f049bcf4d40b26060f845ed3fd8"></a><a name="a5c847f049bcf4d40b26060f845ed3fd8"></a>createCertificate</p>
</td>
</tr>
<tr id="rf657e7801b3f486caad28bb55f9b91c5"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="aafd567e4de5f43b5b09f47386ccd13cb"><a name="aafd567e4de5f43b5b09f47386ccd13cb"></a><a name="aafd567e4de5f43b5b09f47386ccd13cb"></a>Creating a cache rule</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a91421d4a18684e79bde8b66ffbeaf2bb"><a name="a91421d4a18684e79bde8b66ffbeaf2bb"></a><a name="a91421d4a18684e79bde8b66ffbeaf2bb"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a185be9c811954d069bd1caf614ca6c30"><a name="a185be9c811954d069bd1caf614ca6c30"></a><a name="a185be9c811954d069bd1caf614ca6c30"></a>createCacheRule</p>
</td>
</tr>
<tr id="r0491f4be9c1645858baa33442f6ea5c9"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a29f02c0a72d64e61ae807894cd8188f5"><a name="a29f02c0a72d64e61ae807894cd8188f5"></a><a name="a29f02c0a72d64e61ae807894cd8188f5"></a>Creating a cache refreshing task</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p760323518041"><a name="en-us_topic_0100240354_p760323518041"></a><a name="en-us_topic_0100240354_p760323518041"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a5303995aec7a442db103fee7028f1582"><a name="a5303995aec7a442db103fee7028f1582"></a><a name="a5303995aec7a442db103fee7028f1582"></a>createRefreshTask</p>
</td>
</tr>
<tr id="r0a9b5b62122049ddbefe225c27edf0ba"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a00724393183941a2b137db1fd1f410ba"><a name="a00724393183941a2b137db1fd1f410ba"></a><a name="a00724393183941a2b137db1fd1f410ba"></a>Creating a preheating task</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a7ccc0777a88844b7abc49fde630189f0"><a name="a7ccc0777a88844b7abc49fde630189f0"></a><a name="a7ccc0777a88844b7abc49fde630189f0"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a1ab41e107f0a4773b98523254209d0de"><a name="a1ab41e107f0a4773b98523254209d0de"></a><a name="a1ab41e107f0a4773b98523254209d0de"></a>createPreheatingTask</p>
</td>
</tr>
<tr id="r9585f2f7323549298791da8f00df1eb3"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="ace32d54e7aa3413db31a06cb101b3005"><a name="ace32d54e7aa3413db31a06cb101b3005"></a><a name="ace32d54e7aa3413db31a06cb101b3005"></a>Enabling CDN</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="ac3a0e51d606e447681e6cde35413428f"><a name="ac3a0e51d606e447681e6cde35413428f"></a><a name="ac3a0e51d606e447681e6cde35413428f"></a>CDN</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p107935215249"><a name="en-us_topic_0100240354_p107935215249"></a><a name="en-us_topic_0100240354_p107935215249"></a>createBillingMode</p>
</td>
</tr>
</tbody>
</table>

