# Authenticating a Request<a name="obs_03_0010"></a>

Users of OBS \(compatible with OpenStack Swift\) must be authenticated using IAM. In a request sent by a client to OBS \(compatible with OpenStack Swift\), the request header must include the token ID obtained from the IAM service. This token ID is generated and encrypted by IAM based on the domain, project, and role information. In an OBS request, the  **X-Auth-Token**  is used to specify a token ID. For details about the usage, see the corresponding object operation method.

