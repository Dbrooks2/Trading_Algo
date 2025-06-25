"""Vision module for detecting playing cards and table elements using OpenAI's vision API.
This module contains utility functions to grab frames from a webcam or a video file
and send them to the model for detection.
The detection step is stubbed for demonstration purposes.
"""
from __future__ import annotations

import cv2
import numpy as np
from typing import List, Dict, Tuple


def grab_frame(source: int | str = 0) -> np.ndarray:
    """Grab a single frame from a video source.

    Args:
        source: Index of the webcam or path to a video file.
    Returns:
        The captured frame in BGR format.
    """
    cap = cv2.VideoCapture(source)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError("Failed to capture frame")
    return frame


def detect_cards(frame: np.ndarray) -> Dict[str, List[Tuple[str, str]]]:
    """Detect cards and table elements in a frame using OpenAI's vision API.

    This is a placeholder implementation. In a real system, the frame would be
    encoded and sent to OpenAI's vision endpoint, which would return structured
    information about card ranks and suits, chip stacks, and other elements.

    Args:
        frame: An image represented as a NumPy array.

    Returns:
        A dictionary mapping element types ("community", "player1", etc.) to a
        list of tuples (rank, suit).
    """
    # TODO: integrate with OpenAI vision API.
    # For now return an empty structure.
    return {}

