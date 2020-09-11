# Configuring the System<a name="en-us_topic_0045853630"></a>

This section describes how to modify system configurations.

## Procedure<a name="sbde3d45bbc9a455f985ba2f7b92bbbbc"></a>

1.  Log in to OBS Browser.
2.  In the upper right corner of OBS Browser, click  ![](figures/icon-setting.png)  and choose  **System Configuration**. The  **System Configuration**  dialog box is displayed, see  [Figure 1](#fig42068739173655).

    **Figure  1**  Configuring the system<a name="fig42068739173655"></a>  
    ![](figures/configuring-the-system.png "configuring-the-system")

3.  Click  **General**  and modify basic parameters as required.

    [Table 1](#t5b000a761ce742d3a008e78296aa7e23)  describes the parameters that can be modified.

    **Table  1**  General configuration parameters

    <a name="t5b000a761ce742d3a008e78296aa7e23"></a>
    <table><thead align="left"><tr id="rfc94c5f5c90a40ad972e6d88fa20f45b"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="a62b8385fa14a4105b2468a7d054c5d2e"><a name="a62b8385fa14a4105b2468a7d054c5d2e"></a><a name="a62b8385fa14a4105b2468a7d054c5d2e"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="ae69cbd7e88f34342b8f5096e91bff04e"><a name="ae69cbd7e88f34342b8f5096e91bff04e"></a><a name="ae69cbd7e88f34342b8f5096e91bff04e"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rdb7f5ea2a4d74adf91a7682afdb7f55a"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="adfec0a920ba04816b079cbcc34cd4dab"><a name="adfec0a920ba04816b079cbcc34cd4dab"></a><a name="adfec0a920ba04816b079cbcc34cd4dab"></a>Enable HTTPS</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="afc071fbcfdf240bf8db9256ad7baacea"><a name="afc071fbcfdf240bf8db9256ad7baacea"></a><a name="afc071fbcfdf240bf8db9256ad7baacea"></a>If this option is selected, all communication information is encrypted and transferred to OBS over HTTPS.</p>
    </td>
    </tr>
    <tr id="row4738349017324"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p1285744417324"><a name="p1285744417324"></a><a name="p1285744417324"></a>Enable certificate verification</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p3482005917324"><a name="p3482005917324"></a><a name="p3482005917324"></a>When this option is selected, the client will verify the server certificate.</p>
    </td>
    </tr>
    <tr id="row19413122016318"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p14413220133116"><a name="p14413220133116"></a><a name="p14413220133116"></a>Enable KMS encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p491734533119"><a name="p491734533119"></a><a name="p491734533119"></a>When <strong id="a22ebe824789d43b597a5225cea7fc452"><a name="a22ebe824789d43b597a5225cea7fc452"></a><a name="a22ebe824789d43b597a5225cea7fc452"></a>Enable HTTPS</strong> and <strong id="a2444a51a15c24295b5cc3d329a370b7e"><a name="a2444a51a15c24295b5cc3d329a370b7e"></a><a name="a2444a51a15c24295b5cc3d329a370b7e"></a>Enable KMS encryption</strong> are selected, KMS encryption will be implemented for all objects uploaded to OBS.</p>
    </td>
    </tr>
    <tr id="r9d15bd3a61304c50b4a10db1b16925a0"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="a132962e2f4524b5d8a2f88403ae4f77c"><a name="a132962e2f4524b5d8a2f88403ae4f77c"></a><a name="a132962e2f4524b5d8a2f88403ae4f77c"></a>Multipart Upload, Part Size (MB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="af70fafbad2854bf6b27334eeeba60205"><a name="af70fafbad2854bf6b27334eeeba60205"></a><a name="af70fafbad2854bf6b27334eeeba60205"></a>Objects whose size is larger than the specified part size (5 MB by default) are segmented and uploaded at the OBS background. The size of each part can be set in this dialog box. The value of <strong id="b2101885531161958"><a name="b2101885531161958"></a><a name="b2101885531161958"></a>Part Size (MB)</strong> can range from 5 MB to 5 GB.</p>
    <div class="note" id="n9e51b629c15d48a298363e92b7bf6dea"><a name="n9e51b629c15d48a298363e92b7bf6dea"></a><a name="n9e51b629c15d48a298363e92b7bf6dea"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="a691932aa2cb04490bb10a8762bc8d051"><a name="a691932aa2cb04490bb10a8762bc8d051"></a><a name="a691932aa2cb04490bb10a8762bc8d051"></a>Multipart upload is used by default. Recommended settings of <strong id="b35010965113018"><a name="b35010965113018"></a><a name="b35010965113018"></a>Part Size (MB)</strong> are as follows:</p>
    <p class="textintable" id="ad311b703bed74dbc9022d8020ecc98e7"><a name="ad311b703bed74dbc9022d8020ecc98e7"></a><a name="ad311b703bed74dbc9022d8020ecc98e7"></a>To maximize client performance, set <strong id="a4b013af2e67c4b0a9010deead1b30e9b"><a name="a4b013af2e67c4b0a9010deead1b30e9b"></a><a name="a4b013af2e67c4b0a9010deead1b30e9b"></a>Part Size (MB)</strong> based on the upload speed. You are advised to set the <strong id="b1353816100111817"><a name="b1353816100111817"></a><a name="b1353816100111817"></a>Part Size (MB)</strong> value larger than the maximum upload speed. For example, if the maximum upload speed is 10 MB/s, set <strong id="a7d866fbffd3a406794b97a2bc6280517"><a name="a7d866fbffd3a406794b97a2bc6280517"></a><a name="a7d866fbffd3a406794b97a2bc6280517"></a>Part Size (MB)</strong> to an integer greater than 10 MB. It is recommended that the part size be set to a value two to three times the maximum upload speed.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r88b5ad2d934b424f8e157781e9436d43"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="a532027aaefee454199b89f4387ea435e"><a name="a532027aaefee454199b89f4387ea435e"></a><a name="a532027aaefee454199b89f4387ea435e"></a>Max Number of Upload Tasks</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="a7a16a5ea0764416daaa08d97eae1c4fd"><a name="a7a16a5ea0764416daaa08d97eae1c4fd"></a><a name="a7a16a5ea0764416daaa08d97eae1c4fd"></a>Specifies the maximum number of upload tasks. Enter an integer ranging from 2 to 20.</p>
    </td>
    </tr>
    <tr id="rb637bccab7c44ddcb9b24df68c58d0ec"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="abe704fe194774e3e8f814c7b27e851bc"><a name="abe704fe194774e3e8f814c7b27e851bc"></a><a name="abe704fe194774e3e8f814c7b27e851bc"></a>Max Number of Download Tasks</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="a3a1bd2c33d274f5d942eddc07a5363c1"><a name="a3a1bd2c33d274f5d942eddc07a5363c1"></a><a name="a3a1bd2c33d274f5d942eddc07a5363c1"></a>Specifies the maximum number of download tasks. Enter an integer ranging from 5 to 50.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Network**  and set proxy server information as required. See  [Figure 2](#fig543149173827).

    **Figure  2**  Network configurations<a name="fig543149173827"></a>  
    ![](figures/network-configurations.png "network-configurations")

    **Table  2**  Network configuration parameters

    <a name="t2cfc046d12034a839cfcf75e8cf8d10b"></a>
    <table><thead align="left"><tr id="r0490806c5cb5479da3ea9bc271e9302b"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="a5fb752a46e8d4c0693e4c0252427f697"><a name="a5fb752a46e8d4c0693e4c0252427f697"></a><a name="a5fb752a46e8d4c0693e4c0252427f697"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="a69e6d93152234df8924ce9bfd4caface"><a name="a69e6d93152234df8924ce9bfd4caface"></a><a name="a69e6d93152234df8924ce9bfd4caface"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5d619d0924594f0ea5a7e192c9512dce"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="a84ae2cb1419341779c5c75689d62bc74"><a name="a84ae2cb1419341779c5c75689d62bc74"></a><a name="a84ae2cb1419341779c5c75689d62bc74"></a>Enable proxy</p>
    </td>
    <td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="a01bf42ec6e244394a5c2544097a2a1d2"><a name="a01bf42ec6e244394a5c2544097a2a1d2"></a><a name="a01bf42ec6e244394a5c2544097a2a1d2"></a>If this option is selected, the <strong id="ada6624bfe80a43b5a6acf143ba321586"><a name="ada6624bfe80a43b5a6acf143ba321586"></a><a name="ada6624bfe80a43b5a6acf143ba321586"></a>Authentication</strong> option is displayed. Set the following parameters to access OBS through the proxy server:</p>
    <a name="u12af2c34ad70412eb298ce10202467ec"></a><a name="u12af2c34ad70412eb298ce10202467ec"></a><ul id="u12af2c34ad70412eb298ce10202467ec"><li>Address: domain name or IP address of the proxy server</li><li>Port: port of the proxy server (default port is <strong id="a99cd61de49444b87b58e1a743cf16cd2"><a name="a99cd61de49444b87b58e1a743cf16cd2"></a><a name="a99cd61de49444b87b58e1a743cf16cd2"></a>8080</strong>)</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Other**  and set the parameters as required. For details, see  [Figure 3](#fig2876079495946).

    **Figure  3**  Other configurations<a name="fig2876079495946"></a>  
    ![](figures/other-configurations.png "other-configurations")

    **Table  3**  Other parameters

    <a name="t4528f80de97241ccaf60a840dfadb52d"></a>
    <table><thead align="left"><tr id="rb8a4d9d54d524899bcc64f29d2f08ff2"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="a3abde8af0d3f46ff8988aec6bc5faf55"><a name="a3abde8af0d3f46ff8988aec6bc5faf55"></a><a name="a3abde8af0d3f46ff8988aec6bc5faf55"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="aed5e9885ff704ea1b7a9989600707872"><a name="aed5e9885ff704ea1b7a9989600707872"></a><a name="aed5e9885ff704ea1b7a9989600707872"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="re13f6930f0be4e25bd9c8468b8047b12"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="a7ccabcfe43ae4a6c8dff62aef3d66956"><a name="a7ccabcfe43ae4a6c8dff62aef3d66956"></a><a name="a7ccabcfe43ae4a6c8dff62aef3d66956"></a>Enable automatic update check</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="aa43e80355aff410bad82e9709b7d6142"><a name="aa43e80355aff410bad82e9709b7d6142"></a><a name="aa43e80355aff410bad82e9709b7d6142"></a>If this option is selected, each time when you log in to OBS Browser, a check will be automatically performed to determine whether the current software version is the latest.</p>
    </td>
    </tr>
    <tr id="re936197711a94bde9f51b425081d8979"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="a58a7827108c6490f846b1f18d5cb51c8"><a name="a58a7827108c6490f846b1f18d5cb51c8"></a><a name="a58a7827108c6490f846b1f18d5cb51c8"></a>Number of Objects Displayed on Each Page</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="acab87eb7829b49ba95dc38dfe66586a7"><a name="acab87eb7829b49ba95dc38dfe66586a7"></a><a name="acab87eb7829b49ba95dc38dfe66586a7"></a>Set the number of objects that are displayed on each page. The default value is 100. The value ranges from 50 to 300. After setting the value, click the <a name="image0359833184910"></a><a name="image0359833184910"></a><span><img id="image0359833184910" src="figures/icon-fresh.png"></span> button in the upper right corner of the page so that the setting takes effect.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Save**  to save the system configuration.

