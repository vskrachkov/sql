##Learning SQL
Running bank databse:
```
docker run --name msql \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=bank \
    -e MYSQL_USER=vs \
    -e MYSQL_PASSWORD=strong_bank \
    -v /Users/vs/Documents/Draft/SQL/dumps:/docker-entrypoint-initdb.d \
    -v /Users/vs/Documents/Draft/SQL/dumps:/dumps \
    -v /Users/vs/Documents/Draft/SQL/datadir:/var/lib/mysql \
    -p 3306:3306 \
    -d mysql 
```
Running test database:
```
docker run --name msql_test \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=test \
    -e MYSQL_USER=vs \
    -e MYSQL_PASSWORD=strong_test \
    -p 3307:3306 \
    -d mysql 
```
where:

	--name -> docker container name
	-e MYSQL_ROOT_PASSWORD -> env variable that specify password for database root user
	-e MYSQL_DATABASE -> env variable that specify the name of database that will be created
	-e MYSQL_USER -> env variable that specify mysql user
	-e MYSQL_PASSWORD -> env var that specify mysql user password
	-v <host_path>:/docker-entrypoint-initdb.d  -> mounting host dir where initial data stores to container
	-p <host_port>:<container_port> -> expose container port to host machine
	-d mysql -> running container from mysql image in daemon mode
	
`datadir` folder is in gitignore, so create this directory on the same lavel as `scripts` and `dumps`, all databese files will be stored there.
Take in mind that if you change parameters with wich run docker containers you need also change them in `config.py`

For connecting to container shell:
  
    docker exec -it container-name bash
