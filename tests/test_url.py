from translate_bookmark.url import Url, Domain


def test_get_domain():
    domain: Domain = Url.get_domain(
        'https://www.packers.com/news/packers-lb-ty-summers-far-from-satisfied-with-defensive-debut')
    assert domain == Domain.PACKERSCOM
