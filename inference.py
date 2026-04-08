import os
from openai import OpenAI
from environment import SupportAgentEnv

# ✅ Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN is required")

# ✅ OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# ✅ Simple agent (baseline)
def get_action(obs, step):
    if step == 1:
        return {"action_type": "classify", "content": "billing_issue"}
    elif step == 2:
        return {"action_type": "set_priority", "content": "high"}
    elif step == 3:
        return {"action_type": "respond", "content": "Sorry for the issue, we will process your refund"}
    else:
        return {"action_type": "resolve", "content": "issue resolved"}


def run():
    env = SupportAgentEnv()
    obs = env.reset()

    step = 0
    rewards = []
    done = False

    print(f"[START] task=support env=support-agent-env model={MODEL_NAME}")

    try:
        while not done:
            step += 1

            action = get_action(obs, step)
            obs, reward, done, info = env.step(action)

            reward = float(f"{reward:.2f}")
            rewards.append(reward)

            error = info.get("error", None)

            print(
                f"[STEP] step={step} action={action} "
                f"reward={reward:.2f} done={str(done).lower()} "
                f"error={error if error else 'null'}"
            )

    except Exception as e:
        error = str(e)

    finally:
        reward_str = ",".join([f"{r:.2f}" for r in rewards])

        print(
            f"[END] success={str(done).lower()} "
            f"steps={step} rewards={reward_str}"
        )


if __name__ == "__main__":
    run()
