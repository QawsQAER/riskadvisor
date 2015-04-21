# encoding: utf-8
# module errno
# from (built-in)
# by generator 1.136
"""
This module makes available standard errno system symbols.

The value of each symbol is the corresponding integer value,
e.g., on most systems, errno.ENOENT equals the integer 2.

The dictionary errno.errorcode maps numeric codes to symbol names,
e.g., errno.errorcode[2] could be the string 'ENOENT'.

Symbols that are not relevant to the underlying system are not defined.

To map error codes to error messages, use the function os.strerror(),
e.g. os.strerror(2) could return 'No such file or directory'.
"""
# no imports

# Variables with simple values

E2BIG = 7

EACCES = 13
EADDRINUSE = 48
EADDRNOTAVAIL = 49
EAFNOSUPPORT = 47
EAGAIN = 35
EALREADY = 37
EAUTH = 80

EBADARCH = 86
EBADEXEC = 85
EBADF = 9
EBADMACHO = 88
EBADMSG = 94
EBADRPC = 72
EBUSY = 16

ECANCELED = 89
ECHILD = 10
ECONNABORTED = 53
ECONNREFUSED = 61
ECONNRESET = 54

EDEADLK = 11
EDESTADDRREQ = 39
EDEVERR = 83
EDOM = 33
EDQUOT = 69

EEXIST = 17

EFAULT = 14
EFBIG = 27
EFTYPE = 79

EHOSTDOWN = 64
EHOSTUNREACH = 65

EIDRM = 90
EILSEQ = 92
EINPROGRESS = 36
EINTR = 4
EINVAL = 22
EIO = 5
EISCONN = 56
EISDIR = 21

ELOOP = 62

EMFILE = 24
EMLINK = 31
EMSGSIZE = 40
EMULTIHOP = 95

ENAMETOOLONG = 63
ENEEDAUTH = 81
ENETDOWN = 50
ENETRESET = 52
ENETUNREACH = 51
ENFILE = 23
ENOATTR = 93
ENOBUFS = 55
ENODATA = 96
ENODEV = 19
ENOENT = 2
ENOEXEC = 8
ENOLCK = 77
ENOLINK = 97
ENOMEM = 12
ENOMSG = 91
ENOPOLICY = 103
ENOPROTOOPT = 42
ENOSPC = 28
ENOSR = 98
ENOSTR = 99
ENOSYS = 78
ENOTBLK = 15
ENOTCONN = 57
ENOTDIR = 20
ENOTEMPTY = 66
ENOTRECOVERABLE = 104
ENOTSOCK = 38
ENOTSUP = 45
ENOTTY = 25
ENXIO = 6

EOPNOTSUPP = 102
EOVERFLOW = 84
EOWNERDEAD = 105

EPERM = 1
EPFNOSUPPORT = 46
EPIPE = 32
EPROCLIM = 67
EPROCUNAVAIL = 76
EPROGMISMATCH = 75
EPROGUNAVAIL = 74
EPROTO = 100
EPROTONOSUPPORT = 43
EPROTOTYPE = 41
EPWROFF = 82

ERANGE = 34
EREMOTE = 71
EROFS = 30
ERPCMISMATCH = 73

ESHLIBVERS = 87
ESHUTDOWN = 58
ESOCKTNOSUPPORT = 44
ESPIPE = 29
ESRCH = 3
ESTALE = 70

ETIME = 101
ETIMEDOUT = 60
ETOOMANYREFS = 59
ETXTBSY = 26

EUSERS = 68

EWOULDBLOCK = 35

EXDEV = 18

# no functions
# no classes
# variables with complex values

errorcode = {
    1: 'EPERM',
    2: 'ENOENT',
    3: 'ESRCH',
    4: 'EINTR',
    5: 'EIO',
    6: 'ENXIO',
    7: 'E2BIG',
    8: 'ENOEXEC',
    9: 'EBADF',
    10: 'ECHILD',
    11: 'EDEADLK',
    12: 'ENOMEM',
    13: 'EACCES',
    14: 'EFAULT',
    15: 'ENOTBLK',
    16: 'EBUSY',
    17: 'EEXIST',
    18: 'EXDEV',
    19: 'ENODEV',
    20: 'ENOTDIR',
    21: 'EISDIR',
    22: 'EINVAL',
    23: 'ENFILE',
    24: 'EMFILE',
    25: 'ENOTTY',
    26: 'ETXTBSY',
    27: 'EFBIG',
    28: 'ENOSPC',
    29: 'ESPIPE',
    30: 'EROFS',
    31: 'EMLINK',
    32: 'EPIPE',
    33: 'EDOM',
    34: 'ERANGE',
    35: 'EAGAIN',
    36: 'EINPROGRESS',
    37: 'EALREADY',
    38: 'ENOTSOCK',
    39: 'EDESTADDRREQ',
    40: 'EMSGSIZE',
    41: 'EPROTOTYPE',
    42: 'ENOPROTOOPT',
    43: 'EPROTONOSUPPORT',
    44: 'ESOCKTNOSUPPORT',
    45: 'ENOTSUP',
    46: 'EPFNOSUPPORT',
    47: 'EAFNOSUPPORT',
    48: 'EADDRINUSE',
    49: 'EADDRNOTAVAIL',
    50: 'ENETDOWN',
    51: 'ENETUNREACH',
    52: 'ENETRESET',
    53: 'ECONNABORTED',
    54: 'ECONNRESET',
    55: 'ENOBUFS',
    56: 'EISCONN',
    57: 'ENOTCONN',
    58: 'ESHUTDOWN',
    59: 'ETOOMANYREFS',
    60: 'ETIMEDOUT',
    61: 'ECONNREFUSED',
    62: 'ELOOP',
    63: 'ENAMETOOLONG',
    64: 'EHOSTDOWN',
    65: 'EHOSTUNREACH',
    66: 'ENOTEMPTY',
    67: 'EPROCLIM',
    68: 'EUSERS',
    69: 'EDQUOT',
    70: 'ESTALE',
    71: 'EREMOTE',
    72: 'EBADRPC',
    73: 'ERPCMISMATCH',
    74: 'EPROGUNAVAIL',
    75: 'EPROGMISMATCH',
    76: 'EPROCUNAVAIL',
    77: 'ENOLCK',
    78: 'ENOSYS',
    79: 'EFTYPE',
    80: 'EAUTH',
    81: 'ENEEDAUTH',
    82: 'EPWROFF',
    83: 'EDEVERR',
    84: 'EOVERFLOW',
    85: 'EBADEXEC',
    86: 'EBADARCH',
    87: 'ESHLIBVERS',
    88: 'EBADMACHO',
    89: 'ECANCELED',
    90: 'EIDRM',
    91: 'ENOMSG',
    92: 'EILSEQ',
    93: 'ENOATTR',
    94: 'EBADMSG',
    95: 'EMULTIHOP',
    96: 'ENODATA',
    97: 'ENOLINK',
    98: 'ENOSR',
    99: 'ENOSTR',
    100: 'EPROTO',
    101: 'ETIME',
    102: 'EOPNOTSUPP',
    103: 'ENOPOLICY',
    104: 'ENOTRECOVERABLE',
    105: 'EOWNERDEAD',
}

