import random
import asyncio

async def send_notification(notification_type: str, content: str) -> bool:
    print(f"[Mock] Sending {notification_type.upper()}: {content}")
    await asyncio.sleep(1)
    return random.random() < 0.8  # Simulate 80% success

async def send_with_retry(notification_type: str, content: str, retries: int = 3, delay: int = 1):
    for _ in range(retries):
        success = await send_notification(notification_type, content)
        if success:
            return True
        await asyncio.sleep(delay)
    return False