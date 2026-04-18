# StreamFleet

## Run

Run commands from the **`server`** or **`client`** folder (so the `src` package is on `PYTHONPATH` via the current directory), or export `PYTHONPATH` explicitly to that folder.

### Viewer (FastAPI + WebSockets)

```bash
cd server
uvicorn src.streamfleet_server.presentation.app:app --host 0.0.0.0 --port 8000
```

There is no `presentation.api.stream_ws` module anymore; the ASGI app lives in **`presentation.app`**.

### Producer (camera → server)

```bash
cd client
python -m src.streamfleet_client.main
```

Start the viewer first, then the producer.

## WebSocket got `403 Forbidden`

- Use the **`ws://`** URL (not `http://`), e.g. `ws://127.0.0.1:8000/v1/ws/test`.
- If the page is served over **HTTPS**, the browser may block **insecure** `ws://`; use **`wss://`** behind TLS or test from `http://` pages.
- Try the same host for page and API (**`localhost` vs `127.0.0.1`** can matter for some clients).
