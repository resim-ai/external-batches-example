import os
from dotenv import load_dotenv
from resim.sdk.auth.username_password_client import UsernamePasswordClient
from resim.sdk.batch import Batch
from resim.sdk.test import Test

load_dotenv()


def _require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise EnvironmentError(f"Required environment variable '{name}' is not set")
    return value


def main():
    project_name = _require_env("RESIM_PROJECT_NAME")
    username = _require_env("RESIM_USERNAME")
    password = _require_env("RESIM_PASSWORD")

    client = UsernamePasswordClient(username=username, password=password)

    # Create a batch, and run the "my metrics" metrics set against it. See config.resim.yml
    with Batch(
        client=client,
        project_name=project_name,
        branch="metrics-test-branch",
        metrics_set_name="my metrics",
        metrics_config_path="resim/config.resim.yml",
    ) as batch:
        print(f"Created batch {batch.friendly_name} with id {batch.id}")

        # Create 2 tests, and emit some random data for the "position" topic
        with Test(client, batch, "test 1") as test:
            for i in range(10):
                test.emit("position", {"x": float(i), "y": float(i)}, i)
        print("test 1 done")

        with Test(client, batch, "test 2") as test:
            for i in range(10):
                test.emit("position", {"x": float(i), "y": float(i * 2)}, i)
        print("test 2 done")

        print(
            f"Batch done. After a few minutes, you can view your metrics here: https://app.resim.ai/projects/{batch.project_id}/batches/{batch.id}"
        )


if __name__ == "__main__":
    main()
