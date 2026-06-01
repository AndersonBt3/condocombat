"""WebSocket connection manager with broadcast and heartbeat."""

import asyncio
import json
import logging
from datetime import datetime, timezone

from fastapi import WebSocket

from app.schemas.ws_message import EventType, WSMessage

logger = logging.getLogger(__name__)

HEARTBEAT_INTERVAL = 30  # seconds


class WSConnectionManager:
    """Gerencia conexões WebSocket com broadcast e heartbeat."""

    def __init__(self) -> None:
        self._connections: dict[WebSocket, str | None] = {}
        # WebSocket -> str | None (user_email if authenticated)
        self._heartbeat_tasks: dict[WebSocket, asyncio.Task] = {}

    @property
    def active_connections(self) -> int:
        return len(self._connections)

    async def connect(
        self, websocket: WebSocket, user_email: str | None = None
    ) -> None:
        await websocket.accept()
        self._connections[websocket] = user_email
        task = asyncio.create_task(self._heartbeat_loop(websocket))
        self._heartbeat_tasks[websocket] = task
        logger.info(
            "WS connect: %s connections=%d",
            user_email or "anonymous",
            self.active_connections,
        )

    def disconnect(self, websocket: WebSocket) -> None:
        self._connections.pop(websocket, None)
        task = self._heartbeat_tasks.pop(websocket, None)
        if task is not None:
            task.cancel()
        logger.info(
            "WS disconnect: connections=%d", self.active_connections
        )

    async def broadcast(self, message: WSMessage) -> None:
        """Envia mensagem para todas as conexões ativas."""
        payload = message.model_dump(mode="json")
        disconnected: list[WebSocket] = []
        for ws in self._connections:
            try:
                await ws.send_json(payload)
            except Exception:
                disconnected.append(ws)
        for ws in disconnected:
            self.disconnect(ws)

    async def send_personal(
        self, message: WSMessage, websocket: WebSocket
    ) -> None:
        """Envia mensagem para uma conexão específica."""
        payload = message.model_dump(mode="json")
        try:
            await websocket.send_json(payload)
        except Exception:
            self.disconnect(websocket)

    async def _heartbeat_loop(self, websocket: WebSocket) -> None:
        """Envia ping periódico e detecta dead connections."""
        try:
            while True:
                await asyncio.sleep(HEARTBEAT_INTERVAL)
                ping = WSMessage(type=EventType.PING)
                try:
                    await websocket.send_json(
                        ping.model_dump(mode="json")
                    )
                except Exception:
                    self.disconnect(websocket)
                    break
        except asyncio.CancelledError:
            pass

    async def shutdown(self) -> None:
        """Cleanup all connections on app shutdown."""
        for ws in list(self._connections.keys()):
            self.disconnect(ws)


# Singleton
manager = WSConnectionManager()
