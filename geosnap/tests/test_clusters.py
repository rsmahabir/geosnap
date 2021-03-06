from geosnap import Community, io

reno = Community.from_census(msa_fips="39900")
columns = ["median_household_income", "p_poverty_rate", "p_unemployment_rate"]

# Aspatial Clusters


def test_gm():

    r = reno.cluster(columns=columns, method="gaussian_mixture", best_model=True)
    assert len(r.gdf.gaussian_mixture.unique()) >= 5


def test_ward():
    io.store_census()
    r = reno.cluster(columns=columns, method="ward")
    assert len(r.gdf.ward.unique()) == 7


def test_spectral():

    r = reno.cluster(columns=columns, method="spectral")
    assert len(r.gdf.spectral.unique()) == 7


def test_kmeans():

    r = reno.cluster(columns=columns, method="kmeans")
    assert len(r.gdf.kmeans.unique()) == 7


def test_aff_prop():

    r = reno.cluster(columns=columns, method="affinity_propagation", preference=-100)
    assert len(r.gdf.affinity_propagation.unique()) == 3


def test_hdbscan():

    r = reno.cluster(columns=columns, method="hdbscan")
    assert len(r.gdf.hdbscan.unique()) >= 4


# Spatial Clusters


def test_spenc():

    r = reno.cluster_spatial(columns=columns, method="spenc")
    assert len(r.gdf.spenc.unique()) == 7


def test_maxp():

    r = reno.cluster_spatial(columns=columns, method="max_p", initial=10)
    assert len(r.gdf.max_p.unique()) >= 8


def test_ward_spatial():

    r = reno.cluster_spatial(columns=columns, method="ward_spatial", n_clusters=7)
    assert len(r.gdf.ward_spatial.unique()) == 8


def test_skater():

    r = reno.cluster_spatial(columns=columns, method="skater", n_clusters=10)
    assert len(r.gdf.skater.unique()) == 11


def test_azp():
    r = reno.cluster_spatial(columns=columns, method="azp", n_clusters=7)
    assert len(r.gdf.azp.unique()) == 8
