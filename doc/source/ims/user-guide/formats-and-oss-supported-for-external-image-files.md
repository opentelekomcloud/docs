# Formats and OSs Supported for External Image Files<a name="EN-US_TOPIC_0030713143"></a>

## Supported File Formats<a name="section161026175283"></a>

An external image file is a file that is in VMDK, VHD, QCOW2, RAW, VHDX, QED, VDI, QCOW, ZVHD2, or ZVHD format and can be used to create private images. Select a format that meets your requirements.

## Supported OSs<a name="en-us_topic_0029124551_section35898979162323"></a>

When you upload an external image file to an OBS bucket on the management console, the OS contained in the image file will be identified.  [Table 1](#table6432073491848)  lists the OSs supported for external image files.

If the OS cannot be identified or is not supported:


-   For Windows,  **Other\_Windows \(64\_bit\)**  or  **Other\_Windows \(32\_bit\)**  will be selected during image registration.
-   For Linux,  **Other\_Linux \(64\_bit\)**  or  **Other\_Linux \(32\_bit\)**  will be selected during image registration.

>![](/images/icon-note.gif) **NOTE:**   
>-   Uploading image files using OSs not listed in  [Table 1](#table6432073491848)  may fail. You are advised to contact the customer service before uploading these image files.  
>-   For details about the formats and OSs supported for BMS images, see  ___Bare Metal Server Private Image Creation Guide_.  
>-   When uploading a CoreOS image file, set the OS type to CoreOS. Otherwise, the OS type will be set to  **Other \(64bit\)**. In addition, ensure that coreos-cloudinit has been installed and configured for CoreOS. Automatic system upgrades must be disabled. Otherwise, they may make ECSs created using this image unavailable.  
>-   You can only use external image files using Windows 10 64bit or Windows 7 Enterprise 64bit to create ECSs on a Dedicated Host \(DeH\).  

**Table  1**  Supported OSs

<a name="table6432073491848"></a>
<table><thead align="left"><tr id="row201480991848"><th class="cellrowborder" valign="top" width="34.339999999999996%" id="mcps1.2.3.1.1"><p id="p6304755791848"><a name="p6304755791848"></a><a name="p6304755791848"></a><strong id="b155675123"><a name="b155675123"></a><a name="b155675123"></a>OS Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65.66%" id="mcps1.2.3.1.2"><p id="p5858011191848"><a name="p5858011191848"></a><a name="p5858011191848"></a>OS Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row6258123091848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p5298947991848"><a name="p5298947991848"></a><a name="p5298947991848"></a>Windows</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p149292815585"><a name="p149292815585"></a><a name="p149292815585"></a>Windows 10 64bit</p>
<p id="p79411805812"><a name="p79411805812"></a><a name="p79411805812"></a>Windows 7 Enterprise 64bit</p>
<p id="p9928151385810"><a name="p9928151385810"></a><a name="p9928151385810"></a>Windows Server 2016 Standard 64bit</p>
<p id="p2708788317910"><a name="p2708788317910"></a><a name="p2708788317910"></a>Windows Server 2016 Datacenter 64bit</p>
<p id="p2068974491848"><a name="p2068974491848"></a><a name="p2068974491848"></a>Windows Server 2012 R2 Standard 64bit</p>
<p id="p1830619891848"><a name="p1830619891848"></a><a name="p1830619891848"></a>Windows Server 2012 Essentials R2 64bit</p>
<p id="p5516814391848"><a name="p5516814391848"></a><a name="p5516814391848"></a>Windows Server 2012 R2 Datacenter 64bit</p>
<p id="p4850551391848"><a name="p4850551391848"></a><a name="p4850551391848"></a>Windows Server 2012 Datacenter 64bit</p>
<p id="p5854607591848"><a name="p5854607591848"></a><a name="p5854607591848"></a>Windows Server 2012 Standard 64bit</p>
<p id="p1314733791848"><a name="p1314733791848"></a><a name="p1314733791848"></a>Windows Server 2008 WEB R2 64bit</p>
<p id="p3475103291848"><a name="p3475103291848"></a><a name="p3475103291848"></a>Windows Server 2008 R2 Standard 64bit</p>
<p id="p4901102891848"><a name="p4901102891848"></a><a name="p4901102891848"></a>Windows Server 2008 R2 Enterprise 64bit</p>
<p id="p2631775891848"><a name="p2631775891848"></a><a name="p2631775891848"></a>Windows Server 2008 R2 Datacenter 64bit</p>
</td>
</tr>
<tr id="row398604091848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p1067557092045"><a name="p1067557092045"></a><a name="p1067557092045"></a>SUSE</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p427144841012"><a name="p427144841012"></a><a name="p427144841012"></a>SUSE Linux Enterprise Server 15 64bit</p>
<p id="p19875592192623"><a name="p19875592192623"></a><a name="p19875592192623"></a>SUSE Linux Enterprise Server 12 SP3 64bit</p>
<p id="p2528337917931"><a name="p2528337917931"></a><a name="p2528337917931"></a>SUSE Linux Enterprise Server 12 SP2 64bit</p>
<p id="p2498311292045"><a name="p2498311292045"></a><a name="p2498311292045"></a>SUSE Linux Enterprise Server 12 SP1 64bit</p>
<p id="p5855455559"><a name="p5855455559"></a><a name="p5855455559"></a>SUSE Linux Enterprise Server 12 64bit</p>
<p id="p4611313792045"><a name="p4611313792045"></a><a name="p4611313792045"></a>SUSE Linux Enterprise Server 11 SP4 64bit</p>
<p id="p2768989492045"><a name="p2768989492045"></a><a name="p2768989492045"></a>SUSE Linux Enterprise Server 11 SP3 64bit</p>
<p id="p3155453692045"><a name="p3155453692045"></a><a name="p3155453692045"></a>SUSE Linux Enterprise Server 11 SP3 32bit</p>
<p id="p147075291059"><a name="p147075291059"></a><a name="p147075291059"></a>SUSE Linux Enterprise Server 11 SP1 32bit</p>
</td>
</tr>
<tr id="row4131173791848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p6060867192053"><a name="p6060867192053"></a><a name="p6060867192053"></a>Oracle Linux</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p1135017501872"><a name="p1135017501872"></a><a name="p1135017501872"></a>Oracle Linux Server release 7.6 64bit</p>
<p id="p4665153392814"><a name="p4665153392814"></a><a name="p4665153392814"></a>Oracle Linux Server release 7.5 64bit</p>
<p id="p2785403117463"><a name="p2785403117463"></a><a name="p2785403117463"></a>Oracle Linux Server release 7.4 64bit</p>
<p id="p1815436517104"><a name="p1815436517104"></a><a name="p1815436517104"></a>Oracle Linux Server release 7.3 64bit</p>
<p id="p6270319017104"><a name="p6270319017104"></a><a name="p6270319017104"></a>Oracle Linux Server release 7.2 64bit</p>
<p id="p19691557172223"><a name="p19691557172223"></a><a name="p19691557172223"></a>Oracle Linux Server release 7.1 64bit</p>
<p id="p66143123171016"><a name="p66143123171016"></a><a name="p66143123171016"></a>Oracle Linux Server release 7.0 64bit</p>
<p id="p1513271372316"><a name="p1513271372316"></a><a name="p1513271372316"></a>Oracle Linux Server release 6.10 64bit</p>
<p id="p4106295311445"><a name="p4106295311445"></a><a name="p4106295311445"></a>Oracle Linux Server release 6.9 64bit</p>
<p id="p1656143445914"><a name="p1656143445914"></a><a name="p1656143445914"></a>Oracle Linux Server release 6.8 64bit</p>
<p id="p5687927192053"><a name="p5687927192053"></a><a name="p5687927192053"></a>Oracle Linux Server release 6.7 64bit</p>
<p id="p1855955317955"><a name="p1855955317955"></a><a name="p1855955317955"></a>Oracle Linux Server release 6.5 64bit</p>
</td>
</tr>
<tr id="row3711547791848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p915147591848"><a name="p915147591848"></a><a name="p915147591848"></a>RedHat</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p1154574012920"><a name="p1154574012920"></a><a name="p1154574012920"></a>RedHat Linux Enterprise 8.0 64bit</p>
<p id="p13638929488"><a name="p13638929488"></a><a name="p13638929488"></a>RedHat Linux Enterprise 7.6 64bit</p>
<p id="p1197765915277"><a name="p1197765915277"></a><a name="p1197765915277"></a>RedHat Linux Enterprise 7.5 64bit</p>
<p id="p51518502175218"><a name="p51518502175218"></a><a name="p51518502175218"></a>RedHat Linux Enterprise 7.4 64bit</p>
<p id="p132197595549"><a name="p132197595549"></a><a name="p132197595549"></a>RedHat Linux Enterprise 7.3 64bit</p>
<p id="p1652040991848"><a name="p1652040991848"></a><a name="p1652040991848"></a>RedHat Linux Enterprise 7.2 64bit</p>
<p id="p4139349692119"><a name="p4139349692119"></a><a name="p4139349692119"></a>RedHat Linux Enterprise 7.1 64bit</p>
<p id="p6616643991848"><a name="p6616643991848"></a><a name="p6616643991848"></a>RedHat Linux Enterprise 7.0 64bit</p>
<p id="p1911971033018"><a name="p1911971033018"></a><a name="p1911971033018"></a>RedHat Linux Enterprise 6.10 64bit</p>
<p id="p8478538103747"><a name="p8478538103747"></a><a name="p8478538103747"></a>RedHat Linux Enterprise 6.9 64bit</p>
<p id="p940876191848"><a name="p940876191848"></a><a name="p940876191848"></a>RedHat Linux Enterprise 6.8 64bit</p>
<p id="p536737317113"><a name="p536737317113"></a><a name="p536737317113"></a>RedHat Linux Enterprise 6.7 64bit</p>
<p id="p4522477891848"><a name="p4522477891848"></a><a name="p4522477891848"></a>RedHat Linux Enterprise 6.6 64bit</p>
<p id="p3350195891848"><a name="p3350195891848"></a><a name="p3350195891848"></a>RedHat Linux Enterprise 6.6 32bit</p>
<p id="p40974123164247"><a name="p40974123164247"></a><a name="p40974123164247"></a>RedHat Linux Enterprise 6.5 64bit</p>
<p id="p2993376091848"><a name="p2993376091848"></a><a name="p2993376091848"></a>RedHat Linux Enterprise 6.4 64bit</p>
<p id="p5216355591848"><a name="p5216355591848"></a><a name="p5216355591848"></a>RedHat Linux Enterprise 6.4 32bit</p>
</td>
</tr>
<tr id="row4251554391848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p1617108691848"><a name="p1617108691848"></a><a name="p1617108691848"></a>Ubuntu</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p892523312573"><a name="p892523312573"></a><a name="p892523312573"></a>Ubuntu 19.04 server 64bit</p>
<p id="p669121852716"><a name="p669121852716"></a><a name="p669121852716"></a>Ubuntu 18.04 server 64bit</p>
<p id="p1667678691848"><a name="p1667678691848"></a><a name="p1667678691848"></a>Ubuntu 16.04 server 64bit</p>
<p id="p19054638203840"><a name="p19054638203840"></a><a name="p19054638203840"></a>Ubuntu 14.04.5 server 64bit</p>
<p id="p984759291848"><a name="p984759291848"></a><a name="p984759291848"></a>Ubuntu 14.04.4 server 64bit</p>
<p id="p839523391848"><a name="p839523391848"></a><a name="p839523391848"></a>Ubuntu 14.04.4 server 32bit</p>
<p id="p4240022691848"><a name="p4240022691848"></a><a name="p4240022691848"></a>Ubuntu 14.04.3 server 64bit</p>
<p id="p3993447491848"><a name="p3993447491848"></a><a name="p3993447491848"></a>Ubuntu 14.04.3 server 32bit</p>
<p id="p401530691848"><a name="p401530691848"></a><a name="p401530691848"></a>Ubuntu 14.04.1 server 64bit</p>
<p id="p862071491848"><a name="p862071491848"></a><a name="p862071491848"></a>Ubuntu 14.04.1 server 32bit</p>
<p id="p5795835991848"><a name="p5795835991848"></a><a name="p5795835991848"></a>Ubuntu 14.04 server 64bit</p>
<p id="p3970382391848"><a name="p3970382391848"></a><a name="p3970382391848"></a>Ubuntu 14.04 server 32bit</p>
</td>
</tr>
<tr id="row5520923091848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p5283379791848"><a name="p5283379791848"></a><a name="p5283379791848"></a>openSUSE</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p62904197145636"><a name="p62904197145636"></a><a name="p62904197145636"></a>OpenSUSE 42.3 64bit</p>
<p id="p21456491171121"><a name="p21456491171121"></a><a name="p21456491171121"></a>OpenSUSE 42.2 64bit</p>
<p id="p5109479792147"><a name="p5109479792147"></a><a name="p5109479792147"></a>OpenSUSE 42.1 64bit</p>
<p id="p1768688291848"><a name="p1768688291848"></a><a name="p1768688291848"></a>OpenSUSE 15.1 64bit</p>
<p id="p3147103321110"><a name="p3147103321110"></a><a name="p3147103321110"></a>OpenSUSE 15.0 64bit</p>
<p id="p1825454818287"><a name="p1825454818287"></a><a name="p1825454818287"></a>OpenSUSE 13.2 64bit</p>
<p id="p1243535391848"><a name="p1243535391848"></a><a name="p1243535391848"></a>OpenSUSE 11.3 64bit</p>
</td>
</tr>
<tr id="row5273302091848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p764933691848"><a name="p764933691848"></a><a name="p764933691848"></a>CentOS</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p559218414573"><a name="p559218414573"></a><a name="p559218414573"></a>CentOS 8.0 64bit</p>
<p id="p1132121414286"><a name="p1132121414286"></a><a name="p1132121414286"></a>CentOS 7.7 64bit</p>
<p id="p5531192499"><a name="p5531192499"></a><a name="p5531192499"></a>CentOS 7.6 64bit</p>
<p id="p875883719286"><a name="p875883719286"></a><a name="p875883719286"></a>CentOS 7.5 64bit</p>
<p id="p15299896174939"><a name="p15299896174939"></a><a name="p15299896174939"></a>CentOS 7.4 64bit</p>
<p id="p38720702171135"><a name="p38720702171135"></a><a name="p38720702171135"></a>CentOS 7.3 64bit</p>
<p id="p4548500491848"><a name="p4548500491848"></a><a name="p4548500491848"></a>CentOS 7.2 64bit</p>
<p id="p5145754791848"><a name="p5145754791848"></a><a name="p5145754791848"></a>CentOS 7.1 64bit</p>
<p id="p6090982291848"><a name="p6090982291848"></a><a name="p6090982291848"></a>CentOS 7.0 64bit</p>
<p id="p4202818891848"><a name="p4202818891848"></a><a name="p4202818891848"></a>CentOS 7.0 32bit</p>
<p id="p35181521163010"><a name="p35181521163010"></a><a name="p35181521163010"></a>CentOS 6.10 64bit</p>
<p id="p20658102142619"><a name="p20658102142619"></a><a name="p20658102142619"></a>CentOS 6.10 32bit</p>
<p id="p6192921611555"><a name="p6192921611555"></a><a name="p6192921611555"></a>CentOS 6.9 64bit</p>
<p id="p1426387791848"><a name="p1426387791848"></a><a name="p1426387791848"></a>CentOS 6.8 64bit</p>
<p id="p6325763891848"><a name="p6325763891848"></a><a name="p6325763891848"></a>CentOS 6.7 64bit</p>
<p id="p270086291848"><a name="p270086291848"></a><a name="p270086291848"></a>CentOS 6.7 32bit</p>
<p id="p5214175191848"><a name="p5214175191848"></a><a name="p5214175191848"></a>CentOS 6.6 64bit</p>
<p id="p4101103391848"><a name="p4101103391848"></a><a name="p4101103391848"></a>CentOS 6.6 32bit</p>
<p id="p1118902291848"><a name="p1118902291848"></a><a name="p1118902291848"></a>CentOS 6.5 64bit</p>
<p id="p3384504491848"><a name="p3384504491848"></a><a name="p3384504491848"></a>CentOS 6.5 32bit</p>
<p id="p5360667491848"><a name="p5360667491848"></a><a name="p5360667491848"></a>CentOS 6.4 64bit</p>
<p id="p787298891848"><a name="p787298891848"></a><a name="p787298891848"></a>CentOS 6.4 32bit</p>
<p id="p636527191848"><a name="p636527191848"></a><a name="p636527191848"></a>CentOS 6.3 64bit</p>
<p id="p3655057591848"><a name="p3655057591848"></a><a name="p3655057591848"></a>CentOS 6.3 32bit</p>
</td>
</tr>
<tr id="row3896173391848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p791533091848"><a name="p791533091848"></a><a name="p791533091848"></a>Debian</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p13265111871117"><a name="p13265111871117"></a><a name="p13265111871117"></a>Debian GNU/Linux 10.0.0 64bit</p>
<p id="p13109825114924"><a name="p13109825114924"></a><a name="p13109825114924"></a>Debian GNU/Linux 9.3.0 64bit</p>
<p id="p929485515275"><a name="p929485515275"></a><a name="p929485515275"></a>Debian GNU/Linux 9.0.0 64bit</p>
<p id="p3085892315275"><a name="p3085892315275"></a><a name="p3085892315275"></a>Debian GNU/Linux 8.8.0 64bit</p>
<p id="p17514512018"><a name="p17514512018"></a><a name="p17514512018"></a>Debian GNU/Linux 8.7.0 64bit</p>
<p id="p3681491491848"><a name="p3681491491848"></a><a name="p3681491491848"></a>Debian GNU/Linux 8.6.0 64bit</p>
<p id="p5720116091848"><a name="p5720116091848"></a><a name="p5720116091848"></a>Debian GNU/Linux 8.5.0 64bit</p>
<p id="p5456596591848"><a name="p5456596591848"></a><a name="p5456596591848"></a>Debian GNU/Linux 8.4.0 64bit</p>
<p id="p695525291848"><a name="p695525291848"></a><a name="p695525291848"></a>Debian GNU/Linux 8.2.0 64bit</p>
<p id="p12687127065"><a name="p12687127065"></a><a name="p12687127065"></a>Debian GNU/Linux 8.1.0 64bit</p>
</td>
</tr>
<tr id="row1015039291848"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p763825091848"><a name="p763825091848"></a><a name="p763825091848"></a>Fedora</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p641644811120"><a name="p641644811120"></a><a name="p641644811120"></a>Fedora 30 64bit</p>
<p id="p13288940163817"><a name="p13288940163817"></a><a name="p13288940163817"></a>Fedora 29 64bit</p>
<p id="p6586195917286"><a name="p6586195917286"></a><a name="p6586195917286"></a>Fedora 28 64bit</p>
<p id="p43589011114737"><a name="p43589011114737"></a><a name="p43589011114737"></a>Fedora 27 64bit</p>
<p id="p42286882145654"><a name="p42286882145654"></a><a name="p42286882145654"></a>Fedora 26 64bit</p>
<p id="p39288857171156"><a name="p39288857171156"></a><a name="p39288857171156"></a>Fedora 25 64bit</p>
<p id="p5981371991848"><a name="p5981371991848"></a><a name="p5981371991848"></a>Fedora 24 64bit</p>
<p id="p3350596091848"><a name="p3350596091848"></a><a name="p3350596091848"></a>Fedora 23 64bit</p>
<p id="p3020992791848"><a name="p3020992791848"></a><a name="p3020992791848"></a>Fedora 22 64bit</p>
</td>
</tr>
<tr id="row4508369092157"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p213057229220"><a name="p213057229220"></a><a name="p213057229220"></a>EulerOS</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p1435613411306"><a name="p1435613411306"></a><a name="p1435613411306"></a>EulerOS 2.5 64bit</p>
<p id="p350528079220"><a name="p350528079220"></a><a name="p350528079220"></a>EulerOS 2.3 64bit</p>
<p id="p1589714971115"><a name="p1589714971115"></a><a name="p1589714971115"></a>EulerOS 2.2 64bit</p>
<p id="p14137503112"><a name="p14137503112"></a><a name="p14137503112"></a>EulerOS 2.1 64bit</p>
<p id="p125241706711"><a name="p125241706711"></a><a name="p125241706711"></a>EulerOS 2.0 SP3 64bit</p>
<p id="p12527603720"><a name="p12527603720"></a><a name="p12527603720"></a>EulerOS 2.0 SP2 64bit</p>
</td>
</tr>
<tr id="row43529124143712"><td class="cellrowborder" valign="top" width="34.339999999999996%" headers="mcps1.2.3.1.1 "><p id="p36382066132836"><a name="p36382066132836"></a><a name="p36382066132836"></a>CoreOS</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.3.1.2 "><p id="p10122186171218"><a name="p10122186171218"></a><a name="p10122186171218"></a>CoreOS 1068.10.0</p>
<p id="p4503238917837"><a name="p4503238917837"></a><a name="p4503238917837"></a>CoreOS 1010.5.0</p>
<p id="p14631727171223"><a name="p14631727171223"></a><a name="p14631727171223"></a>CoreOS 1298.6.0</p>
</td>
</tr>
</tbody>
</table>

## Related Operations<a name="section20796426191216"></a>

For how to upload an external image file, see  [Uploading an External Image File](uploading-an-external-image-file-(windows).md)  and  [Uploading an External Image File](uploading-an-external-image-file-(linux).md).

After an external image file is successfully uploaded, you can register this image file as a private image on the cloud platform. For details, see  [Registering an External Image File as a Private Image](registering-an-external-image-file-as-a-private-image-(windows).md)  and  [Registering an External Image File as a Private Image](registering-an-external-image-file-as-a-private-image-(linux).md).

