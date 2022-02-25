# The main repository of Praxis Bot can be found at: <https://github.com/TheCuriousNerd/Praxis-Bot>.
# Copyright (C) 2021

# Author Info Examples:
# Name / Email / Website
# Twitter / Twitch / Youtube

# Authors:
#   Alex Orid / inquiries@thecuriousnerd.com / TheCuriousNerd.com
#       Twitter: @TheCuriousNerd / Twitch: TheCuriousNerd / Youtube: thecuriousnerd / Github: TheCuriousNerd

# This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from enum import Enum
import badwords as badwords

credentialsNickname = "praxis_bot"

FORCE_Verify_Credentials = False

test_module: bool = False
user_module: bool = True

autoJoin_TwitchChannel = "thecuriousnerd"
autoJoin_TwitchChannels = ["thecuriousnerd"]
allowedCommandsList_TwitchPowerUsers = ["thecuriousnerd"]
allowedTTS_List = ["thecuriousnerd", "<@!76078763984551936>", "<@76078763984551936>", "76078763984551936"]
adminUsers_List = ["thecuriousnerd", "<@!76078763984551936>", "<@76078763984551936>", "76078763984551936"]

raidTeamIDs = [76078763984551936]

#Twitch Module Configs
block_TwitchChannelsMessaging = [""] # Blocks the ability to send messages to twitch channels
blockAll_TwitchChatChannelsMessaging = False # Blocks the ability to send messages to twitch channels

autoEnabled_TwitchTTS = False # Enables TTS for ALL
autoEnabled_TwitchTTS_SpeakersList_Only = False # Enables TTS for Allowed TTS List Only

#Discord Module Configs
block_DiscordChannelsMessaging = [""] # Blocks the ability to send messages to Discord channels
blockAll_DiscordChannelsMessaging = False # Blocks the ability to send messages to Discord channels
blockAll_DiscordPrivateMessaging = False # Private Messaging not yet implemented


autoEnabled_DiscordChannelsTTS = True
selected_DiscordTTSChannels = ["431129571308339210"]
block_DiscordChannelsTTS = [""] # block supersedes the tts_enabled bool
blockAll_DiscordChannelsTTS = False # blockAll supersedes the force bool and force list and tts_enabled bool
force_DiscordChannelsTTS = [""] # force supersedes the block list
forceAll_DiscordChatChannelsTTS = False # forceAll supersedes the blockAll bool and block list and force list


#User Module Configs
blockAll_TTS_URL_UserModule = True

#Chyron Module Configs
chyronListSpaceCount = 25

#Lights Module Configs
colorParse_maxDigits = 4


#General Configs
skip_splashScreen = False
skip_splashScreenClear = False
skip_splashScreenSleep = False

botList = ("Nightbot", "StreamElements", "Moobot", "Praxis Bot", "praxis_bot", "MEE6 +", "Nerdy", "Rythm", "Groovy")

class FileNameStrategy(Enum):
    TIME_BASED = 1
    CONTENT_BASED = 2

fileNameStrategy = FileNameStrategy.CONTENT_BASED

#OLD CLASS WILL DELETE
class DBStrategy(Enum):
    SQLite = 1
    MySQL = 2
#OLD CONFIGS WILL BE DELETED SOON
#dbStrategy = DBStrategy.SQLite

#TTS Configs
is_tts_Speaker_Enabled = False
is_tts_URL_Blocked = True

is_tts_Speaker_forDiscord_Enabled = False

class Speaker(Enum):
    GOOGLE_TEXT_TO_SPEECH = 1

currentSpeaker = Speaker.GOOGLE_TEXT_TO_SPEECH


#Networking Configs (Unused are commented out)
standalone_channelrewards_address = "standalone_channelrewards"
standalone_channelrewards_port = "42069"
standalone_command_address = "standalone_command"
standalone_command_port = "42010"
standalone_db_address = "standalone_db"
standalone_db_port = "42002"
#standalone_discord_script_address = "standalone_discord_script"
#standalone_discord_script_port = "NONE"
standalone_eventLog_address = "standalone_eventlog"
standalone_eventLog_port = "42008"

standalone_lights_address = "standalone_lights"
standalone_lights_port = "42042"
#standalone_obsWebSocket_address = "standalone_obsWebSocket"
#standalone_obsWebSocket_port = "NONE"

standalone_tts_core_address = "standalone_tts_core"
standalone_tts_core_port = "42064"
tts_speaker_address = "192.168.191.208"
tts_speaker_port = "40085"
tts_speakers = [{"ip":"192.168.191.208", "port":"40085"}]


#standalone_twitch_script_address = "standalone_twitch_script"
#standalone_twitch_script_port = "NONE"
#standalone_twitch_pubsub_address = "standalone_twitch_pubsub"
#standalone_twitch_pubsub_port = "NONE"

standalone_user_client_address = "standalone_user_client"
standalone_user_client_port = "42055"
standalone_websource_address = "standalone_websource"


#Misc Configs
slurList = badwords.slurList

praxisVersion_Alpha = "2 " #Build
praxisVersion_Delta = "0 " #Minor
praxisVersion_Omega = "1 " #Major
