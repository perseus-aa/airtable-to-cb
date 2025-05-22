import csv

IMAGE_SERVER: str = "http://iiif.perseus.tufts.edu/iiif/3"


class Row:
    def __init__(self, **data):
        self.data = data


    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def images(self):
        return self.data.get("images")

    @property
    def objectid(self) -> str:
        return self.id

    @property
    def parentid(self) -> str | None:
        return None


class ArtifactRow(Row):
    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.data["objectid"] = self.data["id"]
        self.data["object_location"] = self.object_location
        self.data["image_small"] = self.image_small
        self.data["image_thumb"] = self.image_thumb
        self.data["display_template"] = self.display_template
        self.data["format"] = self.format
        self.data["objtype"] = self.data.get("type")
        self.data["type"] = self.type
        if self.data["title"] == "":
            self.data["title"] = self.data["name"]

    @property
    def icon_id(self) -> str | None:
        if self.images:
            return self.images.split(",")[0]

    @property
    def object_location(self) -> str | None:
        location = None
        if self.icon_id:
            location = f"{IMAGE_SERVER}/{self.icon_id}/full/max/0/default.jpg"
        return location

    @property
    def image_small(self) -> str | None:
        location = None
        if self.icon_id:
            location = f"{IMAGE_SERVER}/{self.icon_id}/full/^800,/0/default.jpg"
        return location

    @property
    def image_thumb(self) -> str | None:
        location = None
        if self.icon_id:
            location = f"{IMAGE_SERVER}/{self.icon_id}/full/^450,/0/default.jpg"
        return location

    @property
    def display_template(self) -> str:
        return "compound_object"

    @property
    def format(self) -> str:
        return "compound_object"

    @property
    def type(self) -> str:
        return "record"


class ImageRow(Row):
    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.data['objectid'] = f"i{self.data['id'].replace('.', '')}"
        self.data["parentid"] = self.data["represents"]
        self.data["object_location"] = self.object_location
        self.data["image_small"] = self.image_small
        self.data["image_thumb"] = self.image_thumb
        self.data["display_template"] = self.display_template
        self.data["format"] = self.format
        self.data["type"] = self.type
        self.data['title'] = self.data['caption']

        # del self.data["represents"]
        # del self.data["credits"]
        # del self.data["uri"]
        # del self.data["caption"]
        del self.data["thumbnail_url"]

    @property
    def parentid(self) -> str:
        return self.data["represents"]

    @property
    def object_location(self) -> str:
        return f"{IMAGE_SERVER}/{self.id}/full/max/0/default.jpg"

    @property
    def image_small(self) -> str:
        return f"{IMAGE_SERVER}/{self.id}/full/^800,/0/default.jpg"

    @property
    def image_thumb(self) -> str:
        return f"{IMAGE_SERVER}/{self.id}/full/^450,/0/default.jpg"

    @property
    def display_template(self) -> str:
        return "image"

    @property
    def format(self) -> str:
        return "image/jpeg"

    @property
    def type(self) -> str:
        return "Image;StillImage"


class CBTable:
    fieldnames = [
        "id",
        "objectid",
        "parentid",
        "title",
        "display_template",
        "format",
        "type",
        "object_location",
        "image_small",
        "image_thumb",
        "credits",
        "caption",
        "represents",
        "uri",
        "accession_number",
        "actual_weight",
        "architect",
        "architect_evidence",
        "architectural_order",
        "assoc_building",
        "attributed_by",
        "beazley_number",
        "building_type",
        "category",
        "ceramic_phase",
        "collection",
        "collection_history",
        "commentary",
        "comparanda",
        "condit",
        "condition_description",
        "context",
        "context_mod",
        "culture",
        "date_description",
        "date_for_sort",
        "decoration_description",
        "denomination",
        "description",
        "die_axis",
        "dimensions",
        "documentary_references",
        "donor",
        "end_date",
        "end_mod",
        "entered_by",
        "essay_number",
        "essay_text",
        "exploration",
        "extent",
        "findspot",
        "findspot_mod",
        "form_style_description",
        "graffiti",
        "history",
        "human_name",
        "image",
        "images",
        "in_group",
        "in_whole",
        "inscription",
        "inscription_bibliography",
        "inscriptions",
        "issuing_authority",
        "location",
        "material",
        "material_description",
        "name",
        "object_function",
        "obverse_legend",
        "obverse_type",
        "original",
        "original_or_copy",
        "other_bibliography",
        "other_notes",
        "painter",
        "painter_mod",
        "period",
        "period_for_sort",
        "periods",
        "perseus_version",
        "physical",
        "placement",
        "plan",
        "potter",
        "potter_mod",
        "primary_citation",
        "region",
        "relief",
        "reverse_legend",
        "reverse_type",
        "scale",
        "scale_for_sort",
        "sculptor",
        "sculptor_mod",
        "sculpture_type",
        "see_also",
        "shape",
        "shape_description",
        "site_type",
        "sources_used",
        "start_date",
        "start_mod",
        "style",
        "subject_description",
        "summary",
        "technique",
        "technique_description",
        "objtype",
        "unitary_date",
        "unitary_mod",
        "ware",
    ]

    def __init__(self, artifacts_file, images_file):
        self.image_idx = {}
        self.artifact_idx = {}

        with open(images_file, "r", newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for record in reader:
                row = ImageRow(**record)
                self.image_idx[row.id] = row

        with open(artifacts_file, "r", newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for record in reader:
                row = ArtifactRow(**record)
                self.artifact_idx[row.id] = row

    def dump(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for _, artifact in self.artifact_idx.items():
                writer.writerow(artifact.data)
            for _, image in self.image_idx.items():
                writer.writerow(image.data)


ifile = "/Users/wulfmanc/Downloads/images-CollectionBuilder.csv"
afile = "/Users/wulfmanc/Downloads/artifacts-CollectionBuilder.csv"
