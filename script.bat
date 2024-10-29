@echo off
echo Parando todos os containers...
docker stop $(docker ps -aq)

echo Removendo todos os containers...
docker rm $(docker ps -aq)

echo Removendo todos os volumes...
docker volume rm $(docker volume ls -q)

echo Removendo todas as redes...
docker network rm $(docker network ls -q)

echo Realizando limpeza geral do Docker...
docker system prune -a --volumes -f

echo Limpeza completa! Todos os containers, volumes, redes e imagens foram removidos.
pause
