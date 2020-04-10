# Logging In to a Node<a name="cce_01_0185"></a>

## Constraints<a name="section1492661620507"></a>

-   If you use SSH to log in to a node \(an ECS\), ensure that the ECS already has an EIP \(a public IP address\).
-   Only login to a running ECS is allowed.
-   Only the user  **linux**  can log in to a Linux ECS.

## Login Modes<a name="section1391822316511"></a>

You can log in to an ECS in either of the following modes:

-   Management console \(VNC\)

    If an ECS has no EIP, log in to the ECS console and click  **Remote Login**  in the same row as the ECS.

    For details, see  [Login Using VNC](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0093263550.html).

-   SSH

    This mode applies only to ECSs running Linux. Usually, you can use a remote login tool, such as PuTTY, XShell, and SecureCRT, to log in to your ECS. If none of the remote login tools can be used, log in to the ECS console and click  **Remote Login**  in the same row as the ECS to view the connection status and running status of the ECS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   When you use the Windows OS to log in to a Linux node, set  **Auto-login username**  to linux.  
    >-   The CCE console does not support node OS upgrade. Do not upgrade the node OS using YUM. Otherwise, the container network will be unavailable.  


**Table  1**  Linux ECS login modes

<a name="table8204165071419"></a>
<table><thead align="left"><tr id="row192061050201414"><th class="cellrowborder" valign="top" width="18.061806180618063%" id="mcps1.2.4.1.1"><p id="p8206135011143"><a name="p8206135011143"></a><a name="p8206135011143"></a>EIP Binding</p>
</th>
<th class="cellrowborder" valign="top" width="20.312031203120313%" id="mcps1.2.4.1.2"><p id="p15206250101419"><a name="p15206250101419"></a><a name="p15206250101419"></a>On-Premises OS</p>
</th>
<th class="cellrowborder" valign="top" width="61.626162616261624%" id="mcps1.2.4.1.3"><p id="p112061550171411"><a name="p112061550171411"></a><a name="p112061550171411"></a>Connection Method</p>
</th>
</tr>
</thead>
<tbody><tr id="row94594911172"><td class="cellrowborder" valign="top" width="18.061806180618063%" headers="mcps1.2.4.1.1 "><p id="p2808101311171"><a name="p2808101311171"></a><a name="p2808101311171"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.312031203120313%" headers="mcps1.2.4.1.2 "><p id="p48080138173"><a name="p48080138173"></a><a name="p48080138173"></a>Windows</p>
</td>
<td class="cellrowborder" valign="top" width="61.626162616261624%" headers="mcps1.2.4.1.3 "><p id="p1065011512466"><a name="p1065011512466"></a><a name="p1065011512466"></a>Use remote login tools such as PuTTY and Xshell.</p>
<p id="p146111921720"><a name="p146111921720"></a><a name="p146111921720"></a>For details, see "Logging In to the Linux ECS from Local Windows" in <a href="https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0017955380.html" target="_blank" rel="noopener noreferrer">Login Using an SSH Key</a>.</p>
</td>
</tr>
<tr id="row14822105881716"><td class="cellrowborder" valign="top" width="18.061806180618063%" headers="mcps1.2.4.1.1 "><p id="p141559316187"><a name="p141559316187"></a><a name="p141559316187"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.312031203120313%" headers="mcps1.2.4.1.2 "><p id="p1815593101813"><a name="p1815593101813"></a><a name="p1815593101813"></a>Linux</p>
</td>
<td class="cellrowborder" valign="top" width="61.626162616261624%" headers="mcps1.2.4.1.3 "><p id="p865975924510"><a name="p865975924510"></a><a name="p865975924510"></a>Run commands.</p>
<p id="p1082285816172"><a name="p1082285816172"></a><a name="p1082285816172"></a>For details, see "Logging In to the Linux ECS from Local Windows" in <a href="https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0017955633.html" target="_blank" rel="noopener noreferrer">Login Using an SSH Password</a></p>
</td>
</tr>
<tr id="row0207145014149"><td class="cellrowborder" valign="top" width="18.061806180618063%" headers="mcps1.2.4.1.1 "><p id="p13383131101518"><a name="p13383131101518"></a><a name="p13383131101518"></a>Yes/No</p>
</td>
<td class="cellrowborder" valign="top" width="20.312031203120313%" headers="mcps1.2.4.1.2 "><p id="p5383813159"><a name="p5383813159"></a><a name="p5383813159"></a>Windows/Linux</p>
</td>
<td class="cellrowborder" valign="top" width="61.626162616261624%" headers="mcps1.2.4.1.3 "><p id="p238317110159"><a name="p238317110159"></a><a name="p238317110159"></a>For details, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0093263550.html" target="_blank" rel="noopener noreferrer">Login Using VNC</a>.</p>
</td>
</tr>
</tbody>
</table>

