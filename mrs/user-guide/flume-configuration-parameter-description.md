# Flume Configuration Parameter Description<a name="EN-US_TOPIC_0125375494"></a>

## Scenario<a name="s454afc1cd99b461ea10dbc8d65277765"></a>

This section describes how to configure the sources, channels, and sinks of Flume, and modify the configuration items of each module.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You must input encrypted information for some configurations. For details on how to encrypt information, see  [Using the Encryption Tool of the Flume Client](using-the-encryption-tool-of-the-flume-client.md).  

## Common Source Configurations<a name="s48f55eafe7fa40498b2ef96286541327"></a>

-   **Avro Source**

    An Avro source listens to the Avro port, receives data from the external Avro client, and places data into configured channels. Common configurations are as follows.

    **Table  1**  Common configurations of an Avro source

    <a name="t597fe57e59464498823a61c122d2ee7f"></a>
    <table><thead align="left"><tr id="rf9ea0151184a4ed0ba388e6827db316e"><th class="cellrowborder" valign="top" width="30.209999999999997%" id="mcps1.2.4.1.1"><p id="a4d26a93e1bc845afbfcc4387b7f636b2"><a name="a4d26a93e1bc845afbfcc4387b7f636b2"></a><a name="a4d26a93e1bc845afbfcc4387b7f636b2"></a><strong id="a8c9a68a3fd944215a9a1230f1d540f59"><a name="a8c9a68a3fd944215a9a1230f1d540f59"></a><a name="a8c9a68a3fd944215a9a1230f1d540f59"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="a450b8a58ec1f424392873cbcb773d241"><a name="a450b8a58ec1f424392873cbcb773d241"></a><a name="a450b8a58ec1f424392873cbcb773d241"></a><strong id="a642dfc75d2734644ad628b35329d1956"><a name="a642dfc75d2734644ad628b35329d1956"></a><a name="a642dfc75d2734644ad628b35329d1956"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.79%" id="mcps1.2.4.1.3"><p id="a2897fc16178e40e988d643622cbc4d6b"><a name="a2897fc16178e40e988d643622cbc4d6b"></a><a name="a2897fc16178e40e988d643622cbc4d6b"></a><strong id="af5e5cd649f144f4fbcf50aaa9d06bc7e"><a name="af5e5cd649f144f4fbcf50aaa9d06bc7e"></a><a name="af5e5cd649f144f4fbcf50aaa9d06bc7e"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ra0dbb11496634f19be753a3286362922"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="a846d8cde1dca4ee79362c8ae5b0b336d"><a name="a846d8cde1dca4ee79362c8ae5b0b336d"></a><a name="a846d8cde1dca4ee79362c8ae5b0b336d"></a>channels</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="afb060101e28d4502ba021f7e6fac7242"><a name="afb060101e28d4502ba021f7e6fac7242"></a><a name="afb060101e28d4502ba021f7e6fac7242"></a><strong id="af0c7b94b75544eaba2e089e15124b389"><a name="af0c7b94b75544eaba2e089e15124b389"></a><a name="af0c7b94b75544eaba2e089e15124b389"></a>-</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="af482108458704571ae8e3935a7228c55"><a name="af482108458704571ae8e3935a7228c55"></a><a name="af482108458704571ae8e3935a7228c55"></a>Channel connected to the source. Multiple channels can be configured but must be separated by spaces.</p>
    <p id="en-us_topic_0066459131_p938226317465"><a name="en-us_topic_0066459131_p938226317465"></a><a name="en-us_topic_0066459131_p938226317465"></a>To define the flow within a single agent, you need to link the sources and sinks via a channel. A source instance can specify multiple channels, but a sink instance can only specify one channel.</p>
    <p id="en-us_topic_0066459131_p194537817528"><a name="en-us_topic_0066459131_p194537817528"></a><a name="en-us_topic_0066459131_p194537817528"></a>The format is as follows:</p>
    <p id="a5a0318680976464da94edc96db7bf92b"><a name="a5a0318680976464da94edc96db7bf92b"></a><a name="a5a0318680976464da94edc96db7bf92b"></a><strong id="a4a61ec2bcbfb435f8be723a270063f77"><a name="a4a61ec2bcbfb435f8be723a270063f77"></a><a name="a4a61ec2bcbfb435f8be723a270063f77"></a>&lt;Agent &gt;.sources.&lt;Source&gt;.channels = &lt;channel1&gt; &lt;channel2&gt; &lt;channel3&gt;...</strong></p>
    <p id="aeeb82b6937f34705b6d49bc90333ced1"><a name="aeeb82b6937f34705b6d49bc90333ced1"></a><a name="aeeb82b6937f34705b6d49bc90333ced1"></a><strong id="a85c52fb3087f49f9b994c8933cb66003"><a name="a85c52fb3087f49f9b994c8933cb66003"></a><a name="a85c52fb3087f49f9b994c8933cb66003"></a>&lt;Agent &gt;.sinks.&lt;Sink&gt;.channels = &lt;channel1&gt;</strong></p>
    </td>
    </tr>
    <tr id="r8e5d3ea783a24eebaa41714d84c01f30"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="ae1da017a68f7469db54823c9e2222119"><a name="ae1da017a68f7469db54823c9e2222119"></a><a name="ae1da017a68f7469db54823c9e2222119"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a31bdae100d044ec5844c23f0031b6bfc"><a name="a31bdae100d044ec5844c23f0031b6bfc"></a><a name="a31bdae100d044ec5844c23f0031b6bfc"></a>avro</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="a4b46884996c145aaa8164378e8f37330"><a name="a4b46884996c145aaa8164378e8f37330"></a><a name="a4b46884996c145aaa8164378e8f37330"></a>Type, which is set to <span class="parmvalue" id="pb6dd803efd22453ca704ee0aa1cc451d"><a name="pb6dd803efd22453ca704ee0aa1cc451d"></a><a name="pb6dd803efd22453ca704ee0aa1cc451d"></a><b>avro</b></span>. The type of each source is fixed.</p>
    </td>
    </tr>
    <tr id="r30cc651e98db4f859243fc1280dffa15"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="a6aac8644cb9e4890a6965cd46a3e0986"><a name="a6aac8644cb9e4890a6965cd46a3e0986"></a><a name="a6aac8644cb9e4890a6965cd46a3e0986"></a>bind</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a239ed46fc0b14424adacfec3adc534c4"><a name="a239ed46fc0b14424adacfec3adc534c4"></a><a name="a239ed46fc0b14424adacfec3adc534c4"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="add89b16ac6b54b71a5b3d6d0179526e9"><a name="add89b16ac6b54b71a5b3d6d0179526e9"></a><a name="add89b16ac6b54b71a5b3d6d0179526e9"></a>Bind to the host name or IP address that is associated with the source.</p>
    </td>
    </tr>
    <tr id="r326ea5a5d6ae41fc821c79fa4f9ed118"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="ab65a47c198ed4ca89797bd36d944bbe6"><a name="ab65a47c198ed4ca89797bd36d944bbe6"></a><a name="ab65a47c198ed4ca89797bd36d944bbe6"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1c9eb91e7f15478b8a56fc2500eb48c7"><a name="a1c9eb91e7f15478b8a56fc2500eb48c7"></a><a name="a1c9eb91e7f15478b8a56fc2500eb48c7"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="a2371027b8d8844608119849ab7f1ac1b"><a name="a2371027b8d8844608119849ab7f1ac1b"></a><a name="a2371027b8d8844608119849ab7f1ac1b"></a>Bound port</p>
    </td>
    </tr>
    <tr id="r87a95a35db0a4d8ebff32e4a396fe09e"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="a0b54bf48439a4833abad0c6ed65ba9d2"><a name="a0b54bf48439a4833abad0c6ed65ba9d2"></a><a name="a0b54bf48439a4833abad0c6ed65ba9d2"></a>ssl</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a069ecf9c46c641d281af3d849a6421c5"><a name="a069ecf9c46c641d281af3d849a6421c5"></a><a name="a069ecf9c46c641d281af3d849a6421c5"></a>false</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="afcf97e7737c146bb86041c5814e3b1e6"><a name="afcf97e7737c146bb86041c5814e3b1e6"></a><a name="afcf97e7737c146bb86041c5814e3b1e6"></a>Indicates whether to use SSL encryption.</p>
    <a name="ud16ab1727e7343958506ca2ad2e3fa96"></a><a name="ud16ab1727e7343958506ca2ad2e3fa96"></a><ul id="ud16ab1727e7343958506ca2ad2e3fa96"><li>true</li><li>false</li></ul>
    </td>
    </tr>
    <tr id="ra5a4aebe06c743429b4a52b943790922"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="a9fef493c3f0f4bc097cb16972d6886bb"><a name="a9fef493c3f0f4bc097cb16972d6886bb"></a><a name="a9fef493c3f0f4bc097cb16972d6886bb"></a>truststore-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ab9492f789792409280a2b801201bec00"><a name="ab9492f789792409280a2b801201bec00"></a><a name="ab9492f789792409280a2b801201bec00"></a>JKS</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="aec5456eae04b4f1896c6ac892d21bbd6"><a name="aec5456eae04b4f1896c6ac892d21bbd6"></a><a name="aec5456eae04b4f1896c6ac892d21bbd6"></a>Java truststore type. Enter JKS or other supported Java truststore type<span id="p1a29f0e794254ba8a753689bdbbb9418"><a name="p1a29f0e794254ba8a753689bdbbb9418"></a><a name="p1a29f0e794254ba8a753689bdbbb9418"></a>.</span></p>
    </td>
    </tr>
    <tr id="r307f389b12904a4f8656f33e97a66228"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="a0593aead76f54415924fb1b595056246"><a name="a0593aead76f54415924fb1b595056246"></a><a name="a0593aead76f54415924fb1b595056246"></a>truststore</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a9928b1bf2f52495db460db15517b0be1"><a name="a9928b1bf2f52495db460db15517b0be1"></a><a name="a9928b1bf2f52495db460db15517b0be1"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="a63703b6c96294e55b74fbd2cbab61eab"><a name="a63703b6c96294e55b74fbd2cbab61eab"></a><a name="a63703b6c96294e55b74fbd2cbab61eab"></a>Java truststore file.</p>
    </td>
    </tr>
    <tr id="r2d5c620eced44c7bb5e8984dffcd659c"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="ad647a1616b574fed93b3ef78bcc9c0f1"><a name="ad647a1616b574fed93b3ef78bcc9c0f1"></a><a name="ad647a1616b574fed93b3ef78bcc9c0f1"></a>truststore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="afd09414cc08a42e3a286875882593610"><a name="afd09414cc08a42e3a286875882593610"></a><a name="afd09414cc08a42e3a286875882593610"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="aa3127cbf84994e4f881fbca727c3d261"><a name="aa3127cbf84994e4f881fbca727c3d261"></a><a name="aa3127cbf84994e4f881fbca727c3d261"></a>Java truststore password.</p>
    </td>
    </tr>
    <tr id="r246caa697f4740c6a56a63660ecb50d8"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="ad0cf2fa62d2a43e3878c77872ec0dd15"><a name="ad0cf2fa62d2a43e3878c77872ec0dd15"></a><a name="ad0cf2fa62d2a43e3878c77872ec0dd15"></a>keystore-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ab997f883210343ba8a38ebb80a8d558e"><a name="ab997f883210343ba8a38ebb80a8d558e"></a><a name="ab997f883210343ba8a38ebb80a8d558e"></a>JKS</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="a485c7719d8e3421dbf86b463aeafa5e1"><a name="a485c7719d8e3421dbf86b463aeafa5e1"></a><a name="a485c7719d8e3421dbf86b463aeafa5e1"></a>Keystore type. Enter JKS or other supported Java keystore type<span id="en-us_topic_0066459131_ph9860219121"><a name="en-us_topic_0066459131_ph9860219121"></a><a name="en-us_topic_0066459131_ph9860219121"></a>.</span></p>
    </td>
    </tr>
    <tr id="rb6832ed9e7a94689a28c46cec1fc132f"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="a4d4d8b18163b439c8b9ed076fd1b6a40"><a name="a4d4d8b18163b439c8b9ed076fd1b6a40"></a><a name="a4d4d8b18163b439c8b9ed076fd1b6a40"></a>keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ae0e35ba39b614793bd278a0a9ed9158a"><a name="ae0e35ba39b614793bd278a0a9ed9158a"></a><a name="ae0e35ba39b614793bd278a0a9ed9158a"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="a1d4f8600932244fe938ccd44e1390855"><a name="a1d4f8600932244fe938ccd44e1390855"></a><a name="a1d4f8600932244fe938ccd44e1390855"></a>Keystore file.</p>
    </td>
    </tr>
    <tr id="r37401d3479b94e1ba4b48a4e02f77944"><td class="cellrowborder" valign="top" width="30.209999999999997%" headers="mcps1.2.4.1.1 "><p id="a42c916fb7aec4f32a62ab02e37cf07c0"><a name="a42c916fb7aec4f32a62ab02e37cf07c0"></a><a name="a42c916fb7aec4f32a62ab02e37cf07c0"></a>keystore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ae098d147ac354acc96a8e0f914a448c1"><a name="ae098d147ac354acc96a8e0f914a448c1"></a><a name="ae098d147ac354acc96a8e0f914a448c1"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.79%" headers="mcps1.2.4.1.3 "><p id="acd0d3840b1254fcfbd91dd2bc6b413b6"><a name="acd0d3840b1254fcfbd91dd2bc6b413b6"></a><a name="acd0d3840b1254fcfbd91dd2bc6b413b6"></a>Keystore password.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Spooling Source**

    A Spooling source monitors and transmits new files that have been added to directories in quasi-real-time mode. Common configurations are as follows.

    **Table  2**  Common configurations of a Spooling source

    <a name="t64306cc4f48a48febfc9ae7400805de3"></a>
    <table><thead align="left"><tr id="r7efe216c66ab41a4862b55d5bf32499e"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="a0d8ca7f7fe15457c99edcc0122dd4581"><a name="a0d8ca7f7fe15457c99edcc0122dd4581"></a><a name="a0d8ca7f7fe15457c99edcc0122dd4581"></a><strong id="a61bb8ac4ca51423284d4d0111a1c023a"><a name="a61bb8ac4ca51423284d4d0111a1c023a"></a><a name="a61bb8ac4ca51423284d4d0111a1c023a"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="a993894154df84c9f88d5eb02f4435c5a"><a name="a993894154df84c9f88d5eb02f4435c5a"></a><a name="a993894154df84c9f88d5eb02f4435c5a"></a><strong id="ad11fea447c2b49e585b6d0a38209841f"><a name="ad11fea447c2b49e585b6d0a38209841f"></a><a name="ad11fea447c2b49e585b6d0a38209841f"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="ae25360d5dfa04a2bba669bfca6c1f9e7"><a name="ae25360d5dfa04a2bba669bfca6c1f9e7"></a><a name="ae25360d5dfa04a2bba669bfca6c1f9e7"></a><strong id="a108b593c7b5d40e0b9097ea6efcd7762"><a name="a108b593c7b5d40e0b9097ea6efcd7762"></a><a name="a108b593c7b5d40e0b9097ea6efcd7762"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r9bec175749e14ff89526eb7155977d99"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ab07f7bd935e14cfaad1b2248dc7f54a8"><a name="ab07f7bd935e14cfaad1b2248dc7f54a8"></a><a name="ab07f7bd935e14cfaad1b2248dc7f54a8"></a>channels</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1c448c222b61472894936aa92a1105e6"><a name="a1c448c222b61472894936aa92a1105e6"></a><a name="a1c448c222b61472894936aa92a1105e6"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a40c449baf79d44e0be1c800af2a45249"><a name="a40c449baf79d44e0be1c800af2a45249"></a><a name="a40c449baf79d44e0be1c800af2a45249"></a>Channel connected to the source. Multiple channels can be configured.</p>
    </td>
    </tr>
    <tr id="rd87f2a44aef14dabb7170e81a79e7c5c"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a4e30013c42eb467b9ecb2558dce88481"><a name="a4e30013c42eb467b9ecb2558dce88481"></a><a name="a4e30013c42eb467b9ecb2558dce88481"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aaa6f2d29ce0140d0bd359599bd01a5b7"><a name="aaa6f2d29ce0140d0bd359599bd01a5b7"></a><a name="aaa6f2d29ce0140d0bd359599bd01a5b7"></a>spooldir</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2559ef9ecd0146eda55843d1b1aa6b7e"><a name="a2559ef9ecd0146eda55843d1b1aa6b7e"></a><a name="a2559ef9ecd0146eda55843d1b1aa6b7e"></a>Type, which is set to <span class="parmvalue" id="p1f0e8c2525aa43bab66384ea20a37749"><a name="p1f0e8c2525aa43bab66384ea20a37749"></a><a name="p1f0e8c2525aa43bab66384ea20a37749"></a><b>spooldir</b></span>.</p>
    </td>
    </tr>
    <tr id="rad4323fd48a94872b8b6e219e8d75526"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a72c0f5504b8f431793dcd99e37e28653"><a name="a72c0f5504b8f431793dcd99e37e28653"></a><a name="a72c0f5504b8f431793dcd99e37e28653"></a>monTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a393a05b5315245199779ed8738691f16"><a name="a393a05b5315245199779ed8738691f16"></a><a name="a393a05b5315245199779ed8738691f16"></a>0 (disabled)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a913464d84b844ceb81256b95056c8e9f"><a name="a913464d84b844ceb81256b95056c8e9f"></a><a name="a913464d84b844ceb81256b95056c8e9f"></a>Thread monitoring threshold. When the update time (seconds) exceeds the threshold, the source is restarted.</p>
    </td>
    </tr>
    <tr id="r4abe313e1bbe4d43890b9b30b849b07a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a61086a25875e423d980b371a8726051c"><a name="a61086a25875e423d980b371a8726051c"></a><a name="a61086a25875e423d980b371a8726051c"></a>spoolDir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="afa43780b758c4be6ba5e0c9daf26c8b7"><a name="afa43780b758c4be6ba5e0c9daf26c8b7"></a><a name="afa43780b758c4be6ba5e0c9daf26c8b7"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8ac3dca2e47f443aa34cfd06c5ca64f5"><a name="a8ac3dca2e47f443aa34cfd06c5ca64f5"></a><a name="a8ac3dca2e47f443aa34cfd06c5ca64f5"></a>Monitoring directory.</p>
    </td>
    </tr>
    <tr id="r2150b5e6fbdf47209d51086bfc61b39c"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ad565c456b3294ed093614ac216ce1cbb"><a name="ad565c456b3294ed093614ac216ce1cbb"></a><a name="ad565c456b3294ed093614ac216ce1cbb"></a>fileSuffix</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a03a41d1e039641ef81679259850c7815"><a name="a03a41d1e039641ef81679259850c7815"></a><a name="a03a41d1e039641ef81679259850c7815"></a>.COMPLETED</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a72a6b5b481cf4108bbf9147983eddf79"><a name="a72a6b5b481cf4108bbf9147983eddf79"></a><a name="a72a6b5b481cf4108bbf9147983eddf79"></a>Suffix added after file transmission is complete.</p>
    </td>
    </tr>
    <tr id="r880f1473baa54aaea03562d9a5e56094"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aba6d3df817634aa3aa75161f65217b12"><a name="aba6d3df817634aa3aa75161f65217b12"></a><a name="aba6d3df817634aa3aa75161f65217b12"></a>deletePolicy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ae864be1d3aea40398bb8a0d05274a15a"><a name="ae864be1d3aea40398bb8a0d05274a15a"></a><a name="ae864be1d3aea40398bb8a0d05274a15a"></a>never</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a76c2d6ee9d264dc5801684f59d5719aa"><a name="a76c2d6ee9d264dc5801684f59d5719aa"></a><a name="a76c2d6ee9d264dc5801684f59d5719aa"></a>Source file deletion policy after file transmission is complete. The value can be either <span class="parmvalue" id="p5875dad05e0f400db3a638a5ad540139"><a name="p5875dad05e0f400db3a638a5ad540139"></a><a name="p5875dad05e0f400db3a638a5ad540139"></a><b>never</b></span>&nbsp;or&nbsp;<span class="parmvalue" id="p107829041f9a4bfaa3dd4f91c34254c4"><a name="p107829041f9a4bfaa3dd4f91c34254c4"></a><a name="p107829041f9a4bfaa3dd4f91c34254c4"></a><b>immediate</b></span>.</p>
    </td>
    </tr>
    <tr id="r90b164bf2ab04a0b8e9ea30d00ab0e13"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a29e363da631746569eef56dfd2c279b5"><a name="a29e363da631746569eef56dfd2c279b5"></a><a name="a29e363da631746569eef56dfd2c279b5"></a>ignorePattern</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a85490444501848ed9e32bff74bb90580"><a name="a85490444501848ed9e32bff74bb90580"></a><a name="a85490444501848ed9e32bff74bb90580"></a>^$</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a89a873381cb345279b07f11bc1091074"><a name="a89a873381cb345279b07f11bc1091074"></a><a name="a89a873381cb345279b07f11bc1091074"></a>Regular expression of a file to be ignored.</p>
    </td>
    </tr>
    <tr id="rce5431fbc0944e23aaf34fa030eb2220"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aea2468653df0420683786c02b5bc1af8"><a name="aea2468653df0420683786c02b5bc1af8"></a><a name="aea2468653df0420683786c02b5bc1af8"></a>trackerDir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a72d71ee1817f46b480c74a9d075c680d"><a name="a72d71ee1817f46b480c74a9d075c680d"></a><a name="a72d71ee1817f46b480c74a9d075c680d"></a>.flumespool</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3535bbec341740cbb64e5702d7dbee5b"><a name="a3535bbec341740cbb64e5702d7dbee5b"></a><a name="a3535bbec341740cbb64e5702d7dbee5b"></a>Metadata storage directory during transmission.</p>
    </td>
    </tr>
    <tr id="r6ef1477c93164e95a9c19c09d7a6e42b"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ae78001810fe34dc08719204620ff92c3"><a name="ae78001810fe34dc08719204620ff92c3"></a><a name="ae78001810fe34dc08719204620ff92c3"></a>batchSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a4dab5250f74c475e875b698824f9dfc7"><a name="a4dab5250f74c475e875b698824f9dfc7"></a><a name="a4dab5250f74c475e875b698824f9dfc7"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a672bf0dd92fd4b9c9753b0702d034027"><a name="a672bf0dd92fd4b9c9753b0702d034027"></a><a name="a672bf0dd92fd4b9c9753b0702d034027"></a>Source transmission granularity.</p>
    </td>
    </tr>
    <tr id="rfacac58840a540eab782ac64c2cbb4bc"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a17d339e09d1048bdabbd53c7c255cfd0"><a name="a17d339e09d1048bdabbd53c7c255cfd0"></a><a name="a17d339e09d1048bdabbd53c7c255cfd0"></a>decodeErrorPolicy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a710f7c5c06cf4c93971fe7b444092e11"><a name="a710f7c5c06cf4c93971fe7b444092e11"></a><a name="a710f7c5c06cf4c93971fe7b444092e11"></a>FAIL</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8e8d239424d6428b9a4cca71e625fb2d"><a name="a8e8d239424d6428b9a4cca71e625fb2d"></a><a name="a8e8d239424d6428b9a4cca71e625fb2d"></a>Code error policy</p>
    <p id="a9fca84d74664464c94cb3b7ec04cf348"><a name="a9fca84d74664464c94cb3b7ec04cf348"></a><a name="a9fca84d74664464c94cb3b7ec04cf348"></a>The options are <strong id="en-us_topic_0066459131_b599452115913"><a name="en-us_topic_0066459131_b599452115913"></a><a name="en-us_topic_0066459131_b599452115913"></a>FAIL</strong>,&nbsp;<strong id="en-us_topic_0066459131_b27581542598"><a name="en-us_topic_0066459131_b27581542598"></a><a name="en-us_topic_0066459131_b27581542598"></a>REPLACE</strong>, and&nbsp;<strong id="a2bc251ddc2084010aa6eab45769dab23"><a name="a2bc251ddc2084010aa6eab45769dab23"></a><a name="a2bc251ddc2084010aa6eab45769dab23"></a>IGNORE</strong>.</p>
    <p id="ac1a1474f3f094f65bc567f11cff71b00"><a name="ac1a1474f3f094f65bc567f11cff71b00"></a><a name="ac1a1474f3f094f65bc567f11cff71b00"></a><strong id="en-us_topic_0066459131_b1111448372"><a name="en-us_topic_0066459131_b1111448372"></a><a name="en-us_topic_0066459131_b1111448372"></a>FAIL</strong>: Throw an exception and make resolution fail.</p>
    <p id="a65fd206e5eab4123b05f7a3da1ca5517"><a name="a65fd206e5eab4123b05f7a3da1ca5517"></a><a name="a65fd206e5eab4123b05f7a3da1ca5517"></a><strong id="en-us_topic_0066459131_b14834611972"><a name="en-us_topic_0066459131_b14834611972"></a><a name="en-us_topic_0066459131_b14834611972"></a>REPLACE</strong>: Replace unidentified characters with other characters (typically, U+FFFD).</p>
    <p id="a95ff3234f1a84d87b2a9ce8214add84e"><a name="a95ff3234f1a84d87b2a9ce8214add84e"></a><a name="a95ff3234f1a84d87b2a9ce8214add84e"></a><strong id="en-us_topic_0066459131_b15697152076"><a name="en-us_topic_0066459131_b15697152076"></a><a name="en-us_topic_0066459131_b15697152076"></a>IGNORE</strong>: Directly discard character strings that fail to be resolved.</p>
    <div class="note" id="n80afb6534c1549449804ccc5a67eebe2"><a name="n80afb6534c1549449804ccc5a67eebe2"></a><a name="n80afb6534c1549449804ccc5a67eebe2"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a3c56bcbf67754a319613f254148b846b"><a name="a3c56bcbf67754a319613f254148b846b"></a><a name="a3c56bcbf67754a319613f254148b846b"></a>If a code error occurs in the file, set <strong id="a6ae64b5ed4a647ca8af630613d3e763c"><a name="a6ae64b5ed4a647ca8af630613d3e763c"></a><a name="a6ae64b5ed4a647ca8af630613d3e763c"></a>decodeErrorPolicy</strong>&nbsp;to&nbsp;<strong id="ab69e4f0ff3aa4c3591de1df5c4ec2261"><a name="ab69e4f0ff3aa4c3591de1df5c4ec2261"></a><a name="ab69e4f0ff3aa4c3591de1df5c4ec2261"></a>REPLACE</strong>&nbsp;or&nbsp;<strong id="ad7b1113983d943b48473225eef94dee4"><a name="ad7b1113983d943b48473225eef94dee4"></a><a name="ad7b1113983d943b48473225eef94dee4"></a>IGNORE</strong>. Flume will skip the code error and continue to collect subsequent logs.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r50d636bf2bf340a8999181c9fc3efff8"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a59b99d6bbcf44b699769ae92091852af"><a name="a59b99d6bbcf44b699769ae92091852af"></a><a name="a59b99d6bbcf44b699769ae92091852af"></a>deserializer</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a515008769e6d49778a1f73f81d035137"><a name="a515008769e6d49778a1f73f81d035137"></a><a name="a515008769e6d49778a1f73f81d035137"></a>LINE</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab2fb8f1aad384b5981e3ccae23de61d9"><a name="ab2fb8f1aad384b5981e3ccae23de61d9"></a><a name="ab2fb8f1aad384b5981e3ccae23de61d9"></a>File parser. The value can be either <span class="parmvalue" id="p2c31a287631d488698f97c939427f256"><a name="p2c31a287631d488698f97c939427f256"></a><a name="p2c31a287631d488698f97c939427f256"></a><b>LINE</b></span>&nbsp;or&nbsp;<span class="parmvalue" id="pd4e07e34db1947528d56aa7875663e3b"><a name="pd4e07e34db1947528d56aa7875663e3b"></a><a name="pd4e07e34db1947528d56aa7875663e3b"></a><b>BufferedLine</b></span>.</p>
    <a name="u93c4964adf5247099dd501b32ae24d6a"></a><a name="u93c4964adf5247099dd501b32ae24d6a"></a><ul id="u93c4964adf5247099dd501b32ae24d6a"><li>When the value is set to <span class="parmname" id="p51be5235d0ed45f489bbbf75a1458f2c"><a name="p51be5235d0ed45f489bbbf75a1458f2c"></a><a name="p51be5235d0ed45f489bbbf75a1458f2c"></a><b>LINE</b></span>, characters read from the file are transcoded one by one.</li><li>When the value is set to <span class="parmvalue" id="p7dcee043f84745d69cb245f540f8d8b6"><a name="p7dcee043f84745d69cb245f540f8d8b6"></a><a name="p7dcee043f84745d69cb245f540f8d8b6"></a><b>BufferedLine</b></span>, one line or multiple lines of characters read from the file are transcoded in batches, which delivers better performance.</li></ul>
    </td>
    </tr>
    <tr id="r82643c602ede4a469375e794ce703cde"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aa928b1d86c234372a93102fddee5abff"><a name="aa928b1d86c234372a93102fddee5abff"></a><a name="aa928b1d86c234372a93102fddee5abff"></a>deserializer.maxLineLength</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ab5602215e604480e883bb8ec9904d92f"><a name="ab5602215e604480e883bb8ec9904d92f"></a><a name="ab5602215e604480e883bb8ec9904d92f"></a>2048</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aba38a273343e47fcbb392d3550fa9743"><a name="aba38a273343e47fcbb392d3550fa9743"></a><a name="aba38a273343e47fcbb392d3550fa9743"></a>Maximum length for resolution by line.</p>
    <p id="en-us_topic_0066459131_p878062184938"><a name="en-us_topic_0066459131_p878062184938"></a><a name="en-us_topic_0066459131_p878062184938"></a>The value ranges from 0 to 2,147,483,647.</p>
    </td>
    </tr>
    <tr id="r15acb6818ab44d54a864ae1e563edce2"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p914884165858"><a name="en-us_topic_0066459131_p914884165858"></a><a name="en-us_topic_0066459131_p914884165858"></a>deserializer.maxBatchLine</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ae84dbd64c1e944b59b5119d519760b10"><a name="ae84dbd64c1e944b59b5119d519760b10"></a><a name="ae84dbd64c1e944b59b5119d519760b10"></a>1</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a54fbf4bc57fb4977a14d7d46ea2f0600"><a name="a54fbf4bc57fb4977a14d7d46ea2f0600"></a><a name="a54fbf4bc57fb4977a14d7d46ea2f0600"></a>Maximum number of lines for resolution by line. If multiple lines are set, <span class="parmvalue" id="p079c604a0ed34fb5bdd482b96741b9ad"><a name="p079c604a0ed34fb5bdd482b96741b9ad"></a><a name="p079c604a0ed34fb5bdd482b96741b9ad"></a><b>maxLineLength</b></span> must be set to a corresponding multiplier.</p>
    <p id="a23331d77926f4df68056f7c7184ecc30"><a name="a23331d77926f4df68056f7c7184ecc30"></a><a name="a23331d77926f4df68056f7c7184ecc30"></a>For example, if <strong id="en-us_topic_0066459131_b954710551281"><a name="en-us_topic_0066459131_b954710551281"></a><a name="en-us_topic_0066459131_b954710551281"></a>maxBatchLine</strong>&nbsp;is set to 2,&nbsp;<span class="parmvalue" id="p4f35d4e5e4534392a1ae320de530ba50"><a name="p4f35d4e5e4534392a1ae320de530ba50"></a><a name="p4f35d4e5e4534392a1ae320de530ba50"></a><b>maxLineLength</b></span> is set to 4096 (2048 x 2) accordingly.</p>
    </td>
    </tr>
    <tr id="r51b4b0d7fcd947a29f6295ba70ae393e"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a83b6f98775ba4589a22f9f7aa47ccb18"><a name="a83b6f98775ba4589a22f9f7aa47ccb18"></a><a name="a83b6f98775ba4589a22f9f7aa47ccb18"></a>selector.type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a04ae096e4878453bb7cb98c396cf1491"><a name="a04ae096e4878453bb7cb98c396cf1491"></a><a name="a04ae096e4878453bb7cb98c396cf1491"></a>replicating</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8f8cf29fdb4c424490fecb5a8cc133d9"><a name="a8f8cf29fdb4c424490fecb5a8cc133d9"></a><a name="a8f8cf29fdb4c424490fecb5a8cc133d9"></a>Selector type. The value can be either <span class="parmvalue" id="p5db432fa45e14e3cbc996a8859291f52"><a name="p5db432fa45e14e3cbc996a8859291f52"></a><a name="p5db432fa45e14e3cbc996a8859291f52"></a><b>replicating</b></span>&nbsp;or&nbsp;<span class="parmvalue" id="p3c6d4115f04f4da9bc989b1a51ae7d9d"><a name="p3c6d4115f04f4da9bc989b1a51ae7d9d"></a><a name="p3c6d4115f04f4da9bc989b1a51ae7d9d"></a><b>multiplexing</b></span>.</p>
    <a name="u1f0dc03b879b4e6db7ee3eb59e0556a2"></a><a name="u1f0dc03b879b4e6db7ee3eb59e0556a2"></a><ul id="u1f0dc03b879b4e6db7ee3eb59e0556a2"><li><span class="parmvalue" id="pd4af0aa01be94cfa926dc3e8b11f8e7a"><a name="pd4af0aa01be94cfa926dc3e8b11f8e7a"></a><a name="pd4af0aa01be94cfa926dc3e8b11f8e7a"></a><b>replicating</b></span> indicates that the same content is sent to every channel.</li><li><span class="parmvalue" id="pf9317a475cbe4049b7ce393a9693a9a7"><a name="pf9317a475cbe4049b7ce393a9693a9a7"></a><a name="pf9317a475cbe4049b7ce393a9693a9a7"></a><b>multiplexing</b></span> indicates that content is selectively sent to some channels according to the replicating distribution rule.</li></ul>
    </td>
    </tr>
    <tr id="r5b63934ba2144fe382d0685273ae7a5f"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a4d37b498c3794f2facfee032d6daf573"><a name="a4d37b498c3794f2facfee032d6daf573"></a><a name="a4d37b498c3794f2facfee032d6daf573"></a>interceptors</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a41b52cd6f90247f6968e54b1b1cde370"><a name="a41b52cd6f90247f6968e54b1b1cde370"></a><a name="a41b52cd6f90247f6968e54b1b1cde370"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3db514f500fe4051941f5660fc96d4f8"><a name="a3db514f500fe4051941f5660fc96d4f8"></a><a name="a3db514f500fe4051941f5660fc96d4f8"></a>Interceptor</p>
    <p id="a320de985f77448ccab0b7b8c9c1cf9cc"><a name="a320de985f77448ccab0b7b8c9c1cf9cc"></a><a name="a320de985f77448ccab0b7b8c9c1cf9cc"></a>For details about configuration, see <a href="https://flume.apache.org/FlumeUserGuide.html#flume-interceptors" target="_blank" rel="noopener noreferrer">Flume User Guide</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The Spooling source ignores the last line feed character of each event when data is read by line. Therefore, Flume does not calculate the data volume counters used by the last line feed character.  

-   **Kafka Source**

    A Kafka source consumes data from Kafka topics. Multiple sources can consume data of the same topic, and the sources consume different partitions of the topic. Common configurations are as follows.

    **Table  3**  Common configurations of a Kafka source

    <a name="t557491865132467e986489452fe5e2e1"></a>
    <table><thead align="left"><tr id="r9ee23a39f3a3480ca2c49c079fb21199"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="a63044e98361a4141b3ea8bb645bf6d57"><a name="a63044e98361a4141b3ea8bb645bf6d57"></a><a name="a63044e98361a4141b3ea8bb645bf6d57"></a><strong id="ac70bcf983ae54328b8fe419bcf3608b6"><a name="ac70bcf983ae54328b8fe419bcf3608b6"></a><a name="ac70bcf983ae54328b8fe419bcf3608b6"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="ab7fab71fd9a048a78c1a8bacb56c6a9e"><a name="ab7fab71fd9a048a78c1a8bacb56c6a9e"></a><a name="ab7fab71fd9a048a78c1a8bacb56c6a9e"></a><strong id="ae4e26011e1304ae1a9a73d3e1fac2431"><a name="ae4e26011e1304ae1a9a73d3e1fac2431"></a><a name="ae4e26011e1304ae1a9a73d3e1fac2431"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="af96637ebb62d440f91076829d4441b92"><a name="af96637ebb62d440f91076829d4441b92"></a><a name="af96637ebb62d440f91076829d4441b92"></a><strong id="a089ea61b265849159a9ec440663b3d6d"><a name="a089ea61b265849159a9ec440663b3d6d"></a><a name="a089ea61b265849159a9ec440663b3d6d"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r6de4a88bad37442bb751aecb1013cd3f"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a3d40fdbf12254b2d8f2082a8ba14b95d"><a name="a3d40fdbf12254b2d8f2082a8ba14b95d"></a><a name="a3d40fdbf12254b2d8f2082a8ba14b95d"></a>channels</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a4cac3dd396234897ab696f09f2d4a6c9"><a name="a4cac3dd396234897ab696f09f2d4a6c9"></a><a name="a4cac3dd396234897ab696f09f2d4a6c9"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac92107fdab1b44f68ece68afff3e1057"><a name="ac92107fdab1b44f68ece68afff3e1057"></a><a name="ac92107fdab1b44f68ece68afff3e1057"></a>Channel connected to the source. Multiple channels can be configured.</p>
    </td>
    </tr>
    <tr id="r76c7dac8a6044a57997c350d53d430df"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ae454306d067647a89b9051cae5202cb2"><a name="ae454306d067647a89b9051cae5202cb2"></a><a name="ae454306d067647a89b9051cae5202cb2"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ac75b4957bb574eebbd5f26122f7066e1"><a name="ac75b4957bb574eebbd5f26122f7066e1"></a><a name="ac75b4957bb574eebbd5f26122f7066e1"></a>org.apache.flume.source.kafka.KafkaSource</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2bff088578794ce0a2fc09e56056c1b5"><a name="a2bff088578794ce0a2fc09e56056c1b5"></a><a name="a2bff088578794ce0a2fc09e56056c1b5"></a>Type, which is set to <span class="parmvalue" id="p68903bd5c17f4372b9af7668085fa9d2"><a name="p68903bd5c17f4372b9af7668085fa9d2"></a><a name="p68903bd5c17f4372b9af7668085fa9d2"></a><b>org.apache.flume.source.kafka.KafkaSource</b></span>.</p>
    </td>
    </tr>
    <tr id="r711359b699e74aaa9cfe9392ba51deb9"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a63f4b660916146cd891921404b8e4b00"><a name="a63f4b660916146cd891921404b8e4b00"></a><a name="a63f4b660916146cd891921404b8e4b00"></a>monTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p10022165858"><a name="en-us_topic_0066459131_p10022165858"></a><a name="en-us_topic_0066459131_p10022165858"></a>0 (disabled)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p811818165858"><a name="en-us_topic_0066459131_p811818165858"></a><a name="en-us_topic_0066459131_p811818165858"></a>Thread monitoring threshold. When the update time (seconds) exceeds the threshold, the source is restarted.</p>
    </td>
    </tr>
    <tr id="r86162231859d41cb9bd279646ed3e56a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="afb11333caa1f4469afaf9d175678dcb9"><a name="afb11333caa1f4469afaf9d175678dcb9"></a><a name="afb11333caa1f4469afaf9d175678dcb9"></a>nodatatime</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a31bc6eab7ea34cc9aa49e236538dae3a"><a name="a31bc6eab7ea34cc9aa49e236538dae3a"></a><a name="a31bc6eab7ea34cc9aa49e236538dae3a"></a>0 (disabled)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a7d51faa7c8bb425f8791bba1745a1556"><a name="a7d51faa7c8bb425f8791bba1745a1556"></a><a name="a7d51faa7c8bb425f8791bba1745a1556"></a>Alarm threshold. An alarm is triggered when the duration (seconds) that Kafka does not release data to subscribers exceeds the threshold.</p>
    </td>
    </tr>
    <tr id="rcaf9a1e0b38b48d6b45de6a42f0c52bf"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aaa535845c19d4c77b9ebeff0cfc04354"><a name="aaa535845c19d4c77b9ebeff0cfc04354"></a><a name="aaa535845c19d4c77b9ebeff0cfc04354"></a>batchSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a7398f7a3a50743c8bad3409154f60344"><a name="a7398f7a3a50743c8bad3409154f60344"></a><a name="a7398f7a3a50743c8bad3409154f60344"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a85278b764f174f2ab22e59142d6adab4"><a name="a85278b764f174f2ab22e59142d6adab4"></a><a name="a85278b764f174f2ab22e59142d6adab4"></a>Number of events written into a channel at a time.</p>
    </td>
    </tr>
    <tr id="r18fe9a643ca441d9a80a352010549beb"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a72b97323c0ab40feb7cba0607c5e5734"><a name="a72b97323c0ab40feb7cba0607c5e5734"></a><a name="a72b97323c0ab40feb7cba0607c5e5734"></a>batchDurationMillis</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ab09333daab6a4177925fe64c95fa2cf0"><a name="ab09333daab6a4177925fe64c95fa2cf0"></a><a name="ab09333daab6a4177925fe64c95fa2cf0"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2e7fc933dc8a481a931b66fd9cca6b11"><a name="a2e7fc933dc8a481a931b66fd9cca6b11"></a><a name="a2e7fc933dc8a481a931b66fd9cca6b11"></a>Maximum duration of topic data consumption at a time. The unit is millisecond.</p>
    </td>
    </tr>
    <tr id="r69f75bdd5e2f4f159aa9cfecee2f36b9"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="adcb5b7cce81740c08ec562d4496ef3e1"><a name="adcb5b7cce81740c08ec562d4496ef3e1"></a><a name="adcb5b7cce81740c08ec562d4496ef3e1"></a>keepTopicInHeader</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a4d8f80b5f76a464aa0308486871b3530"><a name="a4d8f80b5f76a464aa0308486871b3530"></a><a name="a4d8f80b5f76a464aa0308486871b3530"></a>false</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad2ed80bc063f437c874097c36a76faa1"><a name="ad2ed80bc063f437c874097c36a76faa1"></a><a name="ad2ed80bc063f437c874097c36a76faa1"></a>Indicates whether to save topics in the event header. If topics are saved, topics configured in Kafka sinks become invalid.</p>
    <a name="ue4cc5e18acbe437b8b47b6267587c0f0"></a><a name="ue4cc5e18acbe437b8b47b6267587c0f0"></a><ul id="ue4cc5e18acbe437b8b47b6267587c0f0"><li>true</li><li>false</li></ul>
    </td>
    </tr>
    <tr id="r528efdd4ea21440784b3bc5bd6348aa9"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a75f87119abf14359a10ca0fa0c94b8e0"><a name="a75f87119abf14359a10ca0fa0c94b8e0"></a><a name="a75f87119abf14359a10ca0fa0c94b8e0"></a>keepPartitionInHeader</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aa0c0ff38c5c048ea81f09b43231b84d8"><a name="aa0c0ff38c5c048ea81f09b43231b84d8"></a><a name="aa0c0ff38c5c048ea81f09b43231b84d8"></a>false</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="acabb595fd9ed471daa33ad087466bd19"><a name="acabb595fd9ed471daa33ad087466bd19"></a><a name="acabb595fd9ed471daa33ad087466bd19"></a>Indicates whether to save partition IDs in the event header. If partition IDs are saved, Kafka sinks write data to the corresponding partitions.</p>
    <a name="uef838947872348599cc145788b959e45"></a><a name="uef838947872348599cc145788b959e45"></a><ul id="uef838947872348599cc145788b959e45"><li>true</li><li>false</li></ul>
    </td>
    </tr>
    <tr id="r62d0dc2bde4441859c8638bdde18c7ac"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a71eda3d4d127428380e5d1e38fd55e4b"><a name="a71eda3d4d127428380e5d1e38fd55e4b"></a><a name="a71eda3d4d127428380e5d1e38fd55e4b"></a>kafka.bootstrap.servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ab8835805d255414b9b1a6739f2543590"><a name="ab8835805d255414b9b1a6739f2543590"></a><a name="ab8835805d255414b9b1a6739f2543590"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a0ae5f1103563403eb0ca587edb42d1b4"><a name="a0ae5f1103563403eb0ca587edb42d1b4"></a><a name="a0ae5f1103563403eb0ca587edb42d1b4"></a>List of Broker addresses, which are separated by commas.</p>
    </td>
    </tr>
    <tr id="r39ca6949d6b44cd58663d336bd393c54"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a1f84a39f443f457aad80d053adf3ef5a"><a name="a1f84a39f443f457aad80d053adf3ef5a"></a><a name="a1f84a39f443f457aad80d053adf3ef5a"></a>kafka.consumer.group.id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a13c1cdd3658840468be191bd9bf1d891"><a name="a13c1cdd3658840468be191bd9bf1d891"></a><a name="a13c1cdd3658840468be191bd9bf1d891"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aae7e3581608248c18518914e0861dddd"><a name="aae7e3581608248c18518914e0861dddd"></a><a name="aae7e3581608248c18518914e0861dddd"></a>Kafka consumer group ID.</p>
    </td>
    </tr>
    <tr id="r42cf5ff2baa94176989fe8de4592a335"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ae78e00271f2347a98632d92f7ae1a08e"><a name="ae78e00271f2347a98632d92f7ae1a08e"></a><a name="ae78e00271f2347a98632d92f7ae1a08e"></a>kafka.topics</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a89eef9ad06c94310ab73f04c4d579444"><a name="a89eef9ad06c94310ab73f04c4d579444"></a><a name="a89eef9ad06c94310ab73f04c4d579444"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a1a41700dbbcb4b2aa28425f5577bf355"><a name="a1a41700dbbcb4b2aa28425f5577bf355"></a><a name="a1a41700dbbcb4b2aa28425f5577bf355"></a>List of subscribed Kafka topics, which are separated by commas.</p>
    </td>
    </tr>
    <tr id="r4defd28df3d74b0d85be8494298e03a8"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a4f540e7ddb2a4f23b8834c87a9f089b8"><a name="a4f540e7ddb2a4f23b8834c87a9f089b8"></a><a name="a4f540e7ddb2a4f23b8834c87a9f089b8"></a>kafka.topics.regex</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1e76d4d66da14044bfd689e59ec1a2bf"><a name="a1e76d4d66da14044bfd689e59ec1a2bf"></a><a name="a1e76d4d66da14044bfd689e59ec1a2bf"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a6a71fdc21bca456e8cc200376d249a4c"><a name="a6a71fdc21bca456e8cc200376d249a4c"></a><a name="a6a71fdc21bca456e8cc200376d249a4c"></a>Subscribed topics that comply with regular expressions. <strong id="a4d9ce8203dc94fb0bfbb9e91c49344b2"><a name="a4d9ce8203dc94fb0bfbb9e91c49344b2"></a><a name="a4d9ce8203dc94fb0bfbb9e91c49344b2"></a>kafka.topics.regex</strong>&nbsp;has a higher priority than&nbsp;<strong id="a341e27d2470d4854b61ddac05344bbab"><a name="a341e27d2470d4854b61ddac05344bbab"></a><a name="a341e27d2470d4854b61ddac05344bbab"></a>kafka.topics</strong>&nbsp;and will overwrite&nbsp;<strong id="aebdbbc6d94d64639b99664352d765da8"><a name="aebdbbc6d94d64639b99664352d765da8"></a><a name="aebdbbc6d94d64639b99664352d765da8"></a>kafka.topics</strong>.</p>
    </td>
    </tr>
    <tr id="r7253dee081cc46bea4d00a8b8a592201"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="adacbdd192b204c31ab8cd5ccc79781a1"><a name="adacbdd192b204c31ab8cd5ccc79781a1"></a><a name="adacbdd192b204c31ab8cd5ccc79781a1"></a>kafka.security.protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a6fc4e4fe34b0415dbef1740b4624f90a"><a name="a6fc4e4fe34b0415dbef1740b4624f90a"></a><a name="a6fc4e4fe34b0415dbef1740b4624f90a"></a>SASL_PLAINTEXT</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a0b783c8507fc40fea942ee32b44c2787"><a name="a0b783c8507fc40fea942ee32b44c2787"></a><a name="a0b783c8507fc40fea942ee32b44c2787"></a>Security protocol of Kafka. The value must be set to <span class="parmvalue" id="p02a2ab911e8841b68d6d2626fd862aba"><a name="p02a2ab911e8841b68d6d2626fd862aba"></a><a name="p02a2ab911e8841b68d6d2626fd862aba"></a><b>PLAINTEXT</b></span> for clusters in which Kerberos authentication is disabled.</p>
    </td>
    </tr>
    <tr id="r6d7ea3c99a154209b494543f01656251"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a764f252e7636423c84b1452ac827a702"><a name="a764f252e7636423c84b1452ac827a702"></a><a name="a764f252e7636423c84b1452ac827a702"></a>Other Kafka Consumer Properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="abd77304a39434879ac03512ef28c975b"><a name="abd77304a39434879ac03512ef28c975b"></a><a name="abd77304a39434879ac03512ef28c975b"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a45c24b3e054a4000855dd4a9b115c33b"><a name="a45c24b3e054a4000855dd4a9b115c33b"></a><a name="a45c24b3e054a4000855dd4a9b115c33b"></a>Other Kafka configurations. This parameter can be set to any consumption configuration supported by Kafka, and the <span class="parmvalue" id="pe77e5d176eb449b9aa53235ed54077fa"><a name="pe77e5d176eb449b9aa53235ed54077fa"></a><a name="pe77e5d176eb449b9aa53235ed54077fa"></a><b>.kafka</b></span> prefix must be added to the configuration.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Taildir Source**

    A Taildir source monitors file changes in a directory and automatically reads the file content. In addition, it can transmit data in real time. Common configurations are as follows.

    **Table  4**  Common configurations of a Taildir source

    <a name="t67f7c8d08a2b4683bc7d1215178d6ef8"></a>
    <table><thead align="left"><tr id="r34a2a770b485477dad5c9bab817b389c"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="a681bfc65ba6b4079b57cda6bde073ff2"><a name="a681bfc65ba6b4079b57cda6bde073ff2"></a><a name="a681bfc65ba6b4079b57cda6bde073ff2"></a><strong id="ad825348cefae4a2f9d082f071d8dcb96"><a name="ad825348cefae4a2f9d082f071d8dcb96"></a><a name="ad825348cefae4a2f9d082f071d8dcb96"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="ae4fee49c397843d6b03f98b2119ad165"><a name="ae4fee49c397843d6b03f98b2119ad165"></a><a name="ae4fee49c397843d6b03f98b2119ad165"></a><strong id="a88e37abb938b4b508ef2c21cb0abb727"><a name="a88e37abb938b4b508ef2c21cb0abb727"></a><a name="a88e37abb938b4b508ef2c21cb0abb727"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a30bf9e6b24c548e0a03c028ab405b17b"><a name="a30bf9e6b24c548e0a03c028ab405b17b"></a><a name="a30bf9e6b24c548e0a03c028ab405b17b"></a><strong id="ab98431a983dc4c7db20652940c423110"><a name="ab98431a983dc4c7db20652940c423110"></a><a name="ab98431a983dc4c7db20652940c423110"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r918fd1d25ca34b20918438f1d637718a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ac95a0e1f3a064d38a1e7824e7a4e1ce8"><a name="ac95a0e1f3a064d38a1e7824e7a4e1ce8"></a><a name="ac95a0e1f3a064d38a1e7824e7a4e1ce8"></a><span id="p6985841be6fc4a8ba7c5a019cacaf5cf"><a name="p6985841be6fc4a8ba7c5a019cacaf5cf"></a><a name="p6985841be6fc4a8ba7c5a019cacaf5cf"></a>channels</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a07896edb240649fe9163c5811e739f6a"><a name="a07896edb240649fe9163c5811e739f6a"></a><a name="a07896edb240649fe9163c5811e739f6a"></a><span id="pcebdd2905f484778a5cfc2e83f521018"><a name="pcebdd2905f484778a5cfc2e83f521018"></a><a name="pcebdd2905f484778a5cfc2e83f521018"></a>-</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="af0771df35f4644af85459226c8e09295"><a name="af0771df35f4644af85459226c8e09295"></a><a name="af0771df35f4644af85459226c8e09295"></a>Channel connected to the source. Multiple channels can be configured.</p>
    </td>
    </tr>
    <tr id="r26028dd05b2c4f35a34c0ad5ee476d60"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aaf199c24f41d47058289923dcc77af1d"><a name="aaf199c24f41d47058289923dcc77af1d"></a><a name="aaf199c24f41d47058289923dcc77af1d"></a><span id="p4240130af18846c9847c6a15bae8d18c"><a name="p4240130af18846c9847c6a15bae8d18c"></a><a name="p4240130af18846c9847c6a15bae8d18c"></a>type</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ab0539bc97919452fa246ef67c654fb72"><a name="ab0539bc97919452fa246ef67c654fb72"></a><a name="ab0539bc97919452fa246ef67c654fb72"></a>taildir</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a69cdfaf182df4016b933b27f7ecab017"><a name="a69cdfaf182df4016b933b27f7ecab017"></a><a name="a69cdfaf182df4016b933b27f7ecab017"></a>Type, which is set to <span class="parmvalue" id="pac988df2a6e74299b8db64f8d064b77e"><a name="pac988df2a6e74299b8db64f8d064b77e"></a><a name="pac988df2a6e74299b8db64f8d064b77e"></a><b>taildir</b></span>.</p>
    </td>
    </tr>
    <tr id="rac1d3efed6cf4b6798f414ef28bec630"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aa2c62d74fa324e87bb7be33f26f22415"><a name="aa2c62d74fa324e87bb7be33f26f22415"></a><a name="aa2c62d74fa324e87bb7be33f26f22415"></a>filegroups</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1baea3783e6c4c0f8629c60ac2308d91"><a name="a1baea3783e6c4c0f8629c60ac2308d91"></a><a name="a1baea3783e6c4c0f8629c60ac2308d91"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="acbd24971df804c66b12525b1d108cb15"><a name="acbd24971df804c66b12525b1d108cb15"></a><a name="acbd24971df804c66b12525b1d108cb15"></a>Group name of a collection file directory. Group names are separated by spaces.</p>
    </td>
    </tr>
    <tr id="r1d99c4d90b134b8d80139f5c144c8d29"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="afcfd64c47ca24329b5d48c896bb524a7"><a name="afcfd64c47ca24329b5d48c896bb524a7"></a><a name="afcfd64c47ca24329b5d48c896bb524a7"></a>filegroups.&lt;filegroupName&gt;.parentDir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ae4f60b2191384307859971ac7376b1f7"><a name="ae4f60b2191384307859971ac7376b1f7"></a><a name="ae4f60b2191384307859971ac7376b1f7"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a766d6a4474e74ee393324dac17a70523"><a name="a766d6a4474e74ee393324dac17a70523"></a><a name="a766d6a4474e74ee393324dac17a70523"></a>Parent directory. The value must be an absolute path.</p>
    </td>
    </tr>
    <tr id="r91c7a0c8aeed4b858d3ac70ef5265b05"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a16813e553732499bbd5e24fc53a4e2ea"><a name="a16813e553732499bbd5e24fc53a4e2ea"></a><a name="a16813e553732499bbd5e24fc53a4e2ea"></a>filegroups.&lt;filegroupName&gt;.filePattern</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="abf5ef013341b4250866a2eae70b18a64"><a name="abf5ef013341b4250866a2eae70b18a64"></a><a name="abf5ef013341b4250866a2eae70b18a64"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a54f0316fdecd48b9add947215aeec8f1"><a name="a54f0316fdecd48b9add947215aeec8f1"></a><a name="a54f0316fdecd48b9add947215aeec8f1"></a>Relative file path of the file group's parent directory. Directories can be included and regular expressions are supported. It must be used together with <strong id="acdfd25968d82412dac90c4c4022241b9"><a name="acdfd25968d82412dac90c4c4022241b9"></a><a name="acdfd25968d82412dac90c4c4022241b9"></a>parentDir</strong>.</p>
    </td>
    </tr>
    <tr id="re552021eacb14debbc7d303aa6768e74"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p440251165858"><a name="en-us_topic_0066459131_p440251165858"></a><a name="en-us_topic_0066459131_p440251165858"></a>positionFile</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="af6a1e716ffe74f6e89b0373894c21ea2"><a name="af6a1e716ffe74f6e89b0373894c21ea2"></a><a name="af6a1e716ffe74f6e89b0373894c21ea2"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ae558ef37db764aecbbdfe5ddb0a3b6ad"><a name="ae558ef37db764aecbbdfe5ddb0a3b6ad"></a><a name="ae558ef37db764aecbbdfe5ddb0a3b6ad"></a>Metadata storage directory during transmission.</p>
    </td>
    </tr>
    <tr id="rb32801861c1e4e4f95531688fafa33ae"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a1367c44de6254f4d9e850356fae33dc6"><a name="a1367c44de6254f4d9e850356fae33dc6"></a><a name="a1367c44de6254f4d9e850356fae33dc6"></a>headers.&lt;filegroupName&gt;.&lt;headerKey&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ae9c1674102ae4a8f844372e3a6a55ea5"><a name="ae9c1674102ae4a8f844372e3a6a55ea5"></a><a name="ae9c1674102ae4a8f844372e3a6a55ea5"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="afd633faad93b45c19e257ef2023b26df"><a name="afd633faad93b45c19e257ef2023b26df"></a><a name="afd633faad93b45c19e257ef2023b26df"></a>Key-value of an event when data of a group is being collected.</p>
    </td>
    </tr>
    <tr id="r44c2323a7046403bab6cc782929e24f4"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ac0ecfe20041c4289822c8f4ec0b8d2bd"><a name="ac0ecfe20041c4289822c8f4ec0b8d2bd"></a><a name="ac0ecfe20041c4289822c8f4ec0b8d2bd"></a>byteOffsetHeader</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ae3f96ee17ec44809945375b5dc501154"><a name="ae3f96ee17ec44809945375b5dc501154"></a><a name="ae3f96ee17ec44809945375b5dc501154"></a>false</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8642a4514fd64ba1be30108236430c99"><a name="a8642a4514fd64ba1be30108236430c99"></a><a name="a8642a4514fd64ba1be30108236430c99"></a>Indicates whether each event header should contain the location information about the event in the source file. The location information is saved in the <span class="parmname" id="p208f0929559e44479ad20f4db541beaa"><a name="p208f0929559e44479ad20f4db541beaa"></a><a name="p208f0929559e44479ad20f4db541beaa"></a><b>byteoffset</b></span> variable.</p>
    </td>
    </tr>
    <tr id="rfb226c5242c441598684a8f6ba8a365a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ab96f7c043e5b49d99ebbd37406e7bae0"><a name="ab96f7c043e5b49d99ebbd37406e7bae0"></a><a name="ab96f7c043e5b49d99ebbd37406e7bae0"></a>skipToEnd</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a76c642f257a549a9a48dbe6b88c97ebd"><a name="a76c642f257a549a9a48dbe6b88c97ebd"></a><a name="a76c642f257a549a9a48dbe6b88c97ebd"></a>false</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8771121dd47041bb8ef553de86900cff"><a name="a8771121dd47041bb8ef553de86900cff"></a><a name="a8771121dd47041bb8ef553de86900cff"></a>Indicates whether Flume can locate the latest location of a file and read the latest data after restart.</p>
    </td>
    </tr>
    <tr id="rf2d54d38e46c47f5baf3a28a8ed9143c"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a514c47846cc441cbac5ab4f9daad174a"><a name="a514c47846cc441cbac5ab4f9daad174a"></a><a name="a514c47846cc441cbac5ab4f9daad174a"></a>idleTimeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a4854905815eb4a448d128a8e33ee7ee7"><a name="a4854905815eb4a448d128a8e33ee7ee7"></a><a name="a4854905815eb4a448d128a8e33ee7ee7"></a>120000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aef692c0e075946f1b7ffed3c731a9ef0"><a name="aef692c0e075946f1b7ffed3c731a9ef0"></a><a name="aef692c0e075946f1b7ffed3c731a9ef0"></a>Idle period during file reading, expressed in milliseconds. If the file data is not changed in this idle period, the source closes the file. If data is written into this file after it is closed, the source opens the file and reads data.</p>
    </td>
    </tr>
    <tr id="rf33393b52a3a40bcaf02df0b94b71dbc"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a2e1854a4afb947c89e52dcbd89c1bac1"><a name="a2e1854a4afb947c89e52dcbd89c1bac1"></a><a name="a2e1854a4afb947c89e52dcbd89c1bac1"></a>writePosInterval</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a96d9d0fcd71946aba34250ece1040637"><a name="a96d9d0fcd71946aba34250ece1040637"></a><a name="a96d9d0fcd71946aba34250ece1040637"></a>3000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac5a2c528546948bc97f894b507d50f2f"><a name="ac5a2c528546948bc97f894b507d50f2f"></a><a name="ac5a2c528546948bc97f894b507d50f2f"></a>Interval for writing metadata to a file, expressed in milliseconds.</p>
    </td>
    </tr>
    <tr id="r02a2373071984c17aaf8fe369d81ac0a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a1d257dda914d460c8ff7b90761706230"><a name="a1d257dda914d460c8ff7b90761706230"></a><a name="a1d257dda914d460c8ff7b90761706230"></a>batchSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1d368a45701c42d0a2b68ac78d6f5069"><a name="a1d368a45701c42d0a2b68ac78d6f5069"></a><a name="a1d368a45701c42d0a2b68ac78d6f5069"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a704026e2b06b42239026529bd9ffa1cf"><a name="a704026e2b06b42239026529bd9ffa1cf"></a><a name="a704026e2b06b42239026529bd9ffa1cf"></a>Number of events written into a channel in a batch.</p>
    </td>
    </tr>
    <tr id="rb5f6f862940c4d1f9a9593db8128d28d"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a57f0e79c6b3941cdb4f14b5964603671"><a name="a57f0e79c6b3941cdb4f14b5964603671"></a><a name="a57f0e79c6b3941cdb4f14b5964603671"></a><span id="p36383c17cb8e4810ad6c2d885c61c062"><a name="p36383c17cb8e4810ad6c2d885c61c062"></a><a name="p36383c17cb8e4810ad6c2d885c61c062"></a>monTime</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a2a2666dd946b446993fcbaa1a57a9282"><a name="a2a2666dd946b446993fcbaa1a57a9282"></a><a name="a2a2666dd946b446993fcbaa1a57a9282"></a>0 (disabled)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad71164cdda1742c7b213c597cdada2da"><a name="ad71164cdda1742c7b213c597cdada2da"></a><a name="ad71164cdda1742c7b213c597cdada2da"></a>Thread monitoring threshold. When the update time (seconds) exceeds the threshold, the source is restarted.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **HTTP Source**

    An HTTP source receives data from an external HTTP client and sends the data to the configured channels. Common configurations are as follows.

    **Table  5**  Common configurations of an HTTP source

    <a name="t255a6a724b83454ba9eb6d1704ea91eb"></a>
    <table><thead align="left"><tr id="refd6a740b90a493da5d272318affb19d"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="abe1cc0cf393847beb8e2d051ae8f69bb"><a name="abe1cc0cf393847beb8e2d051ae8f69bb"></a><a name="abe1cc0cf393847beb8e2d051ae8f69bb"></a><strong id="af043d67ca8434dea816287a0617f79a0"><a name="af043d67ca8434dea816287a0617f79a0"></a><a name="af043d67ca8434dea816287a0617f79a0"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="a23c9949317554d419d73209af5ad6d87"><a name="a23c9949317554d419d73209af5ad6d87"></a><a name="a23c9949317554d419d73209af5ad6d87"></a><strong id="a3aa976bc247a48039ecf93ad8bb0df00"><a name="a3aa976bc247a48039ecf93ad8bb0df00"></a><a name="a3aa976bc247a48039ecf93ad8bb0df00"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a39c2214884e34bc3b09c4dca7aefbcdf"><a name="a39c2214884e34bc3b09c4dca7aefbcdf"></a><a name="a39c2214884e34bc3b09c4dca7aefbcdf"></a><strong id="ae35670d158f84cfabde18ee74ba19bfa"><a name="ae35670d158f84cfabde18ee74ba19bfa"></a><a name="ae35670d158f84cfabde18ee74ba19bfa"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r70082bbdef8541e4b088ff441b028a97"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a172c114936ae410d9394025cd05444f4"><a name="a172c114936ae410d9394025cd05444f4"></a><a name="a172c114936ae410d9394025cd05444f4"></a>channels</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1fa00d7c10b9447185674a072b5cb747"><a name="a1fa00d7c10b9447185674a072b5cb747"></a><a name="a1fa00d7c10b9447185674a072b5cb747"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a033418f2398c49599e6c3257582fbd22"><a name="a033418f2398c49599e6c3257582fbd22"></a><a name="a033418f2398c49599e6c3257582fbd22"></a>Channel connected to the source. Multiple channels can be configured.</p>
    </td>
    </tr>
    <tr id="rf3a254dd3229423ea6bf8bdd5f96c750"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a4313e824a0e84bd494e29e06b9c5746c"><a name="a4313e824a0e84bd494e29e06b9c5746c"></a><a name="a4313e824a0e84bd494e29e06b9c5746c"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a08178df88e384603ad10b4fa7d17a664"><a name="a08178df88e384603ad10b4fa7d17a664"></a><a name="a08178df88e384603ad10b4fa7d17a664"></a>http</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ae561d9c07f654279ad732c2f329b8574"><a name="ae561d9c07f654279ad732c2f329b8574"></a><a name="ae561d9c07f654279ad732c2f329b8574"></a>Type, which is set to <span class="parmvalue" id="p26d4b5d18d08442896bf4781f55a9e46"><a name="p26d4b5d18d08442896bf4781f55a9e46"></a><a name="p26d4b5d18d08442896bf4781f55a9e46"></a><b>http</b></span>.</p>
    </td>
    </tr>
    <tr id="r3fa7c2f70af84d7f9f0d62d8a8b76cc4"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a3832a84445cf4c88874f84a941b67274"><a name="a3832a84445cf4c88874f84a941b67274"></a><a name="a3832a84445cf4c88874f84a941b67274"></a>bind</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a22c935d6cdc84ceabf69778080381618"><a name="a22c935d6cdc84ceabf69778080381618"></a><a name="a22c935d6cdc84ceabf69778080381618"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a1fb938f1eee84956ba52331735542e04"><a name="a1fb938f1eee84956ba52331735542e04"></a><a name="a1fb938f1eee84956ba52331735542e04"></a>Name or IP address of the bound host</p>
    </td>
    </tr>
    <tr id="r1269379bf5444342a9ea45f65e2a6fb2"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a11dfd72893a541759f93504e6035555b"><a name="a11dfd72893a541759f93504e6035555b"></a><a name="a11dfd72893a541759f93504e6035555b"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a9c27322161ee4a7680abfcdbf72d3969"><a name="a9c27322161ee4a7680abfcdbf72d3969"></a><a name="a9c27322161ee4a7680abfcdbf72d3969"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a020034e0fb5b44d288a54f87fce1c058"><a name="a020034e0fb5b44d288a54f87fce1c058"></a><a name="a020034e0fb5b44d288a54f87fce1c058"></a>Bound port</p>
    </td>
    </tr>
    <tr id="rdd5f23b8c9474d0eb1c291b041ed20ea"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a8a40abc52c47421cafb587b424d2ecd5"><a name="a8a40abc52c47421cafb587b424d2ecd5"></a><a name="a8a40abc52c47421cafb587b424d2ecd5"></a>handler</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a6b57a274b9bd488f90606cd85b5de52d"><a name="a6b57a274b9bd488f90606cd85b5de52d"></a><a name="a6b57a274b9bd488f90606cd85b5de52d"></a>org.apache.flume.source.http.JSONHandler</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad811222c8ce0425c87da39d40f967616"><a name="ad811222c8ce0425c87da39d40f967616"></a><a name="ad811222c8ce0425c87da39d40f967616"></a>Message parsing method of an HTTP request. The following methods are supported:</p>
    <a name="u2092e28a08cc478f9560246a674390e1"></a><a name="u2092e28a08cc478f9560246a674390e1"></a><ul id="u2092e28a08cc478f9560246a674390e1"><li><span class="parmvalue" id="p2417c2ce5a5d472cbceecce2c2f7b4b1"><a name="p2417c2ce5a5d472cbceecce2c2f7b4b1"></a><a name="p2417c2ce5a5d472cbceecce2c2f7b4b1"></a><b>org.apache.flume.source.http.JSONHandler</b></span>: JSON</li><li><span class="parmvalue" id="p4a96fcb3f8474df5a56d03bac6c496f1"><a name="p4a96fcb3f8474df5a56d03bac6c496f1"></a><a name="p4a96fcb3f8474df5a56d03bac6c496f1"></a><b>org.apache.flume.sink.solr.morphline.BlobHandler</b></span>: BLOB</li></ul>
    </td>
    </tr>
    <tr id="r81999e391793498e9eeb958e61004dd1"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aa6c29f654ac148548d0dfbefdad161df"><a name="aa6c29f654ac148548d0dfbefdad161df"></a><a name="aa6c29f654ac148548d0dfbefdad161df"></a>handler.*</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a46e2a86b2c3b4131a58b4f13abe43a4b"><a name="a46e2a86b2c3b4131a58b4f13abe43a4b"></a><a name="a46e2a86b2c3b4131a58b4f13abe43a4b"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8a63417c5c2b4057af6e9efb3937698d"><a name="a8a63417c5c2b4057af6e9efb3937698d"></a><a name="a8a63417c5c2b4057af6e9efb3937698d"></a>Handler parameters.</p>
    </td>
    </tr>
    <tr id="r521743e977d54c95b575435ef1d75f79"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="acb8a7d6be0114160950779fdec98d1da"><a name="acb8a7d6be0114160950779fdec98d1da"></a><a name="acb8a7d6be0114160950779fdec98d1da"></a>enableSSL</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ac87f6404fb764c6fbf6535220ef564b3"><a name="ac87f6404fb764c6fbf6535220ef564b3"></a><a name="ac87f6404fb764c6fbf6535220ef564b3"></a>false</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a325d24f0c9d546239415f2578db887d8"><a name="a325d24f0c9d546239415f2578db887d8"></a><a name="a325d24f0c9d546239415f2578db887d8"></a>Indicates whether SSL is enabled in HTTP.</p>
    </td>
    </tr>
    <tr id="r96e9ac4b6eb44732b97280ecd5515a5a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a7af82a2e1ebd432aae1e8a6e4004084b"><a name="a7af82a2e1ebd432aae1e8a6e4004084b"></a><a name="a7af82a2e1ebd432aae1e8a6e4004084b"></a>keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a135d642c5c5e4c5191e3eed64240d1d7"><a name="a135d642c5c5e4c5191e3eed64240d1d7"></a><a name="a135d642c5c5e4c5191e3eed64240d1d7"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a827d70d60fe443f2b107d68a288928c2"><a name="a827d70d60fe443f2b107d68a288928c2"></a><a name="a827d70d60fe443f2b107d68a288928c2"></a>Keystore path after SSL is enabled in HTTP.</p>
    </td>
    </tr>
    <tr id="rc9214a682660416a80eea7a67409fe16"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a6b1b98b041014765a6e7f17be45673a0"><a name="a6b1b98b041014765a6e7f17be45673a0"></a><a name="a6b1b98b041014765a6e7f17be45673a0"></a>keystorePassword</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="acee36d9763e44ae782fb28deeb8e5c81"><a name="acee36d9763e44ae782fb28deeb8e5c81"></a><a name="acee36d9763e44ae782fb28deeb8e5c81"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a84dec87e9d1a4b2a8d945c71fa7e7882"><a name="a84dec87e9d1a4b2a8d945c71fa7e7882"></a><a name="a84dec87e9d1a4b2a8d945c71fa7e7882"></a>Keystore password after SSL is enabled in HTTP.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **OBS Source**

    An OBS source monitors and transmits new files that have been added to specified buckets in quasi-real-time mode. Common configurations are as follows.

    **Table  6**  Common configurations of an OBS source

    <a name="t58fa0b46ed4c44ffa9357c99e4ae3c2d"></a>
    <table><thead align="left"><tr id="r910a9ccfae434f7aa392b60d6a34facd"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="af664a91cefc649999d4a9856373f542a"><a name="af664a91cefc649999d4a9856373f542a"></a><a name="af664a91cefc649999d4a9856373f542a"></a><strong id="ab27525c4ae9444d5baed3640ebeb6bad"><a name="ab27525c4ae9444d5baed3640ebeb6bad"></a><a name="ab27525c4ae9444d5baed3640ebeb6bad"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="ae42f197f619b4744bbebd4bf9b2a7957"><a name="ae42f197f619b4744bbebd4bf9b2a7957"></a><a name="ae42f197f619b4744bbebd4bf9b2a7957"></a><strong id="a6a930c9c0239456eaf8f8e25ecdd3a99"><a name="a6a930c9c0239456eaf8f8e25ecdd3a99"></a><a name="a6a930c9c0239456eaf8f8e25ecdd3a99"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="ad5d51ac92d0f47d29f2a7d09391bbd9f"><a name="ad5d51ac92d0f47d29f2a7d09391bbd9f"></a><a name="ad5d51ac92d0f47d29f2a7d09391bbd9f"></a><strong id="ae8a41b9e72e641feb84bc8b14cbe9a17"><a name="ae8a41b9e72e641feb84bc8b14cbe9a17"></a><a name="ae8a41b9e72e641feb84bc8b14cbe9a17"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r8438096bf3634d6d80cb75ac4e023dfb"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="abca14bd7a510428b9895fe8dac92abb9"><a name="abca14bd7a510428b9895fe8dac92abb9"></a><a name="abca14bd7a510428b9895fe8dac92abb9"></a>channels</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a17023c7c45f24e23b431fb2b2e740b4f"><a name="a17023c7c45f24e23b431fb2b2e740b4f"></a><a name="a17023c7c45f24e23b431fb2b2e740b4f"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a51d8e27c4f4746358ea5f61c5584e48d"><a name="a51d8e27c4f4746358ea5f61c5584e48d"></a><a name="a51d8e27c4f4746358ea5f61c5584e48d"></a>Channel connected to the source. Multiple channels can be configured.</p>
    </td>
    </tr>
    <tr id="r5cca258002494fff844048bc258fa0f8"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a30d83863939149faa9df4253f2e2ead8"><a name="a30d83863939149faa9df4253f2e2ead8"></a><a name="a30d83863939149faa9df4253f2e2ead8"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ac91acd25292e46a78a83fe08710f4b34"><a name="ac91acd25292e46a78a83fe08710f4b34"></a><a name="ac91acd25292e46a78a83fe08710f4b34"></a>http</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a08cda59f8d824e359a2cef18898f069b"><a name="a08cda59f8d824e359a2cef18898f069b"></a><a name="a08cda59f8d824e359a2cef18898f069b"></a>Type, which is set to <span class="parmvalue" id="p963e0f6568a8432aa732e9cb9bb0d235"><a name="p963e0f6568a8432aa732e9cb9bb0d235"></a><a name="p963e0f6568a8432aa732e9cb9bb0d235"></a><b>org.apache.flume.source.s3.OBSSource</b></span>.</p>
    </td>
    </tr>
    <tr id="rafbf9ce30a5f45e09388d1fd82e9951d"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a1412735d4d23404cabdf3ac6245567f3"><a name="a1412735d4d23404cabdf3ac6245567f3"></a><a name="a1412735d4d23404cabdf3ac6245567f3"></a>bucketName</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ace7def42355147c1a52da8b58a0293b5"><a name="ace7def42355147c1a52da8b58a0293b5"></a><a name="ace7def42355147c1a52da8b58a0293b5"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aaeffef279bfd479c9ec0ce5f3b1b07d7"><a name="aaeffef279bfd479c9ec0ce5f3b1b07d7"></a><a name="aaeffef279bfd479c9ec0ce5f3b1b07d7"></a>OBS bucket name.</p>
    </td>
    </tr>
    <tr id="ra53e90d01b9a46bcba203201aee2b080"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a83a1a764fe8748bc8d46ead5364686ab"><a name="a83a1a764fe8748bc8d46ead5364686ab"></a><a name="a83a1a764fe8748bc8d46ead5364686ab"></a><span id="p68a11e5377c8497d89a55fc0175df509"><a name="p68a11e5377c8497d89a55fc0175df509"></a><a name="p68a11e5377c8497d89a55fc0175df509"></a>prefix</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1483d76f7cbb4d69badb942fef743852"><a name="a1483d76f7cbb4d69badb942fef743852"></a><a name="a1483d76f7cbb4d69badb942fef743852"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a268f5bdb843749129a878a3a3be809b4"><a name="a268f5bdb843749129a878a3a3be809b4"></a><a name="a268f5bdb843749129a878a3a3be809b4"></a><span id="pc362c57f9141425881add514ce508058"><a name="pc362c57f9141425881add514ce508058"></a><a name="pc362c57f9141425881add514ce508058"></a>Monitored OBS path of the specified bucket. The path cannot start with a slash (/). If this parameter is not set, the root directory of the bucket will be monitored by default.</span></p>
    </td>
    </tr>
    <tr id="r6604b420b2c649ca8ed00e446995bb1a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a9d06e271818b400e9c14e6f3f8875091"><a name="a9d06e271818b400e9c14e6f3f8875091"></a><a name="a9d06e271818b400e9c14e6f3f8875091"></a>accessKey</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aa65ceb12a2b0458f97fce80fde540c5f"><a name="aa65ceb12a2b0458f97fce80fde540c5f"></a><a name="aa65ceb12a2b0458f97fce80fde540c5f"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad52aa4b1d42743379b367ec8916768c8"><a name="ad52aa4b1d42743379b367ec8916768c8"></a><a name="ad52aa4b1d42743379b367ec8916768c8"></a>User AK information.</p>
    </td>
    </tr>
    <tr id="r2c0cab1e74ca47df8ff3fb170a30599a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aa6b90a70d6804a7582b610c1650776fe"><a name="aa6b90a70d6804a7582b610c1650776fe"></a><a name="aa6b90a70d6804a7582b610c1650776fe"></a>secretKey</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aa4228a7e17054bf2be8c283e24609781"><a name="aa4228a7e17054bf2be8c283e24609781"></a><a name="aa4228a7e17054bf2be8c283e24609781"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="acaa8b2c793d84091abea9c9f5721fba3"><a name="acaa8b2c793d84091abea9c9f5721fba3"></a><a name="acaa8b2c793d84091abea9c9f5721fba3"></a>User SK information in ciphertext.</p>
    </td>
    </tr>
    <tr id="r03c44e07eece455a861590bafad8bf98"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aeaa3f2d623a440419eb1487147c1207d"><a name="aeaa3f2d623a440419eb1487147c1207d"></a><a name="aeaa3f2d623a440419eb1487147c1207d"></a>backingDir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aeea5951876964ec9bfb1f8d9e9847ff1"><a name="aeea5951876964ec9bfb1f8d9e9847ff1"></a><a name="aeea5951876964ec9bfb1f8d9e9847ff1"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a91ceaff1670e4937892cf66ae9909f76"><a name="a91ceaff1670e4937892cf66ae9909f76"></a><a name="a91ceaff1670e4937892cf66ae9909f76"></a>Metadata storage directory during transmission.</p>
    </td>
    </tr>
    <tr id="refc209575f9446e0a023846fb468f95c"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ae437cb1ecf314236a6f66f7afbee64cf"><a name="ae437cb1ecf314236a6f66f7afbee64cf"></a><a name="ae437cb1ecf314236a6f66f7afbee64cf"></a>endPoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ad758440a31814cdfab0d3e34db53d8a1"><a name="ad758440a31814cdfab0d3e34db53d8a1"></a><a name="ad758440a31814cdfab0d3e34db53d8a1"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a82a6b71333b943d9827fdf42aae195e4"><a name="a82a6b71333b943d9827fdf42aae195e4"></a><a name="a82a6b71333b943d9827fdf42aae195e4"></a>OBS access address. The address must be in the same region as MRS. The value can be either a domain name or an IP address.</p>
    </td>
    </tr>
    <tr id="re6647b73cd504ac6a12bf6469f9a86c6"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a9db721bbfa88440c899deced174f2adf"><a name="a9db721bbfa88440c899deced174f2adf"></a><a name="a9db721bbfa88440c899deced174f2adf"></a>basenameHeader</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="af7d54ced70c74ac385ab028ffa933c0a"><a name="af7d54ced70c74ac385ab028ffa933c0a"></a><a name="af7d54ced70c74ac385ab028ffa933c0a"></a>false</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aeef838a451774d3495c69d058d11dd92"><a name="aeef838a451774d3495c69d058d11dd92"></a><a name="aeef838a451774d3495c69d058d11dd92"></a>Indicates whether to save file names in the event header. <span class="parmvalue" id="p762e6ad3f56742acba6d93540f373d9d"><a name="p762e6ad3f56742acba6d93540f373d9d"></a><a name="p762e6ad3f56742acba6d93540f373d9d"></a><b>false</b></span> indicates that file names are not saved.</p>
    </td>
    </tr>
    <tr id="r6da2b599e2cd45e4a8b28e1213cd37cb"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ac27883a8da914e7189493c340b2d4a6d"><a name="ac27883a8da914e7189493c340b2d4a6d"></a><a name="ac27883a8da914e7189493c340b2d4a6d"></a>basenameHeaderKey</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a50a39925b34b4410a97947bb2701ec28"><a name="a50a39925b34b4410a97947bb2701ec28"></a><a name="a50a39925b34b4410a97947bb2701ec28"></a>basename</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a852f302623614c338a187287456b66e4"><a name="a852f302623614c338a187287456b66e4"></a><a name="a852f302623614c338a187287456b66e4"></a>Name of the field that the event header uses to save a file name, which is also called the key name.</p>
    </td>
    </tr>
    <tr id="r42b4fd84a1a14ccda087ebeaef4c6806"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a817c53628f8b4bc7b6c3bcc815eda768"><a name="a817c53628f8b4bc7b6c3bcc815eda768"></a><a name="a817c53628f8b4bc7b6c3bcc815eda768"></a>batchSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a5e2cbdd49bbc400c8edd0400b5f31edd"><a name="a5e2cbdd49bbc400c8edd0400b5f31edd"></a><a name="a5e2cbdd49bbc400c8edd0400b5f31edd"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="acc87be2de54446a6845fb2d4876a147c"><a name="acc87be2de54446a6845fb2d4876a147c"></a><a name="acc87be2de54446a6845fb2d4876a147c"></a>Source transmission granularity.</p>
    </td>
    </tr>
    <tr id="r0dec623452d8410895a5c2a471c5a259"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a556849fec2a24f359fe3fb008f590e8b"><a name="a556849fec2a24f359fe3fb008f590e8b"></a><a name="a556849fec2a24f359fe3fb008f590e8b"></a>decodeErrorPolicy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a4723653019bd4b81bdedf80ef30572ad"><a name="a4723653019bd4b81bdedf80ef30572ad"></a><a name="a4723653019bd4b81bdedf80ef30572ad"></a>FAIL</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a56a9f3a0a9e7425e8e807bee7864cb91"><a name="a56a9f3a0a9e7425e8e807bee7864cb91"></a><a name="a56a9f3a0a9e7425e8e807bee7864cb91"></a>Code error policy</p>
    <div class="note" id="n36fd53ff6c594e7da6968a68ad9a9c91"><a name="n36fd53ff6c594e7da6968a68ad9a9c91"></a><a name="n36fd53ff6c594e7da6968a68ad9a9c91"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="acaa0728e26324421a2f0d14f06819360"><a name="acaa0728e26324421a2f0d14f06819360"></a><a name="acaa0728e26324421a2f0d14f06819360"></a>If a code error occurs in the file, set <strong id="a524f116425614dcfa7e36fb6ec9bc70d"><a name="a524f116425614dcfa7e36fb6ec9bc70d"></a><a name="a524f116425614dcfa7e36fb6ec9bc70d"></a>decodeErrorPolicy</strong>&nbsp;to&nbsp;<strong id="a3a15cea6c60d4a5f91a51cc6f923d1b4"><a name="a3a15cea6c60d4a5f91a51cc6f923d1b4"></a><a name="a3a15cea6c60d4a5f91a51cc6f923d1b4"></a>REPLACE</strong>&nbsp;or&nbsp;<strong id="acce1d071dd3c463cabe835536ce96916"><a name="acce1d071dd3c463cabe835536ce96916"></a><a name="acce1d071dd3c463cabe835536ce96916"></a>IGNORE</strong>. Flume will skip the code error and continue to collect subsequent logs.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r4c7fa0bcc1434fdb87ab18f5f9ac4798"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a9a963823b21040bcb31ba7426cbbb7da"><a name="a9a963823b21040bcb31ba7426cbbb7da"></a><a name="a9a963823b21040bcb31ba7426cbbb7da"></a>deserializer</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ac2eaacd583b24183ab44dd7bcf0fce1d"><a name="ac2eaacd583b24183ab44dd7bcf0fce1d"></a><a name="ac2eaacd583b24183ab44dd7bcf0fce1d"></a>LINE</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a7fa7c462c74244498d9f5597aec956c4"><a name="a7fa7c462c74244498d9f5597aec956c4"></a><a name="a7fa7c462c74244498d9f5597aec956c4"></a>File parser. The value can be either <span class="parmvalue" id="p4b5681c35a194d46ad369480d50e0fe6"><a name="p4b5681c35a194d46ad369480d50e0fe6"></a><a name="p4b5681c35a194d46ad369480d50e0fe6"></a><b>LINE</b></span>&nbsp;or&nbsp;<span class="parmvalue" id="pd3520b7faf584d79aa875551f7e40334"><a name="pd3520b7faf584d79aa875551f7e40334"></a><a name="pd3520b7faf584d79aa875551f7e40334"></a><b>BufferedLine</b></span>.</p>
    <a name="u65c5347be016494aa025ec4b930c3571"></a><a name="u65c5347be016494aa025ec4b930c3571"></a><ul id="u65c5347be016494aa025ec4b930c3571"><li>When the value is set to <span class="parmname" id="paf2746e1726041a095f71a62e920faea"><a name="paf2746e1726041a095f71a62e920faea"></a><a name="paf2746e1726041a095f71a62e920faea"></a><b>LINE</b></span>, characters read from the file are transcoded one by one.</li><li>When the value is set to <span class="parmvalue" id="p6045e83794cc4fcebae1f5a6aef08ed8"><a name="p6045e83794cc4fcebae1f5a6aef08ed8"></a><a name="p6045e83794cc4fcebae1f5a6aef08ed8"></a><b>BufferedLine</b></span>, one line or multiple lines of characters read from the file are transcoded in batches, which delivers better performance.</li></ul>
    </td>
    </tr>
    <tr id="r117570b71f0745aeac14f18f1bbc1fbe"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a380501247a624b24978bc12b890cfe0c"><a name="a380501247a624b24978bc12b890cfe0c"></a><a name="a380501247a624b24978bc12b890cfe0c"></a>deserializer.maxLineLength</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="abc790072aae84fd1993b705d6de1b8ea"><a name="abc790072aae84fd1993b705d6de1b8ea"></a><a name="abc790072aae84fd1993b705d6de1b8ea"></a>2048</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aaa3794b113af48f0a7008eed29576efb"><a name="aaa3794b113af48f0a7008eed29576efb"></a><a name="aaa3794b113af48f0a7008eed29576efb"></a>Maximum length for resolution by line.</p>
    </td>
    </tr>
    <tr id="ra66399f245224217b657b270e9fa6314"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a96d8947e9ed344a5b260154eb2571b67"><a name="a96d8947e9ed344a5b260154eb2571b67"></a><a name="a96d8947e9ed344a5b260154eb2571b67"></a>deserializer.maxBatchLine</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a7f6099d50d824825a44c8d9b7f1619ed"><a name="a7f6099d50d824825a44c8d9b7f1619ed"></a><a name="a7f6099d50d824825a44c8d9b7f1619ed"></a>1</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab1c37ee70fa54541bcaed88f64b067f1"><a name="ab1c37ee70fa54541bcaed88f64b067f1"></a><a name="ab1c37ee70fa54541bcaed88f64b067f1"></a>Maximum number of lines for resolution by line. If multiple lines are set, <span class="parmvalue" id="peeacf51516304d428c7f39b15fc54a61"><a name="peeacf51516304d428c7f39b15fc54a61"></a><a name="peeacf51516304d428c7f39b15fc54a61"></a><b>maxLineLength</b></span> must be set to a corresponding multiplier.</p>
    </td>
    </tr>
    <tr id="ra2f8925ce41e401a95a59e5f93ed09b5"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ad32094fcaa2a4d9c972c9b9c7fe8ca47"><a name="ad32094fcaa2a4d9c972c9b9c7fe8ca47"></a><a name="ad32094fcaa2a4d9c972c9b9c7fe8ca47"></a>selector.type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a53a9dbc32b494c389556597dfcf0ebfc"><a name="a53a9dbc32b494c389556597dfcf0ebfc"></a><a name="a53a9dbc32b494c389556597dfcf0ebfc"></a>replicating</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a84c1fe548f2b453fa7f40303727201d7"><a name="a84c1fe548f2b453fa7f40303727201d7"></a><a name="a84c1fe548f2b453fa7f40303727201d7"></a>Selector type. The value can be either <span class="parmvalue" id="pe215c1e0e10846aba2e54bf575f22ec3"><a name="pe215c1e0e10846aba2e54bf575f22ec3"></a><a name="pe215c1e0e10846aba2e54bf575f22ec3"></a><b>replicating</b></span>&nbsp;or&nbsp;<span class="parmvalue" id="pc28ed50656114a7a91c552a473777c8a"><a name="pc28ed50656114a7a91c552a473777c8a"></a><a name="pc28ed50656114a7a91c552a473777c8a"></a><b>multiplexing</b></span>.</p>
    </td>
    </tr>
    <tr id="r06c665dc229e40b584f97660e6fa4dd9"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a27eedb82689c451ca89ad82eeed61e6b"><a name="a27eedb82689c451ca89ad82eeed61e6b"></a><a name="a27eedb82689c451ca89ad82eeed61e6b"></a>interceptors</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ac2301d230bb64dc58cd3de804e2a13bd"><a name="ac2301d230bb64dc58cd3de804e2a13bd"></a><a name="ac2301d230bb64dc58cd3de804e2a13bd"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a176151ae2c9248e9a7b5254f2ea54001"><a name="a176151ae2c9248e9a7b5254f2ea54001"></a><a name="a176151ae2c9248e9a7b5254f2ea54001"></a>Interceptor</p>
    </td>
    </tr>
    </tbody>
    </table>


## Common Channel Configurations<a name="saf598c83a3f742d494a14e6b97dfeea3"></a>

-   **Memory Channel**

    A memory channel uses memory as the cache. Events are stored in memory queues. Common configurations are as follows.

    **Table  7**  Common configurations of a memory channel

    <a name="t38d60de16ddc447d94d0b223fe207a99"></a>
    <table><thead align="left"><tr id="r341f97106148453d895bea231c820b72"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="en-us_topic_0066459131_p194642081758"><a name="en-us_topic_0066459131_p194642081758"></a><a name="en-us_topic_0066459131_p194642081758"></a><strong id="en-us_topic_0066459131_b245323111758"><a name="en-us_topic_0066459131_b245323111758"></a><a name="en-us_topic_0066459131_b245323111758"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="en-us_topic_0066459131_p294379441758"><a name="en-us_topic_0066459131_p294379441758"></a><a name="en-us_topic_0066459131_p294379441758"></a><strong id="en-us_topic_0066459131_b330970441758"><a name="en-us_topic_0066459131_b330970441758"></a><a name="en-us_topic_0066459131_b330970441758"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0066459131_p525339371758"><a name="en-us_topic_0066459131_p525339371758"></a><a name="en-us_topic_0066459131_p525339371758"></a><strong id="en-us_topic_0066459131_b356632651758"><a name="en-us_topic_0066459131_b356632651758"></a><a name="en-us_topic_0066459131_b356632651758"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r57cddcb768a44664b3965a460d043038"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p40372161758"><a name="en-us_topic_0066459131_p40372161758"></a><a name="en-us_topic_0066459131_p40372161758"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p585790501758"><a name="en-us_topic_0066459131_p585790501758"></a><a name="en-us_topic_0066459131_p585790501758"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p472825921758"><a name="en-us_topic_0066459131_p472825921758"></a><a name="en-us_topic_0066459131_p472825921758"></a>Type, which is set to <span class="parmvalue" id="pc4ce950703ca4cc9add5a80290f957b2"><a name="pc4ce950703ca4cc9add5a80290f957b2"></a><a name="pc4ce950703ca4cc9add5a80290f957b2"></a><b>memory</b></span>.</p>
    </td>
    </tr>
    <tr id="r87be99b70c7346ae8abf84e8b924c6d8"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p421630201758"><a name="en-us_topic_0066459131_p421630201758"></a><a name="en-us_topic_0066459131_p421630201758"></a>capacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p597614891758"><a name="en-us_topic_0066459131_p597614891758"></a><a name="en-us_topic_0066459131_p597614891758"></a>10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p88424631758"><a name="en-us_topic_0066459131_p88424631758"></a><a name="en-us_topic_0066459131_p88424631758"></a>Maximum number of events cached in a channel.</p>
    </td>
    </tr>
    <tr id="r4308dd7d93714d53a3422eb6acba6a04"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p37047091758"><a name="en-us_topic_0066459131_p37047091758"></a><a name="en-us_topic_0066459131_p37047091758"></a>transactionCapacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p316460311758"><a name="en-us_topic_0066459131_p316460311758"></a><a name="en-us_topic_0066459131_p316460311758"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p131917091758"><a name="en-us_topic_0066459131_p131917091758"></a><a name="en-us_topic_0066459131_p131917091758"></a>Maximum number of events accessed each time.</p>
    </td>
    </tr>
    <tr id="rf4553ea20d29421299025608b31bbc97"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p201886971758"><a name="en-us_topic_0066459131_p201886971758"></a><a name="en-us_topic_0066459131_p201886971758"></a>channelfullcount</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p246717781758"><a name="en-us_topic_0066459131_p246717781758"></a><a name="en-us_topic_0066459131_p246717781758"></a>10</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p522569711758"><a name="en-us_topic_0066459131_p522569711758"></a><a name="en-us_topic_0066459131_p522569711758"></a>Channel full count. When the count reaches the threshold, an alarm is reported.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **File Channel**

    A file channel uses local disks as the cache. Events are stored in the folder specified by  **dataDirs**. Common configurations are as follows.

    **Table  8**  Common configurations of a file channel

    <a name="t12faa00fb2e34243bd0044df35bc77aa"></a>
    <table><thead align="left"><tr id="rd997981abc2f46c4b9cab2b45146db88"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="en-us_topic_0066459131_p498158311758"><a name="en-us_topic_0066459131_p498158311758"></a><a name="en-us_topic_0066459131_p498158311758"></a><strong id="en-us_topic_0066459131_b428177941758"><a name="en-us_topic_0066459131_b428177941758"></a><a name="en-us_topic_0066459131_b428177941758"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="en-us_topic_0066459131_p98456381758"><a name="en-us_topic_0066459131_p98456381758"></a><a name="en-us_topic_0066459131_p98456381758"></a><strong id="en-us_topic_0066459131_b85505001758"><a name="en-us_topic_0066459131_b85505001758"></a><a name="en-us_topic_0066459131_b85505001758"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0066459131_p639308151758"><a name="en-us_topic_0066459131_p639308151758"></a><a name="en-us_topic_0066459131_p639308151758"></a><strong id="en-us_topic_0066459131_b592992071758"><a name="en-us_topic_0066459131_b592992071758"></a><a name="en-us_topic_0066459131_b592992071758"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd61b8ea3de4b44189827eeb5cc608d3b"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p196810201758"><a name="en-us_topic_0066459131_p196810201758"></a><a name="en-us_topic_0066459131_p196810201758"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p506588201758"><a name="en-us_topic_0066459131_p506588201758"></a><a name="en-us_topic_0066459131_p506588201758"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p97237401758"><a name="en-us_topic_0066459131_p97237401758"></a><a name="en-us_topic_0066459131_p97237401758"></a>Type, which is set to <span class="parmvalue" id="pb5232050cc0e4992b9ee554acee083fc"><a name="pb5232050cc0e4992b9ee554acee083fc"></a><a name="pb5232050cc0e4992b9ee554acee083fc"></a><b>file</b></span>.</p>
    </td>
    </tr>
    <tr id="r157923c3e6b54321a954754154ee71af"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p421758891758"><a name="en-us_topic_0066459131_p421758891758"></a><a name="en-us_topic_0066459131_p421758891758"></a>checkpointDir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p608038491758"><a name="en-us_topic_0066459131_p608038491758"></a><a name="en-us_topic_0066459131_p608038491758"></a>${BIGDATA_DATA_HOME}/flume/checkpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p389699911758"><a name="en-us_topic_0066459131_p389699911758"></a><a name="en-us_topic_0066459131_p389699911758"></a>Checkpoint storage directory.</p>
    </td>
    </tr>
    <tr id="rfccc615f28cd4917818f964fe59c7b64"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p220743101758"><a name="en-us_topic_0066459131_p220743101758"></a><a name="en-us_topic_0066459131_p220743101758"></a>dataDirs</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p431886571758"><a name="en-us_topic_0066459131_p431886571758"></a><a name="en-us_topic_0066459131_p431886571758"></a>${BIGDATA_DATA_HOME}/flume/data</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p271583691758"><a name="en-us_topic_0066459131_p271583691758"></a><a name="en-us_topic_0066459131_p271583691758"></a>Data cache directory. Multiple directories can be configured to improve performance. The directories are separated by commas (,).</p>
    </td>
    </tr>
    <tr id="r1ede950e458747abb2217b349568252a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p13367481758"><a name="en-us_topic_0066459131_p13367481758"></a><a name="en-us_topic_0066459131_p13367481758"></a>maxFileSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p411677971758"><a name="en-us_topic_0066459131_p411677971758"></a><a name="en-us_topic_0066459131_p411677971758"></a>2146435071</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p462572661758"><a name="en-us_topic_0066459131_p462572661758"></a><a name="en-us_topic_0066459131_p462572661758"></a>Maximum size of a single cache file. The unit is byte.</p>
    </td>
    </tr>
    <tr id="rbdcaa41b45934db4a7414c01ff39ea3a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p328977111758"><a name="en-us_topic_0066459131_p328977111758"></a><a name="en-us_topic_0066459131_p328977111758"></a>minimumRequiredSpace</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p474689261758"><a name="en-us_topic_0066459131_p474689261758"></a><a name="en-us_topic_0066459131_p474689261758"></a>524288000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p197778221758"><a name="en-us_topic_0066459131_p197778221758"></a><a name="en-us_topic_0066459131_p197778221758"></a>Minimum idle space in the cache. The unit is byte.</p>
    </td>
    </tr>
    <tr id="r99644c7342564141ab3f3b36dba7a924"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p567358561758"><a name="en-us_topic_0066459131_p567358561758"></a><a name="en-us_topic_0066459131_p567358561758"></a>capacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p322015841758"><a name="en-us_topic_0066459131_p322015841758"></a><a name="en-us_topic_0066459131_p322015841758"></a>1000000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p581914841758"><a name="en-us_topic_0066459131_p581914841758"></a><a name="en-us_topic_0066459131_p581914841758"></a>Maximum number of events cached in a channel.</p>
    </td>
    </tr>
    <tr id="r5e6c68901e5c4110bb4b8b33053e2be7"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p87903811758"><a name="en-us_topic_0066459131_p87903811758"></a><a name="en-us_topic_0066459131_p87903811758"></a>transactionCapacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p409322801758"><a name="en-us_topic_0066459131_p409322801758"></a><a name="en-us_topic_0066459131_p409322801758"></a>10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p271803961758"><a name="en-us_topic_0066459131_p271803961758"></a><a name="en-us_topic_0066459131_p271803961758"></a>Maximum number of events accessed each time.</p>
    </td>
    </tr>
    <tr id="r7860e8a4d87c472aa770ec530e8a8334"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p173938391758"><a name="en-us_topic_0066459131_p173938391758"></a><a name="en-us_topic_0066459131_p173938391758"></a>channelfullcount</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p667237271758"><a name="en-us_topic_0066459131_p667237271758"></a><a name="en-us_topic_0066459131_p667237271758"></a>10</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p359127871758"><a name="en-us_topic_0066459131_p359127871758"></a><a name="en-us_topic_0066459131_p359127871758"></a>Channel full count. When the count reaches the threshold, an alarm is reported.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Memory File Channel**

    A memory file channel uses both memory and local disks as its cache and supports message persistence. It provides similar performance as a memory channel and better performance than a file channel. Common configurations are as follows.

    **Table  9**  Common configurations of a memory file channel

    <a name="tfe0604af3bc94ed7875591e953d4d7df"></a>
    <table><thead align="left"><tr id="rfeebe04305c64105bf3b89788408ec87"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="en-us_topic_0066459131_p320572941758"><a name="en-us_topic_0066459131_p320572941758"></a><a name="en-us_topic_0066459131_p320572941758"></a><strong id="en-us_topic_0066459131_b35619211758"><a name="en-us_topic_0066459131_b35619211758"></a><a name="en-us_topic_0066459131_b35619211758"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="en-us_topic_0066459131_p158830191758"><a name="en-us_topic_0066459131_p158830191758"></a><a name="en-us_topic_0066459131_p158830191758"></a><strong id="en-us_topic_0066459131_b465040221758"><a name="en-us_topic_0066459131_b465040221758"></a><a name="en-us_topic_0066459131_b465040221758"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0066459131_p359969161758"><a name="en-us_topic_0066459131_p359969161758"></a><a name="en-us_topic_0066459131_p359969161758"></a><strong id="en-us_topic_0066459131_b114561971758"><a name="en-us_topic_0066459131_b114561971758"></a><a name="en-us_topic_0066459131_b114561971758"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r161baf5ece7b43bc8910df299227974b"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p196765481758"><a name="en-us_topic_0066459131_p196765481758"></a><a name="en-us_topic_0066459131_p196765481758"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p502965381758"><a name="en-us_topic_0066459131_p502965381758"></a><a name="en-us_topic_0066459131_p502965381758"></a>org.apache.flume.channel.MemoryFileChannel</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p247371421758"><a name="en-us_topic_0066459131_p247371421758"></a><a name="en-us_topic_0066459131_p247371421758"></a>Type, which is set to <span class="parmvalue" id="p935ed37d3b7d48f7bc85775afe1479f8"><a name="p935ed37d3b7d48f7bc85775afe1479f8"></a><a name="p935ed37d3b7d48f7bc85775afe1479f8"></a><b>org.apache.flume.channel.MemoryFileChannel</b></span>.</p>
    </td>
    </tr>
    <tr id="reb1fc8e7b6c14bfbb1fc39d377433272"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p482015931758"><a name="en-us_topic_0066459131_p482015931758"></a><a name="en-us_topic_0066459131_p482015931758"></a>capacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p120149941758"><a name="en-us_topic_0066459131_p120149941758"></a><a name="en-us_topic_0066459131_p120149941758"></a>50000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p336904631758"><a name="en-us_topic_0066459131_p336904631758"></a><a name="en-us_topic_0066459131_p336904631758"></a>Channel cache: maximum number of events cached in a channel.</p>
    </td>
    </tr>
    <tr id="rce41e92fb9fc414abc70c97873271d42"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p656126921758"><a name="en-us_topic_0066459131_p656126921758"></a><a name="en-us_topic_0066459131_p656126921758"></a>transactionCapacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p130278271758"><a name="en-us_topic_0066459131_p130278271758"></a><a name="en-us_topic_0066459131_p130278271758"></a>5000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p486210911758"><a name="en-us_topic_0066459131_p486210911758"></a><a name="en-us_topic_0066459131_p486210911758"></a>Transaction cache: maximum number of events processed by a transaction.</p>
    <a name="u1d488811fe4343cd975c257c567f304f"></a><a name="u1d488811fe4343cd975c257c567f304f"></a><ul id="u1d488811fe4343cd975c257c567f304f"><li>The parameter value must be greater than the <span class="parmname" id="p4ea16e501c4148aa8f9b92b4727f7fe0"><a name="p4ea16e501c4148aa8f9b92b4727f7fe0"></a><a name="p4ea16e501c4148aa8f9b92b4727f7fe0"></a><b>batchSize</b></span> of the source and sink.</li><li>The value of <strong id="a8a2fd9df798b4f0c8a68a11244fcd2fa"><a name="a8a2fd9df798b4f0c8a68a11244fcd2fa"></a><a name="a8a2fd9df798b4f0c8a68a11244fcd2fa"></a>transactionCapacity</strong>&nbsp;must be less than or equal to that of&nbsp;<strong id="a36548a0b0a2f4ad88f0e4d7538d73ca2"><a name="a36548a0b0a2f4ad88f0e4d7538d73ca2"></a><a name="a36548a0b0a2f4ad88f0e4d7538d73ca2"></a>capacity</strong>.</li></ul>
    </td>
    </tr>
    <tr id="r0bcfcf2279a54214b0fa9035bc7fb105"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p226459771758"><a name="en-us_topic_0066459131_p226459771758"></a><a name="en-us_topic_0066459131_p226459771758"></a>subqueueByteCapacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p223848741758"><a name="en-us_topic_0066459131_p223848741758"></a><a name="en-us_topic_0066459131_p223848741758"></a>20971520</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p12355441758"><a name="en-us_topic_0066459131_p12355441758"></a><a name="en-us_topic_0066459131_p12355441758"></a>Maximum size (bytes) of events that can be stored in a subqueue.</p>
    <p id="en-us_topic_0066459131_p111199011758"><a name="en-us_topic_0066459131_p111199011758"></a><a name="en-us_topic_0066459131_p111199011758"></a>A memory file channel uses both queues and subqueues to cache data. Events are stored in a subqueue, and subqueues are stored in a queue.</p>
    <p id="en-us_topic_0066459131_p213092601758"><a name="en-us_topic_0066459131_p213092601758"></a><a name="en-us_topic_0066459131_p213092601758"></a><span class="parmname" id="pbf7d567a40a14980b88f963350b0beaa"><a name="pbf7d567a40a14980b88f963350b0beaa"></a><a name="pbf7d567a40a14980b88f963350b0beaa"></a><b>subqueueCapacity</b></span>&nbsp;and&nbsp;<span class="parmname" id="p7165e464c04145a1a272df90e0a74f08"><a name="p7165e464c04145a1a272df90e0a74f08"></a><a name="p7165e464c04145a1a272df90e0a74f08"></a><b>subqueueInterval</b></span>&nbsp;determine the size of events that can be stored in a subqueue.&nbsp;<span class="parmname" id="p5a2d7ab011534bdea36388a30c44b9e5"><a name="p5a2d7ab011534bdea36388a30c44b9e5"></a><a name="p5a2d7ab011534bdea36388a30c44b9e5"></a><b>subqueueCapacity</b></span>&nbsp;specifies the capacity of a subqueue, and&nbsp;<span class="parmname" id="pa225362680c34dc4b54400a7c7fff6ab"><a name="pa225362680c34dc4b54400a7c7fff6ab"></a><a name="pa225362680c34dc4b54400a7c7fff6ab"></a><b>subqueueInterval</b></span>&nbsp;specifies the duration that a subqueue can store events. Events in a subqueue are sent to the destination only after the subqueue reaches the upper limit of&nbsp;<span class="parmname" id="p38b7317db12941bea70f725137997311"><a name="p38b7317db12941bea70f725137997311"></a><a name="p38b7317db12941bea70f725137997311"></a><b>subqueueCapacity</b></span>&nbsp;or&nbsp;<span class="parmname" id="pec2464c9ec1c400db7a2288bbd89e62a"><a name="pec2464c9ec1c400db7a2288bbd89e62a"></a><a name="pec2464c9ec1c400db7a2288bbd89e62a"></a><b>subqueueInterval</b></span>.</p>
    <div class="note" id="n1a0f2a290d274927a89e93452a96477f"><a name="n1a0f2a290d274927a89e93452a96477f"></a><a name="n1a0f2a290d274927a89e93452a96477f"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0066459131_p483284801758"><a name="en-us_topic_0066459131_p483284801758"></a><a name="en-us_topic_0066459131_p483284801758"></a>The value of <span class="parmname" id="p44a4acdaec64450b97e41e2a7afb2bcf"><a name="p44a4acdaec64450b97e41e2a7afb2bcf"></a><a name="p44a4acdaec64450b97e41e2a7afb2bcf"></a><b>subqueueByteCapacity</b></span>&nbsp;must be greater than the number of events specified by&nbsp;<strong id="a84dee1c74c8b44bb8a788c0384f8e8d4"><a name="a84dee1c74c8b44bb8a788c0384f8e8d4"></a><a name="a84dee1c74c8b44bb8a788c0384f8e8d4"></a>batchSize</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r526a3a9d9d0446de9f489e96ed9a3ec9"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p608864221758"><a name="en-us_topic_0066459131_p608864221758"></a><a name="en-us_topic_0066459131_p608864221758"></a>subqueueInterval</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p328531271758"><a name="en-us_topic_0066459131_p328531271758"></a><a name="en-us_topic_0066459131_p328531271758"></a>2000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p438576621758"><a name="en-us_topic_0066459131_p438576621758"></a><a name="en-us_topic_0066459131_p438576621758"></a>Maximum duration (milliseconds) that a subqueue can store events.</p>
    </td>
    </tr>
    <tr id="r4bd1c0de201548928dba6284d66db00b"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p284163581758"><a name="en-us_topic_0066459131_p284163581758"></a><a name="en-us_topic_0066459131_p284163581758"></a>keep-alive</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p200236381758"><a name="en-us_topic_0066459131_p200236381758"></a><a name="en-us_topic_0066459131_p200236381758"></a>3</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p113019911758"><a name="en-us_topic_0066459131_p113019911758"></a><a name="en-us_topic_0066459131_p113019911758"></a>Waiting time of the Put and Take threads when the transaction or channel cache is full. The unit is second.</p>
    </td>
    </tr>
    <tr id="r7fcf47814c5043e0ac908dba7cdcc769"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p641804901758"><a name="en-us_topic_0066459131_p641804901758"></a><a name="en-us_topic_0066459131_p641804901758"></a>dataDir</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p312372291758"><a name="en-us_topic_0066459131_p312372291758"></a><a name="en-us_topic_0066459131_p312372291758"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p471876001758"><a name="en-us_topic_0066459131_p471876001758"></a><a name="en-us_topic_0066459131_p471876001758"></a>Cache directory for local files.</p>
    </td>
    </tr>
    <tr id="r75618daaca7345b0bc0083180cac3236"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p400221351758"><a name="en-us_topic_0066459131_p400221351758"></a><a name="en-us_topic_0066459131_p400221351758"></a>byteCapacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p205675391758"><a name="en-us_topic_0066459131_p205675391758"></a><a name="en-us_topic_0066459131_p205675391758"></a>80% of the maximum JVM memory</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p553579301758"><a name="en-us_topic_0066459131_p553579301758"></a><a name="en-us_topic_0066459131_p553579301758"></a>Channel cache capacity. Unit: byte</p>
    </td>
    </tr>
    <tr id="re085a9bfb97842959cfa6804ef4bfbb1"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p102116951758"><a name="en-us_topic_0066459131_p102116951758"></a><a name="en-us_topic_0066459131_p102116951758"></a>compression-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p218409721758"><a name="en-us_topic_0066459131_p218409721758"></a><a name="en-us_topic_0066459131_p218409721758"></a>None</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p565586961758"><a name="en-us_topic_0066459131_p565586961758"></a><a name="en-us_topic_0066459131_p565586961758"></a>Message compression format. The value can be either <span class="parmvalue" id="p66bbf8fb01a246bfb409e954fad66234"><a name="p66bbf8fb01a246bfb409e954fad66234"></a><a name="p66bbf8fb01a246bfb409e954fad66234"></a><b>None</b></span>&nbsp;or&nbsp;<span class="parmvalue" id="p58f8c796bcf748eea16a0c1361fec9a8"><a name="p58f8c796bcf748eea16a0c1361fec9a8"></a><a name="p58f8c796bcf748eea16a0c1361fec9a8"></a><b>Snappy</b></span>. When the format is&nbsp;<span class="parmvalue" id="p143527a7b8264df4913f00f88e713a92"><a name="p143527a7b8264df4913f00f88e713a92"></a><a name="p143527a7b8264df4913f00f88e713a92"></a><b>Snappy</b></span>, event message bodies that are compressed in the Snappy format can be decompressed.</p>
    </td>
    </tr>
    <tr id="rd0a78d0bbf3b457eb42fe410a7fd2f3d"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p264474701758"><a name="en-us_topic_0066459131_p264474701758"></a><a name="en-us_topic_0066459131_p264474701758"></a>channelfullcount</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p618703141758"><a name="en-us_topic_0066459131_p618703141758"></a><a name="en-us_topic_0066459131_p618703141758"></a>10</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p454394981758"><a name="en-us_topic_0066459131_p454394981758"></a><a name="en-us_topic_0066459131_p454394981758"></a>Channel full count. When the count reaches the threshold, an alarm is reported.</p>
    </td>
    </tr>
    </tbody>
    </table>

    The following is a configuration example of a memory file channel:

    ```
    server.channels.c1.type = org.apache.flume.channel.MemoryFileChannel
    server.channels.c1.dataDir = /opt/flume/mfdata
    server.channels.c1.subqueueByteCapacity = 20971520
    server.channels.c1.subqueueInterval=2000
    server.channels.c1.capacity = 500000
    server.channels.c1.transactionCapacity = 40000
    ```

-   **Kafka Channel**

    A Kafka channel uses a Kafka cluster as the cache. Kafka provides high availability and multiple copies to prevent data from being immediately consumed by sinks when Flume or Kafka Broker crashes.

    **Table  10**  Common configurations of a Kafka channel

    <a name="t489af7f4f3cc4546b697898c978946d7"></a>
    <table><thead align="left"><tr id="r85174cd31c4b42668dc288c5c79697d0"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="en-us_topic_0066459131_p105045311758"><a name="en-us_topic_0066459131_p105045311758"></a><a name="en-us_topic_0066459131_p105045311758"></a><strong id="af8303a22f3e84111a81e9d73d540f8c2"><a name="af8303a22f3e84111a81e9d73d540f8c2"></a><a name="af8303a22f3e84111a81e9d73d540f8c2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="en-us_topic_0066459131_p73927981758"><a name="en-us_topic_0066459131_p73927981758"></a><a name="en-us_topic_0066459131_p73927981758"></a><strong id="aee1d75ae659d491893984d339db283f5"><a name="aee1d75ae659d491893984d339db283f5"></a><a name="aee1d75ae659d491893984d339db283f5"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0066459131_p206406681758"><a name="en-us_topic_0066459131_p206406681758"></a><a name="en-us_topic_0066459131_p206406681758"></a><strong id="ad0d295f1eb854435b93597a972b517cb"><a name="ad0d295f1eb854435b93597a972b517cb"></a><a name="ad0d295f1eb854435b93597a972b517cb"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rf0cdacef18f646e3967953557ef8e8d0"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p648505311758"><a name="en-us_topic_0066459131_p648505311758"></a><a name="en-us_topic_0066459131_p648505311758"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p184016431758"><a name="en-us_topic_0066459131_p184016431758"></a><a name="en-us_topic_0066459131_p184016431758"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p601339601758"><a name="en-us_topic_0066459131_p601339601758"></a><a name="en-us_topic_0066459131_p601339601758"></a>Type, which is set to <span class="parmvalue" id="pabd7fb62bd5b4949adac573fc50b9a8f"><a name="pabd7fb62bd5b4949adac573fc50b9a8f"></a><a name="pabd7fb62bd5b4949adac573fc50b9a8f"></a><b>org.apache.flume.channel.kafka.KafkaChannel</b></span>.</p>
    </td>
    </tr>
    <tr id="r6b8982d829514def8bdc66beb57fc482"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p155690131758"><a name="en-us_topic_0066459131_p155690131758"></a><a name="en-us_topic_0066459131_p155690131758"></a>kafka.bootstrap.servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p531305751758"><a name="en-us_topic_0066459131_p531305751758"></a><a name="en-us_topic_0066459131_p531305751758"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p86093461758"><a name="en-us_topic_0066459131_p86093461758"></a><a name="en-us_topic_0066459131_p86093461758"></a>List of Brokers in the Kafka cluster.</p>
    </td>
    </tr>
    <tr id="r35e75abcac2942cb809f30bfa6478cd5"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p350890541758"><a name="en-us_topic_0066459131_p350890541758"></a><a name="en-us_topic_0066459131_p350890541758"></a>kafka.topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p236411081758"><a name="en-us_topic_0066459131_p236411081758"></a><a name="en-us_topic_0066459131_p236411081758"></a>flume-channel</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p358816321758"><a name="en-us_topic_0066459131_p358816321758"></a><a name="en-us_topic_0066459131_p358816321758"></a>Kafka topic used by the channel to cache data.</p>
    </td>
    </tr>
    <tr id="r23672a59fced4e23b54b991c7aea71a9"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p523617011758"><a name="en-us_topic_0066459131_p523617011758"></a><a name="en-us_topic_0066459131_p523617011758"></a>kafka.consumer.group.id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p134394111758"><a name="en-us_topic_0066459131_p134394111758"></a><a name="en-us_topic_0066459131_p134394111758"></a>flume</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p148504811758"><a name="en-us_topic_0066459131_p148504811758"></a><a name="en-us_topic_0066459131_p148504811758"></a>Kafka consumer group ID.</p>
    </td>
    </tr>
    <tr id="r7c112e7063a9457aae892163061896fa"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p214736031758"><a name="en-us_topic_0066459131_p214736031758"></a><a name="en-us_topic_0066459131_p214736031758"></a>parseAsFlumeEvent</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p616402731758"><a name="en-us_topic_0066459131_p616402731758"></a><a name="en-us_topic_0066459131_p616402731758"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p268062201758"><a name="en-us_topic_0066459131_p268062201758"></a><a name="en-us_topic_0066459131_p268062201758"></a>Indicates whether data is parsed into Flume events.</p>
    </td>
    </tr>
    <tr id="rb218fd025d7842e9adf01faa4d9d539e"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p130550941758"><a name="en-us_topic_0066459131_p130550941758"></a><a name="en-us_topic_0066459131_p130550941758"></a>migrateZookeeperOffsets</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p508296631758"><a name="en-us_topic_0066459131_p508296631758"></a><a name="en-us_topic_0066459131_p508296631758"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p235620001758"><a name="en-us_topic_0066459131_p235620001758"></a><a name="en-us_topic_0066459131_p235620001758"></a>Indicates whether to search for offsets in ZooKeeper and submits them to Kafka when there is no offset in Kafka.</p>
    </td>
    </tr>
    <tr id="rb0a2d5717c4c48fca7499042541f3225"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p639379881758"><a name="en-us_topic_0066459131_p639379881758"></a><a name="en-us_topic_0066459131_p639379881758"></a>kafka.consumer.auto.offset.reset</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p115945781758"><a name="en-us_topic_0066459131_p115945781758"></a><a name="en-us_topic_0066459131_p115945781758"></a>latest</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p667456361758"><a name="en-us_topic_0066459131_p667456361758"></a><a name="en-us_topic_0066459131_p667456361758"></a>Consumes data from the specified location when there is no offset.</p>
    </td>
    </tr>
    <tr id="r0e814b52d66748e8ac68b37979455227"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p36428141758"><a name="en-us_topic_0066459131_p36428141758"></a><a name="en-us_topic_0066459131_p36428141758"></a>kafka.producer.security.protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p266325551758"><a name="en-us_topic_0066459131_p266325551758"></a><a name="en-us_topic_0066459131_p266325551758"></a>SASL_PLAINTEXT</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p97533361758"><a name="en-us_topic_0066459131_p97533361758"></a><a name="en-us_topic_0066459131_p97533361758"></a>Kafka producer security protocol.</p>
    </td>
    </tr>
    <tr id="rc25c86c5849a48f3983b4d8880dbca8c"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p637514191758"><a name="en-us_topic_0066459131_p637514191758"></a><a name="en-us_topic_0066459131_p637514191758"></a>kafka.consumer.security.protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p635912801758"><a name="en-us_topic_0066459131_p635912801758"></a><a name="en-us_topic_0066459131_p635912801758"></a>SASL_PLAINTEXT</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa1fe3005b4cb4fd88d5d25e3a180b124"><a name="aa1fe3005b4cb4fd88d5d25e3a180b124"></a><a name="aa1fe3005b4cb4fd88d5d25e3a180b124"></a>Kafka consumer security protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Common Sink Configurations<a name="s54ef19c65fb24c78bfe72811887ba1ba"></a>

-   **HDFS Sink**

    An HDFS sink writes data into HDFS. Common configurations are as follows.

    **Table  11**  Common configurations of an HDFS sink

    <a name="td6d120e24627405892879e7a7610a621"></a>
    <table><thead align="left"><tr id="r837477cdea6b444e886057cf9356ebdf"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="a53f592785c79422e99754093b3db21d6"><a name="a53f592785c79422e99754093b3db21d6"></a><a name="a53f592785c79422e99754093b3db21d6"></a><strong id="a4dbdf569c93e45929dd2b153f1270775"><a name="a4dbdf569c93e45929dd2b153f1270775"></a><a name="a4dbdf569c93e45929dd2b153f1270775"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="a95286b3374774ac3969d680d0a7fd25a"><a name="a95286b3374774ac3969d680d0a7fd25a"></a><a name="a95286b3374774ac3969d680d0a7fd25a"></a><strong id="ab065f06d10744d21b68c4fa90a2aee4e"><a name="ab065f06d10744d21b68c4fa90a2aee4e"></a><a name="ab065f06d10744d21b68c4fa90a2aee4e"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0066459131_p328508017533"><a name="en-us_topic_0066459131_p328508017533"></a><a name="en-us_topic_0066459131_p328508017533"></a><strong id="ac733a79373e4438192e44a1f6244adfe"><a name="ac733a79373e4438192e44a1f6244adfe"></a><a name="ac733a79373e4438192e44a1f6244adfe"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r3a603bc0504c4668b2181cccc3e0d512"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ad2631a0b45694d3681b0e0a93b4922f0"><a name="ad2631a0b45694d3681b0e0a93b4922f0"></a><a name="ad2631a0b45694d3681b0e0a93b4922f0"></a>channel</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a3aa48a255f1e4d7a9794930a8da1d1fd"><a name="a3aa48a255f1e4d7a9794930a8da1d1fd"></a><a name="a3aa48a255f1e4d7a9794930a8da1d1fd"></a><strong id="aebe584752e2e4ca6a74517f17b1834ea"><a name="aebe584752e2e4ca6a74517f17b1834ea"></a><a name="aebe584752e2e4ca6a74517f17b1834ea"></a>-</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p619013817533"><a name="en-us_topic_0066459131_p619013817533"></a><a name="en-us_topic_0066459131_p619013817533"></a>Channel connected to the sink.</p>
    </td>
    </tr>
    <tr id="r7eb1f2b69e3346c0baa2fededb1cad6e"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aba4b49ae6ebd476ca0e1b69550b86ff3"><a name="aba4b49ae6ebd476ca0e1b69550b86ff3"></a><a name="aba4b49ae6ebd476ca0e1b69550b86ff3"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a7558487ef34340ab8ab8904bf325afe2"><a name="a7558487ef34340ab8ab8904bf325afe2"></a><a name="a7558487ef34340ab8ab8904bf325afe2"></a>hdfs</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a443baad96cdf4aaa955939ee3b94281d"><a name="a443baad96cdf4aaa955939ee3b94281d"></a><a name="a443baad96cdf4aaa955939ee3b94281d"></a>Type, which is set to <span class="parmvalue" id="pff4cb5cfce2a4e9684518821aa8ffce4"><a name="pff4cb5cfce2a4e9684518821aa8ffce4"></a><a name="pff4cb5cfce2a4e9684518821aa8ffce4"></a><b>hdfs</b></span>.</p>
    </td>
    </tr>
    <tr id="r056696f1b15b41f789ba32894d78cba3"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="abcbf8e1fb923440e821172fbf7b900df"><a name="abcbf8e1fb923440e821172fbf7b900df"></a><a name="abcbf8e1fb923440e821172fbf7b900df"></a>monTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p843901117533"><a name="en-us_topic_0066459131_p843901117533"></a><a name="en-us_topic_0066459131_p843901117533"></a>0 (disabled)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a85b2614baecb462bab3e5d0a60d89131"><a name="a85b2614baecb462bab3e5d0a60d89131"></a><a name="a85b2614baecb462bab3e5d0a60d89131"></a>Thread monitoring threshold. When the update time (seconds) exceeds the threshold, the sink is restarted.</p>
    </td>
    </tr>
    <tr id="rbc839e5cd2834aab9e6e430ad51cf05b"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ab2e1446f1c3541a5bec269d3d696ff7c"><a name="ab2e1446f1c3541a5bec269d3d696ff7c"></a><a name="ab2e1446f1c3541a5bec269d3d696ff7c"></a>hdfs.path</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a405e77690e1e42c88e689ee5a427c5a7"><a name="a405e77690e1e42c88e689ee5a427c5a7"></a><a name="a405e77690e1e42c88e689ee5a427c5a7"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ae4673d8a36584e89844c8969020ccaa1"><a name="ae4673d8a36584e89844c8969020ccaa1"></a><a name="ae4673d8a36584e89844c8969020ccaa1"></a>HDFS path.</p>
    </td>
    </tr>
    <tr id="r73d44f658ed94605b2a6310d90fe8425"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a5a6c0b4071464c9f9ae81162d8fef34a"><a name="a5a6c0b4071464c9f9ae81162d8fef34a"></a><a name="a5a6c0b4071464c9f9ae81162d8fef34a"></a>hdfs.inUseSuffix</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a11dc7fbda4f145549726e4d5f1930f59"><a name="a11dc7fbda4f145549726e4d5f1930f59"></a><a name="a11dc7fbda4f145549726e4d5f1930f59"></a>.tmp</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3413f03494834bbe920a1386baddd58f"><a name="a3413f03494834bbe920a1386baddd58f"></a><a name="a3413f03494834bbe920a1386baddd58f"></a>Suffix of the HDFS file being written.</p>
    </td>
    </tr>
    <tr id="rf904647a26cc4629bbdc5e8a55b869a4"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a1e2cd384f7b04973a5a88c403586c9ee"><a name="a1e2cd384f7b04973a5a88c403586c9ee"></a><a name="a1e2cd384f7b04973a5a88c403586c9ee"></a>hdfs.rollInterval</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p880104717533"><a name="en-us_topic_0066459131_p880104717533"></a><a name="en-us_topic_0066459131_p880104717533"></a>30</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a54f0eb8e4a09490484dc429b82129215"><a name="a54f0eb8e4a09490484dc429b82129215"></a><a name="a54f0eb8e4a09490484dc429b82129215"></a>Interval for file rolling. The unit is second.</p>
    </td>
    </tr>
    <tr id="rd0731f7216a04b80ab6f824a88ffbfd3"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p201758517533"><a name="en-us_topic_0066459131_p201758517533"></a><a name="en-us_topic_0066459131_p201758517533"></a>hdfs.rollSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aac8bf50e782848fe98275d994a0ed70c"><a name="aac8bf50e782848fe98275d994a0ed70c"></a><a name="aac8bf50e782848fe98275d994a0ed70c"></a>1024</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8f3bf764f0e0441d965a0f59049a2f3e"><a name="a8f3bf764f0e0441d965a0f59049a2f3e"></a><a name="a8f3bf764f0e0441d965a0f59049a2f3e"></a>Size for file rolling. The unit is byte.</p>
    </td>
    </tr>
    <tr id="rebf6f1c968e342c887ef2ee16756431b"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="abb2cd629857c4b41a688524c0c5d0260"><a name="abb2cd629857c4b41a688524c0c5d0260"></a><a name="abb2cd629857c4b41a688524c0c5d0260"></a>hdfs.rollCount</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aa6bd3ce1be6143c980a35b2d7c2a7d76"><a name="aa6bd3ce1be6143c980a35b2d7c2a7d76"></a><a name="aa6bd3ce1be6143c980a35b2d7c2a7d76"></a>10</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a4bcf59460aba40baafe4c1d0505a48fc"><a name="a4bcf59460aba40baafe4c1d0505a48fc"></a><a name="a4bcf59460aba40baafe4c1d0505a48fc"></a>Number of events for file rolling.</p>
    </td>
    </tr>
    <tr id="racd3375fe2254561b1f0df17ec7cb30e"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a5fae5711ef46466e93c6d5d071658a74"><a name="a5fae5711ef46466e93c6d5d071658a74"></a><a name="a5fae5711ef46466e93c6d5d071658a74"></a>hdfs.idleTimeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p981461617533"><a name="en-us_topic_0066459131_p981461617533"></a><a name="en-us_topic_0066459131_p981461617533"></a>0</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad9a48b96edbc4306b1b3cdae6cc72160"><a name="ad9a48b96edbc4306b1b3cdae6cc72160"></a><a name="ad9a48b96edbc4306b1b3cdae6cc72160"></a>Timeout interval for closing idle files automatically. The unit is second.</p>
    </td>
    </tr>
    <tr id="r1cb003c70c8d420c86844025a81ebc95"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aa215613787414301a2ec8b09c65ced67"><a name="aa215613787414301a2ec8b09c65ced67"></a><a name="aa215613787414301a2ec8b09c65ced67"></a>hdfs.batchSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a174cff47b6fe4dabb161046dd5a04465"><a name="a174cff47b6fe4dabb161046dd5a04465"></a><a name="a174cff47b6fe4dabb161046dd5a04465"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="af3f9ca4a17e44086a622190d8aca08c9"><a name="af3f9ca4a17e44086a622190d8aca08c9"></a><a name="af3f9ca4a17e44086a622190d8aca08c9"></a>Number of events written into HDFS at a time.</p>
    </td>
    </tr>
    <tr id="r3bd652b13d7e4715b2d9cc979133a5a5"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="af1c8eb95e57f42158326e7d9e1b6e55c"><a name="af1c8eb95e57f42158326e7d9e1b6e55c"></a><a name="af1c8eb95e57f42158326e7d9e1b6e55c"></a>hdfs.kerberosPrincipal</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a3dc1cec4d98e4b3385c59f6cac89591a"><a name="a3dc1cec4d98e4b3385c59f6cac89591a"></a><a name="a3dc1cec4d98e4b3385c59f6cac89591a"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a64e4b1898ccc4bf5acf36422c4c4e60b"><a name="a64e4b1898ccc4bf5acf36422c4c4e60b"></a><a name="a64e4b1898ccc4bf5acf36422c4c4e60b"></a>Kerberos username for HDFS authentication. This parameter is not required for a cluster in which Kerberos authentication is disabled.</p>
    </td>
    </tr>
    <tr id="ra4fec5b078374e57b1c818e37eaae991"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a3b1a57316f594b8b80e4cc5c74f91de6"><a name="a3b1a57316f594b8b80e4cc5c74f91de6"></a><a name="a3b1a57316f594b8b80e4cc5c74f91de6"></a>hdfs.kerberosKeytab</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a0dd23880351c42c3b8585c4daae27624"><a name="a0dd23880351c42c3b8585c4daae27624"></a><a name="a0dd23880351c42c3b8585c4daae27624"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a60585f6fd60e4d51bfde861c8ce1f304"><a name="a60585f6fd60e4d51bfde861c8ce1f304"></a><a name="a60585f6fd60e4d51bfde861c8ce1f304"></a>Kerberos keytab for HDFS authentication. This parameter is not required for a cluster in which Kerberos authentication is disabled.</p>
    </td>
    </tr>
    <tr id="rd08cfd3a3d7144ee8e1513f434b4ee85"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aabb08ddf87164c0c9482c062ecb7e76b"><a name="aabb08ddf87164c0c9482c062ecb7e76b"></a><a name="aabb08ddf87164c0c9482c062ecb7e76b"></a>hdfs.fileCloseByEndEvent</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a28306420c258407ca94ac041919cdc37"><a name="a28306420c258407ca94ac041919cdc37"></a><a name="a28306420c258407ca94ac041919cdc37"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="abb13c13835774baf80e1f3a703548657"><a name="abb13c13835774baf80e1f3a703548657"></a><a name="abb13c13835774baf80e1f3a703548657"></a>Indicates whether the file is closed when the last event is received.</p>
    </td>
    </tr>
    <tr id="r299854accc8147718befb94f27819246"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="abe70f79c0f7645d1bbf38f370ff6bbf5"><a name="abe70f79c0f7645d1bbf38f370ff6bbf5"></a><a name="abe70f79c0f7645d1bbf38f370ff6bbf5"></a>hdfs.batchCallTimeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1d574f52ab444e70b2dccf3a4ecfe470"><a name="a1d574f52ab444e70b2dccf3a4ecfe470"></a><a name="a1d574f52ab444e70b2dccf3a4ecfe470"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a0b685064ff2941a3a22c9027696391e8"><a name="a0b685064ff2941a3a22c9027696391e8"></a><a name="a0b685064ff2941a3a22c9027696391e8"></a>Timeout control duration (milliseconds) each time events are written into HDFS.</p>
    <p id="ad9681a1c7ecc4c1ab39ad6bc17351b44"><a name="ad9681a1c7ecc4c1ab39ad6bc17351b44"></a><a name="ad9681a1c7ecc4c1ab39ad6bc17351b44"></a>If this parameter is not specified, the timeout duration is controlled when each event is written into HDFS. When the value of <span class="parmname" id="pfcf12bdcb148451f90f07a38e4c79104"><a name="pfcf12bdcb148451f90f07a38e4c79104"></a><a name="pfcf12bdcb148451f90f07a38e4c79104"></a><b>hdfs.batchSize</b></span> is greater than 0, configure this parameter to improve the performance of writing data into HDFS.</p>
    <div class="note" id="n36570996163049a8addcd8e06d365eed"><a name="n36570996163049a8addcd8e06d365eed"></a><a name="n36570996163049a8addcd8e06d365eed"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="abc290330f6d4486186a45ca1cb890b94"><a name="abc290330f6d4486186a45ca1cb890b94"></a><a name="abc290330f6d4486186a45ca1cb890b94"></a>The value of <span class="parmname" id="p0f91960486cb483a810e674baf12afa1"><a name="p0f91960486cb483a810e674baf12afa1"></a><a name="p0f91960486cb483a810e674baf12afa1"></a><b>hdfs.batchCallTimeout</b></span>&nbsp;depends on&nbsp;<span class="parmname" id="pbc58d56c879b4968a136daf7278fddd1"><a name="pbc58d56c879b4968a136daf7278fddd1"></a><a name="pbc58d56c879b4968a136daf7278fddd1"></a><b>hdfs.batchSize</b></span>. A greater&nbsp;<span class="parmname" id="p05e89521e1b2402f81c0aa85b66397d2"><a name="p05e89521e1b2402f81c0aa85b66397d2"></a><a name="p05e89521e1b2402f81c0aa85b66397d2"></a><b>hdfs.batchSize</b></span>&nbsp;requires a larger&nbsp;<span class="parmname" id="p94b79ebf928a403cb74839045341f12d"><a name="p94b79ebf928a403cb74839045341f12d"></a><a name="p94b79ebf928a403cb74839045341f12d"></a><b>hdfs.batchCallTimeout</b></span>. If the value of&nbsp;<span class="parmname" id="p7e0266c034b94080b6157c0544b5c75f"><a name="p7e0266c034b94080b6157c0544b5c75f"></a><a name="p7e0266c034b94080b6157c0544b5c75f"></a><b>hdfs.batchCallTimeout</b></span> is too small, writing events to HDFS may fail.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r5c77c4082f234d1b82dbd13b66a0cf10"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a67a60153025c4dd08d4329f76f24aed8"><a name="a67a60153025c4dd08d4329f76f24aed8"></a><a name="a67a60153025c4dd08d4329f76f24aed8"></a>serializer.appendNewline</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a681b548c5a114e4aa042a38e8cb3ef3d"><a name="a681b548c5a114e4aa042a38e8cb3ef3d"></a><a name="a681b548c5a114e4aa042a38e8cb3ef3d"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9a45a9d8c42a4e738bbbae650b80569c"><a name="a9a45a9d8c42a4e738bbbae650b80569c"></a><a name="a9a45a9d8c42a4e738bbbae650b80569c"></a>Indicates whether to add a line feed character (<strong id="a70f6e9b70e754b759319f25938531edb"><a name="a70f6e9b70e754b759319f25938531edb"></a><a name="a70f6e9b70e754b759319f25938531edb"></a>\n</strong>) after an event is written to HDFS. If a line feed character is added, the data volume counters used by the line feed character will not be calculated by HDFS sinks.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Avro Sink**

    An Avro sink converts events into Avro events and sends them to the monitoring ports of the hosts. Common configurations are as follows.

    **Table  12**  Common configurations of an Avro sink

    <a name="t2a9949d7426743a187c25c2b072c21c7"></a>
    <table><thead align="left"><tr id="rb910856e933f4a0f8ed59fbda0d07732"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="en-us_topic_0066459131_p660555417533"><a name="en-us_topic_0066459131_p660555417533"></a><a name="en-us_topic_0066459131_p660555417533"></a><strong id="a942c0682ab934a2fa08571814a47edb9"><a name="a942c0682ab934a2fa08571814a47edb9"></a><a name="a942c0682ab934a2fa08571814a47edb9"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="a5fbf1540aeff45b0b645de9f686ab9ae"><a name="a5fbf1540aeff45b0b645de9f686ab9ae"></a><a name="a5fbf1540aeff45b0b645de9f686ab9ae"></a><strong id="a514eb8dff57747b68a9b815d57f97e93"><a name="a514eb8dff57747b68a9b815d57f97e93"></a><a name="a514eb8dff57747b68a9b815d57f97e93"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a47c221b8ac2b49d49a40e40a54b11dd7"><a name="a47c221b8ac2b49d49a40e40a54b11dd7"></a><a name="a47c221b8ac2b49d49a40e40a54b11dd7"></a><strong id="aec9c1f1d8bf547c2876d7200d57980a9"><a name="aec9c1f1d8bf547c2876d7200d57980a9"></a><a name="aec9c1f1d8bf547c2876d7200d57980a9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r612d37c5f3a54e4fb3bb9493d4d6c9b0"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aeacb92298b204d9597eb8700f405652b"><a name="aeacb92298b204d9597eb8700f405652b"></a><a name="aeacb92298b204d9597eb8700f405652b"></a>channel</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a3c0d7f80b03f4ef9b846e67f9c87e308"><a name="a3c0d7f80b03f4ef9b846e67f9c87e308"></a><a name="a3c0d7f80b03f4ef9b846e67f9c87e308"></a><strong id="ac695b748096340769231099db70ea55d"><a name="ac695b748096340769231099db70ea55d"></a><a name="ac695b748096340769231099db70ea55d"></a>-</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a50aaa53fee95427dba20fb7c72e97f78"><a name="a50aaa53fee95427dba20fb7c72e97f78"></a><a name="a50aaa53fee95427dba20fb7c72e97f78"></a>Channel connected to the sink.</p>
    </td>
    </tr>
    <tr id="r2316a367c9e2413aa1f49e1e3c502ef7"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a15db7b8d111b4ffc8762711446998bb2"><a name="a15db7b8d111b4ffc8762711446998bb2"></a><a name="a15db7b8d111b4ffc8762711446998bb2"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a5b6bdc5feeb14a5b913f0c88ddff3f38"><a name="a5b6bdc5feeb14a5b913f0c88ddff3f38"></a><a name="a5b6bdc5feeb14a5b913f0c88ddff3f38"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a221a3ea31ce448029ef12edb2c208112"><a name="a221a3ea31ce448029ef12edb2c208112"></a><a name="a221a3ea31ce448029ef12edb2c208112"></a>Type, which is set to <span class="parmvalue" id="pe99657d6c88644cbba899ce7f54d33d4"><a name="pe99657d6c88644cbba899ce7f54d33d4"></a><a name="pe99657d6c88644cbba899ce7f54d33d4"></a><b>avro</b></span>.</p>
    </td>
    </tr>
    <tr id="r022e27c9f665447a9eeac370c5ea709a"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aba040a4aa45e41099eedaede7cfeef6e"><a name="aba040a4aa45e41099eedaede7cfeef6e"></a><a name="aba040a4aa45e41099eedaede7cfeef6e"></a>hostname</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p35597717533"><a name="en-us_topic_0066459131_p35597717533"></a><a name="en-us_topic_0066459131_p35597717533"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a44df6ed006214dbfb0a16b2625bb6ad4"><a name="a44df6ed006214dbfb0a16b2625bb6ad4"></a><a name="a44df6ed006214dbfb0a16b2625bb6ad4"></a>Name or IP address of the bound host</p>
    </td>
    </tr>
    <tr id="r635b0f237685424fae20de8129138c4f"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a4ad5816e63f442e69cfd7d59abd6db85"><a name="a4ad5816e63f442e69cfd7d59abd6db85"></a><a name="a4ad5816e63f442e69cfd7d59abd6db85"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p924698617533"><a name="en-us_topic_0066459131_p924698617533"></a><a name="en-us_topic_0066459131_p924698617533"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a0290a2e762b4471cbfaf68245f403f42"><a name="a0290a2e762b4471cbfaf68245f403f42"></a><a name="a0290a2e762b4471cbfaf68245f403f42"></a>Monitoring port</p>
    </td>
    </tr>
    <tr id="r69ea539ddeba41c18f37bb22eee47182"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a5fcbbbf051974d8889d7b51b984e5238"><a name="a5fcbbbf051974d8889d7b51b984e5238"></a><a name="a5fcbbbf051974d8889d7b51b984e5238"></a>batch-size</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aef860c3bbf3441c1b3cfb8e0868d4ea6"><a name="aef860c3bbf3441c1b3cfb8e0868d4ea6"></a><a name="aef860c3bbf3441c1b3cfb8e0868d4ea6"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a237c2c2660e144919ade001dd8c4adbf"><a name="a237c2c2660e144919ade001dd8c4adbf"></a><a name="a237c2c2660e144919ade001dd8c4adbf"></a>Number of events sent in a batch.</p>
    </td>
    </tr>
    <tr id="r1e61d04138554af491cff21e984ac2b2"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a1102f8d6bc8146438c18c90bd0a36e08"><a name="a1102f8d6bc8146438c18c90bd0a36e08"></a><a name="a1102f8d6bc8146438c18c90bd0a36e08"></a>ssl</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p334117217533"><a name="en-us_topic_0066459131_p334117217533"></a><a name="en-us_topic_0066459131_p334117217533"></a>false</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p219951417533"><a name="en-us_topic_0066459131_p219951417533"></a><a name="en-us_topic_0066459131_p219951417533"></a>Indicates whether to use SSL encryption.</p>
    </td>
    </tr>
    <tr id="r25cb26ffd3294c35b8f411ec0be60626"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a81feb4411a4e400c96bd187ab69063f6"><a name="a81feb4411a4e400c96bd187ab69063f6"></a><a name="a81feb4411a4e400c96bd187ab69063f6"></a>truststore-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ad3b289748c0d4cbea9ee74c4c6d3bf50"><a name="ad3b289748c0d4cbea9ee74c4c6d3bf50"></a><a name="ad3b289748c0d4cbea9ee74c4c6d3bf50"></a>JKS</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ae81054280aa3452cbcf67d8dd2c628d2"><a name="ae81054280aa3452cbcf67d8dd2c628d2"></a><a name="ae81054280aa3452cbcf67d8dd2c628d2"></a>Java truststore type.</p>
    </td>
    </tr>
    <tr id="rfcffc13759584289a7dab010d16f6975"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a162b5a4bda2341519c587593addce46a"><a name="a162b5a4bda2341519c587593addce46a"></a><a name="a162b5a4bda2341519c587593addce46a"></a>truststore</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="af979635751184d39bf5ef2f24c3c2680"><a name="af979635751184d39bf5ef2f24c3c2680"></a><a name="af979635751184d39bf5ef2f24c3c2680"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p196860717533"><a name="en-us_topic_0066459131_p196860717533"></a><a name="en-us_topic_0066459131_p196860717533"></a>Java truststore file.</p>
    </td>
    </tr>
    <tr id="r6b947d885bad46cd92eaeb6d62d3b701"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ad368c088bca9483caeee321aacf0a32d"><a name="ad368c088bca9483caeee321aacf0a32d"></a><a name="ad368c088bca9483caeee321aacf0a32d"></a>truststore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aa15d18d746234179a531b956b2215ced"><a name="aa15d18d746234179a531b956b2215ced"></a><a name="aa15d18d746234179a531b956b2215ced"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a3f7b1b27f30542eaab73a692ae12f29f"><a name="a3f7b1b27f30542eaab73a692ae12f29f"></a><a name="a3f7b1b27f30542eaab73a692ae12f29f"></a>Java truststore password.</p>
    </td>
    </tr>
    <tr id="rf63bf2ad46584013bb667acb64809d33"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a57fe54bc5f2945e18d4ba444f0fec43f"><a name="a57fe54bc5f2945e18d4ba444f0fec43f"></a><a name="a57fe54bc5f2945e18d4ba444f0fec43f"></a>keystore-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p476166117533"><a name="en-us_topic_0066459131_p476166117533"></a><a name="en-us_topic_0066459131_p476166117533"></a>JKS</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac0732fd9619e4c5c8af3f86219eddadd"><a name="ac0732fd9619e4c5c8af3f86219eddadd"></a><a name="ac0732fd9619e4c5c8af3f86219eddadd"></a>Keystore type.</p>
    </td>
    </tr>
    <tr id="r59f80081977c408db991b4b012725622"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a4ea83c0676d54e39919fabb7e12d978d"><a name="a4ea83c0676d54e39919fabb7e12d978d"></a><a name="a4ea83c0676d54e39919fabb7e12d978d"></a>keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p831478117533"><a name="en-us_topic_0066459131_p831478117533"></a><a name="en-us_topic_0066459131_p831478117533"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p240867317533"><a name="en-us_topic_0066459131_p240867317533"></a><a name="en-us_topic_0066459131_p240867317533"></a>Keystore file.</p>
    </td>
    </tr>
    <tr id="rbd302194144346908279e270cc119a37"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a081b5354554b4e0d9c1366aaa819eb85"><a name="a081b5354554b4e0d9c1366aaa819eb85"></a><a name="a081b5354554b4e0d9c1366aaa819eb85"></a>keystore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a3e779210bd53463fa6017fce7d435b34"><a name="a3e779210bd53463fa6017fce7d435b34"></a><a name="a3e779210bd53463fa6017fce7d435b34"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aea83b8ffbd094013936071b8495921ae"><a name="aea83b8ffbd094013936071b8495921ae"></a><a name="aea83b8ffbd094013936071b8495921ae"></a>Keystore password.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **HBase Sink**

    An HBase sink writes data into HBase. Common configurations are as follows.

    **Table  13**  Common configurations of an HBase sink

    <a name="t7fecc39f93b34222a30a9298080d678d"></a>
    <table><thead align="left"><tr id="r7e82d60ce638454c829c6c4090fb21fe"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="ac1f9c672b3b8463e821c4770129e2717"><a name="ac1f9c672b3b8463e821c4770129e2717"></a><a name="ac1f9c672b3b8463e821c4770129e2717"></a><strong id="af75f82a19db341e0b7a26a826f05d493"><a name="af75f82a19db341e0b7a26a826f05d493"></a><a name="af75f82a19db341e0b7a26a826f05d493"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="ac938d68cc0bc4d6c835c75047c34b0c1"><a name="ac938d68cc0bc4d6c835c75047c34b0c1"></a><a name="ac938d68cc0bc4d6c835c75047c34b0c1"></a><strong id="a91e8f811d8aa433e907ac239c23b3e3f"><a name="a91e8f811d8aa433e907ac239c23b3e3f"></a><a name="a91e8f811d8aa433e907ac239c23b3e3f"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="en-us_topic_0066459131_p763900917533"><a name="en-us_topic_0066459131_p763900917533"></a><a name="en-us_topic_0066459131_p763900917533"></a><strong id="a9ab86fa99abf44a2a4d136c37b95f0ac"><a name="a9ab86fa99abf44a2a4d136c37b95f0ac"></a><a name="a9ab86fa99abf44a2a4d136c37b95f0ac"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r40d12c8f996547da87b393062b9d3448"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a48fa61da6cf3470384e375c0fd6a705e"><a name="a48fa61da6cf3470384e375c0fd6a705e"></a><a name="a48fa61da6cf3470384e375c0fd6a705e"></a>channel</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="abb42c90b30ef4b51bd7e7fc8c781d34b"><a name="abb42c90b30ef4b51bd7e7fc8c781d34b"></a><a name="abb42c90b30ef4b51bd7e7fc8c781d34b"></a><strong id="adc1e9609d4434b7494448651b4203a2b"><a name="adc1e9609d4434b7494448651b4203a2b"></a><a name="adc1e9609d4434b7494448651b4203a2b"></a>-</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a25d2cf74d4554711847de6c756f5d304"><a name="a25d2cf74d4554711847de6c756f5d304"></a><a name="a25d2cf74d4554711847de6c756f5d304"></a>Channel connected to the sink.</p>
    </td>
    </tr>
    <tr id="r05943b7a869049e9b1da9047cdabc664"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p568160617533"><a name="en-us_topic_0066459131_p568160617533"></a><a name="en-us_topic_0066459131_p568160617533"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1100edd3d5464fd785dcd1727a8e7782"><a name="a1100edd3d5464fd785dcd1727a8e7782"></a><a name="a1100edd3d5464fd785dcd1727a8e7782"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a53411825409044f188a3f4cca548933b"><a name="a53411825409044f188a3f4cca548933b"></a><a name="a53411825409044f188a3f4cca548933b"></a>Type, which is set to <span class="parmvalue" id="p34da2f1f29894dbd99df745c7ecf82a1"><a name="p34da2f1f29894dbd99df745c7ecf82a1"></a><a name="p34da2f1f29894dbd99df745c7ecf82a1"></a><b>hbase</b></span>.</p>
    </td>
    </tr>
    <tr id="r7e509cdc28354cf0a77816b79e858d5c"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a8c8cf8b8d1a84e5e884d3d692de7bf17"><a name="a8c8cf8b8d1a84e5e884d3d692de7bf17"></a><a name="a8c8cf8b8d1a84e5e884d3d692de7bf17"></a>table</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a0e94d64967cc4da58dd3ec497a7abbbd"><a name="a0e94d64967cc4da58dd3ec497a7abbbd"></a><a name="a0e94d64967cc4da58dd3ec497a7abbbd"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9841fe0f73a1409287c95c1a21184114"><a name="a9841fe0f73a1409287c95c1a21184114"></a><a name="a9841fe0f73a1409287c95c1a21184114"></a>HBase table name.</p>
    </td>
    </tr>
    <tr id="r886afc4019c64457bcb6bce3711a8b34"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p99517817533"><a name="en-us_topic_0066459131_p99517817533"></a><a name="en-us_topic_0066459131_p99517817533"></a>monTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a90483535eb734b88b061b7a09cb58124"><a name="a90483535eb734b88b061b7a09cb58124"></a><a name="a90483535eb734b88b061b7a09cb58124"></a>0 (disabled)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a458fb59e17734ebca1e622ade538e252"><a name="a458fb59e17734ebca1e622ade538e252"></a><a name="a458fb59e17734ebca1e622ade538e252"></a>Thread monitoring threshold. When the update time (seconds) exceeds the threshold, the sink is restarted.</p>
    </td>
    </tr>
    <tr id="rea412468a96f42f78e922260d2932e1e"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p802703117533"><a name="en-us_topic_0066459131_p802703117533"></a><a name="en-us_topic_0066459131_p802703117533"></a>columnFamily</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a89cc2374f5b04cfa94d9c67fc71c42bd"><a name="a89cc2374f5b04cfa94d9c67fc71c42bd"></a><a name="a89cc2374f5b04cfa94d9c67fc71c42bd"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a023d273f01714c5e9d98ddb36d90c104"><a name="a023d273f01714c5e9d98ddb36d90c104"></a><a name="a023d273f01714c5e9d98ddb36d90c104"></a>HBase column family.</p>
    </td>
    </tr>
    <tr id="rf977d6b7792e439e88008b552078a397"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a8003c9615e56440f86c2dd2151506487"><a name="a8003c9615e56440f86c2dd2151506487"></a><a name="a8003c9615e56440f86c2dd2151506487"></a>batchSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a845f0d7d6f6a44a7adecb22f5cc2fb9f"><a name="a845f0d7d6f6a44a7adecb22f5cc2fb9f"></a><a name="a845f0d7d6f6a44a7adecb22f5cc2fb9f"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa508f4698a844cca9a9f2889dc64d97f"><a name="aa508f4698a844cca9a9f2889dc64d97f"></a><a name="aa508f4698a844cca9a9f2889dc64d97f"></a>Number of events written into HBase at a time.</p>
    </td>
    </tr>
    <tr id="r796649aa3d7b4f01b291891dfe650645"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p980622217533"><a name="en-us_topic_0066459131_p980622217533"></a><a name="en-us_topic_0066459131_p980622217533"></a>kerberosPrincipal</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ad70805f76b744bffb4cb2d14fc053edb"><a name="ad70805f76b744bffb4cb2d14fc053edb"></a><a name="ad70805f76b744bffb4cb2d14fc053edb"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a151098f74de7480eac8a0f233649fc99"><a name="a151098f74de7480eac8a0f233649fc99"></a><a name="a151098f74de7480eac8a0f233649fc99"></a>Kerberos username for HBase authentication. This parameter is not required for a cluster in which Kerberos authentication is disabled.</p>
    </td>
    </tr>
    <tr id="r442d05eb42de44cca70f3949a3425711"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p379596517533"><a name="en-us_topic_0066459131_p379596517533"></a><a name="en-us_topic_0066459131_p379596517533"></a>kerberosKeytab</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a2a31a62aa80a434eba708096bafcd6b4"><a name="a2a31a62aa80a434eba708096bafcd6b4"></a><a name="a2a31a62aa80a434eba708096bafcd6b4"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p794234417533"><a name="en-us_topic_0066459131_p794234417533"></a><a name="en-us_topic_0066459131_p794234417533"></a>Kerberos keytab for HBase authentication. This parameter is not required for a cluster in which Kerberos authentication is disabled.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Kafka Sink**

    A Kafka sink writes data into Kafka. Common configurations are as follows.

    **Table  14**  Common configurations of a Kafka sink

    <a name="t3fcf8adcdec44e92977aa5daafe65e5e"></a>
    <table><thead align="left"><tr id="rafc4597666f045448c21a6aebfa10a92"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="en-us_topic_0066459131_p565891217533"><a name="en-us_topic_0066459131_p565891217533"></a><a name="en-us_topic_0066459131_p565891217533"></a><strong id="en-us_topic_0066459131_b808530817533"><a name="en-us_topic_0066459131_b808530817533"></a><a name="en-us_topic_0066459131_b808530817533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="adfdb30bb368147e4a35e2bdaedecdd9e"><a name="adfdb30bb368147e4a35e2bdaedecdd9e"></a><a name="adfdb30bb368147e4a35e2bdaedecdd9e"></a><strong id="aad15b6e7b2034cc18fae7a7805319bad"><a name="aad15b6e7b2034cc18fae7a7805319bad"></a><a name="aad15b6e7b2034cc18fae7a7805319bad"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="aeb76601616c84166a9d74d4688452238"><a name="aeb76601616c84166a9d74d4688452238"></a><a name="aeb76601616c84166a9d74d4688452238"></a><strong id="a66dd1499034e4d9887bfb95a21c3f30e"><a name="a66dd1499034e4d9887bfb95a21c3f30e"></a><a name="a66dd1499034e4d9887bfb95a21c3f30e"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rc14dd32926c440feaf39d1ecb3221901"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a3ab52f9eeec84138ae4a75b7a1b432c5"><a name="a3ab52f9eeec84138ae4a75b7a1b432c5"></a><a name="a3ab52f9eeec84138ae4a75b7a1b432c5"></a>channel</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aec25b206781b4f9ba0fb07350edeafd5"><a name="aec25b206781b4f9ba0fb07350edeafd5"></a><a name="aec25b206781b4f9ba0fb07350edeafd5"></a><strong id="af551177094a94253aa2840a7d7050cc1"><a name="af551177094a94253aa2840a7d7050cc1"></a><a name="af551177094a94253aa2840a7d7050cc1"></a>-</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac301bef94fee4e7a9d9bd3059dfdd480"><a name="ac301bef94fee4e7a9d9bd3059dfdd480"></a><a name="ac301bef94fee4e7a9d9bd3059dfdd480"></a>Channel connected to the sink.</p>
    </td>
    </tr>
    <tr id="rf36436b61f064b9193aaea32319dbff4"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="afced5f20d548413980e55220feb76373"><a name="afced5f20d548413980e55220feb76373"></a><a name="afced5f20d548413980e55220feb76373"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a2dc9e8b532804a35ab8796f8d8f4b627"><a name="a2dc9e8b532804a35ab8796f8d8f4b627"></a><a name="a2dc9e8b532804a35ab8796f8d8f4b627"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8511e648a25a411ebf88469862cc4b8e"><a name="a8511e648a25a411ebf88469862cc4b8e"></a><a name="a8511e648a25a411ebf88469862cc4b8e"></a>Type, which is set to <span class="parmvalue" id="p49e03f152dc04d56ad53e8c10914d5f5"><a name="p49e03f152dc04d56ad53e8c10914d5f5"></a><a name="p49e03f152dc04d56ad53e8c10914d5f5"></a><b>org.apache.flume.sink.kafka.KafkaSink</b></span>.</p>
    </td>
    </tr>
    <tr id="rc040894a5bdb4d3b878256e07b6952de"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="afac59cec7811439cb2f917ebf6603b12"><a name="afac59cec7811439cb2f917ebf6603b12"></a><a name="afac59cec7811439cb2f917ebf6603b12"></a>kafka.bootstrap.servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a21a76f0d18dd4039873763576cff171b"><a name="a21a76f0d18dd4039873763576cff171b"></a><a name="a21a76f0d18dd4039873763576cff171b"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab8657a8fd89240e6b39bf45f4f5ed6e8"><a name="ab8657a8fd89240e6b39bf45f4f5ed6e8"></a><a name="ab8657a8fd89240e6b39bf45f4f5ed6e8"></a>List of Kafka Brokers, which are separated by commas.</p>
    </td>
    </tr>
    <tr id="r9e15adce0b2c4a168fa9ae29bc35f891"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ad107e61ce69440168eaf6f8cbc34d4e1"><a name="ad107e61ce69440168eaf6f8cbc34d4e1"></a><a name="ad107e61ce69440168eaf6f8cbc34d4e1"></a>monTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a9bbbc7adab2c4df98124b9eda53f8e31"><a name="a9bbbc7adab2c4df98124b9eda53f8e31"></a><a name="a9bbbc7adab2c4df98124b9eda53f8e31"></a>0 (disabled)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a6366348b55284b79857fb10aedae1220"><a name="a6366348b55284b79857fb10aedae1220"></a><a name="a6366348b55284b79857fb10aedae1220"></a>Thread monitoring threshold. When the update time (seconds) exceeds the threshold, the sink is restarted.</p>
    </td>
    </tr>
    <tr id="r1f17997c18be4faa9c4b60e7e32e5ad8"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ab5690a246ab8483784903cf27b8bfbce"><a name="ab5690a246ab8483784903cf27b8bfbce"></a><a name="ab5690a246ab8483784903cf27b8bfbce"></a>kafka.topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a5a7243c4d9bf43e9a3f31c6ea1f9b3a0"><a name="a5a7243c4d9bf43e9a3f31c6ea1f9b3a0"></a><a name="a5a7243c4d9bf43e9a3f31c6ea1f9b3a0"></a>default-flume-topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac5dd547438a0456aa4348244db34f51a"><a name="ac5dd547438a0456aa4348244db34f51a"></a><a name="ac5dd547438a0456aa4348244db34f51a"></a>Topic where data is written.</p>
    </td>
    </tr>
    <tr id="r554a86e821f843eda00868378c4fc243"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="adbb1394c2244499daed88dafdc0b722f"><a name="adbb1394c2244499daed88dafdc0b722f"></a><a name="adbb1394c2244499daed88dafdc0b722f"></a>flumeBatchSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a3e6ad61fcb2742b9a5e6eefd9bb9ae7d"><a name="a3e6ad61fcb2742b9a5e6eefd9bb9ae7d"></a><a name="a3e6ad61fcb2742b9a5e6eefd9bb9ae7d"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p740582917533"><a name="en-us_topic_0066459131_p740582917533"></a><a name="en-us_topic_0066459131_p740582917533"></a>Number of events written into Kafka at a time.</p>
    </td>
    </tr>
    <tr id="r68390ac8d4fc4147b4bc01a350402c05"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aa808f1a5a33c418e8e82fb5977902fd0"><a name="aa808f1a5a33c418e8e82fb5977902fd0"></a><a name="aa808f1a5a33c418e8e82fb5977902fd0"></a>kafka.security.protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a832f1229bb6d4a9d924ce21618f3b7ba"><a name="a832f1229bb6d4a9d924ce21618f3b7ba"></a><a name="a832f1229bb6d4a9d924ce21618f3b7ba"></a>SASL_PLAINTEXT</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ace49cf4a0c614b84bf61e3edaaad14fd"><a name="ace49cf4a0c614b84bf61e3edaaad14fd"></a><a name="ace49cf4a0c614b84bf61e3edaaad14fd"></a>Security protocol of Kafka. The value must be set to <span class="parmvalue" id="p753077cd458f47cd9b2e797e7a605549"><a name="p753077cd458f47cd9b2e797e7a605549"></a><a name="p753077cd458f47cd9b2e797e7a605549"></a><b>PLAINTEXT</b></span> for clusters in which Kerberos authentication is disabled.</p>
    </td>
    </tr>
    <tr id="rd7c7fa7b258849e69bdd3ce37174323d"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a1519dada1ab84a919f272586a57329f7"><a name="a1519dada1ab84a919f272586a57329f7"></a><a name="a1519dada1ab84a919f272586a57329f7"></a>Other Kafka Producer Properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p897233717533"><a name="en-us_topic_0066459131_p897233717533"></a><a name="en-us_topic_0066459131_p897233717533"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a4b430b99a54f4adf9ac200fb76f41536"><a name="a4b430b99a54f4adf9ac200fb76f41536"></a><a name="a4b430b99a54f4adf9ac200fb76f41536"></a>Other Kafka configurations. This parameter can be set to any production configuration supported by Kafka, and the <span class="parmvalue" id="p1e181022603043c282d96ac81505622c"><a name="p1e181022603043c282d96ac81505622c"></a><a name="p1e181022603043c282d96ac81505622c"></a><b>.kafka</b></span> prefix must be added to the configuration.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **OBS Sink**

    An OBS sink writes data into OBS. As OBS sink and HDFS sink use the same file system interface, their parameter configurations are similar.  [The following table](#t2836629ddb72475d8630a3536e437e44)  provides common configurations of an OBS sink:

    **Table  15**  Common configurations of an OBS sink

    <a name="t2836629ddb72475d8630a3536e437e44"></a>
    <table><thead align="left"><tr id="r7a2b9ba49f4e408594f5830d2f2969aa"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="aaa93c4906128499ca56d8bf1bc4c2afa"><a name="aaa93c4906128499ca56d8bf1bc4c2afa"></a><a name="aaa93c4906128499ca56d8bf1bc4c2afa"></a><strong id="af79e924632134feeac0504a5ab312dc3"><a name="af79e924632134feeac0504a5ab312dc3"></a><a name="af79e924632134feeac0504a5ab312dc3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="a4c2fe163e15543c5a73b9570a8e0ff54"><a name="a4c2fe163e15543c5a73b9570a8e0ff54"></a><a name="a4c2fe163e15543c5a73b9570a8e0ff54"></a><strong id="aafddbc80d1ca4e1c99c1e4ea2f5fdc0c"><a name="aafddbc80d1ca4e1c99c1e4ea2f5fdc0c"></a><a name="aafddbc80d1ca4e1c99c1e4ea2f5fdc0c"></a>Default Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a38f5ea84e8ec4ec48dac82b82fbcd6bb"><a name="a38f5ea84e8ec4ec48dac82b82fbcd6bb"></a><a name="a38f5ea84e8ec4ec48dac82b82fbcd6bb"></a><strong id="ab6e086a4b93b4b36be7f587b37898e6b"><a name="ab6e086a4b93b4b36be7f587b37898e6b"></a><a name="ab6e086a4b93b4b36be7f587b37898e6b"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r07b4bf13401c45208c3babb86eac1ee2"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ad3b978d5ad834ec381921d1c865f0ba8"><a name="ad3b978d5ad834ec381921d1c865f0ba8"></a><a name="ad3b978d5ad834ec381921d1c865f0ba8"></a>channel</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a67d7320acccc4b368f11c9b86109c76b"><a name="a67d7320acccc4b368f11c9b86109c76b"></a><a name="a67d7320acccc4b368f11c9b86109c76b"></a><strong id="af6ff9f9c62bf408390d23f003a16ac06"><a name="af6ff9f9c62bf408390d23f003a16ac06"></a><a name="af6ff9f9c62bf408390d23f003a16ac06"></a>-</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad5d0a96251034d269c6dd61ec4cefccb"><a name="ad5d0a96251034d269c6dd61ec4cefccb"></a><a name="ad5d0a96251034d269c6dd61ec4cefccb"></a>Channel connected to the sink.</p>
    </td>
    </tr>
    <tr id="r433d8a2e2f96400a98ecfbc5f04d8212"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="aee8f8109b632428bb4a8bb34d5057a2a"><a name="aee8f8109b632428bb4a8bb34d5057a2a"></a><a name="aee8f8109b632428bb4a8bb34d5057a2a"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ae88484639de440dab3f5c04aab74d4b1"><a name="ae88484639de440dab3f5c04aab74d4b1"></a><a name="ae88484639de440dab3f5c04aab74d4b1"></a>hdfs</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p93613717555"><a name="en-us_topic_0066459131_p93613717555"></a><a name="en-us_topic_0066459131_p93613717555"></a>Type, which is set to <span class="parmvalue" id="p15867cdd93bd467c8588f468ad64399c"><a name="p15867cdd93bd467c8588f468ad64399c"></a><a name="p15867cdd93bd467c8588f468ad64399c"></a><b>hdfs</b></span>.</p>
    </td>
    </tr>
    <tr id="r187b29736bd841779b8e7c7cac26110d"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a9e7bb1b46ab748f6bfc95c6edaacf761"><a name="a9e7bb1b46ab748f6bfc95c6edaacf761"></a><a name="a9e7bb1b46ab748f6bfc95c6edaacf761"></a>monTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a9b77e987071f454193ba16c46466b518"><a name="a9b77e987071f454193ba16c46466b518"></a><a name="a9b77e987071f454193ba16c46466b518"></a>0 (disabled)</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p449731017555"><a name="en-us_topic_0066459131_p449731017555"></a><a name="en-us_topic_0066459131_p449731017555"></a>Thread monitoring threshold. When the update time (seconds) exceeds the threshold, the sink is restarted.</p>
    </td>
    </tr>
    <tr id="r9e87097fb1c5412eb7965b3b7f46768b"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="afeb3f903a9804bd890fbb5637c7e91db"><a name="afeb3f903a9804bd890fbb5637c7e91db"></a><a name="afeb3f903a9804bd890fbb5637c7e91db"></a>hdfs.path</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a72a29f419885497aa7def4babb978732"><a name="a72a29f419885497aa7def4babb978732"></a><a name="a72a29f419885497aa7def4babb978732"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a8713fe3d723d4795900481f7bf4d7a3b"><a name="a8713fe3d723d4795900481f7bf4d7a3b"></a><a name="a8713fe3d723d4795900481f7bf4d7a3b"></a>OBS path in the <strong id="ada09e9b25da343d8bac765deee405b79"><a name="ada09e9b25da343d8bac765deee405b79"></a><a name="ada09e9b25da343d8bac765deee405b79"></a>s3a://AK:SK@</strong><em id="a8ade2e1500bb44b7af911c12a1a31d0f"><a name="a8ade2e1500bb44b7af911c12a1a31d0f"></a><a name="a8ade2e1500bb44b7af911c12a1a31d0f"></a>Bucket</em>/<em id="aa6a3259066844e84bdb87a5ce2e722db"><a name="aa6a3259066844e84bdb87a5ce2e722db"></a><a name="aa6a3259066844e84bdb87a5ce2e722db"></a>Path</em>/ format, for example, s3a://AK:SK@obs-nemon-sink/obs-sink/</p>
    </td>
    </tr>
    <tr id="rd1530abb7b754fe196d2408002796728"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a5c83d13066a64f96ae8f68c3d057bcf5"><a name="a5c83d13066a64f96ae8f68c3d057bcf5"></a><a name="a5c83d13066a64f96ae8f68c3d057bcf5"></a>hdfs.inUseSuffix</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aa17d1d98b8d2430db26f96dd77e13944"><a name="aa17d1d98b8d2430db26f96dd77e13944"></a><a name="aa17d1d98b8d2430db26f96dd77e13944"></a>.tmp</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2c76007dd9e14db7917a897b8ece417c"><a name="a2c76007dd9e14db7917a897b8ece417c"></a><a name="a2c76007dd9e14db7917a897b8ece417c"></a>Suffix of the OBS file being written.</p>
    </td>
    </tr>
    <tr id="r15bcb264a63d43a4bb53267646060d08"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ad73227d74ddc4855807863f796ec2334"><a name="ad73227d74ddc4855807863f796ec2334"></a><a name="ad73227d74ddc4855807863f796ec2334"></a>hdfs.rollInterval</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ac12502bb4ef541329fcac336040996f1"><a name="ac12502bb4ef541329fcac336040996f1"></a><a name="ac12502bb4ef541329fcac336040996f1"></a>30</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p648439817555"><a name="en-us_topic_0066459131_p648439817555"></a><a name="en-us_topic_0066459131_p648439817555"></a>Interval for file rolling. The unit is second.</p>
    </td>
    </tr>
    <tr id="r8ba3f7bc6d1d4b888774a96713c9ee78"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="ae26c8d9f61814f01881ad895d6a078b7"><a name="ae26c8d9f61814f01881ad895d6a078b7"></a><a name="ae26c8d9f61814f01881ad895d6a078b7"></a>hdfs.rollSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="aeea00da62ad446669a652e2bbf70dad7"><a name="aeea00da62ad446669a652e2bbf70dad7"></a><a name="aeea00da62ad446669a652e2bbf70dad7"></a>1024</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a4271710d53324c23b03f1efe803e7205"><a name="a4271710d53324c23b03f1efe803e7205"></a><a name="a4271710d53324c23b03f1efe803e7205"></a>Size for file rolling. The unit is byte.</p>
    </td>
    </tr>
    <tr id="rb828ec512852445596fbb1fd4c94c176"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0066459131_p811401217555"><a name="en-us_topic_0066459131_p811401217555"></a><a name="en-us_topic_0066459131_p811401217555"></a>hdfs.rollCount</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a1d1621335856425790c068a16726efbb"><a name="a1d1621335856425790c068a16726efbb"></a><a name="a1d1621335856425790c068a16726efbb"></a>10</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="afbb69264a0004fa090a282621eaa4c78"><a name="afbb69264a0004fa090a282621eaa4c78"></a><a name="afbb69264a0004fa090a282621eaa4c78"></a>Number of events for file rolling.</p>
    </td>
    </tr>
    <tr id="r30b259228ee14f16b67059056459eb85"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a09f3479dd4e24d2da07b37713037594e"><a name="a09f3479dd4e24d2da07b37713037594e"></a><a name="a09f3479dd4e24d2da07b37713037594e"></a>hdfs.idleTimeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a16ccef650d9349f19d38a24b219bda16"><a name="a16ccef650d9349f19d38a24b219bda16"></a><a name="a16ccef650d9349f19d38a24b219bda16"></a>0</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a6e077fcea2484568af9975c8b6e9a205"><a name="a6e077fcea2484568af9975c8b6e9a205"></a><a name="a6e077fcea2484568af9975c8b6e9a205"></a>Timeout interval for closing idle files automatically. The unit is second.</p>
    </td>
    </tr>
    <tr id="rf2ead44f469f47dab4e066c61f98c8bd"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a390ef023c6154782910a45d8a7cdaa6d"><a name="a390ef023c6154782910a45d8a7cdaa6d"></a><a name="a390ef023c6154782910a45d8a7cdaa6d"></a>hdfs.batchSize</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ab73e60cc7e25452ea3dfbb32f76a4b0d"><a name="ab73e60cc7e25452ea3dfbb32f76a4b0d"></a><a name="ab73e60cc7e25452ea3dfbb32f76a4b0d"></a>1000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p584776417555"><a name="en-us_topic_0066459131_p584776417555"></a><a name="en-us_topic_0066459131_p584776417555"></a>Number of events written into OBS at a time.</p>
    </td>
    </tr>
    <tr id="rdc6f1b8cd63b4b4eae56fa04a0146b74"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a1cc2c1d396eb440989f081328af3cee1"><a name="a1cc2c1d396eb440989f081328af3cee1"></a><a name="a1cc2c1d396eb440989f081328af3cee1"></a>hdfs.calltimeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ad89e5e18223e444593e7dc79fec912dc"><a name="ad89e5e18223e444593e7dc79fec912dc"></a><a name="ad89e5e18223e444593e7dc79fec912dc"></a>10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="afc55eaeeb79e438f9575f537cb33bdc4"><a name="afc55eaeeb79e438f9575f537cb33bdc4"></a><a name="afc55eaeeb79e438f9575f537cb33bdc4"></a>Timeout interval for interaction with OBS. The unit is millisecond. The timeout interval must be as maximum as possible, for example, 1000000, because files are copied when some operations (such as OBS renaming) are performed, which requires a long time.</p>
    </td>
    </tr>
    <tr id="r814a557d5bac4bc8b86773d34fd43392"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a4df8816df82f4d94aff286e96f863572"><a name="a4df8816df82f4d94aff286e96f863572"></a><a name="a4df8816df82f4d94aff286e96f863572"></a>hdfs.fileCloseByEndEvent</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0066459131_p262275217555"><a name="en-us_topic_0066459131_p262275217555"></a><a name="en-us_topic_0066459131_p262275217555"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a1b398b09a6b243bfa42ffb195a07407f"><a name="a1b398b09a6b243bfa42ffb195a07407f"></a><a name="a1b398b09a6b243bfa42ffb195a07407f"></a>Indicates whether the file is closed when the last event is received.</p>
    </td>
    </tr>
    <tr id="r0ec27c9c001049b9a08f965e7baa75af"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="acedd8bfda389488daa03880ef30960fd"><a name="acedd8bfda389488daa03880ef30960fd"></a><a name="acedd8bfda389488daa03880ef30960fd"></a>hdfs.batchCallTimeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="a098bdc37484f43e197b30b2c2424a623"><a name="a098bdc37484f43e197b30b2c2424a623"></a><a name="a098bdc37484f43e197b30b2c2424a623"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a24913c996ba04e109a2594a8e34a3ad5"><a name="a24913c996ba04e109a2594a8e34a3ad5"></a><a name="a24913c996ba04e109a2594a8e34a3ad5"></a>Timeout control duration (milliseconds) each time events are written into OBS.</p>
    <p id="aa62f67f136bb4346a00c2085a6739b56"><a name="aa62f67f136bb4346a00c2085a6739b56"></a><a name="aa62f67f136bb4346a00c2085a6739b56"></a>If this parameter is not specified, the timeout duration is controlled when each event is written into OBS. When the value of <strong id="adfacf7f6556a45ee949fc188ed46a332"><a name="adfacf7f6556a45ee949fc188ed46a332"></a><a name="adfacf7f6556a45ee949fc188ed46a332"></a>hdfs.batchSize</strong> is greater than 0, configure this parameter to improve the performance of writing data into OBS.</p>
    <div class="note" id="nc2f971b6823a42e1a9bd598d318d089a"><a name="nc2f971b6823a42e1a9bd598d318d089a"></a><a name="nc2f971b6823a42e1a9bd598d318d089a"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0066459131_p104881183711"><a name="en-us_topic_0066459131_p104881183711"></a><a name="en-us_topic_0066459131_p104881183711"></a>The value of <span class="parmname" id="pbb1c5ed0395042538c04a3e5056e7e41"><a name="pbb1c5ed0395042538c04a3e5056e7e41"></a><a name="pbb1c5ed0395042538c04a3e5056e7e41"></a><b>hdfs.batchCallTimeout</b></span>&nbsp;depends on&nbsp;<span class="parmname" id="p33f56dd1459e49e89175efa1dfeb0394"><a name="p33f56dd1459e49e89175efa1dfeb0394"></a><a name="p33f56dd1459e49e89175efa1dfeb0394"></a><b>hdfs.batchSize</b></span>. A greater&nbsp;<span class="parmname" id="pc280929c997c454a96040d06b8c51fd0"><a name="pc280929c997c454a96040d06b8c51fd0"></a><a name="pc280929c997c454a96040d06b8c51fd0"></a><b>hdfs.batchSize</b></span>&nbsp;requires a larger&nbsp;<span class="parmname" id="pb9e4d6b6ac2047f6a3d4458f887afdd6"><a name="pb9e4d6b6ac2047f6a3d4458f887afdd6"></a><a name="pb9e4d6b6ac2047f6a3d4458f887afdd6"></a><b>hdfs.batchCallTimeout</b></span>. If the value of&nbsp;<span class="parmname" id="p68c6e390173248a29ae103b82a973843"><a name="p68c6e390173248a29ae103b82a973843"></a><a name="p68c6e390173248a29ae103b82a973843"></a><b>hdfs.batchCallTimeout</b></span> is too small, writing events to OBS may fail.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r74faa233a8ee4381a8a23c2902a7db42"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="a459a89f21e7245dba2d8cdf4b29af7f3"><a name="a459a89f21e7245dba2d8cdf4b29af7f3"></a><a name="a459a89f21e7245dba2d8cdf4b29af7f3"></a>serializer.appendNewline</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="ad95818b1f8d4419a89dc181a9a26c058"><a name="ad95818b1f8d4419a89dc181a9a26c058"></a><a name="ad95818b1f8d4419a89dc181a9a26c058"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0066459131_p460195010383"><a name="en-us_topic_0066459131_p460195010383"></a><a name="en-us_topic_0066459131_p460195010383"></a>Indicates whether to add a line feed character (<strong id="en-us_topic_0066459131_b14602503383"><a name="en-us_topic_0066459131_b14602503383"></a><a name="en-us_topic_0066459131_b14602503383"></a>\n</strong>) after an event is written to OBS. If a line feed character is added, the data volume counters used by the line feed character will not be calculated by OBS sinks.</p>
    </td>
    </tr>
    </tbody>
    </table>


