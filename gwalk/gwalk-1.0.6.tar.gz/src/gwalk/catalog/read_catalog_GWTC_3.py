#!/home/xevra/.local/bin/python3
'''\
Generate the likelihood function of each event
'''

######## Imports ########
import numpy as np
from gwalk.catalog.coordinates import m1m2_from_mc_eta, mc_eta_from_m1m2
from gwalk.catalog.coordinates import z_from_lum_dist_interp
from gwalk.catalog.coordinates import source_from_detector
from gwalk.catalog.coordinates import chieff_from_m1m2s1s2
from gwalk.catalog.coordinates import coord_labels
from gwalk.data import Database
from os.path import join, isfile

######## Functions ########
#### Database handling ####
def get_samples(
                fname_event,
                names,
                group = "PublicationSamples",
               ):
    '''Get the posterior samples we need
    Parameters
    ----------
    fname_event: str
        Input file name  for catalog samples
    names: list
        Input list of names to draw from catalog samples
    group: str
        Input kind of samples to work with
    '''

    # Check if file exists
    assert isfile(fname_event)

    # Initialize database
    db = Database(fname_event)
    # Check if group exists
    assert db.exists(group, kind="group")

    # check if data exists
    data_addr = join(group, "posterior_samples")
    assert db.exists(data_addr, kind="dset")

    # Get the fields
    fields = db.dset_fields(data_addr)

    # Create a dictionary
    pdict = {}
    
    # Load each item
    for item in names:
        # Make sure the item is correct
        if item in fields:
            # append values
            pdict[item] = db.dset_value(data_addr, field=item)

    return pdict

######## Algorithm ########

def generate_samples(fname_event, group, **kwargs):
    ''' A wrapper for finding the sample values that we need
    Parameters
    ----------
    fname_event: str
        Input file name  for catalog samples
    group: str
        Input kind of samples to work with
    '''

    names = list(coord_labels.keys())

    pdict = \
            get_samples(
                        fname_event,
                        names,
                        group=group,
                       )

    # Generate some things not given
    pdict["inv_lum_dist"] = np.power(pdict["luminosity_distance"],-1.)

    # Check on spin coordinates
    if not "chi_eff" in pdict:
        pdict["chi_eff"] = chieff_from_m1m2s1s2(
                                                pdict["mass_1_source"],
                                                pdict["mass_2_source"],
                                                pdict["a_1"],
                                                pdict["a_2"],
                                               )
    # Check aligned spin
    if not "spin_1z" in pdict:
        pdict["spin_1z"] = pdict["a_1"]*pdict["cos_tilt_1"]
    if not "spin_2z" in pdict:
        pdict["spin_2z"] = pdict["a_2"]*pdict["cos_tilt_2"]

    # check planar spin
    pdict["spin_1xy"] = pdict["a_1"]*np.power(1 - pdict["cos_tilt_1"]**2, 0.5)
    pdict["spin_2xy"] = pdict["a_2"]*np.power(1 - pdict["cos_tilt_2"]**2, 0.5)

    return pdict
