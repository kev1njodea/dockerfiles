# rclone

- https://github.com/rclone/rclone

## WebDAV

Default compose file sets up a WebDAV server.

### Create accounts

Create a username/pw in a **new** `.htpasswd`
- `htpasswd -c ./auth/.htpasswd username`

Create a username/pw in an **existing** `.htpasswd`
- `htpasswd ./auth/.htpasswd username`

Delete a username/pw in an **existing** `.htpasswd`
- Open the `.htpasswd` file, delete the line, save
