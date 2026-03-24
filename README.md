# Running Tests Outside of ReSim

This repo demonstrates how to run tests outside of ReSim and produce metrics on the results. This is useful when you do not have a dockerized build ready for running in our cloud.

Using the ReSim Python SDK lets you still use the ReSim metrics system to analyze data from your tests.

## Setup

The [resim-sdk](https://pypi.org/project/resim-sdk/) package requires Python >= 3.10.

Install dependencies:

```bash
pip install -r requirements.txt
# or, if using uv
uv sync
```

## Running Tests

1. If you do not yet have a project in ReSim, either:
   - Visit <https://app.resim.ai/projects/create> to create one, or
   - Use the [ReSim CLI](https://github.com/resim-ai/api-client#installation) to [create a project](https://docs.resim.ai/setup/projects/).
2. Obtain API credentials by contacting ReSim. The username/password below are _not_ your personal login credentials.
3. Create a `.env` file in the project root, with the following contents:

   ```text
   RESIM_USERNAME=<api-username>
   RESIM_PASSWORD=<api-password>
   RESIM_PROJECT_NAME=<my-project-name>
   ```

4. Run the script:

   ```bash
   python main.py
   # or
   uv run main.py
   ```

The script exits once test data has been uploaded. Metrics processing begins automatically — allow a few minutes for results to appear. Once available, you can:

- edit existing metrics to refine your analysis
- add new metrics
- view the raw data emitted by the tests under the "Artifacts" tab for each test

See the [metrics documentation](https://docs.resim.ai/guides/metrics-2/) for more information.
