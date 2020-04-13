# What Are the Differences Between PUT and POST Upload Methods?<a name="obs_faq_0071"></a>

Parameters are passed through the request header if the PUT method is used to upload objects; if the POST method is used to upload objects, parameters are passed through the form field in the message body.

With the PUT method, you need to specify the object name in the URL, but object name is not required with the POST method, which uses the bucket domain name as the URL. The request lines of the two methods are as follows:

```
PUT /ObjectName HTTP/1.1
```

```
POST / HTTP/1.1
```

Either PUT or POST method allows the object size of \[0, 5GB\] for each upload. If you need to upload an object greater than 5 GB, use the multipart upload method.

