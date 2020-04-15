# Why Are  **user\_name**  and  **op\_service**  Displayed When I Filter Traces by User?<a name="cts_faq_013"></a>

If you submit a request that involves operations requiring high permissions or invocation of other services, you may not have the required permissions. In this case, your permissions will be elevated temporarily on condition that security requirements are met. Your permissions will be resumed after the request is processed, but the permissions elevation will be recorded in CTS logs and the operation user is recorded as  **user\_name**  or  **op\_service**.

