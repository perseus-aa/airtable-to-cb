from pydantic import BaseModel, computed_field

class Image(BaseModel):
    id: str
    represents: str
    caption: str | None = None
    credit: str | None = None
    


class Artifact(BaseModel):
    id: str
    name: str
    imageObjects: list[Image] | None = []
    images: str | list[str] | None = []

    class Config:
        extra = "ignore"  # Ignore extra fields instead of raising error


class Vase(Artifact):
    summary: str | None = None
    collection: str | None = None
    ware: str | None = None
    ceramic_phase: str | None = None
    shape: str | None = None
    shape_description: str | None = None
    potter_mod: str | None = None
    potter: str | None = None
    context_mod: str | None = None
    context: str | None = None
    painter_mod: str | None = None
    painter: str | None = None
    inscriptions: str | None = None
    dimensions: str | None = None
    beazley_number: str | None = None
    unitary_mod: str | None = None
    unitary_date: str | None = None
    date_for_sort: str | None = None
    attributed_by: str | None = None
    period_for_sort: str | None = None
    start_mod: str | None = None
    start_date: str | None = None
    comparanda: str | None = None
    collection_history: str | None = None
    end_mod: str | None = None
    end_date: str | None = None
    date_description: str | None = None
    period: str | None = None
    region: str | None = None
    graffiti: str | None = None
    material_description: str | None = None
    relief: str | None = None
    condit: str | None = None
    accession_number: str | None = None
    perseus_version: str | None = None
    entered_by: str | None = None

    

class Building(Artifact):
    architect: str | None = None
    architect_evidence: str | None = None
    architectural_order: str | None = None
    building_type: str | None = None
    context: str | None = None
    date_description: str | None = None
    date_for_sort: str | None = None
    dimensions: str | None = None
    documentary_references: str | None = None
    end_date: str | None = None
    end_mod: str | None = None
    entered_by: str | None = None
    history: str | None = None
    image: str | None = None
    location: str | None = None
    other_bibliography: str | None = None
    other_notes: str | None = None
    period: str | None = None
    period_for_sort: str | None = None
    "perseus_version"
    plan: str | None = None
    region: str | None = None
    see_also: str | None = None
    sources_used: str | None = None
    start_date: str | None = None
    start_mod: str | None = None
    summary: str | None = None
    type: str | None = None
    unitary_date: str | None = None
    unitary_mod: str | None = None
     

class Coin(Artifact):
    actual_weight: str | None = None
    collection: str | None = None
    collection_history: str | None = None
    commentary: str | None = None
    comparanda: str | None = None
    context: str | None = None
    date_description: str | None = None
    date_for_sort: str | None = None
    denomination: str | None = None
    die_axis: str | None = None
    dimensions: str | None = None
    donor: str | None = None
    end_date: str | None = None
    end_mod: str | None = None
    entered_by: str | None = None
    image: str | None = None
    issuing_authority: str | None = None
    location: str | None = None
    material: str | None = None
    obverse_legend: str | None = None
    obverse_type: str | None = None
    period: str | None = None
    period_for_sort: str | None = None
    perseus_version: str | None = None
    region: str | None = None
    reverse_legend: str | None = None
    reverse_type: str | None = None
    sources_used: str | None = None
    start_date: str | None = None
    start_mod: str | None = None
    type: str | None = None
    unitary_date: str | None = None
    unitary_mod: str | None = None


class Gem(Artifact):
    collection: str | None = None
    culture: str | None = None
    dimensions: str | None = None
    donor: str | None = None
    end_date: str | None = None
    end_mod: str | None = None
    entered_by: str | None = None
    image: str | None = None
    location: str | None = None
    material: str | None = None
    material_description: str | None = None
    period: str | None = None
    perseus_version: str | None = None
    sculpture_type: str | None = None
    sources_used: str | None = None
    start_date: str | None = None
    start_mod: str | None = None
    style: str | None = None
    summary: str | None = None
    type: str | None = None
    unitary_date: str | None = None
    unitary_mod: str | None = None


class Sculpture(Artifact):
    accession_number: str | None = None
    assoc_building: str | None = None
    category: str | None = None
    collection: str | None = None
    collection_history: str | None = None
    comparanda: str | None = None
    condit: str | None = None
    condition_description: str | None = None
    context: str | None = None
    context_mod: str | None = None
    date_description: str | None = None
    date_for_sort: str | None = None
    dimensions: str | None = None
    documentary_references: str | None = None
    end_date: str | None = None
    end_mod: str | None = None
    entered_by: str | None = None
    findspot: str | None = None
    findspot_mod: str | None = None
    form_style_description: str | None = None
    graffiti: str | None = None
    image: str | None = None
    in_group: str | None = None
    in_whole: str | None = None
    inscription: str | None = None
    "inscription_bibliography"
    location: str | None = None
    material: str | None = None
    material_description: str | None = None
    object_function: str | None = None
    original: str | None = None
    original_or_copy: str | None = None
    other_bibliography: str | None = None
    other_notes: str | None = None
    period: str | None = None
    period_for_sort: str | None = None

    placement: str | None = None
    primary_citation: str | None = None
    region: str | None = None
    scale: str | None = None
    sculptor: str | None = None
    sculptor_mod: str | None = None
    sculpture_type: str | None = None
    sources_used: str | None = None
    start_date: str | None = None
    start_mod: str | None = None
    style: str | None = None
    subject_description: str | None = None
    summary: str | None = None
    technique: str | None = None
    technique_description: str | None = None
    title: str | None = None
    type: str | None = None
    unitary_date: str | None = None
    unitary_mod: str | None = None


class Site(Artifact):
    description: str | None = None
    documentary_references: str | None = None
    entered_by: str | None = None
    exploration: str | None = None
    image: str | None
    location: str | None = None
    other_bibliography: str | None = None
    periods: str | None = None
    perseus_version: str | None = None
    physical: str | None = None
    region: str | None = None
    site_type: str | None = None
    sources_used: str | None = None
    summary: str | None = None
    type: str | None = None


IMAGE_SERVER:str = "http://iiif.perseus.tufts.edu/iiif/3"
    

class CBObject(BaseModel):
    id: str
    title: str = "Untitled"

    @computed_field
    @property
    def objectid(self) -> str:
        return f"id_{self.id}"


class CompoundObject(CBObject):
    parentid: str | None = None
    data: Artifact | None = None
    display_template: str = "compound_object"
    format:str = "compound_object"
    type:str = "record"


class ChildObject(CBObject):
    parentid: str
    data:Image | None = None


class ImageObject(ChildObject):
    display_template:str = "image"
    format:str = "image/jpeg"
    type:str = "Image;StillImage"

    @computed_field
    @property
    def object_location(self) -> str:
        return f"{IMAGE_SERVER}/{self.objectid}/full/max/0/default.jpg"

    @computed_field
    @property
    def image_small(self) -> str:
        return f"{IMAGE_SERVER}/{self.objectid}/full/^800,/0/default.jpg"

    @computed_field
    @property
    def image_thumb(self) -> str:
        return f"{IMAGE_SERVER}/{self.objectid}/full/^450,/0/default.jpg"



class CBRecordAll(BaseModel):

    id: str | None = None
    name: str | None = None
    collection: str | None = None
    accession_number: str | None = None
    actual_weight: str | None = None
    architect: str | None = None
    architect_evidence: str | None = None
    architectural_order: str | None = None
    assoc_building: str | None = None
    attributed_by: str | None = None
    beazley_number: str | None = None
    building_type: str | None = None
    category: str | None = None
    ceramic_phase: str | None = None
    collection_history: str | None = None
    commentary: str | None = None
    comparanda: str | None = None
    condit: str | None = None
    context_mod: str | None = None
    condition_description: str | None = None
    context: str | None = None
    culture: str | None = None
    date_description: str | None = None
    date_for_sort: str | None = None
    decoration_description: str | None = None
    denomination: str | None = None
    description: str | None = None
    die_axis: str | None = None
    dimensions: str | None = None
    end_mod: str | None = None
    documentary_references: str | None = None
    donor: str | None = None
    end_date: str | None = None
    entered_by: str | None = None
    essay_number: str | None = None
    essay_text: str | None = None
    exploration: str | None = None
    extent: str | None = None
    findspot: str | None = None
    findspot_mod: str | None = None
    form_style_description: str | None = None
    graffiti: str | None = None
    history: str | None = None
    human_name: str | None = None
    image: str | None = None
    in_group: str | None = None
    in_whole: str | None = None
    inscription: str | None = None
    inscription_bibliography: str | None = None
    inscriptions: str | None = None
    issuing_authority: str | None = None
    location: str | None = None
    material: str | None = None
    material_description: str | None = None
    object_function: str | None = None
    obverse_legend: str | None = None
    obverse_type: str | None = None
    original: str | None = None
    original_or_copy: str | None = None
    other_bibliography: str | None = None
    painter_mod: str | None = None
    other_notes: str | None = None
    painter: str | None = None
    period: str | None = None
    period_for_sort: str | None = None
    potter_mod: str | None = None
    periods: str | None = None
    perseus_version: str | None = None
    physical: str | None = None
    placement: str | None = None
    plan: str | None = None
    potter: str | None = None
    primary_citation: str | None = None
    region: str | None = None
    relief: str | None = None
    reverse_legend: str | None = None
    reverse_type: str | None = None
    scale: str | None = None
    scale_for_sort: str | None = None
    sculptor: str | None = None
    sculptor_mod: str | None = None
    sculpture_type: str | None = None
    see_also: str | None = None
    shape: str | None = None
    shape_description: str | None = None
    site_type: str | None = None
    sources_used: str | None = None
    start_date: str | None = None
    start_mod: str | None = None
    style: str | None = None
    subject_description: str | None = None
    summary: str | None = None
    technique: str | None = None
    technique_description: str | None = None
    title: str | None = None
    type: str | None = None
    unitary_mod: str | None = None
    unitary_date: str | None = None
    ware: str | None = None
    images: str | None = None
