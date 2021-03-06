# Code Kata - Problem 1

## Parse fixed width file

- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

## Setup

Clone the repo

```bash
git clone https://github.com/matrixnl/codeKata.git
```

Run the server

```bash
docker-compose up --build
```

The server will be up on [http://localhost:5000](http://localhost:5000).

Run the tests

```bash
python -m pytest
```

## Requirements

Python >= 3.6

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)
