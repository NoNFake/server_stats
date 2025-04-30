## build

```bash
sudo docker-compose up -d
```

## logs

```bash
sudo docker logs server
```

## restart

```bash
sudo docker stop server
sudo docker start server
```

## stop the running container

```bash
sudo docker-compose down
sudo docker-compose stop

# and rebuild
sudo docker-compose build --no-cache
```
