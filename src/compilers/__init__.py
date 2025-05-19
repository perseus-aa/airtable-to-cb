from pathlib import Path
import csv
import json
import models



def iiif_image_uri(image_id:str) -> str:
    return f"https://iiif.perseus.tufts.edu/iiif/3/{image_id}"

def thumbnail_url(image_id:str) -> str:
    return f"{iiif_image_uri(image_id)}/full/^450,/0/default.jpg"

def small_url(image_id:str) -> str:
    return f"{iiif_image_uri(image_id)}/full/^800,/0/default.jpg"


class ArtifactFactory():
    def __init__(self, airtable_artifacts_file:str) -> None:
        self.artifacts:list[models.Artifact] = []
        with open(airtable_artifacts_file, 'r', newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                obj_type: str = row['type']
                obj_class:type  = getattr(models, obj_type)
                self.artifacts.append(obj_class(**row))


class Db():
    def __init__(self) -> None:
        self.artifacts: dict[str,models.Artifact] = {}
        self.images: dict[str,models.Image] = {}
        self.image_idx = {}
        



    def load_artifacts(self, airtable_artifacts_file:str) -> None:
        with open(airtable_artifacts_file, 'r', newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                obj_type: str = row['type']
                obj_class:type  = getattr(models, obj_type)
                artifact: models.Artifact = obj_class(**row)
                self.artifacts[artifact.id] = artifact



    def load_images(self, images_file:str) -> None:
        with open(images_file, 'r', newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                image:models.Image = models.Image(**row)
                self.images[image.id] = image



    def load_data(self, artifacts_csv:str, images_csv:str) -> None:
        self.load_artifacts(artifacts_csv)
        self.load_images(images_csv)
        


    def artifact(self, id:str) -> models.Artifact | None:
        return self.artifacts.get(id)


    def image(self, id:str) -> models.Image | None:
        return self.images.get(id)



    def associated_images(self, artifact:models.Artifact) -> list[models.Image] | None:
        return [v for _,v in self.images.items() if v.represents == artifact.id]



class CollectionBuilder():
    def __init__(self, db:Db) -> None:
        self.db:Db = db
        self._objects: list[models.CBObject] = []

        
    @property
    def objects(self) -> list[models.CBObject]:
        if len(self._objects) == 0:
            for _, obj in self.db.artifacts.items():
                id:str = obj.id
                title:str = obj.name
                cobj: models.CompoundObject = models.CompoundObject(id=id, title=title, data=obj)
                self._objects.append(cobj)
                images: list[models.Image] | None = self.db.associated_images(obj)
                if images:
                    for i in images:
                        cb_child:models.ChildObject = models.ImageObject(id=i.id, title=title,
                                                                         parentid=cobj.objectid,
                                                                         data=i)
                        self._objects.append(cb_child)
                        
        return self._objects




class ImageTableCompiler():
    def __init__(self, json_file:Path) -> None:
        with open(json_file, 'r', encoding='utf-8') as f:
            self.json_data:list[dict[str,str]]= json.load(f)
        for object in self.json_data:
            object['uri'] = f"https://iiif.perseus.tufts.edu/iiif/3/{object['id']}"
            # object['thumbnail_url'] = f"{object['uri']}/full/pct:20/0/default.jpg"
            object['thumbnail_url'] = f"{object['uri']}/full/^200,/0/default.jpg"

    def to_csv(self, outfile:Path):
        fieldnames: list[str]  = list(self.json_data[0].keys())
        with open(outfile, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            writer.writerows(self.json_data)
            
    
    



class Compiler():
    def __init__(self, object_file:Path, image_file:Path) -> None:
        self.image_index:dict[str,Image] = {}
        with open(image_file, 'r', encoding='utf-8-sig') as f:
            for row in csv.DictReader(f):
                image = Image(**row)
                self.image_index[image.id] = image

            self.images:list[Image] = [Image(**row) for row in csv.DictReader(f)]






class VaseCompiler(Compiler):
    def __init__(self, object_file:Path, image_file:Path) -> None:
        super().__init__(object_file, image_file)
        self.object_index:dict[str,Vase] = {}
        with open(object_file, 'r', encoding='utf-8-sig') as f:
            for row in csv.DictReader(f):
                vase:Vase = Vase(**row)
                self.object_index[vase.id] = vase
                

                
        
image_json_file = Path('/Users/wulfmanc/gh/perseus-aa/json/images/images_with_ids.json')
afile = "/Users/wulfmanc/Downloads/av.csv"
ifile = "/Users/wulfmanc/Downloads/images-CollectionBuilder.csv"
