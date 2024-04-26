# nginx

## Files

- `/etc/nginx/`: configuration files

## Creating password protected area of files

- Used a new location directive that looks like:

```nginx
location /specialurl {
    root /var/www;
    auth_basic "Message"
    auth_basic_user_file /etc/apache2/.htpasswd;
    autoindex on
}
```

- Initially tried to have a `root` location that was under the `/root`
  directory for `root` user. However, I kept running into 'Permission
  Denied' issues.

  If you look [here](https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/#not-using-standard-document-root-locations)
  you'll see that they call out `/` and `/root` as places never to store
  documents. I'm guessing it's hard coded in to never allow those
  locations.

  After moving the data to the `/var/www/specialurl` folder, things
  worked as expected.

- Followed the instructions [here](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/)
  for configuring the authentication.


## SSL/Certbot

Adding a new domain to same server:

```
certbot run --expand --nginx -d domain1 -d domain2 ...
```

Make sure the 'A' DNS record is properly pointing the correct location
before attempting to get a new certificate.

For me, it will likely ask if I want to expand an existing certificate,
do that. Pretty sure the `--extend` option will automatically do this
part.

Important file locations:

`/etc/letsencrypt/live/domain.com/fullchain.pem`

`/etc/letsencrypt/live/domain.com/privkey.pem`

This should add lines like:

```
server {
    server_name my_server.com

    # Added
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/db.command-cx.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/db.command-cx.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

# Whole block added
server {
    if ($host = my_server.com) {
      return 301 https://$host$request_uri;
    }

    server_name my_server.com
    listen 80;
    return 404
}
```

See <https://serverfault.com/questions/1107062/explain-certbots-https-redirect-configuration> for the reasoning on the "return 404" stuff of the http redirect block.

## SSL Testing

https://www.ssllabs.com/ssltest/index.html


## Vulnerabilities

There is the CRIME/BREACH attacks on compression within https.
This comes up with the `gzip on` directive.
It's been hard to determine whether my sites are really at risk.

## Config

```
listen address[:port] [default_server] [ssl]
listen port [default_server] [ssl]
```

## Request Processing

From <https://nginx.org/en/docs/http/request_processing.html>.

1. Decide which server should process request.
  1. First tests against `listen` directives
  2. Then tests against `server_name` directives using matching
     algorithm below
2. Handle the location

## Matching

1. Exact name
2. longest wildcard starting with '\*'
3. longest wildcard ending with '\*'
4. First matching regular expression (starts with '~' or )

PCRE regular expressions


## Reverse Proxy Notes with SkySpark

Was using nginx as a reverse proxy to send requests to multiple running webservers.
As a proxy, it didn't see to like having two public IPs being pointed to.
If I changed the proxy address to `localhost`, things worked fine.

## Test Configuration

Useful to test new updates before bringing down the web server.

```sh
sudo nginx -t
```

## Slashes or no Slashes on `location`s

<https://dev.to/danielkun/nginx-everything-about-proxypass-2ona#:~:text=A%20proxy_pass%20is%20usually%20used%20when%20there%20is,microservices%20that%20are%20responsible%20for%20the%20specific%20locations.>

General advice is to end with slash on everything.


```
# Note the slash at the end of the location and the proxy_pass
location /g/ {
    proxy_pass http://localhost:8080/;
}
```
