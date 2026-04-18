# StreamFleet

## Run

From the repo root, set `PYTHONPATH` so the `src.*` packages resolve (`client` and `server` are the folders that contain the `src` directory).

**Viewer (WebSocket server — receives frames, OpenCV preview):**

```bash
cd server
```

```bash
uvicorn src.streamfleet_server.presentation.api.stream_ws:app --host 0.0.0.0 --port 8000
```

**Producer (camera / drone → server):**
```bash
cd client
```

```bash
python -m src.streamfleet_client.main
```

Run the viewer first, then the producer.
