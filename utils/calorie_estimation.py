import os
import sys
from pathlib import Path
from typing import Union, List, Optional
from PIL import Image
from huggingface_hub import snapshot_download
import torch

# Ensure calorie_clip_model is accessible in sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
LOCAL_MODEL_DIR = ROOT_DIR / "calorie_clip_model"

if str(LOCAL_MODEL_DIR) not in sys.path:
    sys.path.insert(0, str(LOCAL_MODEL_DIR))

try:
    from calorie_clip import CalorieCLIP
except ImportError:
    CalorieCLIP = None


class CalorieEstimation:
    """
    CalorieEstimation wrapper class for food calorie estimation using CalorieCLIP.
    """

    def __init__(
        self,
        model_path: Union[str, Path] = LOCAL_MODEL_DIR,
        device: str = "cpu",
        download: bool = True
    ):
        """
        Initialize the CalorieEstimation model.

        Args:
            model_path: Path to the local model directory.
            device: Device to load the model on ("cpu" or "cuda").
            download: Whether to download/verify model files via Hugging Face Hub.
        """
        self.model_path = Path(model_path)
        self.device = device

        if download:
            self._download_model()

        self._load_model()

    def _download_model(self):
        """Download or verify the CalorieCLIP model files locally."""
        print("[INFO] Downloading/Verifying CalorieCLIP model files locally...")
        repo_dir = snapshot_download(
            repo_id="jc-builds/CalorieCLIP",
            local_dir=str(self.model_path)
        )
        self.model_path = Path(repo_dir)

    def _load_model(self):
        """Load the CalorieCLIP model into memory."""
        if str(self.model_path) not in sys.path:
            sys.path.insert(0, str(self.model_path))

        global CalorieCLIP
        if CalorieCLIP is None:
            from calorie_clip import CalorieCLIP

        print(f"[INFO] Loading CalorieCLIP into memory on device: {self.device}...")
        self.model = CalorieCLIP.from_pretrained(self.model_path, device=self.device)
        print("[INFO] Model loaded successfully!")

    def predict(self, image_path: Union[str, Path, Image.Image]) -> float:
        """
        Predict calories from an image path or PIL Image.

        Args:
            image_path: Path to image file or PIL Image object.

        Returns:
            Estimated calories (float).
        """
        return self.model.predict(image_path)

    def predict_batch(self, images: List[Union[str, Path, Image.Image]]) -> List[float]:
        """
        Predict calories for a batch of images.

        Args:
            images: List of image paths or PIL Image objects.

        Returns:
            Numpy array or list of estimated calories.
        """
        return self.model.predict_batch(images)
