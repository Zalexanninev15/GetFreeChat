#!/usr/bin/env python3

# Script to get the current list of providers
# Copyright (C) 2023-2025 Zalexanninev15

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
import os
import requests

gpt_list = [
    'https://raw.githubusercontent.com/xtekky/gpt4free/main/README.md',
    'https://raw.githubusercontent.com/LiLittleCat/awesome-free-chatgpt/main/urls.json',
    'https://raw.githubusercontent.com/xx025/carrot/main/README.md',
    'https://raw.githubusercontent.com/zukixa/cool-ai-stuff/main/README.md'
]

first = True
unique_urls = []

for url in gpt_list:
    file_name = str(url.split('/')[-1])

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(response.text)
        else:
            print(
                f'Error {response.status_code}:Failed to download file. URL: {url}')
            break

        links = []

        with open(file_name, 'r', encoding='utf-8') as f:
            urls = f.readlines()

        for s in urls:
            if '![Active]' in s:
                links.append(s.split('|')[1].split('(')[1][:-2])

        if len(links) == 0:
            links = re.findall('"(https?://.*?)"', ' '.join(urls))

        for url1 in links:
            url1 = url1.strip('"')
            if url1 not in unique_urls:
                if first:
                    unique_urls.append(url1.replace(")", ''))
                    first = False
                else:
                    unique_urls.append(url1.replace(")", ''))

    except Exception as e:
        print(f'Error processing URL: {str(e)}')

    os.remove(file_name)

result = list(set(x for x in unique_urls if not any(substring in x for substring in
                                                    ['huggingface.co/chat', 'star-history', 'docs', 'api', 'bing', 'openai', '.ico', '.webp',
                                                     'getgpt', 'chatgpt.ch', 'awesome', 'favicon',
                                                     'chatgpt.org', 'cgs.skybyte.me', 'www.aitianhu.com',
                                                     'chatgpt.ai', 'powerchat.', 'p.aifree.site', 'gptgo.ai', 'ai.heptax.com', 'carrot',
                                                     'hteyun.com', 'chat.pinkfong.cn', 'c.newstop.uk', 'ai.zenglingkun.cn', '.png', '.jpg',
                                                     'nav4ai.net', 'coffeecat', 'chat.51buygpt.com', 'ai.mcbbs.gq', 'gptdidi.com', 'github', 'donate',
                                                     'chat.leadscloud.xyz', 'g01.plitun.com', 'www.chatbotui.com', 'freegpt.dingtoucake.xyz'
                                                     'academic.aiearth.dev', 'chat2.xeasy.me', 'www.chatfree.cc', 'wiki',
                                                     'www.devgpt.com', 'a.aiask.me', 'mirrorchat.extkj.cn', 'chatyou.lovebaby.today', '.svg',
                                                     'chat1.manongzyg.one', 'chat.iwoso.co', 'freegpts1.aifree.site', 'suspended-website.com',
                                                     'nb.aitom.cc', '94gpt.com', 'chat.newstop.asia', 'ai.azstudio.top',
                                                     'xjai.cc', 'chatgpt.kiask.xyz', 'aichat.gogpt.site', 'chatgpt.bybyte.cn', 'vvanglro.eu.org',
                                                     'gpt.xeasy.me', 'bettergpt.chat', 'chat.aisoftworks.com', 'hashnode.com', 'www.typingmind.com',
                                                     'www.magicaibot.com', 'chat-shared2.zhile.io', 'home.cutim.top', 'ailink.icu', 'bard.google.com',
                                                     'discord', 'x.com', 't.me', 'file', 'static', 'slack', 'opencopilot',
                                                     'phind', 'deepinfra', 'apps.apple.com', 'play.google.com', 'repositori'])))

with open('providers.txt', 'w') as file:
    file.write('\n'.join(result))

print('Processing is complete.')
