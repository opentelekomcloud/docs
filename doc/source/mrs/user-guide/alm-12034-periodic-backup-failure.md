# ALM-12034 Periodic Backup Failure<a name="EN-US_TOPIC_0125375759"></a>

## Description<a name="se790b9daaa4148fb9f59abeb85842d69"></a>

This alarm is generated when a periodic backup task fails to be executed and is cleared when the next backup task is executed successfully.

## Attribute<a name="s434fc822a4ba43f3ad7307f1600dd1aa"></a>

<a name="tc2cdedb7b6b140678d449aa369cbe782"></a>
<table><thead align="left"><tr id="ra96c9ab69a974b79927b5f200e3776fa"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="ad7002d289c57444b99505f6b1728a4db"><a name="ad7002d289c57444b99505f6b1728a4db"></a><a name="ad7002d289c57444b99505f6b1728a4db"></a><strong id="aa504cfcbbec34921a689f17ee2a665fc"><a name="aa504cfcbbec34921a689f17ee2a665fc"></a><a name="aa504cfcbbec34921a689f17ee2a665fc"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a24a0ad11e015417d83cb5503eecab438"><a name="a24a0ad11e015417d83cb5503eecab438"></a><a name="a24a0ad11e015417d83cb5503eecab438"></a><strong id="a2d88e4f155b840fb9a7e2a26e7ea7c81"><a name="a2d88e4f155b840fb9a7e2a26e7ea7c81"></a><a name="a2d88e4f155b840fb9a7e2a26e7ea7c81"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a5262484e543846b791a99959bc434361"><a name="a5262484e543846b791a99959bc434361"></a><a name="a5262484e543846b791a99959bc434361"></a><strong id="ab7d93f0f497d413c8dfd8d7604d9166f"><a name="ab7d93f0f497d413c8dfd8d7604d9166f"></a><a name="ab7d93f0f497d413c8dfd8d7604d9166f"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r1523cd611d814cd0bbb3b80db792d2d7"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a6bafb630a9c743f3a182fce644d3fcba"><a name="a6bafb630a9c743f3a182fce644d3fcba"></a><a name="a6bafb630a9c743f3a182fce644d3fcba"></a>12034</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a80c784ea9e82466d9db3b014bd307848"><a name="a80c784ea9e82466d9db3b014bd307848"></a><a name="a80c784ea9e82466d9db3b014bd307848"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a6980779d142f482598910af72a59835d"><a name="a6980779d142f482598910af72a59835d"></a><a name="a6980779d142f482598910af72a59835d"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s2d9ff46048f64820bbfce263ce656568"></a>

<a name="td5d734efbea74f49850598392c031b12"></a>
<table><thead align="left"><tr id="r1b3e3aee9f3b4455af93044607d63bbe"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a90fd21e983fe43d3ab6e5bbfbf0988f0"><a name="a90fd21e983fe43d3ab6e5bbfbf0988f0"></a><a name="a90fd21e983fe43d3ab6e5bbfbf0988f0"></a><strong id="a940f9fe6bfad4b50b536b3ca2a4f9745"><a name="a940f9fe6bfad4b50b536b3ca2a4f9745"></a><a name="a940f9fe6bfad4b50b536b3ca2a4f9745"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a90c1e05e2c6e4111be04fac9fd7f7339"><a name="a90c1e05e2c6e4111be04fac9fd7f7339"></a><a name="a90c1e05e2c6e4111be04fac9fd7f7339"></a><strong id="aacde826d121e414b911e724ce70cdd16"><a name="aacde826d121e414b911e724ce70cdd16"></a><a name="aacde826d121e414b911e724ce70cdd16"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r1004d167d4304d509ade1f32d34800cf"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035512808_p271279511447"><a name="en-us_topic_0035512808_p271279511447"></a><a name="en-us_topic_0035512808_p271279511447"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a14e98f6366474b9384abc02dba843921"><a name="a14e98f6366474b9384abc02dba843921"></a><a name="a14e98f6366474b9384abc02dba843921"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rb1300ef5cd5f4ac5a1a6a5bc8f896b09"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7b77c76cb11f426687e5d03f9a4a7dea"><a name="a7b77c76cb11f426687e5d03f9a4a7dea"></a><a name="a7b77c76cb11f426687e5d03f9a4a7dea"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a87a788ab2eda4666ae95b96314ce4b41"><a name="a87a788ab2eda4666ae95b96314ce4b41"></a><a name="a87a788ab2eda4666ae95b96314ce4b41"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rb68e27026dc74ca9a8a482e5938736d6"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a68359f8c7d894c928599d2dd5c1c8f56"><a name="a68359f8c7d894c928599d2dd5c1c8f56"></a><a name="a68359f8c7d894c928599d2dd5c1c8f56"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="acd9b2ea18daf482ea28a2b2ba2769605"><a name="acd9b2ea18daf482ea28a2b2ba2769605"></a><a name="acd9b2ea18daf482ea28a2b2ba2769605"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r2870eb8829954a5bb62fef251da5d47e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aff9f8427bccf4b8bb8b1d9ecc894401a"><a name="aff9f8427bccf4b8bb8b1d9ecc894401a"></a><a name="aff9f8427bccf4b8bb8b1d9ecc894401a"></a>TaskName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7d0fc9b4c5554bf29e87e26f2ca9b7c8"><a name="a7d0fc9b4c5554bf29e87e26f2ca9b7c8"></a><a name="a7d0fc9b4c5554bf29e87e26f2ca9b7c8"></a>Specifies the task.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s8d5f774dcb0f4f51876c0f1d18497213"></a>

No backup package is available, so the system cannot be restored if faults occur.

## Possible Causes<a name="sed056df960a641508a2ceb3d062b8637"></a>

The alarm cause depends on the task details. Handle the alarm according to the logs and alarm details.

## Procedure<a name="s862625fdc3c847119b1514810338c0f1"></a>

Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s9416496488b949ce8e1f7e1c2066d9b1"></a>

N/A

