# Federal Authentication<a name="EN-US_TOPIC_0125560478"></a>

OBS can be accessed by federated users with the V2 or V4 signature information and security token. The AK and security token in the signature information are granted to federated users by IAM. The algorithm of signature information is the same as that used by V2 or V4 common authentication.

When sending a request, a federated user must carry identity authentication information in the following format:

Federated user with V2 common signature:

```
Authorization: AWS AKIAIOSFODNN7EXAMPLE:QBaO+tS/76QYHVnUoxvf9EPH/3o=
x-amz-security-token: security token string
```

When a federated user uses a V2 temporary signature, the x-amz-security-token must be carried in the request URL, as detailed in the following example:

```
http(s)://BucketName.OBS domain name/ObjectKey?AWSAccessKeyId=AccessKeyID&Expires=ExpiresValue&x-amz-security-token=security token string&Signature=signature
```

Federated user with V4 common signature:

```
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20150524/region-1/s3/aws4_request,SignedHeaders=host;range;x-amz-date,Signature=fe5f80f77d5fa3beca038a248ff027d0445342fe2855ddc963176630326f1024
x-amz-security-token: security token string
```

When a federated user uses a V4 temporary signature, the x-amz-security-token must be carried in the request URL, as detailed in the following example:

```
http(s)://BucketName.OBS domain name/test.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20150524%2Fregion-1%2Fs3%2Faws4_request&X-Amz-Date=20150524T000000Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&x-amz-security-token=security token string&X-Amz-Signature=<signature-value>
```

If a request for OBS access contains the x-amz-security-token field, OBS deems that the request is sent by a federated user, and authenticates according to the federal authentication requirements. If either the signature or security token is incorrect, the identity authentication of this request fails.

