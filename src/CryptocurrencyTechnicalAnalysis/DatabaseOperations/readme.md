# Dataset Curation
This submodule operates the back end of the dataset curation process; things like storing publically accessible data as well as handling
sensitive access credentials to allow for multiple users of any given instance of a system.

## Database Creation
The default database 

### Historic Performance Data
| Symbol    | Epoch       | High     | Low      | Open     | Close    |
| --------- | ----------- | -------- | -------- | -------- | -------- |
| `BTC/USD` | 10202938.43 | 47632.23 | 46473.34 | 45765.44 | 48754.69 |

### User Credentials
| UserPass | Alpaca Key | Alpaca Secret | Telegram Key |
| -------- | ---------- | ------------- | ------------ |
| SHA-256  | Fernet     | Fernet        | Fernet       |


## User Validation
I'm using the `Lab93CryptographyAPI` for one-way and two-way encryption to protect broker api keys by implementing a trustless multi-key
authentication method.  We never store user credentials in plain text; we use what we call a `userpass` to distinguish between users and
verify privilege.

The `userpass` is the hashed value of the hash of the password appended to the hash of the username; resulting in a unique identifier
that can only be recreated by supplying the correct username + password combination. --This is written down; and then the hash of the
password appended to the username is used to recreate the Fernet key for encrypting & decrypting the requested credentials.


## DataframeCuration
At its highest level, the database exists to have something to load into a multi-dimensional array that can be interacted with through other
code.  This function provides that object by constructing a Pandas dataframe out of the last variable number of entries arranged in ascending
order.
