#!/bin/bash
cd "standalone_user_client"
docker-compose down
cd ".."
cd "standalone_db"
docker-compose down
cd ".."
cd "standalone_eventLog"
docker-compose down
cd ".."
cd "standalone_command"
docker-compose down
cd ".."
cd "standalone_channelrewards"
docker-compose down
cd ".."
cd "standalone_lights"
docker-compose down
cd ".."
cd "standalone_tts_core"
docker-compose down
cd ".."
cd "standalone_websource"
docker-compose down
cd ".."
cd "standalone_discord_script"
docker-compose down
cd ".."
cd "standalone_twitch_script"
docker-compose down
cd ".."
cd "standalone_twitch_pubsub"
docker-compose down
cd ".."