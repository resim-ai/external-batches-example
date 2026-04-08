from resim.sdk.auth.device_code_client import DeviceCodeClient
from resim.sdk.batch import Batch
from resim.sdk.test import Test

# Change this to your ReSim project name
PROJECT_NAME = "my resim project"


def main():
    client = DeviceCodeClient()  # Authenticate with ReSim

    # Create a batch, and run the "my metrics" metrics set against it. See config.resim.yml
    with Batch(
        client=client,
        project_name=PROJECT_NAME,
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
