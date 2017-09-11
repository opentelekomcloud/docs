## Relationships with Other Services

-   EIPs need to be bound to required ECSs provided by the ECS service.

-   Elastic Load Balance (ELB) uses the EIP and bandwidth provided by the VPC
    service.

-   After the VPC service becomes available to you, you can use Cloud Eye (CES)
    to view monitored object status of the service without requiring additional
    plug-ins to be installed. <a href="#table1">Table 1</a> lists the VPC monitoring metrics
    supported by CES.

<a name="table1">**Table 1**</a> VPC monitoring metrics
<table>
      <tr>
         <th>Metric</th>
         <th>Definition</th>
         <th>Value Range</th>
         <th>Monitored Object</th>
     
     </tr>
     <tr>
        <td>Upstream bandwidth</td>
         <td>Specifies the outbound network rate of the monitored object.</td>
         <td>≥0bit/s</td>
         <td>Bandwidth or EIP</td>
       
     </tr>
     <tr>
         <td >Downstream bandwidth</td>
         <td>Specifies inbound network rate of the monitored object.</td>
         <td>≥0bit/s</td>
         <td>Bandwidth or EIP</td>
      
     </tr> 
     <tr>
        <td>Upstream Traffic</td>
         <td>Specifies the outbound network traffic of the monitored object.</td>
         <td>≥0Byte</td>
         <td>Bandwidth or EIP</td>
        
     </tr> 
     <tr>
         <td>Downstream Traffic</td>
         <td>Specifies the inbound network traffic of the monitored object.</td>
         <td>≥0Byte</td>
         <td>Bandwidth or EIP</td>
  
     </tr>
</table>
