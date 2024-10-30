import sys
sys.path.append(__file__.rsplit("\\tests")[0])
from typing import TYPE_CHECKING
from pymavlink import mavutil
from sitl import run_sitl

if TYPE_CHECKING:
    from pymavlink.mavutil import mavfile


def test_connection():
    run_sitl()
    conn: "mavfile" = mavutil.mavlink_connection('tcp:localhost:5760')
    assert conn is not None, "Expected a mavlink connection to be established, but found None"
