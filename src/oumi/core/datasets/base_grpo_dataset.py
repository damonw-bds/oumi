# Copyright 2025 - Oumi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional, Union

import pandas as pd
from typing_extensions import override

from oumi.core.datasets.base_map_dataset import BaseMapDataset
from oumi.core.tokenizers.base_tokenizer import BaseTokenizer

_PROMPT_KEY = "prompt"
_COMPLETION_KEY = "completion"


class BaseExperimentalGrpoDataset(BaseMapDataset):
    """Preprocess the GRPO samples to the Oumi format.

    Warning:
        This class is experimental and subject to change.
    """

    def __init__(
        self,
        *,
        dataset_name: Optional[str] = None,
        dataset_path: Optional[str] = None,
        split: Optional[str] = None,
        tokenizer: Optional[BaseTokenizer] = None,
        return_tensors: bool = False,
        **kwargs,
    ) -> None:
        """Initializes a new instance of the BaseExperimentalGrpoDataset class."""
        super().__init__(
            dataset_name=dataset_name,
            dataset_path=dataset_path,
            split=split,
            **kwargs,
        )

        if return_tensors:
            raise NotImplementedError(
                "return_tensors=True is not implemented for this class"
            )

        self._tokenizer = tokenizer
        self._return_tensors = return_tensors

        self._data = self._load_data()

    @staticmethod
    def _process_text_value(s: str) -> str:
        # The data contains occasional `\n` at the beginning or end
        # of text values. Let's strip them.
        return s.strip() if s else ""

    def transform_grpo_example(self, example: Union[dict, pd.Series]) -> dict:
        """Validate and transform the GRPO sample into Python `dict`."""
        for required_key in (_PROMPT_KEY, _COMPLETION_KEY):
            if required_key not in example:
                raise ValueError(
                    f"Example doesn't contain '{required_key}'. "
                    f"Actual keys: {sorted(example.keys())}"
                )

        prompt = example[_PROMPT_KEY] or ""
        completion = example[_COMPLETION_KEY] or ""

        if not isinstance(prompt, str):
            raise ValueError(
                f"Example '{_PROMPT_KEY}' must be a string. Actual type: {type(prompt)}"
            )
        elif not isinstance(completion, str):
            raise ValueError(
                f"Example '{_COMPLETION_KEY}' must be a string. "
                f"Actual type: {type(completion)}"
            )

        return {
            _PROMPT_KEY: self._process_text_value(prompt),
            _COMPLETION_KEY: self._process_text_value(completion),
        }

    @override
    def transform(self, sample: pd.Series) -> dict:
        """Validate and transform the sample into Python `dict`."""
        return self.transform_grpo_example(sample)
