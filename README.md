

1. For running Elastic+Kibana only, use:
docker-compose -f elasticsearch.yml up -d

do not forget check free memory or switch on swap, if required:
fallocate -l <N>G /tmp/swap
mkswap /tmp/swap
...edit /etc/fstab:
/tmp/swap swap swap default 0 0
sudo chmod 0600 /tmp/swap
sudo chown root:roor /tmp/swap
sudo swapon -a

2. For running Minecraft server + Filebeat, use:
docker-compose -f minecraft-filebeat.yml up -d

in this case Filebeat search Elasticsearch host in env variable ELASTICSEARCH_HOST, which
can be setted up in .env file

3. For running all-in-one, use docker-compose.yml config

