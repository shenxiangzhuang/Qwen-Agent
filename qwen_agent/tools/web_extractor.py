from typing import Union

import requests

from qwen_agent.tools.base import BaseTool, register_tool


@register_tool('web_extractor')
class WebExtractor(BaseTool):
    description = '根据网页URL，获取网页内容的工具'
    parameters = [{
        'name': 'url',
        'type': 'string',
        'description': '网页URL',
        'required': True
    }]

    def call(self, params: Union[str, dict], **kwargs) -> str:
        params = self._verify_json_format_args(params)

        url = params['url']
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return ''
