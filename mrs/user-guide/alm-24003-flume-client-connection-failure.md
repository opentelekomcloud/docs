# ALM-24003 Flume Client Connection Failure<a name="EN-US_TOPIC_0125376062"></a>

## Description<a name="s86d9374a664c4d1a813bffb40f845179"></a>

The alarm module monitors the port connection status on the Flume server. This alarm is generated when the Flume server fails to receive a connection message from the Flume client in 3 consecutive minutes.

This alarm is cleared when the Flume server receives a connection message from the Flume client.

## Attribute<a name="s2e07bbc9d7bc4a40925cec3416af7c67"></a>

<a name="tf77208f57fbf4d63b02681071cef8d55"></a>
<table><thead align="left"><tr id="r98950981343b4f5e8da83aa4f8312b9d"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aa36ddd1a39554a199a248bc9f65e8f70"><a name="aa36ddd1a39554a199a248bc9f65e8f70"></a><a name="aa36ddd1a39554a199a248bc9f65e8f70"></a><strong id="abdb291b880b64cb7a28fb3c105e3838c"><a name="abdb291b880b64cb7a28fb3c105e3838c"></a><a name="abdb291b880b64cb7a28fb3c105e3838c"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a3e7cc104a53840188fca048f5117d0af"><a name="a3e7cc104a53840188fca048f5117d0af"></a><a name="a3e7cc104a53840188fca048f5117d0af"></a><strong id="adce282f722c04ada9f66e1da7b5007e6"><a name="adce282f722c04ada9f66e1da7b5007e6"></a><a name="adce282f722c04ada9f66e1da7b5007e6"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a9ee8965c634b414a99dc2cbb5810c194"><a name="a9ee8965c634b414a99dc2cbb5810c194"></a><a name="a9ee8965c634b414a99dc2cbb5810c194"></a><strong id="afe1b441fac4b4305bb557282739c84eb"><a name="afe1b441fac4b4305bb557282739c84eb"></a><a name="afe1b441fac4b4305bb557282739c84eb"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="raf0b486824f14f1c87d17462982f087b"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a8666162603b44b4d98b66bcad087b5c1"><a name="a8666162603b44b4d98b66bcad087b5c1"></a><a name="a8666162603b44b4d98b66bcad087b5c1"></a>24003</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="afb77631bc27545dfb951821b455a5cca"><a name="afb77631bc27545dfb951821b455a5cca"></a><a name="afb77631bc27545dfb951821b455a5cca"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a494698839be34bde8427f391189779d8"><a name="a494698839be34bde8427f391189779d8"></a><a name="a494698839be34bde8427f391189779d8"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sebf6c94f77f04527b339e093ba4efc17"></a>

<a name="t8a0a6fd6b8a5478fbcb7984e7b14bd70"></a>
<table><thead align="left"><tr id="r00f1f520c1be4e9396d7db8f276b6235"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a0048db6bd279428396b009587198fe42"><a name="a0048db6bd279428396b009587198fe42"></a><a name="a0048db6bd279428396b009587198fe42"></a><strong id="a8cde74eb89b34ae3ab18ffb25047ac49"><a name="a8cde74eb89b34ae3ab18ffb25047ac49"></a><a name="a8cde74eb89b34ae3ab18ffb25047ac49"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a7eb94e83f93d48f9a0628837ab30a532"><a name="a7eb94e83f93d48f9a0628837ab30a532"></a><a name="a7eb94e83f93d48f9a0628837ab30a532"></a><strong id="a3b9d4e78c1a0490790a13850de4c5d2b"><a name="a3b9d4e78c1a0490790a13850de4c5d2b"></a><a name="a3b9d4e78c1a0490790a13850de4c5d2b"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r5b643b26f54849ecb057843502d11f83"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a663066f739f84a5496406249e749fbb5"><a name="a663066f739f84a5496406249e749fbb5"></a><a name="a663066f739f84a5496406249e749fbb5"></a>ClientIP</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="adebcf2c64ff2492ba28004e96e698313"><a name="adebcf2c64ff2492ba28004e96e698313"></a><a name="adebcf2c64ff2492ba28004e96e698313"></a>Specifies the IP address of the Flume client.</p>
</td>
</tr>
<tr id="r8b8cb7b827c84704b490a58e4da6fba7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a859680a967414bb1bc22f4a8fe80eb63"><a name="a859680a967414bb1bc22f4a8fe80eb63"></a><a name="a859680a967414bb1bc22f4a8fe80eb63"></a>ServerIP</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5d5c46a947d942ca8a237b466484625a"><a name="a5d5c46a947d942ca8a237b466484625a"></a><a name="a5d5c46a947d942ca8a237b466484625a"></a>Specifies the IP address of the Flume server.</p>
</td>
</tr>
<tr id="r748a53a5066446c3adcfbe01b9e2d374"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0054336021_p720032162819"><a name="en-us_topic_0054336021_p720032162819"></a><a name="en-us_topic_0054336021_p720032162819"></a>ServerPort</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aa948a068a88a4b178f6da0cda3fcefeb"><a name="aa948a068a88a4b178f6da0cda3fcefeb"></a><a name="aa948a068a88a4b178f6da0cda3fcefeb"></a>Specifies the port on the Flume server.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s058a33b08f1243aaab9495007528df13"></a>

The communication between the Flume client and server fails. The Flume client cannot send data to the Flume server.

## Possible Causes<a name="s6f4e0c2d547c457ab0f1b0377d5f4f21"></a>

-   The network between the Flume client and server is faulty.
-   The Flume client's process is abnormal.
-   The Flume client is incorrectly configured.

## Procedure<a name="s847690158a184e80b5b3a32f88a06ff3"></a>

1.  Check the network between the Flume client and server.
    1.  Log in to the host where the alarmed Flume client resides. Run the following command to switch to user  **root**:

        **sudo su - root**

    2.  Run the  **ping** _Flume server IP address_  command to check whether the network between the Flume client and server is normal.
        -   If yes, go to  [2.a](#l0888a1fa16174b3f88fb78a4d974dc60).
        -   If no, go to  [4.a](#lca6cf9497b1041bcb641c7852c2cc969).

2.  Check whether the Flume client's process is normal.
    1.  <a name="l0888a1fa16174b3f88fb78a4d974dc60"></a>Log in to the host where the alarmed Flume client resides. Run the following command to switch to user  **root**:

        **sudo su - root**

    2.  Run the  **ps -ef|grep flume |grep client**  command to check whether the Flume client process exists.
        -   If yes, go to  [3.a](#l8f04b4e819964b81979cfd34ecad3c07).
        -   If no, go to  [4.a](#lca6cf9497b1041bcb641c7852c2cc969).

3.  Check the Flume client configuration.
    1.  <a name="l8f04b4e819964b81979cfd34ecad3c07"></a>Log in to the host where the alarmed Flume client resides. Run the following command to switch to user  **root**:

        **sudo su - root**

    2.  Run the  **cd** _Flume installation directory_**/fusioninsight-flume-1.6.0/conf/**  command to go to Flume's configuration directory.
    3.  Run the  **cat properties.properties**  command to query the current configuration file of the Flume client.
    4.  Check whether the  **properties.properties**  file is correctly configured according to the configuration description of the Flume agent.
        -   If yes, go to  [3.e](#l841615bc0da34d31aac9fc79fd70c4f8).
        -   If no, go to  [4.a](#lca6cf9497b1041bcb641c7852c2cc969).

    5.  <a name="l841615bc0da34d31aac9fc79fd70c4f8"></a>Modify the  **properties.properties**  configuration file.
    6.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#lca6cf9497b1041bcb641c7852c2cc969).

4.  Collect fault information.
    1.  <a name="lca6cf9497b1041bcb641c7852c2cc969"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sd5bf3a9eb50f41c797d75881447f264f"></a>

N/A

