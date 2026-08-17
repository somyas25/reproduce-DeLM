# DeLM Reproduction Project

## Overview

This project is a small-scale reproduction of the DeLM paper. DeLM describes a decentralized multi-agent system. The original repository is here: https://github.com/yuzhenmao/DeLM

The original DeLM work uses SWE-bench and Docker-based coding agents at a large scale. This project uses a smaller and simpler benchmark instead. This project uses HumanEval. HumanEval is a set of 164 small coding problems with test cases.

## Core idea being tested

The DeLM paper shows that shared context between independent agent threads improves the solve rate. This project tests the same idea, at a smaller scale.

The system runs several solver threads in parallel. Each thread works alone at first. Each thread keeps its own local memory. The threads write short notes to a shared store during the run. This store is called "Shared Lessons." Other threads read these notes before their next attempt.

The project measures two scores:
- **avg@1** — the average success rate of one single thread, alone.
- **pass@N** — the success rate when at least one thread, out of N threads, solves the problem.

## Plan

The build happens in two stages.

**Stage 1: Baseline, no shared context.**
The project builds one solver agent first. The agent reads a HumanEval problem and writes code. A grading script checks the code against the problem's test cases. The project then runs four solver threads in parallel. The threads do not share any data at this stage. This stage produces a baseline avg@1 score and a baseline pass@N score.

**Stage 2: Shared context added.**
The project adds a shared-lessons store. Each thread writes a short note after each attempt. The note states what the thread tried and if the attempt passed or failed. Each thread reads the shared notes before it writes its next answer. The project re-runs the same problems with this store turned on. The project compares the new scores against the Stage 1 baseline.

## Environment

Each solver thread runs inside its own Docker container. This setup keeps generated code isolated from the host system. HumanEval's test-execution code needs this isolation, since it runs model-written code directly.

## Credits

This project is inspired by, and reproduces a small part of, the original DeLM work: https://github.com/yuzhenmao/DeLM