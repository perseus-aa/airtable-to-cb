from csv import DictReader
from models import Vase, Image

def test_vase_model(shared_datadir):
    with open(shared_datadir / "vases1.csv", 'r', encoding='utf-8-sig') as f:
        reader = DictReader(f)
        vases = []
        for row in reader:
            vases.append(Vase(**row))

    assert len(vases) == 19
    assert vases[0].id == 'aa_3951'


def test_image_model(shared_datadir):
    with open(shared_datadir / "images1.csv", "r", encoding="utf-8-sig") as f:
        images = []
        for row in DictReader(f):
            images.append(Image(**row))

    assert images[0].id == '1990.05.0140'
