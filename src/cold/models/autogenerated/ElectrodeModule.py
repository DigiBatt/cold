
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .ElectrochemicalConstituentModule import ElectrochemicalConstituent





from .BinderModule import Binder



from .ConstituentModule import Constituent



from .ActiveMaterialModule import ActiveMaterial



from .CoatingModule import Coating



from .CurrentCollectorModule import CurrentCollector





class Electrode(Whole, ElectrochemicalConstituent):
    """
    Class representing the `Electrode` entity, which inherits from:
    - Whole, ElectrochemicalConstituent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f007072_a8dd_4798_b865_1bf9363be627'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electrode'`
        - **Alias**: `class_name`
    
    - `hasBinder` (`Optional[Binder]`): 
        - **Default Value**: `None`
        - **Alias**: `hasBinder`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `hasActiveMaterial` (`Optional[ActiveMaterial]`): 
        - **Default Value**: `None`
        - **Alias**: `hasActiveMaterial`
    
    - `contacts` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `contacts`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `hasCoating` (`Optional[Coating]`): 
        - **Default Value**: `None`
        - **Alias**: `hasCoating`
    
    - `hasCurrentCollector` (`Optional[CurrentCollector]`): 
        - **Default Value**: `None`
        - **Alias**: `hasCurrentCollector`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Electrode(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f007072_a8dd_4798_b865_1bf9363be627',
    
    class_name='Electrode',
    
    hasBinder="example_value",
    
    hasConstituent="example_value",
    
    wikidataReference="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    IEVReference="example_value",
    
    hasActiveMaterial="example_value",
    
    contacts="example_value",
    
    wikipediaReference="example_value",
    
    hasCoating=None,
    
    hasCurrentCollector=None,
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f007072_a8dd_4798_b865_1bf9363be627',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electrode',
        alias="class_name"
    )
    
    hasBinder: Optional[Binder] = Field(
        None,
        alias="hasBinder"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    hasActiveMaterial: Optional[ActiveMaterial] = Field(
        None,
        alias="hasActiveMaterial"
    )
    
    contacts: Optional[str] = Field(
        None,
        alias="contacts"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    
    hasCoating: Optional[Coating] = Field(
        None,
        alias="hasCoating"
    )
    
    hasCurrentCollector: Optional[CurrentCollector] = Field(
        None,
        alias="hasCurrentCollector"
    )
    

    
    @validator("hasBinder", pre=True, always=True)
    def validate_hasBinder(cls, value):
        if value is not None and not isinstance(value, Binder):
            raise ValueError(f"Field 'hasBinder' must be an instance of 'Binder' or its subclass.")
        return value
    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    @validator("hasActiveMaterial", pre=True, always=True)
    def validate_hasActiveMaterial(cls, value):
        if value is not None and not isinstance(value, ActiveMaterial):
            raise ValueError(f"Field 'hasActiveMaterial' must be an instance of 'ActiveMaterial' or its subclass.")
        return value
    
    @validator("hasCoating", pre=True, always=True)
    def validate_hasCoating(cls, value):
        if value is not None and not isinstance(value, Coating):
            raise ValueError(f"Field 'hasCoating' must be an instance of 'Coating' or its subclass.")
        return value
    
    @validator("hasCurrentCollector", pre=True, always=True)
    def validate_hasCurrentCollector(cls, value):
        if value is not None and not isinstance(value, CurrentCollector):
            raise ValueError(f"Field 'hasCurrentCollector' must be an instance of 'CurrentCollector' or its subclass.")
        return value
    
    

    

    