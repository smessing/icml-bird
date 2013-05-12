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
 35: 'turdus_viscivorus'
}

def get_species_list():
  return SPECIES.values()

def get_index_to_species_map():
  return SPECIES
