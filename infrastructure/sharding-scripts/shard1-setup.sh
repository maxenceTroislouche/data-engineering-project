#!/bin/bash


# Démarrer mongod en arrière-plan
mongod --shardsvr --replSet shard01ReplSet --port 27018 --bind_ip_all &

# Attendre que mongod soit prêt
until mongo --port 27018 --eval "db.adminCommand('ping')" >/dev/null 2>&1; do
  echo "Attente que shard01 soit prêt..."
  sleep 2
done

mongo --port 27018 --eval 'rs.initiate({
  _id: "shard01ReplSet",
  members: [
    { _id: 0, host: "shard01:27018" }
  ]
})'

# Garder le conteneur en vie
wait