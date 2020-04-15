# Loader Link Configuration<a name="EN-US_TOPIC_0125375650"></a>

## Overview<a name="s7aade5d7f07f4fdbac235f4ad12f66a6"></a>

Loader supports the following links. This section describes configurations of each link.

-   obs-connector
-   generic-jdbc-connector
-   ftp-connector or sftp-connector
-   hbase-connector, hdfs-connector, or hive-connector
-   voltdb-connector

## OBS Link<a name="sbe628698d7c94b30ad4f7eeff62250fb"></a>

An OBS link is a data exchange channel between Loader and OBS.  [Table 1](#t769a6fd0aaf7424b80d59afb1de67c91)  describes the configuration parameters.

**Table  1** **obs-connector**  configuration

<a name="t769a6fd0aaf7424b80d59afb1de67c91"></a>
<table><thead align="left"><tr id="ra1acd34059b6416da6c543e0995a6708"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a679da0116db047e7b06b1daa0cfbdb5c"><a name="a679da0116db047e7b06b1daa0cfbdb5c"></a><a name="a679da0116db047e7b06b1daa0cfbdb5c"></a><strong id="afd8284fd235841a8acb8f6017df07213"><a name="afd8284fd235841a8acb8f6017df07213"></a><a name="afd8284fd235841a8acb8f6017df07213"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="af472ffb2408d43f2ae431d785d8bb1de"><a name="af472ffb2408d43f2ae431d785d8bb1de"></a><a name="af472ffb2408d43f2ae431d785d8bb1de"></a><strong id="a8f4487e1e12746f4abbd0b535e2ab959"><a name="a8f4487e1e12746f4abbd0b535e2ab959"></a><a name="a8f4487e1e12746f4abbd0b535e2ab959"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r06ac592d97ad4b519c6406fe23440a6e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a30c53fa505824c1d833a7849ed145480"><a name="a30c53fa505824c1d833a7849ed145480"></a><a name="a30c53fa505824c1d833a7849ed145480"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a0eccf357d6a1408692d5080802d238bb"><a name="a0eccf357d6a1408692d5080802d238bb"></a><a name="a0eccf357d6a1408692d5080802d238bb"></a>Name of a Loader link</p>
</td>
</tr>
<tr id="r8666a790886642ad8958b8e9d945fc5e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a48fe610ed41143ed9a2f2118bf34bfb7"><a name="a48fe610ed41143ed9a2f2118bf34bfb7"></a><a name="a48fe610ed41143ed9a2f2118bf34bfb7"></a>OBS Server</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aae564225866f46b4aa53ce9e72392038"><a name="aae564225866f46b4aa53ce9e72392038"></a><a name="aae564225866f46b4aa53ce9e72392038"></a>Enter the OBS endpoint address. The common format is <strong id="a2a9e6f49bb414734bdfaf88d73e449cc"><a name="a2a9e6f49bb414734bdfaf88d73e449cc"></a><a name="a2a9e6f49bb414734bdfaf88d73e449cc"></a>OBS.<em id="a1e6c3b47d2674e1e8ae86aa3d96ddabb"><a name="a1e6c3b47d2674e1e8ae86aa3d96ddabb"></a><a name="a1e6c3b47d2674e1e8ae86aa3d96ddabb"></a>Region</em>.<em id="abf6319cf39f14f7d9d3f3b447f3859c9"><a name="abf6319cf39f14f7d9d3f3b447f3859c9"></a><a name="abf6319cf39f14f7d9d3f3b447f3859c9"></a>DomainName</em></strong>.</p>
<p id="af4d2bd1239f44dfdbe937648c0b4a3b5"><a name="af4d2bd1239f44dfdbe937648c0b4a3b5"></a><a name="af4d2bd1239f44dfdbe937648c0b4a3b5"></a>For example, run the following command to view the OBS endpoint address:</p>
<p id="a587dfb6e51144d02941061ef43b48a3f"><a name="a587dfb6e51144d02941061ef43b48a3f"></a><a name="a587dfb6e51144d02941061ef43b48a3f"></a>cat /opt/Bigdata/apache-tomcat-7.0.78/webapps/web/WEB-INF/classes/cloud-obs.properties</p>
</td>
</tr>
<tr id="r007d276f2e1842849377f5d5e49128bf"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="aa8b74abad28a4ff28ee30a70a955dfff"><a name="aa8b74abad28a4ff28ee30a70a955dfff"></a><a name="aa8b74abad28a4ff28ee30a70a955dfff"></a>Port</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="adb5a4cac1ced497ab9a0bfa2e93cfa07"><a name="adb5a4cac1ced497ab9a0bfa2e93cfa07"></a><a name="adb5a4cac1ced497ab9a0bfa2e93cfa07"></a>Port for accessing OBS data. The default value is <span class="parmvalue" id="peafdcf0c0b9c47b6a37a054659794e98"><a name="peafdcf0c0b9c47b6a37a054659794e98"></a><a name="peafdcf0c0b9c47b6a37a054659794e98"></a><b>443</b></span>.</p>
</td>
</tr>
<tr id="r0fe57c838f69427ea1d3b8d266bb79fc"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="aa5a3ad9c85f1459bb6abca40b2dee6e5"><a name="aa5a3ad9c85f1459bb6abca40b2dee6e5"></a><a name="aa5a3ad9c85f1459bb6abca40b2dee6e5"></a>Access Key</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a5617d5ccece9405ca34f674025f36292"><a name="a5617d5ccece9405ca34f674025f36292"></a><a name="a5617d5ccece9405ca34f674025f36292"></a>AK for a user to access OBS</p>
</td>
</tr>
<tr id="r788cb0ebdb1a442a8d49f58fc3e3bb0f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ae376c4b35abb495f90ded20f1d28f9d3"><a name="ae376c4b35abb495f90ded20f1d28f9d3"></a><a name="ae376c4b35abb495f90ded20f1d28f9d3"></a>Security Key</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a20dc5bfd60184aeaa6093634384a0014"><a name="a20dc5bfd60184aeaa6093634384a0014"></a><a name="a20dc5bfd60184aeaa6093634384a0014"></a>SK corresponding to AK</p>
</td>
</tr>
</tbody>
</table>

## Relational Database Link<a name="s64e328eaa7bc48348ccd87d189851568"></a>

A relational database link is a data exchange channel between Loader and a relational database.  [Table 2](#t7b965fa024e54e9eae7c827e646a98ac)  describes the configuration parameters.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Some parameters are hidden by default. They appear only after you click  **Show Senior Parameter**.  

**Table  2** **generic-jdbc-connector**  configuration

<a name="t7b965fa024e54e9eae7c827e646a98ac"></a>
<table><thead align="left"><tr id="r41572a50bd6c400da911bf01e68319ba"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a9c35b25866864cdcbe7ffeb4bf155b34"><a name="a9c35b25866864cdcbe7ffeb4bf155b34"></a><a name="a9c35b25866864cdcbe7ffeb4bf155b34"></a><strong id="a8ece7e4180774ab582b9db0720daeea8"><a name="a8ece7e4180774ab582b9db0720daeea8"></a><a name="a8ece7e4180774ab582b9db0720daeea8"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="aab9f73cc6cdc49b69a7dddbaaff6acf3"><a name="aab9f73cc6cdc49b69a7dddbaaff6acf3"></a><a name="aab9f73cc6cdc49b69a7dddbaaff6acf3"></a><strong id="a53ac44529df64c90ba8d1fdb0b0145ad"><a name="a53ac44529df64c90ba8d1fdb0b0145ad"></a><a name="a53ac44529df64c90ba8d1fdb0b0145ad"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rcdc5ee77011e4830a3caf338df7d4738"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="aec605dec7a344ceda3f3790881af692d"><a name="aec605dec7a344ceda3f3790881af692d"></a><a name="aec605dec7a344ceda3f3790881af692d"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a9acaa996a69d4b499954584aa8a07c6e"><a name="a9acaa996a69d4b499954584aa8a07c6e"></a><a name="a9acaa996a69d4b499954584aa8a07c6e"></a>Name of a Loader link</p>
</td>
</tr>
<tr id="rb60ab3006149475ba429a92f3b5dfa57"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a9b0c5de93c9d4d08a343c9eba8629c16"><a name="a9b0c5de93c9d4d08a343c9eba8629c16"></a><a name="a9b0c5de93c9d4d08a343c9eba8629c16"></a>Database type</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ad02038b818f348ed9cb835ed6c096b32"><a name="ad02038b818f348ed9cb835ed6c096b32"></a><a name="ad02038b818f348ed9cb835ed6c096b32"></a>Data types supported by Loader links: <span class="parmvalue" id="pd7fb0028154a4ee79c899f4ed0f99223"><a name="pd7fb0028154a4ee79c899f4ed0f99223"></a><a name="pd7fb0028154a4ee79c899f4ed0f99223"></a><b>ORACLE</b></span>,&nbsp;<span class="parmvalue" id="pedfd7d03bc044044bb72e6a6534af343"><a name="pedfd7d03bc044044bb72e6a6534af343"></a><a name="pedfd7d03bc044044bb72e6a6534af343"></a><b>MYSQL</b></span>, and&nbsp;<span class="parmvalue" id="p38c33921a3c548729d2da74b8c3d16e1"><a name="p38c33921a3c548729d2da74b8c3d16e1"></a><a name="p38c33921a3c548729d2da74b8c3d16e1"></a><b>MPPDB</b></span></p>
</td>
</tr>
<tr id="r39f733d5b1954797bb2bacf13109d91e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a2f711f19a1814230b1ff610bc44eb595"><a name="a2f711f19a1814230b1ff610bc44eb595"></a><a name="a2f711f19a1814230b1ff610bc44eb595"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a744d15300ac84e3bb369ffa52a3ef961"><a name="a744d15300ac84e3bb369ffa52a3ef961"></a><a name="a744d15300ac84e3bb369ffa52a3ef961"></a>Database access address, which can be an IP address or domain name</p>
</td>
</tr>
<tr id="r568c47b6662349a9a94d3d10522b9e0d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ae30481dfd4ce40dabe7de1e78e6d66ba"><a name="ae30481dfd4ce40dabe7de1e78e6d66ba"></a><a name="ae30481dfd4ce40dabe7de1e78e6d66ba"></a>Port</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a9955895588164948a49bd74b741089dd"><a name="a9955895588164948a49bd74b741089dd"></a><a name="a9955895588164948a49bd74b741089dd"></a>Port for accessing the database</p>
</td>
</tr>
<tr id="rf08a1128432343f698e05fe5c8b520c6"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="aa8e7d23ae064488ba9647d2da11b6073"><a name="aa8e7d23ae064488ba9647d2da11b6073"></a><a name="aa8e7d23ae064488ba9647d2da11b6073"></a>Database</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a1bb368afa55045ff8062120b9fe722b2"><a name="a1bb368afa55045ff8062120b9fe722b2"></a><a name="a1bb368afa55045ff8062120b9fe722b2"></a>Name of the database saving data</p>
</td>
</tr>
<tr id="r5e77a74af0704366a7e6af463993a7ec"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a68ef4acea7524c41970fb28bcc8f0a74"><a name="a68ef4acea7524c41970fb28bcc8f0a74"></a><a name="a68ef4acea7524c41970fb28bcc8f0a74"></a>Username</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ad92c35d6334743f4b4d903ce3892bf02"><a name="ad92c35d6334743f4b4d903ce3892bf02"></a><a name="ad92c35d6334743f4b4d903ce3892bf02"></a>Username for accessing the database</p>
</td>
</tr>
<tr id="rc8838ac2653643efa29344388c135fde"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a8912daa0b3d448939569e475dc193eb0"><a name="a8912daa0b3d448939569e475dc193eb0"></a><a name="a8912daa0b3d448939569e475dc193eb0"></a>Password</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0070859523_p806192162119"><a name="en-us_topic_0070859523_p806192162119"></a><a name="en-us_topic_0070859523_p806192162119"></a>Password of the user. Use the actual password.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Senior parameter configuration

<a name="tf58c34d14d804f7999712bbaa4342f35"></a>
<table><thead align="left"><tr id="r1f6f0e47caba4c308f73dd58deb2ec84"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a021bf1f527ac40e0aa471d63eeef8966"><a name="a021bf1f527ac40e0aa471d63eeef8966"></a><a name="a021bf1f527ac40e0aa471d63eeef8966"></a><strong id="a38ef62cf96e846ba922dda8ac4c6ed75"><a name="a38ef62cf96e846ba922dda8ac4c6ed75"></a><a name="a38ef62cf96e846ba922dda8ac4c6ed75"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="aea9e22beeb6a47019813a46eda0bbf3c"><a name="aea9e22beeb6a47019813a46eda0bbf3c"></a><a name="aea9e22beeb6a47019813a46eda0bbf3c"></a><strong id="acc1c3abbe6194a308830b9a3cfe0db87"><a name="acc1c3abbe6194a308830b9a3cfe0db87"></a><a name="acc1c3abbe6194a308830b9a3cfe0db87"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="re5574fb3d3a445b8acd59f0c4374930f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="aefb938b53725485e95479c86cb9df692"><a name="aefb938b53725485e95479c86cb9df692"></a><a name="aefb938b53725485e95479c86cb9df692"></a>Fetch Size</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aa4e0d7d38fe842978b8ec54c5bf4967f"><a name="aa4e0d7d38fe842978b8ec54c5bf4967f"></a><a name="aa4e0d7d38fe842978b8ec54c5bf4967f"></a>A maximum volume of data obtained during each database access</p>
</td>
</tr>
<tr id="rf5f81b1bc0b04e31b45d19e48e3f7d03"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a9ad5e444f6264fd591b3ece3ecdc14f0"><a name="a9ad5e444f6264fd591b3ece3ecdc14f0"></a><a name="a9ad5e444f6264fd591b3ece3ecdc14f0"></a>Connection Properties</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aa545fcfad605424e8b0a9ddfc0e32996"><a name="aa545fcfad605424e8b0a9ddfc0e32996"></a><a name="aa545fcfad605424e8b0a9ddfc0e32996"></a>Driver properties exclusive to the database link that is supported by databases of different types, for example, <span class="parmname" id="p103d0baa4ff3429e8693e582d463197a"><a name="p103d0baa4ff3429e8693e582d463197a"></a><a name="p103d0baa4ff3429e8693e582d463197a"></a><b>autoReconnect</b></span>&nbsp;of MYSQL. If you want to define the driver properties, click&nbsp;<span class="uicontrol" id="u279a1937a6894c7aa665441d525b89d0"><a name="u279a1937a6894c7aa665441d525b89d0"></a><a name="u279a1937a6894c7aa665441d525b89d0"></a><b>Add</b></span>.</p>
</td>
</tr>
<tr id="rde43a107a56e4babb63d6628d6443f9c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="aafd48429f967435ab0a1094196e2962a"><a name="aafd48429f967435ab0a1094196e2962a"></a><a name="aafd48429f967435ab0a1094196e2962a"></a>Identifier enclose</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a269f41e185b941a39d930001055f497b"><a name="a269f41e185b941a39d930001055f497b"></a><a name="a269f41e185b941a39d930001055f497b"></a>Delimiter for reserving keywords in the database SQL. Delimiters defined in different databases vary.</p>
</td>
</tr>
</tbody>
</table>

## File Server Link<a name="sa997c8b34c734aea87d54e4db19ad4d4"></a>

File server links include FTP and SFTP links and serve as a data exchange channel between Loader and a file server.  [Table 4](#t9e0a10f830fa4547adb8dbfccaa016ce)  describes the configuration parameters.

**Table  4** **ftp-connector** or **sftp-connector**  configuration

<a name="t9e0a10f830fa4547adb8dbfccaa016ce"></a>
<table><thead align="left"><tr id="r9d050a2833514e3d98a76b9986b7bc48"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="ac0418370391c4dafb83c99971fda5650"><a name="ac0418370391c4dafb83c99971fda5650"></a><a name="ac0418370391c4dafb83c99971fda5650"></a><strong id="aca764c4f3ad643ccada2be2ca2d759c1"><a name="aca764c4f3ad643ccada2be2ca2d759c1"></a><a name="aca764c4f3ad643ccada2be2ca2d759c1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="ae7d64d65c34e489aa1f95f5395932356"><a name="ae7d64d65c34e489aa1f95f5395932356"></a><a name="ae7d64d65c34e489aa1f95f5395932356"></a><strong id="a066ef0cfe4514918ab6b0b2b5a7749e9"><a name="a066ef0cfe4514918ab6b0b2b5a7749e9"></a><a name="a066ef0cfe4514918ab6b0b2b5a7749e9"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r60d66c2f77ab4365a9ccd0557c031bf0"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a905829d20e0b4ee4b19bbb19228b4c96"><a name="a905829d20e0b4ee4b19bbb19228b4c96"></a><a name="a905829d20e0b4ee4b19bbb19228b4c96"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ab97ae38602014ede806c02f6ca674d55"><a name="ab97ae38602014ede806c02f6ca674d55"></a><a name="ab97ae38602014ede806c02f6ca674d55"></a>Name of a Loader link</p>
</td>
</tr>
<tr id="r8a71181432c4449dbb357cb817388403"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a7fffd7615fa84323b99216a0099749f4"><a name="a7fffd7615fa84323b99216a0099749f4"></a><a name="a7fffd7615fa84323b99216a0099749f4"></a>Hostname/IP</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ae03225b181bd4285875a2dedcebf76df"><a name="ae03225b181bd4285875a2dedcebf76df"></a><a name="ae03225b181bd4285875a2dedcebf76df"></a>Enter the file server access address, which can be a host name or IP address.</p>
</td>
</tr>
<tr id="r41f4553dc972489e87927f21b04f4706"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ab796f7486410466884d20a625f3218db"><a name="ab796f7486410466884d20a625f3218db"></a><a name="ab796f7486410466884d20a625f3218db"></a>Port</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a495966ee6c1944e1b5518e096facc4e1"><a name="a495966ee6c1944e1b5518e096facc4e1"></a><a name="a495966ee6c1944e1b5518e096facc4e1"></a>Port for accessing the file server.</p>
<a name="ude89e16174e644c6a398bf16313272df"></a><a name="ude89e16174e644c6a398bf16313272df"></a><ul id="ude89e16174e644c6a398bf16313272df"><li>Use port <span class="parmvalue" id="pff3ec188976547249ac06854412807b6"><a name="pff3ec188976547249ac06854412807b6"></a><a name="pff3ec188976547249ac06854412807b6"></a><b>21</b></span> for FTP.</li><li>Use port <span class="parmvalue" id="pe6dd16d4c8734de6902dedb234f6a967"><a name="pe6dd16d4c8734de6902dedb234f6a967"></a><a name="pe6dd16d4c8734de6902dedb234f6a967"></a><b>22</b></span> for SFTP.</li></ul>
</td>
</tr>
<tr id="r9e60dec797544391a34b2e767e58aa76"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a3d67840e427d4f89a94e9ef8f14d1b30"><a name="a3d67840e427d4f89a94e9ef8f14d1b30"></a><a name="a3d67840e427d4f89a94e9ef8f14d1b30"></a>Username</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aa862852dec444427a813ee7d94ca0ae2"><a name="aa862852dec444427a813ee7d94ca0ae2"></a><a name="aa862852dec444427a813ee7d94ca0ae2"></a>Username for logging in to the file server.</p>
</td>
</tr>
<tr id="r347b3337b54d45bfa7902f92d00fc4be"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a574a9df9f8034a349dc42b142c6525d5"><a name="a574a9df9f8034a349dc42b142c6525d5"></a><a name="a574a9df9f8034a349dc42b142c6525d5"></a>Password</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a2f4fbe84ed7b4197826a9fa73698018e"><a name="a2f4fbe84ed7b4197826a9fa73698018e"></a><a name="a2f4fbe84ed7b4197826a9fa73698018e"></a>Password of the user</p>
</td>
</tr>
</tbody>
</table>

## MRS Cluster Link<a name="s9ed8034e9c6a45518e2a5bc6bb9fc075"></a>

MRS cluster links include HBase, HDFS, and Hive links and serve as a data exchange channel between Loader and data.

When configuring an MRS cluster name and link, select a connector, for example,  **hbase-connector**, **hdfs-connector**, or **hive-connector**, and save it.

## VoltDB Link<a name="s8a192ed47cb24f9587b1750d58d62e13"></a>

A VoltDB link is a data exchange channel between Loader and an in-memory database.  [Table 5](#t76dfb1ab507a481c9c0bfa01ca9c3899)  describes the configuration parameters.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Some parameters are hidden by default. They appear only after you click  **Show Senior Parameter**.  

**Table  5** **voltdb-connector**  configuration

<a name="t76dfb1ab507a481c9c0bfa01ca9c3899"></a>
<table><thead align="left"><tr id="r81f3d20511a74dcabeace66835905ad7"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a95ee08ebe2a14d48b17ba876fc666d60"><a name="a95ee08ebe2a14d48b17ba876fc666d60"></a><a name="a95ee08ebe2a14d48b17ba876fc666d60"></a><strong id="a26ead1c4d3ab430f99529fb983ae65af"><a name="a26ead1c4d3ab430f99529fb983ae65af"></a><a name="a26ead1c4d3ab430f99529fb983ae65af"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="aac4b10171b1a4e32865325882d2d19bb"><a name="aac4b10171b1a4e32865325882d2d19bb"></a><a name="aac4b10171b1a4e32865325882d2d19bb"></a><strong id="a1392d918e08d4fc1af884d4a50300970"><a name="a1392d918e08d4fc1af884d4a50300970"></a><a name="a1392d918e08d4fc1af884d4a50300970"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra5f2cd820e2f4f9b836404d61001b6cf"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ad950a97deafd4905904fd5550d77848f"><a name="ad950a97deafd4905904fd5550d77848f"></a><a name="ad950a97deafd4905904fd5550d77848f"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="acd4edb5b23df49e892856c4b489b1160"><a name="acd4edb5b23df49e892856c4b489b1160"></a><a name="acd4edb5b23df49e892856c4b489b1160"></a>Name of a Loader link</p>
</td>
</tr>
<tr id="rbc3430c1783247da836721fa38249d6a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="af77a9e4d1eb142efbee87193ef6bf5be"><a name="af77a9e4d1eb142efbee87193ef6bf5be"></a><a name="af77a9e4d1eb142efbee87193ef6bf5be"></a>Database servers</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0070859523_p856836816354"><a name="en-us_topic_0070859523_p856836816354"></a><a name="en-us_topic_0070859523_p856836816354"></a>Database access address, which can be an IP address or domain name. You can configure multiple database addresses and separate them by comma (,).</p>
</td>
</tr>
<tr id="r8079fa04935740b39017bca81497d678"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0070859523_p521594416354"><a name="en-us_topic_0070859523_p521594416354"></a><a name="en-us_topic_0070859523_p521594416354"></a>Port</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="af349dc1b886c4154af28d903277956c8"><a name="af349dc1b886c4154af28d903277956c8"></a><a name="af349dc1b886c4154af28d903277956c8"></a>Port for accessing the database</p>
</td>
</tr>
<tr id="r98c6e78a9b014b46a146d55847c6e3e3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ab04eb9ccb39c4999ba27d91cd88229df"><a name="ab04eb9ccb39c4999ba27d91cd88229df"></a><a name="ab04eb9ccb39c4999ba27d91cd88229df"></a>Username</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0070859523_p853035416354"><a name="en-us_topic_0070859523_p853035416354"></a><a name="en-us_topic_0070859523_p853035416354"></a>Username for accessing the database</p>
</td>
</tr>
<tr id="rb55f5978c4214cdd974f9fcb4e097564"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ab9f420bc9ec7423e976337367c0e3c25"><a name="ab9f420bc9ec7423e976337367c0e3c25"></a><a name="ab9f420bc9ec7423e976337367c0e3c25"></a>Password</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aa586f0aa031940d288fe8155b404141c"><a name="aa586f0aa031940d288fe8155b404141c"></a><a name="aa586f0aa031940d288fe8155b404141c"></a>Password of the user. Use the actual password.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Senior parameter configuration

<a name="t91d663e88e5a46c0bbf59bf388ba5387"></a>
<table><thead align="left"><tr id="r5ac29bc03c9c49319f87c0d984b55166"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a545b95fa344c49199c997add7bd7b1a7"><a name="a545b95fa344c49199c997add7bd7b1a7"></a><a name="a545b95fa344c49199c997add7bd7b1a7"></a><strong id="a1beb6e5b529241d3a0ebd8b8d14d5808"><a name="a1beb6e5b529241d3a0ebd8b8d14d5808"></a><a name="a1beb6e5b529241d3a0ebd8b8d14d5808"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="aebb7253d42124ea5a7d5304a581264c7"><a name="aebb7253d42124ea5a7d5304a581264c7"></a><a name="aebb7253d42124ea5a7d5304a581264c7"></a><strong id="abb59e7c0c161430682d79a67b6bd4ad1"><a name="abb59e7c0c161430682d79a67b6bd4ad1"></a><a name="abb59e7c0c161430682d79a67b6bd4ad1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rb7837f7180624f0fa5545ca45e4faa4c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a08ed884cb48c4130a8e16b93f0713916"><a name="a08ed884cb48c4130a8e16b93f0713916"></a><a name="a08ed884cb48c4130a8e16b93f0713916"></a>Connection Properties</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a0fee72f4891b49d9bde9d04819790396"><a name="a0fee72f4891b49d9bde9d04819790396"></a><a name="a0fee72f4891b49d9bde9d04819790396"></a>Delimiter for reserving keywords in the memory database SQL</p>
</td>
</tr>
</tbody>
</table>

