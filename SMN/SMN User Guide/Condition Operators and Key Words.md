## Condition Operators and Key Words

### Condition operators

**Table 1** Condition operators
	<table>
    <tr>
       <th>Category</th>
       <th>Operator</th> 
	   <th>Description</th>
     </tr>
     <tr>
         <td rowspan = "6">String</td>
         <td>StringEquals</td>
		 <td>String matching, case-sensitive </td>
     </tr>
     <tr>
         <td>StringNotEquals </td>
		 <td>String excluding, case-sensitive </td>
     </tr>
	<tr>
         <td>StringEqualsIgnoreCase  </td>
		 <td>String matching, case-insensitive </td>
     </tr>
	<tr>
         <td>StringNotEqualsIgnoreCase</td>
		 <td>String excluding, case-insensitive </td>
     </tr>
	<tr>
         <td>StringLike  </td>
		 <td><dd>String matching</dd><dd>The value can contain one or more wildcard characters (\*). </dd></td>
     </tr>
	<tr>
         <td>StringNotLike </td>
		 <td><dd>String excluding</dd><dd>The value can contain one or more wildcard characters (\*). </dd></td>
     </tr>
	<tr>
         <td rowspan = "6">Numeric</td>
         <td>NumericEquals</td>
		 <td>Integer or decimal matching </td>
     </tr>
     <tr>
         <td>NumericNotEquals </td>
		 <td>Integer or decimal excluding </td>
     </tr>
	<tr>
         <td> NumericLessThan </td>
		 <td>Less than an integer or decimal </td>
     </tr>
	<tr>
         <td>NumericLessThanEquals </td>
		 <td>Less than or equal to an integer or decimal </td>
     </tr>
	<tr>
         <td>NumericGreaterThan </td>
		 <td>Greater than an integer or decimal</td>
     </tr>
	<tr>
         <td>NumericGreaterThanEquals</td>
		 <td>Greater than or equal to an integer or decimal </td>
     </tr>
	<tr>
         <td rowspan = "6">Date</td>
         <td>DateEquals</td>
		 <td>Date matching </td>
     </tr>
     <tr>
         <td>DateNotEquals </td>
		 <td>Date excluding </td>
     </tr>
	<tr>
         <td>DateLessThan</td>
		 <td>Earlier than a date or time point  </td>
     </tr>
	<tr>
         <td>DateLessThanEquals</td>
		 <td>Earlier than or equal to a date or time point</td>
     </tr>
	<tr>
         <td>DateGreaterThan   </td>
		 <td>Later than a date or time point</td>
     </tr>
	<tr>
         <td>DateGreaterThanEquals</td>
		 <td>Later than or equal to a date or time point</td>
     </tr>
     <tr>
         <td>Bool</td>
         <td>Bool</td>
		 <td>Boolean value matching</td>
     </tr>
     </table>   

### Condition key words

**Table 2** Condition key words
	<table>
    <tr>
       <th>Key Word </th>
       <th>Description</th>
     </tr>
     <tr>
         <td>csp:CurrentTime</td>
         <td>Current time</td>
     </tr>
     <tr>
         <td>smn:Protocol</td>
         <td>Protocol of a subscription, which is valid only for the SMN:Subscribe action</td>
     </tr>
     <tr>
         <td>smn:Endpoint </td>
         <td>Endpoint of a subscription, which is valid only for the SMN:Subscribe action</td>
     </tr>
     </table>   

### Condition example

    "Condition": {
				     "DateLessThan":{
								     "csp:CurrentTime":"2016-11-07T15:35:00Z"
								     },
				     "StringLike": {
								     "smn:Endpoint":["\*@gmail.com","\*@hotmail.com"]
								    }
    }
    