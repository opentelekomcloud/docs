# Modifying a Password Policy<a name="EN-US_TOPIC_0125375952"></a>

## Scenario<a name="s39357d050bc2477589e45c5cabc919ec"></a>

This section describes how to set password and user login security rules as well as user lock rules. Password policies set on MRS Manager take effect for  **Human-machine** users only, because the passwords of **Machine-machine**  users are randomly generated.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Modify password policies based on service security requirements, because they involve user management security. Otherwise, security risks may be caused.  

## Procedure<a name="s3ec793747bd34bc0bc31577f800ea3b7"></a>

1.  On MRS Manager, click  **System**.
2.  Click  **Configure Password Policy**.
3.  Modify password policies as prompted. For parameter details, see  [Table 1](#tfc7068de781549959cd756ce4b688ba9).

    **Table  1**  Password policy parameter description

    <a name="tfc7068de781549959cd756ce4b688ba9"></a>
    <table><thead align="left"><tr id="rb4436688c04741dfa5bf4e06f4a0f5c9"><th class="cellrowborder" valign="top" width="45%" id="mcps1.2.3.1.1"><p id="a63767f7cf8a04837a1e4e51f5e47d072"><a name="a63767f7cf8a04837a1e4e51f5e47d072"></a><a name="a63767f7cf8a04837a1e4e51f5e47d072"></a><strong id="af940ff353b754416ac63e73e6f1c1572"><a name="af940ff353b754416ac63e73e6f1c1572"></a><a name="af940ff353b754416ac63e73e6f1c1572"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.3.1.2"><p id="ab35f2af090a14051ac6a38b2ff3f08dd"><a name="ab35f2af090a14051ac6a38b2ff3f08dd"></a><a name="ab35f2af090a14051ac6a38b2ff3f08dd"></a><strong id="afba015a6048a43c8aeffafd2677f0dc7"><a name="afba015a6048a43c8aeffafd2677f0dc7"></a><a name="afba015a6048a43c8aeffafd2677f0dc7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r379ee863766a4bfcbeb7eddc5872f943"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="a8182f0d98eb84a52a86c13b01725e579"><a name="a8182f0d98eb84a52a86c13b01725e579"></a><a name="a8182f0d98eb84a52a86c13b01725e579"></a><span class="parmname" id="p4a21c1399cf146c2b1cf3fb51362e75d"><a name="p4a21c1399cf146c2b1cf3fb51362e75d"></a><a name="p4a21c1399cf146c2b1cf3fb51362e75d"></a><b>Minimum Password Length</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="a7955e33f597e4f26bb8d1b1805275122"><a name="a7955e33f597e4f26bb8d1b1805275122"></a><a name="a7955e33f597e4f26bb8d1b1805275122"></a>Indicates the minimum number of characters a password contains. The value ranges from 6 to 32. The default value is <strong id="b575100421528"><a name="b575100421528"></a><a name="b575100421528"></a>6</strong>.</p>
    </td>
    </tr>
    <tr id="red99468b013948fe84dcab5d98c22190"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="a02d41ad714a748fc82f267be3cd996a3"><a name="a02d41ad714a748fc82f267be3cd996a3"></a><a name="a02d41ad714a748fc82f267be3cd996a3"></a><span class="parmname" id="p8b0004a4b57b475da981344420873ca1"><a name="p8b0004a4b57b475da981344420873ca1"></a><a name="p8b0004a4b57b475da981344420873ca1"></a><b>Number of Character Types</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="a28ebf829094448fe942c271bc7bbe7ce"><a name="a28ebf829094448fe942c271bc7bbe7ce"></a><a name="a28ebf829094448fe942c271bc7bbe7ce"></a>Indicates the minimum number of character types a password contains. The character types are uppercase letters, lowercase letters, digits, spaces, and special characters (~`!?,.:;-_'(){}[]/&lt;&gt;@#$%^&amp;*+|\=). The value can be 4 or 5. The default value is <strong id="b6240304915219"><a name="b6240304915219"></a><a name="b6240304915219"></a>2</strong>, which means that a password must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, special characters, and spaces.</p>
    </td>
    </tr>
    <tr id="re89760a23e42432aaecf7b2217ab0b6b"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="a615c9275a60145a7ae1e5dc9152ef959"><a name="a615c9275a60145a7ae1e5dc9152ef959"></a><a name="a615c9275a60145a7ae1e5dc9152ef959"></a><span class="parmname" id="p9a9b4a6d087047ff9fae7119932cd260"><a name="p9a9b4a6d087047ff9fae7119932cd260"></a><a name="p9a9b4a6d087047ff9fae7119932cd260"></a><b>Password Validity Period (days)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="a8bf27b42452b4506b94859ee6fbb0b74"><a name="a8bf27b42452b4506b94859ee6fbb0b74"></a><a name="a8bf27b42452b4506b94859ee6fbb0b74"></a>Indicates the validity period (days) of a password. The value ranges from 0 to 90. 0 means that the password is permanently valid. The default value is <strong id="a2eb38a5002e4498e931f295ecc2a7fc2"><a name="a2eb38a5002e4498e931f295ecc2a7fc2"></a><a name="a2eb38a5002e4498e931f295ecc2a7fc2"></a>90</strong>.</p>
    </td>
    </tr>
    <tr id="row3074002793956"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="p691426993956"><a name="p691426993956"></a><a name="p691426993956"></a><strong id="b58651589142651"><a name="b58651589142651"></a><a name="b58651589142651"></a>Password Expiration Notification Days</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="p2318494093956"><a name="p2318494093956"></a><a name="p2318494093956"></a>It is used to notify password expiration in advance. After the value is set, if the difference between the cluster time and the password expiration time is smaller than this value, the user receives password expiration notifications. When logging in to MRS Manager, the user will be notified that the password is about to expire and a message is displayed asking the user to change the password. The value ranges from <strong id="b5188088394059"><a name="b5188088394059"></a><a name="b5188088394059"></a>0</strong>&nbsp;to&nbsp;<em id="i4110379411"><a name="i4110379411"></a><a name="i4110379411"></a>X</em>&nbsp;(<em id="i409305529416"><a name="i409305529416"></a><a name="i409305529416"></a>X</em>&nbsp;must be set to the half of the password validity period and rounded down). Value&nbsp;<strong id="b5892405094110"><a name="b5892405094110"></a><a name="b5892405094110"></a>0</strong>&nbsp;indicates that no notification is sent. The default value is&nbsp;<strong id="b4632029894118"><a name="b4632029894118"></a><a name="b4632029894118"></a>5</strong>.</p>
    </td>
    </tr>
    <tr id="r53456b21828f476990880cc90d5f2163"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="a5d873043eda84b61af5a9c629cfbb246"><a name="a5d873043eda84b61af5a9c629cfbb246"></a><a name="a5d873043eda84b61af5a9c629cfbb246"></a><span class="parmname" id="p11bf84796eeb4246865a9d516cc0b7d2"><a name="p11bf84796eeb4246865a9d516cc0b7d2"></a><a name="p11bf84796eeb4246865a9d516cc0b7d2"></a><b>Interval of Resetting Authentication Failure Count (min)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="a36aac459ba034c37a399a8ee75db80e6"><a name="a36aac459ba034c37a399a8ee75db80e6"></a><a name="a36aac459ba034c37a399a8ee75db80e6"></a>Indicates the interval (minutes) of retaining incorrect password attempts. The value ranges from 0 to 1440. 0 indicates that incorrect password attempts are permanently retained and 1440 indicates that incorrect password attempts are retained for one day. The default value is <strong id="ace2d69cd20d24e6eb44f5a4dc1ec8206"><a name="ace2d69cd20d24e6eb44f5a4dc1ec8206"></a><a name="ace2d69cd20d24e6eb44f5a4dc1ec8206"></a>5</strong>.</p>
    </td>
    </tr>
    <tr id="r456306a4f8fc4cf4bcee6bdca8bd52c3"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="a5ada26335e364c319cd071a07bd4621f"><a name="a5ada26335e364c319cd071a07bd4621f"></a><a name="a5ada26335e364c319cd071a07bd4621f"></a><span class="parmname" id="pdf885d3b5176499fa414e45c492666e7"><a name="pdf885d3b5176499fa414e45c492666e7"></a><a name="pdf885d3b5176499fa414e45c492666e7"></a><b>Number of Password Retries</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="a09255ef215564914adb2a3728f3e98c1"><a name="a09255ef215564914adb2a3728f3e98c1"></a><a name="a09255ef215564914adb2a3728f3e98c1"></a>Indicates the number of consecutive wrong passwords allowed before the system locks the user. The value ranges from 3 to 30. The default value is <strong id="a6b5f0d6d1d194678be459ada04187934"><a name="a6b5f0d6d1d194678be459ada04187934"></a><a name="a6b5f0d6d1d194678be459ada04187934"></a>5</strong>.</p>
    </td>
    </tr>
    <tr id="r213d58a63d474559996c7b44d7351fad"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.3.1.1 "><p id="a01661286aa9a490a92d3c899e3355c3f"><a name="a01661286aa9a490a92d3c899e3355c3f"></a><a name="a01661286aa9a490a92d3c899e3355c3f"></a><span class="parmname" id="p59f04237f09f4b3b87bb9a4a37c69a5d"><a name="p59f04237f09f4b3b87bb9a4a37c69a5d"></a><a name="p59f04237f09f4b3b87bb9a4a37c69a5d"></a><b>Account Lock Duration (min)</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.3.1.2 "><p id="a669dc4d383d0491dae5c5a3569b707e3"><a name="a669dc4d383d0491dae5c5a3569b707e3"></a><a name="a669dc4d383d0491dae5c5a3569b707e3"></a>Indicates the time period during which a user is locked when the user lockout conditions are met. The value ranges from 5 to 120. The default value is <strong id="a50136e5fe2674317a2219cd3388f2af6"><a name="a50136e5fe2674317a2219cd3388f2af6"></a><a name="a50136e5fe2674317a2219cd3388f2af6"></a>5</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


