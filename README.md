# Similarity Server

Gensim Machine Learning simserver implementation in Python for the purpose of matching words according to keyword.
[Lensity Repo](https://github.com/preposterous-kumquat/preposterous-kumquat)

## Team

  - __Product Owner__: [Josphine Eng](https://github.com/ChirpingMermaid)
  - __Scrum Master__: [Julie Truong](https://github.com/Truong-Julie)
  - __Development Team Members__: [Brian Kilrain](https://github.com/bkilrain)

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

### Create Training Corpus
- Upload training photos to S3
 * naming convention: http://url.com/path/to/photo/im1342.jpg... im1343.jpg... im1344.jpg
- In curator/routes.js -> set training counter to first image file number (line 16)
- Uncomment volume to trainingCorpus.json in yml file
- Send POST request to main-web-server/kickoffTraining with postman
- Copy and paste data in trainingCorpus.json in curator to trainingCorpus.json in simserver

### Training
Once Docker compose is running:
- Use Postman to send POST request to
``` http://0.0.0.0:5000/train ```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
