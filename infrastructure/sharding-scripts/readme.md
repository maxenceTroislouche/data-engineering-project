# Activer le sharding
docker exec -it mongos mongo

# Activer le sharding sur une db
sh.enableSharding("<database>")

# Activer le sharding sur une collection
sh.shardCollection("<database>.<collection>", {"<shardField>": "hashed"})
=> mettre en shardField à _id comme ça pas besoin de mettre un field en plus.

# Regarder la répartition
db["<collection>"].getShardDistribution()