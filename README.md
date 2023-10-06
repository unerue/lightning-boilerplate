# lightning-boilerplate

## Prequisites

### Lighting Trainer API

https://lightning.ai/docs/pytorch/latest/common/trainer.html#trainer-class-api

### pyenv

https://github.com/pyenv/pyenv

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libzma-dev liblzma-dev

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# For zsh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

### Poetry

Linux, macOS, Windows (WSL)
https://python-poetry.org/

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

```bash
git clone --depth 1 --branch main https://github.com/unerue/lightning-boilerplate.git your-project-name
cd your-project-name
```

### Poetry package installation

```bash
pyenv install 3.10.13
```

```bash
poetry init
poetry config virtualenvs.in-project true --local
poetry env use python3.10
poetry run python --version
poetry install
```

#### Pytorch

```bash
poetry source add -p explicit pytorch https://download.pytorch.org/whl/cu117
poetry add --source pytorch torch torchvision
poetry run python -c "import torch;print(torch.cuda.is_available())"
```

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
Equivalent to >=2.1.7, <3.0.0
With the configuration above, poetry update would update beepboop to 2.1.8, 2.2, 2.3, etc. Poetry would not update to beepboop 3.0, because that changes the leftmost non-zero section of the version number from 2 to 3.

zeepzorp = "^0.24.1"
Equivalent to >=0.24.1, <0.25.0
With the configuration above, poetry update would update zeepzorp to 0.24.2. Poetry would not update to zeepzorp 0.25.0, because that changes the leftmost non-zero section of the version number from 24 to 25.

The caret version modifier is pretty aggressive about which upgraded versions are allowed. This can cause problems if the maintainers of your dependencies introduce breaking changes without incrementing the major version number.

## Tilde Version
The tilde ~ character tells Poetry to allow minor updates. If you specify a major, minor, and patch version, only patch-level changes are allowed. If you specify a major and minor version, again only patch-level changes are allowed. If you specify only a major version, then minor- and patch-level changes are allowed.

beepboop = "~2.1.7"
Equivalent to >=2.1.7, <2.2.0

beepboop = "~2.1"
Equivalent to >=2.1.0, <2.2.0

beepboop = "~2"
Equivalent to >=2.0.0, <3.0.0
The tilde version modifier is less aggressive than the caret version modifier in the upgrades it will allow.

## Wildcard Version
The star * character is a wildcard. Any version number is allowed at the wildcard position.

beepboop = "2.1.*"
Equivalent to >=2.1.0, <2.2.0

beepboop = "2.*"
Equivalent to >=2.0.0, <3.0.0

beepboop = "*"
Allows any version. Equivalent to >=0.0.0


```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```
