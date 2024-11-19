#!/bin/bash

# Attendre que les config servers soient prêts
until mongo --host configsvr01 --port 27017 --eval "db.adminCommand('ping')" >/dev/null 2>&1; do
  echo "Attente que configsvr01 soit prêt..."
  sleep 2
done

# Démarrer mongos en arrière-plan
mongos --configdb configReplSet/configsvr01:27017 --bind_ip_all &

# Attendre que mongos soit prêt
until mongo --eval "db.adminCommand('ping')" >/dev/null 2>&1; do
  echo "Attente que mongos soit prêt..."
  sleep 2
done

# Exécuter le script d'initialisation
sleep 30  # Attend que les autres serveurs soit prêts
mongo --eval '
  sh.addShard("shard01ReplSet/shard01:27018");
  sh.addShard("shard02ReplSet/shard02:27019");
'
# Garder le conteneur en vie
wait