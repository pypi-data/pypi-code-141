import abc
from typing import Any, Dict, Union

import gym.spaces as spaces
import numpy as np
import torch


class BasePolicy(abc.ABC):
    """
    Defines core policy functionality for policies to be compatible with multiple code bases.
    """

    def act(
        self,
        obs: Union[torch.Tensor, Dict[str, torch.Tensor]],
        hxs: torch.Tensor,
        masks: torch.Tensor,
        is_eval: bool = False,
    ) -> Dict[str, Any]:
        """
        :returns: Dictionary at least with keys (can include more information
            as needed, such as action log probabilities):
            "actions": torch.Tensor of shape [batch_size, action_dim]
            "hxs": torch.Tensor of shape [batch_size, D] for hidden dimension size D.
        """
        raise NotImplementedError()


class RandomPolicy(BasePolicy):
    def __init__(self, action_space: spaces.Space):
        self._action_space = action_space

    def act(self, obs, hxs, masks, is_eval=False) -> Dict[str, Any]:
        action = torch.tensor(
            np.array([self._action_space.sample() for _ in range(obs.size(0))])
        )

        return {"actions": action, "hxs": hxs}
