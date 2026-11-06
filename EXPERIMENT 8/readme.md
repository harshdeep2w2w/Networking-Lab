# Experiment 8: OpenPGP Encrypted Email with Thunderbird

## Aim

To create and use OpenPGP keys in Thunderbird for sending and receiving encrypted and digitally signed emails.

---

## Objective

- To understand the use of OpenPGP for secure email communication.
- To create an OpenPGP public and secret key pair.
- To exchange public keys securely.
- To verify the fingerprint of a received public key.
- To send and receive encrypted and digitally signed emails.

---

## Tools and Technologies Used

- **Operating System:** Kali Linux
- **Email Client:** Mozilla Thunderbird
- **Security Technology:** OpenPGP
- **Email Protocol:** SMTP/IMAP

---

## Procedure

### Step 1: Configure the Email Account

Configured the email account in Mozilla Thunderbird to send and receive emails.

### Step 2: Create an OpenPGP Key Pair

Created an OpenPGP key pair for the email account.

The key pair contains:

- **Public Key:** Used for encrypting messages and verifying digital signatures.
- **Secret Key:** Used for decrypting messages and creating digital signatures.

### Step 3: Record the Key Fingerprint

Recorded the fingerprint of the generated OpenPGP key.

The fingerprint acts as a unique identifier for the public key and helps in verifying the correct key.

### Step 4: Exchange Public Keys

Exchanged public keys with the other user.

Only the public key is shared. The secret key remains private and is not shared with anyone.

### Step 5: Verify the Public Key Fingerprint

Compared and verified the fingerprint of the received public key before accepting it.

This helps ensure that the correct public key is being used.

### Step 6: Encrypt and Sign the Email

Composed an email and enabled:

- **Encryption:** To protect the confidentiality of the message.
- **Digital Signature:** To verify the sender's signing key and detect changes to the message.

The message was encrypted using the recipient's public key and digitally signed using the sender's secret key.

### Step 7: Receive and Verify the Email

The recipient received the encrypted email and decrypted it using their secret key.

The digital signature was also verified using the sender's public key.

---

## Output

The following observations were obtained during the experiment:

- An OpenPGP key pair was generated for the email account.
- The key fingerprint and key details were recorded.
- Public keys were exchanged between the users.
- The received public key fingerprint was verified.
- An email was encrypted and digitally signed.
- The received email was decrypted and its digital signature was verified.

---

## Security Observation

OpenPGP provides important security features for email communication:

- **Confidentiality:** Encryption helps protect the message from unauthorized reading.
- **Authentication:** Digital signatures help verify the signing key.
- **Integrity:** A signature can help detect whether the signed message has been modified.
- **Fingerprint Verification:** Comparing fingerprints helps establish trust in the correct public key.

> **Important:** Public keys can be shared, but secret keys must always remain private.

---

## Improvement

As an improvement, the partner's public key fingerprint was verified before accepting the key. This added an extra security check and helped confirm that the correct public key was used for secure email communication.

---

## Conclusion

The experiment demonstrated secure email communication using OpenPGP in Mozilla Thunderbird. A key pair was created, public keys were exchanged, fingerprints were verified, and encrypted and digitally signed emails were exchanged.

This experiment helped in understanding the role of encryption, digital signatures, public keys, secret keys, and fingerprint verification in securing email communication.

---

## Lab Environment

| Component | Details |
|---|---|
| Operating System | Kali Linux |
| Email Client | Mozilla Thunderbird |
| Security Technology | OpenPGP |
| Key Type | Public and Secret Key Pair |
| Main Features | Encryption and Digital Signatures |

---

## Repository Structure

```text
Experiment_8/
│
├── README.md
│
└── output/
    ├── Screenshot_1.png
    ├── Screenshot_2.png
    ├── Screenshot_3.png
    └── Screenshot_4.png
