# nginx

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
