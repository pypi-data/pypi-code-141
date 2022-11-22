"""Definition for different licenses."""
from __future__ import annotations

from enum import Enum


class LicenseType(str, Enum):
    """License types available in this tool."""

    no_license = "no-license"
    no_redistribution = "no-redistribution"
    afl_3_0 = "afl-3.0"
    agpl_3_0 = "agpl-3.0"
    apache_2_0 = "apache-2.0"
    artistic_2_0 = "artistic-2.0"
    bigscience_bloom_rail_1_0 = "bigscience-bloom-rail-1.0"
    bigscience_openrail_m = "bigscience-openrail-m"
    bsd = "bsd"
    bsd_2_clause = "bsd-2-clause"
    bsd_3_clause = "bsd-3-clause"
    bsd_3_clause_clear = "bsd-3-clause-clear"
    bsl_1_0 = "bsl-1.0"
    c_uda = "c-uda"
    cc = "cc"
    cc_by_1_0 = "cc-by-1-0"
    cc_by_2_0 = "cc-by-2.0"
    cc_by_2_5 = "cc-by-2.5"
    cc_by_3_0 = "cc-by-3.0"
    cc_by_4_0 = "cc-by-4.0"
    cc_by_nc_2_0 = "cc-by-nc-2.0"
    cc_by_nc_3_0 = "cc-by-nc-3.0"
    cc_by_nc_4_0 = "cc-by-nc-4.0"
    cc_by_nc_nd_4_0 = "cc-by-nc-nd-4.0"
    cc_by_nc_sa = "cc-by-nc-sa"
    cc_by_nc_sa_2_0 = "cc-by-nc-sa-2.0"
    cc_by_nc_sa_3_0 = "cc-by-nc-sa-3.0"
    cc_by_nc_sa_4_0 = "cc-by-nc-sa-4.0"
    cc_by_nd_4_0 = "cc-by-nd-4.0"
    cc_by_sa_3_0 = "cc-by-sa-3.0"
    cc_by_sa_4_0 = "cc-by-sa-4.0"
    cc_by_sa = "cc-by-sa"
    cc0_1_0 = "cc0-1.0"
    creativeml_openrail_m = "creativeml-openrail-m"
    ecl_2_0 = "ecl-2.0"
    eupl_1_1 = "eupl-1.1"
    gfdl = "gfdl"
    gpl = "gpl"
    gpl_2_0 = "gpl-2.0"
    gpl_3_0 = "gpl-3.0"
    isc = "isc"
    lgpl = "lgpl"
    lgpl_2_1 = "lgpl-2.1"
    lgpl_3_0 = "lgpl-3.0"
    lgpl_lr = "lgpl-lr"
    mit = "mit"
    mpl_2_0 = "mpl-2.0"
    ms_pl = "ms-pl"
    odbl = "odbl"
    odc_by = "odc-by"
    openrail = "openrail"
    other = "other"
    pddl = "pddl"
    postgresql = "postgresql"
    unlicense = "unlicense"
    wtfpl = "wtfpl"
    zlib = "zlib"

    @staticmethod
    def list() -> list[str]:
        """Obtains string representations of all values.

        Returns:
            List of all values in str.
        """
        return list(map(lambda c: c.value, LicenseType))
