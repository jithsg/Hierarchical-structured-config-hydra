import hydra
from omegaconf import DictConfig, OmegaConf
from dataclasses import dataclass, field

from hydra.core.config_store import ConfigStore
#import default_factory


@dataclass
class ExperimentConfig:
    name: str = "resnet18"
    epochs: int = 100
    batch_size: int = 32
    
@dataclass
class OptimizerConfig:
    name: str = "sgd"
    lr: float = .01
    momentum: float = 0.9
    

@dataclass
class MyConfig:
    experiment: ExperimentConfig = field(default_factory=ExperimentConfig)
    optimizer: OptimizerConfig = field(default_factory=OptimizerConfig)
    

cs = ConfigStore.instance()
# cs.store(name="config", node=ExperimentConfig)
# cs.store(name="sgd", node=OptimizerConfig)
cs.store(name="config", node=MyConfig)




@hydra.main(config_path="", config_name="config", version_base=None)
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))



if __name__ == "__main__":
    main()