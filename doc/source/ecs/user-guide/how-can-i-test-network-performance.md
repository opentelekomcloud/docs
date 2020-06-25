# How Can I Test Network Performance?<a name="EN-US_TOPIC_0115820205"></a>

This section describes how to use netperf and iperf3 to test network performance between ECSs. The operations include test preparations, TCP bandwidth test, UDP PPS test, and latency test.

## Background<a name="section1048194415433"></a>

-   Tested ECS: an ECS that is tested for network performance. Such an ECS functions as the client \(TX end\) or server \(RX end\) in netperf tests.
-   Auxiliary ECS: an ECS that is used to exchange test data with the tested ECS. The auxiliary ECS functions as the client \(TX end\) or server \(RX end\) in netperf tests.
-   [Table 1](#table15359114885218)  and  [Table 2](#table8470126153613)  list common test tool parameters.

    **Table  1**  Common netperf parameters

    <a name="table15359114885218"></a>
    <table><thead align="left"><tr id="row2036064865210"><th class="cellrowborder" valign="top" width="18.14%" id="mcps1.2.3.1.1"><p id="p153601148175218"><a name="p153601148175218"></a><a name="p153601148175218"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="81.86%" id="mcps1.2.3.1.2"><p id="p33601248105212"><a name="p33601248105212"></a><a name="p33601248105212"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row183601048155212"><td class="cellrowborder" valign="top" width="18.14%" headers="mcps1.2.3.1.1 "><p id="p2360848175217"><a name="p2360848175217"></a><a name="p2360848175217"></a>-p</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.86%" headers="mcps1.2.3.1.2 "><p id="p123601148205212"><a name="p123601148205212"></a><a name="p123601148205212"></a>Port number</p>
    </td>
    </tr>
    <tr id="row13360104815211"><td class="cellrowborder" valign="top" width="18.14%" headers="mcps1.2.3.1.1 "><p id="p1836084825211"><a name="p1836084825211"></a><a name="p1836084825211"></a>-H</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.86%" headers="mcps1.2.3.1.2 "><p id="p9360154875212"><a name="p9360154875212"></a><a name="p9360154875212"></a>IP address of the RX end</p>
    </td>
    </tr>
    <tr id="row736054815213"><td class="cellrowborder" valign="top" width="18.14%" headers="mcps1.2.3.1.1 "><p id="p13360164825212"><a name="p13360164825212"></a><a name="p13360164825212"></a>-t</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.86%" headers="mcps1.2.3.1.2 "><p id="p236094835210"><a name="p236094835210"></a><a name="p236094835210"></a>Protocol used in packet transmitting, the value of which is <strong id="b842352706155518"><a name="b842352706155518"></a><a name="b842352706155518"></a>TCP_STREAM</strong> in bandwidth tests</p>
    </td>
    </tr>
    <tr id="row636015481528"><td class="cellrowborder" valign="top" width="18.14%" headers="mcps1.2.3.1.1 "><p id="p736034875216"><a name="p736034875216"></a><a name="p736034875216"></a>-l</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.86%" headers="mcps1.2.3.1.2 "><p id="p14360164812524"><a name="p14360164812524"></a><a name="p14360164812524"></a>Test duration</p>
    </td>
    </tr>
    <tr id="row1875191425312"><td class="cellrowborder" valign="top" width="18.14%" headers="mcps1.2.3.1.1 "><p id="p1375121465318"><a name="p1375121465318"></a><a name="p1375121465318"></a>-m</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.86%" headers="mcps1.2.3.1.2 "><p id="p9753141435319"><a name="p9753141435319"></a><a name="p9753141435319"></a>Data packet size, which is suggested to be <strong id="b842352706155714"><a name="b842352706155714"></a><a name="b842352706155714"></a>1440</strong> in bandwidth tests</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Common iperf3 parameters

    <a name="table8470126153613"></a>
    <table><thead align="left"><tr id="row154721968360"><th class="cellrowborder" valign="top" width="18.39%" id="mcps1.2.3.1.1"><p id="p147213619362"><a name="p147213619362"></a><a name="p147213619362"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="81.61%" id="mcps1.2.3.1.2"><p id="p13473126183616"><a name="p13473126183616"></a><a name="p13473126183616"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1747386153610"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.2.3.1.1 "><p id="p1147356173617"><a name="p1147356173617"></a><a name="p1147356173617"></a>-p</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.61%" headers="mcps1.2.3.1.2 "><p id="p212175218378"><a name="p212175218378"></a><a name="p212175218378"></a>Port number</p>
    </td>
    </tr>
    <tr id="row164731663365"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.2.3.1.1 "><p id="p1473176153615"><a name="p1473176153615"></a><a name="p1473176153615"></a>-c</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.61%" headers="mcps1.2.3.1.2 "><p id="p418155263716"><a name="p418155263716"></a><a name="p418155263716"></a>IP address of the RX end</p>
    </td>
    </tr>
    <tr id="row4473664362"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.2.3.1.1 "><p id="p1447318613617"><a name="p1447318613617"></a><a name="p1447318613617"></a>-u</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.61%" headers="mcps1.2.3.1.2 "><p id="p8473196193613"><a name="p8473196193613"></a><a name="p8473196193613"></a>UDP packets</p>
    </td>
    </tr>
    <tr id="row84736643618"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.2.3.1.1 "><p id="p1347316643618"><a name="p1347316643618"></a><a name="p1347316643618"></a>-b</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.61%" headers="mcps1.2.3.1.2 "><p id="p3473196193620"><a name="p3473196193620"></a><a name="p3473196193620"></a>TX bandwidth</p>
    </td>
    </tr>
    <tr id="row9473761366"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.2.3.1.1 "><p id="p4473156133619"><a name="p4473156133619"></a><a name="p4473156133619"></a>-t</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.61%" headers="mcps1.2.3.1.2 "><p id="p547317619362"><a name="p547317619362"></a><a name="p547317619362"></a>Test duration</p>
    </td>
    </tr>
    <tr id="row1047315610362"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.2.3.1.1 "><p id="p947312663614"><a name="p947312663614"></a><a name="p947312663614"></a>-l</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.61%" headers="mcps1.2.3.1.2 "><p id="p2473166193611"><a name="p2473166193611"></a><a name="p2473166193611"></a>Data packet size, which is suggested to be <strong id="b1455495502"><a name="b1455495502"></a><a name="b1455495502"></a>16</strong> in PPS tests</p>
    </td>
    </tr>
    <tr id="row1347356173619"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.2.3.1.1 "><p id="p174738613611"><a name="p174738613611"></a><a name="p174738613611"></a>-A</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.61%" headers="mcps1.2.3.1.2 "><p id="p1221192163911"><a name="p1221192163911"></a><a name="p1221192163911"></a>ID of the vCPU used by iperf3</p>
    <p id="p134738683619"><a name="p134738683619"></a><a name="p134738683619"></a>In this section, the maximum number of 16 vCPUs is used as an example for each ECS. If an ECS has 8 vCPUs, the <strong id="b84235270616535"><a name="b84235270616535"></a><a name="b84235270616535"></a>-A</strong> value ranges from 0 to 7.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Test Preparations<a name="section13811327193718"></a>

1.  Prepare ECSs.

    Ensure that both type and specifications of the tested ECS and auxiliary ECSs are the same. In addition, these ECSs are deployed in the same ECS group with anti-affinity enabled.

    **Table  3**  Preparations

    <a name="table9726120145710"></a>
    <table><thead align="left"><tr id="row18725202574"><th class="cellrowborder" valign="top" width="16.12%" id="mcps1.2.6.1.1"><p id="p127251109578"><a name="p127251109578"></a><a name="p127251109578"></a>Category</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.010000000000002%" id="mcps1.2.6.1.2"><p id="p1472515065713"><a name="p1472515065713"></a><a name="p1472515065713"></a>Quantity</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.31%" id="mcps1.2.6.1.3"><p id="p572540105720"><a name="p572540105720"></a><a name="p572540105720"></a>Image</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.560000000000002%" id="mcps1.2.6.1.4"><p id="p272510016574"><a name="p272510016574"></a><a name="p272510016574"></a>Specifications</p>
    </th>
    <th class="cellrowborder" valign="top" width="23%" id="mcps1.2.6.1.5"><p id="p97254095710"><a name="p97254095710"></a><a name="p97254095710"></a>IP Address</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27261503576"><td class="cellrowborder" valign="top" width="16.12%" headers="mcps1.2.6.1.1 "><p id="p1572500135711"><a name="p1572500135711"></a><a name="p1572500135711"></a>Tested ECS</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.010000000000002%" headers="mcps1.2.6.1.2 "><p id="p137265085717"><a name="p137265085717"></a><a name="p137265085717"></a>1</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.31%" headers="mcps1.2.6.1.3 "><p id="p1872650125710"><a name="p1872650125710"></a><a name="p1872650125710"></a>CentOS 7.4 64bit (recommended)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.6.1.4 "><p id="p177261004576"><a name="p177261004576"></a><a name="p177261004576"></a>At least eight vCPUs</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.5 "><p id="p1372650165714"><a name="p1372650165714"></a><a name="p1372650165714"></a>192.168.2.10</p>
    </td>
    </tr>
    <tr id="row17268011576"><td class="cellrowborder" valign="top" width="16.12%" headers="mcps1.2.6.1.1 "><p id="p1172680105719"><a name="p1172680105719"></a><a name="p1172680105719"></a>Auxiliary ECS</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.010000000000002%" headers="mcps1.2.6.1.2 "><p id="p672618095711"><a name="p672618095711"></a><a name="p672618095711"></a>8</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.31%" headers="mcps1.2.6.1.3 "><p id="p177269018573"><a name="p177269018573"></a><a name="p177269018573"></a>CentOS 7.4 64bit (recommended)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.560000000000002%" headers="mcps1.2.6.1.4 "><p id="p137266018574"><a name="p137266018574"></a><a name="p137266018574"></a>At least 8 vCPUs</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.6.1.5 "><p id="p57261801575"><a name="p57261801575"></a><a name="p57261801575"></a>192.168.2.11-192.168.2.18</p>
    </td>
    </tr>
    </tbody>
    </table>

2.  Install the netperf, iperf3, and sar test tools on both the tested ECS and auxiliary ECSs.

    [Table 4](#table231811914413)  lists the procedures for installing these tools.

    **Table  4**  Installing test tools

    <a name="table231811914413"></a>
    <table><thead align="left"><tr id="row732015191241"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.3.1.1"><p id="p133201119647"><a name="p133201119647"></a><a name="p133201119647"></a>Tool</p>
    </th>
    <th class="cellrowborder" valign="top" width="83%" id="mcps1.2.3.1.2"><p id="p17320181911417"><a name="p17320181911417"></a><a name="p17320181911417"></a>Procedure</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row03201819248"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p1674643217411"><a name="p1674643217411"></a><a name="p1674643217411"></a>netperf</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><a name="ol179221601358"></a><a name="ol179221601358"></a><ol id="ol179221601358"><li>Run the following command to install gcc:<p id="p185131568615"><a name="p185131568615"></a><a name="p185131568615"></a><strong id="b163651219616"><a name="b163651219616"></a><a name="b163651219616"></a>yum -y install unzip gcc gcc-c++</strong></p>
    </li><li>Run the following command to download the netperf installation package:<p id="p1613015241619"><a name="p1613015241619"></a><a name="p1613015241619"></a><strong id="b1411816291865"><a name="b1411816291865"></a><a name="b1411816291865"></a>wget --no-check-certificate https://github.com/HewlettPackard/netperf/archive/netperf-2.7.0.zip -O netperf-2.7.0.zip</strong></p>
    </li><li>Run the following commands to decompress the installation package and install netperf:<p id="p1989594715610"><a name="p1989594715610"></a><a name="p1989594715610"></a><strong id="b0796653662"><a name="b0796653662"></a><a name="b0796653662"></a>unzip netperf-2.7.0.zip</strong></p>
    <p id="p1260914421766"><a name="p1260914421766"></a><a name="p1260914421766"></a><strong id="b14798155317611"><a name="b14798155317611"></a><a name="b14798155317611"></a>cd netperf-netperf-2.7.0/</strong></p>
    <p id="p4609184216619"><a name="p4609184216619"></a><a name="p4609184216619"></a><strong id="b207992531869"><a name="b207992531869"></a><a name="b207992531869"></a>./configure &amp;&amp; make &amp;&amp; make install</strong></p>
    </li></ol>
    </td>
    </tr>
    <tr id="row93208191642"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p632019195413"><a name="p632019195413"></a><a name="p632019195413"></a>iperf3</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><a name="ol181051231175"></a><a name="ol181051231175"></a><ol id="ol181051231175"><li>Run the following command to download the iperf3 installation package:<p id="p209001815880"><a name="p209001815880"></a><a name="p209001815880"></a><strong id="b18800181916817"><a name="b18800181916817"></a><a name="b18800181916817"></a>wget --no-check-certificate https://codeload.github.com/esnet/iperf/zip/master -O iperf3.zip</strong></p>
    </li><li>Run the following commands to decompress the installation package and install iperf3:<p id="p71408341481"><a name="p71408341481"></a><a name="p71408341481"></a><strong id="b785311391086"><a name="b785311391086"></a><a name="b785311391086"></a>unzip iperf3.zip</strong></p>
    <p id="p2531228387"><a name="p2531228387"></a><a name="p2531228387"></a><strong id="b08551239184"><a name="b08551239184"></a><a name="b08551239184"></a>cd iperf-master/</strong></p>
    <p id="p165313281088"><a name="p165313281088"></a><a name="p165313281088"></a><strong id="b1985615394815"><a name="b1985615394815"></a><a name="b1985615394815"></a>./configure &amp;&amp; make &amp;&amp; make install</strong></p>
    </li></ol>
    </td>
    </tr>
    <tr id="row183204191410"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p1832018191043"><a name="p1832018191043"></a><a name="p1832018191043"></a>sar</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p7770111616915"><a name="p7770111616915"></a><a name="p7770111616915"></a>Run the following command to install sar:</p>
    <p id="p1332013191649"><a name="p1332013191649"></a><a name="p1332013191649"></a><strong id="b1661120201294"><a name="b1661120201294"></a><a name="b1661120201294"></a>yum -y install sysstat</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Enable NIC multi-queue.

    Perform the following operations on both tested ECS and auxiliary ECSs.

    1.  <a name="li162918018139"></a>Run the following command to check the number of queues supported by the ECSs:

        **ethtool -l eth0 | grep -i Pre -A 5 | grep Combined**

    2.  Run the following command to enable NIC multi-queue:

        **ethtool -L eth0 combined** **_X_**

        In the preceding command,  _X_  is the number of queues obtained in  [3.a](#li162918018139).



## TCP Bandwidth Test \(Using netperf\)<a name="section877203363715"></a>

Perform the test on multiple flows. This section uses 16 flows as an example, which are evenly distributed to eight ECSs.

1.  Test the TCP TX bandwidth.
    1.  Run the following commands on all auxiliary ECSs to start the netserver process:

        **netserver -p** **_12001_**

        **netserver -p** **_12002_**

        In the preceding commands,  **-p**  specifies the listening port.

    2.  Start the netperf process on the tested ECS and specify a netserver port for each auxiliary ECS. For details about common netperf parameters, see  [Table 1](#table15359114885218).

        \#\#The IP address is for the first auxiliary ECS.

        **netperf -H** **192.168.2.11** **-p** **12001 -t TCP\_STREAM -l** **300 -- -m** **1440 &**

        **netperf -H** **192.168.2.11** **-p** **12002 -t TCP\_STREAM -l** **300 -- -m** ****1440 **&**

        \#\#The IP address is for the second auxiliary ECS.

        **netperf -H** **192.168.2.12** **-p** **12001 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        **netperf -H** **192.168.2.12** **-p** **12002 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        \#\#The IP address is for the third auxiliary ECS.

        **netperf -H** **192.168.2.13 -p** **12001 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        **netperf -H** **192.168.2.13 -p** **12002 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        \#\#The IP address is for the fourth auxiliary ECS.

        **netperf -H** **192.168.2.14 -p** **12001 -t TCP\_STREAM -l** ****300**  -- -m  ****1440****  &**

        **netperf -H** **192.168.2.14 -p** **12002 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        \#\#The IP address is for the fifth auxiliary ECS.

        **netperf -H** **192.168.2.15 -p** **12001 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        **netperf -H** **192.168.2.15 -p** **12002 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        \#\#The IP address is for the sixth auxiliary ECS.

        **netperf -H** **192.168.2.16 -p** **12001 -t TCP\_STREAM -l  **300**  -- -m** ******1440****  &**

        **netperf -H** **192.168.2.16 -p** **12002 -t TCP\_STREAM -l  **300**  -- -m** ******1440****  &**

        \#\#The IP address is for the seventh auxiliary ECS.

        **netperf -H** **192.168.2.17 -p** **12001 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        **netperf -H** **192.168.2.17 -p** **12002 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        \#\#The IP address is for the eighth auxiliary ECS.

        **netperf -H** **192.168.2.18 -p** **12001 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

        **netperf -H** **192.168.2.18 -p** **12002 -t TCP\_STREAM -l** ****300**  -- -m** ******1440****  &**

2.  Test the TCP RX bandwidth.
    1.  Start the netserver process on the tested ECS.

        \#\#The port number is for the first auxiliary ECS.

        **netserver -p** **12001**

        **netserver -p** **12002**

        \#\#The port number is for the second auxiliary ECS.

        **netserver -p** **12003**

        **netserver -p** **12004**

        \#\#The port number is for the third auxiliary ECS.

        **netserver -p** **12005**

        **netserver -p** **12006**

        \#\#The port number is for the fourth auxiliary ECS.

        **netserver -p** **12007**

        **netserver -p** **12008**

        \#\#The port number is for the fifth auxiliary ECS.

        **netserver -p 12009**

        **netserver -p 12010**

        \#\#The port number is for the sixth auxiliary ECS.

        **netserver -p** **12011**

        **netserver -p** **12012**

        \#\#The port number is for the seventh auxiliary ECS.

        **netserver -p** **12013**

        **netserver -p** **12014**

        \#\#The port number is for the eighth auxiliary ECS.

        **netserver -p** **12015**

        **netserver -p** **12016**

    2.  Start the netperf process on all auxiliary ECSs.

        Log in to auxiliary ECS 1.

        **netperf -H 192.168.2.10 -p 12001 -t TCP\_STREAM -l 300 -- -m 1440 &**

        **netperf -H 192.168.2.10 -p 12002 -t TCP\_STREAM -l 300 -- -m 1440 &**

        Log in to auxiliary ECS 2.

        **netperf -H 192.168.2.10 -p 12003 -t TCP\_STREAM -l 300 -- -m 1440 &**

        **netperf -H 192.168.2.10 -p 12004 -t TCP\_STREAM -l 300 -- -m 1440 &**

        Log in to auxiliary ECS 3.

        **netperf -H 192.168.2.10 -p 12005 -t TCP\_STREAM -l 300 -- -m 1440 &**

        **netperf -H 192.168.2.10 -p 12006 -t TCP\_STREAM -l 300 -- -m 1440 &**

        Log in to auxiliary ECS 4.

        **netperf -H 192.168.2.10 -p 12007 -t TCP\_STREAM -l 300 -- -m 1440 &**

        **netperf -H 192.168.2.10 -p 12008 -t TCP\_STREAM -l 300 -- -m 1440 &**

        Log in to auxiliary ECS 5.

        **netperf -H 192.168.2.10 -p 12009 -t TCP\_STREAM -l 300 -- -m 1440 &**

        **netperf -H 192.168.2.10 -p 12010 -t TCP\_STREAM -l 300 -- -m 1440 &**

        Log in to auxiliary ECS 6.

        **netperf -H 192.168.2.10 -p 12011 -t TCP\_STREAM -l 300 -- -m 1440 &**

        **netperf -H 192.168.2.10 -p 12012 -t TCP\_STREAM -l 300 -- -m 1440 &**

        Log in to auxiliary ECS 7.

        **netperf -H 192.168.2.10 -p 12013 -t TCP\_STREAM -l 300 -- -m 1440 &**

        **netperf -H 192.168.2.10 -p 12014 -t TCP\_STREAM -l 300 -- -m 1440 &**

        Log in to auxiliary ECS 8.

        **netperf -H 192.168.2.10 -p 12015 -t TCP\_STREAM -l 300 -- -m 1440 &**

        **netperf -H 192.168.2.10 -p 12016 -t TCP\_STREAM -l 300 -- -m 1440 &**

3.  Analyze the test result.

    After the test is complete, the output of the netperf process on one TX end is shown in  [Figure 1](#fig333414318238). The final result is the sum of the test results of the netperf processes on all TX ends.

    **Figure  1**  Output of the netperf process on one TX end<a name="fig333414318238"></a>  
    ![](figures/output-of-the-netperf-process-on-one-tx-end.png "output-of-the-netperf-process-on-one-tx-end")

    >![](/images/icon-note.gif) **NOTE:**   
    >There are a large number of netperf processes. To facilitate statistics collection, you are advised to run the following command to view test data on the tested ECS using sar:  
    >**sar -n DEV 1 60**  


## UDP PPS Test \(Using iperf3\)<a name="section2827154113378"></a>

1.  Test the UDP TX PPS.
    1.  Run the following commands on all auxiliary ECSs to start the server process:

        **iperf3 -s -p 12001 &**

        **iperf3 -s -p 12002 &**

        In the preceding commands,  **-p**  specifies the listening port.

    2.  Start the client process on the tested ECS. For details about common iperf3 parameters, see  [Table 2](#table8470126153613).

        \#\#Auxiliary ECS 1

        **iperf3 -c 192.168.2.11 -p 12001 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.11 -p 12002 -u -b 100M -t 300 -l 16 -A 1 &**

        \#\#Auxiliary ECS 2

        **iperf3 -c 192.168.2.12 -p 12001 -u -b 100M -t 300 -l 16 -A 2 &**

        **iperf3 -c 192.168.2.12 -p 12002 -u -b 100M -t 300 -l 16 -A 3 &**

        ****

        \#\#Auxiliary ECS 3

        **iperf3 -c 192.168.2.13 -p 12001 -u -b 100M -t 300 -l 16 -A 4 &**

        **iperf3 -c 192.168.2.13 -p 12002 -u -b 100M -t 300 -l 16 -A 5 &**

        ****

        \#\#Auxiliary ECS 4

        **iperf3 -c 192.168.2.14 -p 12001 -u -b 100M -t 300 -l 16 -A 6 &**

        **iperf3 -c 192.168.2.14 -p 12002 -u -b 100M -t 300 -l 16 -A 7 &**

        ****

        \#\#Auxiliary ECS 5

        **iperf3 -c 192.168.2.15 -p 12001 -u -b 100M -t 300 -l 16 -A 8 &**

        **iperf3 -c 192.168.2.15 -p 12002 -u -b 100M -t 300 -l 16 -A 9 &**

        ****

        \#\#Auxiliary ECS 6

        **iperf3 -c 192.168.2.16 -p 12001 -u -b 100M -t 300 -l 16 -A 10 &**

        **iperf3 -c 192.168.2.16 -p 12002 -u -b 100M -t 300 -l 16 -A 11 &**

        ****

        \#\#Auxiliary ECS 7

        **iperf3 -c 192.168.2.17 -p 12001 -u -b 100M -t 300 -l 16 -A 12 &**

        **iperf3 -c 192.168.2.17 -p 12002 -u -b 100M -t 300 -l 16 -A 13 &**

        ****

        \#\#Auxiliary ECS 8

        **iperf3 -c 192.168.2.18 -p 12001 -u -b 100M -t 300 -l 16 -A 14 &**

        **iperf3 -c 192.168.2.18 -p 12002 -u -b 100M -t 300 -l 16 -A 15 &**

2.  Test the UDP RX PPS.
    1.  Start the server process on the tested ECS. For details about common iperf3 parameters, see  [Table 2](#table8470126153613).

        \#\#Auxiliary ECS 1

        **iperf3 -s -p 12001 -A 0 -i 60 &**

        **iperf3 -s -p 12002 -A 1 -i 60 &**

        \#\#Auxiliary ECS 2

        **iperf3 -s -p 12003 -A 2 -i 60 &**

        **iperf3 -s -p 12004 -A 3 -i 60 &**

        \#\#Auxiliary ECS 3

        **iperf3 -s -p 12005 -A 4 -i 60 &**

        **iperf3 -s -p 12006 -A 5 -i 60 &**

        \#\#Auxiliary ECS 4

        **iperf3 -s -p 12007 -A 6 -i 60 &**

        **iperf3 -s -p 12008 -A 7 -i 60 &**

        \#\#Auxiliary ECS 5

        **iperf3 -s -p 12009 -A 8 -i 60 &**

        **iperf3 -s -p 12010 -A 9 -i 60 &**

        \#\#Auxiliary ECS 6

        **iperf3 -s -p 12011 -A 10 -i 60 &**

        **iperf3 -s -p 12012 -A 11 -i 60 &**

        \#\#Auxiliary ECS 7

        **iperf3 -s -p 12013 -A 12 -i 60 &**

        **iperf3 -s -p 12014 -A 13 -i 60 &**

        \#\#Auxiliary ECS 8

        **iperf3 -s -p 12015 -A 14 -i 60 &**

        **iperf3 -s -p 12016 -A 15 -i 60 &**

    2.  Start the client process on all auxiliary ECSs. For details about common iperf3 parameters, see  [Table 2](#table8470126153613).

        Log in to auxiliary ECS 1.

        **iperf3 -c 192.168.2.10 -p 12001 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.10 -p 12002 -u -b 100M -t 300 -l 16 -A 1 &**

        Log in to auxiliary ECS 2.

        **iperf3 -c 192.168.2.10 -p 12003 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.10 -p 12004 -u -b 100M -t 300 -l 16 -A 1 &**

        Log in to auxiliary ECS 3.

        **iperf3 -c 192.168.2.10 -p 12005 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.10 -p 12006 -u -b 100M -t 300 -l 16 -A 1 &**

        Log in to auxiliary ECS 4.

        **iperf3 -c 192.168.2.10 -p 12007 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.10 -p 12008 -u -b 100M -t 300 -l 16 -A 1 &**

        Log in to auxiliary ECS 5.

        **iperf3 -c 192.168.2.10 -p 12009 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.10 -p 12010 -u -b 100M -t 300 -l 16 -A 1 &**

        Log in to auxiliary ECS 6.

        **iperf3 -c 192.168.2.10 -p 12011 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.10 -p 12012 -u -b 100M -t 300 -l 16 -A 1 &**

        Log in to auxiliary ECS 7.

        **iperf3 -c 192.168.2.10 -p 12013 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.10 -p 12014 -u -b 100M -t 300 -l 16 -A 1 &**

        Log in to auxiliary ECS 8.

        **iperf3 -c 192.168.2.10 -p 12015 -u -b 100M -t 300 -l 16 -A 0 &**

        **iperf3 -c 192.168.2.10 -p 12016 -u -b 100M -t 300 -l 16 -A 1 &**

3.  Analyze the test result.

    [Figure 2](#fig166644134610)  shows an example of the UDP PPS test result.

    **Figure  2**  UDP PPS test result<a name="fig166644134610"></a>  
    ![](figures/udp-pps-test-result.png "udp-pps-test-result")

    >![](/images/icon-note.gif) **NOTE:**   
    >There are a large number of iperf3 processes. To facilitate statistics collection, you are advised to run the following command to view test data on the tested ECS using sar:  
    >**sar -n DEV 1 60**  


## Latency Test<a name="section63171353123719"></a>

1.  Run the following command to start the qperf process on the tested ECS:

    **qperf &**

2.  Log in to auxiliary ECS 1 and run the following command to perform a latency test:

    **qperf 192.168.2.10 -m 64 -t 60 -vu udp\_lat**

    After the test is complete, the  **lat**  value in the command output is the latency between ECSs.


