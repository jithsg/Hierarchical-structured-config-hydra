import hydra
from omegaconf import DictConfig, OmegaConf, MISSING
from pydantic.dataclasses import dataclass
from typing import Any

from hydra.core.config_store import ConfigStore
#import default_factory

@dataclass
class ExperimentSchema:
    model: str = MISSING
    nrof_epochs: int = 10
    learning_rate: float = 0.001

@dataclass
class Resnet18ConfigSchema(ExperimentSchema):
    model: str = "resnet18"
@dataclass
class Resnet30ConfigSchema(ExperimentSchema):
    model: str = "resnet30"
 
@dataclass
class ConfigSchema:
    experiment: Any
    
cs= ConfigStore.instance()

cs.store(name="config_schema", node=ConfigSchema)
cs.store(group="experiment", name="resnet18_schema", node=Resnet18ConfigSchema)
cs.store(group="experiment", name="resnet30_schema", node=Resnet30ConfigSchema)

@hydra.main(config_path="configs", config_name="config", version_base=None)
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))



if __name__ == "__main__":
    main()