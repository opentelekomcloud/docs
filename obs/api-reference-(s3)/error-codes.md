# Error Codes<a name="EN-US_TOPIC_0125560440"></a>

If a request fails to be processed due to errors, an error response is returned. An error response contains an error code and error details.  [Table 1](#table30733758)  describes all error codes in OBS error responses.

**Table  1**  List of OBS error codes

<a name="table30733758"></a>
<table><thead align="left"><tr id="row64297212"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p40691653"><a name="p40691653"></a><a name="p40691653"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p7689558"><a name="p7689558"></a><a name="p7689558"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18874456"><a name="p18874456"></a><a name="p18874456"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row52435954"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19453901"><a name="p19453901"></a><a name="p19453901"></a>AccessDenied</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32262161"><a name="p32262161"></a><a name="p32262161"></a>Access denied.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p63098212"><a name="p63098212"></a><a name="p63098212"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row4161693416399"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1552848716399"><a name="p1552848716399"></a><a name="p1552848716399"></a>AccessForbidden</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4984790016399"><a name="p4984790016399"></a><a name="p4984790016399"></a>Insufficient permission.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1114807716399"><a name="p1114807716399"></a><a name="p1114807716399"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row31013004"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29025404"><a name="p29025404"></a><a name="p29025404"></a>AccountProblem</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2247504"><a name="p2247504"></a><a name="p2247504"></a>The operation cannot be successfully performed because your OBS account is abnormal, for example, expired or frozen.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p47830129"><a name="p47830129"></a><a name="p47830129"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row20164374162251"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p22701588162251"><a name="p22701588162251"></a><a name="p22701588162251"></a>AllAccessDisabled</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4403858616233"><a name="p4403858616233"></a><a name="p4403858616233"></a>The user has no permission to perform a specific operation.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30553150162251"><a name="p30553150162251"></a><a name="p30553150162251"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row27817977"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38663671"><a name="p38663671"></a><a name="p38663671"></a>AmbiguousGrantByEmailAddress</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44749686"><a name="p44749686"></a><a name="p44749686"></a>The specified email address is associated with multiple accounts.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p845982"><a name="p845982"></a><a name="p845982"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row7613840"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12741319"><a name="p12741319"></a><a name="p12741319"></a>BadDigest</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25413947"><a name="p25413947"></a><a name="p25413947"></a>The specified value of <strong id="b16166114118544"><a name="b16166114118544"></a><a name="b16166114118544"></a>Content-MD5</strong> does not match the value received by OBS.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4721264"><a name="p4721264"></a><a name="p4721264"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row43581222162359"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p40418098162359"><a name="p40418098162359"></a><a name="p40418098162359"></a>BadDomainName</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p676212816248"><a name="p676212816248"></a><a name="p676212816248"></a>Invalid domain name.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36022299162359"><a name="p36022299162359"></a><a name="p36022299162359"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row44715074162331"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p65151241162331"><a name="p65151241162331"></a><a name="p65151241162331"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p57830927162341"><a name="p57830927162341"></a><a name="p57830927162341"></a>Invalid request parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40939960162331"><a name="p40939960162331"></a><a name="p40939960162331"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row42491384"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19250065"><a name="p19250065"></a><a name="p19250065"></a>BucketAlreadyExists</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15751431"><a name="p15751431"></a><a name="p15751431"></a>The requested bucket name already exists. The bucket namespace is shared by all users of OBS. Specify a different name and retry.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p797505"><a name="p797505"></a><a name="p797505"></a>409 Conflict</p>
</td>
</tr>
<tr id="row7177547"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p44510439"><a name="p44510439"></a><a name="p44510439"></a>BucketAlreadyOwnedByYou</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p48575803"><a name="p48575803"></a><a name="p48575803"></a>Your previous request for creating the named bucket succeeded and you already own it.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p42326000"><a name="p42326000"></a><a name="p42326000"></a>409 Conflict</p>
</td>
</tr>
<tr id="row1854035917256"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2537414417256"><a name="p2537414417256"></a><a name="p2537414417256"></a>BucketExpanding</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4203978917256"><a name="p4203978917256"></a><a name="p4203978917256"></a>Indicates that the specified bucket is being expanded.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4977976717256"><a name="p4977976717256"></a><a name="p4977976717256"></a>409 Conflict</p>
</td>
</tr>
<tr id="row45389686"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p52685983"><a name="p52685983"></a><a name="p52685983"></a>BucketNotEmpty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p39706236"><a name="p39706236"></a><a name="p39706236"></a>The bucket that you tried to delete is not empty.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62088566"><a name="p62088566"></a><a name="p62088566"></a>409 Conflict</p>
</td>
</tr>
<tr id="row54648025162430"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p64413922162430"><a name="p64413922162430"></a><a name="p64413922162430"></a>CustomDomainAreadyExist</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p58135650162438"><a name="p58135650162438"></a><a name="p58135650162438"></a>The configured domain already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35226364162430"><a name="p35226364162430"></a><a name="p35226364162430"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row53109718162555"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6919924162555"><a name="p6919924162555"></a><a name="p6919924162555"></a>CustomDomainNotExist</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1130184416265"><a name="p1130184416265"></a><a name="p1130184416265"></a>The domain to be operated does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36030440162555"><a name="p36030440162555"></a><a name="p36030440162555"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row21926185"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p31190552"><a name="p31190552"></a><a name="p31190552"></a>CredentialsNotSupported</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p43406808"><a name="p43406808"></a><a name="p43406808"></a>This request does not support security credentials.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26290577"><a name="p26290577"></a><a name="p26290577"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row41677095162624"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20401497162624"><a name="p20401497162624"></a><a name="p20401497162624"></a>DeregisterUserId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p33047202162634"><a name="p33047202162634"></a><a name="p33047202162634"></a>The user has been deregistered.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39151524162624"><a name="p39151524162624"></a><a name="p39151524162624"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row35288602"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39804474"><a name="p39804474"></a><a name="p39804474"></a>EntityTooSmall</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2936934"><a name="p2936934"></a><a name="p2936934"></a>The size of the object to be uploaded exceeds the lower limit.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36565127"><a name="p36565127"></a><a name="p36565127"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row60650695"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13759282"><a name="p13759282"></a><a name="p13759282"></a>EntityTooLarge</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40760070"><a name="p40760070"></a><a name="p40760070"></a>The size of the object to be uploaded exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13231337"><a name="p13231337"></a><a name="p13231337"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row30186067162657"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29152345162657"><a name="p29152345162657"></a><a name="p29152345162657"></a>FrozenUserId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5286137116276"><a name="p5286137116276"></a><a name="p5286137116276"></a>The user has been frozen.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8279308162657"><a name="p8279308162657"></a><a name="p8279308162657"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row4953199162734"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p65664843162734"><a name="p65664843162734"></a><a name="p65664843162734"></a>IllegalLocationConstraintException</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17252063162734"><a name="p17252063162734"></a><a name="p17252063162734"></a>The configured region limitation is inconsistent with the region where it resides.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55239892162734"><a name="p55239892162734"></a><a name="p55239892162734"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row51973177"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49077817"><a name="p49077817"></a><a name="p49077817"></a>IllegalVersioning ConfigurationException</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15880221"><a name="p15880221"></a><a name="p15880221"></a>The Versioning configuration specified in the request is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11229518"><a name="p11229518"></a><a name="p11229518"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row15113052185426"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16197690185426"><a name="p16197690185426"></a><a name="p16197690185426"></a>InArrearOrInsufficientBalance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36944517185426"><a name="p36944517185426"></a><a name="p36944517185426"></a>Insufficient permission to perform a specific operation in ACL.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39715876185426"><a name="p39715876185426"></a><a name="p39715876185426"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row33956798"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p66146124"><a name="p66146124"></a><a name="p66146124"></a>IncompleteBody</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3529134619300"><a name="p3529134619300"></a><a name="p3529134619300"></a>Incomplete request body.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p59540653"><a name="p59540653"></a><a name="p59540653"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row66103835"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p52810395"><a name="p52810395"></a><a name="p52810395"></a>IncorrectNumberOf FilesInPostRequest</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49783612"><a name="p49783612"></a><a name="p49783612"></a>Each POST request must contain one file to be uploaded.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5940773"><a name="p5940773"></a><a name="p5940773"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row53466965"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p35856894"><a name="p35856894"></a><a name="p35856894"></a>InlineDataTooLarge</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18727300"><a name="p18727300"></a><a name="p18727300"></a>The size of inline data exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40516302"><a name="p40516302"></a><a name="p40516302"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row5430443171114"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13916298171119"><a name="p13916298171119"></a><a name="p13916298171119"></a>InsufficientStorageSpace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53478390171119"><a name="p53478390171119"></a><a name="p53478390171119"></a>Insufficient storage space</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36782301171119"><a name="p36782301171119"></a><a name="p36782301171119"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row29102400"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8484204"><a name="p8484204"></a><a name="p8484204"></a>InternalError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16131920"><a name="p16131920"></a><a name="p16131920"></a>An internal error occurs. Retry later</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p31617173"><a name="p31617173"></a><a name="p31617173"></a>500 Internal Server Error</p>
</td>
</tr>
<tr id="row16119107"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p30579324"><a name="p30579324"></a><a name="p30579324"></a>InvalidAccessKeyId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61006185"><a name="p61006185"></a><a name="p61006185"></a>The provided OBS AK does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p42553971"><a name="p42553971"></a><a name="p42553971"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row47441422"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17549965"><a name="p17549965"></a><a name="p17549965"></a>InvalidAddressingHeader</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12261085"><a name="p12261085"></a><a name="p12261085"></a>The anonymous role must be specified.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53623846"><a name="p53623846"></a><a name="p53623846"></a>N/A</p>
</td>
</tr>
<tr id="row12852567"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p34424967"><a name="p34424967"></a><a name="p34424967"></a>InvalidArgument</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36958915"><a name="p36958915"></a><a name="p36958915"></a>Invalid Argument.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40882164"><a name="p40882164"></a><a name="p40882164"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row62334838162822"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15957156162822"><a name="p15957156162822"></a><a name="p15957156162822"></a>InvalidBucket</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17461270162822"><a name="p17461270162822"></a><a name="p17461270162822"></a>The bucket to be accessed does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5076789162822"><a name="p5076789162822"></a><a name="p5076789162822"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row32395164"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6762647"><a name="p6762647"></a><a name="p6762647"></a>InvalidBucketName</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10903547"><a name="p10903547"></a><a name="p10903547"></a>The specified bucket name is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10772078"><a name="p10772078"></a><a name="p10772078"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row60137811162849"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39324561162849"><a name="p39324561162849"></a><a name="p39324561162849"></a>InvalidBucketState</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63497875162859"><a name="p63497875162859"></a><a name="p63497875162859"></a>Invalid bucket status.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p41975618162849"><a name="p41975618162849"></a><a name="p41975618162849"></a>409 Conflict</p>
</td>
</tr>
<tr id="row41356138163012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p61512896163012"><a name="p61512896163012"></a><a name="p61512896163012"></a>InvalidBucketStoragePolicy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18311707163021"><a name="p18311707163021"></a><a name="p18311707163021"></a>An invalid new policy is specified during bucket policy modification.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60515229163012"><a name="p60515229163012"></a><a name="p60515229163012"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row29839846"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1108470"><a name="p1108470"></a><a name="p1108470"></a>InvalidDigest</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p22677226"><a name="p22677226"></a><a name="p22677226"></a>The specified <strong id="b2768445"><a name="b2768445"></a><a name="b2768445"></a>Content-MD5</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22917507"><a name="p22917507"></a><a name="p22917507"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row42095675162511"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p54306539162511"><a name="p54306539162511"></a><a name="p54306539162511"></a>InvalidEncryptionAlgorithmError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p26712506162531"><a name="p26712506162531"></a><a name="p26712506162531"></a>Incorrect encryption algorithm.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p24248029162511"><a name="p24248029162511"></a><a name="p24248029162511"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row4930976"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p63864753"><a name="p63864753"></a><a name="p63864753"></a>InvalidLocationConstraint</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5662536"><a name="p5662536"></a><a name="p5662536"></a>The specified location constraint is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p56012234"><a name="p56012234"></a><a name="p56012234"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row59372154145128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15344892145142"><a name="p15344892145142"></a><a name="p15344892145142"></a>InvalidObjectState</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34976701145142"><a name="p34976701145142"></a><a name="p34976701145142"></a>Invalid object status. The error message is displayed when cold objects are not restored or being restored, or when non-cold objects are restored.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14540527145142"><a name="p14540527145142"></a><a name="p14540527145142"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row34348064"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p30729776"><a name="p30729776"></a><a name="p30729776"></a>InvalidPart</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6083937"><a name="p6083937"></a><a name="p6083937"></a>One or more specified parts cannot be found. The parts may not be uploaded or the specified entity tags (ETags) do not match the parts' ETags.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p23036890"><a name="p23036890"></a><a name="p23036890"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row6005426"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16677483"><a name="p16677483"></a><a name="p16677483"></a>InvalidPartOrder</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8698881"><a name="p8698881"></a><a name="p8698881"></a>Parts are not listed in ascending order by part number.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33520731"><a name="p33520731"></a><a name="p33520731"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row33251125"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8986609"><a name="p8986609"></a><a name="p8986609"></a>InvalidPayer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p56826725"><a name="p56826725"></a><a name="p56826725"></a>All access to this object is disabled.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39562042"><a name="p39562042"></a><a name="p39562042"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row20514064"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p51026521"><a name="p51026521"></a><a name="p51026521"></a>InvalidPolicyDocument</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p39507542"><a name="p39507542"></a><a name="p39507542"></a>The content of the form does not meet the conditions specified in the policy document.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p45994352"><a name="p45994352"></a><a name="p45994352"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row11295987"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42559746"><a name="p42559746"></a><a name="p42559746"></a>InvalidRange</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p24787426"><a name="p24787426"></a><a name="p24787426"></a>The requested range is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61624507"><a name="p61624507"></a><a name="p61624507"></a>416 Client Requested Range Not Satisfiable</p>
</td>
</tr>
<tr id="row37618463162019"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27196685162019"><a name="p27196685162019"></a><a name="p27196685162019"></a>InvalidRedirectLocation</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55447851162019"><a name="p55447851162019"></a><a name="p55447851162019"></a>Invalid redirect location.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62090913162019"><a name="p62090913162019"></a><a name="p62090913162019"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row9411574162024"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p24140030162024"><a name="p24140030162024"></a><a name="p24140030162024"></a>InvalidRequest</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9185427162024"><a name="p9185427162024"></a><a name="p9185427162024"></a>Invalid request.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5822108162024"><a name="p5822108162024"></a><a name="p5822108162024"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row9472427163110"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29069126163110"><a name="p29069126163110"></a><a name="p29069126163110"></a>InvalidRequestBody</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p24479620163118"><a name="p24479620163118"></a><a name="p24479620163118"></a>Invalid POST request body.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p66254305163110"><a name="p66254305163110"></a><a name="p66254305163110"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row17749652"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28435668"><a name="p28435668"></a><a name="p28435668"></a>InvalidSecurity</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p21587744"><a name="p21587744"></a><a name="p21587744"></a>The provided security credentials are invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3776865"><a name="p3776865"></a><a name="p3776865"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row33991793"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1871868"><a name="p1871868"></a><a name="p1871868"></a>InvalidStorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17403632"><a name="p17403632"></a><a name="p17403632"></a>The specified storage class is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p408051"><a name="p408051"></a><a name="p408051"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row9836659163133"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58571906163133"><a name="p58571906163133"></a><a name="p58571906163133"></a>InvalidTargetBucketForLogging</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p30780899163144"><a name="p30780899163144"></a><a name="p30780899163144"></a>The delivery group has not ACL permission for the target bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p24925243163133"><a name="p24925243163133"></a><a name="p24925243163133"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row3672467"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29034419"><a name="p29034419"></a><a name="p29034419"></a>InvalidURI</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2977719"><a name="p2977719"></a><a name="p2977719"></a>The specified URI cannot be parsed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39868680"><a name="p39868680"></a><a name="p39868680"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row23273800"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6129654"><a name="p6129654"></a><a name="p6129654"></a>KeyTooLong</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p26740005"><a name="p26740005"></a><a name="p26740005"></a>The provided key is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18456829"><a name="p18456829"></a><a name="p18456829"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row31893735"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p33255758"><a name="p33255758"></a><a name="p33255758"></a>MalformedACLError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9361906"><a name="p9361906"></a><a name="p9361906"></a>The provided XML file is in incorrect format or does not meet format requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p20116922"><a name="p20116922"></a><a name="p20116922"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row54670465163310"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p66231548163310"><a name="p66231548163310"></a><a name="p66231548163310"></a>MalformedError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61973594163322"><a name="p61973594163322"></a><a name="p61973594163322"></a>The XML format in the request is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15293271163310"><a name="p15293271163310"></a><a name="p15293271163310"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row4711278116244"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p5803891016244"><a name="p5803891016244"></a><a name="p5803891016244"></a>MalformedLoggingStatus</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p353123516244"><a name="p353123516244"></a><a name="p353123516244"></a>The Logging XML format is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1759459616244"><a name="p1759459616244"></a><a name="p1759459616244"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row12257227163340"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p53311302163340"><a name="p53311302163340"></a><a name="p53311302163340"></a>MalformedPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p23265485163350"><a name="p23265485163350"></a><a name="p23265485163350"></a>The check of BucketPolicy does not pass.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4056854163340"><a name="p4056854163340"></a><a name="p4056854163340"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row46834575"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p35504265"><a name="p35504265"></a><a name="p35504265"></a>MalformedPOSTRequest</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p57273244"><a name="p57273244"></a><a name="p57273244"></a>The body of the POST request is in incorrect format.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8621167"><a name="p8621167"></a><a name="p8621167"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row12834480162753"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p32959984162753"><a name="p32959984162753"></a><a name="p32959984162753"></a>MalformedQuotaError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52513065162753"><a name="p52513065162753"></a><a name="p52513065162753"></a>The Quota XML format is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25699842162753"><a name="p25699842162753"></a><a name="p25699842162753"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row10481640"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43706494"><a name="p43706494"></a><a name="p43706494"></a>MalformedXML</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p50565162"><a name="p50565162"></a><a name="p50565162"></a>This error code is returned after you send an XML file in incorrect format, stating "The XML you provided was not well-formed or did not validate against our published schema."</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2137425"><a name="p2137425"></a><a name="p2137425"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row19236831"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14679501"><a name="p14679501"></a><a name="p14679501"></a>MaxMessageLength Exceeded</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p48188907"><a name="p48188907"></a><a name="p48188907"></a>The request is too long.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10987361"><a name="p10987361"></a><a name="p10987361"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row31777389"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23831707"><a name="p23831707"></a><a name="p23831707"></a>MaxPostPreDataLength ExceededError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51320118"><a name="p51320118"></a><a name="p51320118"></a>The POST request fields prior to the file to be uploaded are too large.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p63288869"><a name="p63288869"></a><a name="p63288869"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row32728912"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p33796185"><a name="p33796185"></a><a name="p33796185"></a>MetadataTooLarge</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53136426"><a name="p53136426"></a><a name="p53136426"></a>The size of metadata headers exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9083244"><a name="p9083244"></a><a name="p9083244"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row14640334"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45016444"><a name="p45016444"></a><a name="p45016444"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p22453358"><a name="p22453358"></a><a name="p22453358"></a>The specified method is not allowed against the requested resource.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6782733"><a name="p6782733"></a><a name="p6782733"></a>405 Method Not Allowed</p>
</td>
</tr>
<tr id="row61044600"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45665605"><a name="p45665605"></a><a name="p45665605"></a>MissingContentLength</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7926514"><a name="p7926514"></a><a name="p7926514"></a>The HTTP header <strong id="b4229764"><a name="b4229764"></a><a name="b4229764"></a>Content-Length</strong> is not provided.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7066597"><a name="p7066597"></a><a name="p7066597"></a>411 Length Required</p>
</td>
</tr>
<tr id="row29258931163417"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p21163212163417"><a name="p21163212163417"></a><a name="p21163212163417"></a>MissingRegion</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36498646163417"><a name="p36498646163417"></a><a name="p36498646163417"></a>No region in the request and no default region in the system.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3600377163417"><a name="p3600377163417"></a><a name="p3600377163417"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row63599373"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p51275595"><a name="p51275595"></a><a name="p51275595"></a>MissingRequestBodyError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p59682570"><a name="p59682570"></a><a name="p59682570"></a>This error code is returned after you send an empty XML file, stating "Request body is empty."</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2450034"><a name="p2450034"></a><a name="p2450034"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row19777249163448"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58453337163448"><a name="p58453337163448"></a><a name="p58453337163448"></a>MissingRequiredHeader</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9500705163459"><a name="p9500705163459"></a><a name="p9500705163459"></a>No header field in the request.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p52299479163448"><a name="p52299479163448"></a><a name="p52299479163448"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row22050308"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41244539"><a name="p41244539"></a><a name="p41244539"></a>MissingSecurityHeader</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52473391"><a name="p52473391"></a><a name="p52473391"></a>A required header is not provided.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22486279"><a name="p22486279"></a><a name="p22486279"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row1049924"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17935054"><a name="p17935054"></a><a name="p17935054"></a>NoSuchBucket</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p43453297"><a name="p43453297"></a><a name="p43453297"></a>The specified bucket does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30056148"><a name="p30056148"></a><a name="p30056148"></a>404 Not Found</p>
</td>
</tr>
<tr id="row12694837163528"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p21648914163528"><a name="p21648914163528"></a><a name="p21648914163528"></a>NoSuchBucketPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36077378163537"><a name="p36077378163537"></a><a name="p36077378163537"></a>Nonexistent bucket policy.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36170900163528"><a name="p36170900163528"></a><a name="p36170900163528"></a>404 Not Found</p>
</td>
</tr>
<tr id="row31595463163556"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9095715163556"><a name="p9095715163556"></a><a name="p9095715163556"></a>NoSuchCORSConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65664311163556"><a name="p65664311163556"></a><a name="p65664311163556"></a>Nonexistent CORS configuration.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17209004163556"><a name="p17209004163556"></a><a name="p17209004163556"></a>404 Not Found</p>
</td>
</tr>
<tr id="row56946791163627"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49287341163627"><a name="p49287341163627"></a><a name="p49287341163627"></a>NoSuchCustomDomain</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32851721163627"><a name="p32851721163627"></a><a name="p32851721163627"></a>The requested user domain does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43743712163627"><a name="p43743712163627"></a><a name="p43743712163627"></a>404 Not Found</p>
</td>
</tr>
<tr id="row2069877"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p33442331"><a name="p33442331"></a><a name="p33442331"></a>NoSuchKey</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p24474327"><a name="p24474327"></a><a name="p24474327"></a>The specified key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36263438"><a name="p36263438"></a><a name="p36263438"></a>404 Not Found</p>
</td>
</tr>
<tr id="row1759730916373"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1609595716373"><a name="p1609595716373"></a><a name="p1609595716373"></a>NoSuchLifecycleConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2870412516373"><a name="p2870412516373"></a><a name="p2870412516373"></a>The requested LifeCycle does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4333276516373"><a name="p4333276516373"></a><a name="p4333276516373"></a>404 Not Found</p>
</td>
</tr>
<tr id="row11527154163733"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p61284262163733"><a name="p61284262163733"></a><a name="p61284262163733"></a>NoSuchPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65078183163733"><a name="p65078183163733"></a><a name="p65078183163733"></a>The specified policy name does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36841436163733"><a name="p36841436163733"></a><a name="p36841436163733"></a>404 Not Found</p>
</td>
</tr>
<tr id="row57935492"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p62263298"><a name="p62263298"></a><a name="p62263298"></a>NoSuchUpload</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10162352"><a name="p10162352"></a><a name="p10162352"></a>The specified multipart upload does not exist. The upload ID does not exist or the multipart upload has been aborted or completed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17844150"><a name="p17844150"></a><a name="p17844150"></a>404 Not Found</p>
</td>
</tr>
<tr id="row26379626"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p56374952"><a name="p56374952"></a><a name="p56374952"></a>NoSuchVersion</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2968403"><a name="p2968403"></a><a name="p2968403"></a>The specified version ID does not match any existing version.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39114066"><a name="p39114066"></a><a name="p39114066"></a>404 Not Found</p>
</td>
</tr>
<tr id="row8552084163840"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p21630165163840"><a name="p21630165163840"></a><a name="p21630165163840"></a>NoSuchWebsiteConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7212935163840"><a name="p7212935163840"></a><a name="p7212935163840"></a>The requested website does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p47376849163840"><a name="p47376849163840"></a><a name="p47376849163840"></a>404 Not Found</p>
</td>
</tr>
<tr id="row16482277"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59996030"><a name="p59996030"></a><a name="p59996030"></a>NotImplemented</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27840223"><a name="p27840223"></a><a name="p27840223"></a>The provided header implies a function that is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40465585"><a name="p40465585"></a><a name="p40465585"></a>501 Not Implemented</p>
</td>
</tr>
<tr id="row28645947"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38620409"><a name="p38620409"></a><a name="p38620409"></a>NotSignedUp</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41245435"><a name="p41245435"></a><a name="p41245435"></a>Your account is not signed up for OBS. OBS is available only after you sign up.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p52545962"><a name="p52545962"></a><a name="p52545962"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row3151613"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p53954138"><a name="p53954138"></a><a name="p53954138"></a>NotSuchBucketPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8209047"><a name="p8209047"></a><a name="p8209047"></a>The specified bucket does not have a bucket policy.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60953052"><a name="p60953052"></a><a name="p60953052"></a>404 Not Found</p>
</td>
</tr>
<tr id="row323309314529"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13545103145220"><a name="p13545103145220"></a><a name="p13545103145220"></a>ObjectHasAlreadyRestored</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p23411521145220"><a name="p23411521145220"></a><a name="p23411521145220"></a>The cold objects have been restored and the retention period of the objects cannot be shortened.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17285064145220"><a name="p17285064145220"></a><a name="p17285064145220"></a>409 Conflict</p>
</td>
</tr>
<tr id="row11706562"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8707431"><a name="p8707431"></a><a name="p8707431"></a>OperationAborted</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34213288"><a name="p34213288"></a><a name="p34213288"></a>A conflicting operation is being performed on this resource. Retry later.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19812975"><a name="p19812975"></a><a name="p19812975"></a>409 Conflict</p>
</td>
</tr>
<tr id="row44099047"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15253039"><a name="p15253039"></a><a name="p15253039"></a>PermanentRedirect</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27536623"><a name="p27536623"></a><a name="p27536623"></a>The requested bucket must be addressed using a specified endpoint. Send all future requests to the endpoint.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15874000"><a name="p15874000"></a><a name="p15874000"></a>301 Moved Permanently</p>
</td>
</tr>
<tr id="row8648276"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29421769"><a name="p29421769"></a><a name="p29421769"></a>PreconditionFailed</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34353074"><a name="p34353074"></a><a name="p34353074"></a>At least one of the specified preconditions is not met.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p31135608"><a name="p31135608"></a><a name="p31135608"></a>412 Precondition Failed</p>
</td>
</tr>
<tr id="row11785017"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15062292"><a name="p15062292"></a><a name="p15062292"></a>Redirect</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12086144"><a name="p12086144"></a><a name="p12086144"></a>The request is temporarily redirected.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39453604"><a name="p39453604"></a><a name="p39453604"></a>307 Moved Temporarily</p>
</td>
</tr>
<tr id="row19538123"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39084151"><a name="p39084151"></a><a name="p39084151"></a>RequestIsNotMultiPart Content</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11699696"><a name="p11699696"></a><a name="p11699696"></a>A bucket POST request must contain an enclosure-type multipart or the form-data.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8151325"><a name="p8151325"></a><a name="p8151325"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row6253067"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36736418"><a name="p36736418"></a><a name="p36736418"></a>RequestTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p22859873"><a name="p22859873"></a><a name="p22859873"></a>The socket connection to the server has no reads or writes within the timeout period.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39710449"><a name="p39710449"></a><a name="p39710449"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row21849727"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p24997451"><a name="p24997451"></a><a name="p24997451"></a>RequestTimeTooSkewed</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11527611"><a name="p11527611"></a><a name="p11527611"></a>The difference between the request time and the server's time is too big.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61321271"><a name="p61321271"></a><a name="p61321271"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row15020534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8703728"><a name="p8703728"></a><a name="p8703728"></a>RequestTorrentOfBucket Error</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p33913387"><a name="p33913387"></a><a name="p33913387"></a>Requesting the bucket's torrent file is not allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62629839"><a name="p62629839"></a><a name="p62629839"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row18434641145249"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p31345939145259"><a name="p31345939145259"></a><a name="p31345939145259"></a>RestoreAlreadyInProgress</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55993115145259"><a name="p55993115145259"></a><a name="p55993115145259"></a>The cold objects are being restored. The request conflicts with another one.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39148443145259"><a name="p39148443145259"></a><a name="p39148443145259"></a>409 Conflict</p>
</td>
</tr>
<tr id="row31782868164021"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p24275482164021"><a name="p24275482164021"></a><a name="p24275482164021"></a>ServiceNotImplemented</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p20157025164021"><a name="p20157025164021"></a><a name="p20157025164021"></a>The request method is not implemented by the server.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22106320164021"><a name="p22106320164021"></a><a name="p22106320164021"></a>501 Not Implemented</p>
</td>
</tr>
<tr id="row43003550164114"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p60735535164114"><a name="p60735535164114"></a><a name="p60735535164114"></a>ServiceNotSupported</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p20631304164114"><a name="p20631304164114"></a><a name="p20631304164114"></a>The request method is not supported by the server.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60522962164114"><a name="p60522962164114"></a><a name="p60522962164114"></a>409 Conflict</p>
</td>
</tr>
<tr id="row34422712163952"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36776251163952"><a name="p36776251163952"></a><a name="p36776251163952"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1429656616403"><a name="p1429656616403"></a><a name="p1429656616403"></a>The server is overloaded or has internal errors.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p57198039164011"><a name="p57198039164011"></a><a name="p57198039164011"></a>503 Service Unavailable</p>
</td>
</tr>
<tr id="row26797639"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23125146"><a name="p23125146"></a><a name="p23125146"></a>SignatureDoesNotMatch</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61197546"><a name="p61197546"></a><a name="p61197546"></a>The provided signature does not match the signature calculated by OBS. Check your SK and signature calculation method.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58054174"><a name="p58054174"></a><a name="p58054174"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row52725521"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42908823"><a name="p42908823"></a><a name="p42908823"></a>SlowDown</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53062645"><a name="p53062645"></a><a name="p53062645"></a>The request frequency is high. Reduce your request frequency.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3107028"><a name="p3107028"></a><a name="p3107028"></a>503 Service Unavailable</p>
</td>
</tr>
<tr id="row17773985164154"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p30406660164154"><a name="p30406660164154"></a><a name="p30406660164154"></a>System Capacity Not enough</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p47020367164154"><a name="p47020367164154"></a><a name="p47020367164154"></a>Insufficient system capacity.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p50553387164154"><a name="p50553387164154"></a><a name="p50553387164154"></a>403 Forbidden</p>
</td>
</tr>
<tr id="row27963260"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p50431550"><a name="p50431550"></a><a name="p50431550"></a>TemporaryRedirect</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p58423765"><a name="p58423765"></a><a name="p58423765"></a>The request is redirected to the bucket while the domain name server (DNS) is being updated.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34704553"><a name="p34704553"></a><a name="p34704553"></a>307 Moved Temporarily</p>
</td>
</tr>
<tr id="row14517998164321"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11033816164325"><a name="p11033816164325"></a><a name="p11033816164325"></a>TooManyBuckets</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p21323878164325"><a name="p21323878164325"></a><a name="p21323878164325"></a>You have attempted to create more buckets than allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p49512524164325"><a name="p49512524164325"></a><a name="p49512524164325"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row13417899164227"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13108021164227"><a name="p13108021164227"></a><a name="p13108021164227"></a>TooManyCustomDomains</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55116800164227"><a name="p55116800164227"></a><a name="p55116800164227"></a>Too many user domains are configured.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35275828164227"><a name="p35275828164227"></a><a name="p35275828164227"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row56067068164255"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45138691164255"><a name="p45138691164255"></a><a name="p45138691164255"></a>TooManyObjectCopied</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32355317164255"><a name="p32355317164255"></a><a name="p32355317164255"></a>The number of copied users' objects exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3535036164255"><a name="p3535036164255"></a><a name="p3535036164255"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row48382285164438"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26651017164438"><a name="p26651017164438"></a><a name="p26651017164438"></a>TooManyWrongSignature</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11248765164438"><a name="p11248765164438"></a><a name="p11248765164438"></a>The request is rejected due to high-frequency errors.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p38734802164438"><a name="p38734802164438"></a><a name="p38734802164438"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row32528885"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17593999"><a name="p17593999"></a><a name="p17593999"></a>UnexpectedContent</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15827797"><a name="p15827797"></a><a name="p15827797"></a>This request does not support content.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6983217"><a name="p6983217"></a><a name="p6983217"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row62848953"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57600462"><a name="p57600462"></a><a name="p57600462"></a>UnresolvableGrantBy EmailAddress</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p35125868"><a name="p35125868"></a><a name="p35125868"></a>The provided email address does not match any recorded account.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26623034"><a name="p26623034"></a><a name="p26623034"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row38280714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13730148"><a name="p13730148"></a><a name="p13730148"></a>UserKeyMustBeSpecified</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p38400194"><a name="p38400194"></a><a name="p38400194"></a>The user's AK is not carried in the request.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p23408013"><a name="p23408013"></a><a name="p23408013"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row54859382164356"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14424920164356"><a name="p14424920164356"></a><a name="p14424920164356"></a>WebsiteRedirect</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27567887164356"><a name="p27567887164356"></a><a name="p27567887164356"></a>The website request lacks bucketName.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18406403164356"><a name="p18406403164356"></a><a name="p18406403164356"></a>301 Moved Permanently</p>
</td>
</tr>
<tr id="row3790537116488"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58442277164852"><a name="p58442277164852"></a><a name="p58442277164852"></a>KMS.DisabledException</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36204035164852"><a name="p36204035164852"></a><a name="p36204035164852"></a>The master key is disabled in server-side encryption with KMS-managed keys (SSE-KMS) mode.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46845733164852"><a name="p46845733164852"></a><a name="p46845733164852"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row28760464164812"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59237015164852"><a name="p59237015164852"></a><a name="p59237015164852"></a>KMS.NotFoundException</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p33468948164852"><a name="p33468948164852"></a><a name="p33468948164852"></a>The master key does not exist in SSE-KMS mode.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26630257164852"><a name="p26630257164852"></a><a name="p26630257164852"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row63919997103116"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43514285103213"><a name="p43514285103213"></a><a name="p43514285103213"></a>InvalidTagError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34996224103213"><a name="p34996224103213"></a><a name="p34996224103213"></a>An invalid tag is provided when configuring the bucket tag.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16121875103213"><a name="p16121875103213"></a><a name="p16121875103213"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row46442272103123"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8795778103213"><a name="p8795778103213"></a><a name="p8795778103213"></a>MalformedXMLError</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41369454103213"><a name="p41369454103213"></a><a name="p41369454103213"></a>The provided XML format is incorrect when configuring the bucket tag.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62591445103213"><a name="p62591445103213"></a><a name="p62591445103213"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row903770103127"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p62245297103213"><a name="p62245297103213"></a><a name="p62245297103213"></a>NoSuchTagSet</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8704271103213"><a name="p8704271103213"></a><a name="p8704271103213"></a>The specified bucket is not configured with a tag.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33957317103213"><a name="p33957317103213"></a><a name="p33957317103213"></a>404 Not Found</p>
</td>
</tr>
</tbody>
</table>

