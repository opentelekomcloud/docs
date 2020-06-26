# Examples<a name="EN-US_TOPIC_0220024721"></a>

Invoke API demo code.

## Main.java<a name="en-us_topic_0125376203_section6768164511616"></a>

This class is a running entry class for calling APIs. Before running this class, you need to set the following parameters:

1.  IP address of the cluster management node
2.  Login username and password

Before calling service APIs, call login authentication APIs for performing login authentication first. For details about how to call login authentication APIs, see  **CASLogin.java**.

The following example describes how to call the GET and POST APIs.

1.  GET request API

    This example describes how to call the API for querying the installed clusters \(/web/v1/clusters\).

    Before the service API is called, the IP address, port number, and the  **/web**  path are added to the webUrl. Therefore, you need to combine the webUrl with the request API path  **/v1/clusters**  in the operationUrl of the service API.

2.  POST request API

    This example describes how to call the API for starting a service \(/web/v1/maintain/cluster/\{cluster\_id\}/service/\{service\_name\}/start\).

    In the operationUrl of this API, you need to combine the webUrl with the request API path  **v1/maintain/cluster/\{cluster\_id\}/service/\{service\_name\}/start**. In the request path URL, enter the current cluster ID and the name of the service to be started.

    According to the requirements of the API for starting a service, specified parameters need to be inputted in the request body. These parameters are written in the example  **StartService.json**  file in JSON format, and the file path is specified in  **jsonFilePath**.


You can view information about API calling in the generated  **Demo.log**  file. For details about log configurations, see  **Log4j.properties**.

```
package com.MRS;
 
import org.apache.http.client.HttpClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.MRS.login.CASLogin;
import com.MRS.operation.HttpManager;
 
/**
 * Program running entry
 *
 */
public class Main 
{
    private static final Logger LOG = LoggerFactory.getLogger(Main.class);
    
    // IP address of the cluster management node
    public static final String IP_Address = "xxx.xxx.xxx.xxx";
    
    public static void main(String[] args)
    {
        //############# Step 1. Prepare for calling an API.#############
        // Login username and password
        String userName = "xxxxxx";
        String password = "xxxxxxxxx";
        HttpManager httpManager = new HttpManager();
        
        // CAS and Web URLs
        String casUrl = "https://" + IP_Address + ":20009/cas/login";
        String webUrl = "https://" + IP_Address + ":28443/web/";
        
        // userTLSVersion is a mandatory parameter. It is an important parameter used for connecting a JDK 1.6 server to a JDK 1.8 server. If you use JDK 1.8, set this parameter to an empty character string.
        String userTLSVersion = "";
        
        //############# Step 2. Call an API to complete login authentication.#############
        LOG.info("Begin to get httpclient and login cas.");
        HttpClient  httpClient = new CASLogin().login(casUrl, webUrl, userName, password, userTLSVersion);
        
        //############# Step 3. Call APIs based on the service.#############
        
        // Send a GET request to call the API for querying the installed clusters.
        String operationUrl = webUrl + "/v1/clusters";
        httpManager.sendHttpGetRequest(httpClient, operationUrl);
        
        // Send a POST request to call the API for adding a user.
        String jsonFilePath = "./conf/startService.json";
        String operationUrl = webUrl + "/v1/maintain/cluster/{cluster_id}/service/{service_name}/start";
        httpManager.sendHttpPostRequest(httpClient, operationUrl, jsonFilePath);
        
        //############# Step 4. Close the connection.#############
        httpClient.getConnectionManager().shutdown();
    }
}
```

## CASLogin.java<a name="en-us_topic_0125376203_section17411934161712"></a>

This class allows login authentication with a token.

1.  Build an HttpClient client object.
2.  Invoke the  **getCasLoginPage\(\)**  method to obtain the CAS login page, input the casUrl and the HttpClient client object, and obtain the returned  **casLoginPageResponse**  response object.

    The method is to send a GET request to the cluster. The request path is https://_casUrl_/login.

3.  The HttpClient obtains the  **casSessionId**  and  **loginTicket**  from the  **casLoginPageResponse**  response object.
4.  Invoke the  **loginCasServer\(\)**  method to obtain the username and password for CAS server authentication, input the casUrl, webUrl, username, password, HttpClient object, casSessionId, loginTicket, and userTLSVersion parameters to obtain the  **loginPostResponse**  response object.

    This method is to send a POST login authentication request to the cluster. The request path is https://_casUrl_/login?service= https://_webUrl_/ cas\_security\_check.htm.

5.  The HttpClient obtains the authenticated TGC from the  **loginPostResponse**  response object.
6.  Invoke the  **webLoginCheck\(\)**  method to initiate a web application login verification request, input the webUrl and the HttpClient client object, and obtain the  **webLoginCheck**  response object.

    The method is to send a GET verification request to the cluster. The request path is https://_webUrl_/v1/access/login\_check.

7.  The HttpClient obtains the JSESSIONID of the web request from the  **webLoginCheck**  response object.
8.  Return an available HttpClient client object.

```
package com.MRS.login;
 
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import org.apache.commons.lang.StringUtils;
import org.apache.http.Header;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.impl.conn.tsccm.ThreadSafeClientConnManager;
import org.apache.http.message.BasicNameValuePair;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.MRS.operation.WebClientWrapper;
import com.MRS.utils.ParamsValidUtil;
 
public class CASLogin 
{
    private static final Logger LOG = LoggerFactory.getLogger(CASLogin.class);
    private static final String SET_COOKIE = "Set-Cookie";
    private static final String CAS_SESSION_ID_STRING = "casSessionId=";
    private static final String CAS_TGC_STRING = "CASTGC=";
    private static final String SEMICOLON_SEPARATOR = ";";
    private static final String DOUBLE_QUOTAYION = "\"";
    private static final String LOGINTICKET_STRING = "name=\"lt\" value=";
    private static final int LOGINTICKET_INDEX = 5;
    private static final String WRONGPASSWORD = "The credentials you provided cannot be determined to be authentic";
    private static final String RESETPASSWORD = "modify_password.html";
    private static final String ENCODING = "UTF-8";
    public String tgc = "";
 
    public HttpClient login(String casUrl, String webUrl, String userName, String password, String userTLSVersion)
    {
        if (ParamsValidUtil.isEmpty(casUrl, webUrl, userName, password))
        {
            LOG.error("Invalid input param.");
            return null;
        }
        if (userTLSVersion == null || userTLSVersion.isEmpty())
        {
            userTLSVersion = "TLS";
        }
        LOG.info("Get http client for sending https request, username is {}, casUrl is {}, webUrl is {}.",
                userName, casUrl, webUrl);
        
        // Obtain the HttpClient.
        HttpClient httpClient = getHttpClient(userTLSVersion);
        
        // Obtain the CAS login page.
        HttpResponse casLoginPageResponse = getCasLoginPage(casUrl, httpClient);
        LOG.info("get cas login page response is :{}.", casLoginPageResponse);
        
        // Obtain casSessionId and loginTicket.
        String casSessionId = getCasSessionId(casLoginPageResponse);
        String loginTicket = getLoginTicket(casLoginPageResponse);
        LOG.info("casSessionId = {} , loginTicket = {}.", casSessionId, loginTicket);
        if(StringUtils.isBlank(casSessionId) || StringUtils.isBlank(loginTicket))
        {
            LOG.error("Invalid input param.");
            return null;
        }
        
        // Authenticate the username and password on the CAS server.
        HttpResponse loginPostResponse =
                loginCasServer(casUrl, webUrl, userName, password, httpClient, casSessionId, loginTicket, userTLSVersion);
        LOG.info("the login post response is: {}.", loginPostResponse);
        
        // Obtain the authenticated TGC.
        String casTgc = getCASTGC(loginPostResponse);
        LOG.info("casTgc = {}.", casTgc);
        
        // Check the login.
        HttpResponse webLoginCheck = webLoginCheck(webUrl, httpClient);
        LOG.info("web login check response is: {}.", webLoginCheck);
        
        // If the login authentication is successful, the available HttpClient is returned.
        return httpClient;
    }
    
    /**
     * Obtain the HttpClient.
     * @return http client
     */
    @SuppressWarnings("deprecation")
    public HttpClient getHttpClient(String userTLSVersion)
    {
        ThreadSafeClientConnManager safeClientConnManager = new ThreadSafeClientConnManager();
        safeClientConnManager.setMaxTotal(100);
        HttpClient httpclient = WebClientWrapper.wrapClient(new DefaultHttpClient(safeClientConnManager), userTLSVersion);
        return httpclient;
    }
    
    /**
     * Obtain the CAS login page.
     * @param casUrl CAS homepage address
     * @param httpclient  http client
     * @return response Response of the request
     */
    private HttpResponse getCasLoginPage(String casUrl, HttpClient httpclient)
    {
        LOG.info("Enter getCasLoginPage, the casUrl is: {}", casUrl);
        HttpGet preLoginHttpGet = new HttpGet(casUrl);
        HttpResponse httpResponse = null;
        try 
        {
            httpResponse = httpclient.execute(preLoginHttpGet);
        } 
        catch (Exception e) 
        {
            LOG.error("Execute cas login failed.");
        } 
        return httpResponse;
    }
    
    /**
     * Obtain the CAS session ID from the returned login page response.
     * @param preLoginResponse  Response of the login page request
     * @return session id Session ID
     */
    private String getCasSessionId(HttpResponse preLoginResponse)
    {
        Header resHeader = preLoginResponse.getFirstHeader(SET_COOKIE);
        String setCookie = resHeader == null ? "" : resHeader.getValue();
        String casSessionId =
            setCookie.substring(CAS_SESSION_ID_STRING.length(), setCookie.indexOf(SEMICOLON_SEPARATOR));
        return casSessionId;
    }
    
    /**
     * Obtain the login ticket from the returned login page response.
     * @param preLoginResponse  Response of the login page request
     * @return loginTicket Login authentication ticket
     */
    private String getLoginTicket(HttpResponse preLoginResponse)
    {
        BufferedReader bufferedReader = null;
        String loginTicket = "";
        try
        {
            InputStream inputStream = preLoginResponse.getEntity().getContent();
            
            // When the http response is not empty, the context attribute is not null.
            bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
            String lineContent = "";
            while (null != lineContent)
            {
                lineContent = bufferedReader.readLine();
                if ((null != lineContent) && (lineContent.contains(LOGINTICKET_STRING)))
                {
                    // Delete spaces at the beginning and end of the line.
                    lineContent = lineContent.trim();
                    // If LOGINTICKET_STRING (name=\"loginTicket\" value=) exists, split it based on the double quotation marks. The array length cannot be less than 6.
                    loginTicket = lineContent.split(DOUBLE_QUOTAYION)[LOGINTICKET_INDEX];
                    break;
                }
            }
        }
        catch (Exception e)
        {
            LOG.error("Get loginTicket failed.");
        }
        finally
        {
            if (bufferedReader != null)
            {
                try
                {
                    bufferedReader.close();
                }
                catch (IOException e)
                {
                    LOG.warn("Close buffer reader failed.");
                }
            }
        }
        return loginTicket;
    }
    
    /**
     * Obtain the TGC from the response of the request for logging in to the CAS Server.
     * @param loginPostResponse Response object
     * @return TGC Authenticated ticket
     */
    private String getCASTGC(HttpResponse loginPostResponse)
    {
        Header header = loginPostResponse.getLastHeader(SET_COOKIE);
        String casTgcHeader = header == null ? "" : header.getValue();
        String tempCasTgc = casTgcHeader.split(SEMICOLON_SEPARATOR)[0];
        if (StringUtils.isEmpty(tempCasTgc))
        {
            return "";
        }
        String casTgc = tempCasTgc.substring(CAS_TGC_STRING.length());
        this.tgc = casTgc;
        return casTgc;
    }
    
    /**
     * Log in to the CAS server and verify user information.
     * @param casUrl CAS server address
     * @param webUrl Web application address
     * @param userName Login username
     * @param password Login password
     * @param casSessionId CAS session ID
     * @param loginTicket CAS login ticket
     * @return http client HTTP client
     */
    private HttpResponse loginCasServer(String casUrl, String webUrl, String userName, String password,
        HttpClient httpClient, String casSessionId, String loginTicket,String userTLSVersion)
    {
        if (ParamsValidUtil.isEmpty(casUrl, webUrl, userName, password, casSessionId, loginTicket))
        {
            LOG.error("Invalid input param.");
            return null;
        }
        String postUrl = generateCasLoginUrl(casUrl, webUrl);
        LOG.info("login cas server URL is : {}.", postUrl);
        
        HttpPost httpPost = new HttpPost(postUrl);
        List<BasicNameValuePair> FormData = new ArrayList<BasicNameValuePair>();
        FormData.add(new BasicNameValuePair("username", userName));
        FormData.add(new BasicNameValuePair("password", password));
        FormData.add(new BasicNameValuePair("lt", loginTicket));
        FormData.add(new BasicNameValuePair("_eventId", "submit"));
        FormData.add(new BasicNameValuePair("submit", "Login"));
        HttpResponse response = null;
        BufferedReader bufferedReader = null;
        httpPost.addHeader("Cookie", CAS_SESSION_ID_STRING + casSessionId);
        
        try
        {
            httpPost.setEntity(new UrlEncodedFormEntity(FormData, ENCODING));
            response = httpClient.execute(httpPost);
            LOG.info("Login CasServer status is {}", response.getStatusLine());
            
            InputStream inputStream = response.getEntity().getContent();
            bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
            String lineContent = "";
            lineContent = bufferedReader.readLine();
            
            // Performs corresponding operations based on the message returned. Currently, only two types of results are returned on the CAS login page in Java mode.
            while (lineContent != null)
            {
                // Incorrect username or password
                if (lineContent.contains(WRONGPASSWORD))
                {
                    LOG.error("The username or password is wrong");
                }
                // Reset the password upon the first login.
                if (lineContent.contains(RESETPASSWORD))
                {
                    LOG.warn("Login first time,please reset password.");
                }
                lineContent = bufferedReader.readLine();
            }
        }
        catch (Exception e)
        {
            LOG.error("Login cas server failed.");
        }
        finally
        {
            if (bufferedReader != null)
            {
                try
                {
                    bufferedReader.close();
                }
                catch (IOException e)
                {
                    LOG.error("Login cas server failed because of IOException.");
                }
            }
        }
        return response;
    }
    
    /**
     * Generate a complete URL for logging in to CAS.
     * After the login is successful, the specified CAS security check page is displayed.
     * @param casUrl
     * @param webUrl
     * @return
     */
    private String generateCasLoginUrl(String casUrl, String webUrl)
    {
        StringBuilder sb = new StringBuilder();
        sb.append(casUrl);
        sb.append("?service=");
        sb.append(webUrl);
        sb.append("/cas_security_check.htm");
        return sb.toString();
    }
    
    /**
     * Initiate a request for web application login verification.
     * @param webUrl Web application URL
     * @param httpclient http client
     * @return response Login verification response object
     */
    private HttpResponse webLoginCheck(String webUrl, HttpClient httpclient)
    {
        // Web login authentication request path
        HttpGet loginCheckHttpGet = new HttpGet(webUrl + "/v1/access/login_check");
        LOG.info("web login check URL is: {}.", (webUrl + "/v1/access/login_check "));
        
        HttpResponse response = null;
        BufferedReader bufferedReader = null;
        InputStream inputStream  = null;
        try
        {
            response = httpclient.execute(loginCheckHttpGet);
            inputStream = response.getEntity().getContent();
            bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
            String lineContent = "";
            lineContent = bufferedReader.readLine();
            LOG.info("response content is {} : " + lineContent);
        }
        catch (Exception e)
        {
            LOG.error("Get loginTicket failed.");
        }
        finally
        {
            if (bufferedReader != null)
            {
                try
                {
                    bufferedReader.close();
                }
                catch (IOException e)
                {
                    LOG.warn("Close bufferedReader failed.");
                }
            }
            if (inputStream != null)
            {
                try
                {
                    inputStream.close();
                }
                catch (IOException e)
                {
                    LOG.warn("Close inputStream failed.");
                }
            }
        }
        return response;
    }
}
```

## HttpManager.java<a name="en-us_topic_0125376203_section1740919566200"></a>

This class provides specific GET and POST request methods.

```
package com.MRS.operation;
 
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
 
public class HttpManager 
{
    private static final String ENCODING = "UTF-8";
    private static final Logger LOG = LoggerFactory.getLogger(HttpManager.class);
    
    /**
     * Send an httpGet request based on the input parameters such as httpclient and url.
     * @param httpclient
     * @param operationUrl
     */
    public String sendHttpGetRequest(HttpClient httpClient, String operationUrl)
    {
        if (operationUrl == null || operationUrl.isEmpty())
        {
            LOG.error("The operationUrl is emptey.");
            return null;
        }
        LOG.info("The operationUrl is:{}", operationUrl);
        
        BufferedReader bufferedReader = null;
        InputStream inputStream = null;
        StringBuffer lineContent = new  StringBuffer();
        try
        {
            HttpGet httpGet = new HttpGet(operationUrl);
            HttpResponse rsp = httpClient.execute(httpGet);
            LOG.info("Operation status is {}.", rsp.getStatusLine());
            inputStream = rsp.getEntity().getContent();
            bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
            
            String temp = bufferedReader.readLine();
            while (temp != null)
            {
                lineContent.append(temp);
                temp = bufferedReader.readLine();
            }
            bufferedReader.close();
            inputStream.close();
            LOG.info("The get response lineContent is {}.", lineContent);
        }
        catch (Exception e)
        {
            LOG.info("Send http get request field..");
        }
        finally
        {
            if (bufferedReader != null)
            {
                try
                {
                    bufferedReader.close();
                }
                catch (IOException e)
                {
                    LOG.info("Close bufferedReader failed.");
                }
            }
            if (inputStream != null)
            {
                try
                {
                    inputStream.close();
                }
                catch (IOException e)
                {
                    LOG.info("Close inputStream failed.");
                }
            }
        }
        LOG.info("SendHttpGetMessage completely.");
        return lineContent.toString();
    }
    
    /**
     * Send an httpPost request based on the input parameters such as httpclient, url, and jsonFilePath.
     * @param httpclient
     * @param operationUrl
     * @param jsonFilePath
     * @return Return the operation command ID.
     */
    public void sendHttpPostRequest(HttpClient httpClient, String operationUrl, String jsonFilePath)
    {
        if (jsonFilePath == null || jsonFilePath.isEmpty())
        {
            LOG.error("The jsonFilePath is emptey.");
        }
        
        String filePath = jsonFilePath;
        File jsonFile = null;
        BufferedReader br = null;
        InputStream inputStream = null;
        BufferedReader bufferedReader = null;
        try
        {
            jsonFile = new File(filePath);
            List<String> list = new LinkedList<String>();
            br = new BufferedReader(new FileReader(jsonFile));
            String temp = br.readLine();
            // Add the request body in the JSON file to the list. Each line is a complete request. A request may be a line or multiple lines. Multiple HTTP requests need to be sent for multiple lines.
            while (temp != null)
            {
                list.add(temp);
                temp = br.readLine();
            }
            br.close();
            
            for (int line = 0; line < list.size(); line++)
            {
                String tempString = list.get(line);
                String json = tempString;
                
                if (json == null || json.length() == 0)
                {
                    break;
                }
                
                HttpResponse response = null;
                // Build a request header and a request body.
                HttpPost httpPost = new HttpPost(operationUrl);
                httpPost.addHeader("Content-Type", "application/json;charset=UTF-8");
                httpPost.setEntity(new StringEntity(json, "text/plain", ENCODING));
                // Send a POST request.
                response = httpClient.execute(httpPost);
                
                String status = response.getStatusLine().toString();
                LOG.info("The status is :{} ", status);
                
                inputStream = response.getEntity().getContent();
                bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
                String lineContent = "";
                lineContent = bufferedReader.readLine();
                LOG.info("the post response lineContent is {}.", lineContent);
                
                bufferedReader.close();
                inputStream.close();
                LOG.info("sendHttpPostRequest completely.");
            }
        }
        catch (Exception e)
        {
            LOG.error("Send http post request field.");
        }
        finally
        {
            if (bufferedReader != null)
            {
                try
                {
                    bufferedReader.close();
                }
                catch (IOException e)
                {
                    LOG.info("Close bufferedReader failed.");
                }
            }
            if (inputStream != null)
            {
                try
                {
                    inputStream.close();
                }
                catch (IOException e)
                {
                    LOG.info("Close inputStream failed.");
                }
            }
            if (br != null)
            {
                try
                {
                    br.close();
                }
                catch (IOException e)
                {
                    LOG.info("Close bufferedReader failed.");
                }
            }
        }
    }
}
```

## MRSSSLSocketFactory.java<a name="en-us_topic_0125376203_section1238084219215"></a>

```
package com.MRS.operation;
 
import java.io.IOException;
import java.net.Socket;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSocket;
import org.apache.http.conn.ssl.SSLSocketFactory;
import org.apache.http.conn.ssl.X509HostnameVerifier;
import org.apache.http.params.HttpParams;
 
/**
 * Make the TLS version set by the user take effect.
 * Inherit SSLSocketFactory.
 */
public class MRSSSLSocketFactory extends SSLSocketFactory
{
    private static String[] enabelPro = {"TLS"};
    
    public MRSSSLSocketFactory(SSLContext sslContext, X509HostnameVerifier hostnameVerifier,String userTLSVersion)
    {      
        super(sslContext, hostnameVerifier);
        enabelPro[0] = userTLSVersion;
    }
    
    @Override
    public Socket createSocket(HttpParams params)
        throws IOException
    {
        Socket result = super.createSocket(params);
        ((SSLSocket)result).setEnabledProtocols(enabelPro);
        return result;
    }
}
```

## WebClientWrapper.java<a name="en-us_topic_0125376203_section286319244232"></a>

```
package com.MRS.operation;
 
import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManager;
import javax.net.ssl.X509TrustManager;
import org.apache.http.client.HttpClient;
import org.apache.http.conn.ClientConnectionManager;
import org.apache.http.conn.scheme.Scheme;
import org.apache.http.conn.scheme.SchemeRegistry;
import org.apache.http.conn.ssl.SSLSocketFactory;
import org.apache.http.impl.client.DefaultHttpClient;
 
public class WebClientWrapper 
{
    /**
     * Extend the HttpClient class to automatically accept all certificates.
     * @param base
     * @param userTLSVersion
     * @return 
     */
    public static HttpClient wrapClient(HttpClient baseHttpClient, String userTLSVersion)
    {
        ClientConnectionManager clientConnectionManager;
        SSLContext sslContext = null;
        try {
            sslContext = SSLContext.getInstance(userTLSVersion);
        } 
        catch (NoSuchAlgorithmException e1) 
        {
            e1.printStackTrace();
        }
        
        if (sslContext == null)
        {
            return null;
        }
        
        X509TrustManager tm = new X509TrustManager()
        {
            public X509Certificate[] getAcceptedIssuers()
            {
                return null;
            }
            
            public void checkClientTrusted(X509Certificate ax509certificate[], String s) throws CertificateException
            {
            }
            
            public void checkServerTrusted(X509Certificate ax509certificate[], String s) throws CertificateException
            {
            }
        };
        
        try
        {
            sslContext.init(null, new TrustManager[] {tm}, new SecureRandom());
        }
        catch (KeyManagementException e)
        {
            e.printStackTrace();
        }
        
        SSLSocketFactory sslSocketFactory = null;
        if(userTLSVersion == null || userTLSVersion.isEmpty() || userTLSVersion.equals("TLS"))
        {
            sslSocketFactory = new SSLSocketFactory(sslContext, SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);
        }
        else
        {
            sslSocketFactory = new MRSSSLSocketFactory(sslContext, SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER,userTLSVersion);
        }
        
        clientConnectionManager = baseHttpClient.getConnectionManager();
        SchemeRegistry schemeRegistry = clientConnectionManager.getSchemeRegistry();
        schemeRegistry.register(new Scheme("https", 443, sslSocketFactory));
        return new DefaultHttpClient(clientConnectionManager, baseHttpClient.getParams());
    }
}
```

## ParamsValidUtil.java<a name="en-us_topic_0125376203_section1828116520348"></a>

```
package com.MRS.utils;
 
import org.apache.commons.lang.StringUtils;
 
public class ParamsValidUtil {
    /**
     * Check whether there are null parameters.
     * @param obj Input parameter set
     * @return Whether there are null parameters.
     */
    public static boolean isEmpty(String... obj)
    {
        for (int i = 0; i < obj.length; i++)
        {
            if (StringUtils.isEmpty(obj[i]))
            {
                return true;
            }
        }
        return false;
    }
}
```

## S**tartService.json**<a name="en-us_topic_0125376203_section104461019183520"></a>

```
{"only_self":true}
```

## L**og4j.properties**<a name="en-us_topic_0125376203_section15230656113510"></a>

```
##set log4j  DEBUG < INFO < WARN < ERROR < FATAL
log4j.logger.com.MRS=INFO,A1,A2_plus
log4j.logger.org.apache.http=INFO,A1,A2_plus
#print to the console?A1
log4j.appender.A1=org.apache.log4j.ConsoleAppender
log4j.appender.A1.layout=org.apache.log4j.PatternLayout
log4j.appender.A1.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%t] %m %l%n
 
#A2_plus the size of the rest.log < 10M, delete cyclicly
log4j.appender.A2_plus=org.wcc.framework.log.SizeRollingZipFileATimeAppender
log4j.appender.A2_plus.File=./conf/Demo.log
log4j.appender.A2_plus.MaxFileSize=10MB
log4j.appender.A2_plus.MaxBackupIndex=20
log4j.appender.A2_plus.layout=org.apache.log4j.PatternLayout
log4j.appender.A2_plus.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%t] %m %l%n
```

