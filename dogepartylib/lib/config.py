import sys

"""Variables prefixed with `DEFAULT` should be able to be overridden by
configuration file and command‐line arguments."""

UNIT = 100000000        # The same across assets.


# Versions
VERSION_MAJOR = 9
VERSION_MINOR = 59
VERSION_REVISION = 4
VERSION_STRING = str(VERSION_MAJOR) + '.' + str(VERSION_MINOR) + '.' + str(VERSION_REVISION)


# Dogeparty protocol
TXTYPE_FORMAT = '>I'
SHORT_TXTYPE_FORMAT = 'B'

TWO_WEEKS = 2 * 7 * 24 * 3600
MAX_EXPIRATION = 129600   # Three months

MEMPOOL_BLOCK_HASH = 'mempool'
MEMPOOL_BLOCK_INDEX = 9999999


# SQLite3
MAX_INT = 2**63 - 1


# Dogecoin Core
OP_RETURN_MAX_SIZE = 80  # bytes


# Currency agnosticism
DOGE = 'DOGE'
XDP = 'XDP'

DOGE_NAME = 'Dogecoin'
XDP_NAME = 'Dogeparty'
APP_NAME = XDP_NAME.lower()

DEFAULT_RPC_PORT_REGTEST = 24005
DEFAULT_RPC_PORT_TESTNET = 14005
DEFAULT_RPC_PORT = 4005

DEFAULT_BACKEND_PORT_REGTEST = 28335
DEFAULT_BACKEND_PORT_TESTNET = 18335
DEFAULT_BACKEND_PORT = 8335

DEFAULT_INDEXD_PORT_REGTEST = 28435
DEFAULT_INDEXD_PORT_TESTNET = 18435
DEFAULT_INDEXD_PORT = 8435

UNSPENDABLE_REGTEST = 'ndogepartyxxxxxxxxxxxxxxxxxxwpsZCH'
UNSPENDABLE_TESTNET = 'ndogepartyxxxxxxxxxxxxxxxxxxwpsZCH'
UNSPENDABLE_MAINNET = 'DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr'

#DOGECOIN TESTNET
ADDRESSVERSION_TESTNET = b'\x71'
P2SH_ADDRESSVERSION_TESTNET = b'\xc4'
PRIVATEKEY_VERSION_TESTNET = b'\xf1'
#DOGECOIN MAINNET
ADDRESSVERSION_MAINNET = b'\x1e'
P2SH_ADDRESSVERSION_MAINNET = b'\x16'
PRIVATEKEY_VERSION_MAINNET = b'\x9e'
#DOGECOIN REGTEST
ADDRESSVERSION_REGTEST = b'\x71'
P2SH_ADDRESSVERSION_REGTEST = b'\xc4'
PRIVATEKEY_VERSION_REGTEST = b'\xf1'

MAGIC_BYTES_TESTNET = b'\xfc\xc1\xb7\xdc'   # For bip-0010
MAGIC_BYTES_MAINNET = b'\xc0\xc0\xc0\xc0'   # For bip-0010
MAGIC_BYTES_REGTEST = b'\xfc\xc1\xb7\xdc'

BLOCK_FIRST_TESTNET_TESTCOIN = 310000
BURN_START_TESTNET_TESTCOIN = 310000
BURN_END_TESTNET_TESTCOIN = 4017708     # Fifty years, at ten minutes per block.

BLOCK_FIRST_TESTNET = 166371
BLOCK_FIRST_TESTNET_HASH = 'dfb3c6602b59ffb5acf6c3535618b40fb70004e642e7b2d0a3fbea80c6920307'
BURN_START_TESTNET = 3260772
BURN_END_TESTNET = 3270852

BLOCK_FIRST_MAINNET_TESTCOIN = 278270
BURN_START_MAINNET_TESTCOIN = 278310
BURN_END_MAINNET_TESTCOIN = 2500000     # A long time.

BLOCK_FIRST_MAINNET = 335643
BLOCK_FIRST_MAINNET_HASH = '79797a552cbf9432c1752442cb95327dfa9e739d35f940bb038be5e5af10b9f5'
BURN_START_MAINNET = 3919346
BURN_END_MAINNET = 4007186

BLOCK_FIRST_REGTEST = 0
BLOCK_FIRST_REGTEST_HASH = '0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206'
BURN_START_REGTEST = 101
BURN_END_REGTEST = 150000000

BLOCK_FIRST_REGTEST_TESTCOIN = 0
BURN_START_REGTEST_TESTCOIN = 101
BURN_END_REGTEST_TESTCOIN = 150

# Protocol defaults
# NOTE: If the DUST_SIZE constants are changed, they MUST also be changed in dogeblockd/lib/config.py as well
    # TODO: This should be updated, given their new configurability.
# TODO: The dust values should be lowered by 90%, once transactions with smaller outputs start confirming faster: <https://github.com/mastercoin-MSC/spec/issues/192>
DEFAULT_REGULAR_DUST_SIZE = 1000000      # Lower dust limit to 0.01 DOGE
DEFAULT_MULTISIG_DUST_SIZE = 1000000     # 
DEFAULT_OP_RETURN_VALUE = 0
DEFAULT_FEE_PER_KB_ESTIMATE_SMART = 1000000
DEFAULT_FEE_PER_KB = 1000000           # sane/low default, also used as minimum when estimated fee is used
ESTIMATE_FEE_PER_KB = False               # when True will use `estimatesmartfee` from dogecoind instead of DEFAULT_FEE_PER_KB
ESTIMATE_FEE_CONF_TARGET = 3
ESTIMATE_FEE_MODE = 'CONSERVATIVE'

# UI defaults
DEFAULT_FEE_FRACTION_REQUIRED = .009   # 0.90%
DEFAULT_FEE_FRACTION_PROVIDED = .01    # 1.00%


DEFAULT_REQUESTS_TIMEOUT = 20   # 20 seconds
DEFAULT_RPC_BATCH_SIZE = 20     # A 1 MB block can hold about 4200 transactions.

# Custom exit codes
EXITCODE_UPDATE_REQUIRED = 5


DEFAULT_CHECK_ASSET_CONSERVATION = True

BACKEND_RAW_TRANSACTIONS_CACHE_SIZE = 20000
BACKEND_RPC_BATCH_NUM_WORKERS = 6

UNDOLOG_MAX_PAST_BLOCKS = 1440 #the number of past blocks that we store undolog history

DEFAULT_UTXO_LOCKS_MAX_ADDRESSES = 1000
DEFAULT_UTXO_LOCKS_MAX_AGE = 3.0 #in seconds

ADDRESS_OPTION_REQUIRE_MEMO = 1
ADDRESS_OPTION_MAX_VALUE = ADDRESS_OPTION_REQUIRE_MEMO # Or list of all the address options
OLD_STYLE_API = True

API_LIMIT_ROWS = 1000
MEMPOOL_TXCOUNT_UPDATE_LIMIT=60000

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
