# ALM-12038 Monitoring Indicator Dump Failure<a name="EN-US_TOPIC_0125375562"></a>

## Description<a name="s1de1c6b317ef4017a3f9e23801af10b7"></a>

This alarm is generated when dump fails after monitoring indicator dump is configured on MRS Manager and is cleared when dump is successful.

## Attribute<a name="sc30aacbfa7bc47b68a22b8da02cb1c6c"></a>

<a name="t227626b2e39545a6b85de56016b6a154"></a>
<table><thead align="left"><tr id="r4c44dee2219e4aa58c6a605b6a1bec39"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="af6a50dd334924f83bd90b5a0487f0543"><a name="af6a50dd334924f83bd90b5a0487f0543"></a><a name="af6a50dd334924f83bd90b5a0487f0543"></a><strong id="a15f1717be42243d7a242d67eb69e263a"><a name="a15f1717be42243d7a242d67eb69e263a"></a><a name="a15f1717be42243d7a242d67eb69e263a"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a0690af0574884c76ab369bb9aeded0ab"><a name="a0690af0574884c76ab369bb9aeded0ab"></a><a name="a0690af0574884c76ab369bb9aeded0ab"></a><strong id="a751ba63b52dd4b79ac6e76a766e205de"><a name="a751ba63b52dd4b79ac6e76a766e205de"></a><a name="a751ba63b52dd4b79ac6e76a766e205de"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a3dc51ba6ab484e72a1e644833b0c8d9a"><a name="a3dc51ba6ab484e72a1e644833b0c8d9a"></a><a name="a3dc51ba6ab484e72a1e644833b0c8d9a"></a><strong id="ae55441750d674e4a87da00b14aca7a60"><a name="ae55441750d674e4a87da00b14aca7a60"></a><a name="ae55441750d674e4a87da00b14aca7a60"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r1ac20d410fdc4c16958724437a55bff0"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a0d1d78a43c094686aade0f97cae4b8c8"><a name="a0d1d78a43c094686aade0f97cae4b8c8"></a><a name="a0d1d78a43c094686aade0f97cae4b8c8"></a>12038</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a2437fe7a4d564ea9a663094ba0971a2c"><a name="a2437fe7a4d564ea9a663094ba0971a2c"></a><a name="a2437fe7a4d564ea9a663094ba0971a2c"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a2730b3e621b846f1ace73f2a1bcb3c82"><a name="a2730b3e621b846f1ace73f2a1bcb3c82"></a><a name="a2730b3e621b846f1ace73f2a1bcb3c82"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s840cd05cecba4fbeae8d8e77dde6177a"></a>

<a name="tc7aba0d5b4794c999a901afe71d424c5"></a>
<table><thead align="left"><tr id="r8ba5746016c44ee9a4097e0dfdc3b464"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a321b8916c35d46e7b8d84568d1e5f98a"><a name="a321b8916c35d46e7b8d84568d1e5f98a"></a><a name="a321b8916c35d46e7b8d84568d1e5f98a"></a><strong id="abb4a01678bb7476fbb60a29ee6dc1baa"><a name="abb4a01678bb7476fbb60a29ee6dc1baa"></a><a name="abb4a01678bb7476fbb60a29ee6dc1baa"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="afe2ea806386249e3a348d7f42b9914cd"><a name="afe2ea806386249e3a348d7f42b9914cd"></a><a name="afe2ea806386249e3a348d7f42b9914cd"></a><strong id="a4d1994c2aa5b48ef8e55f75ba3849637"><a name="a4d1994c2aa5b48ef8e55f75ba3849637"></a><a name="a4d1994c2aa5b48ef8e55f75ba3849637"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc41cae021c284500b9a7c5f23ed25f77"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="acc2daf1311c94eeeaecdc7ce85926cce"><a name="acc2daf1311c94eeeaecdc7ce85926cce"></a><a name="acc2daf1311c94eeeaecdc7ce85926cce"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af1c9835ea0304417952fe0f92b045856"><a name="af1c9835ea0304417952fe0f92b045856"></a><a name="af1c9835ea0304417952fe0f92b045856"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r3bd2fcd8c6164a10ba45045f7fe64479"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8cc57775168d4ebbbd29db0f8ebb2415"><a name="a8cc57775168d4ebbbd29db0f8ebb2415"></a><a name="a8cc57775168d4ebbbd29db0f8ebb2415"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af4c1f56c76964dafbb974bc8ff98832c"><a name="af4c1f56c76964dafbb974bc8ff98832c"></a><a name="af4c1f56c76964dafbb974bc8ff98832c"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rd84cda2757634d62b41ac8b5cc6c6684"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a955b6bb549c8412c8681e980ce8664c8"><a name="a955b6bb549c8412c8681e980ce8664c8"></a><a name="a955b6bb549c8412c8681e980ce8664c8"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0fad911c8aa44d88bdbcae94a0417faa"><a name="a0fad911c8aa44d88bdbcae94a0417faa"></a><a name="a0fad911c8aa44d88bdbcae94a0417faa"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s0e97f733a6ff493d9a524dc6462f94dc"></a>

The upper-layer management system fails to obtain monitoring indicators from the MRS Manager system.

## Possible Causes<a name="s5302e1982cc94cfc9f359310cdd331d5"></a>

-   The server cannot be connected.
-   The save path on the server cannot be accessed.
-   The monitoring indicator file fails to be uploaded.

## Procedure<a name="sfb5ab0ba089a43d19cb1aee5eb214011"></a>

1.  Contact the public cloud O&M personnel to check whether the network connection between the MRS Manager system and the server is in the normal state.
    -   If yes, go to  [3](#l8b75ef02a06945c0ab3bdc93d2b34296).
    -   If no, go to  [2](#l7b72acc905b1421f9541cc112751ad3c).

2.  <a name="l7b72acc905b1421f9541cc112751ad3c"></a>Contact the public cloud O&M personnel to restore the network and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [3](#l8b75ef02a06945c0ab3bdc93d2b34296).

3.  <a name="l8b75ef02a06945c0ab3bdc93d2b34296"></a>Choose  **System**  \>  **Configure Monitoring Metric Dump**  and check whether the FTP username, password, port, dump mode, and public key that are configured on the configuration page for monitoring indicator dumping are consistent with those on the server.
    -   If yes, go to  [5](#l72c6fdbd6185410bbe2c539d4981a13e).
    -   If no, go to  [4](#l549f948633634cbb940afdc1f6eb8626).

4.  <a name="l549f948633634cbb940afdc1f6eb8626"></a>Enter the correct configuration information, click  **OK**, and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [5](#l72c6fdbd6185410bbe2c539d4981a13e).

5.  <a name="l72c6fdbd6185410bbe2c539d4981a13e"></a>Choose  **System**  \>  **Configure Monitoring Metric Dump** and check the configuration items, including **FTP Username**, **Save Path**, and **Dump Mode**.
    -   If the dumping mode is FTP, go to  [6](#lc2adfd698e1945f192cd41682ddcb06e).
    -   If the dumping mode is SFTP, go to  [7](#lc401c37dbcd542c3aabb34060a7d4fb5).

6.  <a name="lc2adfd698e1945f192cd41682ddcb06e"></a>Log in to the server in FTP mode. In the default path, check whether the relative path  **Save Path** has the read and write permission on **FTP Username**.
    -   If yes, go to  [9](#l1b2d677ea931473092f6f526d9271c30).
    -   If no, go to  [8](#l6389db1b34eb44c0b9463ae9497953cf).

7.  <a name="lc401c37dbcd542c3aabb34060a7d4fb5"></a>Log in to the server in FTP mode. In the default path, check whether the absolute path  **Save Path** has the read and write permission on **FTP Username**.
    -   If yes, go to  [9](#l1b2d677ea931473092f6f526d9271c30).
    -   If no, go to  [8](#l6389db1b34eb44c0b9463ae9497953cf).

8.  <a name="l6389db1b34eb44c0b9463ae9497953cf"></a>Add the read and write permission and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [9](#l1b2d677ea931473092f6f526d9271c30).

9.  <a name="l1b2d677ea931473092f6f526d9271c30"></a>Log in to the server and check whether the save path has sufficient disk space.
    -   If yes, go to  [11](#l9389e0ac38e241fd9a683093d8b59904).
    -   If no, go to  [10](#l0fb71409f53e4832a5f3c6a06864644c).

10. <a name="l0fb71409f53e4832a5f3c6a06864644c"></a>Delete any unnecessary files or go to the configuration page for monitoring indicator dumping to change the save path. Check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [11](#l9389e0ac38e241fd9a683093d8b59904).

11. <a name="l9389e0ac38e241fd9a683093d8b59904"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s86a485a57356472684095bcb196c2a1d"></a>

N/A

