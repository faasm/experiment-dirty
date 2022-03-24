# Experiment dirty

## Set up

To set up Python environment:

```bash
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```

## Build and run

To build:

```bash
source venv/bin/activate

inv build
```

To run (will request `sudo` password if necessary):

```bash
inv run
```
