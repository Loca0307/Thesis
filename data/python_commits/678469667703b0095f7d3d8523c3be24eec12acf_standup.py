from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.utils import get_device
from stable_baselines3.common.vec_env import DummyVecEnv, VecVideoRecorder
from wandb.integration.sb3 import WandbCallback

if get_device() != torch.device("cpu"):
    NVIDIA_ICD_CONFIG_PATH = "/usr/share/glvnd/egl_vendor.d/10_nvidia.json"
    if not os.path.exists(NVIDIA_ICD_CONFIG_PATH):
        with open(NVIDIA_ICD_CONFIG_PATH, "w") as f:
            _ = f.write("""{
                                "file_format_version" : "1.0.0",
                                "ICD" : {
                                    "library_path" : "libEGL_nvidia.so.0"
                                }
                            }""")

    # Configure MuJoCo to use the EGL rendering backend (requires GPU)
    os.environ["MUJOCO_GL"] = "egl"


# taken from https://gymnasium.farama.org/main/_modules/gymnasium/wrappers/record_video/
def capped_cubic_video_schedule(episode_id: int) -> bool:
    """The default episode trigger.

    This function will trigger recordings at the episode indices 0, 1, 8, 27, ..., :math:`k^3`, ..., 729, 1000, 2000, 3000, ...

    Args:
        episode_id: The episode number

    Returns:
        If to apply a video schedule number
    """
    if episode_id < 10000:
        return int(round(episode_id ** (1.0 / 3))) ** 3 == episode_id
    else:
        return episode_id % 10000 == 0


gym.register(
    id="NaoStandup-v1",
    entry_point="nao_env:NaoStandup",
    max_episode_steps=2500,
)

config = {
    "policy_type": "MlpPolicy",
    "total_timesteps": 1000000,
    "env_name": "NaoStandup-v1",
    "render_mode": "rgb_array",
}
