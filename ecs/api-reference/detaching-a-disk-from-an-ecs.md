# Detaching a Disk from an ECS<a name="EN-US_TOPIC_0065817707"></a>

## Function<a name="en-us_topic_0057973182_section25786548"></a>

This API is used to detach a disk from an ECS.

## Constraints<a name="en-us_topic_0057973182_section8335615"></a>

The system disk, the device name of which is  **/dev/sda**, and user disks can be detached from an ECS only when the ECS is in the  **stopped**  state. There are no requirements on OSs or OTC tools.

When an ECS is in the  **active**  state, pay attention to the following restrictions:

1.  Only data disks, the device name of which is not  **/dev/sda**, can be detached from an ECS.
2.  Make sure that OTC tools have been installed and enabled on the ECS. Otherwise, the uninstallation will fail.
3.  For a Linux ECS, you need to log in to the ECS and run the  **umount**  command to disassociate the target disk from the file system. In addition, you need to ensure that no data is being written into or being read from the disk. Otherwise, the detachment will fail.
4.  For a Windows ECS, you need to ensure that no data is being written into or being read from the disk when a disk is to be detached from the running ECS.
5.  OSs supporting EVS disk detachment from a running ECS include two parts:
    -   For the first part, see  [External Image Files and Supported OSs](https://docs.otc.t-systems.com/en-us/usermanual/ims/en-us_topic_0030713143.html).
    -   [Table 1](#en-us_topic_0036046828_table9271324195455)  lists the second part of supported OSs.

        **Table  1**  OSs supporting EVS disk detachment from a running ECS

        <a name="en-us_topic_0036046828_table9271324195455"></a>
        <table><thead align="left"><tr id="en-us_topic_0036046828_row29095028195455"><th class="cellrowborder" valign="top" width="35.709999999999994%" id="mcps1.2.3.1.1"><p id="en-us_topic_0036046828_p3874810195455"><a name="en-us_topic_0036046828_p3874810195455"></a><a name="en-us_topic_0036046828_p3874810195455"></a>OS</p>
        </th>
        <th class="cellrowborder" valign="top" width="64.29%" id="mcps1.2.3.1.2"><p id="en-us_topic_0036046828_p45424225195455"><a name="en-us_topic_0036046828_p45424225195455"></a><a name="en-us_topic_0036046828_p45424225195455"></a>Version</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0036046828_row6164841195455"><td class="cellrowborder" rowspan="4" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p29590097195455"><a name="en-us_topic_0036046828_p29590097195455"></a><a name="en-us_topic_0036046828_p29590097195455"></a>CentOS</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p47987633195455"><a name="en-us_topic_0036046828_p47987633195455"></a><a name="en-us_topic_0036046828_p47987633195455"></a>7.3 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row29235518195455"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p17103579195455"><a name="en-us_topic_0036046828_p17103579195455"></a><a name="en-us_topic_0036046828_p17103579195455"></a>7.2 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row19714485195455"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p27960603195455"><a name="en-us_topic_0036046828_p27960603195455"></a><a name="en-us_topic_0036046828_p27960603195455"></a>6.8 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row50318836195455"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p33382838195455"><a name="en-us_topic_0036046828_p33382838195455"></a><a name="en-us_topic_0036046828_p33382838195455"></a>6.7 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row32010086195455"><td class="cellrowborder" rowspan="2" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p42680203195455"><a name="en-us_topic_0036046828_p42680203195455"></a><a name="en-us_topic_0036046828_p42680203195455"></a>Debian</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p34544441195455"><a name="en-us_topic_0036046828_p34544441195455"></a><a name="en-us_topic_0036046828_p34544441195455"></a>8.6.0 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row42464514195455"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p40785593195455"><a name="en-us_topic_0036046828_p40785593195455"></a><a name="en-us_topic_0036046828_p40785593195455"></a>8.5.0 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row31526020195455"><td class="cellrowborder" rowspan="2" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p3470819195455"><a name="en-us_topic_0036046828_p3470819195455"></a><a name="en-us_topic_0036046828_p3470819195455"></a>Fedora</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p12700947195455"><a name="en-us_topic_0036046828_p12700947195455"></a><a name="en-us_topic_0036046828_p12700947195455"></a>25 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row7771181195618"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p28046932195618"><a name="en-us_topic_0036046828_p28046932195618"></a><a name="en-us_topic_0036046828_p28046932195618"></a>24 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row48634140195618"><td class="cellrowborder" rowspan="4" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p35054084195618"><a name="en-us_topic_0036046828_p35054084195618"></a><a name="en-us_topic_0036046828_p35054084195618"></a>SUSE</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p20808552195618"><a name="en-us_topic_0036046828_p20808552195618"></a><a name="en-us_topic_0036046828_p20808552195618"></a>SUSE Linux Enterprise Server 12 SP2 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row56745994195618"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p28769574195618"><a name="en-us_topic_0036046828_p28769574195618"></a><a name="en-us_topic_0036046828_p28769574195618"></a>SUSE Linux Enterprise Server 12 SP1 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row53117304195618"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p700567195618"><a name="en-us_topic_0036046828_p700567195618"></a><a name="en-us_topic_0036046828_p700567195618"></a>SUSE Linux Enterprise Server 11 SP4 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row1719114311319"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p5009498811319"><a name="en-us_topic_0036046828_p5009498811319"></a><a name="en-us_topic_0036046828_p5009498811319"></a>SUSE Linux Enterprise Server 12 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row588467195618"><td class="cellrowborder" rowspan="2" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p5296204195618"><a name="en-us_topic_0036046828_p5296204195618"></a><a name="en-us_topic_0036046828_p5296204195618"></a>OpenSUSE</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p26339408195618"><a name="en-us_topic_0036046828_p26339408195618"></a><a name="en-us_topic_0036046828_p26339408195618"></a>42.2 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row14494860195618"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p30661931195618"><a name="en-us_topic_0036046828_p30661931195618"></a><a name="en-us_topic_0036046828_p30661931195618"></a>42.1 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row48454688195618"><td class="cellrowborder" rowspan="4" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p33439014195618"><a name="en-us_topic_0036046828_p33439014195618"></a><a name="en-us_topic_0036046828_p33439014195618"></a>Oracle Linux Server release</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p24205579195618"><a name="en-us_topic_0036046828_p24205579195618"></a><a name="en-us_topic_0036046828_p24205579195618"></a>7.3 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row44683344195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p26359341195810"><a name="en-us_topic_0036046828_p26359341195810"></a><a name="en-us_topic_0036046828_p26359341195810"></a>7.2 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row6869729195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p41976870195810"><a name="en-us_topic_0036046828_p41976870195810"></a><a name="en-us_topic_0036046828_p41976870195810"></a>6.8 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row49642196195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p17483405195810"><a name="en-us_topic_0036046828_p17483405195810"></a><a name="en-us_topic_0036046828_p17483405195810"></a>6.7 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row28948492195810"><td class="cellrowborder" rowspan="3" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p59209837195810"><a name="en-us_topic_0036046828_p59209837195810"></a><a name="en-us_topic_0036046828_p59209837195810"></a>Ubuntu Server</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p31267532195810"><a name="en-us_topic_0036046828_p31267532195810"></a><a name="en-us_topic_0036046828_p31267532195810"></a>16.04 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row66691124195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p31012055195810"><a name="en-us_topic_0036046828_p31012055195810"></a><a name="en-us_topic_0036046828_p31012055195810"></a>14.04 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row29984127195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p48048103195810"><a name="en-us_topic_0036046828_p48048103195810"></a><a name="en-us_topic_0036046828_p48048103195810"></a>14.04.4 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row58019688195810"><td class="cellrowborder" rowspan="3" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p52415150195810"><a name="en-us_topic_0036046828_p52415150195810"></a><a name="en-us_topic_0036046828_p52415150195810"></a>Windows (SCSI EVS disks cannot be detached from a running ECS.)</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p17768768195810"><a name="en-us_topic_0036046828_p17768768195810"></a><a name="en-us_topic_0036046828_p17768768195810"></a>Windows Server 2008 R2 Enterprise 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row17974643195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p17286382195810"><a name="en-us_topic_0036046828_p17286382195810"></a><a name="en-us_topic_0036046828_p17286382195810"></a>Windows Server 2012 R2 Standard 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row5831657195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p23420035195810"><a name="en-us_topic_0036046828_p23420035195810"></a><a name="en-us_topic_0036046828_p23420035195810"></a>Windows Server 2016 R2 Standard 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row24482463195810"><td class="cellrowborder" rowspan="2" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p19015578195810"><a name="en-us_topic_0036046828_p19015578195810"></a><a name="en-us_topic_0036046828_p19015578195810"></a>Red Hat Linux Enterprise</p>
        </td>
        <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0036046828_p63866841195810"><a name="en-us_topic_0036046828_p63866841195810"></a><a name="en-us_topic_0036046828_p63866841195810"></a>7.3 64bit</p>
        </td>
        </tr>
        <tr id="en-us_topic_0036046828_row39384495195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0036046828_p55812053195810"><a name="en-us_topic_0036046828_p55812053195810"></a><a name="en-us_topic_0036046828_p55812053195810"></a>6.8 64bit</p>
        </td>
        </tr>
        </tbody>
        </table>



## URI<a name="en-us_topic_0057973182_section30752341"></a>

DELETE /v2/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments/\{volume\_id\}

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments/\{volume\_id\}

[Table 2](#en-us_topic_0057973182_table2814978410562)  describes the parameters in the URI.

**Table  2**  Parameter description

<a name="en-us_topic_0057973182_table2814978410562"></a>
<table><thead align="left"><tr id="en-us_topic_0057973182_row4149654710562"><th class="cellrowborder" valign="top" width="16.650000000000002%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.99000000000001%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973182_row3491217610562"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973182_p931403110562"><a name="en-us_topic_0057973182_p931403110562"></a><a name="en-us_topic_0057973182_p931403110562"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973182_p1623904210562"><a name="en-us_topic_0057973182_p1623904210562"></a><a name="en-us_topic_0057973182_p1623904210562"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.99000000000001%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973182_row12799156113429"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973182_p45509579113512"><a name="en-us_topic_0057973182_p45509579113512"></a><a name="en-us_topic_0057973182_p45509579113512"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973182_p62397288113512"><a name="en-us_topic_0057973182_p62397288113512"></a><a name="en-us_topic_0057973182_p62397288113512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.99000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973182_p21015586113512"><a name="en-us_topic_0057973182_p21015586113512"></a><a name="en-us_topic_0057973182_p21015586113512"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973182_row24368930113434"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973182_p17993785113434"><a name="en-us_topic_0057973182_p17993785113434"></a><a name="en-us_topic_0057973182_p17993785113434"></a>volume_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973182_p48210456113434"><a name="en-us_topic_0057973182_p48210456113434"></a><a name="en-us_topic_0057973182_p48210456113434"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.99000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973182_p349907511364"><a name="en-us_topic_0057973182_p349907511364"></a><a name="en-us_topic_0057973182_p349907511364"></a>Specifies the volume ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section21331833141612"></a>

None

## Response<a name="en-us_topic_0057973182_section36865975"></a>

None

## Example Request<a name="en-us_topic_0057973182_section63358319"></a>

```
DELETE https://{endpoint}/v2/6fbe9263116a4b68818cf1edce16bc4f/servers/ab258e25-e351-47c7-b6e3-0749c5d9ed6a/os-volume_attachments/54667652-3029-4af8-9222-2d53066fd61c
DELETE https://{endpoint}/v2.1/6fbe9263116a4b68818cf1edce16bc4f/servers/ab258e25-e351-47c7-b6e3-0749c5d9ed6a/os-volume_attachments/54667652-3029-4af8-9222-2d53066fd61c
```

## Example Response<a name="section32971253153813"></a>

None

## Returned Values<a name="en-us_topic_0057973182_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

