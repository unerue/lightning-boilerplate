# ⚡lightning-boilerplate

<div align="center">

[![python](https://img.shields.io/badge/-Python_3.9_%7C_3.10_%7C_3.11-255074?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![poetry](https://img.shields.io/badge/-Poetry_1.6+-1e293b?logo=poetry&logoColor=white)](https://python-poetry.org/)
[![pytorch](https://img.shields.io/badge/PyTorch_2.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![cuda](https://img.shields.io/badge/-CUDA_10.7_%7C_10.8_%7C_12.1-91c733?logo=cuda&logoColor=white)](https://pytorch.org/get-started/previous-versions/)
[![lightning](https://img.shields.io/badge/-Lightning_2.0+-792ee5?logo=pytorchlightning&logoColor=white)](https://pytorchlightning.ai/)
[![hydra](https://img.shields.io/badge/Hydra_1.3+-89b8cf)](https://hydra.cc/)
[![hydra](https://img.shields.io/github/contributors/unerue/lightning-boilerplate.svg)](https://github.com/unerue/lightning-boilerplate/graphs/contributors)

</div>

<h4 align="center">
  <p>
    English |
    <a href="https://github.com/unerue/lightning-boilerplate/blob/develop/README.kr.md">한국어</a>
  </p>
</h4>

**Lightning Boilerplate**는 [**lightning-hydra-template**](https://github.com/ashleve/lightning-hydra-template)에서 영감을 받았습니다. `lightning`과 `hydra`를 사용하여 머신러닝/딥러닝 연구자/엔지니어들이 `sklearn`과 `torch`로 연구개발을 효율적으로 수행할 수 있도록 지원합니다. 해당 템플릿은 Python 3.9 이상([PEP 585](https://peps.python.org/pep-0585/))을 지원하며 추천하는 개발환경은 `conda`가 아닌 `pyenv`와 `poetry`입니다.

### Table of Contents

1. [Prerequisites](#⚙-Prerequisites)
2. [Usage of Lightning Boilerplate](#🚀-Usage-of-Lightning-Boilerplate)
3. [Package Version Management with Poetry](#Package-Version-Management-with-Poetry)
4. [Contribution](#Contribution)

#### TODO

- [ ] Documentation in English
- [ ] scikit-learn template with hydra-config
- [ ] PyTorch native template with hydra-config
- [ ] Lightning with video files

## ⚙ Prerequisites

### Development Environment (recommended)

해당 템플릿을 이용해 딥러닝 모형 개발에는 `pyenv`와 `poetry`를 사용합니다. 아래의 절차대로 설치하시기 바랍니다(`conda` 환경은 고려하지 않음).

#### pyenv

`pyenv`는 사용하는 운영체제에 따라 [맥/리눅스](https://github.com/pyenv/pyenv#installation) 또는 [윈도우](https://github.com/pyenv-win/pyenv-win#installation) 버전을 설치하는 방법을 참고하여 파이썬 버전을 관리하시기 바랍니다. 예제는 우분투를 기반으로 합니다.

```bash
curl https://pyenv.run | bash
```

#### Poetry

해당 템플릿은 파이썬 의존성 라이브러리 관리툴인 `poetry`를 사용합니다. Linux, macOS, Windows (PS), Windows (WSL) [설치 방법](https://python-poetry.org/docs/#installing-with-the-official-installer)를 참고하여 의존성을 관리하시기 바랍니다.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

<details>
<summary><b>Anaconda (Not recommended)</b></summary>

에휴...ㅜ

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

</details>

### Optional

<details>
<summary><b>Docker</b></summary>

도커 환경에서 사용하실 분들은 [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) 설치 후 [NGC]()가 아닌 [Docker Hub](https://hub.docker.com/r/pytorch/pytorch/tags)에서 사용할 `CUDA`와 `torch` 버전의 이미지로 컨테이너를 생성하시면 됩니다.

```bash
docker pull pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel
```

</details>

<details>
<summary><b>Visual Studio Code</b></summary>

Python linter로 [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)를 설치합니다.

</details>

## 🚀 Usage of Lightning Boilerplate

해당 템플릿을 `clone`하고 `pyproject.toml` 내에 명시된 파이썬 버전과 시멘틱 버저닝(semantic versioning)을 확인한 다음 `poetry install` 명령어를 실행하여 기본 라이브러리를 설치합니다. `git remote remove origin`을 실행하여 원격 저장소와의 연결을 종료합니다.

```bash
git clone --depth 1 --branch main https://github.com/unerue/lightning-boilerplate.git ${your-project-name}
cd ${your-project-name}
git remote remove origin
poetry install
```

항상 `python` 버전을 확인하고, `torch`와 `cuda`의 버전을 확인하거나 아래와 같이 최신 버전을 쓰기 위해 버전을 설정하시기 바랍니다. 해당 템플릿은 `cuda 11.7`, `torch 2.0.1` 버전입니다. 다음은 `cuda 11.8` 버전으로 `torch`를 설치하기 위한 예시입니다. `poetry install` 명령어를 수행하기 전, `pyproject.toml` 파일을 수정하여 설치하시기 바랍니다.

```toml
[tool.poetry.dependencies]
python = "3.11.*"
torch = {version = "2.1.0+cu118", source = "pytorch"}
torchvision = {version = "0.16.0+cu118", source = "pytorch"}
torchaudio = {version = "2.1.0+cu118", source = "pytorch"}

[[tool.poetry.source]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu118"
priority = "explicit"
```

본 템플릿은 `poetry`를 기반으로 작동됩니다. `poetry`의 자세한 사용법은 문서를 참고하세요. `conda`나 `virtualenv`라면 `python` 명령어로 실행합니다.

```bash
poetry run pytest
poetry run python src/train.py trainer=gpu
```

명령어줄(command line)에서 설정(config) 매개변수 오버라이드(override)는 다음과 같습니다.

```bash
poetry run python src/train.py trainer.max_epochs=20
```

미리 설정하지 않은 매개변수는 아래와 같이 추가합니다.

```bash
poetry run python src/train.py +trainer.new_arg="value"
```

작업 디렉토리 구조는 다음과 같습니다:

```bash
├── .github                 # GitHub Actions workflows
├── .vscode                 # VSCODE configs
├── configs                 # Hydra configs
│   ├── callbacks             # callback configs
│   ├── data                  # DataModule and dataset configs
│   ├── debug                 # debugging configs
│   ├── experiment            # experiment configs
│   ├── extras                # extra utilities configs
│   ├── hydra                 # Hydra configs
│   ├── loggers               # logger configs
│   ├── model                 # model configs
│   ├── paths                 # project paths configs
│   ├── trainer               # trainer configs
│   ├── eval.yaml           # main config for evaluation
│   └── train.yaml          # main config for training
│
├── data                    # dataset
├── logs                    # logs generated by hydra and lightning loggers
├── src                     # source code
│   ├── data                  # dataset scripts
│   ├── models                # model scripts
│   ├── utils                 # utility scripts
│   ├── eval.py               # run evaluation
│   └── train.py              # run training
│
├── tests                   # pytest
│
├── .gitignore                # list of files ignored by git
├── .pre-commit-config.yaml   # configuration of pre-commit hooks for code formatting
├── .project-root             # file for inferring the position of project root directory
├── Makefile                  # Makefile with commands like `make train` or `make test`
├── poetry.lock               # Poetry dependencies lock file
├── poetry.toml               # Poetry local config file
├── pyproject.toml            # configuration options for testing and linting
└── README.md
```

### Build your model with lightning

`src` 폴더에 있는 구조에 맞게 `lightning`과 `torch`를 사용하여 모델링하십시오. `train.py`과 `eval.py` 스크립트는 수정할 필요가 없을 겁니다. `datamodule.py`와 `model.py` 만 선언하면 됩니다. 파이썬 스크립트에 인자를 선언한다음 `configs/model/default.yaml` 파일에 인자들의 임포팅할 모듈들을 `_target_`에 선언해주면 됩니다. 다만, `_target_`에 선언 시 예를 들어, `optimizer`의 경우, 모형의 파라미터를 첫번째 인자값으로 지정해줘야 작동되기지만 해당 `.yaml`에는 모형 파라미터를 입력하기 전에 선언되기때문에 `partial`로 통해 미리 공간을 잡아 둡니다. `partial`을 `true`로 설정해주시면 됩니다.

```python
# src/model.py
class MyModel(LightningModule):
    def __init__(self, model, optimizer, scheduler):
        ...
```

```yaml
# configs/model/default.yaml
_target_: src.model.MyModel
optimizer:
  _target_: torch.optim.Adam
  partial: true
  lr: 1e-3
```

#### Lighting trainer API

`lightning`에 대한 자세한 훅들은 [공식 문서](https://lightning.ai/docs/pytorch/latest/common/trainer.html#trainer-class-api)를 참고하십시오.


### Before push your repository

`pre-commit`으로 훅(hook)으로 작성한 코드를 자동으로 formatter, linter, 보안 등 코드 내 잠재하고 있는 문제점을 찾아내기 위한 도구이다. `poetry install`을 했다는 가정하에:

```bash
poetry run pre-commit install
```

`pre-commit install` 명령어를 통해 `pre-commit-config.yaml` 파일에 미리 설정된 훅들을 설치하고 차후 `git commit`에 따른 코드를 자동으로 수정해줍니다.

## Poetry package installation

`poetry` 사용해 프로젝트 초기화 및 파이토치 등 라이브러리 설치 방법은 다음과 같습니다. `pyenv`로 파이썬 전역 버전을 설정합니다. 아래는 `poetry`로 해당 템플릿이 아닌 다른 프로젝트에서도 사용할 수 있는 간단한 사용방법을 설명합니다.

<details>
<summary><b>Basic poetry usage</b></summary>

`poetry`` 기초 사용 방법은 다음과 같습니다.

```bash
pyenv install 3.10.13 # Windows 3.10.10
pyenv global 3.10.13
```

`git clone`으로 만들어진 폴더로 진입해 프로젝트를 초기화합니다.
* 작업 폴더 내에서 `poetry`를 초기화한다. 초기화 시 PEP에 따라 `pyproject.toml`이 생성됩니다.
* 작업 폴더 내 패키지관리(e.g. JS의 node_modules)와 같이 라이브러리를 관리하고 싶다면 `virtualenvs.in-project`를 `true`로 설정하고 해당 파일을 `--local`로 저장한다. 저장된 로컬 설정파일은 `poetry.toml`입니다.

```bash
poetry init
poetry config virtualenvs.in-project true --local
poetry run python --version
```

초기화로 생성된 `pyproject.toml` 파일에 `[tool.poetry.dependencies]`의 파이썬 버전을 `python = "3.10.*"`으로 변경합니다. 파이토치를 설치하기 전 소스 경로를 추가합니다. 원하는 버전은 [이전 버전](https://pytorch.org/get-started/previous-versions/)에서 확인한 다음 설치합니다.

```bash
poetry source add -p explicit pytorch https://download.pytorch.org/whl/cu117
poetry add --source pytorch torch torchvision
poetry run python -c "import torch;print(torch.cuda.is_available())"
```

### Lightning and dev package installation

* `poetry`는 라이브러리를 다양한 그룹으로 관리할 수 있습니다. 서비스와 상관없이 개발에만 필요한 패키지라면 `--group`인자를 통해 그룹명을 지정한 다음 배포 시 해당 라이브러리를 배제하고 배포가능합니다.

```bash
poetry add lightning hydra-core hydra-colorlog rootutils rich python-dotenv
poetry add pytest black mypy isort pre-commit --group dev
```

</details>


## Package Version Management with Poetry

<details>
<summary><b>Exact version</b></summary>
If you don't include any modifiers, Poetry will keep your dependency pinned at that exact version.

> beepboop = "2.1.7"

With that configuration, if a new version of beepboop is released, poetry update will not install it.
</details>

<details>
<summary><b>Caret version</b></summary>
If you use the caret `^` character, Poetry will update to any new version that does not change the leftmost non-zero section.

> beepboop = "^2.1.7"

Equivalent to >=2.1.7, \<3.0.0

With the configuration above, poetry update would update beepboop to 2.1.8, 2.2, 2.3, etc. Poetry would not update to beepboop 3.0, because that changes the leftmost non-zero section of the version number from 2 to 3.

> zeepzorp = "^0.24.1"

Equivalent to >=0.24.1, \<0.25.0

With the configuration above, poetry update would update zeepzorp to 0.24.2. Poetry would not update to zeepzorp 0.25.0, because that changes the leftmost non-zero section of the version number from 24 to 25.

The caret version modifier is pretty aggressive about which upgraded versions are allowed. This can cause problems if the maintainers of your dependencies introduce breaking changes without incrementing the major version number.
</details>

<details>
<summary><b>Tilde version</b></summary>
The tilde ~ character tells Poetry to allow minor updates. If you specify a major, minor, and patch version, only patch-level changes are allowed. If you specify a major and minor version, again only patch-level changes are allowed. If you specify only a major version, then minor- and patch-level changes are allowed.

> beepboop = "~2.1.7"

Equivalent to >=2.1.7, \<2.2.0

> beepboop = "~2.1"

Equivalent to >=2.1.0, \<2.2.0

> beepboop = "~2"

Equivalent to >=2.0.0, \<3.0.0
The tilde version modifier is less aggressive than the caret version modifier in the upgrades it will allow.
</details>

<details>
<summary><b>Wildcard version</b></summary>
The star * character is a wildcard. Any version number is allowed at the wildcard position.

> beepboop = "2.1.\*"

Equivalent to >=2.1.0, \<2.2.0

> beepboop = "2.\*"

Equivalent to >=2.0.0, \<3.0.0

> beepboop = "\*"

Allows any version. Equivalent to >=0.0.0
</details>
