# Lensity

> Similarity Server
> Machine Learning micro-service to return similarity matched photos

Main Repo:
  - [Lensity](https://github.com/preposterous-kumquat/preposterous-kumquat)

## Team

  - __Product Owner__: [Josphine Eng](https://github.com/ChirpingMermaid)
  - __Scrum Master__: [Julie Truong](https://github.com/Truong-Julie)
  - __Development Team Members__: [Brian Kilrain](https://github.com/bkilrain)

# similarityServer

## Table of Contents

1. [Team](#team)
1. [Docker Development](#docker-development)
    1. [Build Image](#build-image)
    1. [Train Corpus](#train-corpus)
    
1. [Contributing](#contributing)

## Docker Development

### Build Image

In root folder run:
```sh
docker build -t simserver:01 .
```
### Training Corpus
Once Docker comopose is running:
- Use Postman to send POST request to
```sh http://0.0.0.0:5000/train ```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
