# Homomorphic Encryption Of Election Data
We are implementing homomorphic encryption for an election data set to determine the winner of a two party system vote without alternate candidates. Note that we have abstained from some of the more complicated aspects of the US electoral system such as split votes, tie handling, and the existence of the District of Columbia.

## Preparation Instructions
- Make sure to install tenseal, numpy, and pandas
```pip3 install tenseal && pip3 install numpy && pip3 install pandas```

## Build Instructions for Tutorial
- Build utils.py
- Build salary/generateKeys.py
- Build salary/DataOperator.py
- Build salary/DataOwner.py

## Build Instructions for Popular Vote
- Build utils.py
- Build popularVote/generateKeys.py
- Build popularVote/voters.py
- Build popularVote/pollWorker.py
- Build popularVote/decryptVotes.py
- Build popularVote/decryptTally.py

## Build Instructions for Electoral College
- Build utils.py
- Build electoralVote/generateKeys.py
- Build electoralVote/voters.py
- Build electoralVote/pollWorker.py
- Build electoralVote/decryptVotes.py
- Build electoralVote/decryptTally.py