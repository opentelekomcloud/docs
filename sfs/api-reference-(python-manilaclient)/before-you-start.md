# Before You Start<a name="EN-US_TOPIC_0092472213"></a>

## Introduction<a name="section4015089113398"></a>

This document introduces the Scalable File Service \(SFS\) API, including its description, syntax, parameters, and examples. You can obtain the required information according to the following table.

**Table  1**  Introduction

<a name="table2982571113398"></a>
<table><thead align="left"><tr id="row2906568713398"><th class="cellrowborder" valign="top" width="46%" id="mcps1.2.3.1.1"><p id="p551045313398"><a name="p551045313398"></a><a name="p551045313398"></a>Phase</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.3.1.2"><p id="p4369358813398"><a name="p4369358813398"></a><a name="p4369358813398"></a>Related Chapter</p>
</th>
</tr>
</thead>
<tbody><tr id="row4951977213398"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p id="p5167858013398"><a name="p5167858013398"></a><a name="p5167858013398"></a>Learn about the SFS API components and API lists.</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p2521542813398"><a name="p2521542813398"></a><a name="p2521542813398"></a><a href="overview.md">Chapter 2 Overview</a></p>
</td>
</tr>
<tr id="row2616878313398"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p id="p3929666113398"><a name="p3929666113398"></a><a name="p3929666113398"></a>Learn about how to call APIs.</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p2891300913398"><a name="p2891300913398"></a><a name="p2891300913398"></a><a href="api-usage.md">Chapter 3 API Usage</a></p>
</td>
</tr>
<tr id="row5889048913398"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.1 "><p id="p2350601716365"><a name="p2350601716365"></a><a name="p2350601716365"></a>Learn about how to use API commands.</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.2 "><p id="p3477393213398"><a name="p3477393213398"></a><a name="p3477393213398"></a><a href="api-description.md">Chapter 4 API Description</a></p>
</td>
</tr>
</tbody>
</table>

## Required Knowledge<a name="section6522508213398"></a>

The python-manilaclient tool encapsulates the native Manila RESTful API. To use the manila commands provided by python-manilaclient, you need to master the basic concepts and knowledge of python-manilaclient. For details, go to  [https://pypi.python.org/pypi/python-manilaclient](https://pypi.python.org/pypi/python-manilaclient).

## Software Compatibility<a name="section1821310111813"></a>

<a name="table1776913320580"></a>
<table><thead align="left"><tr id="row127701033185820"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.1.4.1.1"><p id="p1333547205811"><a name="p1333547205811"></a><a name="p1333547205811"></a><strong id="b842352706114958"><a name="b842352706114958"></a><a name="b842352706114958"></a>Software Package</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.1.4.1.2"><p id="p1333414785816"><a name="p1333414785816"></a><a name="p1333414785816"></a><strong id="b842352706163827"><a name="b842352706163827"></a><a name="b842352706163827"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.1.4.1.3"><p id="p0337124712585"><a name="p0337124712585"></a><a name="p0337124712585"></a><strong id="b163112058134010"><a name="b163112058134010"></a><a name="b163112058134010"></a>How to Obtain</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row13770163395813"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.1.4.1.1 "><p id="p20735493144259"><a name="p20735493144259"></a><a name="p20735493144259"></a>python-manilaclient</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.1.4.1.2 "><p id="p2889110135914"><a name="p2889110135914"></a><a name="p2889110135914"></a>Client for OpenStack Manila API</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.1.4.1.3 "><p id="p146758821218"><a name="p146758821218"></a><a name="p146758821218"></a>You are advised to use the latest version of <a href="https://pypi.org/project/python-manilaclient/" target="_blank" rel="noopener noreferrer">python-manilaclient</a>. Versions earlier than <a href="https://pypi.org/project/python-manilaclient/1.8.1/" target="_blank" rel="noopener noreferrer">python-manilaclient-1.8.1</a> are not compatible. Some features, for example, ignoring the error status of existing access rules when adding a shared access rule, require <a href="https://pypi.org/project/python-manilaclient/1.12.0/" target="_blank" rel="noopener noreferrer">python-manilaclient-1.12.0</a> or a later version.</p>
<div class="note" id="note71294020404"><a name="note71294020404"></a><a name="note71294020404"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p149115288317"><a name="p149115288317"></a><a name="p149115288317"></a>This API reference document is written and tested based on the python-manilaclient-1.8.1 environment. Although later versions of python-manilaclient are compatible with earlier versions, some descriptions may vary in later versions. Therefore, when you use <a href="https://pypi.org/project/python-manilaclient/" target="_blank" rel="noopener noreferrer">python-manilaclient</a> of the latest version and find description differences, the newest description prevails.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The latest version of manila APIs supported by current SFS is 2.28. For details about how to query the supported versions, see  [Querying All Major Versions](querying-all-major-versions.md). Therefore, in the latest version of python-manilaclient, some parameters requiring the version of manila APIs to be later than 2.28 are not supported by SFS. This document does not describe such parameters. For example, in python-manilaclient-1.23.0, the  **--count <True|False\>**  parameter in the  **manila list**  command requires that the version of manila APIs must be 2.42 or later. As a result, SFS does not support  **--count <True|False\>**  and this parameter is not described in this document.  

