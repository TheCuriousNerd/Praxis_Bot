# The main repository of Praxis Bot can be found at: <https://github.com/TheCuriousNerd/Praxis-Bot>.
# Copyright (C) 2021

# Author Info Examples:
#   Name / Email / Website
#       Twitter / Twitch / Youtube / Github

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

import config
from abc import ABCMeta

from channel_rewards.channelRewards_base import AbstractChannelRewards

from json import loads
from urllib.parse import urlencode
import requests

import threading

import random

class ChannelReward_Workout_Pushups(AbstractChannelRewards, metaclass=ABCMeta):
    """
    this is the Do 20 push-ups reward.
    """
    ChannelRewardName = "Do 20 push-ups"

    def __init__(self):
        super().__init__(ChannelReward_Workout_Pushups.ChannelRewardName, n_args=1, ChannelRewardType=AbstractChannelRewards.ChannelRewardsType.channelPoints)
        self.help = ["This is a Do 20 push-ups channel point reward."]
        self.isChannelRewardEnabled = True
        self.threads = []

    def do_ChannelReward(self, source = AbstractChannelRewards.ChannelRewardsSource.default, user = "User",  rewardName = "", rewardPrompt = "", userInput = "", bonusData = None):

        #print("sending:",user, 16, "!lights hydration")
        try:
            #if self.is_ChannelReward_enabled:
            #    thread_ = threading.Thread(target=self.send_Lights_Command, args=(user, 16, "!lights hydration", ""))
            #    thread_.daemon = True
            #    self.threads.append(thread_)
            #    thread_.start()
            if self.is_ChannelReward_enabled:
                prompt_ = self.get_Phrase(" wants The Curious Nerd, to do 20 pushups")
                thread_ = threading.Thread(target=self.send_TTS, args=("", user + prompt_))
                thread_.daemon = True
                self.threads.append(thread_)
                thread_.start()
        except:
            pass

        return None

    def send_Lights_Command(self, username, light_group, command, rest):
        # todo need to url-escape command and rest
        params = urlencode({'user_name': username, 'light_group': light_group, 'command': command, 'rest':rest})
        #standalone_lights
        url = "http://%s:%s/api/v1/exec_lights?%s" % (config.standalone_lights_address[0].get("ip"), config.standalone_lights_address[0].get("port"), params)
        resp = requests.get(url)
        if resp.status_code == 200:
            print("Got the following message: %s" % resp.text)
            data = loads(resp.text)
            msg = data['message']
            if msg is not None:
                return msg
                # todo send to logger and other relevent services
        else:
            # todo handle failed requests
            pass

    def send_TTS(self, username, message):
        params = urlencode({'tts_sender': username, 'tts_text': message})
        #standalone_tts_core
        url = "http://%s:%s/api/v1/tts/send_text?%s" % (config.standalone_tts_core_address[0].get("ip"), config.standalone_tts_core_address[0].get("port"), params)
        resp = requests.get(url)
        if resp.status_code == 200:
            print("Got the following message: %s" % resp.text)
            data = loads(resp.text)
            msg = data['message']
            if msg is not None:
                return msg
                # todo send to logger and other relevent services
        else:
            # todo handle failed requests
            pass

    def get_Phrase(self, defaultRewardPrompt,
    phrases = [" demands that The Curious Nerd, to do 20 pushups "]):

        phrases.append(defaultRewardPrompt)
        totalPhrases = len(phrases) - 1
        targetPhrase = phrases[random.randint(0,totalPhrases)]
        return targetPhrase

    def get_help(self):
        return self.help