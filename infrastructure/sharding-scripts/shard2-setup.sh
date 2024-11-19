#!/bin/bash

# Démarrer mongod en arrière-plan
mongod --shardsvr --replSet shard02ReplSet --port 27019 --bind_ip_all &

# Attendre que mongod soit prêt
until mongo --port 27019 --eval "db.adminCommand('ping')" >/dev/null 2>&1; do
  echo "Attente que shard02 soit prêt..."
  sleep 2
done

# Exécuter le script d'initialisation
mongo --port 27019 --eval 'rs.initiate({
  _id: "shard02ReplSet",
  members: [
    { _id: 0, host: "shard02:27019" }
  ]
})'

# Garder le conteneur en vie
wait