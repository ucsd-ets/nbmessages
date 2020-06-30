"""Configuration"""

from .utils import load_yaml
import yaml

CONFIG_FILE = '/etc/nbmessage-board/nbmessage-board-config.yaml'


class Config:
    """Representation of the config file"""
    def __init__(self):
        self._configs = load_yaml(CONFIG_FILE)
    
    def _save(self) -> None:
        with open(CONFIG_FILE, 'w') as f:
            yaml.dump(self._configs, f, default_flow_style=False)

    @property
    def config(self) -> dict:
        """Get the config file as a dict

        Returns:
            dict -- config file fields + values
        """
        return self._configs
    
    def update_config(self, kv: dict):
        """Overwrite what's in the config file

        Arguments:
            kv {dict} -- The new config file object representation
        """
        self._configs.update(kv)
        self._save()

