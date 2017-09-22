# Learn Docker in 12 Minutes (<a target="https://youtu.be/YFl2mCHdv24">Video</a>)

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
docker run -p 80:80 -v /home/menuka/Documents/temp/src/:/var/www/html/ php-sample
```

### Notes
* Containers will stop by themselves when the main process exits
* In this it would only be if PHP died for some unexpected reason
* You might have a container which runs tests or a container which run composer install
* The process running in these containers will end when the task is complete
* For the reason you should endeavor to have one process per container because the life of that container is tied directly to a single process. So you don't want five other things going on in the background that will all be brought down without warning when the main process stops