# ⚡lightning-boilerplate

[![python](https://img.shields.io/badge/-Python_3.9_%7C_3.10-255074?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![python](https://img.shields.io/badge/-Poetry_1.6+-1e293b?logo=poetry&logoColor=white)]()
[![python](https://img.shields.io/badge/-CUDA_10.7_%7C_10.8-91c733?logo=cuda&logoColor=white)]()
[![pytorch](https://img.shields.io/badge/PyTorch_2.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![lightning](https://img.shields.io/badge/-Lightning_2.0+-792ee5?logo=pytorchlightning&logoColor=white)](https://pytorchlightning.ai/)
[![hydra](https://img.shields.io/badge/Config-Hydra_1.3+-89b8cf)](https://hydra.cc/)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![contributors](https://img.shields.io/github/contributors/unerue/lightning-boilerplate.svg)](https://github.com/unerue/lightning-boilerplate/graphs/contributors)
<!-- [![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) <br> -->
<!-- [![tests](https://github.com/unerue/lightning-boilerplate/actions/workflows/test.yml/badge.svg)](https://github.com/unerue/lightning-boilerplate/actions/workflows/test.yml) -->
<!-- [![code-quality](https://github.com/unerue/lightning-boilerplate/actions/workflows/code-quality-main.yaml/badge.svg)](https://github.com/unerue/lightning-boilerplate/actions/workflows/code-quality-main.yaml) -->
<!-- [![codecov](https://codecov.io/gh/ashleve/lightning-hydra-template/branch/main/graph/badge.svg)](https://codecov.io/gh/unerue/lightning-boilerplate) <br> -->
<!-- [![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/unerue/lightning-boilerplate#license) -->
<!-- [![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/unerue/lightning-boilerplate/pulls) -->


Lightning Boilerplate는 [lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template)에서 영감을 받았습니다. `lightning`과 `hydra`를 사용하여 머신러닝/딥러닝 연구자/엔지니어들이 `sklearn`과 `torch`로 연구와 개발을 효율적으로 수행할 수 있도록 지원합니다. 해당 템플릿은 Python 3.9 이상을 지원하며 추천하는 개발환경은 `conda`가 아닌 `pyenv`와 `poetry`입니다.

- [ ] PyTorch and Lightning with video files
- [ ] scikit-learn template
- [ ] pytorch native template with hydra-config
- [ ] Documentation in English

## Prerequisites

### Docker

도커 환경에서 사용하실 분들은 [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) 설치 후 [NGC]()가 아닌 [Docker Hub](https://hub.docker.com/r/pytorch/pytorch/tags)에서 사용할 `CUDA`와 `torch` 버전의 이미지로 컨테이너를 생성하시면 됩니다.

```bash
docker pull pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel
```

### pyenv (recommended)

`pyenv`는 본인의 운영체제에 따라 [맥/리눅스 버전](https://github.com/pyenv/pyenv#installation) 또는 [윈도우](https://github.com/pyenv-win/pyenv-win#installation) 설치하는 방법을 참고하여 파이썬 버전을 관리하시기 바랍니다.

```bash
curl https://pyenv.run | bash
```

### Poetry (recommended)

해당 템플릿은 파이썬 의존성 라이브러리 관리툴인 `poetry`를 사용합니다. Linux, macOS, Windows (WSL) [설치 방법](https://python-poetry.org/docs/#installing-with-the-official-installer)를 참고하여 의존성을 관리하시기 바랍니다.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Conda

에휴...ㅜ

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

### VSCODE

Python linter로 [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)를 설치합니다.

## Usage of Lightning Boilerplate

템플릿을 `clone`하고 `pyproject.toml` 내에 명시된 파이썬 버전과 시멘틱 버저닝을 확인한 다음 `poetry install` 명령어를 실행하여 기본 라이브러리를 설치합니다. 그 후 `git remote remove origin`을 실행하여 원격 저장소와 연결을 종료합니다.

```bash
git clone --depth 1 --branch main https://github.com/unerue/lightning-boilerplate.git ${your-project-name}
cd ${your-project-name}
poetry install
git remote remove origin
```

## Poetry package installation

Poetry 사용해 프로젝트 초기화 및 파이토치 등 라이브러리 설치 방법은 다음과 같다. pyenv로 파이썬 전역 버전을 설정한다. 아래는 `poetry`로 해당 템플릿이 아닌 다른 프로젝트에서 사용할 수 있는 간단한 사용방법을 설명한다.

<details>
<summary><b>Basic poetry usage</b></summary>

poetry 기초 사용 방법은 다음과 같다.

```bash
pyenv install 3.10.13 # Windows 3.10.10
pyenv global 3.10.13
```

`git clone`으로 만들어진 폴더로 진입해 프로젝트를 초기화한다.
* 작업 폴더 내에서 `poetry`를 초기화한다. 초기화 시 PEP에 따라 `pyproject.toml`이 생성된다.
* 작업 폴더 내 패키지관리(e.g. JS의 node_modules)와 같이 라이브러리를 관리하고 싶다면 virtualenvs.in-project를 `true`로 설정하고 해당 파일을 `--local`로 저장한다. 저장된 로컬 설정파일은 `poetry.toml`이다.

```bash
poetry init
poetry config virtualenvs.in-project true --local
poetry run python --version
```

초기화로 생성된 pyproject.toml 파일에 `[tool.poetry.dependencies]`의 파이썬 버전을 `python = "3.10.*"`으로 변경한다. 파이토치를 설치하기 전 소스 경로를 추가한다. 원하는 버전은 [이전 버전](https://pytorch.org/get-started/previous-versions/)에서 확인한 다음 설치한다.

```bash
poetry source add -p explicit pytorch https://download.pytorch.org/whl/cu117
poetry add --source pytorch torch torchvision
poetry run python -c "import torch;print(torch.cuda.is_available())"
```

### Lightning and dev package installation

* `poetry`는 라이브러리를 다양한 그룹으로 관리할 수 있다. 서비스와 상관없이 개발에만 필요한 패키지라면 `--group`인자를 통해 그룹명을 지정한 다음 배포 시 해당 라이브러리를 배제하고 배포가능하다.

```bash
poetry add lightning hydra-core hydra-colorlog rootutils rich python-dotenv
poetry add pytest black mypy isort pre-commit --group dev
```

</details>

## Usage of Lightning Boilerplate

Poetry를 기반으로 실행한다. `conda`나 `venv`라면 `python` 명령어로 실행한다.

```bash
pytest run pytest
poetry run python src/train.py trainer=gpu
```

명령어줄(command line)에서 설정(config) 매개변수 오버라이드(override)하기

```bash
python src/train.py trainer.max_epochs=20
```

미리 설정하지 않은 매개변수 추가하기

```bash
python src/train.py +trainer.new_arg="value"
```

작업 디렉토리 구조는 다음과 같음:

```bash
├── .github                 # GitHub Actions workflows
├── .vscode                 # VSCODE configs
├── configs                 # Hydra configs
│   ├── callbacks             # Callbacks configs
│   ├── data                  # DataModule and dataset configs
│   ├── debug                 # Debugging configs
│   ├── experiment            # Experiment configs
│   ├── extras                # Extra utilities configs
│   ├── hydra                 # Hydra configs
│   ├── logger                # Logger configs
│   ├── model                 # Model configs
│   ├── paths                 # Project paths configs
│   ├── trainer               # Trainer configs
│   ├── eval.yaml           # Main config for evaluation
│   └── train.yaml          # Main config for training
│
├── data                    # Dataset
├── logs                    # Logs generated by hydra and lightning loggers
├── src                     # Source code
│   ├── data                  # Dataset scripts
│   ├── models                # Model scripts
│   ├── utils                 # Utility scripts
│   ├── eval.py               # Run evaluation
│   └── train.py              # Run training
│
├── tests                   # PyTest
│
├── .env.example              # Example of file for storing private environment variables
├── .gitignore                # List of files ignored by git
├── .pre-commit-config.yaml   # Configuration of pre-commit hooks for code formatting
├── .project-root             # File for inferring the position of project root directory
├── Makefile                  # Makefile with commands like `make train` or `make test`
├── pyproject.toml            # Configuration options for testing and linting
├── setup.py                  # File for installing project as a package
└── README.md
```

### Before push your repository

`pre-commit`으로 훅(hook)으로 작성한 코드를 자동으로 formatter, linter, 보안 등 코드 내 잠재하고 있는 문제점을 찾아내기 위한 도구이다. `poetry install`을 했다는 가정하에:

```bash
poetry run pre-commit install
```

`pre-commit install` 명령어를 통해 `pre-commit-config.yaml` 파일에 미리 설정된 훅들을 설치하고 차후 `git commit`에 따른 코드를 자동으로 수정해준다.


## (Misc) Package Version Management with Poetry

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

Export pip install -r requirements.txt

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```


## Misc

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libzma-dev liblzma-dev

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# For zsh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

### Lighting Trainer API

https://lightning.ai/docs/pytorch/latest/common/trainer.html#trainer-class-api

#### Poetry install package

```bash
poetry add lightning
poetry add black flake8 mypy isort --group dev
```

### Conda

```bash
conda create --name your-env-name --file environment.yaml
conda activate your-env-name
```

https://docs.python.org/3/library/venv.html

```bash
python -m venv .venv
pip install -r requirements.txt
```

```bash
pytest test
python src/train.py
```

Override argument

```bash
python src/train.py trainer.max_epochs=20 model.optimizer.lr=1e-4
```

```bash
python src/train.py debug=default
python src/train.py debug=fdr
```

```bash
python src/train.py experiment=
python src/train.py -m 'experiment=glob(*)'
```

```bash
python src/train.py trainer=gpu +trainer.precision=16
```

Resume training from checkpoints

```bash
python src/train.py ckpt_path="/path/to/ckpt/name.ckpt"
```

Evaluate checkpoints

```bash
python src/eval.py ckpt_path="/path/to/ckpt/name.ckpt"
```

## Poetry version management

### Exact Version

If you don't include any modifiers, Poetry will keep your dependency pinned at that exact version.

```
beepboop = "2.1.7"
```

With that configuration, if a new version of beepboop is released, poetry update will not install it.

## Caret Version

If you use the caret ^ character, Poetry will update to any new version that does not change the leftmost non-zero section.

beepboop = "^2.1.7"
Equivalent to >=2.1.7, \<3.0.0
With the configuration above, poetry update would update beepboop to 2.1.8, 2.2, 2.3, etc. Poetry would not update to beepboop 3.0, because that changes the leftmost non-zero section of the version number from 2 to 3.

zeepzorp = "^0.24.1"
Equivalent to >=0.24.1, \<0.25.0
With the configuration above, poetry update would update zeepzorp to 0.24.2. Poetry would not update to zeepzorp 0.25.0, because that changes the leftmost non-zero section of the version number from 24 to 25.

The caret version modifier is pretty aggressive about which upgraded versions are allowed. This can cause problems if the maintainers of your dependencies introduce breaking changes without incrementing the major version number.

## Tilde Version

The tilde ~ character tells Poetry to allow minor updates. If you specify a major, minor, and patch version, only patch-level changes are allowed. If you specify a major and minor version, again only patch-level changes are allowed. If you specify only a major version, then minor- and patch-level changes are allowed.

beepboop = "~2.1.7"
Equivalent to >=2.1.7, \<2.2.0

beepboop = "~2.1"
Equivalent to >=2.1.0, \<2.2.0

beepboop = "~2"
Equivalent to >=2.0.0, \<3.0.0
The tilde version modifier is less aggressive than the caret version modifier in the upgrades it will allow.

## Wildcard Version

The star * character is a wildcard. Any version number is allowed at the wildcard position.

beepboop = "2.1.\*"
Equivalent to >=2.1.0, \<2.2.0

beepboop = "2.\*"
Equivalent to >=2.0.0, \<3.0.0

beepboop = "\*"
Allows any version. Equivalent to >=0.0.0

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

```bash
poetry init
poetry config virtualenvs.in-project true --local
poetry env use python3.10
poetry run python --version
poetry install
```
