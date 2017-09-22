# Learn Docker in 12 Minutes

Create the folowing directory structure
```.
├── Dockerfile
└── src
    └── index.php
```
### index.php
```php
<?php
echo "Hello World";
?>
```
### Dockefile

```Dockerfile
FROM php:7.0-apache
COPY src /var/www/html
EXPOSE 80                             
```

### Build a Docker image
```bash
docker build -t php-sample
```

### Spin up a container
```bash
docker run -p 80:80 php-sample  
```

## Using Volumes
Volumes lets you share folders between the host and a container. A local directory in the host is 
mounted as a volume in the container.

```bash
docker run -p 80:80 -v /home/menuka/Documents/temp/src/:/var/www//html/ php-sample
```
