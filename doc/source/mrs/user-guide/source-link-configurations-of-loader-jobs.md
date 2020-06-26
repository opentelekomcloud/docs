# Source Link Configurations of Loader Jobs<a name="EN-US_TOPIC_0125375657"></a>

## Overview<a name="s786da33d6aca4c509fd57907b2c3fb13"></a>

When Loader jobs obtain data from different data sources, a link corresponding to a data source type needs to be selected and the link properties need to be configured.

## obs-connector<a name="s804ec246c3174525b25e3a65acc1805f"></a>

**Table  1**  Data source link properties of  **obs-connector**

<a name="tc09a1f1fd20c4ea6aec386e69b72383f"></a>
<table><thead align="left"><tr id="r88e145d5477d4b628fc25042dee1a836"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="ab7240d3f06b4479184ec25a5f8e7d503"><a name="ab7240d3f06b4479184ec25a5f8e7d503"></a><a name="ab7240d3f06b4479184ec25a5f8e7d503"></a><strong id="ace28aaeab55a435dba17fd1f29ed32f8"><a name="ace28aaeab55a435dba17fd1f29ed32f8"></a><a name="ace28aaeab55a435dba17fd1f29ed32f8"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a70689ba9f4a14ce292c3002d8e2053ee"><a name="a70689ba9f4a14ce292c3002d8e2053ee"></a><a name="a70689ba9f4a14ce292c3002d8e2053ee"></a><strong id="a7f2942d9d39f46aeb20303a6ed6505e6"><a name="a7f2942d9d39f46aeb20303a6ed6505e6"></a><a name="a7f2942d9d39f46aeb20303a6ed6505e6"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rb323d024609944798c9db2d489180675"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="aafb8c6b43923443bb1fb581268be7f54"><a name="aafb8c6b43923443bb1fb581268be7f54"></a><a name="aafb8c6b43923443bb1fb581268be7f54"></a>Bucket Name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a65a6c94fc3c443f9839dd24ef1b71f99"><a name="a65a6c94fc3c443f9839dd24ef1b71f99"></a><a name="a65a6c94fc3c443f9839dd24ef1b71f99"></a>OBS bucket for storing source data</p>
</td>
</tr>
<tr id="re25997c71648491fb5bee9ba9ea2ce65"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ab374d71c9ce749b4aebad5324b172b47"><a name="ab374d71c9ce749b4aebad5324b172b47"></a><a name="ab374d71c9ce749b4aebad5324b172b47"></a>Input directory or file</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a771b55f8c43148b79a13a678452d6f46"><a name="a771b55f8c43148b79a13a678452d6f46"></a><a name="a771b55f8c43148b79a13a678452d6f46"></a>Actual storage form of source data. It can be either all data files in a directory or single data file contained in the bucket.</p>
</td>
</tr>
<tr id="r557eaec28a114a968545d60dc923dc6e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a4b934c14cf8c4b438f9bdb180560964b"><a name="a4b934c14cf8c4b438f9bdb180560964b"></a><a name="a4b934c14cf8c4b438f9bdb180560964b"></a>File format</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="abf4a189340fd4130aa1bfcba8e94542a"><a name="abf4a189340fd4130aa1bfcba8e94542a"></a><a name="abf4a189340fd4130aa1bfcba8e94542a"></a>Loader supports the following file formats of data stored in OBS:</p>
<a name="ue7e2394fdf9c4782ade44db2ec97a44e"></a><a name="ue7e2394fdf9c4782ade44db2ec97a44e"></a><ul id="ue7e2394fdf9c4782ade44db2ec97a44e"><li><strong id="adaeaf0a814cf477b8e10a9c38342661e"><a name="adaeaf0a814cf477b8e10a9c38342661e"></a><a name="adaeaf0a814cf477b8e10a9c38342661e"></a>CSV_FILE</strong>: Specifies a text file. When the destination link is a database link, only the text file is supported.</li><li><strong id="a0e1918920da149f6aedf61983948ee52"><a name="a0e1918920da149f6aedf61983948ee52"></a><a name="a0e1918920da149f6aedf61983948ee52"></a>BINARY_FILE</strong>: Specifies binary files excluding text files.</li></ul>
</td>
</tr>
<tr id="rc9f9bdb961b54169912b76b68921e041"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0071084972_p547205051766"><a name="en-us_topic_0071084972_p547205051766"></a><a name="en-us_topic_0071084972_p547205051766"></a>Line Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0071084972_p527477181766"><a name="en-us_topic_0071084972_p527477181766"></a><a name="en-us_topic_0071084972_p527477181766"></a>Identifier of each line end of source data</p>
</td>
</tr>
<tr id="rd1894be093234839bbdc5bf2614325d1"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a0d4d5ccdb55046bb8257eb043d52c2e9"><a name="a0d4d5ccdb55046bb8257eb043d52c2e9"></a><a name="a0d4d5ccdb55046bb8257eb043d52c2e9"></a>Field Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a2c86009669604774ae17fe62cbf93cda"><a name="a2c86009669604774ae17fe62cbf93cda"></a><a name="a2c86009669604774ae17fe62cbf93cda"></a>Identifier of each field end of source data</p>
</td>
</tr>
<tr id="r59f780ce28d440c3a1afbcd729601f72"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ab02aed3e54b641b2bb0446d0fcdec93d"><a name="ab02aed3e54b641b2bb0446d0fcdec93d"></a><a name="ab02aed3e54b641b2bb0446d0fcdec93d"></a>Encode type</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a0d3f97ca46534969ab2a4d67603569ff"><a name="a0d3f97ca46534969ab2a4d67603569ff"></a><a name="a0d3f97ca46534969ab2a4d67603569ff"></a>Text encoding type of source data. It takes effect for text files only.</p>
</td>
</tr>
<tr id="r8bdac2515cf54b679f11d4c44e2a6a7f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0071084972_p179695571766"><a name="en-us_topic_0071084972_p179695571766"></a><a name="en-us_topic_0071084972_p179695571766"></a>File split type</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><div class="p" id="en-us_topic_0071084972_p98470941766"><a name="en-us_topic_0071084972_p98470941766"></a><a name="en-us_topic_0071084972_p98470941766"></a>The following types are supported:<a name="u6280c66040534d83a948c98ce5e1773c"></a><a name="u6280c66040534d83a948c98ce5e1773c"></a><ul id="u6280c66040534d83a948c98ce5e1773c"><li><strong id="ad50473b6932241e39e1875d9e49683d2"><a name="ad50473b6932241e39e1875d9e49683d2"></a><a name="ad50473b6932241e39e1875d9e49683d2"></a>File</strong>: The number of files is assigned to a map task by the total number of files. The calculation formula is&nbsp;<span class="parmvalue" id="p08fc9643549d49188695df9bfe78dff1"><a name="p08fc9643549d49188695df9bfe78dff1"></a><a name="p08fc9643549d49188695df9bfe78dff1"></a><b>Total number of files/Extractors</b></span>.</li><li><strong id="a19f35fd17d20492f82b75b4b79c55190"><a name="a19f35fd17d20492f82b75b4b79c55190"></a><a name="a19f35fd17d20492f82b75b4b79c55190"></a>Size</strong>: A file size is assigned to a map task by the total file size. The calculation formula is&nbsp;<span class="parmvalue" id="p5b673e26960e41958b2cd9262af03c92"><a name="p5b673e26960e41958b2cd9262af03c92"></a><a name="p5b673e26960e41958b2cd9262af03c92"></a><b>Total file size/Extractors</b></span>.</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## generic-jdbc-connector<a name="s51d589f5a761450392b301229e5a2e97"></a>

**Table  2**  Data source link properties of  **generic-jdbc-connector**

<a name="t44fac1f9f83d4366bf947d6887129eaa"></a>
<table><thead align="left"><tr id="r574dfdd836d141afa54b00ef275f19c3"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a9e3d37ad56e74a48826b775c46ba5f1d"><a name="a9e3d37ad56e74a48826b775c46ba5f1d"></a><a name="a9e3d37ad56e74a48826b775c46ba5f1d"></a><strong id="acbc708158b3047c3b4d00d4b06784536"><a name="acbc708158b3047c3b4d00d4b06784536"></a><a name="acbc708158b3047c3b4d00d4b06784536"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a567cb1db7b024c77b211e2bf69c8dad2"><a name="a567cb1db7b024c77b211e2bf69c8dad2"></a><a name="a567cb1db7b024c77b211e2bf69c8dad2"></a><strong id="a9086909d3fc64976b7a284faad0d49ac"><a name="a9086909d3fc64976b7a284faad0d49ac"></a><a name="a9086909d3fc64976b7a284faad0d49ac"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rdab9aad400104479a44352e90896a473"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a64855105fd56446aa1adf68db5d1c60b"><a name="a64855105fd56446aa1adf68db5d1c60b"></a><a name="a64855105fd56446aa1adf68db5d1c60b"></a>Schema name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a1feeab10c2d34f69b5a8d7325211318e"><a name="a1feeab10c2d34f69b5a8d7325211318e"></a><a name="a1feeab10c2d34f69b5a8d7325211318e"></a>Name of the database storing source data. You can query and select it on the interface.</p>
</td>
</tr>
<tr id="r5394d0800c394e98b55d18c4cab0bdd7"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a5bc08edf156342fe90db7c38a27a0bb7"><a name="a5bc08edf156342fe90db7c38a27a0bb7"></a><a name="a5bc08edf156342fe90db7c38a27a0bb7"></a>Table name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a89850bb40e394f338f1034b61013bb65"><a name="a89850bb40e394f338f1034b61013bb65"></a><a name="a89850bb40e394f338f1034b61013bb65"></a>Data table storing the source data. You can query and select it on the interface.</p>
</td>
</tr>
<tr id="r728e7be1c10a47339979326ad7d49bca"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ab2afd84397164f27981a93bbdc64ef25"><a name="ab2afd84397164f27981a93bbdc64ef25"></a><a name="ab2afd84397164f27981a93bbdc64ef25"></a>Partition column</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a30cbad4f78894b2aad1a8dbc98fa6bf5"><a name="a30cbad4f78894b2aad1a8dbc98fa6bf5"></a><a name="a30cbad4f78894b2aad1a8dbc98fa6bf5"></a>If multiple columns need to be read, use this column to split the result and obtain data.</p>
</td>
</tr>
<tr id="r802db0551f0147db806a30a705dab444"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a3a76185bee204dd5a36d2715bbb84e1b"><a name="a3a76185bee204dd5a36d2715bbb84e1b"></a><a name="a3a76185bee204dd5a36d2715bbb84e1b"></a><span id="pb1b07fde84cd4e678ae32ed0b653596c"><a name="pb1b07fde84cd4e678ae32ed0b653596c"></a><a name="pb1b07fde84cd4e678ae32ed0b653596c"></a>Where clause</span></p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ad90d78c2579f4b3ca12cce6cba18737f"><a name="ad90d78c2579f4b3ca12cce6cba18737f"></a><a name="ad90d78c2579f4b3ca12cce6cba18737f"></a>Query statement used for accessing the database</p>
</td>
</tr>
</tbody>
</table>

## ftp-connector or sftp-connector<a name="s12bda73332f14121a12bb881bec04f43"></a>

**Table  3**  Data source link properties of  **ftp-connector** or **sftp-connector**

<a name="t0a177eecf1d94cd19d9e11a04c4db1bc"></a>
<table><thead align="left"><tr id="rf67c067080634f8fb28e5e4217b3a415"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a8195da52daf247adb8bf67ea3bc3ccee"><a name="a8195da52daf247adb8bf67ea3bc3ccee"></a><a name="a8195da52daf247adb8bf67ea3bc3ccee"></a><strong id="a96252adcd1404042bb0bef2e5ec7e515"><a name="a96252adcd1404042bb0bef2e5ec7e515"></a><a name="a96252adcd1404042bb0bef2e5ec7e515"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a1e604c29ecfa4acd915c05164f4e3e99"><a name="a1e604c29ecfa4acd915c05164f4e3e99"></a><a name="a1e604c29ecfa4acd915c05164f4e3e99"></a><strong id="a5b02d8db328148ed819f0c2025fb7617"><a name="a5b02d8db328148ed819f0c2025fb7617"></a><a name="a5b02d8db328148ed819f0c2025fb7617"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r700b74657318421d93e11ce8edc5421a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a9bbc570d745e48de978f239c4acf2940"><a name="a9bbc570d745e48de978f239c4acf2940"></a><a name="a9bbc570d745e48de978f239c4acf2940"></a>Input directory or file</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ab2bac837e6604f9ab4deae492b2f5e4d"><a name="ab2bac837e6604f9ab4deae492b2f5e4d"></a><a name="ab2bac837e6604f9ab4deae492b2f5e4d"></a>Actual storage form of source data. It can be either all data files in a directory or single data file contained in the file server.</p>
</td>
</tr>
<tr id="rdf78a511d5de4441ab046dcd277b9cec"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="abc5e7055da394310a3ff0c67c93a5e17"><a name="abc5e7055da394310a3ff0c67c93a5e17"></a><a name="abc5e7055da394310a3ff0c67c93a5e17"></a>File format</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a52aa47be710a4d2b8d53fe0025594a3c"><a name="a52aa47be710a4d2b8d53fe0025594a3c"></a><a name="a52aa47be710a4d2b8d53fe0025594a3c"></a>Loader supports the following file formats of data stored in the file server:</p>
<a name="u467946cb418849a398d3c67c2f683ea8"></a><a name="u467946cb418849a398d3c67c2f683ea8"></a><ul id="u467946cb418849a398d3c67c2f683ea8"><li><strong id="a95213d0ed780458192fdb1868be65e11"><a name="a95213d0ed780458192fdb1868be65e11"></a><a name="a95213d0ed780458192fdb1868be65e11"></a>CSV_FILE</strong>: Specifies a text file. When the destination link is a database link, only the text file is supported.</li><li><strong id="a37d9b51519744d45a32b54b4bb7fc8ae"><a name="a37d9b51519744d45a32b54b4bb7fc8ae"></a><a name="a37d9b51519744d45a32b54b4bb7fc8ae"></a>BINARY_FILE</strong>: Specifies binary files excluding text files.</li></ul>
</td>
</tr>
<tr id="r3f3e22e6e34243ffb26ec18f9eddf30a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a67dfdfa290da4ca790e172738012a153"><a name="a67dfdfa290da4ca790e172738012a153"></a><a name="a67dfdfa290da4ca790e172738012a153"></a>Line Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a21a0fac25a894100bda4fccd6cad8c7f"><a name="a21a0fac25a894100bda4fccd6cad8c7f"></a><a name="a21a0fac25a894100bda4fccd6cad8c7f"></a>Identifier of each line end of source data</p>
<div class="note" id="nfc5e989e473b466b8f5347cb923fc9cc"><a name="nfc5e989e473b466b8f5347cb923fc9cc"></a><a name="nfc5e989e473b466b8f5347cb923fc9cc"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a02dbd59c54f34895a87a24e2405935a5"><a name="a02dbd59c54f34895a87a24e2405935a5"></a><a name="a02dbd59c54f34895a87a24e2405935a5"></a>When FTP or SFTP serves as a source link and <span class="parmname" id="p8a7af04345d248f6b54f51bd43188ea2"><a name="p8a7af04345d248f6b54f51bd43188ea2"></a><a name="p8a7af04345d248f6b54f51bd43188ea2"></a><b>File format</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="pd3cc44c06e7c4f6385e0435c0a1255c5"><a name="pd3cc44c06e7c4f6385e0435c0a1255c5"></a><a name="pd3cc44c06e7c4f6385e0435c0a1255c5"></a><b>BINARY_FILE</b></span>, the value of&nbsp;<span class="parmname" id="pf8899dee54324634a4d4b308a3031933"><a name="pf8899dee54324634a4d4b308a3031933"></a><a name="pf8899dee54324634a4d4b308a3031933"></a><b>Line Separator</b></span> in the advanced properties is invalid.</p>
</div></div>
</td>
</tr>
<tr id="r33d326d4609f4f739e7eeb6338341d0c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a1f9ad0432b034cd292a7cf0350905544"><a name="a1f9ad0432b034cd292a7cf0350905544"></a><a name="a1f9ad0432b034cd292a7cf0350905544"></a>Field Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a5fe48d8253034f49a02f69899150ed64"><a name="a5fe48d8253034f49a02f69899150ed64"></a><a name="a5fe48d8253034f49a02f69899150ed64"></a>Identifier of each field end of source data</p>
<div class="note" id="n7560598cced0417aae0321d7ea1c5744"><a name="n7560598cced0417aae0321d7ea1c5744"></a><a name="n7560598cced0417aae0321d7ea1c5744"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="aa7bdff8eecc14aeb988557521e562c31"><a name="aa7bdff8eecc14aeb988557521e562c31"></a><a name="aa7bdff8eecc14aeb988557521e562c31"></a>When FTP or SFTP serves as a source link and <span class="parmname" id="pd9f14e1c16044eee80fefa8162412469"><a name="pd9f14e1c16044eee80fefa8162412469"></a><a name="pd9f14e1c16044eee80fefa8162412469"></a><b>File format</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="p77f5fc7afba7464685a4d34594ed3006"><a name="p77f5fc7afba7464685a4d34594ed3006"></a><a name="p77f5fc7afba7464685a4d34594ed3006"></a><b>BINARY_FILE</b></span>, the value of&nbsp;<span class="parmname" id="p2d71531dbcd2423fb28499c1b18b49a1"><a name="p2d71531dbcd2423fb28499c1b18b49a1"></a><a name="p2d71531dbcd2423fb28499c1b18b49a1"></a><b>Field Separator</b></span> in the advanced properties is invalid.</p>
</div></div>
</td>
</tr>
<tr id="r07a1258321154267b0adf4f66a78035a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ac49a90b14fb2429ea4735e57a1a03628"><a name="ac49a90b14fb2429ea4735e57a1a03628"></a><a name="ac49a90b14fb2429ea4735e57a1a03628"></a>Encode type</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a572e9000d93449acb70f3e53102e4906"><a name="a572e9000d93449acb70f3e53102e4906"></a><a name="a572e9000d93449acb70f3e53102e4906"></a>Text encoding type of source data. It takes effect for text files only.</p>
</td>
</tr>
<tr id="rf9c5eb39cb3a4b16a794e18a7534b4f3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="af02ecdce05334ed9b5b7374c3338364a"><a name="af02ecdce05334ed9b5b7374c3338364a"></a><a name="af02ecdce05334ed9b5b7374c3338364a"></a>File split type</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><div class="p" id="ae8ee802faab44835a44323934ebc0f13"><a name="ae8ee802faab44835a44323934ebc0f13"></a><a name="ae8ee802faab44835a44323934ebc0f13"></a>The following types are supported:<a name="u77b5ba757c4644fcaf328d7c6998ea0e"></a><a name="u77b5ba757c4644fcaf328d7c6998ea0e"></a><ul id="u77b5ba757c4644fcaf328d7c6998ea0e"><li><strong id="ae60ffa5ff90f4c69bf98aabe6f3f2475"><a name="ae60ffa5ff90f4c69bf98aabe6f3f2475"></a><a name="ae60ffa5ff90f4c69bf98aabe6f3f2475"></a>File</strong>: The number of files is assigned to a map task by the total number of files. The calculation formula is&nbsp;<span class="parmvalue" id="p42df494f9d8f438a8391567e5b422498"><a name="p42df494f9d8f438a8391567e5b422498"></a><a name="p42df494f9d8f438a8391567e5b422498"></a><b>Total number of files/Extractors</b></span>.</li><li><strong id="a33e3b8956c2249b8905bc6169fd6d23d"><a name="a33e3b8956c2249b8905bc6169fd6d23d"></a><a name="a33e3b8956c2249b8905bc6169fd6d23d"></a>Size</strong>: A file size is assigned to a map task by the total file size. The calculation formula is&nbsp;<span class="parmvalue" id="p68f1e4d9895d484aa58ab0fe469621df"><a name="p68f1e4d9895d484aa58ab0fe469621df"></a><a name="p68f1e4d9895d484aa58ab0fe469621df"></a><b>Total file size/Extractors</b></span>.</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## hbase-connector<a name="se18d5b711ff44c4b97ccdaf6b9dd7f2a"></a>

**Table  4**  Data source link properties of  **hbase-connector**

<a name="t112b43b1a7114c42ab4d792f2d36f25d"></a>
<table><thead align="left"><tr id="r54b08060ec8b405f8e2e28f20f5f6c28"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a6732fa26372c41f8a091446f303534d1"><a name="a6732fa26372c41f8a091446f303534d1"></a><a name="a6732fa26372c41f8a091446f303534d1"></a><strong id="a719e75464c8d48a981314a13524af667"><a name="a719e75464c8d48a981314a13524af667"></a><a name="a719e75464c8d48a981314a13524af667"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a5860cec084864e2db8dde589ad56f473"><a name="a5860cec084864e2db8dde589ad56f473"></a><a name="a5860cec084864e2db8dde589ad56f473"></a><strong id="aa5aa7fa47aba4af7a74c5b53d7a5a55f"><a name="aa5aa7fa47aba4af7a74c5b53d7a5a55f"></a><a name="aa5aa7fa47aba4af7a74c5b53d7a5a55f"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="re7631c492aa943daab9dc15e82fca7a9"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a0ed17a85defa4ae38c0f49e26d91f528"><a name="a0ed17a85defa4ae38c0f49e26d91f528"></a><a name="a0ed17a85defa4ae38c0f49e26d91f528"></a>Table name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a835238d292c84f0fa1a70bba9893fa71"><a name="a835238d292c84f0fa1a70bba9893fa71"></a><a name="a835238d292c84f0fa1a70bba9893fa71"></a>HBase table storing source data</p>
</td>
</tr>
</tbody>
</table>

## hdfs-connector<a name="se4cb58283fd4451682b708d71e4e3877"></a>

**Table  5**  Data source link properties of  **hdfs-connector**

<a name="t9fe06ca9d0ee4a81983339f7db18661f"></a>
<table><thead align="left"><tr id="r675821440cfa4fbeb99d86fc966e899b"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a1149067da6c04774ba64b87e2d802bad"><a name="a1149067da6c04774ba64b87e2d802bad"></a><a name="a1149067da6c04774ba64b87e2d802bad"></a><strong id="a11865e6496ea4c659bcdd9c6b5700feb"><a name="a11865e6496ea4c659bcdd9c6b5700feb"></a><a name="a11865e6496ea4c659bcdd9c6b5700feb"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a59f31161440d4007abc6b01a1c237862"><a name="a59f31161440d4007abc6b01a1c237862"></a><a name="a59f31161440d4007abc6b01a1c237862"></a><strong id="a26bfe6d9a79d4df1a50cbd61c37fb12d"><a name="a26bfe6d9a79d4df1a50cbd61c37fb12d"></a><a name="a26bfe6d9a79d4df1a50cbd61c37fb12d"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r82d0f79fb51840c0843a8dc18555a597"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0071084972_p385045217275"><a name="en-us_topic_0071084972_p385045217275"></a><a name="en-us_topic_0071084972_p385045217275"></a>Input directory or file</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a15c967eff24245eb818a0863eb5ca28a"><a name="a15c967eff24245eb818a0863eb5ca28a"></a><a name="a15c967eff24245eb818a0863eb5ca28a"></a>Actual storage form of source data. It can be either all data files in a directory or single data file contained in HDFS.</p>
</td>
</tr>
<tr id="rb74d4a04074c4a46b8ea74b98182c285"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a2a9b9ee154db4f708bbc0c0c30cb0ce0"><a name="a2a9b9ee154db4f708bbc0c0c30cb0ce0"></a><a name="a2a9b9ee154db4f708bbc0c0c30cb0ce0"></a>File format</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aa97cbcda72a64421ab513efa53033652"><a name="aa97cbcda72a64421ab513efa53033652"></a><a name="aa97cbcda72a64421ab513efa53033652"></a>Loader supports the following file formats of data stored in HDFS:</p>
<a name="ufb8fd0046b424e4995d583ec4c2d9581"></a><a name="ufb8fd0046b424e4995d583ec4c2d9581"></a><ul id="ufb8fd0046b424e4995d583ec4c2d9581"><li><strong id="a22e2b0e13a3b4f4e826e76914e9eb340"><a name="a22e2b0e13a3b4f4e826e76914e9eb340"></a><a name="a22e2b0e13a3b4f4e826e76914e9eb340"></a>CSV_FILE</strong>: Specifies a text file. When the destination link is a database link, only the text file is supported.</li><li><strong id="a6523409c819f4c4c9ebe66bdc30efe40"><a name="a6523409c819f4c4c9ebe66bdc30efe40"></a><a name="a6523409c819f4c4c9ebe66bdc30efe40"></a>BINARY_FILE</strong>: Specifies binary files excluding text files.</li></ul>
</td>
</tr>
<tr id="r36a42bfa76fd4ca9b008b30974d8899c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ab4827af282ce45e096fe9cc91a6fb2f6"><a name="ab4827af282ce45e096fe9cc91a6fb2f6"></a><a name="ab4827af282ce45e096fe9cc91a6fb2f6"></a>Line Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a7c63293e472e43e18fa5c9895615c86e"><a name="a7c63293e472e43e18fa5c9895615c86e"></a><a name="a7c63293e472e43e18fa5c9895615c86e"></a>Identifier of each line end of source data</p>
<div class="note" id="nf0c5a4c8733e407aa9fb49deae6d9135"><a name="nf0c5a4c8733e407aa9fb49deae6d9135"></a><a name="nf0c5a4c8733e407aa9fb49deae6d9135"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a9d6d3b49e2944a58ad445e8f141da238"><a name="a9d6d3b49e2944a58ad445e8f141da238"></a><a name="a9d6d3b49e2944a58ad445e8f141da238"></a>When HDFS serves as a source link and <span class="parmname" id="p63797a4fd49e47918370ca2e0c5be414"><a name="p63797a4fd49e47918370ca2e0c5be414"></a><a name="p63797a4fd49e47918370ca2e0c5be414"></a><b>File format</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="p51c3d8517cf24d2bbeef0f7007ee6437"><a name="p51c3d8517cf24d2bbeef0f7007ee6437"></a><a name="p51c3d8517cf24d2bbeef0f7007ee6437"></a><b>BINARY_FILE</b></span>, the value of&nbsp;<span class="parmname" id="pbe8840cf7b1f4c1594f26a3fb2a193f3"><a name="pbe8840cf7b1f4c1594f26a3fb2a193f3"></a><a name="pbe8840cf7b1f4c1594f26a3fb2a193f3"></a><b>Line Separator</b></span> in the advanced properties is invalid.</p>
</div></div>
</td>
</tr>
<tr id="rc4e3c7d753074bb78277b422c510fd51"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a70eea416c8a84e97810a2534bfafc3c9"><a name="a70eea416c8a84e97810a2534bfafc3c9"></a><a name="a70eea416c8a84e97810a2534bfafc3c9"></a>Field Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a2b7f1beeeb2b45a18f0659bc445ff60b"><a name="a2b7f1beeeb2b45a18f0659bc445ff60b"></a><a name="a2b7f1beeeb2b45a18f0659bc445ff60b"></a>Identifier of each field end of source data</p>
<div class="note" id="n3e361d9571364fa8bfd87f3d5281c48f"><a name="n3e361d9571364fa8bfd87f3d5281c48f"></a><a name="n3e361d9571364fa8bfd87f3d5281c48f"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ab98243357ebc4d2083402e9ad2795721"><a name="ab98243357ebc4d2083402e9ad2795721"></a><a name="ab98243357ebc4d2083402e9ad2795721"></a>When HDFS serves as a source link and <span class="parmname" id="pca075d91690e4e559450709fb3cfda1f"><a name="pca075d91690e4e559450709fb3cfda1f"></a><a name="pca075d91690e4e559450709fb3cfda1f"></a><b>File format</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="pf2b2e26dd12b4189877b6aa41826cccf"><a name="pf2b2e26dd12b4189877b6aa41826cccf"></a><a name="pf2b2e26dd12b4189877b6aa41826cccf"></a><b>BINARY_FILE</b></span>, the value of&nbsp;<span class="parmname" id="p2ef77e98584b478099a7163b0859428c"><a name="p2ef77e98584b478099a7163b0859428c"></a><a name="p2ef77e98584b478099a7163b0859428c"></a><b>Field Separator</b></span> in the advanced properties is invalid.</p>
</div></div>
</td>
</tr>
<tr id="rb06cd490e62e4d3ab88164efb6faf89c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a3d92a729c66749f6a2f6362ce85674eb"><a name="a3d92a729c66749f6a2f6362ce85674eb"></a><a name="a3d92a729c66749f6a2f6362ce85674eb"></a>File split type</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><div class="p" id="a48b94e047e584b8fbcb43895e83c86a9"><a name="a48b94e047e584b8fbcb43895e83c86a9"></a><a name="a48b94e047e584b8fbcb43895e83c86a9"></a>The following types are supported:<a name="u76da6f7eec2340d5b37a7e7f2ad94b7a"></a><a name="u76da6f7eec2340d5b37a7e7f2ad94b7a"></a><ul id="u76da6f7eec2340d5b37a7e7f2ad94b7a"><li><strong id="a51b9bd977c6b4be895e6befce52ee2c8"><a name="a51b9bd977c6b4be895e6befce52ee2c8"></a><a name="a51b9bd977c6b4be895e6befce52ee2c8"></a>File</strong>: The number of files is assigned to a map task by the total number of files. The calculation formula is&nbsp;<span class="parmvalue" id="p7e0759c96f0842eea37cb12726815db6"><a name="p7e0759c96f0842eea37cb12726815db6"></a><a name="p7e0759c96f0842eea37cb12726815db6"></a><b>Total number of files/Extractors</b></span>.</li><li><strong id="aa1d07d81243a4a0281963b1f114db70a"><a name="aa1d07d81243a4a0281963b1f114db70a"></a><a name="aa1d07d81243a4a0281963b1f114db70a"></a>Size</strong>: A file size is assigned to a map task by the total file size. The calculation formula is&nbsp;<span class="parmvalue" id="p7f246f5bb6e3488daa8fa04d1721c9bb"><a name="p7f246f5bb6e3488daa8fa04d1721c9bb"></a><a name="p7f246f5bb6e3488daa8fa04d1721c9bb"></a><b>Total file size/Extractors</b></span>.</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## hive-connector<a name="see0490b3fc874d8385c7daadaff97a75"></a>

**Table  6**  Data source link properties of  **hive-connector**

<a name="t31c12403de6e4e8ea667471edbbe6bd0"></a>
<table><thead align="left"><tr id="reb66f5ed86044a9790f06ee7890e9d55"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a36e1279b15424b42a5f37b511f10144f"><a name="a36e1279b15424b42a5f37b511f10144f"></a><a name="a36e1279b15424b42a5f37b511f10144f"></a><strong id="en-us_topic_0071084972_b816290111751"><a name="en-us_topic_0071084972_b816290111751"></a><a name="en-us_topic_0071084972_b816290111751"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a8d2b330d0ed6459790d7ecf1ff9509d4"><a name="a8d2b330d0ed6459790d7ecf1ff9509d4"></a><a name="a8d2b330d0ed6459790d7ecf1ff9509d4"></a><strong id="a470602778e234b87bbffe67010b82449"><a name="a470602778e234b87bbffe67010b82449"></a><a name="a470602778e234b87bbffe67010b82449"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r16883692720140bb985b799659115228"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a6f2be32b82b14a6aa637d8b987499c49"><a name="a6f2be32b82b14a6aa637d8b987499c49"></a><a name="a6f2be32b82b14a6aa637d8b987499c49"></a>Database</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aee97784cd7dc40b797144f10734397d4"><a name="aee97784cd7dc40b797144f10734397d4"></a><a name="aee97784cd7dc40b797144f10734397d4"></a>Name of the Hive database storing the data source. You can query and select it on the interface.</p>
</td>
</tr>
<tr id="r02a919f5a01843989cb8d0e5feb17f92"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a109baf51717e477cbb17b3df746a78de"><a name="a109baf51717e477cbb17b3df746a78de"></a><a name="a109baf51717e477cbb17b3df746a78de"></a>Table</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a3b813f051c704a09aeb216921e8cef0a"><a name="a3b813f051c704a09aeb216921e8cef0a"></a><a name="a3b813f051c704a09aeb216921e8cef0a"></a>Name of the Hive table storing the data source. You can query and select it on the interface.</p>
</td>
</tr>
</tbody>
</table>

## voltdb-connector<a name="s7227cc13591042f2b9c0292716479a1f"></a>

**Table  7**  Data source link properties of  **voltdb-connector**

<a name="t3e73a365e3dd4615b52fe388f321ba8b"></a>
<table><thead align="left"><tr id="rb641170d65464a54a6fa6630329e1794"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a374eac0cbdbe4994a9def87dcbb8a795"><a name="a374eac0cbdbe4994a9def87dcbb8a795"></a><a name="a374eac0cbdbe4994a9def87dcbb8a795"></a><strong id="a729fe4d49b184ba1a8b70ee2a09b4a79"><a name="a729fe4d49b184ba1a8b70ee2a09b4a79"></a><a name="a729fe4d49b184ba1a8b70ee2a09b4a79"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a0de2c007bb2e48a5be169b3428fa93e2"><a name="a0de2c007bb2e48a5be169b3428fa93e2"></a><a name="a0de2c007bb2e48a5be169b3428fa93e2"></a><strong id="aebb3097aae524776beb974748474106e"><a name="aebb3097aae524776beb974748474106e"></a><a name="aebb3097aae524776beb974748474106e"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r3b4eeb8f658147b2a86117481edd85a6"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a08c85bb71d6a4619b09ebca5947a1f9a"><a name="a08c85bb71d6a4619b09ebca5947a1f9a"></a><a name="a08c85bb71d6a4619b09ebca5947a1f9a"></a><span id="p2725d73349084ef49616b637d7df365d"><a name="p2725d73349084ef49616b637d7df365d"></a><a name="p2725d73349084ef49616b637d7df365d"></a>Partition column</span></p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a52acea86649c46658c6c033b1c47130e"><a name="a52acea86649c46658c6c033b1c47130e"></a><a name="a52acea86649c46658c6c033b1c47130e"></a><span id="p2bc99f85e8aa4c7ebbe04b9c36e2974d"><a name="p2bc99f85e8aa4c7ebbe04b9c36e2974d"></a><a name="p2bc99f85e8aa4c7ebbe04b9c36e2974d"></a>If multiple columns need to be read, use this column to split the result and obtain data.</span></p>
</td>
</tr>
<tr id="r5c242851b1b0418ab3ecb0dc8e4b1642"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a17c2cd0a2f914aa2827a83e246f1da7c"><a name="a17c2cd0a2f914aa2827a83e246f1da7c"></a><a name="a17c2cd0a2f914aa2827a83e246f1da7c"></a>Table</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ae2f2929c800849c29021b101f3c4f1cc"><a name="ae2f2929c800849c29021b101f3c4f1cc"></a><a name="ae2f2929c800849c29021b101f3c4f1cc"></a>Name of the memory database table storing source data. You can query and select it on the interface.</p>
</td>
</tr>
</tbody>
</table>

