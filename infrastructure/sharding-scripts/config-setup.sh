#!/bin/bash

# Démarrer mongod en arrière-plan
mongod --configsvr --replSet configReplSet --port 27017 --bind_ip_all &


until mongo --eval "db.adminCommand('ping')" >/dev/null 2>&1; do
    echo "Attente que mongo soit prêt"
    sleep 2
done


mongo --eval 'rs.initiate({
    _id: "configReplSet",
    configsvr: true,
    members: [
        { _id: 0, host: "configsvr01:27017" }
    ]
    })'

wait