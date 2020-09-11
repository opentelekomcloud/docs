# API Overview<a name="EN-US_TOPIC_0172486224"></a>

[Table 1](#table40115147113128)  describes MRS APIs that meet RESTful API design standards.

[Table 2](#table521983381017)  lists MRS Manager APIs provided by MRS.

**Table  1**  APIs

<a name="table40115147113128"></a>
<table><thead align="left"><tr id="row25782208113128"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p66967018163957"><a name="p66967018163957"></a><a name="p66967018163957"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.2"><p id="p65482101113316"><a name="p65482101113316"></a><a name="p65482101113316"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p42729830113128"><a name="p42729830113128"></a><a name="p42729830113128"></a>API URI</p>
</th>
</tr>
</thead>
<tbody><tr id="row21342785113250"><td class="cellrowborder" rowspan="5" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1379423716407"><a name="p1379423716407"></a><a name="p1379423716407"></a>Data source APIs</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p2449951113316"><a name="p2449951113316"></a><a name="p2449951113316"></a><a href="creating-a-data-source.md">Creating a Data Source</a></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p31560570113552"><a name="p31560570113552"></a><a name="p31560570113552"></a>POST /v1.1/{project_id}/data-sources</p>
</td>
</tr>
<tr id="row52109770113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p64228362113316"><a name="p64228362113316"></a><a name="p64228362113316"></a><a href="updating-a-data-source.md">Updating a Data Source</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p56424544113552"><a name="p56424544113552"></a><a name="p56424544113552"></a>PUT /v1.1/{project_id}/data-sources/{data_source_id}</p>
</td>
</tr>
<tr id="row32255733113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p35114846113316"><a name="p35114846113316"></a><a name="p35114846113316"></a><a href="querying-the-data-source-list.md">Querying the Data Source List</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p62868253113552"><a name="p62868253113552"></a><a name="p62868253113552"></a>GET /v1.1/{project_id}/data-sources</p>
</td>
</tr>
<tr id="row38169714113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p25730241113316"><a name="p25730241113316"></a><a name="p25730241113316"></a><a href="querying-the-data-source-details.md">Querying the Data Source Details</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p62711668113552"><a name="p62711668113552"></a><a name="p62711668113552"></a>GET /v1.1/{project_id}/data-sources/{data_source_id}</p>
</td>
</tr>
<tr id="row11048509113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p3774814113316"><a name="p3774814113316"></a><a name="p3774814113316"></a><a href="deleting-a-data-source.md">Deleting a Data Source</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p15670193113552"><a name="p15670193113552"></a><a name="p15670193113552"></a>DELETE /v1.1/{project_id}/data-sources/{data_source_id}</p>
</td>
</tr>
<tr id="row1799257113250"><td class="cellrowborder" rowspan="6" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p4343069164024"><a name="p4343069164024"></a><a name="p4343069164024"></a>Cluster management APIs</p>
<p id="p996614414049"><a name="p996614414049"></a><a name="p996614414049"></a></p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p3141141155619"><a name="p3141141155619"></a><a name="p3141141155619"></a><a href="creating-a-cluster-and-running-a-job.md">Creating a Cluster and Running a Job</a></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p15063909113552"><a name="p15063909113552"></a><a name="p15063909113552"></a>POST /v1.1/{project_id}/run-job-flow</p>
</td>
</tr>
<tr id="row32368530113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p3386208113316"><a name="p3386208113316"></a><a name="p3386208113316"></a><a href="resizing-a-cluster.md">Resizing a Cluster</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p42845229113552"><a name="p42845229113552"></a><a name="p42845229113552"></a>PUT /v1.1/{project_id}/cluster_infos/{cluster_id}</p>
</td>
</tr>
<tr id="row4868154113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p5847446113316"><a name="p5847446113316"></a><a name="p5847446113316"></a><a href="querying-a-cluster-list.md">Querying a Cluster List</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p28550250113552"><a name="p28550250113552"></a><a name="p28550250113552"></a>GET /v1.1/{project_id}/cluster_infos</p>
</td>
</tr>
<tr id="row16238315113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p3881124113316"><a name="p3881124113316"></a><a name="p3881124113316"></a><a href="querying-cluster-details.md">Querying Cluster Details</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p9384969113552"><a name="p9384969113552"></a><a name="p9384969113552"></a>GET /v1.1/{project_id}/cluster_infos/{cluster_id}</p>
</td>
</tr>
<tr id="row10682186113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p45935667113316"><a name="p45935667113316"></a><a name="p45935667113316"></a><a href="deleting-a-cluster.md">Deleting a Cluster</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p63647548113552"><a name="p63647548113552"></a><a name="p63647548113552"></a>DELETE /v1.1/{project_id}/clusters/{cluster_id}</p>
</td>
</tr>
<tr id="row1707908314049"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p4860437614049"><a name="p4860437614049"></a><a name="p4860437614049"></a><a href="querying-a-host-list.md">Querying a Host List</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2640899717716"><a name="p2640899717716"></a><a name="p2640899717716"></a>GET /v1.1/{project_id}/clusters/{cluster_id}/hosts</p>
</td>
</tr>
<tr id="row27094209113250"><td class="cellrowborder" rowspan="5" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p41354182164040"><a name="p41354182164040"></a><a name="p41354182164040"></a>Job binary object APIs</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p29801579113316"><a name="p29801579113316"></a><a name="p29801579113316"></a><a href="creating-a-job-binary-object.md">Creating a Job Binary Object</a></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p26837822113552"><a name="p26837822113552"></a><a name="p26837822113552"></a>POST /v1.1/{project_id}/job-binaries</p>
</td>
</tr>
<tr id="row38007108113250"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p65117683113316"><a name="p65117683113316"></a><a name="p65117683113316"></a><a href="updating-a-job-binary-object.md">Updating a Job Binary Object</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p36093202113552"><a name="p36093202113552"></a><a name="p36093202113552"></a>PUT /v1.1/{project_id}/job-binaries/{job_binary_id}</p>
</td>
</tr>
<tr id="row45767088113240"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p40040947113316"><a name="p40040947113316"></a><a name="p40040947113316"></a><a href="querying-the-binary-object-list.md">Querying the Binary Object List</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p5270084113552"><a name="p5270084113552"></a><a name="p5270084113552"></a>GET /v1.1/{project_id}/job-binaries</p>
</td>
</tr>
<tr id="row41379403113240"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p22091284113316"><a name="p22091284113316"></a><a name="p22091284113316"></a><a href="querying-the-binary-object-details.md">Querying the Binary Object Details</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p16685989113552"><a name="p16685989113552"></a><a name="p16685989113552"></a>GET /v1.1/{project_id}/job-binaries/{job_binary_id}</p>
</td>
</tr>
<tr id="row24994487113240"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p44563581113316"><a name="p44563581113316"></a><a name="p44563581113316"></a><a href="deleting-a-job-binary-object.md">Deleting a Job Binary Object</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p17381905113552"><a name="p17381905113552"></a><a name="p17381905113552"></a>DELETE /v1.1/{project_id}/job-binaries/{job_binary_id}</p>
</td>
</tr>
<tr id="row45876160113240"><td class="cellrowborder" rowspan="9" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p52410202164056"><a name="p52410202164056"></a><a name="p52410202164056"></a>Job object APIs (V1)</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p52880343113316"><a name="p52880343113316"></a><a name="p52880343113316"></a><a href="adding-a-job-and-executing-the-job.md">Adding a Job and Executing the Job</a></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p54943020113552"><a name="p54943020113552"></a><a name="p54943020113552"></a>POST /v1.1/{project_id}/jobs/submit-job</p>
</td>
</tr>
<tr id="row25187768113240"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p55449418113316"><a name="p55449418113316"></a><a name="p55449418113316"></a><a href="creating-a-job-object.md">Creating a Job Object</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p56579104113552"><a name="p56579104113552"></a><a name="p56579104113552"></a>POST /v1.1/{project_id}/jobs</p>
</td>
</tr>
<tr id="row62070073113240"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p62217853113316"><a name="p62217853113316"></a><a name="p62217853113316"></a><a href="updating-a-job-object.md">Updating a Job Object</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p41324640113552"><a name="p41324640113552"></a><a name="p41324640113552"></a>PATCH /v1.1/{project_id}/jobs/{job_id}</p>
</td>
</tr>
<tr id="row32912001113212"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p6481304113316"><a name="p6481304113316"></a><a name="p6481304113316"></a><a href="executing-a-job-object.md">Executing a Job Object</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p60891751113552"><a name="p60891751113552"></a><a name="p60891751113552"></a>POST /v1.1/{project_id}/jobs/{job_id}/execute</p>
</td>
</tr>
<tr id="row30907327113226"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p55223620113316"><a name="p55223620113316"></a><a name="p55223620113316"></a><a href="querying-the-job-object-list.md">Querying the Job Object List</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p31127672113552"><a name="p31127672113552"></a><a name="p31127672113552"></a>GET /v1.1/{project_id}/jobs</p>
</td>
</tr>
<tr id="row1339468311333"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p43928232113316"><a name="p43928232113316"></a><a name="p43928232113316"></a><a href="querying-job-object-details.md">Querying Job Object Details</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p9277278113552"><a name="p9277278113552"></a><a name="p9277278113552"></a>GET /v1.1/{project_id}/jobs/{job_id}</p>
</td>
</tr>
<tr id="row1187432111333"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1417069113316"><a name="p1417069113316"></a><a name="p1417069113316"></a><a href="querying-the-exe-object-list-of-jobs.md">Querying the exe Object List of Jobs</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p52249901113552"><a name="p52249901113552"></a><a name="p52249901113552"></a>GET /v1.1/{project_id}/job-exes</p>
</td>
</tr>
<tr id="row1308011611333"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p47673787113316"><a name="p47673787113316"></a><a name="p47673787113316"></a><a href="querying-exe-object-details.md">Querying exe Object Details</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p39452158113552"><a name="p39452158113552"></a><a name="p39452158113552"></a>GET /v1.1/{project_id}/job-exes/{job_exe_id}</p>
</td>
</tr>
<tr id="row2618619111333"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p36371513113316"><a name="p36371513113316"></a><a name="p36371513113316"></a><a href="deleting-a-job-object.md">Deleting a Job Object</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p38030006113552"><a name="p38030006113552"></a><a name="p38030006113552"></a>DELETE /v1.1/{project_id}/jobs/{job_id}</p>
</td>
</tr>
<tr id="row8349212113226"><td class="cellrowborder" rowspan="4" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p25685506164126"><a name="p25685506164126"></a><a name="p25685506164126"></a>Job execution object APIs (V1)</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p60411407113316"><a name="p60411407113316"></a><a name="p60411407113316"></a><a href="querying-the-job-execution-object-list.md">Querying the Job Execution Object List</a></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p7913919113552"><a name="p7913919113552"></a><a name="p7913919113552"></a>GET /v1.1/{project_id}/job-executions</p>
</td>
</tr>
<tr id="row60263068113232"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p61485798113316"><a name="p61485798113316"></a><a name="p61485798113316"></a><a href="querying-job-execution-object-details.md">Querying Job Execution Object Details</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p64993740113552"><a name="p64993740113552"></a><a name="p64993740113552"></a>GET /v1.1/{project_id}/job-executions/{job_execution_id}</p>
</td>
</tr>
<tr id="row40085181113232"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p14293733113316"><a name="p14293733113316"></a><a name="p14293733113316"></a><a href="canceling-job-execution.md">Canceling Job Execution</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1578648113552"><a name="p1578648113552"></a><a name="p1578648113552"></a>GET /v1.1/{project_id}/job-executions/{job_execution_id}/cancel</p>
</td>
</tr>
<tr id="row8001600113232"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p16941749113316"><a name="p16941749113316"></a><a name="p16941749113316"></a><a href="deleting-a-job-execution-object.md">Deleting a Job Execution Object</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p9983910113552"><a name="p9983910113552"></a><a name="p9983910113552"></a>DELETE /v1.1/{project_id}/job-executions/{job_execution_id}</p>
</td>
</tr>
<tr id="row11264052121116"><td class="cellrowborder" rowspan="6" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p19804146131012"><a name="p19804146131012"></a><a name="p19804146131012"></a>Job object APIs (V2)</p>
<p id="p198241546151010"><a name="p198241546151010"></a><a name="p198241546151010"></a></p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p13804746111018"><a name="p13804746111018"></a><a name="p13804746111018"></a><a href="adding-and-executing-a-job.md">Adding and Executing a Job</a></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p7804746171010"><a name="p7804746171010"></a><a name="p7804746171010"></a>POST /v2/{project_id}/clusters/{cluster_id}/job-executions</p>
</td>
</tr>
<tr id="row1450935214111"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p280410468107"><a name="p280410468107"></a><a name="p280410468107"></a><a href="querying-information-about-a-job.md">Querying Information About a Job</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p980412465101"><a name="p980412465101"></a><a name="p980412465101"></a>GET /v2/{project_id}/clusters/{cluster_id}/job-executions</p>
</td>
</tr>
<tr id="row17755105251118"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p20804046191018"><a name="p20804046191018"></a><a name="p20804046191018"></a><a href="querying-a-list-of-jobs.md">Querying a List of Jobs</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p16804154651020"><a name="p16804154651020"></a><a name="p16804154651020"></a>GET /v2/{project_id}/clusters/{cluster_id}/job-executions</p>
</td>
</tr>
<tr id="row14992852141118"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p188044468104"><a name="p188044468104"></a><a name="p188044468104"></a><a href="terminating-a-job.md">Terminating a Job</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p58047466100"><a name="p58047466100"></a><a name="p58047466100"></a>POST /v2/{project_id}/clusters/{cluster_id}/job-executions/{job_execution_id}/kill</p>
</td>
</tr>
<tr id="row1927515315118"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p28047463101"><a name="p28047463101"></a><a name="p28047463101"></a><a href="deleting-jobs-in-batches.md">Deleting Jobs in Batches</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p78041546201014"><a name="p78041546201014"></a><a name="p78041546201014"></a>POST /v2/{project_id}/clusters/{cluster_id}/job-executions/batch-delete</p>
</td>
</tr>
<tr id="row145612053171119"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p168040465103"><a name="p168040465103"></a><a name="p168040465103"></a><a href="obtain-the-sql-result.md">Obtain the SQL Result</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p138051746201012"><a name="p138051746201012"></a><a name="p138051746201012"></a>GET /v2/{project_id}/clusters/{cluster_id}/job-executions/{job_execution_id}/sql-result</p>
</td>
</tr>
<tr id="row55246335103424"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p3022179117221"><a name="p3022179117221"></a><a name="p3022179117221"></a>Auto scaling APIs</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p40261454103435"><a name="p40261454103435"></a><a name="p40261454103435"></a><a href="configuring-an-auto-scaling-rule.md">Configuring an Auto Scaling Rule</a></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p24026536103435"><a name="p24026536103435"></a><a name="p24026536103435"></a>POST /v1.1/{project_id}/autoscaling-policy/{cluster_id}</p>
</td>
</tr>
<tr id="row4997174174913"><td class="cellrowborder" rowspan="6" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p10417204611498"><a name="p10417204611498"></a><a name="p10417204611498"></a>Tag management APIs</p>
<p id="p104291846174918"><a name="p104291846174918"></a><a name="p104291846174918"></a></p>
<p id="p1942814468497"><a name="p1942814468497"></a><a name="p1942814468497"></a></p>
<p id="p44281546114915"><a name="p44281546114915"></a><a name="p44281546114915"></a></p>
<p id="p63723459493"><a name="p63723459493"></a><a name="p63723459493"></a></p>
<p id="p18233321195014"><a name="p18233321195014"></a><a name="p18233321195014"></a></p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p144619242504"><a name="p144619242504"></a><a name="p144619242504"></a><a href="adding-a-tag-to-a-specified-cluster.md">Adding a Tag to a Specified Cluster</a></p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p846010246502"><a name="p846010246502"></a><a name="p846010246502"></a>POST /v1.1/{project_id}/clusters/{cluster_id}/tags</p>
</td>
</tr>
<tr id="row235394434911"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p104591224195016"><a name="p104591224195016"></a><a name="p104591224195016"></a><a href="deleting-a-tag-of-a-specified-cluster.md">Deleting a Tag of a Specified Cluster</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p11459102405017"><a name="p11459102405017"></a><a name="p11459102405017"></a>DELETE /v1.1/{project_id}/clusters/{cluster_id}/tags/{key}</p>
</td>
</tr>
<tr id="row17600344144920"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p134171446184913"><a name="p134171446184913"></a><a name="p134171446184913"></a><a href="querying-tags-of-a-specified-cluster.md">Querying Tags of a Specified Cluster</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1841774624918"><a name="p1841774624918"></a><a name="p1841774624918"></a>GET /v1.1/{project_id}/clusters/{cluster_id}/tags</p>
</td>
</tr>
<tr id="row7850164474912"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p2418546104918"><a name="p2418546104918"></a><a name="p2418546104918"></a><a href="adding-or-deleting-cluster-tags-in-batches.md">Adding or Deleting Cluster Tags in Batches</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p8418154624915"><a name="p8418154624915"></a><a name="p8418154624915"></a>POST /v1.1/{project_id}/clusters/{cluster_id}/tags/action</p>
</td>
</tr>
<tr id="row183721345154911"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p15418346104910"><a name="p15418346104910"></a><a name="p15418346104910"></a><a href="querying-all-tags.md">Querying All Tags</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p7418346144919"><a name="p7418346144919"></a><a name="p7418346144919"></a>GET /v1.1/{project_id}/clusters/tags</p>
</td>
</tr>
<tr id="row623310213506"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p10418184644916"><a name="p10418184644916"></a><a name="p10418184644916"></a><a href="querying-a-list-of-clusters-with-specified-tags.md">Querying a List of Clusters with Specified Tags</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p541934634915"><a name="p541934634915"></a><a name="p541934634915"></a>POST /v1.1/{project_id}/clusters/resource_instances/action</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  MRS Manager API

<a name="table521983381017"></a>
<table><thead align="left"><tr id="row7230733161014"><th class="cellrowborder" valign="top" width="19.79%" id="mcps1.2.4.1.1"><p id="p62321133131017"><a name="p62321133131017"></a><a name="p62321133131017"></a>API</p>
</th>
<th class="cellrowborder" valign="top" width="30.270000000000003%" id="mcps1.2.4.1.2"><p id="p32348330106"><a name="p32348330106"></a><a name="p32348330106"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="49.94%" id="mcps1.2.4.1.3"><p id="p1323614339103"><a name="p1323614339103"></a><a name="p1323614339103"></a>API URI</p>
</th>
</tr>
</thead>
<tbody><tr id="row853143310109"><td class="cellrowborder" rowspan="2" valign="top" width="19.79%" headers="mcps1.2.4.1.1 "><p id="p953511338102"><a name="p953511338102"></a><a name="p953511338102"></a>MRS Manager CAS API</p>
</td>
<td class="cellrowborder" valign="top" width="30.270000000000003%" headers="mcps1.2.4.1.2 "><p id="p75387333103"><a name="p75387333103"></a><a name="p75387333103"></a><a href="logging-in-to-the-cas.md">Logging In to the CAS</a></p>
</td>
<td class="cellrowborder" valign="top" width="49.94%" headers="mcps1.2.4.1.3 "><p id="p18542123313102"><a name="p18542123313102"></a><a name="p18542123313102"></a>POST /cas/login</p>
</td>
</tr>
<tr id="row95431033121010"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p254513339101"><a name="p254513339101"></a><a name="p254513339101"></a><a href="logging-out-of-the-cas.md">Logging Out of the CAS</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p17548193312101"><a name="p17548193312101"></a><a name="p17548193312101"></a>POST /cas/logout</p>
</td>
</tr>
<tr id="row954913351017"><td class="cellrowborder" rowspan="11" valign="top" width="19.79%" headers="mcps1.2.4.1.1 "><p id="p5551133320106"><a name="p5551133320106"></a><a name="p5551133320106"></a>MRS Manager WEB API</p>
</td>
<td class="cellrowborder" valign="top" width="30.270000000000003%" headers="mcps1.2.4.1.2 "><p id="p755463341017"><a name="p755463341017"></a><a name="p755463341017"></a><a href="checking-the-login.md">Checking the Login</a></p>
</td>
<td class="cellrowborder" valign="top" width="49.94%" headers="mcps1.2.4.1.3 "><p id="p10557103312101"><a name="p10557103312101"></a><a name="p10557103312101"></a>GET /web/v1/access/login_check</p>
</td>
</tr>
<tr id="row1655853391012"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p14560103314106"><a name="p14560103314106"></a><a name="p14560103314106"></a><a href="modifying-the-password-of-the-current-login-user.md">Modifying the Password of the Current Login User</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p155631331104"><a name="p155631331104"></a><a name="p155631331104"></a>POST /web/v1/access/modify_self_password</p>
</td>
</tr>
<tr id="row11565033131012"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p185672338104"><a name="p185672338104"></a><a name="p185672338104"></a><a href="querying-the-health-status-of-a-specified-cluster.md">Querying the Health Status of a Specified Cluster</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p205712333104"><a name="p205712333104"></a><a name="p205712333104"></a>GET /web/v1/cluster/{cluster_id}/status</p>
</td>
</tr>
<tr id="row17572163317101"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p8574153318105"><a name="p8574153318105"></a><a name="p8574153318105"></a><a href="querying-basic-information-about-a-specified-cluster.md">Querying Basic Information About a Specified Cluster</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p125771833121018"><a name="p125771833121018"></a><a name="p125771833121018"></a>GET /web/v1/clusters</p>
</td>
</tr>
<tr id="row457943371012"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1058293311107"><a name="p1058293311107"></a><a name="p1058293311107"></a><a href="querying-the-command-execution-progress.md">Querying the Command Execution Progress</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p158610333109"><a name="p158610333109"></a><a name="p158610333109"></a>GET /web/v1/common/command/{command_id}/progress</p>
</td>
</tr>
<tr id="row458718330106"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p658910332107"><a name="p658910332107"></a><a name="p658910332107"></a><a href="saving-configurations.md">Saving Configurations</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p459116334109"><a name="p459116334109"></a><a name="p459116334109"></a>POST /web/v1/config/cluster/{cluster_id}/save</p>
</td>
</tr>
<tr id="row75925332107"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p16595333141010"><a name="p16595333141010"></a><a name="p16595333141010"></a><a href="logging-out-of-a-session.md">Logging Out Of a Session</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p56001733141011"><a name="p56001733141011"></a><a name="p56001733141011"></a>GET /web/v1/logout_action</p>
</td>
</tr>
<tr id="row19601193371016"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p86031133161015"><a name="p86031133161015"></a><a name="p86031133161015"></a><a href="starting-a-service.md">Starting a Service</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p66061133131011"><a name="p66061133131011"></a><a name="p66061133131011"></a>POST /web/v1/maintain/cluster/{cluster_id}/service/{service_name}/start</p>
</td>
</tr>
<tr id="row1608173310107"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p56091533141012"><a name="p56091533141012"></a><a name="p56091533141012"></a><a href="stopping-a-service.md">Stopping a Service</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p56131933131012"><a name="p56131933131012"></a><a name="p56131933131012"></a>POST /web/v1/maintain/cluster/{cluster_id}/service/{service_name}/stop</p>
</td>
</tr>
<tr id="row19614113321012"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p261714335109"><a name="p261714335109"></a><a name="p261714335109"></a><a href="querying-monitoring-data.md">Querying Monitoring Data</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1561920334106"><a name="p1561920334106"></a><a name="p1561920334106"></a>GET /web/v1/monitor/metrics_info</p>
</td>
</tr>
<tr id="row1262110335103"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p6623183391010"><a name="p6623183391010"></a><a name="p6623183391010"></a><a href="querying-summary-of-a-specified-service.md">Querying Summary of a Specified Service</a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p862793311015"><a name="p862793311015"></a><a name="p862793311015"></a>GET /web/v1/cluster/{cluster_id}/services/{service_name}</p>
</td>
</tr>
</tbody>
</table>

