echo "Creating Praxis Bot Images..."

start powershell docker build --file ./standalone-user-client/Dockerfile --tag standalone-user-client .
start powershell docker build --file ./standalone-db/Dockerfile --tag standalone-db .
start powershell docker build --file ./standalone-eventlog/Dockerfile --tag standalone-eventlog .
start powershell docker build --file ./standalone-channelrewards/Dockerfile --tag standalone-channelrewards .
start powershell docker build --file ./standalone-command/Dockerfile --tag standalone-command .
start powershell docker build --file ./standalone-lights/Dockerfile --tag standalone-lights .
start powershell docker build --file ./standalone-tts-core/Dockerfile --tag standalone-tts-core .
start powershell docker build --file ./standalone-websource/Dockerfile --tag standalone-websource .
start powershell docker build --file ./standalone-discord-script/Dockerfile --tag standalone-discord-script .
start powershell docker build --file ./standalone-twitch-script/Dockerfile --tag standalone-twitch-script .
start powershell docker build --file ./standalone-twitch-pubsub/Dockerfile --tag standalone-twitch-pubsub .
