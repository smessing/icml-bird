"""
names.py - Everything related to translating between species, locations and
           times of different formats.
"""
SPECIES = {
  1: 'aegithalos_caudatus',
  2: 'alauda_arvensis',
  3: 'anthus_trivialis',
  4: 'branta_canadensis',
  5: 'carduelis_chloris',
  6: 'certhia_brachydactyla',
  7: 'columba_palumbus',
  8: 'corvus_corone',
  9: 'cuculus_canorus',
 10: 'dendrocopos_major',
 11: 'emberiza_citrinella',
 12: 'erithacus_rubecula',
 13: 'fringilla_coelebs',
 14: 'garrulus_glandarius',
 15: 'luscinia_megarhynchos',
 16: 'motacilla_alba',
 17: 'oriolus_oriolus',
 18: 'parus_caeruleus',
 19: 'parus_major',
 20: 'parus_palustris',
 21: 'pavo_cristatus',
 22: 'phasianus_colchicus',
 23: 'phoenicurus_phoenicurus',
 24: 'phylloscopus_collybita',
 25: 'picus_viridis',
 26: 'prunella_modularis',
 27: 'sitta_europaea',
 28: 'streptopelia_decaocto',
 29: 'strix_aluco',
 30: 'sturnus_vulgaris',
 31: 'sylvia_atricapilla',
 32: 'troglodytes_troglodytes',
 33: 'turdus_merula',
 34: 'turdus_philomelos',
 35: 'turdus_viscivorus',
 36: 'NO_SPECIES'
}

SPECIES_INV = {
  'aegithalos_caudatus': 1,
  'alauda_arvensis': 2,
  'anthus_trivialis': 3,
  'branta_canadensis': 4,
  'carduelis_chloris': 5,
  'certhia_brachydactyla': 6,
  'columba_palumbus': 7,
  'corvus_corone': 8,
  'cuculus_canorus': 9,
  'dendrocopos_major': 10,
  'emberiza_citrinella': 11,
  'erithacus_rubecula': 12,
  'fringilla_coelebs': 13,
  'garrulus_glandarius': 14,
  'luscinia_megarhynchos': 15,
  'motacilla_alba': 16,
  'oriolus_oriolus': 17,
  'parus_caeruleus': 18,
  'parus_major': 19,
  'parus_palustris': 20,
  'pavo_cristatus': 21,
  'phasianus_colchicus': 22,
  'phoenicurus_phoenicurus': 23,
  'phylloscopus_collybita': 24,
  'picus_viridis': 25,
  'prunella_modularis': 26,
  'sitta_europaea': 27,
  'streptopelia_decaocto': 28,
  'strix_aluco': 29,
  'sturnus_vulgaris': 30,
  'sylvia_atricapilla': 31,
  'troglodytes_troglodytes': 32,
  'turdus_merula': 33,
  'turdus_philomelos': 34,
  'turdus_viscivorus': 35,
  'NO_SPECIES': 36
}

NO_SPECIES = 'NO_SPECIES'
NO_SPECIES_KEY = 36


def get_species_list():
  """
    Get a list of the species we'll try to identify.
  """
  # chomp off the NO_SPECIES label.
  return SPECIES.values()[:-1]


def get_index_to_species_map():
  """
    Get a map of index -> species_name, where index is the numerical code
    representing the given species.
  """
  return SPECIES


def get_species_for_index(index):
  """
    Get the corresponding species name for a given species index.
  """
  return SPECIES[index]


def get_index_for_species(species):
  """
    Get the corresponding index for the given species.
  """
  return SPECIES_INV[species]


def get_species_to_index_map():
  """
    Get a map of species_name -> index. Where index is the numerical
    code representing the given species.
  """
  return SPECIES_INV


TESTING_TIMES = [
  '20090324_063100',
  '20090326_062700',
  '20090328_062300',
  '20090330_061800',
  '20090401_061400',
  '20090403_061000',
  '20090405_060600',
  '20090407_060200',
  '20090409_055800',
  '20090411_055400',
  '20090413_055000',
  '20090415_054600',
  '20090417_054200',
  '20090419_053900',
  '20090421_053500',
  '20090423_053100',
  '20090425_052800',
  '20090427_052400',
  '20090429_052100',
  '20090501_051700',
  '20090503_051400',
  '20090505_051100',
  '20090507_050800',
  '20090509_050500',
  '20090511_050200',
  '20090513_045900',
  '20090515_045600',
  '20090517_045400',
  '20090520_045000',
  '20090522_044800'
]


def get_testing_times():
  """
    Get a list of the times corresponding to all test recordings.
  """
  return TESTING_TIMES


TESTING_LOCATIONS = ['A', 'B', 'C']


def get_testing_locations():
  """
    Get a list of the locations for all test recordings.
  """
  return TESTING_LOCATIONS
