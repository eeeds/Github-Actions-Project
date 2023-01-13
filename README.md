# Github Actions Project
This project has been created to learn and apply Github Actions and it's part of a challenge called [Project-of-the-week](https://github.com/DataTalksClub/project-of-the-week/blob/main/2023-01-11-github_actions-1.md) that is being held by Datatalks.club.

## Technologies
- GitHub
- Unit Testing
- Linting and formatting libraries
# Concepts
## What is Github Actions?
Github Actions is a feature that allows you to automate tasks within your software development life cycle. You can create workflows that are triggered by events within your repository such as creating a pull request or merging a pull request. You can also schedule workflows to run on a specific day and time.

## What is a workflow?
A workflow is a configurable automated process made up of one or more jobs. A workflow can be scheduled or triggered by an event. A workflow file is a YAML file in your repository that defines your workflow. You can add a workflow file to your repository's `.github/workflows` directory. You can name your workflow file anything you like. For example, you can name your file `build.yml`, `deploy.yml`, or `main.yml`. You can also put your workflow file in a subdirectory of `.github/workflows`. For example, `.github/workflows/my-workflows/deploy.yml`.

## What is a job?
A job is a set of steps that execute on the same runner. You can define dependencies between jobs using the needs keyword. You can also define dependencies between steps using the needs keyword.

## What is a step?
A step is an individual task that can run commands. Steps are the smallest portable building block of a job. Steps can run commands, run setup tasks, or run an action. Each step runs in its own process in the runner environment and has access to the workspace and filesystem. You can use the `run` keyword to run a single command or a group of commands in the same shell. You can also use the `run` keyword to execute a script.

## What is an action?
An action is a piece of code that performs one single modular task. You can combine actions to create jobs. You can also create your own actions and share them with the GitHub community. For more information, see "[Creating a JavaScript action](https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action)".

## What is a runner?
A runner is a server that has the GitHub Actions runner application installed. You can use runners hosted by GitHub or you can host your own. For more information, see "[About self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners)".

## What is a container?
A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. For more information, see "[Docker overview](https://docs.docker.com/get-started/overview/)".

# First Steps

## Quickstart for GitHub Actions
Working on this [link](https://docs.github.com/en/actions/quickstart)
## Create your first workflow
1. Create a `.github/workflows` directory in your repository on GitHub if this directory does not already exist.
2. In the `.github/workflows` directory, create a file named `github-actions-demo.yml`
3. Copy this code:
    ```
        name: GitHub Actions Demo
        run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
        on: [push]
        jobs:
        Explore-GitHub-Actions:
            runs-on: ubuntu-latest
            steps:
            - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
            - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
            - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
            - name: Check out repository code
                uses: actions/checkout@v3
            - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
            - run: echo "🖥️ The workflow is now ready to test your code on the runner."
            - name: List files in the repository
                run: |
                ls ${{ github.workspace }}
            - run: echo "🍏 This job's status is ${{ job.status }}."
    ```
4. Committing the workflow file to a branch in your repository triggers the push event and runs your workflow.

## Understanding the worflow file
1. `name: GitHub Actions Demo` is the name of the workflow as it will appear in the "Actions" tab of the GitHub repository.
2. `run-name: ${{ github.actor }} is testing out GitHub Actions 🚀` is the name for workflow runs generated from the workflow, which will appear in the list of workflow runs on your repository's `Actions` tab. This example uses an expression with the `github` context to display the username of the actor that triggered the workflow run.
3. `on: [push]`. It specifies the trigger for this workflow. This example uses the push event, so a workflow run is triggered every time someone pushes a change to the repository or merges a pull request.
4. `jobs:` groups together all the jobs that run in the `GitHub Actions Demo` workflow.
5. `Explore-GitHub-Actions:`. Defines a job named `Explore-GitHub-Actions`
. The child keys will define properties of the job.
6. `runs-on: ubuntu-latest`. Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub
7. `steps`. Groups together all the steps that run in the `Explore-Github-Actions` job. Each item under this section is a separate action or shell script.
8. `uses: actions/checkout@v3`. The uses keyword specifies that this step will run v3 of the actions/checkout action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will run against the repository's code.

# Building and Testing Python
You can create a continuous integration (CI) workflow to build and test your Python project.
## Python Starter workflow
Working following this [tutorial](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python).

## Trying something by my own.
I have written a python script named `src/script.py`. This script invokes `datetime.now()` function and save it into a `.txt` file called [dates.txt](dates.txt).

I have created a workflow file named [Write Dates Workflow](.github/workflows/write-dates.yml).

The workflow file is as follows:
```
name: Writing Dates
on:
  push:
    branches:
      - main
  schedule:
    - cron: '* 1/6 * * *'
jobs:
  write-dates:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Set up Python 3.9
        uses: actions/setup-python@v4
        with:
          ## Setting Python version equal to 3.9
          python-version: '3.9'
          ## Setting architecture equal to x64
          architecture: 'x64' 
      - name: Write date
        run: |
          python src/script.py >> dates.txt
      - name: Commit changes
        run: |
          git config --local user.email "encinaesteban27@gmail.com"
          git config --local user.name "github-actions[bot]"
          git add .
          git commit -m "Updating dates"
      - uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}
```
## Analize the workflow
1. `name: Writing Dates` is the name of the workflow as it will appear in the "Actions" tab of the GitHub repository.
2. It will trigger on `push` on the `main` branch and also on a schedule using crontab. `* 1/6 * * *` means `at every minute past every 6th hour from 1 through 23`.
  ```
  on:
    push:
      branches:
        - main
    schedule:
      - cron: '* 1/6 * * *'
  ```
3. `jobs:` groups together all the jobs that run in the `Writing Dates` workflow. `write-dates` is the job name. It will run on an ubuntu machine.
4. We will use this repository, so we have to use `actions/checkout@v3`.
```
    steps:
      - name: Checkout
        uses: actions/checkout@v3
```
5. We will use Python 3.9, so we have to use `actions/setup-python@v4`.
```
    steps:
      - name: Set up Python 3.9
        uses: actions/setup-python@v4
        with:
          ## Setting Python version equal to 3.9
          python-version: '3.9'
          ## Setting architecture equal to x64
          architecture: 'x64' 
```
6. We will run the script `src/script.py` and save the output into `dates.txt`.
```
    steps:
      - name: Write date
        run: |
          python src/script.py >> dates.txt
```
7. We will commit the changes and push them to the repository.
  ```
      steps:
        - name: Commit changes
          run: |
            git config --local user.email "
            git config --local user.name "github-actions[bot]"
            git add .
            git commit -m "Updating dates"
        - uses: ad-m/github-push-action@master
          with:
            github_token: ${{ secrets.GITHUB_TOKEN }}
            branch: ${{ github.ref }}
  ```

# Triggering a workflow
Working following this [tutorial](https://docs.github.com/en/actions/learn-github-actions/events-that-trigger-workflows).