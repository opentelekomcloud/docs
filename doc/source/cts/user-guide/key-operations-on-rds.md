# Key Operations on RDS<a name="en-us_topic_0100363625"></a>

Relational Database Service \(RDS\) is a cloud-based web service that is reliable, scalable, easy to manage, and immediately ready for use.

With CTS, you can record operations associated with RDS for future query, audit, and backtrack operations.

**Table  1**  RDS operations that can be recorded by CTS

<a name="table27743863194823"></a>
<table><thead align="left"><tr id="r16cd56af9fb340308aee844e27568144"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="af0d3b5a410114ab28f61818ba5768621"><a name="af0d3b5a410114ab28f61818ba5768621"></a><a name="af0d3b5a410114ab28f61818ba5768621"></a><strong id="en-us_topic_0100240370_b726976511613"><a name="en-us_topic_0100240370_b726976511613"></a><a name="en-us_topic_0100240370_b726976511613"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="a46e334c347b348259d14019fe61b273a"><a name="a46e334c347b348259d14019fe61b273a"></a><a name="a46e334c347b348259d14019fe61b273a"></a><strong id="a9b030b079e204c88b9f19a65adb90031"><a name="a9b030b079e204c88b9f19a65adb90031"></a><a name="a9b030b079e204c88b9f19a65adb90031"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="a42c5e5ccb54e4e94afefcde649d57695"><a name="a42c5e5ccb54e4e94afefcde649d57695"></a><a name="a42c5e5ccb54e4e94afefcde649d57695"></a><strong id="af2aa8f455c8a402f826c472836da0631"><a name="af2aa8f455c8a402f826c472836da0631"></a><a name="af2aa8f455c8a402f826c472836da0631"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra0690a1ae591410e938e90e40299e283"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a0c7da73cad5141feab2f28e0949d185f"><a name="a0c7da73cad5141feab2f28e0949d185f"></a><a name="a0c7da73cad5141feab2f28e0949d185f"></a>Creating a DB instance, restoring data to a new DB instance, creating a read replica (using the console, Open API, or Trove API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a75140065d4204488800a25359037b3a4"><a name="a75140065d4204488800a25359037b3a4"></a><a name="a75140065d4204488800a25359037b3a4"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a1e02609146a94b399bbd922def9d4ea1"><a name="a1e02609146a94b399bbd922def9d4ea1"></a><a name="a1e02609146a94b399bbd922def9d4ea1"></a>createInstance</p>
</td>
</tr>
<tr id="ra23f5a4b0385412ca8635bd978cd7cf4"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a0a7707edd9914524b9651cd60fd45f43"><a name="a0a7707edd9914524b9651cd60fd45f43"></a><a name="a0a7707edd9914524b9651cd60fd45f43"></a>Restarting and scaling up a DB instance, changing the DB instance class, and restoring data to the old DB instance (using the console, Open API, or Trove API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p418869210749"><a name="en-us_topic_0100240370_p418869210749"></a><a name="en-us_topic_0100240370_p418869210749"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="abd3da082687c4df0b0cf55a10f9a9c10"><a name="abd3da082687c4df0b0cf55a10f9a9c10"></a><a name="abd3da082687c4df0b0cf55a10f9a9c10"></a>instanceAction</p>
</td>
</tr>
<tr id="rcaec9d496c7d4b46bde166331685db80"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="ad1c67831112c49d089eef5c0ae2db34f"><a name="ad1c67831112c49d089eef5c0ae2db34f"></a><a name="ad1c67831112c49d089eef5c0ae2db34f"></a>Resetting the password (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a5d056219db234bdbab4d5b618de971fb"><a name="a5d056219db234bdbab4d5b618de971fb"></a><a name="a5d056219db234bdbab4d5b618de971fb"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a0c209611c5594b0fb4daaa05d800c319"><a name="a0c209611c5594b0fb4daaa05d800c319"></a><a name="a0c209611c5594b0fb4daaa05d800c319"></a>resetPassword</p>
</td>
</tr>
<tr id="r08720fcd8a53435cae1e66b7e08f56cf"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a260e0652731f489a8655758dd2fa97d1"><a name="a260e0652731f489a8655758dd2fa97d1"></a><a name="a260e0652731f489a8655758dd2fa97d1"></a>Setting the DB version parameters (using Open API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="ac84028025e654687b96eef7f3c7550ad"><a name="ac84028025e654687b96eef7f3c7550ad"></a><a name="ac84028025e654687b96eef7f3c7550ad"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a3eb68fd728604282a4e53b481278fb25"><a name="a3eb68fd728604282a4e53b481278fb25"></a><a name="a3eb68fd728604282a4e53b481278fb25"></a>setDBParameters</p>
</td>
</tr>
<tr id="r73422f0da4ea4ebe9ef3ed4b69f12617"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a90f48f48bac34ceeae2c3a2348e40cd3"><a name="a90f48f48bac34ceeae2c3a2348e40cd3"></a><a name="a90f48f48bac34ceeae2c3a2348e40cd3"></a>Resetting the DN version parameters (using Open API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a5e93d651a60e45518789f4d91cf47d70"><a name="a5e93d651a60e45518789f4d91cf47d70"></a><a name="a5e93d651a60e45518789f4d91cf47d70"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="abb75c45a6fe14e8f8833c35ede113ea5"><a name="abb75c45a6fe14e8f8833c35ede113ea5"></a><a name="abb75c45a6fe14e8f8833c35ede113ea5"></a>resetDBParameters</p>
</td>
</tr>
<tr id="r52848f4c69114681bcac1124a9295577"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a526f3388db994fd3945d216938b578ae"><a name="a526f3388db994fd3945d216938b578ae"></a><a name="a526f3388db994fd3945d216938b578ae"></a>Setting <strong id="b842352706201653"><a name="b842352706201653"></a><a name="b842352706201653"></a>Backup Policy</strong> to <strong id="b842352706201656"><a name="b842352706201656"></a><a name="b842352706201656"></a>On</strong>, <strong id="b842352706201659"><a name="b842352706201659"></a><a name="b842352706201659"></a>Off,</strong> or <strong id="b84235270620173"><a name="b84235270620173"></a><a name="b84235270620173"></a>Modify</strong> (using the console or Open API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="af9ca8567a8df4d0fb346cf4f9167ba38"><a name="af9ca8567a8df4d0fb346cf4f9167ba38"></a><a name="af9ca8567a8df4d0fb346cf4f9167ba38"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a9d782418ec9143559c288e752b6b8b19"><a name="a9d782418ec9143559c288e752b6b8b19"></a><a name="a9d782418ec9143559c288e752b6b8b19"></a>setBackupPolicy</p>
</td>
</tr>
<tr id="r61c72fe22808425f9262a11f161807ba"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a2b5cf1d7c55c453796057bbdf20c69a2"><a name="a2b5cf1d7c55c453796057bbdf20c69a2"></a><a name="a2b5cf1d7c55c453796057bbdf20c69a2"></a>Modifying the DB port number (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a8516e6c67b41444eabd230d795eb1479"><a name="a8516e6c67b41444eabd230d795eb1479"></a><a name="a8516e6c67b41444eabd230d795eb1479"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a2ef6ed81dbfe411e97326436c182726d"><a name="a2ef6ed81dbfe411e97326436c182726d"></a><a name="a2ef6ed81dbfe411e97326436c182726d"></a>changeInstancePort</p>
</td>
</tr>
<tr id="r3cf84f08e8ea415f87c0e6b00ba99857"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240370_p24834310535"><a name="en-us_topic_0100240370_p24834310535"></a><a name="en-us_topic_0100240370_p24834310535"></a>Binding or unbinding an elastic IP address (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p824076810749"><a name="en-us_topic_0100240370_p824076810749"></a><a name="en-us_topic_0100240370_p824076810749"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a6597514044db45a2a204348f3b1f4ee2"><a name="a6597514044db45a2a204348f3b1f4ee2"></a><a name="a6597514044db45a2a204348f3b1f4ee2"></a>setOrResetPublicIP</p>
</td>
</tr>
<tr id="red10207c664d40baa9054f7111b27ab0"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="af5e471f8e0494506b136d9b260d08a63"><a name="af5e471f8e0494506b136d9b260d08a63"></a><a name="af5e471f8e0494506b136d9b260d08a63"></a>Modifying a security group (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a0d23dae83f084a2cac3ace9d83c72361"><a name="a0d23dae83f084a2cac3ace9d83c72361"></a><a name="a0d23dae83f084a2cac3ace9d83c72361"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="aff96f57e5fbf49f086a952d37918263c"><a name="aff96f57e5fbf49f086a952d37918263c"></a><a name="aff96f57e5fbf49f086a952d37918263c"></a>modifySecurityGroup</p>
</td>
</tr>
<tr id="rf30d0854813b4ec7a872f912445a57c6"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="aa028ddcdb22143a38f47e7ba74b8a37e"><a name="aa028ddcdb22143a38f47e7ba74b8a37e"></a><a name="aa028ddcdb22143a38f47e7ba74b8a37e"></a>Creating a tag (using the console or Open API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="aae2c0d7d85b642b19e97b033709d96dd"><a name="aae2c0d7d85b642b19e97b033709d96dd"></a><a name="aae2c0d7d85b642b19e97b033709d96dd"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a50cde6251166471898ead3d5f161f9df"><a name="a50cde6251166471898ead3d5f161f9df"></a><a name="a50cde6251166471898ead3d5f161f9df"></a>createTag</p>
</td>
</tr>
<tr id="r8ad5dc1165ab49768bfdb044ba2ef391"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="af1764d8428e14cc08ae6a06a85a55ced"><a name="af1764d8428e14cc08ae6a06a85a55ced"></a><a name="af1764d8428e14cc08ae6a06a85a55ced"></a>Deleting a tag (using the console or Open API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p178320210749"><a name="en-us_topic_0100240370_p178320210749"></a><a name="en-us_topic_0100240370_p178320210749"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="ae1ca172b7a9146009ba12ad8d44d448c"><a name="ae1ca172b7a9146009ba12ad8d44d448c"></a><a name="ae1ca172b7a9146009ba12ad8d44d448c"></a>deleteTag</p>
</td>
</tr>
<tr id="r7513ffc0027345179a243342a57fde46"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a0b0605aa3de84cfa9444c5dccf7a936d"><a name="a0b0605aa3de84cfa9444c5dccf7a936d"></a><a name="a0b0605aa3de84cfa9444c5dccf7a936d"></a>Modifying a tag (using the console or Open API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a05d0c99e587f42d4ad7c3822eb306db4"><a name="a05d0c99e587f42d4ad7c3822eb306db4"></a><a name="a05d0c99e587f42d4ad7c3822eb306db4"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a9acd7f4fc7f1495b8bf0c4881f83407f"><a name="a9acd7f4fc7f1495b8bf0c4881f83407f"></a><a name="a9acd7f4fc7f1495b8bf0c4881f83407f"></a>modifyTag</p>
</td>
</tr>
<tr id="r9e4fe85224f8472587536feb79dffaf9"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="ac4f924677b8847b49d70c275b63536a9"><a name="ac4f924677b8847b49d70c275b63536a9"></a><a name="ac4f924677b8847b49d70c275b63536a9"></a>Deleting a DB instance from a cluster (using the console, Open API, or Trove API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a961b81354c304059bf6e0196f3d8bc1e"><a name="a961b81354c304059bf6e0196f3d8bc1e"></a><a name="a961b81354c304059bf6e0196f3d8bc1e"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a4bee002ff83f42c8b73d6f1ea2f1c7e8"><a name="a4bee002ff83f42c8b73d6f1ea2f1c7e8"></a><a name="a4bee002ff83f42c8b73d6f1ea2f1c7e8"></a>deleteInstance</p>
</td>
</tr>
<tr id="r0c7e2a5e9a4f4f46bbabb602a9e18054"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240370_p525050710535"><a name="en-us_topic_0100240370_p525050710535"></a><a name="en-us_topic_0100240370_p525050710535"></a>Creating a snapshot (using the console or Open API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a193675502dcf4b00ae847306d6b99320"><a name="a193675502dcf4b00ae847306d6b99320"></a><a name="a193675502dcf4b00ae847306d6b99320"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a46a44edda1574d6bba45bb8747520e15"><a name="a46a44edda1574d6bba45bb8747520e15"></a><a name="a46a44edda1574d6bba45bb8747520e15"></a>createManualSnapshot</p>
</td>
</tr>
<tr id="r58eb9ae1915945ef8ab1002bd293c742"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240370_p241488010535"><a name="en-us_topic_0100240370_p241488010535"></a><a name="en-us_topic_0100240370_p241488010535"></a>Copying a snapshot (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="ae0922d5301a740629b4f7e8d0342d3b2"><a name="ae0922d5301a740629b4f7e8d0342d3b2"></a><a name="ae0922d5301a740629b4f7e8d0342d3b2"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a087182f165b0433780c601a33bca5bf5"><a name="a087182f165b0433780c601a33bca5bf5"></a><a name="a087182f165b0433780c601a33bca5bf5"></a>copySnapshot</p>
</td>
</tr>
<tr id="r8ec24506a48f4dc58f274fd2f9b88762"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a855d08e1fe4d478c9dfc6d897a5aed39"><a name="a855d08e1fe4d478c9dfc6d897a5aed39"></a><a name="a855d08e1fe4d478c9dfc6d897a5aed39"></a>Deleting a snapshot (using the console or Open API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a8e70614efaa34ab8b5d49fa43c249724"><a name="a8e70614efaa34ab8b5d49fa43c249724"></a><a name="a8e70614efaa34ab8b5d49fa43c249724"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a3de0b36c6df9470ea43cfd7e0f29df95"><a name="a3de0b36c6df9470ea43cfd7e0f29df95"></a><a name="a3de0b36c6df9470ea43cfd7e0f29df95"></a>deleteManualSnapshot</p>
</td>
</tr>
<tr id="r982e3dd19f8e424598fe293e64e105ec"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a06a11d83d5194d67b87142e5bc7433b7"><a name="a06a11d83d5194d67b87142e5bc7433b7"></a><a name="a06a11d83d5194d67b87142e5bc7433b7"></a>Creating a parameter group (using the console or Trove API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="aca039f71417442f29681036bdd1e55f0"><a name="aca039f71417442f29681036bdd1e55f0"></a><a name="aca039f71417442f29681036bdd1e55f0"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a1abd5feb47294e0e9b9b53dc64707023"><a name="a1abd5feb47294e0e9b9b53dc64707023"></a><a name="a1abd5feb47294e0e9b9b53dc64707023"></a>createParameterGroup</p>
</td>
</tr>
<tr id="r782691e768ad4117ab2963c245c67170"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240370_p719530510535"><a name="en-us_topic_0100240370_p719530510535"></a><a name="en-us_topic_0100240370_p719530510535"></a>Modifying a parameter group (using the console or Trove API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a0a2db672500f4415990aa29c254d50ff"><a name="a0a2db672500f4415990aa29c254d50ff"></a><a name="a0a2db672500f4415990aa29c254d50ff"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="aed215bc0d3d5494582be29f62f4c4801"><a name="aed215bc0d3d5494582be29f62f4c4801"></a><a name="aed215bc0d3d5494582be29f62f4c4801"></a>updateParameterGroup</p>
</td>
</tr>
<tr id="reab51e832e9f4c469d0871907d7bfbcd"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a164b97bdc7f54a59b012203b7d4d6a04"><a name="a164b97bdc7f54a59b012203b7d4d6a04"></a><a name="a164b97bdc7f54a59b012203b7d4d6a04"></a>Deleting a parameter group (using the console or Trove API)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a868a53c5ce8d4dfbaaa73a90da18808e"><a name="a868a53c5ce8d4dfbaaa73a90da18808e"></a><a name="a868a53c5ce8d4dfbaaa73a90da18808e"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a4e6d5742512f4cad99c397ddc0f4e900"><a name="a4e6d5742512f4cad99c397ddc0f4e900"></a><a name="a4e6d5742512f4cad99c397ddc0f4e900"></a>deleteParameterGroup</p>
</td>
</tr>
<tr id="rf4260e18249048759ba217e28ee02980"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="abdd70d5f38dd43959c2a52d693a5b68e"><a name="abdd70d5f38dd43959c2a52d693a5b68e"></a><a name="abdd70d5f38dd43959c2a52d693a5b68e"></a>Copying a parameter group (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a0767a46bdc5841dfab4a870beb96d832"><a name="a0767a46bdc5841dfab4a870beb96d832"></a><a name="a0767a46bdc5841dfab4a870beb96d832"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="ac911bb0973624169a0166e241b8654d6"><a name="ac911bb0973624169a0166e241b8654d6"></a><a name="ac911bb0973624169a0166e241b8654d6"></a>copyParameterGroup</p>
</td>
</tr>
<tr id="ra435a3e7ffab4f4aa9ec1e3087d1adf8"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="ab5f37dac49d24543af56b12765cefdbe"><a name="ab5f37dac49d24543af56b12765cefdbe"></a><a name="ab5f37dac49d24543af56b12765cefdbe"></a>Resetting a parameter group (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="af3fe655f1a9844d5847cff2ddcf3593c"><a name="af3fe655f1a9844d5847cff2ddcf3593c"></a><a name="af3fe655f1a9844d5847cff2ddcf3593c"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="add34489aa5284481978fe9af7d9e4abc"><a name="add34489aa5284481978fe9af7d9e4abc"></a><a name="add34489aa5284481978fe9af7d9e4abc"></a>resetParameterGroup</p>
</td>
</tr>
<tr id="rd313e82d239b4fbca3b6458ef2638f6a"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="a2a715302d32a4d67aac6369589f0948d"><a name="a2a715302d32a4d67aac6369589f0948d"></a><a name="a2a715302d32a4d67aac6369589f0948d"></a>Comparing parameter groups (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="a18f25fb34dbb4224b786db49fae9945e"><a name="a18f25fb34dbb4224b786db49fae9945e"></a><a name="a18f25fb34dbb4224b786db49fae9945e"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="a354e5bb52a5c4cc987822bfdd7ae6b62"><a name="a354e5bb52a5c4cc987822bfdd7ae6b62"></a><a name="a354e5bb52a5c4cc987822bfdd7ae6b62"></a>compareParameterGroup</p>
</td>
</tr>
<tr id="r13f028996b204410a72e072d3215996d"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="ac4820ad5bb4f4366ac77c0290e506d12"><a name="ac4820ad5bb4f4366ac77c0290e506d12"></a><a name="ac4820ad5bb4f4366ac77c0290e506d12"></a>Applying a parameter group (using the console)</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="ac97d9318636a4537b66c3d95e8a1552a"><a name="ac97d9318636a4537b66c3d95e8a1552a"></a><a name="ac97d9318636a4537b66c3d95e8a1552a"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="aa97a103d20d345c4b269973cd1a2d1c7"><a name="aa97a103d20d345c4b269973cd1a2d1c7"></a><a name="aa97a103d20d345c4b269973cd1a2d1c7"></a>applyParameterGroup</p>
</td>
</tr>
</tbody>
</table>

