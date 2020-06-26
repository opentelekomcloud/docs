# Executing a Job Object<a name="EN-US_TOPIC_0172486204"></a>

## Function<a name="section40666287163540"></a>

This API is used to execute a created job object. This API is compatible with Sahara.

## URI<a name="section25682805163556"></a>

-   Format

    POST /v1.1/\{project\_id\}/jobs/\{job\_id\}/execute

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16571835194812"><a name="p16571835194812"></a><a name="p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p141410194812"><a name="p141410194812"></a><a name="p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11454278194812"><a name="p11454278194812"></a><a name="p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12931900144556"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p40851019144556"><a name="p40851019144556"></a><a name="p40851019144556"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p20598275144556"><a name="p20598275144556"></a><a name="p20598275144556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p57847563144556"><a name="p57847563144556"></a><a name="p57847563144556"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row5348473617029"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3729636117029"><a name="p3729636117029"></a><a name="p3729636117029"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p110643517029"><a name="p110643517029"></a><a name="p110643517029"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2251243817029"><a name="p2251243817029"></a><a name="p2251243817029"></a>Job object ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7976792193238"></a>

**Table  2**  Request parameter description

<a name="table51257841151049"></a>
<table><thead align="left"><tr id="row8480851151049"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p15860319151049"><a name="p15860319151049"></a><a name="p15860319151049"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p9617423151049"><a name="p9617423151049"></a><a name="p9617423151049"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p40813771151049"><a name="p40813771151049"></a><a name="p40813771151049"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p17581180151049"><a name="p17581180151049"></a><a name="p17581180151049"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33862023103039"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3981883717238"><a name="p3981883717238"></a><a name="p3981883717238"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1092483717238"><a name="p1092483717238"></a><a name="p1092483717238"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1312411717238"><a name="p1312411717238"></a><a name="p1312411717238"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p4114259017238"><a name="p4114259017238"></a><a name="p4114259017238"></a>Cluster ID</p>
</td>
</tr>
<tr id="row2799322317244"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5285858517244"><a name="p5285858517244"></a><a name="p5285858517244"></a>input_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p6533931417336"><a name="p6533931417336"></a><a name="p6533931417336"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p460372817352"><a name="p460372817352"></a><a name="p460372817352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p8800137165528"><a name="p8800137165528"></a><a name="p8800137165528"></a>Input data source ID of a job object</p>
<p id="p58968452306"><a name="p58968452306"></a><a name="p58968452306"></a>For details on how to obtain the input data source ID, see <a href="creating-a-data-source.md">Creating a Data Source</a>.</p>
</td>
</tr>
<tr id="row6387801017255"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p673631817255"><a name="p673631817255"></a><a name="p673631817255"></a>output_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4358774117336"><a name="p4358774117336"></a><a name="p4358774117336"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p690407217352"><a name="p690407217352"></a><a name="p690407217352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p3368190317255"><a name="p3368190317255"></a><a name="p3368190317255"></a>Output data source ID of a job object</p>
<p id="p18012513306"><a name="p18012513306"></a><a name="p18012513306"></a>For details on how to obtain the output data source ID, see <a href="creating-a-data-source.md">Creating a Data Source</a>.</p>
</td>
</tr>
<tr id="row54445180144846"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p47983487144846"><a name="p47983487144846"></a><a name="p47983487144846"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p61457218144846"><a name="p61457218144846"></a><a name="p61457218144846"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p11978733144846"><a name="p11978733144846"></a><a name="p11978733144846"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p30753321144846"><a name="p30753321144846"></a><a name="p30753321144846"></a>Whether a job object is protected</p>
<a name="ul360256379574"></a><a name="ul360256379574"></a><ul id="ul360256379574"><li>true</li><li>false</li></ul>
<p id="p6483812795728"><a name="p6483812795728"></a><a name="p6483812795728"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row5737606144852"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62092923144852"><a name="p62092923144852"></a><a name="p62092923144852"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p63470881144852"><a name="p63470881144852"></a><a name="p63470881144852"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p40867743144852"><a name="p40867743144852"></a><a name="p40867743144852"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p21952926144852"><a name="p21952926144852"></a><a name="p21952926144852"></a>Whether a job object is public</p>
<a name="ul11534704151937"></a><a name="ul11534704151937"></a><ul id="ul11534704151937"><li>true</li><li>false</li></ul>
<p id="p20191752151937"><a name="p20191752151937"></a><a name="p20191752151937"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row22681519104555"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4472907517312"><a name="p4472907517312"></a><a name="p4472907517312"></a>job_configs</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2866668517336"><a name="p2866668517336"></a><a name="p2866668517336"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5513246917312"><a name="p5513246917312"></a><a name="p5513246917312"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5205454817312"><a name="p5205454817312"></a><a name="p5205454817312"></a>Key-value pair set for saving job running configurations</p>
<p id="p1643215115412"><a name="p1643215115412"></a><a name="p1643215115412"></a>If the job type is MapReduce or Spark, set the first parameter of <strong id="b15486475114527"><a name="b15486475114527"></a><a name="b15486475114527"></a>args</strong> to be the same as the <strong id="b21464722151721"><a name="b21464722151721"></a><a name="b21464722151721"></a>arguments</strong> parameter in <a href="adding-a-job-and-executing-the-job.md">Adding a Job and Executing the Job</a>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section38599577193858"></a>

**Table  3**  Response parameter description

<a name="table5154210817547"></a>
<table><thead align="left"><tr id="row5182537317547"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p3710571317547"><a name="p3710571317547"></a><a name="p3710571317547"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p4673655817547"><a name="p4673655817547"></a><a name="p4673655817547"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p2756483917547"><a name="p2756483917547"></a><a name="p2756483917547"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6552698617547"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p608565317547"><a name="p608565317547"></a><a name="p608565317547"></a>output_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6530536017547"><a name="p6530536017547"></a><a name="p6530536017547"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5524276817547"><a name="p5524276817547"></a><a name="p5524276817547"></a>Output data source ID of a job object</p>
</td>
</tr>
<tr id="row4779481717637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4617494417637"><a name="p4617494417637"></a><a name="p4617494417637"></a>info</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2439775617637"><a name="p2439775617637"></a><a name="p2439775617637"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3006119217637"><a name="p3006119217637"></a><a name="p3006119217637"></a>Job object status information</p>
</td>
</tr>
<tr id="row1495495217648"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p339159817648"><a name="p339159817648"></a><a name="p339159817648"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p14268918171114"><a name="p14268918171114"></a><a name="p14268918171114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2443087417648"><a name="p2443087417648"></a><a name="p2443087417648"></a>Job object ID</p>
</td>
</tr>
<tr id="row2384662617658"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5252854817658"><a name="p5252854817658"></a><a name="p5252854817658"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p19786981171114"><a name="p19786981171114"></a><a name="p19786981171114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row305452361779"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p582450651779"><a name="p582450651779"></a><a name="p582450651779"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p25043732171114"><a name="p25043732171114"></a><a name="p25043732171114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p535623701779"><a name="p535623701779"></a><a name="p535623701779"></a>Job object creation time</p>
</td>
</tr>
<tr id="row3627093394233"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5226450094233"><a name="p5226450094233"></a><a name="p5226450094233"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p4820418094233"><a name="p4820418094233"></a><a name="p4820418094233"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1222448494233"><a name="p1222448494233"></a><a name="p1222448494233"></a>Job object update time</p>
</td>
</tr>
<tr id="row5667785094240"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2750313894240"><a name="p2750313894240"></a><a name="p2750313894240"></a>return_code</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p5946630494240"><a name="p5946630494240"></a><a name="p5946630494240"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5204131894240"><a name="p5204131894240"></a><a name="p5204131894240"></a>Response code after job execution</p>
</td>
</tr>
<tr id="row5615267117721"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5207250917721"><a name="p5207250917721"></a><a name="p5207250917721"></a>oozie_job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p35218413171114"><a name="p35218413171114"></a><a name="p35218413171114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5296742017721"><a name="p5296742017721"></a><a name="p5296742017721"></a>Workflow ID returned by Oozie</p>
</td>
</tr>
<tr id="row4660982117733"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1729913217733"><a name="p1729913217733"></a><a name="p1729913217733"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1851829617733"><a name="p1851829617733"></a><a name="p1851829617733"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p2358698017733"><a name="p2358698017733"></a><a name="p2358698017733"></a>Whether a job object is protected</p>
<a name="ul18949663162327"></a><a name="ul18949663162327"></a><ul id="ul18949663162327"><li>true</li><li>false</li></ul>
<p id="p56987367162327"><a name="p56987367162327"></a><a name="p56987367162327"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row2048741417746"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3546551417754"><a name="p3546551417754"></a><a name="p3546551417754"></a>input_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2280823617754"><a name="p2280823617754"></a><a name="p2280823617754"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3552784217754"><a name="p3552784217754"></a><a name="p3552784217754"></a>Input data source ID of a job object</p>
</td>
</tr>
<tr id="row36805501785"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4117938217811"><a name="p4117938217811"></a><a name="p4117938217811"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p6475407017811"><a name="p6475407017811"></a><a name="p6475407017811"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1058834117811"><a name="p1058834117811"></a><a name="p1058834117811"></a>Cluster ID</p>
</td>
</tr>
<tr id="row2196179617822"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3407507017822"><a name="p3407507017822"></a><a name="p3407507017822"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2691075917822"><a name="p2691075917822"></a><a name="p2691075917822"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3228784617822"><a name="p3228784617822"></a><a name="p3228784617822"></a>Whether a job object is public</p>
<a name="ul45445577141414"></a><a name="ul45445577141414"></a><ul id="ul45445577141414"><li>true</li><li>false</li></ul>
<p id="p14310885151440"><a name="p14310885151440"></a><a name="p14310885151440"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row2742286517547"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p665958717547"><a name="p665958717547"></a><a name="p665958717547"></a>job_configs</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p568200817547"><a name="p568200817547"></a><a name="p568200817547"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5758951617547"><a name="p5758951617547"></a><a name="p5758951617547"></a>Key-value pair set for saving job running configurations</p>
</td>
</tr>
<tr id="row3736230917853"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p644819317853"><a name="p644819317853"></a><a name="p644819317853"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2801293817853"><a name="p2801293817853"></a><a name="p2801293817853"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p5445552817853"><a name="p5445552817853"></a><a name="p5445552817853"></a>Job object ID</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    ```
    The request example of MapReduce job: 
    {        
        "cluster_id": "811e1134-666f-4c48-bc92-afb5b10c9d8c",          
        "input_id": "3e1bc8e6-8c69-4749-8e52-90d9341d15bc",          
        "output_id": "52146b52-6540-4aac-a024-fee253cf52a9",         
        "is_protected": false,         
        "is_public": false,         
        "job_configs": {            
            "configs": {                
               "mapred.map.tasks": "1",                  
               "mapred.reduce.tasks": "1"            
           },             
           "args": [                
               "wordcount",                 
               "arg2"            
           ],             
           "params": {                
              "param2": "value2",                 
              "param1": "value1"            
           }        
        }    
    } 
    
    The request example of Spark job: 
    { 
        "cluster_id": "8f3a547d-d53a-44ba-9aad-ded0b0b26e9c",  
        "input_id": "3e1bc8e6-8c69-4749-8e52-90d9341d15bc",  
        "output_id": "8bb0259f-309a-49f4-843b-0be86ac1623a",  
        "job_configs": { 
            "configs": { },  
            "args": [ 
                "org.apache.spark.examples.SparkPi 10",  
                "arg2" 
            ],  
            "params": { 
                "param2": "value2",  
                "param1": "value1" 
            } 
        }  
    }
    
    The request example of DistCp job:
    {        
        "cluster_id": "811e1134-666f-4c48-bc92-afb5b10c9d8c",          
        "input_id": "3e1bc8e6-8c69-4749-8e52-90d9341d15bc",          
        "output_id": "52146b52-6540-4aac-a024-fee253cf52a9",         
        "is_protected": false,         
        "is_public": false,         
        "job_configs": {            
            "configs": { },             
           "args": [                
               "arg1",                 
               "arg2"            
           ],             
           "params": {                
              "param2": "value2",                 
              "param1": "value1"            
           }        
        }    
    }
    
    The request example of Hive job:
    {        
        "cluster_id": "8f3a547d-d53a-44ba-9aad-ded0b0b26e9c",          
        "input_id": "3e1bc8e6-8c69-4749-8e52-90d9341d15bc",          
        "output_id": "8bb0259f-309a-49f4-843b-0be86ac1623a",         
        "is_protected": false,         
        "is_public": false,         
        "job_configs": {            
            "configs": { },             
           "args": [                
               "arg1",                 
               "arg2"            
           ],             
           "params": {                
              "param2": "value2",                 
              "param1": "value1"            
           }        
        }    
    }
    
    The request example of SparkScript job:
    {        
        "cluster_id": "811e1134-666f-4c48-bc92-afb5b10c9d8c",          
        "input_id": "3e1bc8e6-8c69-4749-8e52-90d9341d15bc",          
        "output_id": "52146b52-6540-4aac-a024-fee253cf52a9",         
        "is_protected": false,         
        "is_public": false,         
        "job_configs": {            
            "configs": { },             
           "args": [                
               "arg1",                 
               "arg2"            
           ],             
           "params": {                
              "param2": "value2",                 
              "param1": "value1"            
           }        
        }    
    }
    ```

-   Example response

    ```
    { 
        "job_execution":{ 
            "created_at":"2017-02-20T09:11:32", 
            "updated_at":"2017-02-20T09:11:32", 
            "id":"4a56525d-34db-43e3-99c9-af67491025cd", 
            "tenant_id":"3f99e3319a8943ceb15c584f3325d064", 
            "job_id":"2c12ff33-da22-47b1-b51f-2828c16bbad8", 
            "start_time":"2017-02-20T09:11:32", 
            "end_time":null, 
            "cluster_id":"c1000b4f-f2a1-49e1-af3c-2e19fc1eb72d", 
            "oozie_job_id":null, 
            "return_code":null, 
            "input_id":"ce8c2b04-f46c-4580-8b58-5b6aaf4a44a9", 
            "output_id":"9d59ce5b-d0f4-46d4-8738-6e50c2a5c68a", 
            "is_protected":null, 
            "is_public":null, 
            "job_configs":{ 
                "configs":{ 
                    "mapred.map.tasks":"1", 
                    "mapred.reduce.tasks":"1" 
                }, 
                "args":[ 
                    "wordcount ", 
                    "arg2" 
                ], 
                "params":{ 
                    "param2":"value2", 
                    "param1":"value1" 
                } 
            }, 
            "data_source_urls":null, 
            "info":null 
        } 
    }
    ```


## Status Code<a name="section7365446163631"></a>

[Table 4](#table1584477916050)  describes the status code of this API.

**Table  4**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The job object has been executed successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

