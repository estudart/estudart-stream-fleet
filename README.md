# StreamFleet

## Run

Run commands from the **`server`** or **`client`** folder (so the `src` package is on `PYTHONPATH` via the current directory), or set `PYTHONPATH` to that folder explicitly.

### Server (FastAPI + WebSockets + Redis)

```bash
cd server
uvicorn src.streamfleet_server.presentation.app:app --host 0.0.0.0 --port 8000
```

The ASGI app module is **`src.streamfleet_server.presentation.app:app`**.

### Client — publisher (camera → server / Redis)

```bash
cd client
python -m src.streamfleet_client.main_publisher
```

### Client — consumer (subscribe + OpenCV preview)

Set **`CHANNEL`** to the same Redis/WebSocket channel the publisher uses (must match the publisher’s `?channel=` / default channel logic).

```bash
cd client
CHANNEL=4856177744 python -m src.streamfleet_client.main_consumer
```

Start the **server** first, then run **publisher** and/or **consumer** as needed.

## WebSocket got `403 Forbidden`

- Use the **`ws://`** URL (not `http://`), e.g. `ws://127.0.0.1:8000/v1/ws/test`.
- If the page is served over **HTTPS**, the browser may block **insecure** `ws://`; use **`wss://`** behind TLS or test from `http://` pages.
- Try the same host for page and API (**`localhost` vs `127.0.0.1`** can matter for some clients).
