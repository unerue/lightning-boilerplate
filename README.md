# lightning-boilerplate

```bash
git clone --depth 1 --branch main https://github.com/unerue/lightning-boilerplate.git your-project-name
cd your-project-name
conda create --name your-env-name --file environment.yaml
conda activate your-env-name
```

```
pytest test
python src/train.py
```
Override argument

```
python src/train.py trainer.max_epochs=20 model.optimizer.lr=1e-4
```

```
python src/train.py debug=default
python src/train.py debug=fdr
```

```
python src/train.py experiment=
python src/train.py -m 'experiment=glob(*)'
```

```
python src/train.py trainer=gpu +trainer.precision=16
```

Resume training from checkpoints
```
python src/train.py ckpt_path="/path/to/ckpt/name.ckpt"
```

Evaluate checkpoints
```
python src/eval.py ckpt_path="/path/to/ckpt/name.ckpt"
```

