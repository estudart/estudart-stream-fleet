#!/usr/bin/env python3
"""
Run this once from the SAME app you want to allow (Terminal.app, iTerm, or Cursor).
macOS only lists apps after they try to use the camera — this triggers that request.

Example (from project root):
  ./venv/bin/python scripts/camera_permission_prompt.py
"""
import sys

import cv2


def main() -> int:
    print("Requesting camera access (watch for a system dialog)…", flush=True)
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
    if not cap.isOpened():
        print("Could not open camera. Grant permission in System Settings if prompted, then run again.", file=sys.stderr)
        return 1
    ok, frame = cap.read()
    cap.release()
    if not ok or frame is None:
        print("Opened device but read failed — check Camera permission for this app.", file=sys.stderr)
        return 1
    print("Success. You can open System Settings → Privacy & Security → Camera and confirm this app is enabled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
