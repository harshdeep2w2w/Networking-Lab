# Experiment 3

## Title

Challenge-Response Authentication and Replay Attack Handling

## Aim

To implement and understand challenge-response authentication using a nonce, timestamp, shared secret and HMAC-SHA256, and to detect and prevent replay attacks.

## Theory

Challenge-response authentication allows a server to authenticate a client without directly transmitting the shared secret.

The server generates a fresh nonce. The client uses the nonce and shared secret to generate an HMAC-SHA256 response. The server verifies the response.

Replay attacks are prevented using fresh nonces, one-time nonce tracking and timestamp-based expiry.

## Implementation

The Python program implements:

- Random nonce generation
- Shared secret
- HMAC-SHA256
- Timestamp verification
- One-time nonce tracking
- Replay attack detection
- Expired response detection

## Tests

1. Successful authentication
2. Replay attack
3. Delayed/expired response

## Expected Results

- First use → Authentication successful
- Replay → Replay detected
- Delayed response → Expired response

## Language

Python

## Libraries

- hashlib
- hmac
- secrets
- time
